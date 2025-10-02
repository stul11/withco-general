# 00_README.md

## What’s in this package

This package provides a complete, source‑backed, **Excel‑ready** reference for two common real‑estate investor tax situations:

- **A) K‑1 Property LLC** — investor receives a **Schedule K‑1 (Form 1065)** from a real‑estate partnership/LLC.
- **B) UPREIT w/ 1099‑DIV** — investor holds **REIT common shares** (receives **Form 1099‑DIV**) while other investors may hold **Operating Partnership (OP) units** (receive **K‑1**). Includes side‑by‑side form workflows and when an investor could see **both** a K‑1 and a 1099‑DIV (e.g., holding OP units **and** REIT shares, taxable exchanges, or sales).

You’ll find:

- **IRS form workflows & triggers** (schedules, when they’re required, and where items flow on Form 1040).
- **TurboTax Online** support mapping by **tier** (Free, **Deluxe**, **Premium** (formerly Premier/Self‑Employed)) and **current pricing snapshots** (federal, state add‑ons, and e‑file fee notes).
- **Professional preparation fee ranges** from reputable surveys and representative CPA firm schedules.
- **Excel‑ready TSV calculators** to compute:
  - Minimum **TurboTax tier** and **software cost** for a scenario.
  - Estimated **professional preparation cost** for the same scenario.
- **Scenario matrices**, **decision trees**, **worked examples**, **glossary**, and a **consolidated bibliography**.

## How to use the TSV calculators

All TSVs are designed to be pasted **starting in Excel cell A1**.

1. Open the `.tsv` file.
2. Select **all** text and paste into **Excel A1**.
3. Each calculator has:
   - An **INPUTS** block at **A1** with two columns: `Name` and `Value`. Change **only** the `Value` cells.
   - A **CALCULATIONS** block starting at **A20** that uses **absolute references** (e.g., `$B$2`) to the INPUTS.  
     The formulas will work immediately after you paste.

> Tip: Use `05_SCENARIO_INPUTS_TEMPLATE.tsv` as your master input sheet. Then paste the same values into `06_…SOFTWARE.tsv` and `07_…PROFESSIONAL.tsv` to get comparable software vs. pro‑prep estimates.

## How deliverables map to the two investor scenarios

- **Forms & triggers:** See `01_IRS_FORM_LINKS.tsv`, `10_DECISION_TREES.md`.
- **TurboTax support & pricing:** See `02_TURBOTAX_SUPPORT_MATRIX.tsv`, `03_TURBOTAX_PRICING.tsv`.
- **Costs & calculators:** See `05_SCENARIO_INPUTS_TEMPLATE.tsv`, `06_COST_CALCULATOR_SOFTWARE.tsv`, `07_COST_CALCULATOR_PROFESSIONAL.tsv`.
- **Scenario libraries:** See `08_K1_PROPERTY_LLC_SCENARIOS.tsv`, `09_UPREIT_1099DIV_SCENARIOS.tsv`.
- **Worked examples:** See `11_WORKED_EXAMPLES.md`.
- **Definitions & sources:** See `12_GLOSSARY.md`, `13_SOURCES.md`.

## Caveats & scope

- Jurisdiction: **U.S. individual (Form 1040)** federal and state returns.
- Filing seasons prioritized: **2024–2025** (returns filed in **2025–2026**). When rules changed, we note timing.
- **Always** rely on the latest IRS instructions for final positions. State rules vary—nonresident filing triggers and composite/withholding procedures differ by state.
- **TurboTax Online** pricing is **seasonal and dynamic**. We include multiple snapshots with **accessed dates** and official TurboTax URLs. Use the calculators to model **incremental** costs as you add K‑1s, states, or forms.
