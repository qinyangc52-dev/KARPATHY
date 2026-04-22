#!/usr/bin/env python3
"""
Promote reviewed concept candidates into wiki/concepts/.

Promotion is explicit: the script never creates concept pages unless a slug is
passed with --promote. Generated pages are drafts and keep evidence boundaries
clear.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - handled at runtime
    yaml = None


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATES = REPO_ROOT / "raw" / "extracted" / "concepts" / "candidates.json"
CONCEPT_DIR = REPO_ROOT / "wiki" / "concepts"
REGISTRY = CONCEPT_DIR / "_registry.yml"
INDEX = REPO_ROOT / "wiki" / "index.md"
LOG = REPO_ROOT / "wiki" / "log.md"
STRUCTURED_LINK_HEADERS = {
    "术语和概念",
    "可提炼页面",
    "相关页面",
    "候选拆分页",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists() or yaml is None:
        return {}
    data = yaml.safe_load(read_text(path)) or {}
    return data if isinstance(data, dict) else {}


def dump_yaml(data: dict[str, Any]) -> str:
    if yaml is None:
        raise RuntimeError("PyYAML is required for concept promotion.")
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False)


def load_candidates(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(
            f"Candidate manifest not found: {path}. Run scripts/concept_candidates.py first."
        )
    payload = json.loads(read_text(path))
    return {item["slug"]: item for item in payload.get("candidates", [])}


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, flags=re.DOTALL)
    if not match or yaml is None:
        return {}, text
    data = yaml.safe_load(match.group(1)) or {}
    body = text[match.end() :]
    return (data if isinstance(data, dict) else {}), body


def write_frontmatter(frontmatter: dict[str, Any], body: str) -> str:
    return "---\n" + dump_yaml(frontmatter).strip() + "\n---\n" + body


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def source_list(candidate: dict[str, Any]) -> list[str]:
    return list(
        dict.fromkeys(str(item).replace("\\", "/") for item in candidate.get("source_files", []) if item)
    )


def display_title(candidate: dict[str, Any], slug: str) -> str:
    title = candidate.get("normalized_name") or candidate.get("raw_name") or slug
    aliases = [str(item) for item in candidate.get("aliases", [])]
    for alias in aliases:
        if alias.isupper() and len(alias) <= 8:
            return alias
    return str(title)


def clean_context(context: str) -> str:
    context = re.sub(r"\[\[([^\]]+)\]\]", r"\1", context)
    context = context.replace("[[", "").replace("]]", "")
    return context


def concept_page(slug: str, candidate: dict[str, Any]) -> str:
    title = display_title(candidate, slug)
    sources = source_list(candidate)
    confidence = "medium" if int(candidate.get("evidence_count") or 0) >= 2 else "low"
    aliases = [item for item in candidate.get("aliases", []) if item != title]
    contexts = [clean_context(item) for item in candidate.get("contexts", [])[:3]]
    context_lines = "\n".join(f"- {context}" for context in contexts) or "-"
    alias_line = ", ".join(aliases) if aliases else "暂无"
    first_source = sources[0] if sources else "现有信息不足"
    source_lines = "\n".join(f"- `{source}`" for source in sources) or "-"
    brief_definition = find_definition(title, aliases, sources)
    if brief_definition:
        strict_definition = "现有来源提供了简明解释；严格定义仍需继续补充和核验。"
        supported_line = f"来源中明确给出简明定义：{brief_definition}"
    else:
        brief_definition = "现有信息不足，需要人工补充。"
        strict_definition = "现有信息不足，需要回到来源材料核验。"
        supported_line = "现有材料只支持该术语或概念在来源中出现，尚不足以形成完整定义。"

    return f"""---
id: concept-{slug}
type: concept
title: "{title}"
created: {today()}
updated: {today()}
sources:
{chr(10).join(f"  - {source}" for source in sources) if sources else "  - needs-source"}
tags:
  - concept
related: []
status: draft
importance: medium
confidence: {confidence}
evidence_policy: inferred
aliases:
{chr(10).join(f"  - {alias}" for alias in aliases) if aliases else "  []"}
---

# {title}

> 来源：由候选概念 `{slug}` 晋升而来。当前页面是草稿，不能把个人归纳伪装成文献结论。

## 核心结论

{title} 是一个候选晋升概念。当前可确认的是它在 `{first_source}` 等来源中反复出现或具有结构化知识价值；具体定义仍需继续补充和核验。

## 定义

- **简明定义**：{brief_definition}
- **严格定义**：{strict_definition}
- **不应混淆的概念**：现有信息不足。

## 背景

该概念来自候选抽取与人工晋升流程。别名或变体：{alias_line}。

## 关键组成

1. 现有信息不足。
2. 现有信息不足。
3. 现有信息不足。

## 与其他概念的关系

- 现有信息不足。

## 例子

- **典型例子**：现有信息不足。
- **反例**：现有信息不足。

## 争议与局限

- 当前页面只完成概念节点创建和来源追踪，不代表该概念已稳定。

## 来源与证据

- **source-supported**：{supported_line}
- **inferred**：晋升为概念页是基于候选出现位置、上下文和人工判断。
- **background-knowledge**：未补充。
- **needs-verification**：需要补充严格定义、边界、例子和反例。

## 候选上下文

{context_lines}

## 来源

{source_lines}

## 后续问题

- 这个概念的最小定义是什么？
- 它与哪些实体、主题或相邻概念容易混淆？
- 是否还有更多来源支持它成为稳定概念？
"""


def find_definition(title: str, aliases: list[str], sources: list[str]) -> str:
    names = [title, *aliases]
    for source in sources:
        path = REPO_ROOT / source
        if not path.exists() or path.suffix.lower() != ".md":
            continue
        text = read_text(path)
        for name in names:
            escaped = re.escape(name)
            patterns = [
                rf"^-\s+{escaped}\s*[：:]\s*(.+)$",
                rf"^\*\*{escaped}\*\*\s*[：:]\s*(.+)$",
            ]
            for pattern in patterns:
                match = re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE)
                if match:
                    return match.group(1).strip()
    return ""


def registry_alias_map(registry: dict[str, Any]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for slug, item in (registry.get("concepts") or {}).items():
        mapping[slug.lower()] = slug
        mapping[str(item.get("title", slug)).lower()] = slug
        for alias in item.get("aliases") or []:
            mapping[str(alias).lower()] = slug
    return mapping


def promote(slug: str, candidates: dict[str, dict[str, Any]], force: bool = False) -> Path:
    if slug not in candidates:
        raise KeyError(f"Unknown candidate slug: {slug}")
    candidate = candidates[slug]
    if candidate.get("suggested_type") != "concept_candidate" and not force:
        raise ValueError(
            f"{slug} is {candidate.get('suggested_type')}; use --force only after manual review."
        )

    registry = load_yaml(REGISTRY) or {"concepts": {}}
    registry.setdefault("concepts", {})
    alias_map = registry_alias_map(registry)
    title = candidate.get("normalized_name") or candidate.get("raw_name") or slug
    if slug.lower() in alias_map and alias_map[slug.lower()] != slug:
        raise ValueError(f"{slug} is already registered as alias of {alias_map[slug.lower()]}")
    if title.lower() in alias_map and alias_map[title.lower()] != slug:
        raise ValueError(f"{title} is already registered as alias of {alias_map[title.lower()]}")

    concept_path = CONCEPT_DIR / f"{slug}.md"
    if concept_path.exists():
        raise FileExistsError(f"Concept page already exists: {concept_path}")

    write_text(concept_path, concept_page(slug, candidate))
    registry["concepts"][slug] = {
        "title": title,
        "aliases": sorted(set(candidate.get("aliases", []))),
        "status": "draft",
        "sources": source_list(candidate),
        "promoted_from": str(DEFAULT_CANDIDATES.relative_to(REPO_ROOT)),
        "created": today(),
    }
    write_text(REGISTRY, dump_yaml(registry))
    update_index(slug, title)
    update_log(slug, title)
    backfill_links(slug, title, candidate)
    return concept_path


def update_index(slug: str, title: str) -> None:
    if not INDEX.exists():
        return
    text = read_text(INDEX)
    bullet = f"- [[{slug}]] - {title}"
    if bullet in text:
        return
    match = re.search(r"^## 概念\s*$", text, flags=re.MULTILINE)
    if not match:
        text = text.rstrip() + f"\n\n## 概念\n\n{bullet}\n"
    else:
        start = match.end()
        next_header = re.search(r"^##\s+", text[start:], flags=re.MULTILINE)
        end = start + next_header.start() if next_header else len(text)
        section = text[start:end]
        if "当前概念页仍在重建" in section or "当前概念页处于重建" in section:
            section = "\n\n" + bullet + "\n\n"
        else:
            section = section.rstrip() + "\n" + bullet + "\n\n"
        text = text[:start] + section + text[end:]
    write_text(INDEX, text)


def update_log(slug: str, title: str) -> None:
    entry = (
        f"\n## [{today()}] promote | 晋升概念 {title}\n\n"
        f"- 从候选概念清单晋升 `[[{slug}]]`。\n"
        f"- 页面写入 `wiki/concepts/{slug}.md`，默认状态为 `draft`。\n"
    )
    text = read_text(LOG) if LOG.exists() else "# Wiki 维护日志\n"
    if f"[[{slug}]]" not in text:
        write_text(LOG, text.rstrip() + "\n" + entry)


def backfill_links(slug: str, title: str, candidate: dict[str, Any]) -> None:
    link = f"[[{slug}]]"
    sources = set(source_list(candidate))
    aliases = {title, candidate.get("raw_name", ""), candidate.get("normalized_name", "")}
    aliases.update(candidate.get("aliases", []))
    aliases = {str(alias) for alias in aliases if alias}

    for path in (REPO_ROOT / "wiki").rglob("*.md"):
        if "concepts" in path.parts or path.name in {"index.md", "log.md"}:
            continue
        rel = str(path.relative_to(REPO_ROOT))
        text = read_text(path)
        if link in text:
            continue
        if rel not in sources and not any(alias in text for alias in aliases):
            continue
        frontmatter, body = parse_frontmatter(text)
        page_type = str(frontmatter.get("type", ""))
        if page_type not in {"source", "entity", "topic", "synthesis"}:
            continue
        related = frontmatter.get("related")
        if not isinstance(related, list):
            related = []
        if slug not in related:
            related.append(slug)
        frontmatter["related"] = related
        body = append_structured_link(body, slug, title)
        write_text(path, write_frontmatter(frontmatter, body))


def append_structured_link(body: str, slug: str, title: str) -> str:
    line = f"- [[{slug}]]：{title}\n"
    lines = body.splitlines(keepends=True)
    insert_at: int | None = None
    for idx, item in enumerate(lines):
        match = re.match(r"^##\s+(.+?)\s*$", item.strip())
        if match and match.group(1) in STRUCTURED_LINK_HEADERS:
            insert_at = idx + 1
            while insert_at < len(lines) and not lines[insert_at].startswith("## "):
                insert_at += 1
            break
    if insert_at is None:
        return body.rstrip() + f"\n\n## 相关页面\n\n{line}"
    if insert_at > 0 and lines[insert_at - 1].strip():
        line = "\n" + line
    lines.insert(insert_at, line)
    return "".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Promote reviewed concept candidates.")
    parser.add_argument("--candidates", default=str(DEFAULT_CANDIDATES), help="Candidate JSON path.")
    parser.add_argument("--dry-run", action="store_true", help="List promotable candidates.")
    parser.add_argument("--all", action="store_true", help="Show all concept candidates in dry-run.")
    parser.add_argument("--promote", action="append", default=[], help="Candidate slug to promote.")
    parser.add_argument("--force", action="store_true", help="Allow promoting non-concept candidates.")
    args = parser.parse_args()

    candidates = load_candidates(Path(args.candidates))
    if args.dry_run or not args.promote:
        print("Promotable concept candidates:")
        for slug, item in sorted(candidates.items()):
            if item.get("suggested_type") == "concept_candidate" and (
                args.all or item.get("decision") == "review"
            ):
                print(
                    f"- {slug}: {item.get('normalized_name')} "
                    f"(evidence={item.get('evidence_count')}, decision={item.get('decision')})"
                )
        if not args.promote:
            return 0

    for slug in args.promote:
        path = promote(slug, candidates, force=args.force)
        print(f"Promoted {slug} -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
