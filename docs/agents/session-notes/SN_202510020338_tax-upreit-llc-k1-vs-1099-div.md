---
id: SN_202510020338_tax-upreit-llc-k1-vs-1099-div
title: Tax UPREIT vs K-1 – calculators and workbook assembly
version: 1.0.0
created: 2025-10-02T03:38:00Z
updated: 2025-10-02T03:38:00Z
owner: slittle
status: Draft
tags: [session-note, taxes, calculators, excel]
---

# Session NOTE

- **Task ID**: tax-upreit-llc-k1-vs-1099-div
- **Agent**: background coding assistant (Cursor)
- **Owner**: slittle
- **Date**: 2025-10-02T03:38:00Z
- **Duration**: n/a

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - `linear/tickets/drafts/research-prompts/tax-upreit-llc-k1-vs-1099-div-20251001/tax-upreit-llc-k1-vs-1099-div-20251001-response/00_README.md`
  - `.../01_IRS_FORM_LINKS.tsv`
  - `.../02_TURBOTAX_SUPPORT_MATRIX.tsv`
  - `.../03_TURBOTAX_PRICING.tsv`
  - `.../04_PROFESSIONAL_PREP_FEES.tsv`
  - `.../05_SCENARIO_INPUTS_TEMPLATE.tsv`
  - `.../06_COST_CALCULATOR_SOFTWARE.tsv`
  - `.../07_COST_CALCULATOR_PROFESSIONAL.tsv`
  - `.../08_K1_PROPERTY_LLC_SCENARIOS.tsv`
  - `.../09_UPREIT_1099DIV_SCENARIOS.tsv`
  - `.../10_DECISION_TREES.md`, `11_WORKED_EXAMPLES.md`, `12_GLOSSARY.md`, `13_SOURCES.md`
- **Context & Requirements**:
  - Build an Excel workbook from TSV/MD deliverables per README mapping; add auto-calculating scenario sheets.
  - Provide a single copy/paste calculator; fix broken/locked formulas in 06/07.
- **Relevant Prior Work**:
  - Existing calculators (06/07) contained mis-referenced cells and parsing comments inside TSVs.

---

## Full Findings

- **Summary of Findings**:
  - Created consolidated Excel workbook with INDEX + per-deliverable sheets; added 16 auto-calculating scenario tabs.
  - Identified formula reference issues in `06` and `07`; produced corrected CALCULATIONS blocks.
  - Delivered a transposed, selector-driven single-sheet calculator to avoid sheet protection/locked cell issues.
- **Detailed Findings**:
  - **Calculator refs**:
    - `06_COST_CALCULATOR_SOFTWARE.tsv:L17-L23` – original refs to `$B$20`/`$B$21` misaligned once pasted; semicolon comments broke TSV parsing.
    - `07_COST_CALCULATOR_PROFESSIONAL.tsv:L27-L39` – add-on lines referenced wrong flags (e.g., 4797/6252).
  - **Workbook assembly**:
    - Generated `Tax_UPREIT_LLC_K1_vs_1099DIV_Complete_Reference.xlsx` and `..._Enhanced_With_Scenarios.xlsx` with INDEX and scenario tabs.

---

## Steps Taken

- **Major Actions**:
  - Assembled workbook from TSV/MD per README mapping with stable sheet names.
  - Enhanced workbook with one sheet per scenario (7 K‑1 + 9 UPREIT); pre-populated inputs + formulas.
  - Authored corrected CALCULATIONS blocks for `06` and `07`.
  - Provided transposed single-sheet calculator with scenario selector to bypass locked/relative-reference issues after paste.
- **Key Decisions**:
  - Adopt `04_PROFESSIONAL_PREP_FEES.tsv` to fill sequence gap (01–13).
  - Use selector-based, transposed calculator as portable canonical artifact.
- **Tools/Methods Used**:
  - Python (`openpyxl`, `pandas`) for workbook assembly; Excel formula ref auditing.

---

## Outputs

- **Files Created/Modified**:
  - `.../Tax_UPREIT_LLC_K1_vs_1099DIV_Complete_Reference.xlsx` (assembled)
  - `.../Tax_UPREIT_LLC_K1_vs_1099DIV_Enhanced_With_Scenarios.xlsx` (scenario sheets)
  - Corrected CALCULATIONS blocks for `06` and `07` (provided in chat for paste-over)
  - Transposed single-sheet calculator (provided in chat, paste into A1)
- **Key Deliverables**:
  - Working workbook + per-scenario calculators; copy/paste one-sheet calculator.
- **Documented Decisions**:
  - See Decision Docket entry 2025-10-02 (A).

---

## Citations

- `.../06_COST_CALCULATOR_SOFTWARE.tsv:L17-L23`
- `.../07_COST_CALCULATOR_PROFESSIONAL.tsv:L27-L39`
- `.../11_WORKED_EXAMPLES.md:L7-L31,L113-L137,L168-L193`
- `.../08_K1_PROPERTY_LLC_SCENARIOS.tsv:L1-L6`
- `.../09_UPREIT_1099DIV_SCENARIOS.tsv:L1-L6`

---

## Risks & Issues Identified

- Some Excel environments interpret TRUE/FALSE as text upon paste; boolean coercion added in transposed sheet.
- TSV inline comments can break parsing; calculators should avoid trailing `;` annotations inside TSVs.

---

## Reasoning & Rationale

- Selector-based sheet minimizes cross-sheet dependencies and avoids locked/protected cell side effects.
- Corrected formulas align with visible INPUTS row positions and intended decision logic (tier gating; pro add-ons).

---

## Next Actions

- Validate calculators on Windows + Mac Excel; confirm boolean coercion works universally.
- Optional: Macro/button to duplicate scenario into dedicated tab automatically.
- If desired: integrate pricing snapshots as named ranges for seasonal updates.

---

## Signoff

- **Reviewer**: slittle
- **Status**: pending
- **Date**: 2025-10-02T03:38:00Z
- **Notes**: Ready for review; validations to run as part of offboarding.
