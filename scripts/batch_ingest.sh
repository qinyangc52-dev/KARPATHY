#!/bin/bash
# 批处理摄取脚本
# 用于批量处理raw目录中的新文件

set -e  # 出错时退出

# 配置
WIKI_DIR="wiki"
RAW_DIR="raw"
LOG_FILE="$WIKI_DIR/log.md"
INDEX_FILE="$WIKI_DIR/index.md"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🔍 开始批量处理新文件..."
echo "项目根目录: $PROJECT_ROOT"
echo "原始资料目录: $RAW_DIR"
echo "Wiki目录: $WIKI_DIR"

# 确保目录存在
mkdir -p "$RAW_DIR"/{articles,papers,books,transcripts,images,assets}
mkdir -p "$WIKI_DIR"/{sources,entities,concepts,topics,comparisons,synthesis}

# 查找所有支持的文件类型
# 注意：这个脚本只列出文件，实际处理需要LLM完成
echo ""
echo "📂 找到以下待处理文件:"

# 统计文件
find "$RAW_DIR" -type f \( \
  -name "*.md" -o \
  -name "*.txt" -o \
  -name "*.pdf" -o \
  -name "*.docx" -o \
  -name "*.html" -o \
  -name "*.epub" \) \
  | while read -r file; do
    filename=$(basename "$file")
    rel_path=$(realpath --relative-to="$PROJECT_ROOT" "$file")

    # 检查是否已在日志中提到（简单检查）
    if grep -q "$filename" "$LOG_FILE" 2>/dev/null; then
        echo "  ✓ $rel_path (已处理)"
    else
        echo "  ✗ $rel_path (未处理)"
    fi
done

echo ""
echo "📋 处理建议:"
echo "1. 对于每个未处理的文件，运行以下命令:"
echo "   python scripts/search.py \"关键词\" --path wiki"
echo "2. 或让LLM处理单个文件:"
echo "   \"请处理 raw/articles/文件名.md\""
echo ""
echo "3. 手动处理所有未处理文件:"
echo "   for file in \$(find raw -type f -name \"*.md\"); do"
echo "     echo \"处理 \$file\""
echo "     # 调用LLM处理"
echo "   done"

echo ""
echo "⚠️  注意: 实际的文件处理需要LLM完成。"
echo "   本脚本仅用于列出和识别待处理文件。"

# 更新日志
if [ ! -f "$LOG_FILE" ]; then
    echo "# 操作日志" > "$LOG_FILE"
    echo "" >> "$LOG_FILE"
fi

echo "" >> "$LOG_FILE"
echo "## [$(date '+%Y-%m-%d %H:%M')] batch-scan | 批量扫描未处理文件" >> "$LOG_FILE"
echo "- 扫描原始资料目录" >> "$LOG_FILE"
echo "- 识别未处理文件" >> "$LOG_FILE"
echo "- 更新处理日志" >> "$LOG_FILE"

echo ""
echo "✅ 扫描完成。查看上面列表获取未处理文件。"
echo "📝 日志已更新: $LOG_FILE"