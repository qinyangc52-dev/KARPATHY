---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 5
chunk_count: 10
char_count: 8556
---

KL surface when DFA-structure cor-
relation was maximized at the critical region ( See Figure
3E).
At the inter-node level, the correlation between edge
strength and CC resembled the patterns observed with the
DFA exponent, peaking at criticality while remaining low in
both subcritical and supercritical zones ( See Figure 3H,I).
The correlation between PLV and edge strength exhibited a
Myrov et al.
PNAS
—
January 6, 2025
—
vol. XXX
—
no. XX
—
5
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

<!-- page:6 -->
DRAFT
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
unimodal shape, with a wide peak on the subcritical side and
dropping around the critical peak ( See Figure 3F). Unlike
other observables, the PLV showed higher correlation with
SC in regions where global coupling is stronger than local
coupling ( See Figure 3G).
As a result we found that the correlation between the
model structural properties explains observed oscillatory
dynamics differently for synchronization and criticality prop-
erties. The correlation between edge weights and intra/inter-
areal synchronization dips in the critical region but peaks
for LRTCs and cross-correlation.
Given these results we
hypothesize that synchronization will be the most sensitive to
internally-caused changed in coupling strength (e.g. plasticity-
induced) or external perturbation such as stimuli in subcrit-
ical system while LRTCs and cross-correlation will require
fewer changes to control at criticality.
Brain dynamics during the resting-state is the most cor-
related with observables in subcritical-critical region. The
model demonstrates a wide spectrum of self-organized dy-
namics from sub-critical to critical regimes, and we asked how
similar is the model activity to that observed in human resting-
state MEG recordings.
Narrow-band MEG signals were
derived by filtering broad-band MEG resting-state recordings
from 24 subjects using Morlet wavelets (ω = 7.5). Frequencies
ranged logarithmically from 2 Hz to 100 Hz across 41 bands.
From these signals, we computed key observables of oscillatory
dynamics, including the weighted Phase Lag Index (wPLI),
DFA exponents, and amplitude cross-correlation ( Figure
4A). For wPLI and CC we also included in the analysis the
average value across edges that belong to the same node.
Next, we developed a structural connectome (SC)-informed
model by initializing inter-node coupling strengths based
on an averaged structural connectome across subjects. For
simulated data we computed DFA exponents, PLV and
CC (both node and edge-level), and for MEG data we
computed the same observables but wPLI instead of PLV (
See Figure 4B). Finally, to evaluate the similarity between
real MEG recordings and simulated data, we estimated
Pearson’s correlation coefficients between observables from
model nodes/edges and MEG parcels/edges corresponding
to the same anatomical regions.
As a starting step, we analyzed the similarity between
model and MEG dynamics as a function of narrow-band
frequency. The model showed the most similar dynamics to
the low-frequency activity, particularly in the theta frequency
range (3–8Hz) for the DFA exponent and node- and edge-
level phase-synchrony. However, the amplitude correlation
exhibited several significant peaks including theta (4.2Hz),
alpha (12.3Hz) and beta frequencies (28.3Hz,
See Figure
4C).
Investigating the most-similar frequencies, we found that
the significant correlation for all observables included in the
analysis was found following the critical ridge ( See Figure 4D-
H), which supports the notion that the human brain operates
primarily in a subcritical-critical zone.
Interestingly, the
correlation coefficient for the DFA exponent and node-level
CC is positive on the subcritical side of the critical regime
but becomes negative on the critical-supercritical side ( See
Figure 4D,F) which may indicate that the critical region in
the human brain might be wider than observed in the model.
The spectral properties of oscillatory activity are shaped
by the distribution of underlying frequencies. Traditionally,
oscillations are quantified by their magnitude, often using
power spectral methods. Different system properties, such
as interaction delays, have been shown to regulate the shape
of the spectra and emergence of oscillatory modes. However,
in previous studies, the operating point of a system was not
considered.
To replicate individual power spectral properties in the
model, we aligned the oscillator frequency distribution with
the shape of the recorded power spectrum.
We achieved
this by first computing the power spectrum density (PSD)
of the MEG recordings and removing the 1/f component
using the FOOOF method (62).
The resulting PSD was
then transformed into a probability distribution of oscillator
frequencies by normalizing it with the cumulative sum.
For each model node, we sampled brain-region oscillator
frequencies from these distributions individually for each
MEG parcel ( Figure 5A).
To assess the similarity between real and simulated data,
we computed the PSD of the simulated and MEG data using
the Welch method, and estimated the Pearson correlation
coefficient between them. In addition, we estimated the model
frequency shift calculated by the absolute distance between
alpha peaks in model and MEG spectra.
Initially, we found that regions with low intra-nodal
coupling and high inter-nodal coupling in the subcritical
side showed low, non-significant peaks in the power spectrum.
In the supercritical model, a dominant peak appeared in the
power spectra at the alpha band. Additionally, the power
spectrum exhibited a slight drift toward the weighted average
of alpha (9.8 Hz) and beta (19.5 Hz) frequencies, calculated as
12.85 Hz weighted by frequency probability. In contrast, the
spectrum of the critical-like model was well-matched, with
the peaks corresponding to those observed in the real data (
See Figure 5B).
Since the properties of critical-like dynamics—particularly
the critical state’s position within the control parameter
space—depend on the oscillator frequency distribution, we
initially investigated whether a model with a heterogeneous
non-parametric frequency distribution exhibits such dynamics.
Our findings confirm that a model initialized with a non-
parametric distribution of oscillator frequencies does indeed
display critical-like dynamics and LRTCs emerge during
the phase transition at the same time preserving the multi-
frequency activity (see Supplementary Figure 3).
Analyzing the similarity between the model and the MEG-
derived power spectrum, we found that the highest correlation
was achieved on the subcritical side of the extended critical
regime, with high local and low global coupling strength and
it decays after the critical ridge where the alpha frequency
becomes the driving force ( See Figure 5C,D).
As the model transitioned from the subcritical to the
critical regime, oscillatory peaks began to emerge. These
peaks, largely absent at low control parameters, grew with
increasing coupling strength and became dominated by the
alpha band near the critical zone. Interestingly, the peaks
were well-aligned with the real data in the subcritical and
critical states, but in the supercritical regime, the alpha
and beta frequency peaks exhibited a small drift toward the
weighted average. The low correlation between the simulated
6
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
