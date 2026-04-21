#!/usr/bin/env python3
"""
Basic wiki health checks.

The lint focuses on repository invariants that are cheap to verify locally:
- Markdown files should have YAML-style frontmatter.
- Obsidian wiki links should point to existing wiki pages.
- Source pages should not be marked stable when their source was not extracted.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List

try:
    import yaml
except ImportError:  # pragma: no cover - handled at runtime
    yaml = None


REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Issue:
    level: str
    file: Path
    line: int
    message: str

    def format(self) -> str:
        rel = self.file.as_posix()
        return f"{self.level}: {rel}:{self.line}: {self.message}"


def parse_frontmatter(text: str) -> Dict[str, object]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, flags=re.DOTALL)
    if not match or yaml is None:
        return {}
    data = yaml.safe_load(match.group(1))
    return data if isinstance(data, dict) else {}


def iter_markdown(root: Path) -> Iterable[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def page_names(files: Iterable[Path], wiki_root: Path) -> set[str]:
    names: set[str] = set()
    for path in files:
        names.add(path.stem)
        names.add(path.relative_to(wiki_root).with_suffix("").as_posix())
    return names


def lint(wiki_root: Path) -> List[Issue]:
    files = list(iter_markdown(wiki_root))
    names = page_names(files, wiki_root)
    issues: List[Issue] = []

    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        frontmatter = parse_frontmatter(text)
        requires_frontmatter = path.name != "log.md"
        if requires_frontmatter and not frontmatter:
            issues.append(Issue("ERROR", path, 1, "missing or invalid frontmatter"))

        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in re.finditer(r"\[\[([^\]|#]+)", line):
                target = match.group(1).strip()
                if target and target not in names:
                    issues.append(
                        Issue(
                            "WARN",
                            path,
                            line_number,
                            f"wiki link target does not exist: [[{target}]]",
                        )
                    )

        if frontmatter.get("type") == "source":
            status = str(frontmatter.get("status", "")).lower()
            extraction = str(frontmatter.get("extraction_status", "")).lower()
            if status == "stable" and extraction not in {"extracted", "verified"}:
                issues.append(
                    Issue(
                        "ERROR",
                        path,
                        1,
                        "source page is stable but extraction_status is not extracted/verified",
                    )
                )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local wiki health checks.")
    parser.add_argument("--wiki", default=str(REPO_ROOT / "wiki"), help="Wiki directory.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero for warnings as well as errors.",
    )
    args = parser.parse_args()

    issues = lint(Path(args.wiki))
    for issue in issues:
        print(issue.format())

    errors = [issue for issue in issues if issue.level == "ERROR"]
    warnings = [issue for issue in issues if issue.level == "WARN"]
    print(f"Checked {args.wiki}: {len(errors)} error(s), {len(warnings)} warning(s)")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
