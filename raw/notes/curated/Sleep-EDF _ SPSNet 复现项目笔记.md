# SPSNet 复现与论文理解整理
## 1. 文档目的
本文档用于系统整理当前 **Sleep-EDF / SPSNet** 复现项目的核心内容，包括：

+ 项目目标与当前完成情况
+ 论文原始方法主线
+ 当前实现版本与论文的对应关系
+ Baseline / BiGRU / EpochFusion / GraphBlock-lite 的实验结论
+ Graph 分支当前暴露的问题与修复思路
+ 对论文中各个模块（Attention、BiLSTM、SNN、GraphFC、BiGRU、Conv2D、BN、Pool、ReLU、Flatten 等）的直观解释
+ 当前推荐路线与下一步工作建议

---

## 2. 项目背景与目标
本项目以 **Sleep-EDF** 数据集为基础，按照论文 **SPSNet: A spiking neural network with relation graphs for sleep stage classification based on polysomnography** 的整体思路，逐步完成睡眠分期系统的复现。

当前目标分为三个层次：

1. 完成 **数据预处理 + STFT + 序列样本构造**
2. 完成 **论文前半段 baseline**
3. 逐步逼近论文完整结构：
    - SpikeBlock
    - GraphBlock
    - BiGRU
    - 完整实验协议

---

## 3. 当前已完成的部分
### 3.1 数据预处理
已经完成从原始 EDF 到训练输入的基础处理流程。

已实现内容：

+ 读取 PSG 与 Hypnogram
+ 默认选择通道：
    - `EEG Fpz-Cz`
    - `EEG Pz-Oz`
    - `EOG horizontal`
+ 按 `30s` 切分 epoch
+ 标签映射为五分类：
    - `W`
    - `N1`
    - `N2`
    - `N3`
    - `REM`
+ 保存为 `npz`

相关脚本：

+ `scripts/preprocess_sleepedf.py`
+ `scripts/check_sleepedf.py`

输出目录：

+ `outputs/preprocessed/`

输出形式：

+ `X.shape = [num_epochs, num_channels, samples_per_epoch]`
+ `y.shape = [num_epochs]`

### 3.2 STFT 特征缓存
已经完成 STFT 特征提取，并将结果统一缓存，避免每次训练时重复计算。

STFT 参数：

+ `2s Hanning window`
+ `50% overlap`
+ `256 FFT`

相关脚本：

+ `scripts/build_sleepedf_stft_cache.py`

输出目录：

+ `outputs/stft_cache/`

单个样本示例：

+ `S.shape = (2650, 3, 129, 29)`

含义：

+ `2650`：该整晚样本的 epoch 数
+ `3`：通道数
+ `129`：频率维
+ `29`：时间维

### 3.3 可视化
已经完成原始信号和 STFT 结果的可视化。

相关脚本：

+ `scripts/visualize_sleepedf.py`
+ `scripts/visualize_stft_cache.py`

可视化内容：

+ 原始 PSG
+ hypnogram 标注
+ 指定 epoch / channel 的 STFT 热力图
+ 原始波形与 STFT 对照图

### 3.4 数据集与滑动窗口构造
已经实现基于 `stft_cache` 构造训练样本。

数据集文件：

+ `src/datasets/sleepedf_stft_dataset.py`

当前样本构造方式：

+ `seq_len = 11`
+ 每个训练样本由连续 `11` 个 epoch 构成
+ 标签取窗口中心 epoch 的标签

即：

+ 输入：`[t-5, ..., t, ..., t+5]`
+ 输出：中心 `t` 的标签

单个样本输入 shape：

+ `[11, 3, 129, 29]`

---

## 4. 论文方法主线
论文 **SPSNet** 的整体结构可以概括为：

```latex
原始 PSG
-> 30s epoch
-> STFT
-> Linear Frequency Reduction
-> Attention-BiLSTM
-> SpikeBlock
-> GraphBlock
-> BiGRU
-> 取中心时刻特征
-> FC + Softmax
-> 5类分类
```

更细化的 epoch-level 到 sequence-level 主线为：

```latex
STFT
-> Linear Frequency Reduction
-> Attention-BiLSTM   得到 A_i
-> SConv2D            (SpikeBlock)
-> Conv2D
-> BN2D
-> AvgPool2D
-> ReLU
-> Flatten
-> GraphFC            (GraphBlock) 得到 B_i
-> BiGRU              建模 {B_1 ... B_N}
-> 取中心时刻特征
-> FC + Softmax
```

---

## 5. 当前与论文一致的部分
当前已经和论文一致或基本一致的内容：

1. `30s` epoch 切分
2. 五分类标签：`W / N1 / N2 / N3 / REM`
3. STFT 主参数：
    - `2s Hanning`
    - `50% overlap`
    - `256 FFT`
4. `seq_len = 11`
5. 预测中心 epoch 标签
6. Frequency Reduction
7. Attention + BiLSTM

因此，目前已经完成了论文前半段的主要基础链路。

---

## 6. 当前 Baseline 模型
### 6.1 结构
相关文件：

+ `src/models/spsnet_baseline.py`
+ `train_baseline.py`

结构：

```latex
STFT
-> Frequency Reduction
-> Attention + BiLSTM
-> 中心 epoch 分类
```

### 6.2 各部分作用
#### Frequency Reduction
作用：

+ 对 STFT 的频率维做线性降维
+ 压缩频率维度
+ 保留更重要的频带信息
+ 降低后续训练难度

本质：

把较高维的 STFT 频率表示压缩成更紧凑、更有判别力的频率特征。

#### Attention + BiLSTM
作用：

+ 建模 **单个 epoch 内部** 的时序变化
+ BiLSTM 负责看时间维上的前后依赖
+ Attention 负责选择更重要的时间帧

本质：

从单个 30s epoch 内部的时频变化中提取关键局部特征。

注意：

这一步仍属于 **epoch-level** 特征提取。

#### 中心 epoch 分类
当前训练样本不是单个 epoch，而是连续 11 个 epoch 的窗口。

但是模型最终不是给整个窗口一个标签，而是只预测中间那个 epoch 的标签。

目的：

+ 前后 epoch 提供上下文
+ 中间 epoch 才是真正要分类的对象

### 6.3 Baseline 正式实验结果
当前正式 baseline 结果：

+ 最优验证集 `macro-F1 = 0.6805`
+ 测试集：
    - `ACC = 0.8717`
    - `macro-F1 = 0.7300`
    - `Cohen’s kappa = 0.7531`

当前 baseline 结论：

+ 收敛正常
+ 泛化正常
+ 无明显过拟合
+ `W` 很强
+ `N2 / N3 / REM` 已经可用
+ `N1` 是当前最大短板

主要错分方向：

+ `W -> N1`
+ `N2 -> N1`
+ `N2 -> N3`
+ `N2 -> REM`
+ `REM -> N2`

说明：

当前 baseline 已经跑通，接下来优化重点不再是“能不能训练”，而是“如何改善阶段边界，尤其是 N1”。

---

## 7. 为什么论文在 BiLSTM 后面还接 BiGRU
论文中：

+ `BiLSTM` 负责 **epoch 内部** 的时序建模
+ `BiGRU` 负责 **多个 epoch 之间** 的 sequence-level 建模

所以这不是重复，而是两层时序建模：

1. **epoch-level temporal modeling**
2. **sequence-level temporal modeling**

也就是说：

+ BiLSTM：看一个 30s epoch 里面的时间变化
+ BiGRU：看多个 epoch 连起来的上下文，再判断中心那个 epoch 的类别

---

## 8. 当前 BiGRU 路线的实验结论
### 8.1 bigru_fusion 路线
已知阶段性结果：

+ `48 文件 / 5 epoch`
    - `ACC = 0.8093`
    - `macro-F1 = 0.6263`
    - `kappa = 0.6572`
+ `全量 152 文件 / 10 epoch`
    - `ACC = 0.7430`
    - `macro-F1 = 0.5519`
    - `kappa = 0.5515`

结论：

+ 能稳定训练
+ 不塌缩
+ 说明 sequence-level 建模这条路线是对的
+ 但明显弱于 baseline
+ 当前 bigru_fusion 形式已经接近能力平台

### 8.2 关键判断
+ baseline 仍然是当前最强正式对照组
+ 问题不在“BiGRU 能不能训练”
+ 更可能的问题在于：
    - **BiGRU 前的 epoch 表示还不够“论文式”**

因此，不建议继续只调 bigru_fusion 的超参数去“硬拗提升”。

---

## 9. 推荐的过渡版本：EpochFusionBlock
最推荐的下一步是：

```latex
Attention-BiLSTM
-> EpochFusionBlock
-> BiGRU
-> 分类
```

其中 EpochFusionBlock 暂时不做完整 SpikeBlock / GraphBlock，而先做论文风格更强的简化版：

```latex
Conv2D
BN
AvgPool
ReLU
Flatten
Linear / Graph-like FC
```

目的：

+ 先把 BiGRU 前的 epoch 表示做得更像论文中的 `B_i`
+ 再看 sequence-level 模型能否继续提升

这也是当前中间版本的核心出发点。

---

## 10. 当前中间版本的完成状态
当前中间版本已完成：

+ 新模型文件：`src/models/spsnet_epochfusion_bigru.py`
+ 新训练脚本：`train_epochfusion_bigru.py`

模型结构已完成：

+ FrequencyReduction
+ Attention-BiLSTM
+ EpochFusionBlock：
    - `Conv2D + BatchNorm2d + AvgPool2d + ReLU + Flatten + Linear`
    - 后续尝试扩展到 `Graph-like FC / GraphBlock-lite`
+ BiGRU
+ 中心 epoch 分类头

训练链路已完成：

+ 支持 CUDA
+ 支持 AMP
+ 支持 weighted_sampler
+ 支持 grad_clip
+ 支持大部分 CLI 参数
+ 输出：
    - `history.json`
    - `test_metrics.json`
    - `history_curves.png`
    - 最优 checkpoint

验证已完成：

+ 最小 forward check 已通过
+ tiny overfit 已跑通
+ 24 files 中等规模 smoke 已跑通
+ 同配置下明显优于当前 bigru_fusion

仍未完成：

+ 完整 SpikeBlock
+ 完整 GraphBlock
+ SNN / 脉冲编码
+ 完整 SPSNet
+ 论文级 cross-validation
+ 正式 README / 配置说明 / 推理脚本 / 文档体系

---

## 11. 中间版本的代表性结果
推荐关注 `24 files / 3 epochs / eval_subset_size=4000` 这组结果，因为它比 tiny overfit 更接近真实训练表现。

整体指标：

+ `ACC = 0.8932`
+ `Macro-F1 = 0.7441`
+ `Cohen's Kappa = 0.7916`

各类别测试集指标如下：

| 类别 | Precision | Recall | F1 |
| --- | ---: | ---: | ---: |
| W | 0.9993 | 0.9769 | 0.9880 |
| N1 | 0.2131 | 0.8544 | 0.3411 |
| N2 | 0.9737 | 0.6354 | 0.7690 |
| N3 | 0.7653 | 0.9375 | 0.8427 |
| REM | 0.8178 | 0.7449 | 0.7797 |


解读：

+ `W` 很强，已经接近饱和
+ `N3` 和 `REM` 表现不错
+ `N2` precision 很高，但 recall 偏低，说明漏检还比较多
+ `N1` 仍然是最弱类，当前是高 recall、低 precision，说明模型会把一部分别的阶段打成 N1

同配置下，对照版 `bigru_fusion` 的 test `Macro-F1 = 0.5916`，这版提升比较明显。

---

## 12. N1 为什么那么差
当前 N1 差，不是你这版模型独有的问题，而是睡眠分期里的典型难点，论文也明确提到了。

### 12.1 论文中的原因
1. **N1 本身就是过渡期**
    - 位于 `W` 和 `N2` 之间
    - 特征边界模糊
    - 很容易和相邻阶段混淆
2. **N1 的信号特征不够“显眼”**
    - 处于 `α 波 -> θ 波` 的过渡期
    - 振幅较低
    - 缺少高对比度的典型波形
3. **类别不平衡**
    - N1 样本占比通常只有 `5%~10%`
    - 明显少于其他阶段
    - 模型更难学到稳定边界

### 12.2 你当前结果的具体含义
你当前 N1 的表现是：

+ `Precision = 0.2131`
+ `Recall = 0.8544`
+ `F1 = 0.3411`

这说明：

+ 真正的 N1 抓到了不少
+ 但是模型把很多非 N1 也打成了 N1
+ 本质上是 **N1 判定边界太宽了，出现明显的过预测**

所以当前 N1 差，不是“完全学不到 N1”，而是：

**W / N1 / N2 的过渡边界学得太松。**

---

## 13. GraphBlock-lite 当前状态与问题
### 13.1 GraphBlock-lite 的意图
GraphBlock-lite 的目标不是完整复刻论文 GraphBlock，而是：

+ 在当前中间版本中，把 `EpochFusionBlock` 末端的普通 `Linear` 升级成 Graph 风格的 `GraphFC`
+ 让 `B_i` 更接近论文风格
+ 保持输出维度与原 FC 基线一致，便于公平消融

### 13.2 已验证的事实
当前已经确认：

+ 数据集没有坏
+ 训练脚本主流程没有坏
+ 指标计算没有坏
+ `non-graph` 版本能正常学起来
+ `graph` 版本一开启就容易塌缩成单类预测
+ `weighted_sampler` 会加重问题，但不是根因
+ 改成 `class_weight` 后 graph 还是塌缩

因此目前的结论是：

**问题在 graph 分支本身，而不在数据、训练主流程或评估计算。**

### 13.3 当前可疑路径
当前 graph 分支可以概括为：

```latex
epoch_grids
-> flat_to_graph
-> GraphFC
-> graph_out_proj
-> + sequence_skip
-> LayerNorm
```

从现象看：

+ graph 头输出没有提供有效判别信息
+ 训练后会直接塌到单类
+ weighted_sampler 会加重问题，但不是根因

### 13.4 已有修复尝试
#### 第一轮有效修复
当前保留的修复包括：

+ 默认不再把 graph 输入过度压缩到固定 `1024` 维
+ 保留 graph 分支和局部线性投影的直接残差相加

这版虽然还没完全稳定，但至少已经修掉了最初“图分支明显失效/直接塌缩”的实现错误。

#### 第二轮失败修复
第二轮尝试过“门控压图分支”的方案，但结果更差：

+ 再次单类塌缩
+ 并且偏到 `N2`
+ 测试集 `ACC = 0.0648`
+ `Macro-F1 = 0.0244`

结论：

+ 末端强门控在当前结构下不是稳定化
+ 反而在破坏主干可学习性
+ 因此这轮改动已经回退

### 13.5 当前最推荐的修复方向
不再继续折腾末端门控，而是回到更贴论文的修正路线：

1. **优先修改 GraphFC 本体**
    - 邻接归一化
    - 固定 WS relation graph
    - 更稳的权重初始化
    - 输出维度严格对齐原 FC 基线
2. **保留轻量残差，但变成小扰动**
    - local -> graph delta
    - graph 分支只做小修正，不直接重写主干表征
3. **不要把 GraphFC 当成后挂的融合器**
    - GraphFC 应该是 epoch-level FC 的图结构版本
    - 不是融合末端再挂一个门控器

---

## 14. Graph 与论文的关系：你现在做到哪一步了
当前你做的，不是论文完整 SPSNet，而是：

```latex
STFT
-> Frequency Reduction
-> Attention + BiLSTM
-> Graph-like FC / GraphBlock-lite
-> BiGRU / 分类
```

这意味着：

+ 已经有 `Attention + BiLSTM`
+ 正在尝试 `graph` 分支
+ **还没有真正上论文里的 SNN / SpikeBlock**

也就是说，你现在做的是：

**论文前半段 + Graph-like FC 过渡版**

而不是：

**完整 SpikeBlock + GraphBlock + BiGRU 的 SPSNet**

---

## 15. 为什么论文要加 SNN，不只用图网络
论文不是“Attention-BiLSTM 后直接分类”，也不是“Attention-BiLSTM 后只接图网络分类”，而是：

```latex
Attention-BiLSTM
-> SpikeBlock
-> GraphBlock
-> BiGRU
-> 分类
```

原因是三个模块的职责不同：

### 15.1 Attention + BiLSTM
负责：

+ 单个 epoch 内部的时序建模
+ 从时频序列中提取注意力增强后的初始表示 `A_i`

### 15.2 SpikeBlock / SNN
负责：

+ 用脉冲机制做局部动态变换
+ 让 epoch-level 融合更接近生物神经元的工作方式
+ 利用 SNN 的稀疏、低功耗、生物可解释性

### 15.3 GraphBlock / GraphFC
负责：

+ 在单个 epoch 内，对不同通道 / 节点之间的关系做结构化建模
+ 增强“神经元之间的通信”
+ 完成 relation graph 下的消息传递和融合

### 15.4 BiGRU
负责：

+ 建模多个 epoch 之间的 sequence-level 依赖
+ 利用前后上下文来决定中心 epoch 的类别

一句话概括：

+ `Attention + BiLSTM`：看一个 epoch 内部发生了什么
+ `SpikeBlock`：用脉冲机制做局部动态融合
+ `GraphBlock`：看这个 epoch 内不同通道/节点之间怎么相互关联
+ `BiGRU`：看多个 epoch 连起来，当前这个 epoch 应该判成什么阶段

---

## 16. 从 A_i 到 B_i 的直观流程图
### 16.1 论文版
```latex
单个 epoch 的注意力输出
A_i ∈ R^(C × 2h)
│
├─ 1) SConv2D   （SpikeBlock）
│      作用：用 SNN 的脉冲卷积先做一次局部变换
│      输出：脉冲机制增强后的局部特征图
│
├─ 2) Conv2D
│      作用：继续提炼局部时频/跨通道模式
│      输出：更稳定的卷积特征图
│
├─ 3) BN2D
│      作用：稳定特征分布，便于训练
│      输出：数值更平稳的特征图
│
├─ 4) AvgPool2D
│      作用：压缩尺寸、降噪、保留整体趋势
│      输出：更紧凑的特征图
│
├─ 5) ReLU
│      作用：加入非线性，增强表达能力
│      输出：非线性激活后的特征图
│
├─ 6) Flatten
│      作用：把二维特征图摊平成向量/节点表示
│      输出：一维特征表示
│
└─ 7) GraphFC   （GraphBlock）
       作用：按 relation graph 做节点间消息传递与融合
       输出：B_i（更稳定、更“论文式”的 epoch 表示）
```

### 16.2 当前过渡版
```latex
A_i
│
├─ Conv2D
├─ BN
├─ AvgPool
├─ ReLU
├─ Flatten
└─ Linear / Graph-like FC
    ↓
   B_i（过渡版）
```

你的当前版本本质上就是：

**先做一个更像论文的 EpochFusionBlock，再把它接到 BiGRU 前面。**

---

## 17. 论文里这些基础模块分别是什么意思
### 17.1 普通卷积（Conv2D）
作用：

+ 用局部窗口在二维特征图上滑动
+ 提取局部时频块的组合模式
+ 在时频图里可理解为抓取局部时间-频率联合模式

在论文里：

+ `SConv2D` 更偏向脉冲机制下的局部变换
+ `Conv2D` 更偏向把这些局部响应再整理成更稳定的局部模式

### 17.2 注意力融合项（Attention 输出）
作用：

+ BiLSTM 先编码 epoch 内部序列
+ Attention 再给不同时间帧分配不同权重
+ 强调更重要的时间片段

得到的就是初始 epoch 表示 `A_i`。

### 17.3 为什么要转成 SNN
论文引入 SNN 的原因：

+ 脉冲通信天然更稀疏、低功耗
+ LIF 神经元更接近生物神经元的工作方式
+ 作者希望引入更强的生物合理性与生物可解释性
+ 对 EEG/EOG/ECG 这类生物时序信号，作者认为 SNN 更有潜力

### 17.4 为什么不是 EI 平衡网络
论文没有讨论 EI（兴奋-抑制）平衡网络。

更合理的工程推断是：

+ 这篇论文目标是做一个能和 STFT、BiLSTM、卷积、图结构、BiGRU 顺畅拼接的睡眠分期模型
+ LIF + SConv2D 已经足以提供“更像生物”的特性
+ 若改成显式 EI 平衡网络，通常需要额外设计兴奋/抑制神经元分群、连接符号约束、平衡机制与训练稳定性，工程复杂度会显著增加

### 17.5 二维批归一化（BN2D）
作用：

+ 对一个 batch 内二维特征图的通道分布做标准化
+ 稳定数值范围
+ 减少分布漂移
+ 让训练更稳、更容易收敛

### 17.6 平均池化（AvgPool2D）
作用：

+ 压缩特征尺寸
+ 降低参数量
+ 减少细碎局部波动
+ 保留整体趋势

### 17.7 ReLU 非线性激活
作用：

+ 给网络加入非线性
+ 增强表达能力
+ 让网络能表示更复杂的模式
+ 计算简单，训练稳定

### 17.8 Flatten
作用：

+ 把二维特征图摊平成向量或节点表示
+ 为后续 GraphFC / FC 提供输入格式

一句话概括：

**SConv2D 和 Conv2D 先把局部特征做出来，BN/Pool/ReLU 把它变稳、变紧凑，Flatten 把它整理成向量，GraphFC 再在这些特征之间做关系建模，最终形成适合 BiGRU 使用的 **`B_i`**。**

---

## 18. 当前完成度判断
如果按 **论文完整复现** 来算：

+ 你当前完成的是论文前半段基础工程 + 过渡版本验证
+ 还没有进入完整 SPSNet 闭环

一个比较保守的完成度估计：

+ **约 50% 左右**

因为：

+ 前处理、STFT、滑动窗口、Baseline、BiGRU 路线、中间版 EpochFusionBlock 都已完成
+ 但完整论文里最核心的两个增量模块：
    - SpikeBlock
    - GraphBlock  
仍未真正稳定落地
+ 论文级 cross-validation 也未完成

如果按 **单数据集工程推进** 来算：

+ 你已经完成了大部分基础工程链路
+ 处于从“论文前半段”走向“核心模块复现”的阶段

一个更宽松的完成度估计：

+ **约 70% 左右**

---

## 19. 当前最推荐的下一步
### 19.1 不要继续只调 bigru_fusion 超参
原因：

+ bigru_fusion 已经稳定训练
+ 全量结果仍明显弱于 baseline
+ 当前结构表达能力已接近平台

### 19.2 不要继续在 graph 融合末端硬加门控
原因：

+ 第二轮门控版已经验证更差
+ 这条路不是稳定化，而是在破坏主干可学习性

### 19.3 最推荐的路线
优先级如下：

1. **修正 GraphFC 本体**
    - 邻接归一化
    - 固定 WS relation graph
    - 更稳的初始化
    - 输出维度与原 FC 基线严格一致
2. **把 graph 分支改成 local -> graph delta 的小扰动块**
    - 保留 local 主干
    - graph 只做小修正
    - 初始残差影响要小
3. **先在中等规模上验证（如 24 files / 3 epochs）**
    - 不要一上来就全量从零跑 graph
4. **GraphFC 稳定后，再考虑补最小 SpikeBlock 占位**
    - 哪怕先不用完整 LIF，也应该让结构顺序更接近论文：
        * `Attention-BiLSTM -> Spike-like conv -> GraphFC -> BiGRU`

---

## 20. 当前一句话总结
**目前已经完成了论文前半段的可运行 baseline 和 sequence-level BiGRU 的初步验证；baseline 仍是当前最强结果，而下一步最值得做的是实现更接近论文的 EpochFusionBlock / GraphFC 修正版，并在此基础上逐步补齐 SpikeBlock，作为通往完整 SPSNet 的过渡版本。**

---

## 21. 附：当前常用训练命令示例
### 21.1 中间版本全量首跑（非 graph，已验证较稳的推荐风格）
```bash
python train_epochfusion_bigru.py --device cuda --amp --epochs 10 --batch-size 8 --imbalance-mode weighted_sampler --lr 3e-4 --grad-clip 1.0 --cache-mode one --num-workers 4 --pin-memory --persistent-workers --prefetch-factor 2 --save-dir outputs\epochfusion_bigru_runs\full_run
```

### 21.2 中间版本全量短版 smoke
```bash
python train_epochfusion_bigru.py --device cuda --amp --epochs 3 --batch-size 8 --imbalance-mode weighted_sampler --lr 3e-4 --grad-clip 1.0 --cache-mode one --num-workers 4 --pin-memory --persistent-workers --prefetch-factor 2 --save-dir outputs\epochfusion_bigru_runs\full_smoke
```

### 21.3 Graph 版全量命令（当前为 GraphBlock-lite 过渡版，不是完整 SPSNet）
```bash
python .\train_epochfusion_bigru.py --device cuda --amp --batch-size 16 --epochs 20 --data-dir C:\SAO\SPSNet\outputs\stft_cache --save-dir C:\SAO\SPSNet\outputs\epochfusion_bigru_graph_full --cache-mode all --imbalance-mode weighted_sampler --use-graphblock --graph-num-nodes 32 --graph-k 4 --graph-p 0.1 --graph-self-loop --graph-act relu --graph-dropout 0.0 --graph-alpha-init 0.5 --graph-norm-mode post_add --graph-bypass-mode none
```

注意：

+ 这条命令对应的是当前 **GraphBlock-lite 过渡结构**
+ 不是论文原始的完整 **SpikeBlock + GraphBlock + BiGRU** 训练命令
+ 当前主要作用是验证 graph 分支工程可用性与稳定性

---

## 22. 文档用途说明
本文档适合用于：

+ 项目阶段总结
+ 代码开发记录
+ 论文答辩前的自我梳理
+ 给 Codex / 协作开发者作为上下文说明
+ 继续整理成 Word 文档或实验日志

