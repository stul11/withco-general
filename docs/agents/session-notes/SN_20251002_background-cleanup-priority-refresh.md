---
id: SN_20251002_background-cleanup-priority-refresh
title: Session Note - background-cleanup-priority-refresh
version: 1.0.0
created: 2025-10-02T04:05:19Z
updated: 2025-10-02T04:05:19Z
owner: slittle
status: Draft
tags: [session-note, audit, cleanup]
---

# Session NOTE

- **Task ID**: background-cleanup-priority-refresh
- **Agent**: gpt-5-codex
- **Owner**: slittle
- **Date**: 2025-10-02T04:05:19Z
- **Duration**: ~1.0h

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - `docs/global/TODO_Log.md`
  - `docs/Deal_Structure_Model_Spec.md`
  - `docs/global/GLOSSARY.md`
  - `docs/global/glossary/APPROVED-GLOSSARY.md`
  - `docs/global/glossary/INFORMAL-GLOSSARY.md`
  - `linear/tickets/archive/LEG-TKT_Collect_Cost_of_Manufacturing_an_Offering_Inputs.md`
- **Context & Requirements**:
  - Audit repository for lingering cleanup items, conflicts, and stranded TODO markers.
  - Do not implement fixes; instead, surface prioritized follow-up tasks and update global trackers.
- **Relevant Prior Work**:
  - Previous cleanup sessions logged in `docs/global/TODO_Log.md` and supporting session notes for 2025-01-27 and 2025-10-01.

---

## Full Findings

- **Summary of Findings**:
  - The TODO Log still lists high-priority cleanup items as open even though corresponding work is marked complete, creating conflicting status signals.
  - The deal-structure modeling spec retains numerous `TBD` placeholders for fee defaults and Linear hierarchy metadata that are not represented in the TODO Log.
  - Glossary documentation is duplicated across three files with the same definitions, leaving unclear which source is authoritative.
  - An archived ticket references the deprecated `GLB-TKT_Best_Practices.md` path, reintroducing the resolved naming inconsistency.

- **Detailed Findings**:
  1. **TODO Log Conflicts**
     - **Description**: `Repository Cleanup (High Priority)` includes unchecked items (e.g., duplicate template resolution, stranded TODO cleanup) even though the `Completed` section already marks the same tasks done.
     - **File(s) Involved**: `docs/global/TODO_Log.md`
     - **Line Numbers/Sections**: Completed section (`L36-L45`) vs. open `Repository Cleanup` entries (`L130-L140`).
     - **Reasoning**: Conflicting status entries obscure the current backlog and mislead future sessions about remaining work.
  2. **Untracked Deal-Structure Placeholders**
     - **Description**: The modeling spec still contains `TBD` values for key fee defaults, hierarchy metadata, and policy decisions.
     - **File(s) Involved**: `docs/Deal_Structure_Model_Spec.md`
     - **Line Numbers/Sections**: Linear hierarchy metadata and fee table (`L15-L66`).
     - **Reasoning**: These placeholders represent substantive modeling decisions that should be tracked or resolved before implementation.
  3. **Glossary Duplication**
     - **Description**: `docs/global/GLOSSARY.md`, `docs/global/glossary/APPROVED-GLOSSARY.md`, and `docs/global/glossary/INFORMAL-GLOSSARY.md` all contain identical definitions while the Approved/Informal files remain in "Draft" status.
     - **File(s) Involved**: `docs/global/GLOSSARY.md`; `docs/global/glossary/APPROVED-GLOSSARY.md`; `docs/global/glossary/INFORMAL-GLOSSARY.md`
     - **Line Numbers/Sections**: `docs/global/GLOSSARY.md` (`L1-L8`); Approved glossary (`L33-L77`); Informal glossary (`L33-L55`).
     - **Reasoning**: Duplicate sources create uncertainty about canonical terminology and undermine the Approved vs Informal separation.
  4. **Residual GLB Reference**
     - **Description**: Archived LEG ticket still references `withco-general/docs/global/GLB-TKT_Best_Practices.md` instead of the corrected `GBL` prefix.
     - **File(s) Involved**: `linear/tickets/archive/LEG-TKT_Collect_Cost_of_Manufacturing_an_Offering_Inputs.md`
     - **Line Numbers/Sections**: Related docs list (`L38-L44`).
     - **Reasoning**: Reintroduces previously resolved naming inconsistency and can mislead future cleanup efforts.

---

## Steps Taken

- **Major Actions**:
  - Reviewed the entirety of `docs/global/TODO_Log.md` for conflicting or stale entries.
  - Ran `rg "TODO|FIXME|TBD|XXX|\\?\\?\\?" -n` across the repository to surface stranded markers.
  - Inspected modeling, glossary, and archived ticket documents to trace unresolved placeholders and outdated references.
- **Key Decisions**:
  - No new decisions; surfaced follow-up recommendations only.
- **Tools/Methods Used**:
  - `rg` for marker inventory.
  - Manual markdown inspection with `sed`, `nl`, and `cat` to verify contexts.

---

## Outputs

- **Files Created/Modified**:
  - `docs/agents/session-notes/SN_20251002_background-cleanup-priority-refresh.md` (this session NOTE).
  - `docs/global/TODO_Log.md` (appended prioritized follow-up section and refreshed metadata).
- **Key Deliverables**:
  - New high-to-low priority action list capturing unresolved cleanup tasks.
- **Documented Decisions**:
  - None added to the Decision Docket during this session.

---

## Citations

- `docs/global/TODO_Log.md` (`L36-L47`, `L130-L140`, `L174-L179`).
- `docs/Deal_Structure_Model_Spec.md` (`L15-L66`).
- `docs/global/GLOSSARY.md` (`L1-L8`).
- `docs/global/glossary/APPROVED-GLOSSARY.md` (`L33-L77`).
- `docs/global/glossary/INFORMAL-GLOSSARY.md` (`L33-L55`).
- `linear/tickets/archive/LEG-TKT_Collect_Cost_of_Manufacturing_an_Offering_Inputs.md` (`L38-L44`).

---

## Risks & Issues Identified

- **Potential Issues**:
  - Backlog confusion persists until the TODO Log is reconciled.
  - Modeling spec may stall without explicit ownership of remaining `TBD` decisions.
- **Mitigation Strategies**:
  - Prioritize a TODO Log reconciliation pass before implementing further cleanup.
  - Assign modeling placeholders to specific follow-up tasks or owners in the refreshed TODO list.

---

## Reasoning & Rationale

- Documented each finding with precise file references to enable quick cleanup without re-running the full audit.
- Focused on high-impact documentation conflicts (TODO Log, modeling spec, glossary) before minor issues, aligning with repository cleanup objectives.

---

## Next Actions

- **Immediate Follow-ups**:
  - Reconcile duplicate entries in `docs/global/TODO_Log.md` and remove or close resolved items.
  - Update the archived LEG ticket reference to use `GBL-TKT_Best_Practices.md`.
- **For Next Session**:
  - Convert modeling spec `TBD` placeholders into concrete tasks/values.
  - Decide on glossary consolidation strategy (single source vs maintained tiers).
- **Pending Approvals/Decisions**:
  - None identified; awaiting owner prioritization of follow-up tasks.

---

## Signoff

- **Reviewer**: pending
- **Status**: pending
- **Date**: 2025-10-02T04:05:19Z
- **Notes**: Awaiting review.
