---
id: LEG-standardized-vendor-list
title: Standardized Vendor List & Cost Unit Scope Enums
status: Draft
stage: Planning
owner: slittle
people: [finance_team, legal_team]
reviewers: [ksong, bfetterolf]
approver: ksong
priority: Medium
tags: [vendor-list, enums, cost-modeling, LEG-63]
# Linear Hierarchy
team: Product
super_initiative: "Cost of Manufacturing Program"
initiative: "LEG-63 Cost of Manufacturing Inputs"
project: "Vendor & Pricing Normalization"
milestone: "v0.1 Vendor & Schema Draft"
requirement: "Define canonical vendor list and enums"
linear_issue_link: "https://linear.app/withco/issue/LEG-63"
# Timestamps & Versioning
created: 2025-01-27T17:30:00Z
updated: 2025-01-27T17:30:00Z
version: 0.1.0
# Context & Relationships
related_docs:
  - docs/global/GBL-TKT_Best_Practices.md
  - linear/tickets/drafts/excel-cost-analysis-funnel-integration.md
  - docs/raw/economics-cost-structure-initial-context.md
risk_level: Medium
repo_only: true
---

# Standardized Vendor List & Cost Unit Scope Enums

## Goal / Purpose

- Decision enabled: Establish a canonical vendor list and enum schema so cost models, LEG-63 tickets, and automation prompts share the same vocabulary.
- Why now: Excel funnel work and RSM pricing updates depend on consistent naming and scope definitions to avoid duplicate mapping.
- Success metric: Approved enum table + vendor roster referenced by LEG-63 workflows without ad-hoc edits.

## Assumptions

- Existing vendor research is accurate but unstructured.
- Cost unit scopes must align with Shortcut automation schema.
- Pricing tiers can be refined later; current draft focuses on structure.
- LEG-63 remains authoritative for minimum requirements.

## Inputs / Dependencies

- RSM call outputs and cost modeling drafts.
- Legacy vendor list spreadsheets (internal).
- Excel cost analysis funnel integration ticket (for schema alignment).
- Dependencies: confirmation from finance/legal on categories; automation prompts referencing enums.

## Deliverable

- Markdown draft containing:
  - Cost unit scope enums (primary, secondary, composite, one-time).
  - Standardized vendor table grouped by category.
  - Cost card schema reference for automation.
- Consumers: LEG-63 owners, automation engineers, finance/legal reviewers.

## Definition of Done (DoD)

### Fast (same day)

- [ ] Enum tables captured with definitions and examples.
- [ ] Vendor list compiled for core platform, compliance, property services, and operations.
- [ ] Cost card schema documented for automation hand-off.

### Standard (2–3 days)

- [ ] Pricing placeholders validated with finance/legal (notes or TBD markers).
- [ ] Stage activation mapping aligned with funnel integration ticket.
- [ ] Reviewer checklist completed; feedback incorporated into draft.

### Gold (1–2 weeks)

- [ ] Pricing tiers populated with min/step commitments.
- [ ] Enum + vendor data exported to structured format for Shortcut prompts.
- [ ] Change log + version history appended and linked to Decision Docket entry.

## Feedback & Reviews

- Reviewers: KS (business scope), BF (model integration).
- SLA: Provide review-ready draft before Excel toggle implementation completes.

## Explicitly Out of Scope

- Negotiating vendor contracts or final pricing.
- Publishing to company-wide documentation without approval.
- Building the automation export (tracked separately).

## Open Questions

1. Which vendors should be marked as primary vs backup for each category?
2. Do we need additional enums for hybrid pricing (e.g., per investor + per asset)?
3. Where should version history live once the schema stabilizes?
4. How should we surface payer/timing defaults for automation prompts?

## Plan (small steps)

- [ ] Consolidate vendor research into canonical categories (1 hr).
- [ ] Align enum definitions with Excel schema + Shortcut prompt (1 hr).
- [ ] Review with finance/legal for missing vendors or scopes (30 min sync).
- [ ] Document open pricing gaps and assign owners (30 min).

## Reviewer Checklist

- [ ] Front matter populated with template-compliant fields and ISO timestamps.
- [ ] Enum tables cover all required cost scopes with examples.
- [ ] Vendor list segmented by major categories and matches LEG-63 needs.
- [ ] Schema + stage mapping align with excel-cost-analysis-funnel-integration draft.

## Appendix

### Cost Unit Scope Enums

#### Primary Scopes

| Enum | Definition | Use Case | Example |
| --- | --- | --- | --- |
| `PER_INVESTOR` | Cost scales with number of investors | KYC/AML, tax forms, investor communications | $5 per investor for KYC/AML |
| `PER_ASSET` | Cost scales with number of properties/assets | Property management, appraisals, insurance | $2,500 per property for appraisal |
| `PER_OFFERING` | Fixed cost per offering regardless of scale | Reg A+ filing, legal structuring, audit setup | $50,000 for Reg A+ filing |
| `PER_PRIMARY_OFFERING` | Cost per primary (initial) offering | Initial Reg A+, TA onboarding | $75,000 primary setup |
| `PER_SECONDARY_OFFERING` | Cost per secondary offering / follow-on raises | Supplementary offering statement, marketing | $25,000 per secondary raise |
| `PER_TRANSACTION` | Cost per individual transaction | ACH transfers, DocuSign envelopes, escrow | $0.25 per ACH transfer |
| `PER_SMB` | Cost per Small/Medium Business partner | SMB onboarding, program management | $10,000 per SMB onboarding |
| `PER_PLATFORM` | Platform-wide fixed cost | Platform infrastructure, compliance systems | $100,000 annual platform license |

#### Secondary Scopes

| Enum | Definition | Use Case | Example |
| --- | --- | --- | --- |
| `PER_API` | Cost per API call to external service | Data services, credit checks | $0.10 per API call |
| `PER_YEAR` | Annual recurring cost | Annual audits, compliance reporting | $25,000 annual audit fee |
| `PER_FILING` | Cost per regulatory filing | SEC filings, state registrations | $2,500 per SEC filing |

#### Composite Scopes

| Enum | Definition | Use Case | Example |
| --- | --- | --- | --- |
| `PER_INVESTOR_PER_YEAR` | Annual cost per investor | Ongoing investor management | $50 per investor per year |
| `PER_ASSET_PER_YEAR` | Annual cost per asset | Property management, insurance | $1,000 per asset per year |
| `PER_OFFERING_PER_YEAR` | Annual cost per offering | Ongoing compliance, reporting | $15,000 per offering per year |
| `PER_PRIMARY_OFFERING_PER_YEAR` | Annual cost per primary raise | Ongoing Reg A+ compliance | $20,000 per year |
| `PER_SECONDARY_OFFERING_PER_YEAR` | Annual cost per secondary raise | Ongoing secondary compliance | $10,000 per year |
| `PER_PLATFORM_PER_YEAR` | Annual cost per platform | Platform infrastructure, licenses | $120,000 per year |

#### One-time Composite Scopes

| Enum | Definition | Use Case | Example |
| --- | --- | --- | --- |
| `PER_INVESTOR_ONE_TIME` | One-time cost per investor | Initial KYC bundle | $7 per investor one-time |
| `PER_ASSET_ONE_TIME` | One-time cost per asset | Initial appraisal/survey | $3,000 per asset one-time |
| `PER_OFFERING_ONE_TIME` | One-time cost per offering | Offering docs, EDGAR setup | $50,000 one-time |
| `PER_PRIMARY_OFFERING_ONE_TIME` | One-time cost per primary raise | Primary setup (TA onboarding) | $75,000 one-time |
| `PER_SECONDARY_OFFERING_ONE_TIME` | One-time cost per secondary raise | Follow-on offering statement | $25,000 one-time |
| `PER_PLATFORM_ONE_TIME` | One-time cost per platform | Initial platform implementation | $250,000 one-time |

### Standardized Vendor List (v0.1)

#### Core Platform Vendors

| Vendor | Category | Primary Services | Cost Unit Scope | Notes |
| --- | --- | --- | --- | --- |
| North Capital | Platform Infrastructure | White-label platform, investor portal | `PER_OFFERING` + `PER_INVESTOR` | Primary platform provider |
| Oscilar | Compliance | KYC/AML, investor verification | `PER_INVESTOR` | Per-investor verification |
| Enigma | Data Services | Property data, market analytics | `PER_API` | Data API calls |
| Baselayer | Infrastructure | Cloud infrastructure, security | `PER_PLATFORM` | Platform-wide service |
| Rutter | Financial Data | Banking data aggregation | `PER_API` | Financial data API |
| Extend | Document Management | Document storage, retrieval | `PER_TRANSACTION` | Per document transaction |
| Cherre | Property Data | Property intelligence, valuations | `PER_API` | Property data API |

#### Regulatory & Compliance Vendors

| Vendor | Category | Primary Services | Cost Unit Scope | Notes |
| --- | --- | --- | --- | --- |
| Transfer Agent | Investor Services | Share registry, distributions | `PER_INVESTOR` + `PER_TRANSACTION` | Per investor + per distribution |
| EDGAR Service | SEC Compliance | SEC filing, EDGAR submissions | `PER_FILING` | Per SEC filing |
| Auditor | Financial Compliance | Annual audit, quarterly reviews | `PER_OFFERING_PER_YEAR` | Annual audit per offering |
| REIT Compliance Accountant | Tax Compliance | REIT testing, tax compliance | `PER_OFFERING_PER_YEAR` | Annual REIT compliance |
| CRE Counsel | Legal Services | Property legal, compliance | `PER_OFFERING` + `PER_ASSET` | Setup + per property |

#### Property Services Vendors

| Vendor | Category | Primary Services | Cost Unit Scope | Notes |
| --- | --- | --- | --- | --- |
| Appraisal Vendors | Valuation | Property appraisal, due diligence | `PER_ASSET` | Typical commercial appraisal |
| Property Management Firms | Operations | Property management, tenant interface | `PER_ASSET_PER_YEAR` | Annual management fee |
| Special Servicer | Asset Management | Distressed asset management | `PER_ASSET` | Per distressed asset |
| Insurance Providers | Risk Management | Property insurance, liability | `PER_ASSET_PER_YEAR` | Annual per property |

#### Technology & Operations Vendors

| Vendor | Category | Primary Services | Cost Unit Scope | Notes |
| --- | --- | --- | --- | --- |
| DocuSign | Document Management | Electronic signatures | `PER_TRANSACTION` | Per signature transaction |
| ACH Providers | Payment Processing | ACH transfers, payments | `PER_TRANSACTION` | Per ACH transaction |
| Credit Card Processors | Payment Processing | Credit card payments | `PER_TRANSACTION` | Per credit card transaction |
| Data Centers | Infrastructure | Server hosting, backup | `PER_PLATFORM` | Platform-wide infrastructure |

### Cost Card Schema Reference

```yaml
cost_card:
  id: string
  vendor: string
  service: string
  cost_unit_scope: enum
  secondary_scope: enum
  unit_price: number
  minimum_commitment: number
  step_tiers: array
  payer: enum
  timing: enum
  accounting: enum
  amortization_period: number
  scalability_note: string
  replacement_candidates: array
  switching_costs: number
  stage_activation: array
  upreit_specific: boolean
  llc_specific: boolean
  reg_a_required: boolean
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
