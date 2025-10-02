---
id: SLF-78-boxwood-means-acquisition-exploration
title: Boxwood Means Acquisition Model Exploration & Research Primer
status: Draft
stage: Planning
owner: slittle
people: []
reviewers: [finance-team, legal-team]
approver: exec
priority: High
tags: [acquisition, research, modeling, boxwood-means]

# Linear Hierarchy
team: Shelf
super_initiative: "Strategic Acquisitions"
initiative: "Boxwood Means Acquisition"
project: "Acquisition Research & Modeling"
milestone: "Research Primer & Framework Development"
requirement: "SLF-78: Boxwood Means Acquisition Model Exploration"
linear_issue_link: "SLF-78"

# Timestamps & Versioning
created: 2025-01-27T18:00:00Z
updated: 2025-01-27T18:00:00Z
version: 0.1.0

# Context & Relationships
related_docs:
  - linear/tickets/drafts/research-prompts/try-shortcut-prompt-style-guide.md
  - withco-general/docs/global/GBL-TKT_Best_Practices.md
risk_level: Medium
repo_only: true
---

# Boxwood Means Acquisition Model Exploration & Research Primer

Type: Finance Model | Research | Acquisition Analysis  
Owner: @slittle Due: 2025-02-03 Status: Draft

> **How to use this file**
>
> - Skim each section and brain‑dump in bullets.
> - Use the "Quick Commands" below to drop links/notes fast; your LLM (via **TKT‑filler**) will harvest them into the Appendix and a Context Digest, then propose a tight DoD + plan.
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

- Decision enabled: Enable informed decision-making on Boxwood Means acquisition through comprehensive research and illustrative modeling framework
- Why now: Founder meeting completed, need to capitalize on momentum and create draft proposal before receiving actual financials
- Success metric: Complete research primer and Shortcut-ready acquisition modeling prompt delivered within 1 week

## Assumptions

<!-- LLM: List explicit assumptions; flag High‑risk ones; propose 1 quick validation per High risk (<60 min). -->

- A1: Boxwood Means revenue range of $10-20M is accurate (HIGH RISK - validate through public sources)
- A2: Stock-heavy acquisition structure is preferred by both parties
- A3: Public information sufficient for initial research phase
- A4: Shortcut prompt style guide format is appropriate for acquisition modeling
- A5: ~~Company has existing acquisition modeling framework to integrate with~~ → No existing framework, need to create from scratch
- A6: Actual financials will be provided after initial proposal (NEW)

## Inputs / Dependencies

<!-- LLM: Inventory inputs (data, contracts, prior models), owners, dates; call out blockers. -->

- Input → Source/Owner/Date:
  - Boxwood Means company profile → Web research / slittle / 2025-01-27
  - Founder meeting notes → slittle / 2025-01-27
  - Shortcut prompt style guide → linear/tickets/drafts/research-prompts/try-shortcut-prompt-style-guide.md
  - Acquisition modeling framework → SLF-76.0 (dependency) / slittle / TBD
- Upstream dependency: Founder meeting completion (DONE)
- Blockers: Need to create acquisition modeling framework first

## Deliverable

<!-- LLM: Name the artifact(s) + format(s) consumers expect (sheet, redline PDF, memo, dashboard). -->

- Artifacts:
  - Boxwood Means research primer (markdown document)
  - Deep research prompt for company analysis (markdown)
  - Shortcut-ready acquisition modeling prompt (markdown)
  - Illustrative acquisition model based on research estimates
- Consumers: Finance team, executive team, acquisition decision makers

## Definition of Done (pick a ladder)

<!-- LLM: Propose a 3‑tier DoD ladder; each tier must be independently shippable. Keep checks binary and evidence‑backed. -->

- **Fast (same-day):**
  - [ ] Company overview document created with basic Boxwood Means profile
  - [ ] Initial research prompt template drafted
  - [ ] Shortcut prompt framework outlined
- **Standard (2–3 days):**
  - [ ] Comprehensive company research primer completed (financials, business model, market position)
  - [ ] Deep research prompt finalized with specific questions and sources
  - [ ] Shortcut-ready acquisition modeling prompt created per style guide
  - [ ] Illustrative acquisition model created based on research estimates
  - [ ] Competitive analysis included in research primer
  - [ ] Both prompts tested and validated for completeness
- **Gold (1–2 weeks):**
  - [ ] Full acquisition model inputs gathered and validated
  - [ ] Financial model framework established in Shortcut
  - [ ] Due diligence checklist created
  - [ ] Integration plan with existing company models documented

## Feedback & Reviews

<!-- LLM: Identify reviewers + what to check; set SLAs; schedule the earliest possible review. -->

- Reviewer → content/completeness: @slittle
- Reviewer → financial modeling: @finance-team
- Reviewer → legal compliance: @legal-team
- SLA/dates: Review within 24 hours of completion, final approval within 48 hours

## Explicitly Out of Scope

<!-- LLM: List tempting-but-out items with rationale to protect timeline. -->

- OOS1: Actual financial due diligence (requires NDA and confidential access)
- OOS2: Legal analysis of acquisition structure (separate legal workstream)
- OOS3: Integration planning beyond high-level framework
- OOS4: Final valuation calculations (illustrative model only)
- OOS5: Confidential information gathering (public sources only)

## Open Questions

<!-- LLM: Ask up to 5 clarifying Qs; include "how to answer" suggestions (Notion MCP, data pull, ping @). -->

1. What specific financial metrics are most critical for the acquisition model? → Ask finance team for existing model inputs
2. ~~Are there preferred research sources or databases for company analysis?~~ → No preferred sources, use best available public information
3. What level of detail is needed in the Shortcut prompt for acquisition modeling? → Review existing acquisition templates
4. Should the research primer include competitive analysis of similar companies? → Yes, include competitive analysis
5. ~~What timeline constraints exist for the acquisition decision process?~~ → No constraints, focus on creating draft proposal

## Plan (small steps)

<!-- LLM: Break into 20–60 min tasks; order for shortest path to a reviewable artifact; insert checkpoints. -->

- [ ] **Research Setup (30 min)**: Create research primer template and gather initial Boxwood Means data
- [ ] **Deep Research Prompt (45 min)**: Develop comprehensive research questions covering financials, operations, market position
- [ ] **Shortcut Prompt Creation (60 min)**: Build acquisition modeling prompt following style guide format
- [ ] **Illustrative Model Creation (90 min)**: Create preliminary acquisition model based on research estimates
- [ ] **Competitive Analysis (60 min)**: Research and analyze similar companies in the space
- [ ] **Validation & Testing (30 min)**: Review both prompts for completeness and usability
- [ ] **Documentation (20 min)**: Package deliverables and create handover notes
- [ ] **Checkpoint**: Create "Draft complete" checkpoint for review
- [ ] **Review Integration**: Incorporate feedback and finalize deliverables

## Reviewer Checklist

- [ ] Front matter matches ticket template (team, timestamps, related docs).
- [ ] Required sections (Goal, Assumptions, Inputs, Deliverable, DoD, Feedback, Scope, Questions, Plan) are filled.
- [ ] Sub-ticket breakdown aligns with DoD tiers and dependencies.
- [ ] Appendix links reference current templates and research sources.

---

## Proposed Sub-Tickets (Standard DoD)

### SLF-76.0: Acquisition Modeling Framework & Inputs Definition

**Type**: Finance Model | Framework Development  
**Owner**: @slittle  
**Duration**: 1 day  
**Priority**: HIGH (dependency for other tickets)  
**Deliverable**: Acquisition modeling framework and input requirements

**Tasks**:

- [ ] Define acquisition model structure and key components
- [ ] Identify required financial inputs and data sources
- [ ] Create model assumptions framework
- [ ] Define stock-heavy acquisition mechanics
- [ ] Establish validation criteria and quality checks
- [ ] Document model limitations and sensitivities

**Key Inputs to Define**:

- Revenue metrics (historical, projected, growth rates)
- Cost structure (COGS, SG&A, operating expenses)
- Balance sheet items (assets, liabilities, equity)
- Cash flow components (operating, investing, financing)
- Valuation multiples and comparables
- Synergy assumptions and integration costs
- Stock exchange ratios and dilution impact
- Tax implications and structure considerations

### SLF-76.1: Boxwood Means Company Research Primer

**Type**: Research | Company Analysis  
**Owner**: @slittle  
**Duration**: 1 day  
**Dependencies**: SLF-76.0 (for input requirements)  
**Deliverable**: Comprehensive company research document

**Tasks**:

- [ ] Company overview and business model analysis
- [ ] Financial performance research and estimates (per framework inputs)
- [ ] Market position and competitive landscape
- [ ] Key personnel and organizational structure
- [ ] Service offerings and client base analysis

### SLF-76.2: Deep Research Prompt Development

**Type**: Research | Prompt Creation  
**Owner**: @slittle  
**Duration**: 4 hours  
**Dependencies**: SLF-76.0 (for input requirements)  
**Deliverable**: Structured research prompt for comprehensive analysis

**Tasks**:

- [ ] Define research objectives and scope (aligned with framework inputs)
- [ ] Create structured question framework for required data points
- [ ] Identify key research sources and methods
- [ ] Develop validation criteria for research findings
- [ ] Test prompt completeness and usability

### SLF-76.3: Shortcut Acquisition Modeling Prompt

**Type**: Finance Model | Prompt Creation  
**Owner**: @slittle  
**Duration**: 6 hours  
**Dependencies**: SLF-76.0 (framework), SLF-76.1 (research data)  
**Deliverable**: Shortcut-ready acquisition modeling prompt

**Tasks**:

- [ ] Follow Shortcut prompt style guide format
- [ ] Incorporate acquisition model framework and inputs
- [ ] Create illustrative model structure based on research
- [ ] Include validation and quality checks per framework
- [ ] Test prompt in Shortcut environment

### SLF-76.4: Illustrative Acquisition Model

**Type**: Finance Model | Acquisition Analysis  
**Owner**: @slittle  
**Duration**: 1.5 days  
**Dependencies**: SLF-76.0 (framework), SLF-76.1 (research), SLF-76.3 (prompt)  
**Deliverable**: Preliminary acquisition model based on research

**Tasks**:

- [ ] Implement acquisition model framework in Shortcut
- [ ] Input research-based estimates and assumptions
- [ ] Model stock-heavy acquisition structure and mechanics
- [ ] Include sensitivity analysis and scenarios
- [ ] Document assumptions and limitations per framework

### SLF-76.5: Competitive Analysis & Market Context

**Type**: Research | Market Analysis  
**Owner**: @slittle  
**Duration**: 1 day  
**Dependencies**: SLF-76.0 (for valuation context)  
**Deliverable**: Competitive landscape analysis

**Tasks**:

- [ ] Identify direct and indirect competitors
- [ ] Analyze market positioning and differentiation
- [ ] Research industry trends and growth drivers
- [ ] Assess acquisition precedents in the space
- [ ] Document strategic implications and valuation context

---

## Appendix (iteratively built with TKT‑filler)

> The LLM will keep a running **Context Digest** and **Decision Log** here from your drops and answers.

### Links & Resources

- [Boxwood Means Company Website](https://www.boxwoodmeans.com/)
- [Shortcut Prompt Style Guide](research-prompts/try-shortcut-prompt-style-guide.md)
- [Ticket Best Practices](../../../docs/global/GBL-TKT_Best_Practices.md)

### Precedents (why relevant)

- Research prompt templates in linear/tickets/drafts/research-prompts/
- Acquisition modeling frameworks from existing company models
- Shortcut prompt examples for financial modeling

### Prior Work We Can Reuse

- Existing research prompt templates
- Company acquisition model frameworks
- Shortcut prompt style guide format

### Data & Queries

- Boxwood Means public company information
- Industry benchmarks for commercial real estate valuation companies
- Acquisition modeling best practices

### People to Ping / Stakeholders

- Finance team (acquisition model inputs)
- Legal team (compliance review)
- Executive team (decision makers)

### Decision Log (BDR‑style)

- **Decision:** Focus on stock-heavy acquisition structure **Why now:** Founder meeting completed **Options considered:** Cash vs stock vs hybrid **Revisit:** 2025-02-03
- **Decision:** Create illustrative model before receiving actual financials **Why now:** Need draft proposal to maintain momentum **Options considered:** Wait for financials vs proceed with estimates **Revisit:** 2025-02-03

### Context Digest (LLM‑maintained)

- Boxwood Means: Commercial real estate valuation company, $10-20M revenue, 14 employees, founded 2003
- Acquisition context: Stock-heavy structure, founder meeting completed, need research primer and modeling framework
- Deliverables: Research primer, deep research prompt, Shortcut-ready acquisition modeling prompt, illustrative model
- Approach: Create draft proposal based on research estimates, refine with actual financials when available
