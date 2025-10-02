---
type: session-NOTE
team: global
created: 2025-10-02T12:45:00Z
updated: 2025-10-02T12:45:00Z
status: completed
title: TODO List Changes v2
---

## Session NOTE

- **Task ID**: todo-list-changes-v2
- **Agent**: GPT-5 (Cursor)
- **Owner**: slittle
- **Date**: 2025-10-02T12:45:00Z
- **Duration**: ~30 minutes

## Inputs & Context

- docs/raw/plans/2025-10-02_todo-codelens-integration.md
- docs/raw/plans/2025-10-02_document-categorization-and-workflows.md
- .cursor/commands/todo-add.md
- .cursor/rules/todo-cursor.mdc
- docs/agents/templates/TODO_Log_Template.md

## Full Findings

- Adopted Option 3 (list item with leading `TODO:`) as canonical across logs.
- Template, command, and rule updated to enforce triggers and stable IDs.
- Added guarded converter and piloted changes in global log; seeded team logs.

## Steps Taken

- Updated template to `- TODO:` with multi-line metadata and stable IDs
- Revised `/TODO-add` doc to emit Option 3 schema
- Amended rule to require `TODO:` trigger + ID; added lint guards
- Added `scripts/todos/convert_todo_format.py`
- Converted a block in `docs/global/TODO_Log.md`; seeded `linear/{TEAM}/TODO.md`
- Updated README files and rollout phase docs

## Outputs

- Modified: docs/agents/templates/TODO_Log_Template.md
- Modified: .cursor/commands/todo-add.md
- Modified: .cursor/rules/todo-cursor.mdc
- Added: scripts/todos/convert_todo_format.py
- Modified: docs/global/TODO_Log.md
- Modified: linear/{global,PROD,ANA,DATA,LEG,AM}/TODO.md
- Modified: README.md, docs/global/README.md
- Modified: docs/raw/plans/rollout/phase-02_rules-and-commands.md

## Citations

- docs/agents/templates/TODO_Log_Template.md
- .cursor/commands/todo-add.md
- .cursor/rules/todo-cursor.mdc
- scripts/todos/convert_todo_format.py
- docs/global/TODO_Log.md
- linear/\*/TODO.md
- README.md; docs/global/README.md
- docs/raw/plans/rollout/phase-02_rules-and-commands.md

## Risks & Issues Identified

- Contributors must open sidecars for CodeLens; provide brief guidance in READMEs
- Ensure sidecar sync is run after edits (pre-commit/CI check recommended)

## Reasoning & Rationale

- Option 3 maximizes CodeLens reliability without losing Markdown metadata

## Next Actions

- Verify sidecar sync after next generator run
- Expand conversion via the script if additional sections need migration

## Signoff

- **Reviewer**: slittle
- **Status**: approved
- **Date**: 2025-10-02T12:45:00Z
