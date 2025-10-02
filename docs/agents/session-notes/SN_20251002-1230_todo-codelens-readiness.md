---
id: SN_20251002_todo-codelens-readiness
title: Session Note - TODO CodeLens Readiness Audit
version: 1.0.0
created: 2025-10-02T12:30:00Z
updated: 2025-10-02T12:30:00Z
owner: slittle
status: Draft
tags: [session-note, planning, todos]
---

# Session NOTE

- **Task ID**: todo-codelens-readiness
- **Agent**: gpt-5-codex
- **Owner**: slittle
- **Date**: 2025-10-02T12:30:00Z
- **Duration**: ~1.2h

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - `00-key-docs/TODO_Log.md`
  - `docs/global/TODO_Log.md`
  - `docs/agents/templates/TODO_Log_Template.md`
  - `.cursor/commands/todo-add.md`
  - `.cursor/rules/todo-cursor.mdc`
  - `docs/raw/plans/2025-10-02_document-categorization-and-workflows.md`
  - Repository root README and `docs/global/README.md`
- **Context & Requirements**:
  - Assess the entire repository for TODO tracking patterns and supporting rules.
  - Produce a restructuring plan that enables Cursor/Codex CodeLens on TODO items without breaking existing workflows.
- **Relevant Prior Work**:
  - The taxonomy planning doc proposes renaming TODO logs and adding TOPLAN companions but has not been implemented yet.
  - Offboarding and session note requirements enforce updates to the global TODO log at the end of each session.

---

## Full Findings

- **Summary of Findings**:
  - Global and local TODO logs are Markdown checklist documents; they do not emit comment-style TODO markers that would trigger
    CodeLens.
  - `/TODO-add` and the TODO template reinforce the checkbox schema, so any redesign must stay compatible with the automated
    tooling.
  - The taxonomy plan already anticipates renaming and normalizing backlog files, providing a natural milestone for layering in
    CodeLens support.
- **Detailed Findings**:
  1. **Canonical backlog duplication**
     - `00-key-docs/TODO_Log.md` and `docs/global/TODO_Log.md` contain the same data and expect manual checkbox updates; neither
       emits TODO comments.
     - Team TODO stubs under `linear/` are empty shells, so CodeLens readiness must account for future content there.
  2. **Template & command coupling**
     - `docs/agents/templates/TODO_Log_Template.md` prescribes section headings that would need ID annotations for any comment
       sync logic.
     - `.cursor/commands/todo-add.md` assumes Markdown output, and `.cursor/rules/todo-cursor.mdc` forces agents to use
       `todo_write`, cementing the Markdown-first workflow.
  3. **Planning alignment**
     - `docs/raw/plans/2025-10-02_document-categorization-and-workflows.md` already defines shared schemas and file renames,
       making it the best anchor for any structural changes tied to CodeLens.

---

## Steps Taken

- Read both global TODO log copies and sampled team TODO placeholders.
- Reviewed TODO-related templates, cursor commands, and rules to capture automation boundaries.
- Inspected taxonomy planning guidance for upcoming structural changes.
- Ran `rg "TODO" -n` to spot ad-hoc markers and confirm CodeLens exposure gaps.
- Drafted a dedicated planning document outlining options and phased implementation.

---

## Outputs

- **Files Created/Modified**:
  - `docs/raw/plans/2025-10-02_todo-codelens-integration.md` (new planning document recommending a dual-surface backlog with CodeLens sidecars).
- **Key Deliverables**:
  - Repository-wide plan for aligning Markdown TODO logs with CodeLens automation while preserving audit trails.
- **Documented Decisions**:
  - Recommend pursuing a dual-surface backlog (Markdown canonical + generated comment sidecar) pending maintainer review.

---

## Citations

- `00-key-docs/TODO_Log.md`
- `docs/global/TODO_Log.md`
- `docs/agents/templates/TODO_Log_Template.md`
- `.cursor/commands/todo-add.md`
- `.cursor/rules/todo-cursor.mdc`
- `docs/raw/plans/2025-10-02_document-categorization-and-workflows.md`
- `README.md`
- `docs/global/README.md`

---

## Risks & Issues Identified

- Adding comment sidecars introduces synchronization overhead; automation must prevent drift.
- CodeLens behavior for custom file extensions needs validation before committing to a sidecar format.
- Pending taxonomy migrations may overlap with the TODO rename; workstreams should coordinate to avoid conflicting edits.

---

## Reasoning & Rationale

- Keeping Markdown as the canonical backlog respects existing automation (todo_write, `/TODO-add`) while giving CodeLens a clean
  signal via sidecar files.
- Introducing stable IDs per item allows deterministic generation of comment entries without brittle text matching.
- Aligning the rollout with the taxonomy plan minimizes duplicate migration passes across TODO-related assets.

---

## Next Actions

- **Immediate Follow-ups**:
  - [ ] Validate CodeLens detection for proposed sidecar formats (HTML comment vs `.todo`).
  - [ ] Prototype ID tagging strategy within the Markdown schema.
- **For Next Session**:
  - [ ] Update TODO templates and `/TODO-add` spec based on the recommended architecture.
  - [ ] Define sync script requirements and testing strategy.
- **Pending Approvals/Decisions**:
  - [ ] Maintainer approval of the dual-surface backlog approach and coordination with taxonomy migration timing.

---

## Signoff

- **Reviewer**: pending
- **Status**: pending
- **Date**: 2025-10-02T12:30:00Z
- **Notes**: Awaiting maintainer feedback on the plan.
