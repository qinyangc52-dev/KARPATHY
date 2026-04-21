---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 1
chunk_count: 6
char_count: 14790
---

<!-- page:1 -->
DRAFT
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
Hierarchical whole-brain modeling of critical
synchronization dynamics in human brains
Vladislav Myrova,1, Alina Suleimanovaa, Samanta Knapiˇca,b, Paula Partanenb, Maria Vesterinenb, Wenya Liua,b, Satu Palvab,c,
and J. Matias Palvaa,b,c
This manuscript was compiled on January 6, 2025
Brain activity exhibits critical-like dynamics, which is fundamental for cognitive functions.
Whole-brain computational modeling has become indispensable in studying the systems-level
mechanisms that govern the dynamics of large-scale brain activity in health and disease.
However, previous approaches have focused on modeling either functional connectivity or
criticality, and capturing both simultaneously in whole-brain systems remains a challenge.
Here, we advance a new approach to modeling multi-scale synchronization dynamics with
the Hierarchical Kuramoto model. At two levels of hierarchy, the model comprises a network
of nodes that each encapsulate a large number of coupled oscillators, which enables
dissection of local and inter-areal coupling and dynamics. We found the model to produce
oscillations with critical-like dynamics, including emergent long-range temporal correlations
(LRTCs) and inter-areal order correlations at the critical transition between asynchronous
and synchronous phases. The model predicted unique structure-function relationships for
functional observables so that coupling with structure peaked at criticality for LRTCs and
order correlations but collapsed for inter-areal phase synchronization. Comparison of the
model dynamics with human resting-state magnetoencephalography (MEG) showed that
model-MEG correlations were maximized in the subcritical side of an extended critical regime
for all observables and across the model parameter space. Finally, we found that the model
may also yield realistic-like multi-peak power spectra and that also their similarity with MEG
data is maximized below peak criticality. In conclusion, Hierarchical Kuramoto modeling
yields realistic and separable local and global synchronization dynamics that are directly
comparable with neuroimaging, which opens new avenues for understanding collectivity in
brain activity.
Brain Oscillations | Criticality | Modeling | Kuramoto | MEG
H
uman brains in vivo exhibit moderate levels of long-range phase synchronization
in both intra-cerebral stereo-EEG (SEEG) (1–3) and non-invasive M/EEG
recordings (4–6). Synchronization plays mechanistic roles in regulating neuronal
communication in brain networks (7–9) underlying cognitive functions (10–12).
Inadequate or excessive synchronization, on the other hand, constitutes a core
mechanism for neurological disorders such as epilepsy (2, 13) and Parkinson’s
disease (14), and characterizes neuropsychiatric diseases such as depression (15, 16),
where abnormalities in synchrony are correlated with the severity of depressive
symptoms (17–19).
Neuronal oscillations are rhythmic excitability fluctuations that arise with
frequency-specific synaptic mechanisms in neuronal micro- and macrocircuits (20).
To study these oscillations, researchers employ electrophysiological methods such as
electroencephalography (EEG), stereo-EEG (SEEG), and/or magnetoencephalogra-
phy (MEG) in humans ( Figure 1A). Typically, recordings are collapsed into cortical
parcellations, and the parcel time series are filtered to obtain narrow-band analytical
time series ( See Figure 1B). Observables such as local power spectra ( See Figure
1C) that is a proxy to local neuronal synchronization within a population,and inter-
areal amplitude ( See Figure 1D,F) and phase correlations ( See Figure 1E,G) to
operationalize functional connectome, are then obtained.These measures of neuronal
oscillations exhibit considerable variability in characteristics such as frequency,
power, and inter-areal coupling (phase-synchronization, amplitude correlations) and
this variability is functionally significant, e.g., in predicting cognitive performance
(15, 21, 22), learning (23), and neurological state (13).
The framework of criticality provides an approach to understanding these
neuronal dynamics and their variability: the ”critical brain” hypothesis (24–27)
proposes that the Operating Point (OP) of neuronal systems in vivo lies very near the
critical phase transition between the subcritical (disorder) and supercritical (order)
Significance Statement
Healthy brain activity depends on
both moderate levels of inter-areal
phase synchronization and emer-
gent critical-like dynamics. We in-
troduce here the Hierarchical Ku-
ramoto model that yields a novel
framework for simulating both facets
of critical synchronization dynam-
ics on the whole-brain scale. The
model revealed that the coupling
between structure connectivity and
emergent functional architecture
has unique breakpoints for both
synchronization and criticality. The
similarity between emergent dynam-
ics in the model and observed with
magnetoencephalography system-
atically peaked on the subcritical
side of an extended critical regime,
suggesting that healthy brain activ-
ity in vivo is confined to this range.
These findings provide a new plat-
form of modeling whole-brain activ-
ity and accessing new mechanistic
insight into the organizational princi-
ples of neuronal dynamics
Author affiliations: aDepartment of Neuroscience and
Biomedical Engineering, Aalto University, Espoo,
Finland; beuroscience Center, Helsinki Institute of
Life Science, University of Helsinki, Helsinki, Finland;
cCentre for Cognitive Neuroimaging, School of Neu-
roscience and Psychology, University of Glasgow,
Glasgow, UK
V.M:
conceived
the
study;model
develop-
ment;performed computational modeling;performed
data analysis;
A.S.: performed computational modeling;performed
data analysis;
S.K.: provided preprocessed DWI data;
P.P.: MEG data recording;
W.L.: provided preprocessed MEG data;
M.V.: MEG data recording;
S.P.: curated the data collection;
J.M.P.: conceived the study;
The authors declare no competing interests.
1To whom correspondence should be addressed. E-
mail: vladislav.myrovaalto.fi
www.pnas.org/cgi/doi/10.1073/pnas.XXXXXXXXXX
PNAS
—
January 6, 2025
—
vol. XXX
—
no. XX
—
1–12
.
CC-BY-NC-ND 4.0 International license
available under a
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint
this version posted January 6, 2025. 
; 
https://doi.org/10.1101/2024.05.08.593146
doi: 
bioRxiv preprint

<!-- page:2 -->
DRAFT
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
phases of the system’s state space.
Operation at critical
transition leads to emergence of scale-free spatiotemporal
correlations, observable both as long-range temporal corre-
lations (LRTCs, (26)) and power-law scaled avalanches (27),
and yields several functional advantages, such as maximized
information capacity (24), complexity (28) and processing,
dynamic range (29), and transmission rate (30, 31).
Operating point is a measure that defines the position in
the system’s critical state space. It is regulated by underlying
control parameters that for neuronal systems are excitation-
inhibition (E/I) balance (32), neuromodulation of synaptic
plasticity (33, 34), and structural connectivity patterns such
as network modularity (35–38). A given OP is associated with
specific emergent dynamics, which can be operationalized
with a range of synchronization and criticality observables (26,
27, 39–41). Because neither the control parameters nor the
system’s states are readily observable, their relationships with
observables such as synchrony, LRTCs, and avalanches have
remained a topic where computational modeling is essential
for mechanistic understanding.
Numerous computational models have been developed
to investigate the principles underlying whole-brain neural
dynamics (42–44). Inter-areal functional connectivity (phase
synchronization) has been modeled with the Wilson-Cowan
model (3), Hopf model (45), and Kuramoto model (46–
48).In contrast, computational models used in criticality
research, have used to study avalanches using branching-
process (49) and Ising models (50) from statistical physics,
as well as neurophysiology-inspired population models (51–
53) and networks of excitatory and inhibitory neurons (39)
like the critical oscillations (CROS) model that exhibits
LRTCs (54, 55).Thus, at present, there is a lack of models
that would accurately capturate realistic oscillation-based
functional connectivity and critical dynamics. The Kuramoto
model is the simplest model of synchronization dynamics
and captures the emergence of self-organized synchrony in a
system of coupled oscillators. The model exhibits a transi-
tion between subcritical (asynchronous) and supercritical
(synchronous) phases, characterized by the emergence of
critical-like dynamics such as LRTCs (40) and avalanches
(56).
In prior research using Kuramoto modeling in the
neuroscience context, the activity of the neuronal populations
representing single cortical parcels has been represented by
single Kuramoto oscillators (57).
This approach models
whole-brain network dynamics but does not yield criticality-
relevant node-level observables such as order fluctuations or
LRTCs. Another approach for using the Kuramoto model
represents a neuronal system as either a single (58, 59) or
two populations (48, 60) of oscillators, capturing critical-like
dynamics at the node level but not extending the model into
a whole-brain scale networks.
We advance here a hierarchical extension of the classic
Kuramoto model, consisting of a whole-brain network where
each node contains a large group of oscillators.
This
multi-level architecture yields separable local and inter-areal
synchronization dynamics and allows direct comparability
with neuroimaging data. Utilizing the model we investigated
organizational principles in brain dynamics by examining the
architecture of structural connections at different operating
points, and compared the model output with MEG-observed
dynamics.
By further extending the modeling approach,
we studied how multi-modal spectral properties behave at
different levels of criticality. Ultimately, our approach enables
whole-brain scale modeling of self-organized critical dynamics
at both the nodal and systems levels, opening new avenues
to investigate how system properties affect brain activity.
Results
Whole-brain model of critical oscillations. Activity in the
brain is guided by interactions on both macro and micro scale
from individual neurons to large neuronal populations whose
magnetic fields are detectable with non-invasive neuromaging
methods such as MEG ( See Figure 1A). These complex
interactions gives rise to oscillatory activity at different time-
scales ( See Figure 1B) and multiple phenomena are observed
at inter- ( See Figure 1C) and intra-areal levels ( See Figure
1D-G).
In order to capture intra- and inter-areal dynamics simulta-
neously, we designed a hierarchical model in which each node
is a full system of Kuramoto oscillators (20, 48, 61) analogous
to each cortical area containing a large population of neurons.
The oscillators are directionally coupled within the node with
coupling weighted by local control parameter K ( See Figure
1H, see Methods). We quantified within-node synchronization
using the Kuramoto order, here refered as ’node order’,
defined as the alignment of oscillators’ phases. Each node thus
yielded synchronization dynamics with fluctuations between
weaker and stronger internal synchronization ( See Figure 1H)
similar to the in vivo neocortical synchronization dynamics
reflected in MEG oscillation amplitude fluctuations ( See
Figure 1B).
On the next level of hierarchy, we defined the interaction
between the nodes as being guided by directional phase-
difference of respective complex node time series weighted by
node order and edge weight (see Methods). This approach
encapsulates interactions between different levels of hierarchy
and induces an additional level of heterogeneity in the
model.
We found that model time series exhibited local
synchronization fluctuations ( See Figure 1I) with both local
features, such as power spectra ( See Figure 1J), and inter-
areal correlations, such as amplitude correlations ( See Figure
1K,M) and phase synchrony ( See Figure 1L,N), similar to
those observed in real narrow-band MEG time-series.
Local and global control parameters shape the model criti-
cal-like dynamics. According to the critical brain hypothesis,
neural networks operate near a critical point between order
and disorder to optimize computational capabilities and
adaptability. The state-space of critical dynamics emerges
from a position in parameter space. In oscillatory network
models, these parameters are local and global coupling
strengths ( Figure 2A) such that critical phase transition
occurs between desynchronization and complete synchroniza-
tion on both nodal and inter-node levels, operationalized with
node order and inter-node phase synchronization, respectively.
At the critical regime, oscillations are characterized by Long
Range Temporal Correlations (LRTCs), operationalized using
Detrended Fluctuation Analysis (DFA, See Figure 2B).
To assess how model parameters affect the criticality
properties of the model, we set the initial distribution of
inter-nodal edge weights to match a single-subject structural
connectome (SC, quantified as DTI fiber count, see Methods).
2
—
www.pnas.org/cgi/doi/10.1073/pnas.XXXXXXXXXX
Myrov et al.
.
CC-BY-NC-ND 4.0 International license
available under a
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint
this version posted January 6, 2025. 
; 
https://doi.org/10.1101/2024.05.08.593146
doi: 
bioRxiv preprint
