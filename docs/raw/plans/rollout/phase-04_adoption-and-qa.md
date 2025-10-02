---
type: plan
team: global
created: 2025-10-02T00:00:00Z
updated: 2025-10-02T00:00:00Z
tags: [planning, rollout, phase-04]
status: draft
---

# Phase 04 — Adoption & QA

Purpose: Drive consistent usage of the new taxonomy, commands, and naming conventions; validate quality via checks; smooth handoff to day-to-day operations.

## Outcomes

- Teams consistently use `TODO.md`/`TOPLAN.md` and the new directories
- Session NOTEs follow naming and frontmatter standards (CREATED-rounded HHMM, immutable)
- Commands `/todo-add` and `/toplan-add` used with required `source:` links
- Link and timestamp checks pass in CI (or local equivalent)

## Prerequisites

- Phase 01–03 merged
- PRs for command/rule docs merged

## Step-by-step Tasks

1. Enable CI Checks (Owner: Agent)
   - Add a CI workflow to run `scripts/check_markdown_links.py` and `scripts/validate_iso_timestamps.py docs` (if scripts exist)
   - If not present, add a simple GitHub Action to run a grep-based link check placeholder and timestamp linter TODO

2. Author Usage Guides (Owner: Agent)
   - `docs/README.md`: quick start, where to put work, links to `TODO.md` and `TOPLAN.md`
   - `linear/*/README.md`: brief usage per team (routing rules, drafts folders)

3. Command Adoption (Owner: Agent)
   - Add examples to `.cursor/commands/todo-add.md` and `toplan-add.md` for team/global
   - Ensure both docs show multi-line schema and `source:` requirement

4. Session NOTE Consistency (Owner: Agent)
   - Add a short “Session NOTE checklist” snippet to `docs/agents/templates/Session_Note_Template.md`
   - Cross-link from `agent-session-notes.mdc`

5. Link Cleanup Sweep (Owner: Agent)
   - Run link checker and fix any residual broken references after Phase 03
   - Commit with `chore(phase-04): link cleanup`

6. Training & Handoff (Owner: Human)
   - Brief walkthrough of structure and commands
   - Confirm preferences for future enhancements (e.g., `RS_` usage)

## Checks (Background Agent Verification)

### Check A: Command Adoption
**Ask**: Verify at least one new item added to global `TODO.md` and one team `TOPLAN.md` via commands with `source:` links.
**Output**: `docs/agents/session-notes/SN_YYYYMMDD-HHMM_phase-04-command-adoption.md` with file paths and snippets.

### Check B: Session NOTE Consistency
**Ask**: Sample 5 latest session NOTEs; verify filename pattern, frontmatter created/updated, and required sections.
**Output**: `SN_YYYYMMDD-HHMM_phase-04-session-note-consistency.md` with a checklist table.

### Check C: CI/Local Validation
**Ask**: Run link and timestamp checks; report results and fixes.
**Output**: `SN_YYYYMMDD-HHMM_phase-04-validation.md` summarizing outcomes.

## Success Criteria

- CI (or local) checks pass
- Command usage verified in both global and one team area
- Sampled session NOTEs comply fully
