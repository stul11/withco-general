---
type: session-NOTE
team: global
created: 2025-10-02T15:00:00Z
updated: 2025-10-02T15:00:00Z
status: completed
title: Low-Hanging Cleanup TODO Audit
tags: [todo-log, cleanup]
---

# Session NOTE

- **Task ID**: low-hanging-cleanup-audit
- **Agent**: gpt-5-codex
- **Owner**: slittle
- **Date**: 2025-10-02T15:00:00Z
- **Duration**: ~45 minutes

---

## Purpose & Scope

Catalog outstanding, low-effort cleanup tasks across the repository with an emphasis on
session note consistency and deprecated documentation copies that could drift.

---

## Inputs & Context

- Global TODO backlog and CodeLens sidecar (`docs/global/TODO_Log.md`, `docs/global/TODO.codelens.todo`)
- Session NOTE directories under `docs/agents/session-notes/`
- Linear template copies (`linear/docs/templates/ticket-template.md`, `docs/templates/linear/ticket-template.md`)
- Repository-wide rules from `.cursor/rules/`

---

## Findings & Decisions

- Found duplicate `reorganization-phase-1-2` NOTES (10:45 & 10:52) plus an empty 10:50 stub; decided to
  consolidate into one canonical NOTE and track cleanup via TODO-20251002-210.
- Identified multiple Phase 02 NOTES (`phase-02-sample-items`, `phase-02-command-docs-check`) missing
  required front matter; logged TODO-20251002-211 and TODO-20251002-212 to align them with the template.
- Observed `SN_20251002-0745_markdownlint-implementation.md` and
  `SN_20251002-1135_phase-03-validation.md` bypass the standard NOTE structure; captured
  TODO-20251002-213 and TODO-20251002-214 to reformat or relocate the raw outputs.
- Noted the deprecated Linear ticket template copy still mirrors full content with formatting drift;
  recorded TODO-20251002-215 to reduce it to a safe pointer or automated sync.

---

## Outputs

- Added TODO-20251002-210 through TODO-20251002-215 under "General Backlog > Open Work" in
  `docs/global/TODO_Log.md` and regenerated the CodeLens sidecar.
- Documented findings in this session NOTE to satisfy global documentation requirements.

---

## Next Steps

- Prioritize the new backlog items with the maintainer.
- When executing the cleanup, ensure session NOTE template compliance and update or retire the
  deprecated template copy per TODO guidance.
