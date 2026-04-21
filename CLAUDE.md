# 基于LLM的个人知识库模式

## 概述

这是一个使用大型语言模型（LLM）构建和维护个人知识库的系统。核心思想是让LLM充当wiki的维护者，将原始资料编译成结构化的、相互链接的markdown文件集合，而不是在每次查询时重新发现知识。

系统有三个层次：
1. **原始资料** (`raw/`) - 用户收集的源文档（文章、论文、图像等），LLM读取但不修改
2. **Wiki** (`wiki/`) - LLM生成和维护的markdown文件集合（摘要、实体页面、概念页面等）
3. **模式** (`CLAUDE.md`) - 本文件，定义wiki的结构、约定和工作流程

## 目录结构

```
D:\X\Karpathy\
├── CLAUDE.md                 # 本文件 - 模式定义
├── raw/                      # 原始资料（不可变）
│   ├── articles/             # 文章、博客帖子
│   ├── papers/               # 学术论文
│   ├── books/                # 书籍章节
│   ├── transcripts/          # 会议记录、播客文字稿
│   ├── images/               # 图片资源
│   ├── extracted/            # 从PDF/长文抽取出的可摄取文本和分块缓存
│   └── assets/               # 其他资产（视频、音频等）
├── wiki/                     # LLM生成和维护的wiki
│   ├── index.md              # 内容索引（分类目录）
│   ├── log.md                # 操作日志（按时间顺序）
│   ├── sources/              # 源文档摘要
│   ├── entities/             # 实体页面（人物、地点、组织等）
│   ├── concepts/             # 概念页面（理论、方法、技术等）
│   ├── topics/               # 主题概述页面
│   ├── comparisons/          # 比较分析页面
│   └── synthesis/            # 综合分析和洞察
├── templates/                # 页面模板
│   ├── source_summary.md     # 源文档摘要模板
│   ├── entity_page.md        # 实体页面模板
│   ├── concept_page.md       # 概念页面模板
│   └── topic_overview.md     # 主题概述模板
└── scripts/                  # 辅助脚本（可选）
    └── search.py             # 本地搜索脚本
```

## 模式约定

### 文件命名
- 使用小写字母、数字和连字符（`-`）
- 避免空格，使用连字符分隔单词
- 示例：`artificial-intelligence.md`, `alan-turing.md`, `transformer-architecture.md`

### 页面结构
每个wiki页面应包含：
1. **Frontmatter** (YAML格式) - 元数据
2. **标题** - 页面主题
3. **内容** - 结构化信息
4. **链接** - 相关页面引用
5. **来源** - 引用和参考

### Frontmatter字段
```yaml
---
id: unique-identifier          # 唯一标识符
type: entity|concept|topic|source|comparison|synthesis  # 页面类型
title: 页面标题                 # 显示标题
created: YYYY-MM-DD            # 创建日期
updated: YYYY-MM-DD            # 最后更新日期
sources:                      # 相关源文档
  - raw/articles/article1.md
  - raw/papers/paper1.pdf
tags:                         # 标签
  - tag1
  - tag2
related:                      # 相关页面
  - wiki/entities/entity1.md
  - wiki/concepts/concept1.md
status: draft|stable|archived|needs-extraction|needs-verification # 页面状态
importance: low|medium|high   # 重要性
confidence: low|medium|high   # 信息置信度
extraction_status: extracted|ocr-needed|failed|not-applicable # 源文本抽取状态
evidence_policy: source-supported|inferred|background-knowledge|needs-verification # 主要证据类型
---
```

### 链接约定
- 使用Obsidian风格的wiki链接：`[[页面名称]]`
- 避免绝对路径
- 在适当的位置添加双向链接

## 摄取流程

当添加新源文档时，LLM应遵循以下流程：

### 0. 源文本准备（PDF和长文必须执行）
- 对PDF、超长Markdown、超长TXT，先运行 `scripts/prepare_source.py` 生成可追溯的抽取文本和分块：
  ```
  python scripts/prepare_source.py raw/articles/example.pdf
  ```
- 普通PDF文本抽取结果保存到 `raw/extracted/`，长文分块保存到 `raw/extracted/chunks/`。
- 如果PDF页面没有可抽取文本，必须标记 `status: needs-extraction`、`extraction_status: ocr-needed`，不要生成稳定摘要。
- 如果抽取失败，只能创建占位页或失败记录，不能基于文件名、标题或领域常识生成完整源摘要。
- 长文摄取必须逐块处理。每次发送给模型的内容应只包含当前chunk、必要的相邻chunk摘要、相关wiki页面摘要和目标模板，避免一次性塞入完整长文。
- 生成最终源摘要前，先综合各chunk摘要，再写入 `wiki/sources/`。

### 1. 源文档分析
- 读取并理解源文档内容
- 识别关键实体、概念和主题
- 提取主要观点、论据和证据
- 明确每条重要结论的证据类型：
  - `source-supported`：源文本明确支持
  - `inferred`：从源文本合理推断
  - `background-knowledge`：来自领域背景知识，非本文直接给出
  - `needs-verification`：需要回到原文或外部资料核验

### 2. 创建源摘要
- 在 `wiki/sources/` 中创建摘要页面
- 包括：概述、关键要点、重要引用、作者信息、出版详情
- 添加适当的标签和分类
- 源摘要必须引用 `raw/extracted/` 中的抽取文本或chunk路径。
- 对PDF来源，frontmatter必须包含 `source_file`、`extracted_file`、`extraction_status`。
- 不得把 `inferred` 或 `background-knowledge` 内容伪装成原文结论。

### 3. 更新现有页面
- 识别与源文档相关的现有wiki页面
- 更新这些页面以包含新信息
- 标记冲突、矛盾或补充信息

### 4. 创建新页面
- 如果源文档引入了新实体或概念，创建相应页面
- 遵循模板确保一致性

### 5. 更新索引和日志
- 在 `wiki/index.md` 中添加新页面的引用
- 在 `wiki/log.md` 中添加操作记录
- 运行 `python scripts/lint_wiki.py` 检查frontmatter和wiki链接。
- 每次摄取完成后提交git变更，提交信息应说明处理的源文档。

### 摄取命令示例
```
请处理 raw/articles/new-article.md 并将其集成到wiki中。
```

## 查询流程

当用户提出问题时，LLM应：

### 1. 搜索相关页面
- 首先检查 `wiki/index.md` 查找相关页面
- 使用搜索工具（如 `scripts/search.py` 或 Obsidian搜索）查找更多相关页面

### 2. 综合回答
- 读取相关页面内容
- 综合信息形成连贯回答
- 提供引用（链接到wiki页面和源文档）

### 3. 可选：创建新页面
- 如果回答包含有价值的分析或洞察，可将其保存为新wiki页面
- 例如：比较分析、深入探讨、新连接

### 查询示例
```
"比较神经网络和符号AI的优缺点"
```

## Lint流程

定期运行健康检查：

### 1. 一致性检查
- 查找页面间的矛盾
- 识别过时声明
- 标记需要更新的页面

### 2. 完整性检查
- 查找孤页（无入站链接）
- 识别提到但缺少页面的重要概念
- 检查缺少的交叉引用

### 3. 结构检查
- 确保所有页面有适当的frontmatter
- 验证所有链接有效
- 检查文件命名一致性

### 4. 改进建议
- 建议新问题调查
- 推荐新源文档
- 提出结构调整建议

### Lint命令示例
```
请对wiki进行健康检查，报告问题并提出改进建议。
```

本地脚本：
```
python scripts/lint_wiki.py
```

## 索引和日志维护

### `wiki/index.md`
- 按类别组织的wiki页面目录
- 每个页面包括：链接、一行摘要、可选元数据
- 在每次摄取后更新
- 结构示例：
  ```
  # Wiki索引
  
  ## 源文档摘要
  - [[文章标题]] - 关于AI伦理的讨论...
  - [[论文标题]] - 神经网络架构研究...
  
  ## 实体
  - [[实体名称]] - 人物/组织描述...
  
  ## 概念
  - [[概念名称]] - 理论/方法描述...
  ```

### `wiki/log.md`
- 按时间顺序的操作记录
- 每个条目有标准前缀：`## [YYYY-MM-DD HH:MM] 操作类型 | 描述`
- 易于用grep解析：`grep "^## \[" log.md | tail -5`
- 记录：摄取、查询、lint操作、重大更新

## Obsidian配置

### 推荐设置
1. **文件与链接设置**：
   - "附件文件夹路径"：`raw/assets/`
   - "使用Wiki链接"：启用
   - "自动转换URL到链接"：启用

2. **核心插件**：
   - 反向链接面板
   - 星标页面
   - 标签面板
   - 图形视图
   - 模板
   - Dataview（用于frontmatter查询）

3. **社区插件**：
   - Advanced Tables
   - Excalidraw（用于图表）
   - Kanban（用于项目管理）
   - Calendar（用于时间线）

### 热键推荐
- `Ctrl+Shift+D`：下载当前文件的附件
- `Ctrl+P`：命令面板
- `Ctrl+O`：快速切换

## 工具和脚本

### 搜索工具 (`scripts/search.py`)
```python
#!/usr/bin/env python3
"""
简单的wiki搜索工具
支持关键词搜索和向量搜索（可选）
"""
import argparse
import os
import re
from pathlib import Path

def search_wiki(keyword, wiki_path="wiki"):
    """在wiki中搜索关键词"""
    results = []
    for root, dirs, files in os.walk(wiki_path):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if keyword.lower() in content.lower():
                            # 提取包含关键词的行
                            lines = content.split('\n')
                            for i, line in enumerate(lines):
                                if keyword.lower() in line.lower():
                                    results.append({
                                        'file': filepath,
                                        'line': i+1,
                                        'snippet': line.strip()[:100]
                                    })
                except Exception as e:
                    continue
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="搜索wiki内容")
    parser.add_argument("keyword", help="搜索关键词")
    parser.add_argument("--path", default="wiki", help="wiki路径")
    args = parser.parse_args()
    
    results = search_wiki(args.keyword, args.path)
    
    print(f"找到 {len(results)} 个结果:")
    for r in results:
        print(f"{r['file']}:{r['line']} - {r['snippet']}")
```

### 源文本准备工具 (`scripts/prepare_source.py`)
```bash
# 从PDF抽取文本并按长文摄取预算分块
python scripts/prepare_source.py raw/articles/example.pdf

# 只抽取文本，不生成chunk
python scripts/prepare_source.py raw/articles/example.pdf --no-chunks

# 调整chunk大小，降低模型上下文压力
python scripts/prepare_source.py raw/articles/example.pdf --max-chars 12000 --overlap-chars 800
```

输出约定：
- `raw/extracted/<source>.txt`：抽取出的全文文本
- `raw/extracted/<source>.manifest.json`：抽取方法、页数、字符数、页码映射
- `raw/extracted/chunks/<source>/chunk-0001.md`：可逐块发送给LLM的文本块
- `raw/extracted/chunks/<source>/manifest.json`：分块数量和参数

### Wiki健康检查工具 (`scripts/lint_wiki.py`)
```bash
python scripts/lint_wiki.py
python scripts/lint_wiki.py --strict
```

检查内容：
- Markdown页面是否有frontmatter
- Obsidian `[[wiki-link]]` 是否指向已存在页面
- `type: source` 页面是否把未抽取/未验证内容标记为稳定状态

### 批量摄取脚本
```bash
#!/bin/bash
# scripts/batch_ingest.sh
# 批量处理raw目录中的新文件

WIKI_DIR="wiki"
RAW_DIR="raw"
LOG_FILE="$WIKI_DIR/log.md"

echo "开始批量处理新文件..."

# 查找未处理的文件（根据日志判断）
# 这里简化处理：处理所有raw目录下的新文件
find $RAW_DIR -type f \( -name "*.md" -o -name "*.txt" -o -name "*.pdf" \) | while read file; do
    echo "处理: $file"
    # 这里可以调用LLM进行处理
    # 实际实现需要与LLM API集成
done

echo "批量处理完成。"
```

## 最佳实践

### 源文档管理
1. **下载附件**：使用Obsidian Web Clipper和`Ctrl+Shift+D`下载图片
2. **保持原始性**：原始资料永不修改
3. **版本控制**：使用git跟踪wiki变化

### LLM协作
1. **逐步摄取**：一次处理一个源文档，保持参与
2. **验证更新**：检查LLM对现有页面的修改
3. **指导重点**：告诉LLM需要强调什么
4. **证据优先**：未读取源文本时不生成完整摘要；长文必须先分块再综合
5. **控制上下文**：优先传chunk摘要和相关页面摘要，而不是传入完整长文和完整wiki

### Wiki维护
1. **定期Lint**：每周运行健康检查
2. **更新索引**：每次摄取后立即更新
3. **保持日志**：记录所有重要操作

## 工作流示例

### 典型会话
1. **用户**：请处理 `raw/articles/ai-ethics.md`
2. **LLM**：读取文章，创建摘要，更新相关页面，更新索引和日志
3. **用户**：浏览更新后的wiki页面，检查链接
4. **用户**："AI伦理中的主要争议有哪些？"
5. **LLM**：搜索相关页面，综合回答，引用wiki页面
6. **用户**：将这个分析保存为比较页面
7. **LLM**：创建 `wiki/comparisons/ai-ethics-controversies.md`

### 批处理模式
```bash
# 处理所有未处理的源文档
请批量处理raw目录中所有新文件。
```

## 故障排除

### 常见问题
1. **链接断开**：运行lint检查，修复或移除无效链接
2. **信息冲突**：创建`wiki/comparisons/`页面记录不同观点
3. **文件重复**：合并相似页面，更新所有引用

### 性能优化
- Wiki较小（<1000页）：使用`index.md`足够
- Wiki较大：实现搜索脚本或使用qmd
- 定期归档：将不活跃页面移动到`wiki/archive/`

## 扩展可能性

### 输出格式
- **幻灯片**：使用Marp从wiki生成演示文稿
- **图表**：使用Excalidraw创建图表并嵌入
- **时间线**：使用Calendar插件可视化事件
- **报告**：组合多个页面生成综合报告

### 自动化
- **监视文件夹**：自动处理添加到`raw/`的新文件
- **定期摘要**：生成每周/每月知识摘要
- **交叉验证**：自动检查新源文档与现有知识的矛盾

---

*本模式由LLM维护和更新。随着wiki的发展，可调整和优化本文件以反映实际工作实践。*
