#!/bin/bash
# 批处理摄取扫描脚本
# 用于列出 raw/ 目录中的待处理文件；实际知识抽取仍由 LLM 完成。

set -e

WIKI_DIR="wiki"
RAW_DIR="raw"
LOG_FILE="$WIKI_DIR/log.md"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT"

echo "开始批量扫描新文件..."
echo "项目根目录: $PROJECT_ROOT"
echo "原始资料目录: $RAW_DIR"
echo "Wiki目录: $WIKI_DIR"

mkdir -p "$RAW_DIR"/{articles,papers,books,transcripts,images,extracted,assets}
mkdir -p "$WIKI_DIR"/{sources,entities,concepts,topics,comparisons,synthesis}

echo ""
echo "找到以下待处理文件:"

find "$RAW_DIR" -type f \( \
  -name "*.md" -o \
  -name "*.txt" -o \
  -name "*.pdf" -o \
  -name "*.docx" -o \
  -name "*.html" -o \
  -name "*.epub" \) \
  ! -path "$RAW_DIR/extracted/*" \
  | while read -r file; do
    filename=$(basename "$file")
    rel_path="${file#$PROJECT_ROOT/}"

    if grep -q "$filename" "$LOG_FILE" 2>/dev/null; then
        echo "  done    $rel_path"
    else
        echo "  pending $rel_path"
    fi
done

echo ""
echo "处理建议:"
echo "1. PDF或长文先生成抽取文本和分块:"
echo "   python scripts/prepare_source.py raw/articles/example.pdf"
echo "2. 搜索已有wiki上下文:"
echo "   python scripts/search.py \"keyword\" --path wiki"
echo "3. 让LLM基于抽取文本或chunk逐步摄取源文档。"
echo "4. 完成后运行健康检查:"
echo "   python scripts/lint_wiki.py"
echo ""
echo "注意: 本脚本只负责扫描和提示，不直接生成wiki页面。"

if [ ! -f "$LOG_FILE" ]; then
    echo "# 操作日志" > "$LOG_FILE"
    echo "" >> "$LOG_FILE"
fi

echo "" >> "$LOG_FILE"
echo "## [$(date '+%Y-%m-%d %H:%M')] batch-scan | 批量扫描未处理文件" >> "$LOG_FILE"
echo "- 扫描原始资料目录" >> "$LOG_FILE"
echo "- 识别未处理文件" >> "$LOG_FILE"
echo "- 提示先运行 prepare_source.py 和 lint_wiki.py" >> "$LOG_FILE"

echo ""
echo "扫描完成。日志已更新: $LOG_FILE"
