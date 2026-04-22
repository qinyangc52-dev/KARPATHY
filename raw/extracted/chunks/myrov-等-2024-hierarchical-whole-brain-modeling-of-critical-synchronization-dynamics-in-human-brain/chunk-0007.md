---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 7
chunk_count: 10
char_count: 8811
---

spectra, and rhythmicity (2, 40, 59, 63).
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
