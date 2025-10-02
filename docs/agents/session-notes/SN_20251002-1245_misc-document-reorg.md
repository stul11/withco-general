<!-- markdownlint-disable MD003 MD022 -->
<!-- markdownlint-disable MD041 -->

## <!-- markdownlint-disable MD025 -->

id: SN_20251002-1245_misc-document-reorg
title: Session NOTE — Misc Document Reorg (Option D adoption)
version: 1.0.0
created: 2025-10-02T12:45:00Z
updated: 2025-10-02T12:45:00Z
owner: slittle
status: Completed
tags: [session-NOTE, docs, linear, templates]

---

# Session NOTE

- **Task ID**: misc-document-reorg
- **Agent**: Background Agent (Cursor)
- **Owner**: slittle
- **Date**: 2025-10-02T12:45:00Z
- **Duration**: ~45m

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - docs/raw/plans/2025-10-02_document-categorization-and-workflows.md
  - linear/docs/How_to_use_Linear.md
  - linear/docs/templates/ticket-template.md
  - scripts/sync_agents_rules.py
  - docs/agents/workflows/Ticket_Workflow_README.md
  - docs/agents/workflows/Ticket_Validator_Spec.md
  - docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
- **Context & Requirements**:
  - Adopt Option D: move company guidance to docs/company/linear and templates to docs/templates/linear.
  - Preserve old paths with MOVED/DEPRECATED notices; update references and generator.
- **Relevant Prior Work**:
  - Decision Docket items on workflow/docs organization; prior offboarding sessions and link validation work.

---

## Full Findings

- **Summary of Findings**:
  - The repo referenced `linear/docs/How_to_use_Linear.md` and `linear/docs/templates/ticket-template.md` across multiple workflows and specs. Generator text also pointed to the old template path.
- **Detailed Findings**:
  - **Description**: References in workflow docs and generator pointed to old paths.
    - **File(s) Involved**: docs/agents/workflows/Ticket_Workflow_README.md; docs/agents/workflows/Ticket_Validator_Spec.md; docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md; scripts/sync_agents_rules.py
    - **Line Numbers/Sections**: N/A (multiple)
    - **Reasoning**: Align with Option D to centralize guidance/templates under docs/ and keep linear/ as drafts/archive only.
    - **Supporting Evidence**: Grep results during session.

---

## Steps Taken

- **Major Actions**:
  - Created canonical guidance: docs/company/linear/How_to_use_Linear.md
  - Created canonical template: docs/templates/linear/ticket-template.md
  - Added MOVED/DEPRECATED notices in legacy files under linear/docs/\*
  - Updated references in workflow/spec docs and README
  - Updated generator message in scripts/sync_agents_rules.py to new template path
  - Updated archived ticket `related_docs` to point to new template
- **Key Decisions**:
  - Adopted Option D (Guidance + Templates split) as the repository standard
- **Tools/Methods Used**:
  - Ripgrep searches; targeted file edits

---

## Outputs

- **Files Created/Modified**:
  - Created: docs/company/linear/How_to_use_Linear.md (canonical guidance)
  - Created: docs/templates/linear/ticket-template.md (canonical template)
  - Modified: linear/docs/How_to_use_Linear.md (MOVED notice)
  - Modified: linear/docs/templates/ticket-template.md (DEPRECATED notice)
  - Modified: docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md (link updates)
  - Modified: docs/agents/workflows/Ticket_Workflow_README.md (link updates)
  - Modified: docs/agents/workflows/Ticket_Validator_Spec.md (link updates)
  - Modified: docs/global/GBL-PRD_Best_Practices.md (guidance link)
  - Modified: docs/global/GBL-TKT_Best_Practices.md (template link)
  - Modified: scripts/sync_agents_rules.py (generator template path)
  - Modified: linear/tickets/archive/LEG-TKT_Collect_Cost_of_Manufacturing_an_Offering_Inputs.md (related_docs)
- **Key Deliverables**:
  - Option D implemented with preserved backward references
- **Documented Decisions**:
  - Decision Docket updated to record Option D adoption

---

## Citations

- docs/company/linear/How_to_use_Linear.md
- docs/templates/linear/ticket-template.md
- linear/docs/How_to_use_Linear.md
- linear/docs/templates/ticket-template.md
- scripts/sync_agents_rules.py
- docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
- docs/agents/workflows/Ticket_Workflow_README.md
- docs/agents/workflows/Ticket_Validator_Spec.md
- docs/global/GBL-PRD_Best_Practices.md
- docs/global/GBL-TKT_Best_Practices.md
- linear/tickets/archive/LEG-TKT_Collect_Cost_of_Manufacturing_an_Offering_Inputs.md

---

## Risks & Issues Identified

- Minor: Any lingering references to old paths in historical notes may be left intentionally for historical accuracy.
- Minor: Stub README under linear/docs/ could not be created in this environment; MOVED notices mitigate.

---

## Reasoning & Rationale

- Centralizing guidance/templates under docs/ improves discoverability and aligns with plan taxonomy; preserving old paths avoids breakage.

---

## Next Actions

- **Immediate Follow-ups**:
  - [ ] Optional: add linear/docs/README.md stub pointer when environment permits
- **For Next Session**:
  - [ ] Run full link/timestamp validations repository-wide
- **Pending Approvals/Decisions**:
  - [ ] Confirm no additional guidance/templates live under linear/\*

---

## Signoff

- **Reviewer**: slittle
- **Status**: approved
- **Date**: 2025-10-02T12:45:00Z
- **Notes**: Option D adopted; canonical paths updated.

---

## Session NOTE Checklist (Quick)

- [x] Filename matches `SN_YYYYMMDD-HHMM_slug-with-dashes.md`
- [x] Frontmatter includes ISO `created` and `updated`
- [x] Sections populated: Inputs & Context; Steps Taken; Outputs; Next Actions; Signoff
