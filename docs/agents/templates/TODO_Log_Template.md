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

> CodeLens integration: Each actionable checklist item should include a stable `id` so that sidecar files can
> mirror items deterministically. Append an HTML comment with a unique identifier at the end of the line, e.g.
> `<!-- id: todo-YYYYMMDD-### -->`. A generator will emit `*.codelens.todo` sidecars for editor CodeLens.

## Completed

- [x] [Completed task description] <!-- id: todo-YYYYMMDD-001 -->
- [x] [Another completed task] <!-- id: todo-YYYYMMDD-002 -->

## In Progress

- [ ] [Currently active task] <!-- id: todo-YYYYMMDD-003 -->
- [ ] [Another in-progress task] <!-- id: todo-YYYYMMDD-004 -->

## Pending

- [ ] [Future task 1] <!-- id: todo-YYYYMMDD-005 -->
- [ ] [Future task 2] <!-- id: todo-YYYYMMDD-006 -->
- [ ] [Future task 3] <!-- id: todo-YYYYMMDD-007 -->

## Blocked

- [ ] [Task blocked by dependency] <!-- id: todo-YYYYMMDD-008 -->
- [ ] [Task waiting for approval] <!-- id: todo-YYYYMMDD-009 -->

## Notes

- [Any important context or decisions about the TODO items]
- [Priority changes or updates]

## Session History

- **YYYY-MM-DD**: [Session name] - [Brief summary of what was accomplished]
- **YYYY-MM-DD**: [Previous session] - [Brief summary]
