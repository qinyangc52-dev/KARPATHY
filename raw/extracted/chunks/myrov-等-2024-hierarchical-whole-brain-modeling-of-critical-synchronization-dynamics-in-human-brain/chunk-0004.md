---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 4
chunk_count: 10
char_count: 4958
---

s were reproduced with a log-transformed
structural connectome (see Supplementary Figure 1), however,
the variability between critical peaks is lower and the
critical ridge is more narrow in contrast to the original non-
transformed SC. Consequently, the average DFA exponent
and CC are higher when using log-transformed edge weights.
This highlights that the emergence of LRTCs is not a
4
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

<!-- page:5 -->
DRAFT
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
Fig. 3. Modeling reveals diverse forms of Structure-Function coupling around the phase transition. A Analysis pipeline: The structural connectome (SC) of an individual
is used to construct an SC-informed Kuramoto model, where inter-nodal coupling weights are derived from the SC. The model generates oscillatory dynamics, from which
observables such as Phase Locking Value (PLV), DFA exponent (DF Aexp), order, and amplitude cross-correlation (CC) are computed. Structure-function coupling is
quantified as the correlation between these observables and structural measures (e.g., node strength or edge fiber count).B-E Correlation between model order and SC node
strength (B), DF Aexp and SC node strength (C), PLV and SC edge weight (D), node order cross-correlation and edge weight (E) as a function of local coupling strength (K).
Orange line indicates Pearson correlation coefficient (ρ) and the blue line average observable. Shaded areas represent confidence intervals (CIs) based on standard error
(SE). On the bottom, heatmaps showing the Pearson correlation coefficient between the respective observables and structural measures (node strength or edge strength) as
functions of local (K) and global (L) coupling strengths. The white contour outlines the critical regime consistent with Figure 2.
property of a specific structural architecture but is a general
phenomena.
Interaction-specific breakdown or maximization of structure–
function coupling at criticality. The structural connectome is a
backbone of functional relations in the brain and despite there
were numerious studies assessing their relations, criticality
was not taken into account. To analyze relationships between
the model’s structural architecture and oscillatory dynamics,
we computed the Pearson correlation coefficient using prior
simulations. We correlated node strength (average structural
connectivity of a node) with node-level observables (e.g.,
order, DFA exponent), and inter-node statistics (e.g., edge
strength of PLV/CC) were correlated with edge weights (
Figure 3A).
Investigating the structure-function correlations in the
model at the individual node level, we found that the node
order was positively correlated with Node Strength (NS,
average edge weight of each node), increasing slightly from
the subcritical to the critical region, dipping at criticality, and
increasing sharply at supercritical region ( See Figure 3B).
Notably, this correlation remains around zero independent of
the local coupling in a region with low but non-zero global
coupling parameter ( See Figure 3C).
The correlation between the DFA exponent and NS, on the
other hand, fluctuates around zero in the subcritical region,
peaking at criticality, and becoming strongly negative in the
supercritical zone ( See Figure 3D). A similar phenomenon
was observed on the KL surface when DFA-structure cor-
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
