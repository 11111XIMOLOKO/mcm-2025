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

## What I Learned

I didn't come into this competition knowing LaTeX. The week before, right after finals, my teammates and I ran 2-3 full mock competitions with past MCM problems. I collected several award-winning papers and studied their formatting. For equations and tables, I found online visual editors that let me draw what I needed and then auto-generated the LaTeX code — I'd copy, paste, tweak. By the time the real competition started, I'd already gone through the full paper-production cycle multiple times.

What followed was less about learning LaTeX and more about the density of revision. The source file grew from 25KB to 80KB across 15 iterations — not because I was still figuring out the tools, but because the paper itself was evolving: structure tightening, figures swapping, notation standardizing. Each iteration was small, but there were a lot of them.

The harder skill was invisible. I wasn't building the models — but the team's shared principle was simple: the paper is the product. Everyone's job was to figure out the most efficient way to get their work onto the page. That meant designing a relay system: my teammates would walk me through what they'd built, I'd draft the section, they'd check it for accuracy, and we'd iterate. The mock training from the week before was what made this possible — we already knew how each other communicated, so the handoffs were fast.

And the models kept changing. Drafting against a moving target — structuring arguments that could survive last-minute adjustments — turned out to be the most transferable skill of all. It taught me something specific about how to structure a team writing workflow: build the narrative backbone early, then slot in final numbers later. That way the writer isn't hostage to the modeler's timeline.

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
