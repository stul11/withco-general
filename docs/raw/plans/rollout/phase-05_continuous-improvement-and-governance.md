---
type: plan
team: global
created: 2025-10-02T00:00:00Z
updated: 2025-10-02T00:00:00Z
tags: [planning, rollout, phase-05]
status: draft
---

# Phase 05 — Continuous Improvement & Governance

## Purpose

Lock in long-term sustainability of the taxonomy, naming, and workflows by hardening quality gates, finishing
Gold+ migration artifacts, consolidating duplicates, and establishing governance and ownership.

## Outcomes

- Gold+ upgrade path from the main plan (§10.4) fully realized (rename index, migration report, stubs/symlinks).
- Docs QA expanded to enforce naming, session NOTE completeness, and TODO/TOPLAN metadata rules.
- Duplicates consolidated (glossary, TODO logs) with a single canonical source and clear ownership.
- Team adoption guidance finalized; steady-state governance documented.

## Prerequisites

- Phases 01–04 merged and the Docs QA workflow green.
- Rename candidates/index prepared where needed.

## Step-by-step Tasks

1. Gold+ Hardening (per main plan §10.4)

   - Create/refresh `docs/indexes/renames-YYYYMMDD.md` mapping old → new and rationale.
   - Add `docs/indexes/migration-report-YYYYMMDD.md` summarizing batches, deviations, and residuals.
   - For high-traffic legacy paths, add short stubs or symlinks with a pointer to new locations.

2. Governance & Ownership

   - Document maintainers and escalation for taxonomy/rules in `docs/indexes/governance.md`
     (scope: naming, session notes, TODO/TOPLAN, rollout plans).
   - Add a brief "Contributor Standards" section in `docs/README.md` linking to governance and rules.

3. Quality Gates Expansion (Docs QA + local)

   - Enforce NOTE filename patterns and ISO timestamps (already present; keep).
   - Add checks:
     - Session NOTE completeness: required sections present (template-aligned).
     - TODO/TOPLAN items: enforce `source:` and stable ID presence; labels/priorities schema.
     - Naming rule: SN/MN/GR/RN filename patterns across `docs/**`.
   - Provide scripts under `scripts/validators/`:
     - `validate_session_notes.py`
     - `validate_todo_toplan_items.py`
     - `validate_note_filenames.py`
   - Mirror these in CI (`.github/workflows/docs-qa.yml`) and document local equivalents.

4. Consolidation & Canonicalization

   - Glossary: designate `docs/global/glossary/APPROVED-GLOSSARY.md` as canonical; fold others or mark as MOVED.
   - TODO logs: complete the rename path to `00-key-docs/TODO.md` and ensure `docs/global/TODO_Log.md` references
     are updated or deprecated per migration plan.
   - Remove or annotate duplicated context docs; link the canonical counterpart.

5. Team Adoption & Training

   - Add lightweight `linear/{TEAM}/README.md` usage notes (routing rules; `TODO.md`/`TOPLAN.md` pointers).
   - Include one verified sample in a team list demonstrating labels, priority, `source:`, and stable ID.

## Checks (Background Agent Verification)

- Check A: Gold+ artifacts exist

  - [ ] `docs/indexes/renames-YYYYMMDD.md` present and complete
  - [ ] `docs/indexes/migration-report-YYYYMMDD.md` present and linked from the main plan

- Check B: Quality gates pass

  - [ ] CI `Docs QA` green on PR and main
  - [ ] Local validators report 0 errors (naming, session notes, TODO/TOPLAN)

- Check C: Consolidation complete

  - [ ] Glossary canonicalized; non-canonical files carry MOVED/DEPRECATED notice
  - [ ] Global TODO rename completed; legacy references updated or stubbed

- Check D: Team adoption

  - [ ] At least one team `README.md` updated
  - [ ] One validated sample item present in a team list

**Output**: Create `docs/agents/session-notes/SN_YYYYMMDD-HHMM_phase-05-validation.md` summarizing each check.

## Success Criteria

- Gold+ artifacts committed and linked; no broken links.
- Governance doc in place with clear ownership.
- CI/local quality gates enforce naming, completeness, and item schemas.
- Consolidation done; contributors have clear guidance and examples.
