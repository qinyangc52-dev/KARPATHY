---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 8
chunk_count: 10
char_count: 9333
---

complete absence of oscillations in the subcritical region to
strong, sustained oscillations with peaks shifted towards the
weighted average of the oscillator frequencies.
Based on
these results, we hypothesize that activity in the critical-like
region achieves a balance between sustained oscillations with
persistent individual peaks without collapsing into a singular
central frequency.
Myrov et al.
PNAS
—
January 6, 2025
—
vol. XXX
—
no. XX
—
9
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

<!-- page:10 -->
DRAFT
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
In conclusion, we introduce here a framework for generative
hierarchical models of synchronization dynamics that enable
explicit representation of local and inter-areal coupling
and observations of emergent multi-scale synchronization
dynamics. Our results show that the Hierarchical Kuramoto
model produces meso- and macro-scale synchronization-
dynamics observables that are physiologically plausible in the
light of MEG data. The model enables detailed analysis of
control parameters for local and inter-areal coupling, paving
the way for future studies on personalized modeling of stimuli
responses.
Materials and Methods
Hierachical kuramoto model. The classical Kuramoto model de-
scribes the synchronization dynamics of coupled oscillators, where
each oscillator aligns its phase with others based on coupling
strength
δϕi
δt = ωi + 1
N
PN
j=1 Kijsin(ϕj −ϕi)
where N is the total number of oscillators, ϕi is the i-th oscillator
phase, ωi is the frequency of the i-th oscillator and Kij is the
coupling parameter between the i-th and j-th oscillators.
In this framework, each oscillator represents a brain region
or parcel, and the coupling parameter reflects the structural
connectivity between two zones.
However, a single Kuramoto
oscillator has constant amplitude in complex domain, which
makes comparison with real brain imaging data a challenging
task. To overcome this, we introduce a hierarchical extension of
the Kuramoto model with multiple nodes which may correspond to
a recording from a single brain area or electrode. This allows for the
representation of local synchronization within nodes and inter-areal
interactions across nodes. Each node comprises multiple oscillators,
whose behavior can be described by three key components:
δϕn
i
δt
= Natural + Internal + External + Noise
Where Natural = wn
i represents the central frequency of the
i-th oscillator in the n-th node and ϕn
i is the phase of the i-th
oscillator in the n-th node,
Internal = Kn
N
PN
j=1 sin(ϕn
i −ϕn
j )
where Kn is the local coupling parameter of the n-th node
and N is the total number of oscillators within the node. In this
context, the phase of each oscillator is shifted towards the average
phase difference with the oscillators in the same node,
External = Pk
j=1 Ln,j ∗Wn,j ∗sin(ϕn
i −Φj) ∗Rj
Where Ln,j is the coupling coefficient between the n-th and
j-th nodes (global control parameter), Wn,j is the structural con-
nectivity between the n-th and j-th nodes, Φj is the cyclic average
of the phases of the n-th node defined as Φj = arg( 1
N
PN
q=1 eiϕj
q)
and Rj is the order of the j-th node (see the definition below).
In this context, the phase of each oscillator is compared to the
average phase of other nodes and weighted by a node order and
structural connectivity.
and Noise = ηn
i is the white noise for the i-th oscillator in the
n-th node.
At the final step, we computed the signal for each node by
averaging the complex values of all oscillators, and the analytical
time series of the n-th node is defined as Sn =
1
N
P
j = 1Nei∗ϕn
j .
Thus, one is able to match a model’s node to a single brain area
or any other source of LFP recordings.
To improve computational performance, we use a complex-value
representation for oscillator states. Thus, the coupling function
between oscillators x and y becomes imag(x ∗y∗), where x and y
are complex values representing an oscillator phase, and y∗is a
conjugate of y.
A. Computational experiments. For all experiments, each model
node contained 1000 oscillators to ensure sufficient granularity
in capturing local dynamics.
In experiments for figures 2,3,4,
oscillator frequencies were sampled from a normal distribution,
centered at each node’s central frequency (10 Hz), with a standard
deviation of 1 Hz. As the noise component, we used normally
distributed random values with a mean of 0 and a scale of 3 in all
experiments.
We simulated 6 minutes of resting-state activity varying local
and global control parameters, in experiments for figures 2,3 and 4
the K and L had equally spaced values from 0 to 8, in experiment
for figure 5 the local coupling was varied from 0 to 20 and global
coupling from 0 to 40. We cutoff the first minute of simulation to
avoit the warmup period which inflates the DFA exponent values.
Observables of oscillatory dynamics. The order parameter is a key
observable in the Kuramoto model, which quantifies the synchrony
among oscillators within a node.. It is defined as the absolute
value of the average complex-valued phase across oscillators that
belong to the same node:
R = | 1
N
PN
i=1 ei∗θi|
Where N is the number of oscillators and θi is the phase of the
i-th oscillator.
To estimate inter-areal phase interactions, we computed phase
synchrony metrics for each pair of nodes (in the model data) or
parcels (in the MEG data). For the model, we used the phase
locking value (PLV), defined as the absolute value of the complex
PLV:
cPLV = E[CSx,y]
Where E[.] denotes the expected value and CSx,y denotes the
cross-spectrum between a complex signals X and Y. In practice,
cPLV is estimated using limited data and sample cPLV is defined
as
cPLV sample =
1
N
PN
i=1 CSx,y
where N is the total number of samples.
For MEG data, we employed the weighted Phase Lag Index
(wPLI), a metric robust to spurious zero-lag interactions, defined
as:
wPLI =
|PN
i=0 imag(CSx,y)|
PN
i=0 |imag(CSx,y)|
where imag(CSx,y) is the imaginary part of the cross-spectrum
of the complex time series x and y (77, 78).
The correlation coefficient between node time series is another
way of estimating bivariate relations in a system. To include them
in the analysis, we computed the Pearson correlation coefficient
between each pair of model node order time series.
To measure long-range temporal correlations (LRTCs) in the
model and MEG recordings, we used Detrended Fluctuation
Analysis (DFA, (79)), which we computed in the Fourier domain
to speed up the estimation (80). To obtain the DFA exponents
from model or MEG data, we fitted the fluctuations as a function
of window sizes using robust linear regression (81) with a bisquare
weight function. We used 30 equally log-spaced windows, with
sizes ranging from 10 central frequency cycles to 25% of the data.
Measures of similarity between observables of simulated and real
data. We employed the Pearson correlation coefficient to quan-
tify the similarity between observables of oscillatory dynamics
derived from simulated and MEG data.
For univariate node-
level observables such as DFA and pACF, we computed the
correlation coefficient between vectors of values for each parcel.
For bivariate observables such as Phase Synchrony and Cross-
Correlation matrices, we computed the correlation between values
from the upper triangle of the matrix.
Code availability. The model code will be open-sourced following
publication.
Data acquisition. Fifteen minutes eyes-open resting-state data were
recorded from 20 healthy controls with 306-channel MEG (TRIUX,
MEGIN Oy, Helsinki, Finland; 204 planar gradiometers and 102
magnetometers) at BioMag Laboratory, HUS Medical Imaging
Center, Helsinki, Finland and 306-channel MEG (TRIUX neo,
MEGIN Oy, Helsinki, Finland; 204 planar gradiometers and 102
magnetometers) at MEG Core, Aalto University, Espoo, Finland.
Bipolar horizontal and vertical electrooculography (EOG) and
electrocardiography (ECG) were also recorded. Participants were
instructed to sit as still as possible and keep their eyes open to
10
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
