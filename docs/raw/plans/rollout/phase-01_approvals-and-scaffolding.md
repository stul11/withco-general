---
type: plan
team: global
created: 2025-10-02T00:00:00Z
updated: 2025-10-02T00:00:00Z
tags: [planning, rollout, phase-01]
status: draft
---

# Phase 01 — Approvals & Scaffolding

Purpose: Lock decisions and prepare the repo for implementation without changing existing content semantics. Designed for handoff to new agents; steps are explicit and verifiable.

## Outcomes

- Approved naming conventions, taxonomy, and schemas (as defined in the main plan)
- Scaffolding created for directories and placeholder docs (no content migration yet)
- Links established between main plan and sub-plans

## Prerequisites

- Read: `docs/raw/plans/2025-10-02_document-categorization-and-workflows.md`
- Read: `docs/raw/plans/rollout/INDEX.md`

## Step-by-step Tasks

1. Confirm Decisions (Owner: Human)

   - Review Sections in main plan:
     - §1 Naming Conventions
     - §2 Directory Taxonomy
     - §3 TODO/TOPLAN Schema
     - §4 Frontmatter Standard
     - §6 Granola and Research
     - §7 Raw → Organized Workflow
     - §10 Migration Plan (choose Standard or Gold)
   - Record decision summary in this file under “Decision Log”.

2. Create Directory Scaffolding (Owner: Agent, via PR)

   - For each team in `{PROD, ANA, DATA, LEG, AM, global}` create:
     - `linear/{TEAM}/TODO.md` (empty) — do not rename existing lists yet
     - `linear/{TEAM}/TOPLAN.md` (empty)
     - `linear/{TEAM}/docs/.keep`
     - `linear/{TEAM}/raw/.keep`
     - `linear/{TEAM}/tickets/draft/.keep`
     - `linear/{TEAM}/projects/draft/.keep`
     - `linear/{TEAM}/plans/draft/.keep`
   - In `docs/` ensure presence of:
     - `docs/agents/session-notes/` (no change)
     - `docs/granola/outputs/.keep`
     - `docs/research/` (optional)
     - `docs/meeting-notes/` (optional)
     - `docs/raw/` (no change)
     - `docs/raw/plans/rollout/INDEX.md` (exists)

3. Add Placeholders and READMEs (Owner: Agent)

   - Add minimal `README.md` files to newly created directories describing purpose and examples (no heavy content).
   - Ensure line length <= 120 and headings follow Markdown linting rules.

4. Link Sub-Plans (Owner: Agent)

   - From the main plan’s “Phased Rollout” section, add links to:
     - `rollout/INDEX.md`
     - `rollout/phase-01_approvals-and-scaffolding.md`

5. Open PR for Scaffolding (Owner: Agent)
   - Title: `chore: scaffold taxonomy rollout directories (phase 01)`
   - Description: Summarize decisions, list created dirs/files, and include links to plans.
   - Request review from Human owner.

## Success Criteria

- All directories exist as specified
- Placeholders/READMEs added
- No existing files renamed or moved
- PR opened and linked to plan documents

## Decision Log

- Migration mode: <Standard | Gold>
- Meeting-notes handling: <separate `docs/meeting-notes/` | folded into granola>
- Research category: <introduce `RS_` now | defer>

## Risks & Mitigations

- Risk: Directory churn without usage — Mitigation: keep placeholders minimal and documented
- Risk: Confusion over team/global placement — Mitigation: follow rule “team if known, else global” in commands
