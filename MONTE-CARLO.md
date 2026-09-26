# BB11 sparse-sampling Monte Carlo and exhaustive control checks

## Answer

Known-deployed satellites can produce a single optical deficit comparable with BB11: the historic SCORE sample reaches 4.10 mag. **None of the available control subsets reproduces BB11’s persistent three-date pattern**, and no eligible single-pass comparison with two controls reproduces the September 16 launch-mate pattern. This supports the unusualness of BB11 in the sampled data. It does not measure a deployment probability or validate a physical cause.

## Question and benchmark

Treat a confirmed-deployed satellite as the unknown target, restrict it to sparse observations, and ask whether it looks like BB11. The benchmark from the principal BB11–BB6 result is a three-date median deficit >=3.4851 mag and every date >=3.1627 mag. I also examine a relaxed definition requiring both thresholds within 0.5 mag, and a sensitivity relaxing both by 1.0 mag. These thresholds use the already observed target result; this is exploratory, not preregistered hypothesis testing.

A separate single-pass test asks whether a pseudo-target is at least 4.026 mag fainter than one control and at least 5.385 mag fainter than the other, matching the shared-measurement BB11/12/13 comparison. It preserves the same target pass for both edges.

## Sampling design

1. Retain the identity of a deployed pseudo-target and a fixed deployed comparator across a simulated three-date experiment.
2. Use matched pass summaries, not independent frame counts. Collapse multiple passes/cameras within each pair/date to a date median.
3. Choose three distinct dates without replacement. Repeating one extreme date three times is forbidden.
4. Sample eligible ordered satellite pairs uniformly; within each, sample the three-date subsets uniformly. Results depend on this chosen weighting and the observed sampling coverage.
5. Analyze Slingshot and SCORE separately; do not assume their bands or sampled conditions are interchangeable.
6. Repeat 100,000 times per eligible source, seed 20260926, and independently enumerate every possible three-date subset. Also condition on date spans <=3 calendar days, matching the principal BB11 span.

Strict Slingshot control matching leaves only one or two dates per pair. **The exact strict-geometry three-date test is not estimable.** I do not manufacture dates. The broader Slingshot analysis lowers the elevation cut to 10° while retaining other geometry cuts and the five-frame minimum. This is a robustness comparison, not perfectly identical coverage.

## Results

| Control source | Eligible ordered pairs | Distinct three-date cases | MC draws | Cases matching BB11 |
|---|---:|---:|---:|---:|
| Strict Slingshot | 0 | 0 | Not run | Not estimable |
| Broader Slingshot, elevation >=10° | 8 | 194 | 100,000 | 0 |
| Historical SCORE BB8/9/10 | 6 | 80 | 100,000 | 0 |

Ordered pairs include both directions of the same physical pair; cases share dates and satellites. They are not 274 independent experiments. The number of true satellites remains four in the Slingshot controls and three in SCORE.

The maximum attainable three-date median is **2.4959 mag** in Slingshot and **0.8457 mag** in SCORE, versus BB11’s 3.4851. The closest Slingshot case is the BB6 pseudo-target against the BB10-labeled export on September 23–25; its minimum date deficit is only **0.5121 mag**, versus BB11’s 3.1627. It therefore does not reproduce the sustained pattern, even with a 1-mag tolerance on both thresholds.

Restricting to a <=3-day span leaves 30 oriented Slingshot cases and six SCORE cases. None matches. In the simulations, 37,821 Slingshot and 8,357 SCORE draws meet this span restriction; these are subsets of the existing draws, not additional independent tests.

All results also fail the 0.5-mag relaxed sustained benchmark. None passes the 1.0-mag relaxed sustained benchmark. The largest Slingshot median alone is about 0.99 mag below BB11; the minimum-date condition is what makes the persistence distinction especially informative.

## Sampling fewer frames

A further 20,000 trials (seed 20260927) regenerate the original broader-geometry frame matches and check they reproduce all 34 control pass summaries. Each trial selects a fixed ordered satellite pair, three distinct dates, one matched pass pair per date, and samples 17, 12 and 20 frames without replacement, corresponding to BB11’s principal frame counts.

If a control pass has fewer frames, all available frames are used. **16,819 trials have at least one such smaller pool**, so this is a sparse-frame sensitivity, not an exactly frame-count-matched null experiment. Multiple frame differences within a pass remain correlated; random frame selection is not treated as extra independent satellite evidence.

No trial matches BB11’s median, persistent benchmark, or relaxed persistent benchmarks. Maximum simulated median remains 2.4959 mag. This tests within-observed-pass subsampling, not unseen atmospheric/calibration errors or unsampled attitude states.

## Single observations and two-control checks

Historical SCORE has two oriented pass contrasts >=3.485 mag, reaching 4.0977 mag. The broader Slingshot sample reaches 3.3009 mag. Thus the answer to “can a deployed satellite ever look comparably faint in limited data?” is **yes for a single pass**.

Requiring the same pseudo-target pass to be faint against two different deployed controls is more restrictive. There are 36 eligible broader Slingshot cases and 15 SCORE cases (plus three strict Slingshot cases). None reproduces the BB11 launch-mate benchmark. None is >=3 mag fainter than both controls. The greatest deficit against the brighter-of-the-two comparisons is not used alone: the maximum of the *smaller* paired deficits is 2.4959 mag in broader Slingshot and 0.6565 mag in SCORE. These cases share observations and are not independent.

## Drag and joint evidence

A finite leave-one-deployed-satellite-out check compares each control to pairs of other deployed controls. Across BB8/9/10/12/13 there are 30 role assignments. The lowest target-to-comparator-mean BSTAR ratio is **0.8185**, versus BB11’s **0.3566** against BB12/13. Including BB6 yields 60 role assignments and a minimum ratio **0.6794**. None resembles BB11’s low ratio.

This is an exhaustive snapshot comparison, not a temporal drag Monte Carlo. The identities share one epoch window and there is no representative attitude/drag history to resample. A calibrated joint brightness-and-drag null distribution cannot be estimated: the observations are not simultaneous, the satellite/date coverage differs, and attitude affects both. Multiplying optical and drag tail rates would be invalid.

## What zero hits means

Zero hits is an exact fact about the observed finite support, not “less than one in 100,000” physical probability. In particular, the broader Slingshot sample’s maximum single-pass median (3.30 mag) is already below the target three-date median (3.485 mag); resampling those summaries cannot create a larger value. The Monte Carlo quantifies the consequences of the sample, not its completeness.

No 99.999% confidence, binomial rule-of-three bound, deployment probability or malfunction probability is reported. Those would confuse numerical sampling precision with uncertainty about which deployed states are missing from the data. Full historical orbit data, more comparable deployed observations, calibrated errors, and attitude information remain absent.

## Effect on the conclusion

The control data do not reproduce BB11’s **persistent** optical anomaly under the tested sparse-sampling designs. Individual faint measurements can be ordinary; the repeated pattern is harder to reproduce in these controls. The orbital snapshot also lacks a comparable deployed pseudo-target.

This strengthens the empirical outlier characterization and argues against dismissing the result as merely a small number of frames. It does not exclude an unsampled fully deployed attitude mode, nor establish malfunction, management motives or launch causation. The leading delayed/incomplete-deployment interpretation remains a hypothesis with limited causal confidence.

Files: run.py, frame_sampling.py, settings.json, Monte Carlo summaries, full exact subsets, coverage and per-pair tables. Commercial-derived detailed outputs remain in the local analysis. The public repository adds the historical SCORE control summaries and a standalone public resampling script so that portion can be checked independently.
