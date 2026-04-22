---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 6
chunk_count: 10
char_count: 8464
---

control parameters, grew with
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

<!-- page:7 -->
DRAFT
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
Fig. 4. The model observables on the subcritical slope of the Griffiths Phase are the most similar to those found in MEG recordings. A. MEG analysis pipeline: MEG
recordings are source-modeled to derive parcel-level time series, filtered into narrowband signals (e.g., using Morlet wavelets), and analyzed to compute observables such
as phase synchronization matrices. B Modeling pipeline: The SC-informed Kuramoto model is used to simulate time series, from which the same observables (e.g., phase
synchrony, DFA exponent) as in MEG data are computed. Pearson correlations are calculated between MEG and model observables at the parcel (node) level to quantify
structure-function similarity. C The 95th percentile of the Pearson correlation coefficient across the KL-surface between MEG and model observables as a function of frequency.
The dashed horizontal line indicates the statistical significance threshold determined via spin-permutation tests. The vertical dashed line highlights the frequency at which the
correlation peaks. D-H Correlation maps and KL-surface slices for observables at the peak frequency identified in C. The Pearson correlation coefficient between simulated and
MEG-derived DFA exponent (E), average phase-synchrony of a node (D), average cross-correlation of a node (F, edge phase synchrony (G) and edge cross-correlation (H) as
a function of local (K) and global (L) coupling coefficients for frequency with maximum 95th percentile (see C). Black thick contours in the heatmaps indicate regions with
statistically significant correlations (p < 0.01) based on spin-permutation tests. Black dashed contours delineate the critical regime (as defined in Figure 2). The line plots at
the bottom represent a slice of the KL-surface for the same L = 4.
and real data could be explained by this drift in the power
spectrum properties ( See Figure 5E).
These findings suggest that operating near criticality
achieves a precise balance in spectral properties. This balance
enables the model to generate significant peaks in the power
spectrum, closely reproduce MEG-derived PSDs, and prevent
collapse into a singular frequency maintaining a bimodal
spectrum.
Discussion
Neuronal oscillations are fundamental to brain function and
exhibit significant inter-areal and inter-individual variability
in synchronization dynamics.
Computational modeling
approaches are emerging as central tools for understanding
the systems-level mechanisms that determine the local and
inter-areal synchronization dynamics of neuronal oscillations
in brain health and disease.
This study presents a whole-brain-scale Hierarchical Ku-
ramoto network model, which replicates key features of in vivo
human brain dynamics and generates novel, experimentally
Myrov et al.
PNAS
—
January 6, 2025
—
vol. XXX
—
no. XX
—
7
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

<!-- page:8 -->
DRAFT
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
Fig. 5. Critical-like state supports multi-frequency spectral properties A Oscillator frequency distribution derived from parcel-level power spectral density (PSD) of real
MEG recordings (left panel), with the 1/f component subtracted (middle panel) and are individually set for mode node that corresponds a brain area (right panel). B Average
PSD across model nodes (blue) compared with MEG-derived PSD (gray) for three regimes: subcritical, critical, and supercritical. Dashed vertical lines indicate the alpha (∼9.8
Hz) and beta (∼19.5 Hz) frequency peaks. The critical model aligns closely with MEG-derived PSD, while subcritical and supercritical regimes deviate. C Pearson correlation
coefficient between MEG-derived and simulated PSDs as a function of local (K) and global (L) coupling strengths (upper panel). The black contour highlights the critical ridge,
defined by DFA exponent (DF Aexp ≥0.65). The semi-transparent area indicates regions without significant spectral peaks. Bottom panel: Correlation coefficient (orange)
and average DF Aexp (blue) as functions of local coupling (K) for a fixed global coupling (L = 20). DModel PSDs for different combinations of local (K) and global (L) coupling
strengths, color-coded by their correlation with MEG-derived PSDs, as shown in C. Simulated spectra with critical-like dynamics exhibit the most realistic multi-peak structure. E.
Difference between simulated and MEG alpha peak frequencies (∆Falpha) averaged across model nodes as a function of control parameters. The white contour highlights
regions with significant alignment of alpha peaks. Bottom panel: ∆Falpha (orange) and average DF Aexp (blue) as functions of local coupling (K), indicating the region of
optimal alpha frequency alignment with critical-like dynamics.
.
testable predictions.
Each node in the model represents
a meso-scale neuronal population, encapsulated by a large
ensemble of Kuramoto oscillators corresponding to cortical
parcels and subcortical regions.
As established in prior
art of whole-brain model studies, these nodes are then
connected into a whole-brain network with coupling that
is proportional to the counts of individual white-matter
axonal fibers connecting each parcel pair ( See Figure
1).
This approach enables realistic local synchronization
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
