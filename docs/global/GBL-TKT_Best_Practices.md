---
id: GBL-TKT_Best_Practices
title: Ticket Best Practices
status: Draft
stage: Planning
owner: slittle
people: []
reviewers: []
approver: exec
priority: Medium
tags: [ticket, workflow, linear, best-practices]

# Linear Hierarchy
team: Product
super_initiative: "TBD"
initiative: "TBD"
project: "TBD"
milestone: "TBD"
requirement: "TBD"
linear_issue_link: "TBD"

# Timestamps & Versioning
created: 2025-09-27T15:00:00Z
updated: 2025-09-27T15:00:00Z
version: 0.1.0

# Context & Relationships
related_docs:
  - withco-general/linear/docs/templates/ticket-template.md
risk_level: Low
repo_only: true
---

# <Ticket Title>

> Scope: Personal drafting best practices for tickets in this repo. Do not modify company Linear documentation; use `linear/docs/How_to_use_Linear.md` as read-only reference.

Type: <Finance Model | Contract Review | Pricing Change | Data Pull | Compliance | Vendor | Board | Other>
Owner: @me Due: YYYY‑MM‑DD Status: Draft

> **How to use this file**
>
> - Skim each section and brain‑dump in bullets.
> - Use the “Quick Commands” below to drop links/notes fast; your LLM (via **TKT‑filler**) will harvest them into the Appendix and a Context Digest, then propose a tight DoD + plan.
> - Keep the **Requirement** under 1 week for a single IC; group larger things under a **Milestone**.

## Quick Commands (inline while chatting)

`+link <label>: <url>`  
`+precedent <why relevant>: <url>`  
`+doc <type>: <url>` (e.g., MSA/SOW/memo/model)  
`+NOTE <short fact>`  
`+assume <assumption>`  
`+risk <risk>`  
`+owner <who>`  
`+deadline <YYYY‑MM‑DD>`

---

## Goal / Purpose

<!-- LLM: In 1–2 sentences, translate this into the decision this deliverable enables, and why now. Offer a one‑line success metric. -->

- Decision enabled:
- Why now:
- Success metric:

## Assumptions

<!-- LLM: List explicit assumptions; flag High‑risk ones; propose 1 quick validation per High risk (<60 min). -->

- A1:
- A2:

## Inputs / Dependencies

<!-- LLM: Inventory inputs (data, contracts, prior models), owners, dates; call out blockers. -->

- Input → Source/Owner/Date:
- Upstream dependency:
- Blockers:

## Deliverable

<!-- LLM: Name the artifact(s) + format(s) consumers expect (sheet, redline PDF, memo, dashboard). -->

- Artifacts:
- Consumers:

## Definition of Done (pick a ladder)

<!-- LLM: Propose a 3‑tier DoD ladder; each tier must be independently shippable. Keep checks binary and evidence‑backed. -->

- **Fast:**
  - [ ] …
- **Standard:**
  - [ ] …
- **Gold:**
  - [ ] …

## Feedback & Reviews

<!-- LLM: Identify reviewers + what to check; set SLAs; schedule the earliest possible review. -->

- Reviewer → scope/sign‑off: @
- Reviewer → numbers/legal: @
- SLA/dates:

## Explicitly Out of Scope

<!-- LLM: List tempting-but-out items with rationale to protect timeline. -->

- OOS1:
- OOS2:

## Open Questions

<!-- LLM: Ask up to 5 clarifying Qs; include “how to answer” suggestions (Notion MCP, data pull, ping @). -->

1.
2.
3.

## Plan (small steps)

<!-- LLM: Break into 20–60 min tasks; order for shortest path to a reviewable artifact; insert checkpoints. -->

- [ ] Step 1
- [ ] Step 2
- [ ] Step 3

---

## Appendix (iteratively built with TKT‑filler)

> The LLM will keep a running **Context Digest** and **Decision Log** here from your drops and answers.

### Links & Resources

- …

### Precedents (why relevant)

- …

### Prior Work We Can Reuse

- …

### Data & Queries

- …

### People to Ping / Stakeholders

- …

### Decision Log (BDR‑style)

- **Decision:** … **Why now:** … **Options considered:** A/B/C **Revisit:** YYYY‑MM‑DD

### Context Digest (LLM‑maintained)

- …
