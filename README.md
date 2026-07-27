# MCM/ICM 2025 — Meritorious Winner (Top 7%)

> ⚠️ **Repository Status: Complete / Archived.** This repository was retrospectively created in July 2026 to archive work originally completed in May 2025. It will not receive updates.

## Problem

**2025 MCM Problem C:** Olympic Medal Prediction & Sports Strategy Analysis

[Problem Statement (PDF)](./2025_MCM_Problem_C.pdf)

## Approach

Four-model cascade:

1. **Multiple Linear Regression** — Predict total medal counts using number of events, types of sports, historical medal data, and host country effect
2. **Bayesian Dirichlet Posterior** — Decompose total medals into gold/silver/bronze distribution given historical data
3. **Advantage-Event Relaxation Function** — Classify events as advantage (score >0.6), balanced (0.4-0.6), or disadvantage (<0.4) events; correct Bayesian estimates for zero-medal countries
4. **Great Coach Effect** — Wilcoxon signed-rank test (qualitative) + quantitative measurement of athlete performance changes before/after coaching; investment ROI analysis for three countries

### Key Findings

- Predicted the 2028 Los Angeles Olympic medal table with 95% confidence intervals
- 22 countries predicted to win their first-ever Olympic medals
- Pareto effect: 80% of medals concentrated in 20% of athletes (r = 0.62 correlation between sport diversity and medal count)
- Sensitivity analysis: Gaussian noise perturbation on event count, athlete performance, and historical medal rates

## My Role

**Lead English paper writer & LaTeX typesetter.** Responsible for translating the team's modeling work into a complete English academic paper, including full LaTeX typesetting with figures, tables, mathematical notation, and bibliography.

## Iteration History

The `Latex版本_论文/` directory contains 15 sequential versions (Article_1 through Article_15), showing the complete writing and revision process from initial draft to final submission.

| File | Description |
|---|---|
| `Article_1.tex/pdf` | Initial draft |
| `Article_2.tex/pdf` through `Article_14.tex/pdf` | Incremental revisions |
| `Article_15.tex/pdf` | **Final submission** |
| `MCM-ICM_Summary.tex/pdf` | Official MCM Summary Sheet |

## Repository Structure

```
mcm-2025/
├── README.md
├── 2025_MCM_Problem_C.pdf          # Problem statement
├── scripts/                         # Data analysis scripts
│   └── *.py
└── Latex版本_论文/                   # LaTeX sources + compiled PDFs
    ├── mcmthesis.cls                # MCM template class
    ├── Article_1.tex/pdf through Article_15.tex/pdf
    ├── MCM-ICM_Summary.tex/pdf
    └── *.png                        # Figures
```

## Award

**Meritorious Winner (Top 7% globally)** — MCM/ICM 2025

## License

[CC BY 4.0](./LICENSE) — You may share and adapt with attribution. Commercial journals may require original work; check their policies before reusing content.

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
