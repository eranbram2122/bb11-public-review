# BB11 public review package

Start with [WHITE-PAPER.md](WHITE-PAPER.md). Version 1.4, evidence cutoff September 25, 2026.

This repository tests descriptive differences in optical brightness and fitted GP drag proxies. It does not establish deployment percentage, failure, management motives or a price forecast. AI-assisted calculations and writing have not been independently peer reviewed.

## Reproduce the public results

With Python 3 installed, from this folder:

```sh
python3 reproduce.py
```

No internet, account or third-party Python packages are needed. Outputs appear in `results/`. The script checks source counts, matching counts and a reference magnitude contrast. Raw SCORE observations preserve observer attribution.

To repeat the supplemental same-time orbit comparison, use an isolated Python environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-supgp.txt
.venv/bin/python compare_supgp.py
```

The two-snapshot Kepler axis changes in the core output are descriptive fitted-element proxies, not measured physical decay rates. The SupGP script compares predictions in TEME at identical times; differences are not measured maneuvers.

## Scope of reproducibility

The core script reproduces the paper’s public BB11/12/13 September SCORE matches, deployed-control BSTAR snapshot, and two-snapshot GP axis proxies. The optional script reproduces the newer SupGP comparison. The paper also summarizes a larger commercial optical analysis, periodicity and eclipse checks. Those are not reproduced by this public-only package. The old ~4.1-mag open-control example is documented in `HISTORICAL-SCORE-CONTEXT.md`; its selected raw records are included, but the core script does not recreate every historical analysis.

No raw Slingshot TDM, ICD, account identifiers, session data, credentials, or local Desktop paths are included. The commercial portion can be reproduced by researchers who lawfully obtain equivalent tracking data and implement the methods stated in the paper. Redistribution rights were not established during this work.

## Download and review

Use GitHub's **Code → Download ZIP** to download all files, or browse the data, scripts and results directly here. Unzip the download before running the scripts. Start with [WHITE-PAPER.md](WHITE-PAPER.md) and [MONTE-CARLO.md](MONTE-CARLO.md).

This public-data package excludes purchased Slingshot raw data. It reproduces the public-data portion of the investigation, not every result described in the paper. The evidence cutoff remains September 25, 2026.

## Independent review requests

Please report source identity errors, matching mistakes, reproduction discrepancies, or comparable deployed satellites that challenge the interpretation. Include exact dates, catalog identifiers, observation IDs and methods. A longer GP history, density/maneuver model or independently established attitude would improve causal inference.

Source terms remain with their respective providers. See [ATTRIBUTION.md](ATTRIBUTION.md). No blanket license over third-party material is asserted.

## Sparse-sampling follow-up

Run `python3 reproduce_monte_carlo.py` to repeat the public SCORE resampling and exact enumeration. It consumes the included historical public pass summaries; those upstream summaries are not reconstructed from raw records by this script. `MONTE-CARLO.md` also reports the commercial-data checks, which remain outside the public reproduction scope. Zero simulated hits is not a population p-value.

## Technical scope

The white paper excludes share-price discussion. Failure boundaries and proposed discriminating observations appear in sections 9–10.
