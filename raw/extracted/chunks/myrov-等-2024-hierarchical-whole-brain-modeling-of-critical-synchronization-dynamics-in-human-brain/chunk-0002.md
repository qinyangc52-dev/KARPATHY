---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 2
chunk_count: 10
char_count: 8644
---

tional modeling;performed
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
