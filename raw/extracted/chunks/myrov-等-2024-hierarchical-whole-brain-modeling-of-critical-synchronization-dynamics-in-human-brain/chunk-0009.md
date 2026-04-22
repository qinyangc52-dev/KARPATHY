---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 9
chunk_count: 10
char_count: 11235
---

dical Imaging
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

<!-- page:11 -->
DRAFT
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
focus on a cross displayed at the center of the screen in front of
them.
T1-weighted anatomical magnetic resonance imaging (MRI)
and diffusion weighted imaging (DWI) scans were obtained with
a 3 Tesla whole-body MRI scanner (Magnetom Skyra, Siemens,
Munich, Germany) at AMI Centre, Aalto University using a 32-
channel head coil. T1-weighted MRI data were recorded with a
resolution of 0.8×0.8×0.8 mm, repetition time of 2530 ms, and
echo time of 3.42 ms. DWI data were recorded with a resolution
of 3.0×3.0×3.0 mm, repetition time of 4100 ms, and echo time of
105 ms.
The study protocol for MEG, MRI, and DWI data was approved
by the HUS ethical committee (HUS/3043/2021, 27.4.2022),
written informed consent was obtained from each participant prior
to the experiment, and all research was carried out according to
the Declaration of Helsinki.
MEG data preprocessing and source modeling. Data preprocessing
and source modeling were performed using the MNE software
package (https://mne.tools/stable/index.html). Temporal signal space
separation (tSSS) in the Maxfilter software (Elekta Neuromag
Ltd., Finland) was used to suppress extracranial noise from MEG
sensors, interpolate bad channels, and compensate for head motions.
Independent components analysis was used to identify and remove
components that were correlated with ocular (using the EOG
signal), heart-beat (using the magnetometer signal as reference),
or muscle artefacts.
We used the FreeSurfer 7.3.2 software (https://surfer.nmr.mgh.
harvard.edu/) for volumetric segmentation of MRI data, surface
reconstruction, flattening, and cortical parcellation.
Source
reconstruction was performed with minimum norm estimation
(MNE) using dynamic statistical parametric maps (dSPM). A
surface-based source space with 5 mm spacing and 1 layer (inner
skull) symmetric boundary element method (BEM) was used in
computing the forward operator, and noise covariance matrices
were obtained from preprocessed data filtered to 151-249 Hz. We
then estimated vertex fidelity to obtain fidelity-weighted inverse
operators to reduce the effects of spurious connections resulting
from source leakage and collapsed the inverse-transformed source
time series into parcel time series in a manner that maximizes the
source-reconstruction accuracy (82, 83). Source time series were
collapsed to the 200 parcels of the Schaefer atlas (84).
In this study, we used complex Morlet wavelets to obtain a
narrow-band representation of a MEG signal (85). 50 Hz line-noise
and it’s harmonics were suppressed with a notch filter with 1 Hz
band transition widths. The band-pass (1-249 Hz) filtered data
were then separated into narrow frequency bands with 41 equally
log-spaced Morlet wavelets with frequencies ranging from 1 Hz to
100 Hz (number of cycles in a Morlet Wavelet = 5.0).
DWI data preprocessing. The DWI data preprocessing, including
denoising and motion correction, was conducted using the MRtrix3
3.0.1 Toolbox (86) and FMRIB Software Library (FSL) 6.0.5
(87).
To lessen potential biases or artifacts arising during
image acquisition or processing, the Advanced Normalization
Tools (ANTs) 2.3.5 was used (88). For T1-weighted anatomical
MRI data preprocessing, creation of head models and cortical
surface reconstruction, we used the open-source FreeSurfer 7.3.2
software (available at https://surfer.nmr.mgh.harvard.edu/, (89)). In
the subsequent step, Constrained Spherical Deconvolution (CSD)
(90) was employed to determine the fiber orientation distributions
(FODs) within each voxel, allowing for the accurate decomposition
of the diffusion signal into individual fiber orientations. In order to
improve the accuracy of fiber tracking, anatomically-constrained
tractography (ACT, (91)) was also applied by incorporating
anatomical information through the five-tissue-type (5TT) seg-
mentation derived from diverse brain tissues. The resulting FODs
provided a detailed map of white matter tracts. For tractography
construction, the principal diffusion direction was obtained from
each of the 20 000 000 seed points. To refine the quality of the
diffusion image and minimize tractogram reconstruction biases, we
applied the Spherical informed filtering of tractograms approach
(SIFT2, (92)).
T1-weighted anatomical MRI and DWI coregistration was
performed using the Spm 12 package within MATLAB R2022a
software. All preprocessing steps were executed on the CentOS
Linux operating system, operating on the Triton high-performance
computing cluster at Aalto University.
Following preprocessing, structural connectomes (SCs) were
constructed as edge-adjacency matrices representing the count of
white matter connections between parcelled cortical and subcortical
brain regions. The resulting matrices are symmetric, reflecting
undirected pairwise connections between brain regions (nodes).
The nodes correspond to the 200 parcels of the Schaefer atlas (84),
matched with Yeo 17 networks (93).
ACKNOWLEDGMENTS.
We
thank
Sheng
Wang,
Felix
Siebenh¨uhner and Joonas J. Juvonen for feedback about the study.
We also thank professor Guido Nolte on helpful comments on an
earlier version of the manuscript. This study was supported by the
Academy of Finland (J.M.P., project numbers: 296304), by the
Juselius Foundation ( S.P and J.M.P project number 240156).
1. G Arnulfo, J Hirvonen, L Nobili, S Palva, JM Palva, Phase and amplitude correlations in
resting-state activity in human stereotactical eeg recordings. NeuroImage 112, 114–127
(2015).
2. G Arnulfo, et al., Long-range phase synchronization of high-frequency oscillations in human
cortex. Nat. Commun. 11 (2020).
3. N Williams, et al., The influence of inter-regional delays in generating large-scale brain
networks of phase synchronization. NeuroImage 279, 120318 (2023).
4. S Palva, JM Palva, Discovering oscillatory interaction networks with m/eeg: challenges and
breakthroughs. Trends Cogn. Sci. 16, 219–230 (2012).
5. MJ Brookes, et al., Investigating the electrophysiological basis of resting state networks
using magnetoencephalography. Proc. Natl. Acad. Sci. 108, 16783–16788 (2011).
6. M Siems, AA Pape, JF Hipp, M Siegel, Measuring the cortical correlation structure of
spontaneous oscillatory activity with eeg and meg. NeuroImage 129, 345–355 (2016).
7. P Fries, Rhythms for cognition: Communication through coherence. Neuron 88, 220–235
(2015).
8. M Vinck, et al., Principles of large-scale neural interactions. Neuron 111, 987–1002 (2023).
9. M Schneider, et al., A mechanism for inter-areal coherence through communication based
on connectivity and oscillatory power. Neuron 109, 4050–4067.e12 (2021).
10. JM Palva, S Monto, S Kulashekhar, S Palva, Neuronal synchrony reveals working memory
networks and predicts individual memory capacity. Proc. Natl. Acad. Sci. 107, 7580–7585
(2010).
11. H Haque, M Lobier, JM Palva, S Palva, Neuronal correlates of full and partial visual
conscious perception. Conscious. Cogn. 78, 102863 (2020).
12. F Siebenh¨uhner, SH Wang, JM Palva, S Palva, Cross-frequency synchronization connects
networks of fast and slow oscillations during visual working memory maintenance. eLife 5
(2016).
13. SH Wang, et al., Neuronal synchrony and critical bistability: Mechanistic biomarkers for
localizing the epileptogenic network. preprint (2023).
14. LI Boon, et al., A systematic review of meg-based studies in parkinson’s disease: The motor
system and beyond. Hum. Brain Mapp. 40, 2827–2848 (2019).
15. S Pusil, et al., Hypersynchronization in mild cognitive impairment: the ‘x’model. Brain 142,
3936–3950 (2019).
16. G Alamian, et al., Alterations of intrinsic brain connectivity patterns in depression and
bipolar disorders: A critical assessment of magnetoencephalography-based evidence.
Front. Psychiatry 8 (2017).
17. S Zhang, et al., Association between abnormal default mode network activity and suicidality
in depressed adolescents. BMC Psychiatry 16 (2016).
18. RH Kaiser, JR Andrews-Hanna, TD Wager, DA Pizzagalli, Large-scale network dysfunction
in major depressive disorder: A meta-analysis of resting-state functional connectivity. JAMA
Psychiatry 72, 603 (2015).
19. Y Mohammadi, MH Moradi, Prediction of depression severity scores based on functional
connectivity and complexity of the eeg signal. Clin. EEG Neurosci. 52, 52–60 (2020).
20. G Buzs´aki, CA Anastassiou, C Koch, The origin of extracellular fields and currents–EEG,
ECoG, LFP and spikes. Nat. Rev. Neurosci. 13, 407–420 (2012).
21. S Palva, S Monto, JM Palva, Graph properties of synchronized cortical networks during
visual working memory maintenance. NeuroImage 49, 3257–3268 (2010).
22. J Simola, et al., Genetic polymorphisms in comt and bdnf influence synchronization
dynamics of human neuronal oscillations. iScience 25, 104985 (2022).
23. C Micou, T O’Leary, Representational drift as a window into neural and behavioural
plasticity. Curr. Opin. Neurobiol. 81, 102746 (2023).
24. WL Shew, D Plenz, The functional benefits of criticality in the cortex. The Neurosci. 19,
88–100 (2012).
25. DR Chialvo, Emergent complex neural dynamics. Nat. Phys. 6, 744–750 (2010).
26. K Linkenkaer-Hansen, VV Nikouline, JM Palva, RJ Ilmoniemi, Long-range temporal
correlations and scaling behavior in human brain oscillations. The J. Neurosci. 21,
1370–1377 (2001).
27. JM Beggs, D Plenz, Neuronal avalanches in neocortical circuits. The J. Neurosci. 23,
11167–11177 (2003).
Myrov et al.
PNAS
—
January 6, 2025
—
vol. XXX
—
no. XX
—
11
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
