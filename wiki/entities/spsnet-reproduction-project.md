---
id: entity-spsnet-reproduction-project
type: entity
title: "SPSNet 复现工程"
created: 2026-04-22
updated: 2026-04-22
sources:
  - raw/notes/curated/SPSNet 代码项目文档.md
  - raw/notes/curated/Sleep-EDF _ SPSNet 复现项目笔记.md
tags:
  - curated-note
  - spsnet
  - sleep-edf
  - sleep-stage-classification
  - pytorch
  - spiking-neural-network
  - graph-neural-network
  - project-status
related: []
status: stable
importance: high
confidence: medium
evidence_policy: inferred
entity_kind: project
---
jian
# SPSNet 复现工程

## 定位

这是一个围绕 Sleep-EDF 数据集复现 SPSNet 思路的睡眠分期工程。当前目标不是重新写一套项目规则，而是在已有实现和已有笔记框架内，把论文结构、工程实现、实验结果和下一步路线沉淀为可继续执行的项目记录。

原始目标论文是 *SPSNet: A spiking neural network with relation graphs for sleep stage classification based on polysomnography*。项目目前已经完成 Sleep-EDF 单数据集上的预处理、STFT 缓存、数据集窗口、Baseline、BiGRU 融合和 EpochFusion-BiGRU 中间结构；完整 SPSNet 的 SpikeBlock 与稳定 GraphBlock 仍未完成。

## 当前判断

Baseline 是当前最可靠的正式结果；EpochFusion-BiGRU 是最值得继续推进的中间路线；单独调 `bigru_fusion` 收益有限；GraphBlock-lite 已经暴露出分支坍缩问题，下一步应优先修 GraphFC 本体，而不是继续加后端门控。

项目完成度可以分两层看：

- 论文级 SPSNet 复现约 50%：已有 STFT、Frequency Reduction、Attention-BiLSTM、BiGRU 与部分 GraphBlock-lite 试验，缺稳定 GraphBlock 和最小 SpikeBlock。
- Sleep-EDF 单数据集工程约 70%：已有预处理、缓存、可视化、训练脚本、指标输出和若干实验记录。

## 已完成工程

### Sleep-EDF 预处理

已从 PSG 与 Hypnogram 中抽取用于睡眠分期的 epoch 数据。

- 使用通道：`EEG Fpz-Cz`、`EEG Pz-Oz`、`EOG horizontal`
- epoch 长度：`30s`
- 标签集合：`W / N1 / N2 / N3 / REM`
- 输出格式：`npz`
- 相关脚本：`scripts/preprocess_sleepedf.py`、`scripts/check_sleepedf.py`
- 输出目录：`outputs/preprocessed/`
- 数据形状：`X = [num_epochs, num_channels, samples_per_epoch]`，`y = [num_epochs]`

### STFT 缓存

已构建 STFT 缓存，作为后续模型的主要输入。

- 窗口：`2s Hanning window`
- 重叠：`50% overlap`
- FFT 点数：`256`
- 相关脚本：`scripts/build_sleepedf_stft_cache.py`
- 输出目录：`outputs/stft_cache/`
- 示例形状：`S.shape = (2650, 3, 129, 29)`

### 可视化与数据集窗口

已具备基础可视化和序列窗口数据集。

- 可视化脚本：`scripts/visualize_sleepedf.py`、`scripts/visualize_stft_cache.py`
- 数据集文件：`src/datasets/sleepedf_stft_dataset.py`
- 窗口长度：`seq_len = 11`
- 预测目标：中心 epoch 标签
- 单样本形状：`[11, 3, 129, 29]`

## 论文流程映射

论文目标流程可以概括为：

```text
raw PSG
-> 30s epoch
-> STFT
-> Linear Frequency Reduction
-> Attention-BiLSTM
-> SpikeBlock
-> GraphBlock
-> BiGRU
-> center epoch feature
-> FC + Softmax
-> 5 classes
```

当前实现已经对齐的部分包括：

- `30s` epoch
- `W / N1 / N2 / N3 / REM` 五分类
- STFT 参数
- `seq_len = 11`
- 中心 epoch 预测
- Frequency Reduction
- Attention + BiLSTM

尚未稳定对齐的部分包括：

- SpikeBlock
- GraphBlock / GraphFC
- 完整论文级交叉验证与多数据集复现

## 当前模型阶梯

### Baseline

相关文件：

- `src/models/spsnet_baseline.py`
- `train_baseline.py`

结构：

```text
STFT
-> Frequency Reduction
-> Attention + BiLSTM
-> center epoch classifier
```

正式结果：

| 指标 | 数值 |
| --- | ---: |
| best val macro-F1 | 0.6805 |
| test ACC | 0.8717 |
| test macro-F1 | 0.7300 |
| Cohen's kappa | 0.7531 |

判断：Baseline 能正常收敛和泛化，没有明显过拟合。`W` 很强，`N2 / N3 / REM` 可用，`N1` 是主要瓶颈。常见混淆包括 `W -> N1`、`N2 -> N1`、`N2 -> N3`、`N2 -> REM`、`REM -> N2`。

### BiGRU 融合路线

实验结果：

| 设置 | ACC | macro-F1 | kappa |
| --- | ---: | ---: | ---: |
| 48 files / 5 epochs | 0.8093 | 0.6263 | 0.6572 |
| 152 files / 10 epochs | 0.7430 | 0.5519 | 0.5515 |

判断：BiGRU 路线能跑通，但弱于 baseline。问题不应只归因于 BiGRU 参数，而更可能是进入 BiGRU 前的 epoch 表征不够接近论文中的 `B_i`。

### EpochFusion-BiGRU

相关文件：

- `src/models/spsnet_epochfusion_bigru.py`
- `train_epochfusion_bigru.py`

结构：

```text
Frequency Reduction
-> Attention-BiLSTM
-> EpochFusionBlock
-> BiGRU
-> center classifier
```

EpochFusionBlock 是当前对论文中 SpikeBlock / GraphBlock 后段的简化替身：

```text
Conv2D
-> BatchNorm2d
-> AvgPool2d
-> ReLU
-> Flatten
-> Linear / Graph-like FC
```

训练脚本已支持 CUDA、AMP、`weighted_sampler`、`grad_clip`、CLI 参数、`history.json`、`test_metrics.json`、曲线图和 checkpoint。已完成 forward check、tiny overfit、24 files smoke，并在同等配置下明显优于当前 `bigru_fusion`。

代表性中间结果：

| 设置 | ACC | Macro-F1 | Kappa |
| --- | ---: | ---: | ---: |
| 24 files / 3 epochs / eval_subset_size=4000 | 0.8932 | 0.7441 | 0.7916 |

分类别指标：

| 类别 | Precision | Recall | F1 |
| --- | ---: | ---: | ---: |
| W | 0.9993 | 0.9769 | 0.9880 |
| N1 | 0.2131 | 0.8544 | 0.3411 |
| N2 | 0.9737 | 0.6354 | 0.7690 |
| N3 | 0.7653 | 0.9375 | 0.8427 |
| REM | 0.8178 | 0.7449 | 0.7797 |

判断：相比 `bigru_fusion` 的 `Macro-F1 = 0.5916`，EpochFusion-BiGRU 的中间结果有明确提升。但 N1 高召回、低精度，说明模型倾向过度预测 N1，边界仍过宽。

## N1 瓶颈

N1 是过渡睡眠阶段，本身信号弱且形态模糊，常位于 W、N2、REM 的边界。它在数据中占比通常较低，因此对类不平衡、边界样本和损失权重都敏感。

当前 N1 问题不是“完全识别不出来”，而是模型把过多边界 epoch 判成 N1。后续改进应重点关注：

- W/N1/N2 边界样本
- N1 precision 与 recall 的平衡
- 类权重或 sampler 对 N1 过预测的影响
- 序列上下文是否真正帮助中心 epoch 决策

## GraphBlock-lite 诊断

GraphBlock-lite 的目标是把 EpochFusionBlock 末端的普通 `Linear` 升级为 Graph-style GraphFC，使 `B_i` 更接近论文表征。

已验证事实：

- 数据、训练、指标链路本身可用。
- 非 graph 路径能学习。
- graph 路径出现单类坍缩。
- `weighted_sampler` 会加剧问题，但不是根因。
- 仅使用 class weight 仍会坍缩。
- 根因更可能在 graph 分支本体。

当前 graph 路径大致是：

```text
epoch_grids
-> flat_to_graph
-> GraphFC
-> graph_out_proj
-> + sequence_skip
-> LayerNorm
```

已经保留的修正方向：

- 不要把 graph 输入过早压缩到固定 1024。
- 保留 graph branch 与 local linear projection 之间的直接残差。

已经失败的方向：

- terminal hard gating / gated graph branch 导致模型坍缩到 N2。
- 代表结果：`test ACC = 0.0648`，`Macro-F1 = 0.0244`。
- 该路线已经不建议继续。

推荐修复方向：

1. 修 GraphFC 本体：邻接矩阵归一化、固定 WS relation graph、稳定初始化、输出维度对齐 FC baseline。
2. 把 graph 看成 `local -> graph delta` 的小残差，而不是后端融合插件。
3. 不使用 terminal hard gating。
4. 先在 24 files / 3 epochs 小规模上验证不坍缩，再扩大训练。

## 下一步路线

优先级应保持为：

1. 停止继续单独调 `bigru_fusion`。
2. 保留 EpochFusion-BiGRU 作为主线中间模型。
3. 修 GraphFC，使 GraphBlock-lite 不再单类坍缩。
4. 在中等规模数据上验证 graph 版本是否稳定超过非 graph 版本。
5. 再加入最小 SpikeBlock，形成：

```text
Attention-BiLSTM
-> Spike-like conv
-> GraphFC
-> BiGRU
-> center classifier
```

## 可复现实验命令

非 graph 完整运行：

```bash
python train_epochfusion_bigru.py --device cuda --amp --epochs 10 --batch-size 8 --imbalance-mode weighted_sampler --lr 3e-4 --grad-clip 1.0 --cache-mode one --num-workers 4 --pin-memory --persistent-workers --prefetch-factor 2 --save-dir outputs\epochfusion_bigru_runs\full_run
```

非 graph smoke：

```bash
python train_epochfusion_bigru.py --device cuda --amp --epochs 3 --batch-size 8 --imbalance-mode weighted_sampler --lr 3e-4 --grad-clip 1.0 --cache-mode one --num-workers 4 --pin-memory --persistent-workers --prefetch-factor 2 --save-dir outputs\epochfusion_bigru_runs\full_smoke
```

GraphBlock-lite 完整命令：

```bash
python .\train_epochfusion_bigru.py --device cuda --amp --batch-size 16 --epochs 20 --data-dir C:\SAO\SPSNet\outputs\stft_cache --save-dir C:\SAO\SPSNet\outputs\epochfusion_bigru_graph_full --cache-mode all --imbalance-mode weighted_sampler --use-graphblock --graph-num-nodes 32 --graph-k 4 --graph-p 0.1 --graph-self-loop --graph-act relu --graph-dropout 0.0 --graph-alpha-init 0.5 --graph-norm-mode post_add --graph-bypass-mode none
```

## 证据边界

- 本页主要来自两份个人整理笔记，不等同于论文复现实验报告。
- 已列出的指标来自当前项目记录，仍需用固定 split、固定 seed、完整日志和保存的 checkpoint 复核。
- Baseline 结果相对最稳定；EpochFusion-BiGRU 结果是有前景的中间结果；GraphBlock-lite 当前只说明问题定位方向，不能作为有效提升结论。
- 完整 SPSNet 结论需要等待 SpikeBlock、稳定 GraphFC、完整交叉验证和论文指标对照完成后再下判断。
