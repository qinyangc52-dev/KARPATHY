#!/usr/bin/env python3
"""
Extract conservative concept candidates from raw inputs and wiki pages.

The script does not create concept pages. It writes a reviewable candidate
manifest under raw/extracted/concepts/ so concepts can be promoted deliberately.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable

try:
    import yaml
except ImportError:  # pragma: no cover - handled at runtime
    yaml = None


REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIRS = [
    REPO_ROOT / "raw" / "articles",
    REPO_ROOT / "raw" / "papers",
    REPO_ROOT / "raw" / "books",
    REPO_ROOT / "raw" / "transcripts",
    REPO_ROOT / "raw" / "notes" / "curated",
    REPO_ROOT / "raw" / "notes" / "fleeting",
]
WIKI_DIRS = [
    REPO_ROOT / "wiki" / "sources",
    REPO_ROOT / "wiki" / "entities",
    REPO_ROOT / "wiki" / "topics",
    REPO_ROOT / "wiki" / "comparisons",
    REPO_ROOT / "wiki" / "synthesis",
]
DEFAULT_OUTPUT = REPO_ROOT / "raw" / "extracted" / "concepts" / "candidates.json"
REGISTRY = REPO_ROOT / "wiki" / "concepts" / "_registry.yml"

STOPWORDS = {
    "readme",
    "python",
    "pytorch",
    "numpy",
    "scipy",
    "yaml",
    "json",
    "markdown",
    "source",
    "wiki",
    "llm",
    "curated note",
    "literature note",
    "source supported",
    "source-supported",
    "background knowledge",
    "background-knowledge",
    "needs verification",
    "needs-verification",
    "inferred",
    "标题",
    "作者",
    "版本",
    "步骤",
    "方法",
    "输入",
    "数量",
    "包含",
    "不包含",
    "上游问题",
    "下游问题",
    "证据边界",
    "抽取状态",
    "说明模型",
    "e-i",
    "epoch-level",
}
ENTITY_HINTS = {
    "spsnet",
    "sleep-edf",
    "brainpy",
    "pytorch",
    "mnist",
    "rtx",
    "eeg ",
    "eog ",
    "graphblock-lite",
    "graph-like-fc",
    "fc baseline",
    "project",
    "software",
    "dataset",
    "code",
    "repo",
    "repository",
    "implementation",
    "复现",
    "项目",
    "工程",
    "软件",
    "数据集",
    "代码",
}
TOPIC_HINTS = {"研究方向", "问题域", "路线", "应用"}
CHINESE_SUFFIXES = (
    "模型",
    "机制",
    "方法",
    "理论",
    "原则",
    "架构",
    "网络",
    "表征",
    "编码",
    "分类",
    "同步",
    "临界态",
    "平衡",
    "异质性",
)
SLUG_ALIASES = {
    "速率编码": "rate-coding",
    "临界态": "critical-state",
    "临界同步": "critical-synchronization",
    "全脑建模": "whole-brain-modeling",
    "睡眠分期": "sleep-stage-classification",
    "多导睡眠监测": "polysomnography",
    "脉冲神经网络": "spiking-neural-network",
    "图神经网络": "graph-neural-network",
    "抑制异质性": "inhibitory-heterogeneity",
    "结构功能耦合": "structure-function-coupling",
}


@dataclass
class Candidate:
    raw_name: str
    normalized_name: str
    slug: str
    source_files: set[str] = field(default_factory=set)
    contexts: list[str] = field(default_factory=list)
    evidence_count: int = 0
    suggested_type: str = "concept_candidate"
    decision: str = "candidate"
    aliases: set[str] = field(default_factory=set)


def read_text(path: Path) -> str:
    for encoding in ("utf-8", "utf-8-sig", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def parse_frontmatter(text: str) -> dict:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, flags=re.DOTALL)
    if not match or yaml is None:
        return {}
    data = yaml.safe_load(match.group(1))
    return data if isinstance(data, dict) else {}


def strip_frontmatter(text: str) -> str:
    return re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)


def iter_sources(paths: Iterable[Path]) -> Iterable[Path]:
    for base in paths:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if path.is_file() and path.suffix.lower() in {".md", ".txt"}:
                if "__pycache__" not in path.parts:
                    yield path


def normalize_name(name: str) -> str:
    name = unicodedata.normalize("NFKC", name)
    name = re.sub(r"\s+", " ", name.strip(" -*_`：:;，。,.()[]{}<>"))
    return name


def slugify(name: str) -> str:
    normalized = normalize_name(name)
    if normalized in SLUG_ALIASES:
        return SLUG_ALIASES[normalized]
    value = normalized.lower()
    value = value.replace("_", "-").replace(" ", "-")
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff-]+", "", value)
    value = re.sub(r"-+", "-", value).strip("-")
    if value and value.isascii():
        return value
    if value and re.search(r"[\u4e00-\u9fff]", value):
        digest = hashlib.sha1(normalized.encode("utf-8")).hexdigest()[:8]
        return f"concept-{digest}"
    return value or "concept"


def title_from_tag(tag: str) -> str:
    return normalize_name(tag.replace("-", " ").replace("_", " "))


def context_for(text: str, term: str, limit: int = 160) -> str:
    idx = text.lower().find(term.lower())
    if idx < 0:
        return ""
    start = max(0, idx - limit // 2)
    end = min(len(text), idx + len(term) + limit // 2)
    return re.sub(r"\s+", " ", text[start:end]).strip()


def load_registry_aliases(path: Path) -> dict[str, str]:
    if not path.exists() or yaml is None:
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    aliases: dict[str, str] = {}
    for slug, item in (data.get("concepts") or {}).items():
        aliases[slug.lower()] = slug
        aliases[str(item.get("title", slug)).lower()] = slug
        for alias in item.get("aliases") or []:
            aliases[str(alias).lower()] = slug
    return aliases


def is_candidate_name(name: str) -> bool:
    lower = name.lower()
    if len(name) < 2 or len(name) > 60:
        return False
    if lower in STOPWORDS:
        return False
    if lower.startswith(("a ", "an ", "the ", "this ", "that ")):
        return False
    if lower.endswith((" with", " of", " and", " or", " the")):
        return False
    if " et al" in lower:
        return False
    if re.search(r"\bq\d+\b", lower):
        return False
    if re.fullmatch(r"(figure|stage|python|pytorch)\s+\d+", lower):
        return False
    if re.search(r"[|/]{2,}", name):
        return False
    if re.fullmatch(r"\d+", name):
        return False
    if name.startswith("[[") or "{{" in name:
        return False
    return True


def suggested_type(name: str) -> str:
    lower = name.lower()
    if any(hint in lower or hint in name for hint in ENTITY_HINTS):
        return "entity_candidate"
    if re.fullmatch(r"[A-Z][a-z]+(?:-[A-Z][a-z]+)? [A-Z][a-z]+", name):
        concept_words = ("coding", "encoding", "model", "network", "process", "coupling", "synchronization")
        if not any(word in lower for word in concept_words):
            return "entity_candidate"
    if any(hint in name for hint in TOPIC_HINTS):
        return "topic_candidate"
    return "concept_candidate"


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract concept candidates.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Candidate JSON path.")
    parser.add_argument("--raw-only", action="store_true", help="Only scan raw inputs.")
    parser.add_argument("--wiki-only", action="store_true", help="Only scan wiki pages.")
    args = parser.parse_args()

    paths: list[Path] = []
    if not args.wiki_only:
        paths.extend(RAW_DIRS)
    if not args.raw_only:
        paths.extend(WIKI_DIRS)

    registry_aliases = load_registry_aliases(REGISTRY)
    grouped: dict[str, Candidate] = {}

    for path in iter_sources(paths):
        text = read_text(path)
        frontmatter = parse_frontmatter(text)
        body = strip_frontmatter(text)
        raw_terms: list[str] = []
        for key in ("tags", "related"):
            value = frontmatter.get(key)
            if isinstance(value, list):
                raw_terms.extend(title_from_tag(str(item)) for item in value if str(item).strip())
        raw_terms.extend(match.group(1) for match in re.finditer(r"\*\*([^*\n]{2,60})\*\*", body))
        for section in re.findall(
            r"^##\s+(?:术语和概念|可提炼页面|相关页面|候选拆分页)\s*\n(.*?)(?=^##\s+|\Z)",
            body,
            flags=re.MULTILINE | re.DOTALL,
        ):
            for line in section.splitlines():
                bullet = re.match(r"^[-*]\s+`?([^`：:，,]+)`?", line.strip())
                if bullet:
                    raw_terms.append(bullet.group(1))
        raw_terms.extend(re.findall(r"\b[A-Z][A-Za-z0-9]*(?:[- ][A-Z]?[A-Za-z0-9]+){1,4}\b", body))
        raw_terms.extend(
            re.findall(
                r"[\u4e00-\u9fffA-Za-z0-9-]{2,18}(?:"
                + "|".join(re.escape(suffix) for suffix in CHINESE_SUFFIXES)
                + r")",
                body,
            )
        )
        rel = str(path.relative_to(REPO_ROOT))
        for raw in raw_terms:
            name = normalize_name(raw)
            if not is_candidate_name(name):
                continue
            slug = slugify(name)
            if name.lower() in registry_aliases or slug.lower() in registry_aliases:
                slug = registry_aliases.get(name.lower(), registry_aliases.get(slug.lower(), slug))
            candidate = grouped.setdefault(
                slug,
                Candidate(
                    raw_name=name,
                    normalized_name=name,
                    slug=slug,
                    suggested_type=suggested_type(name),
                ),
            )
            candidate.aliases.add(name)
            candidate.source_files.add(rel)
            ctx = context_for(body, name) or name
            if ctx and ctx not in candidate.contexts and len(candidate.contexts) < 5:
                candidate.contexts.append(ctx)

    output_candidates = []
    for candidate in grouped.values():
        candidate.evidence_count = len(candidate.source_files)
        if candidate.suggested_type != "concept_candidate":
            candidate.decision = "defer"
        elif candidate.evidence_count >= 2:
            candidate.decision = "review"
        else:
            candidate.decision = "candidate"
        data = asdict(candidate)
        data["source_files"] = sorted(candidate.source_files)
        data["aliases"] = sorted(candidate.aliases)
        output_candidates.append(data)

    output_candidates.sort(key=lambda item: (-item["evidence_count"], item["slug"]))
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "candidate_count": len(output_candidates),
        "candidates": output_candidates,
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(output_candidates)} candidates to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
