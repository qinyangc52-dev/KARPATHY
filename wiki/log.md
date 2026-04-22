---
id: wiki-log
type: index
title: "Wiki 维护日志"
created: 2026-04-21
updated: 2026-04-22
sources: []
tags: []
related: []
status: stable
importance: medium
confidence: high
evidence_policy: background-knowledge
---

# Wiki 维护日志

本页记录 wiki 结构、来源处理、页面迁移和 lint 状态的主要变更。

## [2026-04-21] init | 建立知识库框架

- 创建 `raw/`、`wiki/`、`templates/`、`scripts/`。
- 创建基础入口页：`wiki/index.md`、`wiki/log.md`。

## [2026-04-21 20:56] workflow | 增加 PDF 抽取与 wiki lint

- 增加 `scripts/prepare_source.py`，用于将 PDF 等来源抽取到 `raw/extracted/`。
- 增加 `scripts/lint_wiki.py`，用于检查 frontmatter、wiki links 和 source 页面状态。
- 增加 `requirements.txt`。

## [2026-04-22 00:00] ingest | 处理 Myrov 2024 文献

- 将 Myrov 等 2024 年论文放入 `raw/articles/`。
- 将抽取文本与 chunks 写入 `raw/extracted/`。
- 创建文献笔记 `wiki/sources/hierarchical-whole-brain-modeling-critical-synchronization-2024.md`。
- 更新 `wiki/index.md`。

## [2026-04-22] restructure | 调整知识库页面结构

- 根据 `AGENTS.md` 将 wiki 页面按 `sources/`、`entities/`、`concepts/`、`topics/`、`comparisons/`、`synthesis/` 组织。
- 更新模板集合。
- 清理或迁移不稳定页面。

## [2026-04-22] migrate | 迁移 SPSNet 项目笔记

- 输入笔记：`raw/notes/curated/SPSNet 代码项目文档.md`。
- 将 SPSNet 复现内容整理为项目实体页 `wiki/entities/spsnet-reproduction-project.md`。
- 将该页定位为 `entity_kind: project`，避免误放入 `topics/`。
- 更新 `wiki/index.md`。

## [2026-04-22] merge | 合并 Sleep-EDF / SPSNet 复现项目笔记

- 输入笔记：`raw/notes/curated/Sleep-EDF _ SPSNet 复现项目笔记.md`。
- 更新 `wiki/entities/spsnet-reproduction-project.md`，合并 Sleep-EDF 预处理、STFT 缓存、Baseline、BiGRU、EpochFusion-BiGRU、GraphBlock-lite 诊断和下一步路线。
- 重写 `wiki/index.md`，保留当前稳定入口。
- 重写 `wiki/log.md`，修正旧日志中指向 `wiki/topics/spsnet-reproduction-project.md` 的不准确记录。
