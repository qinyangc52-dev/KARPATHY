---
source_extracted: "D:/X/Karpathy/raw/extracted/myrov-等-2024-hierarchical-whole-brain-modeling-of-critical-synchronization-dynamics-in-human-brain.txt"
chunk_index: 2
chunk_count: 6
char_count: 12845
---

dynamics emerges
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

<!-- page:3 -->
DRAFT
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
Fig. 1. General representation of an experimental pipeline. A Summary of imaging and data processing techniques, including T1-weighted MRI for anatomical parcellation,
DWI MRI for structural connectome reconstruction, and MEG for functional data acquisition. The figure illustrates MRI-based parcellation, structural connectivity matrix, and
MEG-derived population-level time series. B MEG signals from two parcels showing the broadband signal (gray) overlaid with the narrowband filtered component (10 Hz, Morlet
wavelet, ω = 7.5) and corresponding phase. Bottom: Phase heatmap of MEG signals across channels, with low-amplitude regions shown as transparent. C Power spectral
density (PSD) for two parcels in the MEG data. D Two-dimensional histogram of amplitudes for two MEG signals filtered in the narrowband. E Distribution of phase differences
between a pair of MEG signals, with a weighted phase lag index (wPLI) of 0.39. F Heatmap of pairwise amplitude correlations of alpha-band MEG signals (10Hz). G Pairwise
wPLI matrix of alpha-band MEG signals (10 Hz). modeling pipeline. H On top level, the model is made of multiple inter-connected nodes where each node represents a single
brain region. A node is comprised of huge amount (up to thousands) of basic Kuramoto oscillators with central frequency ω and intra-nodal coupling strength of Kn. The
average value across oscillators is used to obtain complex timeseries I Simulated time series and corresponding phase for two model nodes. J Power spectral density of the
real part of simulated time series. K Two-dimensional histogram of amplitudes for two simulated signals. L Phase difference distribution for two simulated signals, with an
example PLV value of 0.35. M Pairwise amplitude correlation heatmap for simulated time series. N Pairwise PLV matrix of simulated signals.
We then simulated resting-state activity (see Methods) and
computed the DFA exponent for each channel of the simulated
time series as a function of the local coupling coefficient (K)
and global coupling coefficient (L).
The hierarchical approach effectively modeled the critical
transition, and this transition featured a peak in the DFA
scaling exponent near 1, indicating critical-like dynamics ( See
Figure 2C). Interestingly, the position of the DFA exponent
peaks in the control parameter space vary between model
nodes, indicating inter-node variability that could be caused
by differences in node-level parameters.
Next, we created a cohort of structural-connectome-
informed models (N = 24) and analyzed the behaviour
of intra- and inter-node level observables.
At the nodal
level, we found that DFA exponent peaks during the phase
transition of node order and the breakpoint aligns with
maximum criticality ( See Figure 2D). It is worth noting, that
inter-subject variance emerges in slightly subcritical region
Myrov et al.
PNAS
—
January 6, 2025
—
vol. XXX
—
no. XX
—
3
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

<!-- page:4 -->
DRAFT
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
Fig. 2. Phase transition and emergence of critical-like dynamics in Hierachical Kuramoto Model. A Simplified representation of the parameter space, illustrating two key
control parameters: local coupling strength (K) and global coupling strength (L). Colored dots indicate three distinct parameter combinations representing subcritical, critical, and
supercritical regimes. B Example time series for subcritical, critical, and supercritical dynamics, corresponding to the parameter combinations in A. Right: Detrended Fluctuation
Analysis (DFA) fits and their exponents (DF Aexp) for each regime. C DFA exponent (DF Aexp) as a function of local coupling strength (K), where each line represents a
single model node. Black lines indicate nodes with significant DF Aexp peaks (DF Aexp ≥0.65), while gray lines represent nodes without significant peaks. The red
dashed line marks the significance threshold. D Average model order (blue) and DF Aexp (red) as a function of local coupling strength (K). The critical regime (shaded) is
defined as the region where more than 10% of nodes exhibit DF Aexp > 0.65. Shaded areas represent standard error (SE) confidence intervals (± SD
√
N , where N = 24
models). E Heatmaps of average order (left) and DF Aexp (right) across model nodes as functions of local (K) and global (L) coupling strengths. The white contour outlines
the critical regime, defined as regions where more than 10% of nodes have DF Aexp > 0.65. F Average Phase Locking Value (PLV, blue) and cross-correlation (CC, red) as
functions of local coupling strength (K). I Heatmaps of PLV (left) and CC (right) averaged across inter-nodal edges, as functions of local (K) and global (L) coupling strengths.
before the critical-like zone and also achieves a maximum
at criticality. On the KL surface – the DFA exponent as a
function of both control parameters – the critical region is
represented by a linear ridge and achieves a maximum when
local coupling is a bit lower than global ( See Figure 2E).
Inter-nodal interaction dynamics showed a transition from
near zero synchronization to almost perfect synchrony, the
cross-correlation peaking during the transition period and
matches the critical region assessed with LRTCS ( See Figure
2F,G). Unlike the DFA exponent which is maximized when
K > L, the cross-correlation achives the highest values when
L > K.
Similar results were reproduced with a log-transformed
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
