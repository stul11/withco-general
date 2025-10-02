<!-- markdownlint-disable MD003 MD022 -->
<!-- markdownlint-disable MD041 -->

## <!-- markdownlint-disable MD025 -->

id: TODO_Template
title: TODO Log Template
version: 1.0.0
created: 2025-01-27T19:00:00Z
updated: 2025-01-27T19:00:00Z
owner: slittle
status: Active
tags: [template, TODO-log, tracking]

---

# TODO Log

- **Last Updated**: YYYY-MM-DDTHH:MM:SSZ
- **Session**: [Current session identifier]
- **Owner**: [Human owner]

> CodeLens integration: Actionable items must start with `TODO:` and include a stable `id` so sidecar files can mirror
> items deterministically. Append an HTML comment with a unique identifier at the end of the line, e.g.
> `<!-- id: TODO-YYYYMMDD-### -->`. A generator will emit `*.codelens.todo` sidecars for editor CodeLens.

## Completed

- [x] [Completed task description] <!-- id: TODO-YYYYMMDD-001 -->
- [x] [Another completed task] <!-- id: TODO-YYYYMMDD-002 -->

## In Progress

- TODO: (AGENT) [MED] Currently active task <!-- id: TODO-YYYYMMDD-003 -->
  source: docs/agents/session-notes/SN_YYYYMMDD-HHMM_slug.md#section
  tags: session-notes
  notes: Keep the first line concise; add context here if needed

- TODO: (DECISION) [HIGH] Another in-progress task <!-- id: TODO-YYYYMMDD-004 -->
  source: docs/global/Decision_Docket.md#anchor
  tags: decisions

## Pending

- TODO: (AGENT) [LOW] Future task 1 <!-- id: TODO-YYYYMMDD-005 -->
  source: docs/raw/plans/YYYY-MM-DD_topic.md#recommendation
  tags: planning

- TODO: [MED] Future task 2 <!-- id: TODO-YYYYMMDD-006 -->
  source: docs/global/TODO_Log.md#open-work
  tags: backlog

- TODO: [LOW] Future task 3 <!-- id: TODO-YYYYMMDD-007 -->
  source: docs/global/README.md#key-documents
  tags: backlog

## Blocked

- [ ] [Task blocked by dependency] <!-- id: TODO-YYYYMMDD-008 -->
- [ ] [Task waiting for approval] <!-- id: TODO-YYYYMMDD-009 -->

## Notes

- [Any important context or decisions about the TODO items]
- [Priority changes or updates]

## Session History

- **YYYY-MM-DD**: [Session name] - [Brief summary of what was accomplished]
- **YYYY-MM-DD**: [Previous session] - [Brief summary]
