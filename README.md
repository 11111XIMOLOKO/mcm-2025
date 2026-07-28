# MCM/ICM 2025 — Meritorious Winner (Top 7%)

> ⚠️ **Repository Status: Complete / Archived.** This repository was retrospectively created in July 2026 to archive work originally completed in May 2025. It will not receive updates.

## My Role

**Lead English paper writer & LaTeX typesetter.** I translated the team's modeling work into a complete English academic paper with full LaTeX typesetting — writing the narrative, structuring the argument, typesetting equations/tables/figures, managing the bibliography, and producing the final camera-ready PDF.

This was a 3-person team competition. The four models described below were developed by my teammates, who were responsible for model design and programming. My contribution focused on English paper writing and LaTeX typesetting.

## Problem

**2025 MCM Problem C:** Olympic Medal Prediction & Sports Strategy Analysis

[Problem Statement (PDF)](./2025_MCM_Problem_C.pdf)

## Paper Overview

The paper documents a four-model cascade for Olympic medal prediction:

1. **Multiple Linear Regression** — Predicting total medal counts from event participation, sport types, historical performance, and host country effect
2. **Bayesian Dirichlet Posterior** — Decomposing total medals into gold/silver/bronze distributions using historical data as priors
3. **Advantage-Event Relaxation Function** — Classifying events by national strength (advantage/balanced/disadvantage) to correct predictions for zero-medal countries
4. **Great Coach Effect** — Wilcoxon signed-rank test + quantitative before/after analysis of athlete performance under elite coaching; ROI estimation for three target countries

### Key Findings Documented in the Paper

- Predicted 2028 Los Angeles Olympic medal table with 95% confidence intervals
- 22 countries identified as potential first-time medal winners
- Pareto effect observed: 80% of medals concentrated in 20% of athletes
- Sport diversity–medal count correlation: r = 0.62
- Gaussian noise perturbation sensitivity analysis on event count, athlete performance, and historical medal rates

## What This Repository Demonstrates

**English academic writing** — translating technical modeling work into a logically structured, publication-ready English paper with precise terminology.

**LaTeX proficiency** — independent typesetting of a full-length paper: mathematical notation, multi-panel figures, tables, cross-references, bibliography management, and adherence to the MCM official template (`mcmthesis.cls`).

**Writing as a process** — 15 sequential versions (Article_1 through Article_15) show the complete drafting and revision cycle: from initial scaffold → incremental refinement → final polished submission.

**What I learned** — This was my first experience producing a full-length English academic paper under time pressure. I learned how to structure a multi-model narrative so each section builds on the previous one, how to manage a LaTeX project that grows to thousands of lines across 15 iterations, and most importantly, how to serve as the bridge between mathematical modeling and readable prose — a skill directly transferable to graduate research.

## Iteration History

The `latex-source/` directory preserves all 15 versions:

| File | Description |
|---|---|
| `Article_1.tex/pdf` | Initial draft — structure and rough content |
| `Article_2.tex/pdf` through `Article_14.tex/pdf` | Incremental revisions — tightening the narrative, refining notation, fixing figure placement |
| `Article_15.tex/pdf` | **Final submission** |
| `MCM-ICM_Summary.tex/pdf` | Official MCM Summary Sheet |

## Repository Structure

```
mcm-2025/
├── README.md
├── LICENSE
├── award-certificate.pdf            # MCM/ICM award certificate
├── 2025_MCM_Problem_C.pdf           # Problem statement
└── latex-source/                    # LaTeX sources + compiled PDFs
    ├── mcmthesis.cls                # MCM template class
    ├── Article_1.tex/pdf through Article_15.tex/pdf
    ├── MCM-ICM_Summary.tex/pdf
    └── *.png                        # Figures
```

## Award

**Meritorious Winner (Top 7% globally)** — MCM/ICM 2025

[Award Certificate (PDF)](./award-certificate.pdf)

## License

[CC BY 4.0](./LICENSE) — You may share and adapt with attribution.

## Citation

If you reference this work, please cite:

```
@misc{mcm2025-olympic-medal-prediction,
  author  = {Huijuan Qiu and Team 2517063},
  title   = {Olympic Medal Prediction and Sports Strategy Analysis},
  year    = {2025},
  note    = {MCM/ICM 2025 Meritorious Winner (Top 7\%). \url{https://github.com/11111XIMOLOKO/mcm-2025}}
}
```
