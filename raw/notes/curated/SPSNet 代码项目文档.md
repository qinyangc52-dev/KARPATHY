# 
> 面向目标：基于论文 **SPSNet: A spiking neural network with relation graphs for sleep stage classification based on polysomnography**，完成一个可训练、可评估、可扩展的 PyTorch 复现工程。
>
> 本文档聚焦 **代码层面的工程设计**，用于指导后续仓库搭建、模块开发、训练调试和实验复现。
>

---

## 1. 项目目标
### 1.1 任务目标
构建一个支持多导 PSG 睡眠分期的深度学习工程，实现以下能力：

1. 支持 UCD、Sleep-EDF Expanded、HMC 三个公开数据集的数据读取与统一预处理；
2. 实现 SPSNet 主干：`STFT -> 频率降维 -> Attention-BiLSTM -> SpikeBlock -> Conv2D -> BN -> AvgPool -> GraphFC/GraphBlock -> BiGRU -> FC`；
3. 支持 5 分类睡眠分期：`W / N1 / N2 / N3 / REM`；
4. 支持 k-fold 训练、验证、测试、混淆矩阵、分类报告、日志记录与模型保存；
5. 支持窗口长度实验、消融实验与后续改进实验。

根据论文，SPSNet 的输入是长度为 `N` 的 30 秒 PSG epoch 序列，采用 STFT、带注意力的 BiLSTM 做 epoch-level 特征提取，在 epoch-level 融合阶段引入 SpikeBlock 和 GraphBlock，然后用 BiGRU 建模跨 epoch 的序列依赖，并输出中间时刻的五分类结果。论文给出的最优序列长度为 `N=11`，训练使用 Adam，训练轮数 50，batch size 64，learning rate 1e-4。论文实验环境为 Python 3.9.19、PyTorch 2.4.0、RTX A5000。来源：论文原文与实验设置。  
参考论文：你上传的 SPSNet 论文。

### 1.2 工程目标
该工程应满足：

+ **可复现**：同一配置下可重复训练；
+ **可维护**：数据、模型、训练、评估分层清晰；
+ **可扩展**：可替换 SpikeBlock、GraphBlock、序列模块；
+ **可审计**：日志、配置、结果、模型权重可追踪。

---

## 2. 建议开发环境
### 2.1 Python 与核心依赖
建议与论文对齐：

+ Python 3.9.x
+ PyTorch 2.4.x
+ NumPy
+ SciPy
+ pandas
+ scikit-learn
+ mne
+ wfdb
+ pyedflib 或 mne.io
+ PyYAML
+ tqdm
+ matplotlib
+ seaborn（仅用于本地调试可视化，不强依赖）

### 2.2 推荐安装方式
```bash
conda create -n spsnet python=3.9 -y
conda activate spsnet
pip install torch torchvision torchaudio
pip install numpy scipy pandas scikit-learn mne wfdb pyedflib pyyaml tqdm matplotlib
```

### 2.3 硬件建议
+ 最低建议：单卡 12GB 显存
+ 推荐：24GB 显存以上
+ HMC 数据集训练耗时显著高于 UCD 和 Sleep-EDF，建议优先在 Sleep-EDF 或 UCD 上跑通流程，再扩展到 HMC

---

## 3. 仓库目录设计
建议目录如下：

```latex
spsnet/
├─ README.md
├─ requirements.txt
├─ configs/
│  ├─ base.yaml
│  ├─ ucd.yaml
│  ├─ sleep_edfx.yaml
│  ├─ hmc.yaml
│  └─ spsnet.example.yaml
├─ data/
│  ├─ raw/
│  │  ├─ ucddb/
│  │  ├─ sleep-edfx/
│  │  └─ hmc-sleep-staging/
│  ├─ interim/
│  └─ processed/
├─ scripts/
│  ├─ download_datasets.sh
│  ├─ preprocess_ucd.py
│  ├─ preprocess_sleep_edfx.py
│  ├─ preprocess_hmc.py
│  ├─ train.py
│  ├─ evaluate.py
│  ├─ run_kfold.py
│  ├─ run_ablation.py
│  └─ run_window_study.py
├─ src/
│  ├─ __init__.py
│  ├─ data/
│  │  ├─ base_dataset.py
│  │  ├─ ucd_dataset.py
│  │  ├─ sleep_edfx_dataset.py
│  │  ├─ hmc_dataset.py
│  │  ├─ transforms.py
│  │  ├─ label_map.py
│  │  └─ split.py
│  ├─ features/
│  │  ├─ stft.py
│  │  ├─ frequency_reduction.py
│  │  └─ sequence_builder.py
│  ├─ models/
│  │  ├─ spsnet.py
│  │  ├─ blocks/
│  │  │  ├─ attention_bilstm.py
│  │  │  ├─ spike_block.py
│  │  │  ├─ lif.py
│  │  │  ├─ graph_block.py
│  │  │  ├─ graph_fc.py
│  │  │  └─ bigru_head.py
│  ├─ trainer/
│  │  ├─ trainer.py
│  │  ├─ losses.py
│  │  ├─ metrics.py
│  │  └─ callbacks.py
│  ├─ utils/
│  │  ├─ io.py
│  │  ├─ seed.py
│  │  ├─ logger.py
│  │  ├─ checkpoint.py
│  │  └─ plot.py
│  └─ experiments/
│     ├─ ablation.py
│     └─ window_length.py
├─ outputs/
│  ├─ logs/
│  ├─ checkpoints/
│  ├─ figures/
│  └─ reports/
└─ tests/
   ├─ test_shapes.py
   ├─ test_labels.py
   ├─ test_stft.py
   └─ test_forward.py
```

---

## 4. 数据接口设计
### 4.1 原始数据统一目标
三个数据集原始格式并不完全一致，但工程内部建议统一成如下结构：

+ 原始 epoch 张量：`[channels, samples_per_epoch]`
+ 序列输入张量：`[sequence_len, channels, samples_per_epoch]`
+ 标签：`int`，取值范围 `0~4`
+ 标签顺序建议固定为：
    - `0: W`
    - `1: N1`
    - `2: N2`
    - `3: N3`
    - `4: REM`

### 4.2 统一样本定义
建议将一个训练样本定义为：

+ 输入：以中间 epoch 为目标的长度为 `N=11` 的滑动窗口序列；
+ 输出：中间 epoch 的类别标签；
+ 边界处理：序列首尾不足 `N` 时，可采用镜像填充、重复填充或直接丢弃；工程第一版建议直接丢弃，逻辑最清晰。

### 4.3 数据类返回格式
建议 `__getitem__` 返回：

```python
{
    "x": Tensor[sequence_len, channels, samples_per_epoch],
    "y": Tensor[],
    "subject_id": str,
    "epoch_index": int,
    "dataset_name": str,
}
```

---

## 5. 数据预处理规范
### 5.1 通用流程
1. 读取 EDF/REC 与标注文件；
2. 选取论文指定通道；
3. 统一采样率；
4. 切分为 30 秒 epoch；
5. 对齐标注；
6. 去除无效标注；
7. 映射为五分类标签；
8. 存储为中间格式（推荐 `.npz` / `.pt` / parquet + 索引）。

### 5.2 标签清洗规则
论文说明：为实现五分类，移除无效标签，并将 S3 和 S4 合并为 N3。  
工程统一规则建议：

+ `W -> 0`
+ `N1 / Stage 1 -> 1`
+ `N2 / Stage 2 -> 2`
+ `N3 / Stage 3 / Stage 4 -> 3`
+ `REM / R -> 4`
+ `UNKNOWN / MOVEMENT / ARTIFACT / INDETERMINATE / ? -> ignore`

### 5.3 STFT 规范
论文在每个 epoch 上做 STFT，参数为：

+ Hanning window：2 秒
+ overlap：50%
+ FFT points：256

实现建议：

+ 输入长度 `samples_per_epoch = fs * 30`
+ 对每个 channel 单独做 STFT
+ 输出谱图张量形状建议为 `[channels, freq_bins, time_steps]`
+ 后续再进入频率降维模块

---

## 6. 模型实现设计
## 6.1 总体前向流程
建议在 `src/models/spsnet.py` 中实现主类 `SPSNet(nn.Module)`。

逻辑分为三段：

### 第一段：Epoch-level 特征提取
对序列中每个 epoch：

1. STFT
2. 线性频率降维
3. 单通道谱图送入 Attention-BiLSTM
4. 输出 attention-fused matrix

### 第二段：Epoch-level 多通道融合
对每个 epoch 的 attention matrix：

1. SConv2D / SpikeBlock
2. Conv2D
3. BN2D
4. AvgPool2D
5. ReLU
6. Flatten
7. GraphFC / GraphBlock

### 第三段：Sequence-level 建模与分类
1. 将所有 epoch 的融合特征组成序列
2. 送入 BiGRU
3. 取中间时刻特征
4. 全连接分类
5. Softmax 或 logits 输出

---

## 6.2 关键模块说明
### 6.2.1 Attention-BiLSTM
建议接口：

```python
class AttentionBiLSTM(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int):
        ...

    def forward(self, x):
        # x: [channels, freq_bins_reduced, time_steps] 或 [B, channels, freq_bins_reduced, time_steps]
        # return: [channels, 2 * hidden_dim]
        ...
```

实现要点：

+ 对每个 channel 的频谱序列做 BiLSTM；
+ 时间维上做注意力加权汇聚；
+ 输出每个 channel 一个融合向量；
+ 最终形成 `[channels, 2h]` 的 attention matrix。

### 6.2.2 SpikeBlock
作用：在卷积前引入脉冲神经元的时间窗演化、阈值发放与膜电位衰减。

建议拆成两个层次：

1. `LIFNeuron`
2. `SpikingConv2dBlock`

建议接口：

```python
class LIFNeuron(nn.Module):
    def __init__(self, threshold=0.5, decay=0.2):
        ...

    def forward(self, input_current, mem):
        ...
        return spike, new_mem
```

```python
class SpikeBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, time_window, threshold, decay):
        ...

    def forward(self, x):
        # x: [B, 1, C, 2h] 或类似格式
        ...
        return y
```

第一版工程建议：

+ 先实现“可运行版本”，即使用时间窗循环 + LIF 更新；
+ 确保 shape 正确、梯度可传；
+ 后续再优化为更严格的脉冲编码策略。

### 6.2.3 GraphBlock / GraphFC
论文将 Watts–Strogatz 小世界网络转化为 relation graph，并用于 GraphFC 层。第一版工程建议把它实现为：

1. 生成固定 relation graph 邻接矩阵；
2. 对 flatten 后特征做图传播；
3. 输出图增强后的特征表示。

建议接口：

```python
class GraphBlock(nn.Module):
    def __init__(self, in_features, out_features, num_nodes=128, reconnect_prob=0.2):
        ...

    def forward(self, x):
        # x: [B, F]
        ...
        return y
```

工程化建议：

+ 使用 `networkx.watts_strogatz_graph` 生成图；
+ 构造归一化邻接矩阵；
+ 实现一层简单图传播：`A_hat @ X @ W` 或 relation-aware MLP；
+ 如论文实现细节不完全公开，第一版把 GraphFC 定义为“带固定 relation adjacency 的图线性层”，并在文档中注明“工程近似实现”。

### 6.2.4 BiGRU 分类头
建议接口：

```python
class BiGRUHead(nn.Module):
    def __init__(self, input_size, hidden_size=64, num_layers=1, dropout=0.6):
        ...

    def forward(self, x):
        # x: [B, N, F]
        ...
        return logits
```

---

## 7. 张量形状约定
为避免调试混乱，建议在代码中写死 shape 注释。

### 7.1 原始输入
```latex
x_raw: [B, N, C, K]
B: batch_size
N: sequence_len
C: channels
K: samples_per_epoch = fs * 30
```

### 7.2 单个 epoch 的 STFT 输出
```latex
x_stft: [B, N, C, F, T]
```

### 7.3 频率降维后
```latex
x_red: [B, N, C, h, T]
```

### 7.4 Attention-BiLSTM 输出
```latex
x_attn: [B, N, C, 2h]
```

### 7.5 SpikeBlock / Conv2D 后
```latex
x_fused_epoch: [B, N, F_epoch]
```

### 7.6 BiGRU 输出
```latex
x_seq: [B, N, 2H]
mid = x_seq[:, N // 2, :]
logits: [B, 5]
```

---

## 8. 配置管理规范
建议所有超参数写入 YAML，不要散落在脚本里。

### 8.1 核心配置项
```yaml
dataset:
  name: sleep_edfx
  root: ./data/raw/sleep-edfx
  sequence_len: 11
  target_fs: 100
  epoch_seconds: 30
  num_classes: 5

preprocess:
  stft_window_seconds: 2
  stft_overlap: 0.5
  n_fft: 256
  save_intermediate: true

model:
  hidden_dim: 64
  bigru_hidden: 64
  bigru_layers: 1
  conv_filters: 12
  conv_kernel: 9
  conv_stride: 1
  pool_kernel: 5
  pool_stride: 4
  spike_time_window: 20
  spike_threshold: 0.5
  spike_decay: 0.2
  graph_nodes: 128
  graph_reconnect_prob: 0.2
  dropout: 0.6

train:
  epochs: 50
  batch_size: 64
  lr: 0.0001
  weight_decay: 0.0
  num_workers: 4
  seed: 42

experiment:
  output_dir: ./outputs
  save_every: 1
  monitor: mf1
```

---

## 9. 训练流程设计
### 9.1 主训练入口
建议统一入口：

```bash
python scripts/train.py --config configs/sleep_edfx.yaml
```

### 9.2 训练循环职责
`Trainer` 负责：

+ 前向传播
+ loss 计算
+ 反向传播
+ 梯度裁剪（可选）
+ 验证集评估
+ 模型保存
+ 日志输出

### 9.3 推荐日志内容
每轮至少记录：

+ train loss
+ val loss
+ ACC
+ Macro-F1
+ Cohen’s Kappa
+ 每类 precision / recall / f1（可选）
+ best epoch

### 9.4 推荐 checkpoint 内容
```python
{
    "epoch": epoch,
    "model_state_dict": model.state_dict(),
    "optimizer_state_dict": optimizer.state_dict(),
    "config": config,
    "metrics": metrics,
}
```

---

## 10. 评估与实验设计
### 10.1 主实验
按论文设置：

+ UCD：5-fold
+ Sleep-EDF-78：10-fold
+ HMC：10-fold

最终汇总：

+ ACC
+ Macro-F1
+ Cohen’s Kappa

### 10.2 消融实验
至少实现三组：

1. 去掉 SpikeBlock：以普通 Conv2D 替代
2. 去掉 GraphBlock：以普通 FC 替代
3. 去掉 BiGRU：只用 epoch 融合后的中间特征分类

### 10.3 窗口长度实验
Hanning 窗长测试：

+ 1 秒
+ 2 秒
+ 3 秒

### 10.4 可视化输出
建议保存：

+ confusion matrix
+ 每折结果表
+ 整体平均结果表
+ training curve
+ learning rate curve（可选）

---

## 11. 开发优先级与里程碑
### 里程碑 M1：数据通路打通
+ 能读取一个数据集的一条记录
+ 能切 30 秒 epoch
+ 能对齐标签
+ 能得到训练样本 `[N, C, K]`

### 里程碑 M2：主干模型跑通
+ STFT 正常
+ Attention-BiLSTM 正常
+ SpikeBlock / GraphBlock 可前向
+ 能完成一次 forward + backward

### 里程碑 M3：单数据集训练
+ 在 Sleep-EDF 上跑通单 fold
+ 输出 ACC / MF1 / Kappa
+ 生成混淆矩阵

### 里程碑 M4：k-fold 与完整实验
+ 跑通论文对应数据集划分
+ 汇总主结果
+ 补充消融实验

### 里程碑 M5：工程固化
+ 配置文件整理
+ README 完成
+ 脚本参数规范化
+ 结果目录结构固定

---

## 12. 风险点与实现建议
### 12.1 SpikeBlock 细节可能不完全公开
建议采取“功能近似 + 文档透明”的实现策略：

+ 第一版先实现 LIF + 时间窗卷积
+ 所有近似点在 README 和实验报告中说明
+ 保持接口可替换，便于后续迭代

### 12.2 GraphBlock 细节可能存在实现歧义
建议：

+ 固定 graph 生成方式与随机种子
+ 将 graph adjacency 保存到输出目录
+ 在训练日志中记录 graph 参数

### 12.3 数据集标签规范不完全一致
建议：

+ 每个数据集单独写 `label_map`
+ 最终统一到五分类
+ 在预处理阶段生成标签统计表，避免错映射

### 12.4 多数据集采样率不同
建议：

+ 保持“原始采样率读取 + 目标采样率重采样”的清晰路径
+ 不要在 Dataset 类中临时重采样，优先离线预处理

---

## 13. 测试规范
至少编写以下单元测试：

### 13.1 数据测试
+ 标签映射是否正确
+ epoch 数量与标签数量是否一致
+ 读取样本 shape 是否符合约定

### 13.2 特征测试
+ STFT 输出 shape 是否正确
+ 频率降维后维度是否正确

### 13.3 模型测试
+ 单 batch forward 不报错
+ loss.backward() 不报错
+ 输出 logits shape 是否为 `[B, 5]`

### 13.4 稳定性测试
+ 固定 seed 后，首轮指标是否基本一致

---

## 14. 代码风格建议
+ 每个模块顶部写输入输出 shape
+ 所有 magic number 进入配置文件
+ 不要在训练脚本中写数据处理逻辑
+ 不要在 Dataset 中写过多业务逻辑
+ 每个实验必须保存配置快照
+ 每次训练生成独立输出目录

建议函数风格：

+ 单函数单职责
+ 配置对象统一传递
+ 日志统一使用一个 logger
+ 异常尽量在数据预处理阶段暴露

---

## 15. 第一版最小可用实现建议
如果你现在就要开始写代码，建议按下面顺序推进：

1. **先做 Sleep-EDF**：格式清晰，采样率统一，适合先跑通；
2. **先不做严格 Spike 编码优化**：先让 LIF + 卷积结构可运行；
3. **GraphBlock 先做固定图传播**：后续再逼近论文细节；
4. **先完成单 fold**，再扩展到 k-fold；
5. **先实现主实验**，再做消融和窗口长度实验。

---

## 16. 建议交付文件
仓库第一阶段建议至少包含：

+ `README.md`
+ `configs/spsnet.example.yaml`
+ `scripts/download_datasets.sh`
+ `scripts/preprocess_*.py`
+ `scripts/train.py`
+ `src/models/spsnet.py`
+ `src/data/*.py`
+ `src/trainer/*.py`
+ `outputs/reports/复现日志.md`

---

## 17. 结论
这份文档的目的不是替代代码，而是让你在开始实现前把工程边界、模块职责、输入输出、目录结构和训练流程先固定下来。对于 SPSNet 这种同时包含 **SNN、relation graph、时频分析、序列建模** 的模型，前期把工程设计写清楚，后面写代码会快很多，也更不容易陷入 shape 错误和数据错配。

你下一步最适合直接开始的工作是：

1. 先执行数据下载；
2. 先写 `Sleep-EDF` 的预处理；
3. 再写 `SPSNet` 的最小可运行版本；
4. 用单折训练验证整个工程链路。

