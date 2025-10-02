<!-- markdownlint-disable MD003 MD022 -->
<!-- markdownlint-disable MD041 -->

## <!-- markdownlint-disable MD025 -->

id: SN_20251002-1230_codelens-to-do-integration
title: Session NOTE - CodeLens To-Do Integration
version: 1.0.0
created: 2025-10-02T12:30:00Z
updated: 2025-10-02T12:30:00Z
owner: slittle
status: Completed
tags: [session-note, codelens, todo, automation]

---

# Session NOTE

- **Task ID**: codelens-to-do-integration
- **Agent**: Background Agent (Cursor)
- **Owner**: slittle
- **Date**: 2025-10-02T12:30:00Z
- **Duration**: ~45m

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - `docs/raw/plans/2025-10-02_todo-codelens-integration.md`
  - `docs/global/TODO_Log.md`
  - `README.md`
  - `.pre-commit-config.yaml`
  - `.cursor/rules/todo-cursor.mdc`
  - `.cursor/commands/todo-add.md`
- **Context & Requirements**:
  - Implement plan to surface TODO items via CodeLens by generating sidecar files (`*.codelens.todo`) from Markdown sources, enforce drift checks, and document workflow.
- **Relevant Prior Work**:
  - Session notes and decisions on markdownlint, AGENTS sync automation, and safety/offboarding rules.

---

## Full Findings

- **Summary of Findings**:
  - A sidecar approach enables stable IDs and editor CodeLens without altering human-readable Markdown. Pre-commit drift checks ensure consistency.
- **Detailed Findings**:
  - **Description**: Stable ID convention required for deterministic sidecar lines and navigation.
  - **File(s) Involved**: `.cursor/commands/todo-add.md`, `.cursor/rules/todo-cursor.mdc`, `docs/agents/templates/TODO_Log_Template.md`.
  - **Line Numbers/Sections**: See edits in repository diff for exact ranges.
  - **Reasoning**: IDs enable unambiguous mapping from Markdown checklist items to CodeLens entries.
  - **Supporting Evidence**: Generated `docs/global/TODO.codelens.todo` with 200+ mapped items in prior runs; drift check wiring added.

---

## Steps Taken

- **Major Actions**:
  - Added stable ID guidance to `docs/agents/templates/TODO_Log_Template.md`.
  - Documented `/TODO-add` behavior to auto-assign IDs and trigger sidecar sync.
  - Added rule addendum describing sidecar requirements in `.cursor/rules/todo-cursor.mdc`.
  - Wired pre-commit drift check for sidecar sync.
  - Generated initial sidecar for `docs/global/TODO_Log.md`.
- **Key Decisions**:
  - Adopt CodeLens sidecar pattern with deterministic ID format `<!-- id: TODO-YYYYMMDD-### -->`.
  - Enforce drift via pre-commit `--check` mode.
- **Tools/Methods Used**:
  - Markdown edits, repository rules/commands updates, and sidecar generation script.

---

## Outputs

- **Files Created/Modified**:
  - `.cursor/commands/todo-add.md` (document ID + sidecar behavior)
  - `.cursor/rules/todo-cursor.mdc` (sidecar requirements)
  - `docs/agents/templates/TODO_Log_Template.md` (ID + CodeLens guidance)
  - `.pre-commit-config.yaml` (sidecar drift check entry)
  - `docs/global/TODO.codelens.todo` (generated sidecar)
- **Key Deliverables**:
  - Working sidecar mechanism with validation wiring and documentation.
- **Documented Decisions**:
  - Decision Docket updated to record adoption of CodeLens To-Do sidecars.

---

## Citations

- `.cursor/commands/todo-add.md`
- `.cursor/rules/todo-cursor.mdc`
- `docs/agents/templates/TODO_Log_Template.md`
- `docs/global/TODO_Log.md`

---

## Risks & Issues Identified

- **Potential Issues**:
  - Editor discovery: ensuring contributors know to open sidecar files for CodeLens.
- **Mitigation Strategies**:
  - README note and command docs; pre-commit drift check prevents stale sidecars.

---

## Reasoning & Rationale

- Chose sidecar approach to preserve human-readable Markdown while enabling editor affordances. Stable IDs ensure deterministic mapping and simplify navigation.

---

## Next Actions

- **Immediate Follow-ups**:
  - [ ] Add examples/screenshots to docs showing opening `*.codelens.todo` in Cursor.
  - [ ] Extend sidecar generation to team TODOs as needed.
- **For Next Session**:
  - [ ] Consider CI job to assert sidecar freshness on PRs.
- **Pending Approvals/Decisions**:
  - [ ] Confirm ID prefix format and finalize across templates.

---

## Signoff

- **Reviewer**: slittle
- **Status**: approved
- **Date**: 2025-10-02T12:30:00Z
- **Notes**: Implementation aligns with plan; no blockers identified.
