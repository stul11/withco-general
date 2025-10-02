---
id: excel-cost-analysis-funnel-integration
title: Excel Cost Analysis Update - Funnel Stage Integration
status: Draft
stage: Planning
owner: slittle
people: [KS, BF]
reviewers: [KS, BF]
approver: KS
priority: High
tags: [excel, cost-analysis, funnel, finance-model, urgent]
# Linear Hierarchy
team: Product
super_initiative: "TBD"
initiative: "TBD"
project: "TBD"
milestone: "TBD"
requirement: "TBD"
linear_issue_link: "TBD"
# Timestamps & Versioning
created: 2025-01-27T17:30:00Z
updated: 2025-01-27T17:30:00Z
version: 0.1.0
# Context & Relationships
related_docs:
  - cost_of_manufacturing_offering_v3
  - docs/global/GBL-TKT_Best_Practices.md
risk_level: High
repo_only: true
---

# Excel Cost Analysis Update - Funnel Stage Integration

## Goal / Purpose

- Decision enabled: Update the cost of manufacturing analysis with funnel stage integration and "who pays" tracking so the urgent pricing review can close.
- Why now: Cost-of-manufacturing work is blocked on resolving red highlighted cells and mapping expenses to funnel stages.
- Success metric: All red highlighted cells cleared and funnel-stage toggles produce consistent totals across views.

## Assumptions

- Existing cost data structure is fundamentally correct.
- Funnel stage volumes from reference image 2 are current and accurate.
- Red highlighted cells indicate unknown values instead of formula errors.
- Toggle requirements (Annual/Per_Unit, When Incurred/Cumulative) match stakeholder expectations.

## Inputs / Dependencies

- cost_of_manufacturing_offering_v3 (Funnel sheet).
- Funnel stage volume image (INV + SMB counts).
- Vendor cost table with one-time, annual, and per-event entries.
- LEG-63 research context for cost definitions.
- No upstream dependencies or blockers identified.

## Deliverable

- Updated Excel workbook with:
  - Funnel stage mapping applied to every per-event cost.
  - "Who pays" column populated for each cost line.
  - Toggle controls for Annual/Per_Unit and When Incurred/Cumulative views.
  - Summary sheet with executive narrative for KS and BF.
- Primary consumers: KS, BF.

## Definition of Done (DoD)

### Fast (same day)

- [ ] Red highlighted cells catalogued with owner + data request.
- [ ] Baseline funnel stage mapping applied to three representative vendor rows.
- [ ] Manual calculation spot-check completed for those rows.

### Standard (2–3 days)

- [ ] All per-event costs mapped to funnel stages with validation notes.
- [ ] "Who pays" column populated and reviewed with KS.
- [ ] Toggle controls implemented for Annual/Per_Unit and When Incurred/Cumulative views.
- [ ] Summary sheet drafted with Executive Summary + Changes & Assumptions log.
- [ ] Validation checks (duplicates, totals, error scan) implemented on Funnel sheet.

### Gold (1–2 weeks)

- [ ] Cost curves integrated with LEG-9 minimum check analysis.
- [ ] Vendor/service mapping aligned to standardized vendor list.
- [ ] Visualization dashboard built (stage breakdown + payer pie chart).
- [ ] External review completed with finance + legal for compliance sign-off.
- [ ] Documentation packaged for Shortcut automation (prompt + AI rules snippet).

## Feedback & Reviews

- KS → cost accuracy and business logic (same-day review).
- BF → funnel mapping + payer logic (same-day review).
- Schedule: Pair review today before 18:00 ET.

## Explicitly Out of Scope

- Broad vendor database overhaul.
- Adding brand-new cost categories.
- Integrations outside the Excel model (e.g., Airtable, Notion).

## Open Questions

1. What final values should populate the "who pays" column for each vendor category?
2. Should toggle calculations be deterministic formulas or scenario macros?
3. Are validation rules required for outstanding red highlighted cells?
4. How should manual overrides be surfaced for reviewer awareness?
5. Do we need automatic mapping between SMB vs Investor funnels?

## Plan (small steps)

- [ ] Review existing Funnel sheet and flag gaps (1 hr).
- [ ] Map three vendor rows end-to-end (who pays, stage mapping, toggles) for pattern lock (1 hr).
- [ ] Extend mapping + toggles across remaining rows (2 hrs).
- [ ] Build validation and summary sheet (1 hr).
- [ ] Prepare reviewer handoff package with notes + screenshots (30 min).

## Reviewer Checklist

- [ ] Front matter fields align with ticket template and timestamps are ISO 8601.
- [ ] Goal, assumptions, inputs, DoD tiers, feedback, scope, questions, and plan are present.
- [ ] Deliverable description matches attached prompts/schema updates.
- [ ] Appendix artifacts (prompt, schema, references) reference current versions.

## Appendix

### Shortcut Prompt for Automated Excel Work

```markdown
**[BEGIN PROMPT TO PASTE INTO SHORTCUT CHAT]**

**Role & Goal**

- You are a senior Excel analyst inside Shortcut. **Goal:** Update cost of manufacturing analysis with funnel stage integration, "who pays" tracking, and toggle controls for different cost views.

**Starting Point**

- I will upload file: "cost_of_manufacturing_offering_v3".
- If uploading: assume tabs of interest: "Funnel", "Legal Cost", "UPREIT_vs_LLC".

**Data & Context**

- Source data: Cost table with one-time, annual, and per-event costs; funnel stage volumes for INV and SMB platforms; red highlighted cells contain uncertain numbers.
- Key definitions:
  - Per-event costs = Cost/Unit × Funnel Event Volume
  - Funnel stages: PLATFORM, ONBOARDING, ROADSHOW, OFFERING, SUCCESSFUL OFFERING, CLOSED OFFERING, POST CLOSE, DISPOSITION
  - "Who pays" categories: SMB, Offering, Investor, Platform
- Assumptions (initial): Red highlighted cells contain uncertain numbers, not errors; existing cost structure is fundamentally correct.

**Deliverables**

- Work within existing sheets as given; all calculations happen on "Funnel" sheet.
- Add/update the following columns on "Funnel" sheet:
  - Who Pays (text), When Incurred (text), Cumulative Cost (currency)
  - Toggle controls for Annual/Per_Unit and When Incurred/Cumulative views
- Formulas/logic: EN-US function names, structured references where practical, toggle controls using IF statements
- Visuals: Cost breakdown charts by funnel stage, "who pays" pie chart, toggle control dashboard
- Narrative: add a short **Executive Summary** on a sheet called "Summary".

**Standards (house rules)**

- Formatting: dates = YYYY-MM, currency = USD with 0 decimals, negative = red; headings = bold
- Modeling: per-event costs calculated as Cost/Unit × Funnel Event Volume; one-time costs not multiplied
- Data handling: trim/clean text, standardize categorical values to lowercase, dedupe on cost item keys
- Documentation: include a **Changes & Assumptions** log on "Summary"

**Workflow & Checkpoints**

1. **Plan:** Outline the steps and proposed column additions on "Funnel" sheet—pause for confirmation.
2. **Checkpoint:** Create a named checkpoint: `"Plan approved"` before executing.
3. **Execute:** Implement steps in order; avoid volatile functions unless required.
4. **Validate:** Build validation checks on "Funnel" sheet:
   - Row counts and duplicate report on cost item keys
   - Totals tie-outs (sum of all costs = sum of one-time + annual + per-event costs)
   - Error scans: #N/A, #DIV/0!, empty required fields
   - Unit consistency checks (%, currency, dates)
5. **Report:** Update "Summary" with key metrics, charts, and a bullet **Changes & Assumptions** log.
6. **Checkpoint:** Create `"Draft complete"`. If issues arise, **Return to checkpoint** and fix.

**Constraints**

- Be deterministic: work within existing sheet structure; do not create new sheets.
- Do not delete original raw data; work within "Funnel" sheet.
- If information is missing, proceed with reasonable defaults but list them in **Assumptions**.

**Handover**

- Provide a short "Next steps" list (what I should refine or add).
- List any ambiguities or risks that need my decision.

**[END PROMPT TO PASTE INTO SHORTCUT CHAT]**
```

### Cost Unit Scope Enums (Reference)

*Content retained from standardized vendor schema to support toggle logic.*

```yaml
cost_card:
  id: string # Unique identifier
  vendor: string # Vendor name
  service: string # Specific service description
  cost_unit_scope: enum # Primary cost unit scope
  secondary_scope: enum # Optional secondary scope
  unit_price: number # Price per unit
  minimum_commitment: number # Minimum quantity/amount
  step_tiers: array # Tiered pricing structure
  payer: enum # Who pays (Company, REIT, Investor, SMB)
  timing: enum # When paid (pre-close, at-close, ongoing)
  accounting: enum # Expensed vs capitalized
  amortization_period: number # If capitalized, amortization period
  scalability_note: string # What unlocks better pricing
  replacement_candidates: array # Alternative vendors
  switching_costs: number # Cost to switch vendors
  stage_activation: array # Which offering stages this applies to
  upreit_specific: boolean # UPREIT-specific cost
  llc_specific: boolean # LLC-specific cost
  reg_a_required: boolean # Required for Reg A+ compliance
```

### Stage Activation Mapping

```yaml
stage_costs:
  IOI:
    - Platform setup (North Capital)
    - Legal structuring (CRE Counsel)
    - Initial compliance (EDGAR Service)
  COMMITTED_OFFERING:
    - Investor verification (Oscilar)
    - Transfer agent setup (Transfer Agent)
    - Reg A+ filing (EDGAR Service)
  SPECIFIC_OFFERING:
    - Property appraisal (Appraisal Vendors)
    - Due diligence (Cherre, Enigma)
    - Property management setup (Property Management)
  CLOSED_OFFERING:
    - Ongoing property management (Property Management)
    - Annual audit (Auditor)
    - Investor reporting (Transfer Agent)
```

### Attachments Checklist

- cost_of_manufacturing_offering_v3 Excel file.
- Funnel stage volume reference (image 2).
- Vendor cost table (current draft).

### AI Rules Snippet (Shortcut)

- Formatting: Currency = USD with 0 decimals, negative = red; headings = bold; dates = YYYY-MM.
- Modeling: Per-event costs = Cost/Unit × Funnel Event Volume; one-time costs not multiplied; funnel stages follow PLATFORM → ONBOARDING → ROADSHOW → OFFERING → SUCCESSFUL OFFERING → CLOSED OFFERING → POST CLOSE → DISPOSITION.
- Data handling: Trim/clean text, standardize categorical values to lowercase, dedupe on cost item keys.
- Company specifics: "Who pays" categories = SMB, Offering, Investor, Platform; toggles for Annual/Per_Unit and When Incurred/Cumulative views required.

### References

- [LEG-63: Collect Cost of Manufacturing an Offering Inputs](https://linear.app/withco/issue/LEG-63/collect-cost-of-manufacturing-an-offering-inputs)
- [LEG-9: Determine Minimum Check Size](https://linear.app/withco/issue/LEG-9/determine-minimum-check-size)
- [Existing Excel Model](https://docs.google.com/spreadsheets/d/195wUpk6d5dZS61sf5MbemVhean0FWf5YK3o6v8nctlE/edit?usp=drive_link)
- `withco-general/docs/raw/economics-cost-structure-initial-context.md`
