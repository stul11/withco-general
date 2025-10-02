<!-- markdownlint-disable MD013 MD022 MD024 MD025 MD032 MD033 -->

## <!-- markdownlint-disable MD025 -->

id: SN_20251002-1800_ticket-draft-standardization
title: Session NOTE – Ticket Draft Standardization & Backlog Updates
version: 1.0.0
created: 2025-10-02T18:00:00Z
updated: 2025-10-02T18:00:00Z
owner: slittle
status: Pending Review
tags: [ticket-audit, backlog, option3]

---

# Session NOTE

- **Task ID**: Ticket draft audit & backlog normalization
- **Agent**: gpt-5-codex (background)
- **Owner**: slittle
- **Date**: 2025-10-02T18:00:00Z
- **Duration**: ~90 minutes

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - `docs/templates/linear/ticket-template.md`
  - `docs/global/GBL-TKT_Best_Practices.md`
  - `docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md`
  - `docs/global/TODO_Log.md`
  - Draft tickets under `linear/tickets/drafts/`
- **Context & Requirements**:
  - Audit all drafts under `linear/tickets/drafts/` for template compliance, ISO timestamps, and reviewer readiness.
  - Align TODO backlog entries to Option 3 schema with stable IDs.
  - Capture findings via Decision Docket entry and session note; add reviewer checklists per draft.
- **Relevant Prior Work**:
  - Background Agent Draft Review Workflow and ticket wizard documentation from 2025-10-01 to 2025-10-02 sessions.
  - Existing TODO backlog from prior cleanup phases (Option 3 adoption notes).

---

## Full Findings

- **Summary of Findings**:
  - Legacy drafts lacked full front matter, multi-tier DoD, and reviewer guidance; RSM-related drafts also contained duplicate YAML blocks.
  - TODO Log sections still relied on checkbox syntax, preventing CodeLens sidecar alignment.
  - Decision Docket missing entry documenting the normalization effort.
- **Detailed Findings**:
  - **Excel cost analysis draft** lacked tiered DoD, reviewer checklist, and reference alignment. Added full template structure, 3-tier DoD, plan, and appendix consolidation.【F:linear/tickets/drafts/excel-cost-analysis-funnel-integration.md†L1-L197】
  - **RSM documentation/action drafts** required full front matter, DoD tiers, plan normalization, and reviewer checklists; duplicate YAML removed.【F:linear/tickets/drafts/rsm-call-notes-documentation.md†L1-L150】【F:linear/tickets/drafts/rsm-action-items-summary.md†L1-L153】【F:linear/tickets/drafts/rsm-call-notes-organized.md†L1-L165】
  - **Vendor list draft** converted into template-compliant structure with goals, DoD ladders, and appendix-based tables for enums and vendors.【F:linear/tickets/drafts/standardized-vendor-list.md†L1-L233】
  - **SLF-78 draft** retained content but updated ID, added reviewer checklist to mirror workflow requirements.【F:linear/tickets/drafts/SLF-78-boxwood-means-acquisition-exploration-draft.md†L1-L210】
  - **TODO Log**: Replaced checkbox backlog for "Next Agent Session" with Option 3 entries (12 items) to track validator runs, migrations, and automation follow-ups.【F:docs/global/TODO_Log.md†L200-L248】
  - **Decision Docket**: Added entry summarizing normalization decision and linking updated drafts + session note.【F:docs/global/Decision_Docket.md†L9-L16】

---

## Steps Taken

- **Major Actions**:
  - Reviewed ticket template and best practices to map required sections.
  - Normalized six drafts (Excel, RSM trio, vendor list, SLF-78) with consistent front matter, section headings, DoD tiers, plans, and reviewer checklists.
  - Consolidated appendices to house prompts, schemas, and tables while maintaining references.
  - Converted TODO backlog section to Option 3 entries and added new follow-ups for validator checks, SLF-73 updates, vendor review, and sync script offer.
  - Recorded decision summary in Decision Docket and prepared this session note.
- **Key Decisions**:
  - Promote normalization approach vs piecemeal edits to align with Background Agent workflow.
  - Track outstanding validator + documentation tasks via Option 3 items to enable CodeLens.
- **Tools/Methods Used**:
  - Manual markdown editing with `cat`/`apply_patch`.
  - `rg` to locate sections (timestamps, Checkpoint lines).
  - Template references for session note + ticket structure.

---

## Outputs

- **Files Created/Modified**:
  - `linear/tickets/drafts/excel-cost-analysis-funnel-integration.md` – normalized template, DoD tiers, reviewer checklist, appendix restructuring.【F:linear/tickets/drafts/excel-cost-analysis-funnel-integration.md†L1-L197】
  - `linear/tickets/drafts/rsm-call-notes-documentation.md` – single YAML front matter, normalized sections, reviewer checklist.【F:linear/tickets/drafts/rsm-call-notes-documentation.md†L1-L150】
  - `linear/tickets/drafts/rsm-action-items-summary.md` – template-compliant structure and appendix grouping.【F:linear/tickets/drafts/rsm-action-items-summary.md†L1-L153】
  - `linear/tickets/drafts/rsm-call-notes-organized.md` – added goal, DoD tiers, plan, reviewer checklist, and appendix metadata.【F:linear/tickets/drafts/rsm-call-notes-organized.md†L1-L165】
  - `linear/tickets/drafts/standardized-vendor-list.md` – reorganized into template with DoD ladders and tables under appendix.【F:linear/tickets/drafts/standardized-vendor-list.md†L1-L233】
  - `linear/tickets/drafts/SLF-78-boxwood-means-acquisition-exploration-draft.md` – corrected ID, added reviewer checklist.【F:linear/tickets/drafts/SLF-78-boxwood-means-acquisition-exploration-draft.md†L1-L210】
  - `docs/global/TODO_Log.md` – Option 3 backlog items for workflow follow-ups and validator tasks.【F:docs/global/TODO_Log.md†L200-L248】
  - `docs/global/Decision_Docket.md` – new decision entry documenting normalization effort.【F:docs/global/Decision_Docket.md†L9-L16】
  - `docs/agents/session-notes/SN_20251002-1800_ticket-draft-standardization.md` – this session note.
- **Key Deliverables**:
  - Reviewer-ready drafts with checklists aligning to Background Agent workflow.
  - Updated backlog entries to track validator + documentation follow-ups.
  - Decision Docket entry for traceability.
- **Documented Decisions**:
  - See new Decision Docket entry `2025-10-02 (M)` (link above).

---

## Citations

- `docs/templates/linear/ticket-template.md`
- `docs/global/GBL-TKT_Best_Practices.md`
- `docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md`
- Updated draft files and backlog entries listed in Outputs.

---

## Risks & Issues Identified

- **Potential Issues**:
  - Validator has not yet been run post-edit; Option 3 TODO item tracks follow-up.
  - Vendor pricing placeholders remain unvalidated; requires finance/legal review.
  - RSM documentation still needs publication to SLF-73 after human review.
- **Mitigation Strategies**:
  - Assign follow-up tasks via Option 3 entries (IDs 408–410) to ensure owners validate.
  - Highlight vendor review in backlog; escalate to finance/legal leads.
  - Plan next session to push SLF-73 updates once reviewer feedback arrives.

---

## Reasoning & Rationale

- Full normalization chosen over partial edits to respect Background Agent workflow requirements and reduce future validator churn.
- Added reviewer checklists to each draft to mirror workflow review gates and provide quick QA guidance.
- Option 3 backlog ensures CodeLens and sync scripts remain effective; appended script follow-up to encourage post-commit sync.

---

## Next Actions

- **Immediate Follow-ups**:
  - [ ] Run `/ticket-validate` against updated drafts once reviewer approves (TODO-20251002-408).
  - [ ] Publish RSM notes to SLF-73 and confirm cross-links (TODO-20251002-409).
- **For Next Session**:
  - [ ] Review finance/legal feedback on vendor list and update pricing tables (TODO-20251002-410).
  - [ ] Evaluate automation opportunities documented in TODO-20251002-406.
- **Pending Approvals/Decisions**:
  - [ ] Owner review of normalized drafts + TODO backlog changes.
  - [ ] Confirmation before running `scripts/todos/sync_codelens.py` (TODO-20251002-411).

---

## Signoff

- **Reviewer**: _TBD_
- **Status**: pending
- **Date**: _TBD_
- **Notes**: _Awaiting reviewer confirmation._

---
