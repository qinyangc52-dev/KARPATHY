#!/usr/bin/env python3
"""
Prepare raw source files for wiki ingestion.

This script keeps the existing repository layout intact:
- source files stay under raw/
- extracted text is cached under raw/extracted/
- long-document chunks are cached under raw/extracted/chunks/

It does not call an LLM. Its job is to make source text small,
traceable, and safe to pass to an LLM in later ingestion steps.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "raw" / "extracted"
DEFAULT_CHUNK_DIR = DEFAULT_OUTPUT_DIR / "chunks"


@dataclass
class PageSpan:
    page: int
    start_char: int
    end_char: int


@dataclass
class ExtractionResult:
    source_file: str
    extracted_file: str
    manifest_file: str
    status: str
    method: str
    page_count: int
    char_count: int
    warning: Optional[str] = None


@dataclass
class ChunkResult:
    chunk_dir: str
    chunk_count: int
    max_chars: int
    overlap_chars: int


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^\w\s.-]+", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-.") or "source"


def read_text_file(path: Path) -> str:
    for encoding in ("utf-8", "utf-8-sig", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def extract_pdf(path: Path) -> tuple[str, List[PageSpan], int, str, Optional[str]]:
    try:
        import fitz  # PyMuPDF
    except ImportError as exc:
        raise RuntimeError(
            "PyMuPDF is required for PDF extraction. Install dependencies with: "
            "pip install -r requirements.txt"
        ) from exc

    spans: List[PageSpan] = []
    parts: List[str] = []
    warning: Optional[str] = None

    with fitz.open(path) as doc:
        page_count = doc.page_count
        cursor = 0
        for index, page in enumerate(doc, start=1):
            text = page.get_text("text").strip()
            if not text:
                text = "[NO EXTRACTABLE TEXT ON THIS PAGE]"
                warning = (
                    "Some pages had no extractable text. If this is a scanned PDF, "
                    "run OCR before creating stable wiki pages."
                )
            page_block = f"\n\n<!-- page:{index} -->\n{text}\n"
            start = cursor
            cursor += len(page_block)
            end = cursor
            parts.append(page_block)
            spans.append(PageSpan(page=index, start_char=start, end_char=end))

    return "".join(parts).strip() + "\n", spans, page_count, "pymupdf", warning


def extract_source(path: Path, output_dir: Path) -> ExtractionResult:
    if not path.exists():
        raise FileNotFoundError(path)
    if not path.is_file():
        raise ValueError(f"Source is not a file: {path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    stem = slugify(path.stem)
    extracted_path = output_dir / f"{stem}.txt"
    manifest_path = output_dir / f"{stem}.manifest.json"

    suffix = path.suffix.lower()
    spans: List[PageSpan] = []
    warning: Optional[str] = None

    if suffix == ".pdf":
        text, spans, page_count, method, warning = extract_pdf(path)
    elif suffix in {".md", ".txt"}:
        text = read_text_file(path)
        page_count = 0
        method = "plain-text"
    else:
        raise ValueError(f"Unsupported source type: {path.suffix}")

    extracted_path.write_text(text, encoding="utf-8")

    result = ExtractionResult(
        source_file=str(path),
        extracted_file=str(extracted_path),
        manifest_file=str(manifest_path),
        status="extracted" if text.strip() else "empty",
        method=method,
        page_count=page_count,
        char_count=len(text),
        warning=warning,
    )

    manifest = {
        **asdict(result),
        "created": datetime.now().isoformat(timespec="seconds"),
        "page_spans": [asdict(span) for span in spans],
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return result


def split_paragraphs(text: str) -> Iterable[str]:
    for part in re.split(r"\n\s*\n", text):
        part = part.strip()
        if part:
            yield part


def chunk_text(
    extracted_file: Path,
    chunk_root: Path,
    max_chars: int,
    overlap_chars: int,
) -> ChunkResult:
    text = read_text_file(extracted_file)
    chunk_dir = chunk_root / extracted_file.stem
    chunk_dir.mkdir(parents=True, exist_ok=True)

    for old_chunk in chunk_dir.glob("chunk-*.md"):
        old_chunk.unlink()

    chunks: List[str] = []
    current = ""
    for paragraph in split_paragraphs(text):
        candidate = f"{current}\n\n{paragraph}".strip() if current else paragraph
        if len(candidate) <= max_chars:
            current = candidate
            continue
        if current:
            chunks.append(current)
            overlap = current[-overlap_chars:] if overlap_chars > 0 else ""
            current = f"{overlap}\n\n{paragraph}".strip() if overlap else paragraph
        else:
            for start in range(0, len(paragraph), max_chars):
                chunks.append(paragraph[start : start + max_chars])
            current = ""
    if current:
        chunks.append(current)

    total = len(chunks)
    for index, chunk in enumerate(chunks, start=1):
        chunk_path = chunk_dir / f"chunk-{index:04d}.md"
        frontmatter = (
            "---\n"
            f"source_extracted: \"{extracted_file.as_posix()}\"\n"
            f"chunk_index: {index}\n"
            f"chunk_count: {total}\n"
            f"char_count: {len(chunk)}\n"
            "---\n\n"
        )
        chunk_path.write_text(frontmatter + chunk.strip() + "\n", encoding="utf-8")

    summary = {
        "source_extracted": str(extracted_file),
        "chunk_dir": str(chunk_dir),
        "chunk_count": total,
        "max_chars": max_chars,
        "overlap_chars": overlap_chars,
        "created": datetime.now().isoformat(timespec="seconds"),
    }
    (chunk_dir / "manifest.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    return ChunkResult(
        chunk_dir=str(chunk_dir),
        chunk_count=total,
        max_chars=max_chars,
        overlap_chars=overlap_chars,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract raw sources and split long text into ingestion chunks."
    )
    parser.add_argument("source", help="Path to a PDF, Markdown, or text source file.")
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory for extracted text and manifests.",
    )
    parser.add_argument(
        "--chunk-dir",
        default=str(DEFAULT_CHUNK_DIR),
        help="Directory for generated chunk folders.",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=18000,
        help="Approximate maximum characters per chunk.",
    )
    parser.add_argument(
        "--overlap-chars",
        type=int,
        default=1200,
        help="Characters to carry from the previous chunk for continuity.",
    )
    parser.add_argument(
        "--no-chunks",
        action="store_true",
        help="Only extract text; do not create chunks.",
    )
    args = parser.parse_args()

    source = Path(args.source)
    if not source.is_absolute():
        source = REPO_ROOT / source

    try:
        extraction = extract_source(source, Path(args.output_dir))
        print(json.dumps(asdict(extraction), ensure_ascii=False, indent=2))

        if not args.no_chunks:
            chunks = chunk_text(
                Path(extraction.extracted_file),
                Path(args.chunk_dir),
                args.max_chars,
                args.overlap_chars,
            )
            print(json.dumps(asdict(chunks), ensure_ascii=False, indent=2))

        if extraction.warning:
            print(f"WARNING: {extraction.warning}", file=sys.stderr)
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
