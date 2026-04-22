---
id: source-hierarchical-whole-brain-modeling-critical-synchronization-2024
type: source
title: "Hierarchical whole-brain modeling of critical synchronization dynamics in human brains"
created: 2026-04-22
updated: 2026-04-22
source_file: "raw/articles/Myrov 等 - 2024 - Hierarchical whole-brain modeling of critical synchronization dynamics in human brain.pdf"
extracted_file: "raw/extracted/myrov-ç­‰-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_dir: "raw/extracted/chunks/myrov-ç­‰-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain/"
extraction_status: extracted
evidence_policy: source-supported
authors:
  - Vladislav Myrov
  - Alina Suleimanova
  - Samanta Knapić
  - Paula Partanen
  - Maria Vesterinen
  - Wenya Liu
  - Satu Palva
  - J. Matias Palva
publication: "bioRxiv preprint"
date_published: 2025-01-06
doi: "10.1101/2024.05.08.593146"
sources:
  - raw/articles/Myrov 等 - 2024 - Hierarchical whole-brain modeling of critical synchronization dynamics in human brain.pdf
  - raw/extracted/myrov-ç­‰-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt
tags:
  - literature-note
  - computational-neuroscience
  - whole-brain-modeling
  - criticality
  - synchronization
  - kuramoto-model
  - meg
  - structural-connectome
related: []
status: stable
importance: high
confidence: medium
---

# Hierarchical whole-brain modeling of critical synchronization dynamics in human brains

## 一句话结论

这篇预印本提出一个 **Hierarchical Kuramoto model**：把每个脑区建成一群 Kuramoto 振子的局部系统，再用结构连接组约束脑区间耦合。它的核心结果是：模型能同时产生局部临界样动态、脑区间同步、振幅相关和近似 MEG 的频谱结构；与真实静息态 MEG 最相似的参数区不是临界峰值本身，而是扩展临界区的亚临界侧。

## 文献基本信息

- **标题**：Hierarchical whole-brain modeling of critical synchronization dynamics in human brains
- **作者**：Vladislav Myrov, Alina Suleimanova, Samanta Knapić, Paula Partanen, Maria Vesterinen, Wenya Liu, Satu Palva, J. Matias Palva
- **版本**：bioRxiv preprint，页面显示 manuscript compiled on January 6, 2025，DOI 为 `10.1101/2024.05.08.593146`
- **数据类型**：人类静息态 MEG、T1 MRI、DWI 结构连接组；模型仿真数据
- **抽取状态**：PDF 已抽取为文本，共 12 页，10 个 chunk
- **证据边界**：本文主要基于抽取文本和图注；图像没有进行视觉复核，补充材料全文没有读到

## 摘要

作者的问题很清楚：既有全脑模型通常偏向模拟功能连接，临界性模型又常停留在局部或统计物理框架，缺少一个能同时处理 **全脑功能连接** 和 **临界样动态** 的振荡模型。本文用层次化 Kuramoto 模型解决这个缺口。

模型有两层：局部层面，每个脑区节点包含大量 Kuramoto 振子，用局部耦合参数 `K` 控制节点内部同步；全局层面，节点之间通过结构连接权重和全局耦合参数 `L` 相互作用。这个设计让模型既有节点内部同步涨落，也有脑区间相位同步和振幅相关。

主要发现有三点。第一，模型在异步相和同步相之间的转变区产生 LRTCs、DFA 指数升高、节点 order correlation 等临界样特征。第二，不同功能观测量和结构连接的关系并不一致：DFA 与振幅相关在临界区与结构连接最强相关，而相位同步 PLV 在亚临界侧更接近结构连接，并在临界峰附近下降。第三，将模型与真实静息态 MEG 对比时，所有主要观测量的模型-MEG相似性都在扩展临界区的亚临界侧达到最大，而不是在临界峰值处。

这篇文章的价值不是简单地说“大脑在临界点”，而是把“局部同步、全局同步、结构连接、LRTC、MEG 频谱”放到同一个可调参数空间里比较。它给出一个更细的判断：健康静息态脑活动可能处在临界附近的亚临界坡面，而不是精确临界峰。

## 引言

作者从三个事实出发。

第一，人脑 MEG/EEG/SEEG 中存在中等水平的脑区间相位同步。同步参与调节神经通信和认知功能，但同步不足或过度同步也和癫痫、帕金森病、抑郁等疾病有关。

第二，神经振荡有频率、功率、相位同步、振幅相关等多个可观测维度。这些量可以从 MEG 源空间 parcel time series 中获得：功率谱对应局部同步，振幅相关和相位同步对应功能连接。

第三，临界脑假说认为神经系统运行在有序和无序之间的相变附近。临界附近会出现 LRTCs、神经 avalanche、较大的动态范围、信息容量和复杂性。但真实系统的控制参数不可直接观测，因此需要计算模型来连接控制参数和观测量。

已有模型的缺口在于：Wilson-Cowan、Hopf、普通 Kuramoto 等模型可模拟功能连接；branching process、Ising、CROS 等模型可研究临界性；但能同时模拟振荡功能连接和临界样动态的全脑模型不足。本文提出的层次 Kuramoto 模型就是为这个缺口服务。

## 正文部分

### 1. 模型结构

模型的最小单位不是“一个脑区一个振子”，而是“一个脑区一群振子”。每个节点代表一个脑区或记录源，每个节点内部包含 1000 个振子。节点内部振子通过局部耦合 `K` 互相影响，节点之间通过结构连接权重 `W` 和全局耦合 `L` 互相影响。

这个层次化结构解决了普通 Kuramoto 全脑模型的一个弱点：单振子节点没有内部振幅涨落，因此很难和 MEG 中的局部功率、振幅相关和 LRTCs 对齐。本文模型通过节点内部振子的平均复数信号生成节点 time series，使每个节点既有相位，也有 order/amplitude-like fluctuation。

### 2. 控制参数和临界区

模型主要扫描两个控制参数：

- `K`：局部耦合强度，控制节点内振子同步。
- `L`：全局耦合强度，控制节点间相互作用。

作者用 DFA 指数刻画 LRTCs，并把超过阈值的节点比例作为识别临界区的依据。文中把 critical regime 定义为超过 10% 节点 `DFAexp > 0.65` 的区域。模型从亚临界到超临界时，局部 order、PLV、cross-correlation、DFA 等指标呈现不同形状的变化。

关键点是：临界性不是一个单点，而更像参数平面上的 ridge 或 extended regime。这个表述很重要，因为后文模型-MEG 相似性峰值位于临界 ridge 的亚临界侧。

### 3. 结构-功能耦合

作者把结构连接组作为模型的全局连接骨架，然后比较模型生成的功能观测量与结构连接之间的相关性。

结果不是“结构越强功能越强”这么简单。不同观测量在参数空间中的结构-功能关系不同：

- 节点 order 与 node strength 的相关性在部分区域升高，但在临界附近有局部下降。
- DFA exponent 与 node strength 的相关性在临界区达到峰值，在超临界区变成强负相关。
- 节点 order cross-correlation 与结构边权的相关性类似 DFA，在临界附近增强。
- PLV 与结构边权的相关性呈不同形状：在亚临界侧有宽峰，并在临界峰附近下降。

这说明结构连接对功能动态的解释力依赖系统操作点。若不知道系统处于亚临界、临界还是超临界，单纯讨论结构-功能耦合容易混淆不同机制。

### 4. 模型与 MEG 的对应

作者用 20 名健康被试的 15 分钟睁眼静息态 MEG，并结合 MRI/DWI 数据建立真实结构连接和功能观测量。MEG 数据被源重建到 Schaefer 200 parcels，并用 41 个 log-spaced Morlet wavelets 覆盖 1-100 Hz。

模型-MEG 对比用 Pearson correlation：节点级指标比较 parcel 向量，边级指标比较矩阵上三角。对 MEG，作者使用 wPLI 处理相位同步，以减少零滞后虚假连接；对模型使用 PLV。

结果显示，DFA、节点级同步、边级同步、cross-correlation 等观测量的模型-MEG相似性，整体上在亚临界侧的扩展临界区最大。DFA 和节点级 cross-correlation 在临界区另一侧可能转为负相关，作者据此推测真实人脑的临界区可能比模型中的临界峰更宽。

### 5. 频谱结果

为让模型具有更真实的频谱，作者从 MEG parcel-level PSD 中去除 1/f 成分，并把剩余 PSD 转换为每个节点的振子频率分布。随后比较模型 PSD 和 MEG PSD。

结果显示，临界样模型能较好保留 alpha 和 beta 多峰结构；亚临界状态几乎缺少明显振荡峰，超临界状态出现强持续振荡，并且频率峰向振子频率加权平均移动。最高 PSD 相似性同样出现在扩展临界区的亚临界侧，尤其是高局部耦合、低全局耦合区域。

这部分支持一个具体机制判断：临界附近的脑活动可能在“保留个别频率峰”和“不塌缩成单一中心频率”之间取得平衡。

## 图像分析

> 说明：以下分析基于抽取文本中的图注和正文描述，没有进行 PDF 图像视觉复核。

### Figure 1：实验和建模管线

图 1 把真实 MEG/MRI/DWI 管线和模型管线并排说明。真实管线包括 T1 MRI 分区、DWI 构建结构连接、MEG 生成 parcel time series、PSD、振幅相关和 wPLI。模型管线则显示每个节点由大量振子构成，节点间按结构连接相互耦合，并生成可与 MEG 对应的 PSD、振幅相关和相位同步。这个图的作用是证明模型输出和实验观测量在形式上可比较。

### Figure 2：相变和临界样动态

图 2 展示 `K` 和 `L` 参数空间，以及亚临界、临界、超临界三种状态。DFA 指数和 order 随耦合变化，临界区由 `DFAexp >= 0.65` 的节点比例定义。该图支撑本文最基础的模型结论：层次 Kuramoto 模型能够产生 LRTCs 和相变附近的临界样动态。

### Figure 3：结构-功能耦合随操作点变化

图 3 用结构连接组驱动模型，并比较 node strength / edge weight 与 order、DFA、PLV、cross-correlation 的相关性。核心信息是不同功能观测量在临界附近的结构-功能关系不同：DFA 和振幅相关在临界附近增强，PLV 更偏亚临界。该图支撑“不同观测量有不同 breakpoint”的论点。

### Figure 4：模型与 MEG 的相似性

图 4 对比模型和真实 MEG，在不同频段和参数空间中计算相似性。结果显示最显著的模型-MEG 相似性沿着临界 ridge，并偏向亚临界侧。这个图是本文关于“健康脑活动位于扩展临界区亚临界侧”的主要证据。

### Figure 5：多频谱性质

图 5 用 MEG-derived PSD 设定节点振子频率分布，并比较模型和 MEG 的 PSD。结果显示临界样状态比纯亚临界或超临界更能保持真实 MEG 的多峰频谱结构，尤其是 alpha 和 beta 峰。该图把临界样动态和可观测频谱形态连接起来。

## 结论

作者的结论是：层次 Kuramoto 模型提供了一个生成式框架，可显式分离局部耦合和脑区间耦合，同时生成局部和全局多尺度同步动态。模型生成的动态在若干 MEG 可比指标上具有生理合理性。

更具体地说，本文不是证明人脑“正好在临界点”，而是提出：健康静息态脑活动更可能处在扩展临界区的亚临界侧。这个区域既没有完全无序，也没有塌缩成过度同步，能同时支持 LRTCs、振幅相关、相位同步和多峰频谱。

## 参考文献

抽取文本读到了参考文献列表，共编号至 93。没有逐篇展开阅读。与本文论证最直接相关的参考文献包括：

- Shew & Plenz 2012：临界性功能收益。
- Chialvo 2010：复杂神经动力学。
- Linkenkaer-Hansen et al. 2001：人脑振荡中的 LRTCs。
- Beggs & Plenz 2003：神经 avalanche。
- Fuscà et al. 2023：脑临界性预测人类电生理数据中的脑区间同步。
- Kuramoto 1975：Kuramoto 振子模型。
- Donoghue et al. 2020：FOOOF/周期与非周期功率谱参数化。
- Hardstone et al. 2012 与 Nolte et al. 2019：DFA 方法。
- Vinck et al. 2011：wPLI。
- Schaefer et al. 2018 与 Yeo et al. 2011：皮层分区和网络。

## 补充材料

正文提到 Supplementary Figure 1 和 Supplementary Figure 3，但当前抽取文本没有包含完整补充材料。能从正文得到的信息是：

- Supplementary Figure 1：作者用 log-transformed structural connectome 复现了部分结果，但 critical ridge 更窄，critical peaks 变异更低，平均 DFA exponent 和 CC 更高。
- Supplementary Figure 3：使用非参数异质频率分布时，模型仍显示 critical-like dynamics，并在保留多频活动的同时出现 LRTCs。

补充材料的图像和完整说明未读到，因此不能进一步判断。

## Q1-Q16 学术问题回答

### Q1：这篇论文解决什么问题？

它解决“全脑模型如何同时模拟功能连接和临界样动态”的问题。既有模型常在功能连接或临界性之间二选一，本文用层次 Kuramoto 模型把两者放入同一参数空间。

### Q2：核心模型创新是什么？

每个脑区不是一个振子，而是一组振子。局部振子群产生节点内部 order 和振幅涨落，结构连接组约束节点间耦合，因此模型同时有局部和全局动态。

### Q3：控制参数是什么？

主要是局部耦合 `K` 和全局耦合 `L`。`K` 控制节点内同步，`L` 控制节点间相互作用。

### Q4：临界性如何 operationalize？

作者主要用 DFA 指数刻画 LRTCs，并把超过阈值的节点比例用于定义 critical regime。正文和图注中使用 `DFAexp >= 0.65` 作为关键阈值。

### Q5：模型的功能观测量有哪些？

节点 order、DFA exponent、节点 order cross-correlation、PLV、PSD，以及与 MEG 对应的 wPLI/振幅相关等。

### Q6：结构连接如何进入模型？

DWI 得到的结构连接矩阵作为节点间边权 `W`，影响全局耦合项。结构连接组同时用于分析结构-功能相关。

### Q7：主要实证数据是什么？

20 名健康被试，15 分钟睁眼静息态 MEG；同时有 T1 MRI 和 DWI。MEG 源重建到 Schaefer 200 parcels。

### Q8：模型与 MEG 如何比较？

节点级观测量用 parcel 向量相关；边级观测量用矩阵上三角相关。模型相位同步用 PLV，MEG 相位同步用 wPLI。

### Q9：最重要的经验结果是什么？

模型-MEG 相似性在扩展临界区的亚临界侧最高，而不是在临界峰值处最高。

### Q10：结构-功能关系有什么新发现？

不同观测量的结构-功能耦合峰值不一致。DFA 和振幅相关偏临界区，PLV 偏亚临界侧并在临界峰附近下降。

### Q11：这篇论文如何理解“大脑临界性”？

它弱化了“精确临界点”的说法，更强调扩展临界区和操作点。健康脑活动可能位于临界附近的亚临界坡面。

### Q12：频谱分析说明了什么？

真实 MEG 的多峰 PSD 可以通过设置节点频率分布并调节操作点来近似。临界样区域有助于保留 alpha/beta 多峰结构，超临界会更容易向中心频率塌缩。

### Q13：模型的计算优势是什么？

作者称模型计算效率高，能模拟百万级相互作用振子，同时保留与 MEG 可比的节点和边级观测量。

### Q14：模型的主要限制是什么？

它仍是相位振子模型，神经生理细节被大幅简化；模型代码要到发表后开源；补充材料当前未读到；本文数据是静息态健康被试，疾病和任务态推广仍需验证。

### Q15：这篇论文对疾病研究有什么意义？

它提供了一个可把结构连接改变、局部/全局耦合变化、同步异常和临界性偏移联系起来的建模框架。对癫痫、帕金森、抑郁等同步异常疾病有潜在用途，但本文没有直接做疾病数据验证。

### Q16：后续最值得做什么？

最值得做的是个体化建模：用个人结构连接和 MEG 指标估计其操作点，再测试刺激、疾病、药物或学习是否会把操作点推向不同临界区域。

## 三个关键问题及作答

### 关键问题 1：为什么普通 Kuramoto 全脑模型不够？

普通做法常把每个脑区当作单个振子，因此节点本身没有内部同步涨落，难以产生 MEG 中常见的振幅相关、局部 order fluctuation 和 LRTCs。本文把每个脑区扩展成振子群，给每个节点内部增加可观测动态，因此能同时研究局部临界性和脑区间同步。

### 关键问题 2：为什么模型-MEG 最相似点不在临界峰？

临界峰附近同步和涨落可能过强，超临界侧还可能出现过度同步或频谱塌缩。亚临界侧保留了足够的动态灵活性，同时又接近临界区，因而更接近真实健康静息态 MEG。作者的结果支持这种解释，但还不是因果证明。

### 关键问题 3：本文最有用的思想是什么？

最有用的是把“结构-功能耦合”视为操作点依赖的关系。不同功能指标在 `K-L` 参数空间中有不同峰值和断点，因此不能期待一个结构连接矩阵固定解释所有功能观测量。

## 术语和概念

- **Hierarchical Kuramoto model**：每个节点内部包含多个 Kuramoto 振子，节点之间再由结构连接和全局耦合相连。
- **Local coupling `K`**：节点内部振子之间的耦合强度。
- **Global coupling `L`**：节点之间的耦合强度。
- **Order parameter**：节点内部振子相位对齐程度，值越高表示越同步。
- **LRTCs**：long-range temporal correlations，长程时间相关，本文用 DFA exponent 表征。
- **DFA exponent**：Detrended Fluctuation Analysis 的斜率指数，用于刻画尺度相关涨落。
- **PLV**：phase locking value，模型中的相位同步指标。
- **wPLI**：weighted phase lag index，MEG 中用于减少零滞后伪连接影响的同步指标。
- **Structure-function coupling**：结构连接强度与功能观测量之间的统计关系。
- **Extended critical regime**：不是单点临界，而是参数空间中一片临界样区域或 ridge。

## 相关页面

当前仓库中相关概念页处于重建状态，本文暂不创建额外概念页，避免重复和污染。后续可以从本文提炼：

- `criticality`
- `synchronization`
- `kuramoto-model`
- `whole-brain-modeling`
- `meg`
- `structure-function-coupling`
- `long-range-temporal-correlations`

## 证据边界与局限

- **source-supported**：模型结构、控制参数、DFA/PLV/wPLI/PSD 指标、20 名健康被试、MEG/MRI/DWI 数据、Schaefer 200 parcels、模型-MEG 相似性峰值在亚临界侧，均由抽取文本支持。
- **inferred**：本文对疾病研究和个体化建模的意义，是从作者讨论和模型能力合理推断。
- **background-knowledge**：对 Kuramoto 模型、临界脑假说、MEG 源空间分析的简短解释包含领域背景。
- **needs-verification**：补充材料全文、图像视觉细节、最终发表版本和代码实现细节需要进一步核验。

## 后续处理建议

1. 获取正式发表版本或新版 bioRxiv，检查标题年份和 DOI 元数据是否变化。
2. 获取 Supplementary Materials，补齐 Supplementary Figure 1 和 3 的完整解读。
3. 在 `wiki/concepts/` 重建完成后，把本文术语拆分到稳定概念页。
4. 等代码开源后，建立 `wiki/entities/` 或 `wiki/topics/` 页面记录模型实现细节。
5. 用本文框架对照已有 Kuramoto、Hopf、Wilson-Cowan 和 CROS 模型，创建比较页。
