##

id: SN_20251002-2100_todo-log-normalization
title: TODO Log Normalization
version: 1.0.0
created: 2025-10-02T21:00:00Z
updated: 2025-10-02T21:15:00Z
owner: slittle
status: In Progress
tags: [background-agent, backlog]

---

# Session NOTE

- **Task ID**: Normalize TODO_Log backlog to Option 3 standard
- **Agent**: background
- **Owner**: slittle
- **Date**: 2025-10-02T21:00:00Z
- **Duration**: 30m (est)

---

## Inputs & Context

- **Key Documents/Files Provided**:
  - docs/global/TODO_Log.md
  - README.md
  - docs/global/GBL-TKT_Best_Practices.md
  - docs/templates/linear/ticket-template.md
  - docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
  - docs/raw/plans/2025-10-02_document-categorization-and-workflows.md
  - .cursor/rules/background-agent-safety.mdc
  - scripts/README.md
- **Context & Requirements**:
  - Normalize backlog entries to Option 3 format with stable IDs, tags, and priorities.
  - Parse existing TODO log and any team TODO sources; deduplicate overlaps.
  - Update TODO_Log.md and capture rationale plus changelog here.
  - Offer CodeLens sync recommendation when touching TODOs.
- **Relevant Prior Work**:
  - TODO_Log.md current backlog entries dated 2025-10-02 sessions.
  - Recent markdownlint and workflow session notes referenced in backlog items.

---

## Plan

1. Review docs/global/TODO_Log.md and identify sections requiring Option 3 normalization.
2. Search for additional team TODO sidecars or logs to ensure coverage and note overlaps.
3. Draft updated backlog entries with stable IDs, tags, and priority notes; dedupe or merge where needed.
4. Update TODO_Log.md, documenting rationale and priority scoring summaries.
5. Summarize changes, remaining questions, and next actions in this session note; suggest CodeLens sync.

---

## Steps Taken

- Reviewed existing backlog sections in `docs/global/TODO_Log.md` and cataloged entries lacking Option 3 formatting or IDs.
- Surveyed related session notes, plans, and draft tickets to capture authoritative sources and context for each open item.
- Normalized backlog entries across "In Progress", "Pending", "General Backlog", proposal groupings, and historical session follow-ups with stable IDs, tags, and ICE-lite notes.
- Added new Option 3 entries for markdownlint roadmap phases, cleanup follow-ups, and granola workflow validation, de-duplicating overlaps where proposals were already delivered.
- Highlighted where completed work superseded proposals (e.g., `docs/README.md`) and downgraded automation experiments pending adoption data.

---

## Outputs

- `docs/global/TODO_Log.md` — Normalized all open backlog entries to Option 3 format with IDs, tags, and ICE-lite scoring; updated priorities and dedupe notes across sections.
- `docs/agents/session-notes/SN_20251002-2100_todo-log-normalization.md` — Captured plan, execution summary, and follow-up recommendations.

---

## Changelog

- 2025-10-02T21:15:00Z — Converted backlog items to Option 3 format, added ICE-lite notes, and refreshed priorities/proposals dedupe context.

---

## Next Actions

- [ ] Run `python scripts/todos/sync_codelens.py` after review to refresh sidecars (recommendation).
- [ ] Await owner approval on prioritized backlog ordering.

---

## Signoff

- **Reviewer**: Pending
- **Status**: pending
- **Date**: TBD
- **Notes**: N/A
