---
id: wiki-index
type: index
title: "Wiki 索引"
created: 2026-04-21
updated: 2026-04-22
sources: []
tags: []
related: []
status: stable
importance: high
confidence: high
evidence_policy: background-knowledge
---

# Wiki 索引

这里是 `wiki/` 的入口页。`raw/` 保存原始材料，`templates/` 保存页面模板，`wiki/` 保存经过整理后的文献笔记、实体、概念、主题、比较和综合页。

## 文献笔记

- [[hierarchical-whole-brain-modeling-critical-synchronization-2024]] - Myrov 等 2024 年关于人脑临界同步动力学的全脑建模文献笔记。

## 实体

- [[spsnet-reproduction-project]] - Sleep-EDF / SPSNet 睡眠分期复现工程，记录当前实现、实验结果、GraphBlock-lite 问题和下一步路线。

## 主题

当前没有稳定主题页。Sleep staging、PSG 睡眠分期、SNN 睡眠分期和 GraphFC 等主题可从 SPSNet 项目实体页继续抽取。

## 概念

当前概念页仍在重建。建议优先从已整理文献和 curated note 中抽取稳定概念，而不是从零散草稿直接生成。

## 比较

当前没有稳定比较页。

## 综合

当前没有稳定综合页。

## 维护流程

- 修改 `wiki/` 后同步更新本页。
- 修改 `wiki/` 后同步更新 `wiki/log.md`。
- 修改完成后运行 `python scripts/lint_wiki.py`。
