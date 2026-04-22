---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 1
chunk_count: 10
char_count: 6946
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
