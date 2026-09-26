# BB11 is an outlier: what brightness and orbital-drag proxies show—and what they do not

**Independent research note | Evidence cutoff: September 25, 2026 | Version 1.4**

## Executive summary

I investigated whether public orbital data and purchased optical observations support the claim that BlueBird 11 is already fully deployed and merely awaiting an announcement.

**They do not establish that claim. Instead, BB11 differs markedly from the deployed comparison satellites in two deployment-sensitive observables: optical brightness and fitted orbital-drag proxies.** Neither observable directly measures array opening.

In the strongest Slingshot brightness comparisons, BB11 was approximately **18–31 times fainter than deployed BB6 across three dates**. Sparse public observations also put BB11 **37–143 times fainter than deployed launch mates BB12/13**. In two standard-GP orbital snapshots, BB11’s fitted drag term was substantially below BB12/13. In the later snapshot it was **62–69% below each of five deployed controls**, whose values clustered much more closely together.

My working thesis is an unresolved difference in BB11’s deployment or commissioning, potentially involving a malfunction. That explanation deserves more consideration than an assumption that full deployment is complete and good news is imminent. However, different attitude or operating mode remains a credible alternative. I cannot establish a mechanical fault, permanent loss, percentage open, or current communications-payload health.

My background judgment is that the company is troubleshooting an unresolved technical problem, rather than withholding a completed-deployment success story. That is a personal working assumption, not an inference that the measurements can establish.

The evidence narrows several observational explanations but does not localize a failed subsystem. Tracking an object establishes continued orbital presence at the observation time; it does not establish power, commandability, array integrity or mission capability.

This is an exploratory, AI-assisted investigation, not a peer-reviewed spacecraft diagnosis. The public-data calculations are supplied for independent checking. No insider information is used.

## 1. Question and source data

The question is not whether BB11 is in orbit. It is whether its observed behavior resembles independently confirmed-open satellites closely enough to justify assuming successful full deployment.

I used three evidence sets:

| Source | Contents and use | Main limitation |
|---|---|---|
| Slingshot tracking exports | 110 BB11 tracks and 322 control tracks for BB6/8/9/10, September 15–25; 9,872 angular observations and 7,574 brightness values in total | Commercial raw data; unverified redistribution rights; no demonstrated common calibrated bandpass |
| Public IAU CPS SCORE observations | Historical brightness, range, phase, observer and instrument metadata; launch-mate and deployed-control comparisons | Sparse visual observations, uneven coverage and unknown array orientation |
| CelesTrak GP and SupGP records | Fitted orbital elements, drag parameters and forecast comparisons | Sparse saved snapshots; no covariance, full historical series, maneuver reconstruction or atmospheric correction |

[SCORE](https://score.cps.iau.org/) is the public optical source. The repository includes seven selected raw SCORE responses totaling 566 records, including BB6/8/9/10/11/12/13; not every record qualifies for a matched comparison. Earlier work also inspected 552 Block 1 observations, but those are not the central comparison here.

The orbital analysis distinguishes standard **GP**, fitted to tracking observations, from **SupGP**, derived from operator-provided orbital data. They are not interchangeable physical drag measurements. [GP documentation](https://www.celestrak.org/NORAD/documentation/gp-data-formats.php) · [SupGP sources](https://www.celestrak.org/NORAD/elements/supplemental/)

The latest actual BB11 photometry in my archive ends at **September 25 00:21:52 UTC—September 24, 5:21:52 p.m. Pacific**. Later orbital epochs do not constitute newer brightness observations.

## 2. Establishing deployed controls and checking identity

The company’s June-quarter filing confirms prior deployment of BB6 and BB8–10. AST’s public company account separately confirms full deployment of BB12 and BB13. Those launch mates are particularly useful controls because they share BB11’s launch and similar orbital geometry. [SEC filing](https://www.sec.gov/Archives/edgar/data/1780312/000119312526342550/asts-20260630.htm) · [Company account](https://www.linkedin.com/company/ast-spacemobile)

An important correction: an earlier version of my investigation left BB12/13 unverified. Their company confirmation predates the September observations; verifying it strengthens the interpretation of those comparisons.

I also found a cross-source identity discrepancy: the Slingshot BB8-labeled angles fit the catalog BB10 orbit, and vice versa. I preserved original labels and used the best-fitting orbit for geometry. Both identities are deployed controls. The main BB11–BB6 result and BB11/12/13 public comparisons are unaffected. I do not know which source’s labeling is responsible.

## 3. Optical methods and results

Brightness depends strongly on distance. I normalized magnitude to 1,000 km:

`m1000 = observed magnitude − 5 log10(range / 1000 km)`

For the principal Slingshot comparison, I required the same camera and UTC date, elevation at least 20°, phase difference no more than 3°, elevation difference no more than 5°, range ratio no more than 1.25, small angular-model residuals, and full sunlight with a margin from the modeled Earth limb. I matched frames without reuse within a satellite pair/camera/date, collapsed them to pass pairs, and required at least five paired frames.

| Date, UTC | Comparator | Paired frames | BB11 deficit | Comparator/BB11 flux |
|---|---|---:|---:|---:|
| September 19 | BB6 | 17 | 3.716 mag | 30.6× |
| September 20 | BB6 | 12 | 3.485 mag | 24.8× |
| September 22 | BB6 | 20 | 3.163 mag | 18.4× |

These are **three dates against one control**, not 49 independent deployment tests. Matching choices were exploratory rather than preregistered. Tighter and looser matching retained the broad brightness-deficit result.

The public SCORE comparisons use the same observer, instrument designation, filter, site and date, with phase differences within 3°. The launch-mate subset consists of visual/CLEAR observations, not calibrated camera photometry.

| September 16 comparison | BB11 deficit | Comparator/BB11 flux |
|---|---:|---:|
| BB11 versus BB12 | 4.026 mag | 40.8× |
| BB11 versus BB13 | 5.385 mag | 142.6× |
| BB11 versus BB13, second observation | 3.930 mag | 37.3× |

There are only **two unique BB11 measurements on one date** behind those three pairs. BB12 and BB13 themselves differed by 1.359 mag, or 3.50×, in the matched September 16 comparison; their September 17 contrast was 0.478 mag, or 1.55×, in the opposite direction.

BB11 is therefore much farther from both launch mates than they are from each other in this small sample. But deployed satellites can vary substantially: broader matched Slingshot control comparisons reach 3.30 mag, and older public SCORE comparisons among open BB8/9/10 reach approximately 4.1 mag. Faintness is not a universal failure threshold.

## 4. Orbital-drag proxies and control agreement

The relevant standard-GP snapshots are around September 23 23:40 UTC and September 24 20:20 UTC for BB11–13. The later BB8–10 records are from approximately 22:00–23:15 UTC on September 24.

BSTAR is a fitted parameter used by SGP4. I treat it as a drag-related proxy, not a direct area or drag-acceleration measurement.

| Satellite | September 24 BSTAR, ×10^-5 inverse Earth radii |
|---|---:|
| **BB11** | **2.540** |
| BB12 | 6.738 |
| BB13 | 7.508 |
| BB9, catalog identity | 7.747 |
| BB10, catalog identity | 8.148 |
| BB8, catalog identity | 8.316 |

The max/min spread is **11.4% for BB12/13**, **7.3% for BB8–10**, and **23.4% across all five controls**. BB11 is **62.3–69.5% below each control**, at 33.0% of the five-control mean. In the preceding snapshot, BB11 was also well below BB12/13, at 39.7% and 37.3% of their respective values.

BB6’s later snapshot has an even larger BSTAR, but its different altitude, epoch and orbital plane make it a less direct drag comparator. I do not claim to have tested every deployed BlueBird or every deployed attitude state.

As a descriptive cross-check, changes in fitted mean motion correspond to Kepler semimajor-axis proxies decreasing by 3.68 m/day for BB11 versus 9.24 and 9.66 m/day for BB12/13. These are **not independently measured physical decay rates**: they come from the same two fits, involve only metre-scale changes, and lack error covariance. They cannot be counted as another independent detection.

The close control agreement makes BB11 a marked outlier in these records. It does not justify a Gaussian “sigma” claim based on two close launch mates.

## 5. Why orbital proximity helps—but does not settle causation

BB11/12/13 have very similar average orbital altitude and nearly the same plane. At a common propagated time, BB11’s plane differed from BB12’s by about 0.009° and BB13’s by 0.043°.

They are nevertheless separated along the orbit: approximately 1,700 km and 5,250 km from BB11 at that time. They do not occupy identical atmospheric conditions. BB8–10 belong to another orbital plane. Similar altitude and launch cohort reduce confounding without eliminating density, attitude, thrust, or fitting differences.

“Attitude” means orientation. It affects **both** brightness and aerodynamic area: a deployed array seen or flown edge-on can behave differently from one presented broadside. Those viewing and flight directions differ. Attitude-driven drag changes are physically established, including in [NASA’s EO-1 differential-drag work](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20170010724.pdf).

Assuming all deployed satellites use similar attitudes is a useful conditional assumption—not an observation of BB11’s attitude. Assuming random attitudes instead requires modeling the expected distribution; it does not automatically strengthen the deployment inference.

## 6. Combining the evidence

| BB11 relative to comparator | Optical flux ratio, Sep 16 | GP BSTAR ratio, Sep 24 |
|---|---:|---:|
| BB12 | 0.0245 | 0.377 |
| BB13 | 0.0070–0.0268 | 0.338 |

Both differences point in a direction compatible with less exposed area. The agreement among deployed controls makes the combined pattern more concerning than brightness alone.

However, the optical suppression is much larger than the drag-proxy suppression. Under a deliberately restrictive model where one area multiplier controls both, with all other factors unchanged, the drag ratios predict only about 1.1 mag of faintness. The observed deficits are 3.9–5.4 mag. Even partial deployment therefore needs additional orientation, reflectance, dynamics or time-evolution effects to explain the observations quantitatively.

The datasets are about a week apart. They are not a simultaneous measurement of a single configuration, and both signals share attitude as an unknown. I did not multiply two “deployment probabilities” or fit a calibrated joint classifier. No reliable percentage open follows.

## 7. Checks that prevent misleading conclusions

- **Eclipse:** the latest optical pass ends with approximately 5.23% of the Sun visible in the model. Its terminal fading is not independent evidence of failure. Earlier parts of the fade need not be explained entirely by eclipse.
- **Periodicity:** none of 71 eligible tracks produced persuasive periodicity after multiple-search adjustment. This does not exclude tumbling.
- **Newer SupGP:** comparing saved and newer September 25 fits at common times does not reveal a distinctive BB11 revision. At 5 p.m. Pacific their predicted positions differ by 58 m for BB11, 52 m for BB12 and 65 m for BB13. These are forecast differences, not maneuver measurements.
- **Missingness and calibration:** absent magnitudes are not treated as nondetections. Different sensors, bands, viewing conditions and selection effects prevent indiscriminate pooling.
- **Historical coverage:** two GP snapshots are not a full drag history. Backward propagation is not a substitute for contemporaneous orbit fits or a covariance-based maneuver analysis.

## 7a. Can sparse sampling make a deployed satellite look like BB11?

I tested this directly by treating known-deployed satellites as unknown targets. Each simulated experiment preserves one target and one comparator across three distinct dates, clusters observations by pass/date, and does not reuse one extreme day as several observations. Sources remain separate.

In 100,000 draws per source, none of the eligible control subsets reproduced BB11’s three-date median deficit of 3.485 mag with every date at least 3.163 mag. Exhaustive enumeration confirmed the result across 194 oriented broader-Slingshot three-date cases and 80 historical SCORE cases. Those cases share observations; they are not 274 independent experiments. A further 20,000 sparse-frame trials also produced no match.

The largest three-date median among these controls was 2.496 mag in Slingshot and 0.846 mag in SCORE. The closest Slingshot case had a minimum-day deficit of only 0.512 mag, versus BB11’s 3.163 mag. However, **single deployed-control passes do reach about 4.1 mag**: it is the persistent pattern, not faintness on one occasion, that the available controls fail to reproduce.

The strictest Slingshot control subset lacks three dates per pair, so the identical-geometry test cannot be run; the simulation uses a broader elevation cut. Most sparse-frame trials have at least one control pass with fewer frames than the corresponding target pass. No simulated trial models unseen attitude states or unknown systematic errors.

An exhaustive drag-snapshot check also found no comparable deployed pseudo-target: the lowest ratio against two other controls was 0.818 among BB8/9/10/12/13, versus BB11’s 0.357 against BB12/13. This is not an independent time-series significance test.

**Zero matches does not mean a less-than-one-in-100,000 chance of full deployment.** The simulation repeatedly samples a small finite dataset, and cannot invent configurations absent from it. It strengthens the descriptive anomaly without identifying its cause. Details and a public SCORE reproduction script are included in `MONTE-CARLO.md` and `reproduce_monte_carlo.py`.

## 8. Parsimony and competing technical explanations

An unresolved deployment or commissioning issue is my leading low-confidence working hypothesis. A technical malfunction is plausible, but the observations do not identify its mechanism. This explanation is conditional on BB11 otherwise being expected to resemble its deployed peers operationally.

Two broad alternatives remain: less deployed/exposed array area, or a fully deployed spacecraft using a different attitude or operating mode. Both can affect reflected light and aerodynamic exposure. A fault in power, commanding or attitude control could also prevent deployment without any failed array hardware. “Deployment incomplete” describes a state; “deployment mechanism broken” specifies a cause. The former does not establish the latter.

A simple area multiplier does not quantitatively explain both observed ratios. Accordingly, parsimony favors investigating a shared configuration/operating-state difference, but does not uniquely identify mechanical damage. The company’s missing BB11-specific full-deployment confirmation leaves the state unresolved; it is not a measurement of hardware condition or management intent.

### My judgment about the background story

**My working assumption is that BB11 has encountered a technical problem and that the company is managing an unresolved situation. I find that explanation more convincing than the idea that deployment is complete and management is simply preparing a positive surprise.** This is my judgment about the background story; it is separate from the limited causal confidence of the measurements above.

I put weight on the combination: BB11’s measured differences, the tighter agreement among deployed controls, and the absence of the BB11-specific deployment confirmation that the company provided for BB12 and BB13. I do not regard an imminent success announcement as the default explanation for that pattern.

The coherent scenario I would investigate first is that the team is diagnosing the problem, assessing whether BB11 can be recovered, and checking whether the same issue has implications for spacecraft still on the ground. If so, cautious communication while that work proceeds would make operational sense. I suspect the company would want to understand the scope and recovery options before making statements that could later prove premature.

**In that sense, my background thesis is troubleshooting and damage control, rather than a deliberately withheld success story.** I am not using “damage control” to allege deception, to diagnose physical damage, or to claim knowledge of internal decisions. It describes the technical-response scenario I consider most plausible.ok  done  

A connection to later spacecraft readiness would make this account more coherent, but it is an additional assumption. The August business update described BB14–16 as approaching shipment, while the later company update distinguished the completed BB14 from BB15/16 still nearing completion. Those statements do not prove that BB11 caused a launch hold. I would not present that causal link as established. [August business update](https://www.sec.gov/Archives/edgar/data/1780312/000119312526342540/asts-ex99_1.htm) · [Company updates](https://www.linkedin.com/company/ast-spacemobile)

My thesis would weaken if dated evidence showed full deployment and a deliberate operating mode explaining the anomaly, or established unrelated causes for subsequent readiness changes. I am stating which background explanation I favor—not converting coherence into proof.

## 9. What can I rule out or constrain?

All boundaries below apply to the dated observations in this paper, not an unobserved later condition. “Disfavored” is not a statistical exclusion unless the measurement directly contradicts a narrowly stated claim.

| Proposed explanation or condition | What the evidence permits |
|---|---|
| Complete atmospheric reentry before the final optical observation | Inconsistent with a correctly identified BB11-associated object being observed in orbit on September 25 at 00:21:52 UTC. This does not prove the original spacecraft is structurally intact. |
| A mistaken BB12/13 target identity accounts for the BB11 light curve | Strongly disfavored by the angular identity checks among these candidates. This is not a comprehensive audit of every possible catalog association. |
| Different distance alone explains the optical deficit | Inadequate: the deficit persists after range normalization and range sensitivity checks. |
| Eclipse alone explains the repeated principal brightness deficit | Inadequate under the model: the principal matches require full sunlight and a limb-clearance margin. Eclipse does explain the endpoint of the latest pass. |
| One unusual frame/pass explains the entire result | Inadequate: the principal result repeats over three dates. Resampling the observed controls does not reproduce that persistence, though it cannot exclude unsampled configurations. |
| BB11 never established contact after launch | Contrary to the company’s historical report of initial contact, if that report is accepted. This is not independent verification or evidence of current commandability. |
| Rapid, regular tumbling is positively detected | Not supported by my period screen. Slow, rapid beyond cadence, intermittent or nonstationary rotation remains possible. |
| The entire spacecraft is currently powered, controllable and healthy | Not established by optical tracking or fresh orbital fits. Passive objects can be tracked and their ephemerides updated. |
| Catastrophic breakup, appendage loss or other structural damage | Not established, but not excluded. A tracked remnant can remain; no comprehensive debris-event investigation or resolved imagery was obtained. |
| A permanent operational or mission loss | Not established and not excluded. An object can remain in orbit after losing its intended function. |

AST’s public account relayed post-launch contact with BB11–13 and nominal initial operations. This is bounded historical evidence against a never-functioned-at-all launch outcome; it does not establish current power, telemetry, full array deployment, or broadband performance. [Company source](https://www.linkedin.com/company/ast-spacemobile)

### Distinguish three meanings of “total loss”

1. **No object remains in orbit:** inconsistent with the identified optical observation at its timestamp.
2. **No current spacecraft function remains:** my observations cannot rule this out. Sunlight reflection does not require electrical power.
3. **The intended mission is irrecoverable:** also unresolved. A powered, communicating spacecraft may still be unable to deploy or operate its payload.

Therefore I cannot responsibly write “it is not a total loss because it is being tracked.” Nor does the present evidence warrant declaring total loss.

### Remaining fault families

| Fault or operating-state family | Why it remains possible | Best discriminator |
|---|---|---|
| Commanded stowage or intentionally prolonged commissioning | Can retain low exposure without broken hardware | Dated operator confirmation of intended configuration and current command response |
| Deployment mechanism, release, hinge, latch or structural problem | Could leave a smaller or distorted array | Resolved imagery or deployment-position/current telemetry; no specific mechanism is diagnosed here |
| Attitude determination/control problem or safe mode | Can change brightness and drag, and may inhibit deployment | Attitude/rate telemetry, confirmed mode, or sustained attitude-resolved observations |
| Power, thermal or command-chain problem | Could prevent deployment or normal attitude without failure of the array itself | Current telemetry covering power, temperature, commands and mode transitions |
| Fully deployed but atypical commanded attitude | Could lower both optical reflection and aerodynamic exposure | Full-array image plus independently constrained orientation |
| Payload/RF failure with otherwise ordinary geometry | Cannot by itself explain geometric differences if those proxies reflect physical state; associated mode changes could connect them | Satellite-specific authenticated communications testing plus configuration evidence |

These are generic fault families, not claims about undocumented BB11 hardware. The data cannot bound the failure to one subsystem or determine recoverability.

## 10. How to narrow the problem next

The highest-value next evidence separates **current bus function**, **array geometry**, and **payload function**. They are different questions.

1. **Establish current commandability.** A dated operator statement or attributable two-way telemetry/command response would rule out complete contemporaneous loss of the communication/control path demonstrated by that test. A radio signal alone is insufficient without frequency, Doppler, timing and identity checks; payload service and spacecraft control links are distinct. My archive contains no such current verified test.
2. **Establish physical configuration.** A sufficiently resolved, dated image could discriminate stowed, partial and full deployment, and perhaps gross structural damage. Unresolved brightness cannot uniquely recover shape. I have not acquired such an image.
3. **Establish attitude and maneuver behavior.** A longer GP/independent orbit history, atmosphere-aware modeling and credible maneuver evidence could constrain low-drag orientation versus configuration change. A confirmed commanded maneuver would demonstrate some functioning subsystems at that time, not full payload or deployment health. Fit-to-fit differences alone are not that evidence.
4. **Quantify sensitivity to rotation.** Injection–recovery tests on the actual light-curve cadence could determine which periodic amplitudes and periods my screen would detect. Until that is done, “no detected period” cannot become “no tumbling.” Such tests would constrain regular optical modulation, not all attitude faults.
5. **Obtain simultaneous geometry-aware observations.** Matched BB11/12/13 photometry across several phases and dates, ideally with calibrated bands and multi-station coverage, can challenge a fully deployed orientation model. The model must include optical scattering, projected aerodynamic area, atmospheric uncertainty and possible thrust; it must not assume attitude is irrelevant to drag.
6. **Check structural-event evidence if warranted.** A catalog history/debris-event review and resolved observations could test breakup or appendage-loss scenarios. Absence of newly cataloged debris alone would not rule out uncataloged small fragments or an intact mission-dead spacecraft.

With current data, I can reject several simple observational explanations and identify an unusual configuration/operating-state signature. I cannot yet distinguish an intentional mode from a recoverable fault or a permanent mission failure. These proposed discriminators are future work, not tests already completed.

## 11. Reproducibility and sharing

The proposed repository is **`bb11-public-review`**. It contains this Markdown paper, selected public SCORE and CelesTrak snapshots, original observer identifiers, source notes, a standard-library Python reproduction script, generated CSV results, and the combined-evidence figure.

Run `python3 reproduce.py` offline to reproduce the core public-data comparisons. The supplemental SupGP script requires NumPy, pandas, astropy and sgp4. The commercial Slingshot raw files are excluded because redistribution permission has not been established. The reported commercial results are summarized here; they cannot be independently regenerated from the public bundle alone.

SCORE attribution and its documented CC-BY 4.0 terms accompany the data. Public accessibility does not erase third-party terms; no blanket license over source datasets is asserted. CelesTrak sources and saved epochs are preserved. SHA256 checksums identify the exact files used. The public review repository is https://github.com/eranbram2122/bb11-public-review. Download all files using Code → Download ZIP. The repository contains the public-data reproduction, not the purchased optical inputs.

### Conclusion

**BB11 is a marked outlier in the sampled optical observations and fitted GP drag parameters relative to the deployed comparison group.** Control agreement strengthens the anomaly, while unknown attitude, sparse orbital history, and mismatched observation dates limit causal inference.

An unresolved deployment or commissioning problem is my leading low-confidence explanation. A malfunction is plausible; permanent failure and a fleet-wide defect are not established. Current power, commandability, structural integrity and payload performance are not demonstrated by the tracking data. The next step is to distinguish array configuration from operating attitude and then establish subsystem function, rather than treating an orbital track as proof of spacecraft health.

My broader working thesis is troubleshooting and recovery assessment. The technical findings warrant that investigation, but they do not establish the internal response, a launch hold, or management’s motives.
