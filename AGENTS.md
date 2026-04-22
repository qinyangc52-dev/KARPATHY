# 基于 LLM 的个人知识库模式

## 概述

这是一个使用大型语言模型维护个人知识库的项目。LLM 的职责不是每次查询时重新发现知识，而是把原始资料和个人笔记加工成结构化、可链接、可追溯的 Markdown wiki。

系统保持三层结构：

1. **原始资料 `raw/`**：外部资料、旧笔记、随笔草稿。默认不可修改。
2. **Wiki `wiki/`**：LLM 生成和维护的结构化知识页面。
3. **模式 `AGENTS.md`**：本文件，定义目录、模板、证据规则和工作流。

核心边界：

- 文献笔记不能编。
- 已整理笔记不能重复堆。
- 平时随笔不能直接污染稳定知识库。

## 目录结构

```text
D:\X\Karpathy\
├── AGENTS.md
├── raw/
│   ├── articles/
│   ├── papers/
│   ├── books/
│   ├── transcripts/
│   ├── images/
│   ├── extracted/
│   ├── assets/
│   └── notes/
│       ├── curated/      # 已整理好的旧笔记，原样保存
│       └── fleeting/     # 平时随笔、灵感、问题、草稿
├── wiki/
│   ├── index.md
│   ├── log.md
│   ├── sources/
│   ├── entities/
│   ├── concepts/
│   ├── topics/
│   ├── comparisons/
│   └── synthesis/
├── templates/
│   ├── literature_note.md
│   ├── permanent_note.md
│   ├── fleeting_note.md
│   ├── source_summary.md
│   ├── entity_page.md
│   ├── concept_page.md
│   ├── topic_overview.md
│   ├── comparison_page.md
│   └── synthesis_page.md
└── scripts/
    ├── prepare_source.py
    ├── lint_wiki.py
    ├── search.py
    ├── concept_candidates.py
    └── promote_concepts.py
```

## 通用规则

### 文件命名

- 使用小写字母、数字和连字符。
- 避免空格。
- 示例：`artificial-intelligence.md`、`alan-turing.md`、`transformer-architecture.md`。

### 页面结构

每个 wiki 页面应包含：

1. YAML frontmatter
2. 标题
3. 结构化正文
4. 相关链接
5. 来源或证据说明

### Frontmatter 基本字段

```yaml
---
id: unique-identifier
type: entity|concept|topic|source|comparison|synthesis|index|fleeting
title: ""
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
tags: []
related: []
status: draft|stable|archived|needs-extraction|needs-verification|raw|triaged|promoted
importance: low|medium|high
confidence: low|medium|high
evidence_policy: source-supported|inferred|background-knowledge|needs-verification
---
```

### 链接约定

- 使用 Obsidian 风格 wiki 链接：`[[页面名称]]`。
- 避免绝对路径。
- 新增或更新页面时补充必要的双向链接。

## 三类笔记工作流

### 1. 文献笔记

适用对象：

- 论文
- 学术文章
- 技术报告
- 书籍章节
- 访谈文字稿
- 长博客或长文

输入位置：

```text
raw/papers/
raw/articles/
raw/books/
raw/transcripts/
```

输出位置：

```text
wiki/sources/
```

目标：生成严格论文精读报告，而不是读后感。

处理流程：

1. 原文放入 `raw/` 对应目录。
2. PDF 或长文必须先运行：

   ```bash
   python scripts/prepare_source.py <source-file>
   ```

3. 检查抽取结果：
   - 成功：继续精读。
   - 无文本：标记 `status: needs-extraction` 和 `extraction_status: ocr-needed`。
   - 抽取失败：只能创建占位页，不能生成完整总结。
4. 长文逐块处理，先生成 chunk 摘要，再综合为完整文献笔记。
5. 根据文献内容更新相关概念、实体、主题页面。
6. 更新 `wiki/index.md` 和 `wiki/log.md`。
7. 运行 `python scripts/lint_wiki.py`。

文献笔记必须包含：

1. 论文标题和摘要
2. 引言
3. 正文部分
4. 图片分析
5. 结论
6. 参考文献
7. 补充材料
8. Q1-Q16 学术问题回答
9. 三个关键问题及作答
10. 术语、概念、相关页面
11. 证据边界与局限

文献证据标签：

- `source-supported`：原文明确支持。
- `inferred`：从原文合理推断。
- `background-knowledge`：领域背景知识。
- `needs-verification`：需要回查原文或外部资料核验。

文献笔记写作要求：

- 中文 Markdown。
- 先结论，后分析。
- 语言直接、专业、干净。
- 不奉承作者，不迎合用户。
- 不写空话。
- 对复杂概念使用简单但准确的比喻。
- 图表、参考文献、补充材料没读到就明确说没读到。
- 不确定就写“现有信息不足”。

### 2. 已整理笔记

适用对象：

- 旧主题笔记
- 课程笔记
- 研究笔记
- 读书整理
- 已有结构的个人知识文档

输入位置：

```text
raw/notes/curated/
```

输出位置按内容决定：

```text
wiki/concepts/
wiki/topics/
wiki/synthesis/
wiki/comparisons/
wiki/entities/
```

目标：把旧知识迁移进 wiki 网络，重点是合并、去重、补链接。

处理流程：

1. 旧笔记原样放入 `raw/notes/curated/`。
2. 如果旧笔记是 PDF 或长文，可以运行 `python scripts/prepare_source.py <source-file>` 抽取文本到 `raw/extracted/`。
3. 抽取结果只作为迁移、提炼和候选概念抽取的中间证据，不改变该输入“个人已整理笔记”的性质。
4. 只要输入来自 `raw/notes/curated/`，不得自动创建 `wiki/sources/` 页面；输出只能按内容进入 `wiki/concepts/`、`wiki/topics/`、`wiki/synthesis/`、`wiki/comparisons/` 或 `wiki/entities/`。
5. 先判断笔记中的知识单元，而不是按整篇笔记机械生成一个页面。
6. 按全局分类规则决定创建、合并或只列候选页面。
7. 先搜索现有页面，能合并就合并，不能合并再新建。
8. 补充来源、链接、标签和必要证据标记。
9. 更新 `wiki/index.md` 和 `wiki/log.md`。
10. 运行 `python scripts/lint_wiki.py`。

全局分类规则：

| 目录 | 页面回答的问题 | 进入条件 |
|---|---|---|
| `wiki/sources/` | 这份外部资料说了什么？ | 输入来自 `raw/articles/`、`raw/papers/`、`raw/books/` 或 `raw/transcripts/` 的外部资料。不得用于 `raw/notes/curated/` 中的个人已整理笔记。 |
| `wiki/concepts/` | 这个概念、理论、机制或方法是什么？ | 内容能给出定义、边界、例子、相关概念和证据说明。 |
| `wiki/topics/` | 这个研究方向、问题域或长期关注主题包含什么？ | 内容组织多个问题、概念、来源、实体或后续路线。 |
| `wiki/entities/` | 这个可命名对象是谁或是什么？ | 内容核心是人物、组织、模型、数据集、软件、项目等具体实体。 |
| `wiki/comparisons/` | 这些对象如何比较？ | 内容明确比较两个或多个理论、方法、模型、工具或路线，并有比较维度。 |
| `wiki/synthesis/` | 多个来源综合后形成什么判断？ | 内容是跨来源的个人判断、框架、假设或综合观点。 |

分类判定顺序：

1. 来自 `raw/articles/`、`raw/papers/`、`raw/books/` 或 `raw/transcripts/` 的外部资料优先进入 `wiki/sources/`。
2. 具体项目、模型、软件、数据集优先进入 `wiki/entities/`。
3. 研究方向、问题域或长期关注主题进入 `wiki/topics/`。
4. 单一可定义概念、理论、机制或方法进入 `wiki/concepts/`。
5. 明确二元或多元对比进入 `wiki/comparisons/`。
6. 跨多个来源形成的个人判断、框架或假设进入 `wiki/synthesis/`。
7. 内容不足以支撑独立页面时，只在主页面列为“候选拆分页”，不要生成空页。

拆分原则：

- 一篇旧笔记可以生成一个主页面，也可以拆成多个页面，但每个页面必须有足够内容承担自己的类型。
- 具体工程、软件、数据集、模型实现和复现项目默认先按 `entity` 处理；相关研究方向另建 `topic`。
- 关键词出现不等于创建概念页；只有能写清定义、边界和证据时才创建 `concept`。
- 两个术语同时出现不等于创建比较页；只有存在明确比较维度时才创建 `comparison`。
- 个人判断可以进入 `synthesis`，但必须明确区分来源支持、合理推断、背景知识和待验证内容。

处理原则：

- 已整理笔记是二级来源，不是论文原文。
- 不把个人理解伪装成文献结论。
- 不全文搬运，重点是结构化和网络化。
- 可拆分，也可合并，目标是减少重复页面。

### 3. 平时随笔

适用对象：

- 灵感
- 临时想法
- 研究直觉
- 日常问题
- 阅读感想
- 没想清楚的草稿

输入位置：

```text
raw/notes/fleeting/
```

目标：低摩擦捕捉，定期提炼，不急着进入 wiki。

处理流程：

1. 快速写入 `raw/notes/fleeting/`。
2. 文件名使用日期加短标题，例如：

   ```text
   2026-04-22-brain-criticality-question.md
   ```

3. 只记录最少信息：原始想法、触发来源、为什么可能重要、相关页面、下一步处理。
4. 每周提炼一次：
   - 无价值：保留原处。
   - 一句话有价值：补到已有 wiki 页面。
   - 观点成形：进入 `wiki/synthesis/`。
   - 形成研究问题：进入 `wiki/topics/` 或待研究问题页。
5. 只有随笔被提炼进入 `wiki/` 后，才更新索引和日志并运行 lint。

处理原则：

- 不要求证据充分。
- 不要求结构漂亮。
- 不立刻变成概念页。
- 默认低置信度，默认需要后续验证。

## 概念抽取与晋升

目标：让 `wiki/concepts/` 成为稳定概念节点层，而不是 tag 列表或临时术语堆。概念节点必须能通过 `[[wiki-link]]` 连接 source、entity、topic、comparison 和 synthesis 页面。

### 基本角色

- **candidate**：从 raw 或 wiki 页面中抽取出的候选概念，记录在 `raw/extracted/concepts/candidates.json`。candidate 不是稳定知识页。
- **concept**：经过人工或规则确认后晋升到 `wiki/concepts/` 的稳定概念页。
- **registry**：`wiki/concepts/_registry.yml`，记录 canonical slug、aliases、来源和晋升状态，用于避免重复概念和近义词碎片化。
- **tag**：辅助分类，不替代 concept 页面。

### 候选抽取

可从以下输入抽取候选：

```text
raw/articles/
raw/papers/
raw/books/
raw/transcripts/
raw/notes/curated/
raw/notes/fleeting/
wiki/sources/
wiki/entities/
wiki/topics/
wiki/comparisons/
wiki/synthesis/
```

注意：`raw/notes/curated/` 可以参与候选概念抽取，但这不意味着要创建 `wiki/sources/` 页面。若候选概念来自个人已整理笔记，concept 页的 `sources` 可以直接引用 `raw/notes/curated/...` 和对应的 `raw/extracted/...` 抽取文本。

运行：

```bash
python scripts/concept_candidates.py
```

输出：

```text
raw/extracted/concepts/candidates.json
```

候选记录至少包含：

- `raw_name`
- `normalized_name`
- `slug`
- `source_files`
- `contexts`
- `evidence_count`
- `suggested_type`
- `decision`

### 规范化与去重

- 统一大小写。
- 统一空格、下划线和连字符。
- 合并常见别名、近义词和中英文变体。
- 已在 `_registry.yml` 中注册的 alias 不得生成新的概念页。
- 具体项目、软件、数据集、代码仓库、复现工程优先标记为 `entity_candidate`，不得机械晋升为 concept。

### 晋升条件

候选概念进入 `wiki/concepts/` 前必须满足：

1. 可定义，有明确边界、反例或不应混淆对象。
2. 是稳定知识单元，而不是一次性上下文词。
3. 至少有一个明确来源；只有单一来源时默认 `status: draft`。
4. 不更适合进入 `entity`、`topic`、`comparison`、`synthesis` 或 `source`。
5. 与现有 concept 和 registry alias 不重复。
6. 能按 `templates/concept_page.md` 填写核心结论、定义、背景、关系、例子和证据边界。

晋升运行：

```bash
python scripts/promote_concepts.py --dry-run
python scripts/promote_concepts.py --promote <slug>
```

### 回填链接

已晋升概念应回填到相关 wiki 页面：

- 优先在“术语、概念、相关页面”“可提炼页面”“相关页面”“候选拆分页”等结构化段落中补充 `[[concept-slug]]`。
- 不做全文盲替换，避免过度链接和误替换。
- 同步更新页面 frontmatter 的 `related` 字段。
- 更新 `wiki/index.md` 和 `wiki/log.md`。

### 质量边界

- 不把局部词语机械提升为 concept。
- 不把具体项目、软件、数据集、模型实现误当作 concept。
- 不伪造 source-supported 内容；证据不足时使用 `inferred` 或 `needs-verification`。
- candidate 可以长期保留，等待更多来源或人工判断。

## 索引和日志

### `wiki/index.md`

- 文献摄取后，索引加入 `wiki/sources/`。
- 已整理笔记迁移后，索引加入对应的 `concepts/`、`topics/`、`synthesis/`、`comparisons/` 或 `entities/`。
- 随笔只有被提炼进入 `wiki/` 后才加入索引。

### `wiki/log.md`

记录正式摄取、迁移、提炼和 lint 修复。

日志条目格式：

```text
## [YYYY-MM-DD HH:MM] 操作类型 | 描述
```

## Lint 流程

每次修改 `wiki/` 后运行：

```bash
python scripts/lint_wiki.py
```

定期严格检查：

```bash
python scripts/lint_wiki.py --strict
```

检查重点：

- Markdown 页面是否有 frontmatter。
- Obsidian `[[wiki-link]]` 是否指向已存在页面。
- `type: source` 页面是否有来源文件、抽取状态和证据策略。
- 未抽取或未验证的 source 页面不得标记为 `stable`。
- `type: concept` 页面必须位于 `wiki/concepts/`，并包含 `sources`、`related`、`status`、`evidence_policy`。
- `wiki/concepts/_registry.yml` 中标记为 `promoted` 或 `stable` 的概念必须有对应 Markdown 页面。

## 维护节奏

### 每次处理后

只要修改 `wiki/`，固定做三件事：

1. 更新 `wiki/index.md`。
2. 更新 `wiki/log.md`。
3. 运行 `python scripts/lint_wiki.py`。

### 每周

- 提炼 `raw/notes/fleeting/`。
- 检查 `needs-verification` 页面。
- 合并重复概念。
- 更新主题页。
- 运行 `python scripts/lint_wiki.py --strict`。

### 每月

- 整理 `wiki/synthesis/`。
- 生成月度知识总结。
- 检查高频概念是否需要主题页。
- 检查文献笔记是否需要升级为稳定状态。
- 回看随笔中反复出现的问题，形成研究方向。
