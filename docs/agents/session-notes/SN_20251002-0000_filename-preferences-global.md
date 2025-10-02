---
type: session-NOTE
team: global
created: 2025-10-02T00:00:00Z
updated: 2025-10-02T00:00:00Z
tags: [naming, rules]
status: draft
---

# Session NOTE

- **Task ID**: filename-preferences-global
- **Agent**: GPT-5 (Cursor)
- **Owner**: slittle
- **Date**: 2025-10-02T00:00:00Z
- **Duration**: ~25 minutes

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - `docs/raw/plans/2025-10-02_document-categorization-and-workflows.md`
  - `docs/raw/plans/rollout/phase-02_rules-and-commands.md`
  - `docs/raw/plans/rollout/phase-01_approvals-and-scaffolding.md`
  - `.cursor/rules/agent-session-notes.mdc`
- **Context & Requirements**:
  - Apply global NOTE filename patterns across the repo (SN/MN/GR/RN) per plan §1.1.
  - Create a Cursor rule that enforces these patterns globally.
  - Align examples and cross-references; maintain ISO timestamps and 15-min rounding.
- **Relevant Prior Work**:
  - `SN_20251002-0000_phase-01-scaffolding-verification.md`

---

## Full Findings

- **Summary of Findings**:
  - A new global Cursor rule ensures NOTE filename patterns are enforced for SN/MN/GR/RN.
  - The rule cites the main plan and rollout sub-plans for traceability.
- **Detailed Findings**:
  - **Description**: Implemented `.cursor/rules/naming-global.mdc` with `alwaysApply: true` and scope `**/*.md`.
  - **File(s) Involved**: `.cursor/rules/naming-global.mdc`
  - **Line Numbers/Sections**: Header and "Required Filename Patterns" section
  - **Reasoning**: Central enforcement avoids drift and supports future migration.
  - **Supporting Evidence**: Plan §1.1; rollout phases §2 and §1 reference naming and rules

---

## Steps Taken

- **Major Actions**:
  - Created `.cursor/rules/session-NOTE-naming-global.mdc` then expanded to cover SN/MN/GR/RN.
  - Renamed rule to `.cursor/rules/naming-global.mdc`; removed the old file.
  - Resolved a minor lint warning (capitalization in example).
- **Key Decisions**:
  - Use a single global rule for all NOTE types with explicit directories.
- **Tools/Methods Used**:
  - Cursor apply/patch edits; in-repo lint checks

---

## Outputs

- **Files Created/Modified**:
  - `.cursor/rules/naming-global.mdc` (new): global NOTE filename enforcement
  - `.cursor/rules/session-NOTE-naming-global.mdc` (deleted): superseded by the above
- **Key Deliverables**:
  - Repository-wide rule enforcing NOTE filename patterns
- **Documented Decisions**:
  - Will append decision summary to `docs/global/Decision_Docket.md`

---

## Citations

- `docs/raw/plans/2025-10-02_document-categorization-and-workflows.md:L33-L41`
- `docs/raw/plans/rollout/phase-02_rules-and-commands.md:L39-L46`
- `docs/raw/plans/rollout/phase-01_approvals-and-scaffolding.md:L26-L38`

---

## Risks & Issues Identified

- **Potential Issues**:
  - Legacy files may not yet match naming; migration will require careful link updates.
- **Mitigation Strategies**:
  - Follow the Standard migration plan (§10.1) and run link checks before commit.

---

## Reasoning & Rationale

- Centralizing the naming rule reduces duplication and enforces consistency for all NOTE types.

---

## Next Actions

- **Immediate Follow-ups**:
  - Add decision summary to `docs/global/Decision_Docket.md`.
  - Add follow-up tasks to `docs/global/TODO_Log.md` for migration and link verification.
- **For Next Session**:
  - Execute migration steps and generate rename index if choosing Gold option.
- **Pending Approvals/Decisions**:
  - Confirm Standard vs Gold migration mode.

---

## Signoff

- **Reviewer**: slittle
- **Status**: pending
- **Date**: 2025-10-02T00:00:00Z
- **Notes**: —


