---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 4
chunk_count: 6
char_count: 17745
---

nables realistic local synchronization
dynamics and cortical heterogeneity in a manner that are
directly comparable with experimental data and provides
insight into whole-system dynamics.
In particular, the
nodes in the Hierarchical Kuramoto model reproduce several
features of critical meso-scale brain dynamics observed in
electrophysiological recordings, such as LRTCs in amplitude
dynamics, power spectra, and rhythmicity (2, 40, 59, 63).
Moreover, while Kuramoto models express phase correlations
by design, we found the model to also express in vivo-like
(2, 5, 21) emergent amplitude correlations, i.e., inter-areal
correlations in local synchronization dynamics.
We found that these distinct brain dynamics observables
exhibited unique structure-function relationships across the
8
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

<!-- page:9 -->
DRAFT
993
994
995
996
997
998
999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
critical phase transition. Here, we elucidated the models pre-
dictions for the unique structure-function coupling of different
functional observables across the state space. We further
assessed the similarity of the model’s inter-areal correlation
structures with those observed in MEG data and found results
that strongly suggest human brains operate on the subcritical
side of an extended critical regime. Importantly, the model
is computationally highly efficient and enables simulations at
the level of millions of interacting individual oscillators.
A wide range of computational models has been developed
to study emergent brain dynamics at scales ranging from cell
population approaches, such as the CROS model (39), to
large-scale mean-field models, like the Wilson-Cowan (64),
and to models utilizing oscillators to represent brain regions
such as the Kuramoto (45, 61) or the Hopf (52) model.
In this work, we extended this approach by introducing
a hierarchical model, where a single node encapsulates
a population of individual oscillators.
Governed by the
complex non-linear interaction between these oscillators, the
model allows to reconstruct local and global critical-like
dynamics simultaneously with emergence of powerlaw long-
range temporal correlations on node-level and amplitude
cross-correlation on inter-nodal level.
The “critical brain” hypothesis suggests that the brain
operates near a phase transition between order and disorder,
where critical dynamics emerge (24, 25). Notably, long-range
temporal correlations (LRTCs, (40, 41, 65)) and avalanche
dynamics (41, 66, 67) emerge during phase transition, which
are key signatures of critical-like dynamics.
The model
effectively captured the expected phase transition, demon-
strating low inter-areal phase synchronization and local order
in the subcritical phase, which increased toward complete
synchronization in the supercritical phase (40, 68).
At criticality, such phase-based measures of order thus
exhibit moderate values, which magnitude match well with in
vivo research that invariably reports neuronal synchronization
to be weak to moderate. In the model, we observed that the
dynamics of inter-node synchronization as a function of local
coupling have a sigmoidal shape and start to grow in the
subcritical regime and achieve PLV of ∼0.35 at criticality.
In contrast, local synchronization remains low (∼0.05 −
−0.1) at critical point and starts growing rapidly afterwards.
In addition, the variability in observables emerges around
criticality and vanishes at supercritical state.
While intra- and inter-areal synchronization was max-
imuzed by minimization of zero-lag phase difference, node-
order correlations at the whole-brain level peaked at criticality,
similar to LRTCs.
This is congruent with a prior study
reporting maximal amplitude correlations at criticality among
spiking-neuron networks in a two-node system (54). Notably,
the amplitude correlations emerge in the model without direct
optimization but as a result of concurrent changes in local
synchronization.
In the bigger picture, we propose that
amplitude correlations in oscillatory systems are analogous to
power-law dynamic correlations (32) that emerge at criticality
in models of physical systems, such as the Ising model. In
the context of complex oscillatory critical-like systems such
as the brain, we hypothesize that the information transfer is
maximized at criticality.
Recent studies have shown that the architecture of inter-
nodal connectivity shapes the criticality properties, and a
localized, highly-modular topology gives rise to oscillatory
dynamics with long-range temporal correlations (37, 69, 70).
Furthermore, alterations in connectivity push the system
out of criticality towards a subcritical state (71). However,
the nature of the structure-function relations at different
critical-like states remains unknown.
Analyzing the structure-function relationships in the
model, we found that the magnitude of linear correlations
between the model’s structural connectivity and observables
of oscillatory dynamics was dictated by the model’s operating
point. The inter- and intra-areal synchronization had the
strongest correlation with structural connectome in the
subcritical region and linear structure-function relationship
broke down at criticality. On the other hand, the correlation
of inter-areal amplitude correlations and DFA exponent with
structural connectivity peaked at criticality and vanished in
both sub- and supercritical phases.
The brain criticality framework posits that a brain oper-
ates at the phase transition which was shown on microcircuit
level (72). On a whole-brain scale level in humans, it was
shown that models tuned to criticality (73, 74) and models
operating in the region of metastability (45, 75) achieves
the highest correlation with functional connectivity in MEG
and fMRI recordings. But physiological plausibility of other
observables and expecially several of them simultaneously
has remained terra incognita.
In this study, we extended the research and included
LRTCs and cross-correlation to the palette of observables.
We found that the highest correlation between simulated
and MEG-derived observables is achieved on the subcritical
slope of the critical regime – not at its peak. Furthermore,
the correlation between signatures of critical-like dynamics,
such as the DFA exponent and order cross-correlation, was
negative on the supercritical side of the critical regime. This
finding suggests that the critical regime in human brains may
be wider than what is observed in the model.
The power spectrum is one of the fundamental methods to
investigate and operationalize oscillations and prior studies
have suggested multiple mechanistical principles underlying
power spectrum properties. On a neuronal-population level
the hybrid models has achieved a great success with mimicing
the individual spectral properties (76), and on a macro-scale
it was revealed that physiologically plausable power spectrum
is observed within the critical region of high metastability
(45).
Here, we show that the PSD shape is defined by the
both distribution of underlying oscillators frequencies and
the position in the critical space. We found that the model is
able to reproduce the spectral characteristics with the highest
correlation between simulated and MEG power spectra
around the subcritical side of the extended critical regime with
high local and low global control parameters. Varying these
parameters changes the rhythmic properties from an almost
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
