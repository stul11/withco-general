---
id: SN_20251002_repo_background_cleanup
title: Session Note — Repo Background Cleanup Audit
version: 1.0.0
created: 2025-10-02T00:00:00Z
updated: 2025-10-02T00:00:00Z
owner: slittle
status: Draft
tags: [session-note, audit, cleanup]
---

# Session NOTE

- **Task ID**: repo-background-cleanup
- **Agent**: background-analysis
- **Owner**: slittle
- **Date**: 2025-10-02T00:00:00Z
- **Duration**: 2h (approx)

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - docs/global/TODO_Log.md
  - docs/global/Decision_Docket.md
  - docs/global/glossary/APPROVED-GLOSSARY.md
  - docs/global/glossary/INFORMAL-GLOSSARY.md
  - docs/raw/cost-of-manufacturing-offering-context.md
  - docs/raw/economics-cost-structure-initial-context.md
  - linear/docs/How_to_use_Linear.md
  - linear/tickets/drafts/excel-cost-analysis-funnel-integration.md
  - docs/agents/session-notes/SN_20251001_agent-offboarding_handoff.md
- **Context & Requirements**:
  - Perform full repo sweep for uncertainties, duplicated docs, stranded TODOs, and outdated backlog entries per background-clean-up-template.
  - Produce prioritized cleanup actions to append to TODO_Log.
  - Maintain session documentation and prep for offboarding per agent rules.
- **Relevant Prior Work**:
  - SN_20250127_repo-cleanup-analysis.md (baseline cleanup inventory)
  - SN_20251001_agent-offboarding_handoff.md (open follow-ups from previous session)
  - Existing TODO_Log backlog sections spanning repository cleanup tasks.

---

## Full Findings

- **Summary of Findings**:
  - Located high-priority backlog items that remain open in TODO_Log even though upstream work is complete, causing conflicting guidance.
  - Identified duplicate glossary content between informal and approved glossaries with identical definitions, obscuring canonical source of truth.
  - Documented stranded checklists in cost-of-manufacturing context and Excel integration draft that are not referenced in TODO_Log.
  - Flagged outstanding operational tasks from agent-offboarding handoff and unresolved company documentation TODO in Linear usage guide.
  - Noted key modeling spec with TBD placeholders requiring structured follow-up to avoid drift.
- **Detailed Findings**:
  - **Duplicate backlog entries in TODO_Log**:
    - **Description**: Repository cleanup section still lists undone tasks (naming inconsistencies, duplicate templates, empty files, stranded TODOs) despite earlier sessions marking them resolved, creating conflicting guidance for next agents.
    - **File(s) Involved**: docs/global/TODO_Log.md
    - **Line Numbers/Sections**: L128-L143
    - **Reasoning**: Maintaining contradictory status indicators causes repeated audits and uncertainty about true state.
    - **Supporting Evidence**: Completed session summaries immediately below confirm resolution, but checkbox state remains unchecked.
  - **Glossary duplication**:
    - **Description**: APPPROVED-GLOSSARY and INFORMAL-GLOSSARY share identical content and front matter, preventing clarity on which file is authoritative and when terms graduate from informal to approved.
    - **File(s) Involved**: docs/global/glossary/APPROVED-GLOSSARY.md; docs/global/glossary/INFORMAL-GLOSSARY.md
    - **Line Numbers/Sections**: Approved L1-L104; Informal L1-L77
    - **Reasoning**: Without differentiation, updates may diverge and users cannot rely on review status.
  - **Stranded cost-of-manufacturing checklist**:
    - **Description**: Context document retains open checklists for deliverables and research that are not mirrored in TODO_Log.
    - **File(s) Involved**: docs/raw/cost-of-manufacturing-offering-context.md
    - **Line Numbers/Sections**: L175-L188
    - **Reasoning**: Workstream tasks risk being forgotten; need linkage to backlog or status update.
  - **Excel integration draft tasks**:
    - **Description**: Draft ticket contains full DoD checklist with all items unchecked, but TODO_Log no longer references this clean-up work.
    - **File(s) Involved**: linear/tickets/drafts/excel-cost-analysis-funnel-integration.md
    - **Line Numbers/Sections**: L74-L82
    - **Reasoning**: Without backlog item, these tasks remain invisible to planning.
  - **Outstanding offboarding handoff actions**:
    - **Description**: Handoff NOTE enumerates specific steps (run pre-commit, fix link checker findings, etc.) that remain unchecked.
    - **File(s) Involved**: docs/agents/session-notes/SN_20251001_agent-offboarding_handoff.md
    - **Line Numbers/Sections**: L23-L28
    - **Reasoning**: These tasks block compliance of offboarding process; they should surface in TODO_Log for prioritization.
  - **Company documentation TODO**:
    - **Description**: Linear usage guide retains explicit TODO (“where does ad-hoc work go?”) awaiting resolution.
    - **File(s) Involved**: linear/docs/How_to_use_Linear.md
    - **Line Numbers/Sections**: L146-L148
    - **Reasoning**: As read-only reference, unresolved TODO must be tracked externally to avoid indefinite deferral.
  - **Overlapping cost context docs**:
    - **Description**: economics-cost-structure-initial-context replicates large sections of cost-of-manufacturing work, including UPREIT vs LLC analysis and vendor cost inventory, duplicating canonical narrative.
    - **File(s) Involved**: docs/raw/economics-cost-structure-initial-context.md; docs/raw/cost-of-manufacturing-offering-context.md
    - **Line Numbers/Sections**: Economics context L1-L85; Cost context L150-L188
    - **Reasoning**: Without consolidation guidance, updates may diverge, and agents risk editing outdated context.
  - **Deal structure spec TBDs**:
    - **Description**: Deal_Structure_Model_Spec includes TBD placeholders for key fee assumptions (investor processing fee amount, property mgmt percentages, etc.).
    - **File(s) Involved**: docs/Deal_Structure_Model_Spec.md
    - **Line Numbers/Sections**: L58-L66
    - **Reasoning**: Missing data prevents downstream modeling; need action to replace TBDs with current numbers or annotate decision owner.

---

## Steps Taken

- **Major Actions**:
  - Ran ripgrep scans for TODO/TBD markers across repo.
  - Reviewed backlog, glossary, context docs, and Linear guidance for conflicting or missing status tracking.
  - Compared overlapping context documents to identify duplication risk.
  - Documented outstanding checklists in session notes and draft tickets.
- **Key Decisions**:
  - No repository changes executed; focus on analysis and backlog update per template.
- **Tools/Methods Used**:
  - `rg` for marker discovery
  - `nl`/`sed` for line-numbered inspection
  - Manual diff comparison across related docs

---

## Outputs

- **Files Created/Modified**:
  - docs/agents/session-notes/SN_20251002_repo-background-cleanup.md (this session NOTE)
  - docs/global/TODO_Log.md (pending new prioritized section)
- **Key Deliverables**:
  - Consolidated findings captured here and in TODO_Log update.
- **Documented Decisions**:
  - None added to Decision Docket (analysis only).

---

## Citations

- docs/global/TODO_Log.md:L128-L143
- docs/global/glossary/APPROVED-GLOSSARY.md:L1-L104
- docs/global/glossary/INFORMAL-GLOSSARY.md:L1-L77
- docs/raw/cost-of-manufacturing-offering-context.md:L175-L188
- linear/tickets/drafts/excel-cost-analysis-funnel-integration.md:L74-L82
- docs/agents/session-notes/SN_20251001_agent-offboarding_handoff.md:L23-L28
- linear/docs/How_to_use_Linear.md:L146-L148
- docs/raw/economics-cost-structure-initial-context.md:L1-L85
- docs/Deal_Structure_Model_Spec.md:L58-L66

---

## Risks & Issues Identified

- **Potential Issues**:
  - Conflicting backlog status may lead to redundant cleanup efforts.
  - Duplicate glossaries risk drift between “informal” and “approved” definitions.
  - Stranded checklists in key context docs lack visibility for follow-through.
- **Mitigation Strategies**:
  - Append prioritized TODO_Log section consolidating these items.
  - Recommend glossary governance action in TODO_Log update.
  - Encourage linking context deliverables to backlog via TODO_Log entry.

---

## Reasoning & Rationale

- Focused on areas with highest potential for confusion (duplicate statuses, canonical docs) to maximize future agent efficiency.
- Highlighted actionable follow-ups with estimated effort windows to align with template guidance (5–30 min tasks).

---

## Next Actions

- **Immediate Follow-ups**:
  - Update TODO_Log with prioritized cleanup list (completed in this session).
- **For Next Session**:
  - Execute backlog items once prioritized (e.g., reconcile TODO_Log, glossary consolidation, etc.).
- **Pending Approvals/Decisions**:
  - Await owner confirmation on how to resolve ad-hoc work policy and glossary governance.

---

## Signoff

- **Reviewer**: Pending
- **Status**: pending
- **Date**: 2025-10-02T00:00:00Z
- **Notes**: Review recommended during next cleanup implementation session.

