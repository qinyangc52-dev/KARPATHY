# 示例工作流：人工智能伦理知识库

这个示例展示了如何使用LLM构建和维护一个人工智能伦理知识库。

## 步骤1：添加源文档

将一篇关于AI伦理的文章放入 `raw/articles/`：

```bash
# 假设我们有一篇文章：ai-ethics-principles.md
cp /path/to/ai-ethics-article.md raw/articles/ai-ethics-principles.md
```

文章内容示例（简化）：
```markdown
# AI伦理原则：确保负责任的人工智能

作者：Jane Smith | 出版：AI Ethics Journal | 日期：2026-03-15

## 摘要
本文讨论了人工智能伦理的五个核心原则：透明度、公正性、责任、隐私和安全...

## 主要原则
1. **透明度**：AI系统应可解释和透明
2. **公正性**：避免偏见和歧视
3. **责任**：明确责任归属
4. **隐私**：保护个人数据
5. **安全**：确保AI系统安全可靠
```

## 步骤2：处理源文档

告诉LLM处理新文章：

```
请处理 raw/articles/ai-ethics-principles.md
```

LLM执行以下操作：

### 2.1 创建源摘要
在 `wiki/sources/ai-ethics-principles.md` 中创建摘要页面：

```yaml
---
id: source-ai-ethics-principles
type: source
title: "AI伦理原则：确保负责任的人工智能"
created: 2026-04-21
updated: 2026-04-21
source_file: "raw/articles/ai-ethics-principles.md"
author: "Jane Smith"
publication: "AI Ethics Journal"
date_published: 2026-03-15
tags: [ai-ethics, principles, transparency, fairness]
related: []
confidence: high
importance: high
---
```

### 2.2 更新相关页面
- **创建新实体页面**：`wiki/entities/jane-smith.md`（作者）
- **创建新概念页面**：`wiki/concepts/ai-ethics.md`（AI伦理）
- **创建概念页面**：`wiki/concepts/transparency.md`（透明度）
- **创建概念页面**：`wiki/concepts/fairness.md`（公正性）
- **创建概念页面**：`wiki/concepts/accountability.md`（责任）
- **创建概念页面**：`wiki/concepts/privacy.md`（隐私）
- **创建概念页面**：`wiki/concepts/security.md`（安全）

### 2.3 更新索引
更新 `wiki/index.md` 以包含新页面。

### 2.4 更新日志
在 `wiki/log.md` 中添加条目：
```
## [2026-04-21 10:30] ingest | AI伦理原则：确保负责任的人工智能
- 创建源摘要：ai-ethics-principles.md
- 创建实体页面：jane-smith.md
- 创建概念页面：ai-ethics.md, transparency.md, fairness.md, accountability.md, privacy.md, security.md
- 更新wiki索引
```

## 步骤3：添加第二个源文档

添加另一篇关于AI偏见文章：

```
请处理 raw/articles/ai-bias-challenges.md
```

文章内容关于算法偏见和歧视问题。

LLM：
1. 创建源摘要
2. 更新现有页面（`ai-ethics.md`, `fairness.md`）
3. 创建新页面（`wiki/concepts/algorithmic-bias.md`）
4. 记录两个源文档之间的矛盾或补充

## 步骤4：提出问题

询问LLM关于知识库的问题：

```
"AI伦理中的主要挑战有哪些？"
```

LLM搜索wiki页面：
1. 检查 `wiki/index.md` 找到相关页面
2. 读取 `wiki/concepts/ai-ethics.md`, `wiki/concepts/fairness.md`, `wiki/concepts/algorithmic-bias.md`
3. 综合回答，引用相关页面

回答示例：
```
根据知识库，AI伦理的主要挑战包括：

1. **算法偏见**（[[algorithmic-bias]]） - AI系统可能放大社会偏见
2. **透明度缺乏**（[[transparency]]） - 黑箱AI难以解释
3. **责任归属**（[[accountability]]） - 事故责任不明确
4. **隐私侵犯**（[[privacy]]） - 数据收集和使用问题
5. **安全风险**（[[security]]） - AI系统可能被滥用

来源：[[ai-ethics-principles]], [[ai-bias-challenges]]
```

## 步骤5：保存有价值的分析

将回答保存为新页面：

```
请将上面的分析保存为wiki页面。
```

LLM创建 `wiki/comparisons/ai-ethics-challenges.md`：

```yaml
---
id: comparison-ai-ethics-challenges
type: comparison
title: "AI伦理挑战比较分析"
created: 2026-04-21
updated: 2026-04-21
sources:
  - wiki/sources/ai-ethics-principles.md
  - wiki/sources/ai-bias-challenges.md
tags: [ai-ethics, challenges, comparison]
related:
  - wiki/concepts/algorithmic-bias.md
  - wiki/concepts/transparency.md
---
```

## 步骤6：健康检查

运行lint检查：

```
请对wiki进行健康检查。
```

LLM报告：
1. ✅ 所有页面都有正确的frontmatter
2. ✅ 没有断开链接
3. ⚠️  `jane-smith.md` 是孤页（只有出站链接）
4. 🔍 建议：添加更多关于AI安全案例的源文档

## 步骤7：使用Obsidian探索

打开Obsidian：
1. **图形视图**：查看页面之间的关系网络
2. **反向链接**：查看哪些页面链接到 `ai-ethics.md`
3. **标签面板**：查看所有 `ai-ethics` 标签的页面
4. **快速切换**：`Ctrl+O` 快速导航到页面

## 步骤8：搜索内容

使用搜索脚本：

```bash
python scripts/search.py "bias"
```

输出：
```
🔍 搜索 'bias' 的结果 (3个):

1. Algorithmic Bias in AI Systems (相关性: 8.42)
   类型: concept
   摘要: 算法偏见指AI系统在决策过程中...
   链接: [[wiki/concepts/algorithmic-bias]]

2. AI Ethics Principles (相关性: 5.21)
   类型: source
   摘要: 本文讨论了人工智能伦理的五个核心原则...
   链接: [[wiki/sources/ai-ethics-principles]]

3. AI Ethics Challenges Comparison (相关性: 3.15)
   类型: comparison
   摘要: 比较分析AI伦理的主要挑战...
   链接: [[wiki/comparisons/ai-ethics-challenges]]
```

## 步骤9：批量处理

当有多个新文件时：

```bash
bash scripts/batch_ingest.sh
```

列出所有未处理的文件，然后逐一处理。

## 总结

这个工作流展示了：
1. **逐步知识积累**：每个源文档都会丰富wiki
2. **自动维护**：LLM处理交叉引用和更新
3. **复合价值**：查询基于已整合的知识，而非原始文档
4. **持久存储**：所有分析都保存为可浏览的页面

## 实际命令序列

1. `请处理 raw/articles/ai-ethics-principles.md`
2. `请处理 raw/articles/ai-bias-challenges.md`
3. `AI伦理中的主要挑战有哪些？`
4. `请将分析保存为wiki页面`
5. `请对wiki进行健康检查`
6. `python scripts/search.py "transparency"`

---

*这个示例展示了系统的核心功能。根据你的具体领域调整页面类型和分类。*