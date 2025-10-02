---
id: Terms_CF_v2_initial_context
title: Terms (CF) v2 — Initial Context and Project Outline
status: Draft
stage: Planning
owner: slittle
people: []
reviewers: []
approver: TBD
priority: High
tags: [terms, transactibility, SMB, investor, appraisal, EBTDAR, UX]
# Linear Hierarchy
team: Product
super_initiative: "TBD"
initiative: "TBD"
project: "Terms (CF) v2"
milestone: "TBD"
requirement: "TBD"
linear_project_link: "https://linear.app/withco/project/terms-cf-v2-dcdecb129e7d/overview"
# Timestamps & Versioning
created: 2025-10-01T00:00:00Z
updated: 2025-10-01T00:00:00Z
version: 0.1.0
repo_only: true
---

## Purpose

Codify the scope and context for Terms (CF) v2, the second iteration of the Plane of Transactibility. Terms v2 defines how SMBs choose their economics (base rent vs upside share) and how investors see expected outcomes across deal stages, with guardrails for EBTDAR coverage and appraisal viability.

## Problem

- Current presentation of investor economics is a flat 8% target distribution without clear trade‑offs or stage‑appropriate disclosures.
- SMBs cannot explicitly select terms (rent vs upside) within validated guardrails tied to coverage metrics and appraisal constraints.
- Terms logic is not yet formalized as a reusable calculator aligned to the deal stages and the underlying capital/accounting model.

## Goal (Project Page — per How_to_use_Linear.md)

- Provide an SMB‑first terms experience that allows choosing among acceptable base rent and upside combinations, with immediate feedback and validation.
- Present investors with clear, stage‑appropriate expectations (target distribution and upside participation) before and at the Plane of Transactibility (Offering).
- Ensure selections satisfy underwriting guardrails (EBTDAR coverage thresholds) and support restricted appraisal requirements (lease terms + comparable sales).
- Produce a crisp PRD and milestones with concrete requirements that implement the above.

## Assumptions & Inputs

- Structure: Follow upside rules in `docs/Deal_Structure_Model_Spec.md` (retail REIT common with target distribution; Withco profit interests ~20%; SMB up to 80% with vesting and default reallocation logic).
- Stages: PLATFORM → ONBOARDING → ROADSHOW → OFFERING (Plane of Transactibility) → SUCCESSFUL OFFERING → CLOSED OFFERING → POST CLOSE → DISPOSITION.
- Investor presentation before Offering: show expected economics, not just 8% fixed; include upside narrative consistent with structure.
- SMB EBTDAR coverage: use the updated “5 metrics” framework (to be linked) to compute valid rent bands and minimum coverage.
- Appraisal: restricted appraisal will anchor on comparable sales and the new lease terms; terms must fit appraisal feasibility.

## Explicitly Out of Scope (for this project)

- Selecting the global legal structure (UPREIT vs single LLC) — referenced for modeling but decided elsewhere.
- Final vendor selections (TA, auditor, EDGAR); costs inform drag but are not chosen here.
- Building investor tax reporting features; we will model yield displays but not file/report flows.

## Solution Outline (user‑oriented capabilities)

1. SMB Terms Selector (Rent ↔ Upside)

- Inputs: purchase price or rent base, SMB EBTDAR and 5‑metric coverage inputs, minimum/maximum policy caps, appraisal cap‑rate constraints.
- Control: slider or discrete choices for rent percent of purchase price (e.g., 6%–10%+), with real‑time computed eligible upside share.
- Guardrails: invalid selections disabled with reasons (coverage shortfall, appraisal infeasibility).

1. Investor Economics Preview (Pre‑Offering)

- Show target distribution (default 8% accrual if unpaid, policy‑driven) and upside participation framing per structure.
- Offer “Yield‑heavy vs Upside‑heavy” preset views, with consistent risk disclosures.

1. Offering Lock (Plane of Transactibility)

- Freeze agreed rent/upside pair within allowed window; generate Offering terms artifacts and feed to valuation/appraisal package.

1. Validation & Reporting Hooks

- Coverage validation summary (EBTDAR, threshold, pass/fail).
- Appraisal feasibility check summary (target cap rate range, comps‑based sanity).
- Exportable terms bundle for diligence.

## Stages & What Changes

- PLATFORM / ONBOARDING: Collect SMB financials (EBTDAR inputs) and property prelims; compute provisional rent bands and upside ranges.
- ROADSHOW: Display investor expected outcomes (range), with clear assumptions and non‑binding language.
- OFFERING (Plane of Transactibility): Commit to a specific rent/upside point; all validations must pass.
- SUCCESSFUL/CLOSED OFFERING: Publish finalized terms; start accrual/distribution policy clock and document links.

## Inputs → Outputs (contract)

SMB Inputs

- Rent selection basis: percent of purchase price or $/yr; permitted range from policy and coverage model.
- EBTDAR and 5‑metric details (exact metrics TBD; link forthcoming) to compute coverage.
- Optional preferences (e.g., prioritize lower rent vs higher upside, minimum coverage comfort).

Model & Policy Inputs

- Purchase price, target distribution policy (e.g., 8% accrual rules), fee toggles as needed for yield view only.
- Appraisal policy: comp set, cap‑rate bounds consistent with lease terms.

System Outputs

- Chosen terms: base rent %, $/yr, upside share %.
- Coverage validation: computed coverage vs threshold; pass/fail with rationale.
- Investor economics preview: target distribution depiction and upside participation framing; gross→net notes if applicable.
- Appraisal feasibility flag: inline summary for restricted appraisal package.

## Calculators & Guardrails (to implement)

- Coverage Calculator: `coverage = EBTDAR / base_rent` with policy minimum (e.g., configurable `min_coverage`); integrate 5‑metric adjustments.
- Terms Mapping: monotonic mapping between higher base rent and lower upside share (policy curve to be defined; piece‑wise or parametric).
- Investor View Bridge: use structure rules from `Deal_Structure_Model_Spec.md` to derive display values (target distribution accrual behavior; upside split narrative).
- Appraisal Check: verify selected rent and lease terms fall within cap‑rate and comps bounds for restricted appraisal.

## Presentation Options for Investor Economics (decision set)

Option A — Fixed target distribution emphasis

- Keep 8% as the headline target; add a secondary “potential upside participation” explainer.

Option B — Range reveal with presets

- Show two or three presets (Yield‑heavy, Balanced, Upside‑heavy) with the same 8% target as context; emphasize trade‑offs.

Option C — Interactive explainer (read‑only)

- Lightweight slider illustrating how SMB choices map to investor profile, without implying guaranteed outcomes.

Selection Criteria

- Clarity, regulatory friendliness, user comprehension; minimal cognitive load during Roadshow.

## Milestones (1–3 weeks each; requirements are <1 week IC tasks)

Milestone 1 — PRD & Policy Guardrails

- Requirements:
  - Draft PRD aligned to this context; define min coverage and rent range policy.
  - Specify the terms mapping curve (rent↔upside) and validation error states.
  - Define appraisal feasibility checks and required inputs.

Milestone 2 — SMB Terms Selector (UX + Engine v1)

- Requirements:
  - Build terms calculator API with coverage checks and mapping curve.
  - Implement SMB slider/selector UX with disabled states and reasons.
  - Emit a machine‑readable terms bundle for Offering.

Milestone 3 — Investor Economics Preview (Pre‑Offering)

- Requirements:
  - Implement presentation Option B (presets) as baseline; A/C as alternates.
  - Bridge to structure model for target distribution and upside framing.
  - Include disclosures and stage‑appropriate messaging.

Milestone 4 — Offering Lock & Appraisal Package

- Requirements:
  - Freeze agreed terms; generate Offering artifacts.
  - Produce appraisal check report (cap‑rate bounds, comps summary, lease term impact).
  - Handoff package to appraisal/diligence workflow.

## Risks & Open Questions

- Coverage thresholds vs SMB affordability may constrain viable upside; need policy clarity on exceptions.
- Appraisal sensitivity to lease terms may reduce acceptable rent bands; confirm cap‑rate policy by asset class/MSA.
- Regulatory wording for investor “expected outcomes” prior to Offering; legal review required.
- Exact “5 metrics” for EBTDAR updates and their weights; source of truth document needed.

## References

- Company conventions: `linear/docs/How_to_use_Linear.md` (read‑only)
- Structure & economics: `docs/Deal_Structure_Model_Spec.md`
- Context docs: `docs/raw/economics-cost-structure-initial-context.md`, `docs/raw/cost-of-manufacturing-offering-context.md`
- Term sheet (UPREIT/OP concepts): `docs/raw/docs/withco-reit-and-op-high-level-term-sheet.md`
- Market fee examples: `docs/raw/docs/fee_examples.md`
- Vendor data scaffold (for cost drag context): `docs/raw/data/vendor-cost-data.json`
- Linear project (overview reference): [Terms (CF) v2 Project](https://linear.app/withco/project/terms-cf-v2-dcdecb129e7d/overview)

## Appendix — Stages (from image mapping)

- PLATFORM → ONBOARDING → ROADSHOW → OFFERING (Plane of Transactibility) → SUCCESSFUL OFFERING → CLOSED OFFERING → POST CLOSE → DISPOSITION.
