# 操作日志

这是知识库的操作记录，按时间顺序排列。每个条目使用标准前缀 `## [YYYY-MM-DD HH:MM] 操作类型 | 描述` 以便于解析。

---

## [2026-04-21] init | 初始化知识库系统
- 创建目录结构：`raw/`, `wiki/`, `templates/`, `scripts/`
- 编写模式文件：`CLAUDE.md`
- 创建初始wiki页面：`index.md`, `log.md`

---

## [2026-04-21 20:56] workflow | 增强PDF和长文摄取流程
- 新增 `scripts/prepare_source.py`，用于PDF文本抽取和长文分块。
- 新增 `scripts/lint_wiki.py`，用于frontmatter和wiki链接健康检查。
- 新增 `requirements.txt`，声明 `PyYAML` 和 `PyMuPDF` 依赖。
- 更新 `CLAUDE.md` 和 `templates/source_summary.md`，加入抽取状态、证据边界和长文分块规则。
- 已处理现有PDF，生成抽取文本和6个chunk，位置在 `raw/extracted/`。
- 将 `wiki/sources/hierarchical-whole-brain-modeling-critical-synchronization-2024.md` 标记为 `needs-verification`，等待基于chunk重新核验。

---

*日志条目由LLM在每次操作后追加。使用 `grep "^## \[" log.md | tail -5` 查看最近5个操作。*
