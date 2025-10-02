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
team: Product
super_initiative: "TBD"
initiative: "TBD"
project: "TBD"
milestone: "TBD"
requirement: "TBD"
linear_issue_link: "TBD"
created: 2025-01-27T17:30:00Z
updated: 2025-01-27T17:30:00Z
version: 0.1.0
related_docs:
  - cost_of_manufacturing_offering_v3
risk_level: High
repo_only: true
---

# Excel Cost Analysis Update - Funnel Stage Integration

Goal / Purpose

Update cost of manufacturing analysis with funnel stage integration and "who pays" tracking. Major urgency on cost of manufacturing an offering. Success metric: All red highlighted cells resolved, funnel stage costs properly calculated.

Assumptions

- Existing cost data structure is fundamentally correct
- Funnel stage volumes from image 2 are current and accurate
- Red highlighted cells contain uncertain numbers, not errors

Open Questions

1. What specific values should populate the "who pays" column for each cost type?
2. Are there specific validation rules for the uncertain numbers in red highlighted cells?
3. Should the funnel stage mapping be automatic or manual for each cost item?
4. What are the exact toggle control requirements for Annual/Per_Unit views?
5. What are the exact toggle control requirements for When Incurred/Cumulative views?

Inputs / Dependencies

- cost_of_manufacturing_offering_v3 (Funnel sheet)
- Funnel stage volumes (image 2)
- Cost table data (provided)
- No upstream dependencies
- No blockers

Feedback requirements

- KS: Cost accuracy and business logic review
- BF: Funnel stage mapping and "who pays" logic review
- SLA: Today EOD

Explicitly out of scope

- Complete vendor database overhaul
- New cost categories beyond existing structure
- Integration with other systems beyond Excel

Deliverable

Updated Excel spreadsheet with funnel stage integration, "who pays" tracking, and toggle controls for different cost views. Consumers: KS, BF.

Definition of Done (DoD)

- [ ] Red highlighted cells identified and root cause documented
- [ ] Basic funnel stage mapping implemented for per-event costs
- [ ] Manual calculation verification for 3 sample rows
- [ ] "Who pays" column added with initial values
- [ ] All per-event costs properly mapped to funnel stages
- [ ] Toggle controls implemented for Annual/Per_Unit views
- [ ] Toggle controls implemented for When Incurred/Cumulative views
- [ ] "Who pays" column populated for all cost items
- [ ] KS and BF review completed with sign-off

Appendix

## Shortcut Prompt for Automated Excel Work

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

## Attachments Checklist

- cost_of_manufacturing_offering_v3 Excel file
- Funnel stage volumes data (from image 2)
- Cost table data (provided in ticket)

## AI Rules Snippet (optional, to paste under Shortcut > Settings > "AI Rules & Instructions")

- Formatting: Currency = USD with 0 decimals, negative = red; headings = bold; dates = YYYY-MM
- Modeling: Per-event costs = Cost/Unit × Funnel Event Volume; one-time costs not multiplied; funnel stages follow PLATFORM → ONBOARDING → ROADSHOW → OFFERING → SUCCESSFUL OFFERING → CLOSED OFFERING → POST CLOSE → DISPOSITION
- Data handling: Trim/clean text, standardize categorical values to lowercase, dedupe on cost item keys
- Company specifics: "Who pays" categories: SMB, Offering, Investor, Platform; toggle controls for Annual/Per_Unit and When Incurred/Cumulative views
