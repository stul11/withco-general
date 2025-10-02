---
id: LEG-TKT_Collect_Cost_Manufacturing_Offering_Inputs
title: Collect Cost of Manufacturing an Offering Inputs
status: Draft
stage: Planning
owner: slittle
people: [brian, kevin]
reviewers: [brian, kevin]
approver: slittle
priority: High
tags:
  [
    legal,
    data,
    research,
    cost-manufacturing,
    offering-inputs,
    upreit,
    llc,
    minimum-check,
  ]

# Linear Hierarchy
team: Legal
super_initiative: "TBD"
initiative: "TBD"
project: "TBD"
milestone: "TBD"
requirement: "TBD"
linear_issue_link: "https://linear.app/withco/issue/LEG-63/collect-cost-of-manufacturing-an-offering-inputs"

# Timestamps & Versioning
created: 2025-01-27T17:00:00Z
updated: 2025-01-27T17:00:00Z
version: 0.1.0

# Context & Relationships
related_docs:
  - withco-general/docs/templates/linear/ticket-template.md
  - withco-general/docs/global/GLB-TKT_Best_Practices.md
  - https://linear.app/withco/issue/LEG-63/collect-cost-of-manufacturing-an-offering-inputs
  - https://linear.app/withco/issue/LEG-9/determine-minimum-check-size
  - https://docs.google.com/spreadsheets/d/195wUpk6d5dZS61sf5MbemVhean0FWf5YK3o6v8nctlE/edit?usp=drive_link
  - withco-general/docs/raw/economics-cost-structure-initial-context.md
risk_level: High
repo_only: true
---

# Collect Cost of Manufacturing an Offering Inputs

## Goal / Purpose

- **Decision enabled:** Structure choice (UPREIT vs LLC) and minimum check size policy with two-tiered investor structure
- **Why now:** Need draft calculations today for Brian/Kevin review tomorrow; integrate with LEG-9 minimum check size analysis
- **Success metric:** Clean, board-ready cost model supporting both structure decisions and two-tiered minimum analysis

## Assumptions

- **A1:** RSM inputs will be available within 1-2 weeks
- **A2:** New REIT compliance accountant will be identified by Minta/Goodwin
- **A3:** Current Excel model contains all necessary vendor data
- **A4:** Two-tiered minimum structure (existing vs new investors) is viable approach

## Inputs / Dependencies

- **Input → Source/Owner/Date:**
  - Current Excel model → You / Today
  - Vendor contracts/quotes → You / Available
  - RSM inputs → RSM / Pending
  - REIT compliance accountant → Minta/Goodwin / Pending
  - LEG-9 minimum check size work → You / In progress
- **Upstream dependency:** LEG-9 minimum check size analysis
- **Blockers:** RSM inputs, REIT compliance accountant

## Deliverable

- **Artifacts:**
  - Updated Excel model with standardized enums
  - Cost Card schema v0.1
  - Draft calculations for Brian/Kevin review
  - Two-tiered minimum structure analysis
- **Consumers:** Brian, Kevin, LEG-9 team

## Definition of Done (DoD)

**Fast (today):**

- [ ] Core cost calculation draft for both UPREIT/LLC structures
- [ ] Key assumptions documented with pending inputs noted
- [ ] Draft ready for Brian/Kevin review tomorrow
- [ ] Authoritative vendor/service list with enum mappings
- [ ] Provisional Cost Card schema v0.1
- [ ] Excel model standardization with new organization
- [ ] Stage activation mapping completed
- [ ] Research prompts for unverified assumptions
- [ ] Two-tiered minimum structure analysis integrated

## Feedback & Reviews

- **Reviewer → scope/sign-off:** Brian, Kevin / Tomorrow
- **Reviewer → numbers/legal:** You / Final approval
- **SLA/dates:** Draft today, review tomorrow, final Monday

## Explicitly Out of Scope

- **OOS1:** Expense vs. Capitalize accounting treatment
- **OOS2:** Making final structure decisions (UPREIT vs LLC)
- **OOS3:** Creating new vendor relationships

## Open Questions

1. **RSM timeline:** When can we expect RSM inputs?
2. **REIT accountant:** What's the timeline for Minta to find REIT compliance accountant?
3. **Two-tiered structure:** What specific criteria define "existing investor" for minimum check purposes?

## Plan (small steps)

- [ ] **Review existing model & identify key drivers (10 min)**
- [ ] **Integrate available inputs (20 min)**
- [ ] **Draft core calculations (15 min)**
- [ ] **Document assumptions & gaps (10 min)**
- [ ] **Prepare for review (5 min)**
- [ ] **Create standardized vendor list (30 min)**
- [ ] **Develop Cost Card schema (45 min)**
- [ ] **Map stage activations (30 min)**
- [ ] **Integrate two-tiered analysis (45 min)**

---

## Appendix

### Links & Resources

- [LEG-63: Collect Cost of Manufacturing an Offering Inputs](https://linear.app/withco/issue/LEG-63/collect-cost-of-manufacturing-an-offering-inputs)
- [LEG-9: Determine Minimum Check Size](https://linear.app/withco/issue/LEG-9/determine-minimum-check-size)
- [Existing Excel Model](https://docs.google.com/spreadsheets/d/195wUpk6d5dZS61sf5MbemVhean0FWf5YK3o6v8nctlE/edit?usp=drive_link)
- `withco-general/docs/raw/economics-cost-structure-initial-context.md`

### Precedents

- Arrived.com platform (SFR focus)
- Reg A+ (Tier II) offering structure
- North Capital white-label platform
- Two-tiered minimum structures from retail investment platforms

### Prior Work

- Existing Excel model with ~50 vendor/service rows
- Initial LEG-9 minimum check size work
- Stage mapping already aligned
- Vendor contracts and quotes available

### Data & Queries

- Current Excel model (Google Sheets)
- Cost_Unit_Scope enums (Per SMB, Per Investor, Per Asset, etc.)
- Platform minimum check research data

### People to Ping / Stakeholders

- Brian (reviewer)
- Kevin (reviewer)
- Minta/Goodwin (REIT compliance accountant)
- RSM (pending inputs)

### Decision Log

- **Decision:** Target Fast tier for today's draft **Why now:** Brian/Kevin review tomorrow **Options considered:** Fast/Standard/Gold **Revisit:** Tomorrow after review

### Context Digest

- Urgent need for draft calculations today
- Integration with LEG-9 two-tiered minimum structure analysis
- Pending inputs from RSM and REIT compliance accountant
- Focus on both UPREIT and LLC structure cost comparison
