# Session Note

- **Task ID**: granola-review-workflow-initial-implementation
- **Agent**: Background Agent (Cursor)
- **Owner**: slittle
- **Date**: 2025-10-02T00:00:00Z
- **Duration**: —

## Inputs

- `.cursor/commands/granola-review.md`
- `.cursor/rules/granola-review.mdc`
- `docs/agents/workflows/Granola_Review_Workflow.md`
- `docs/agents/templates/Granola_Paste_Template.md`
- `docs/global/Decision_Docket.md`
- `docs/global/TODO_Log.md`

## Steps Taken

- Created a docs-first command for paste-based Granola ingestion; removed the `--scope` flag.
- Added normalization/safety rules and auto-detection of one vs two pasted blocks.
- Authored workflow runbook and a paste template for consistent inputs.
- Ensured markdown lint passes on new/updated docs.

## Outputs

- Created: `.cursor/commands/granola-review.md`
- Created: `.cursor/rules/granola-review.mdc`
- Created: `docs/agents/workflows/Granola_Review_Workflow.md`
- Created: `docs/agents/templates/Granola_Paste_Template.md`
- Updated: `docs/global/Decision_Docket.md` (new decision appended)
- Updated: `docs/global/TODO_Log.md` (new dated session entry)

## Citations

- `.cursor/commands/granola-review.md`
- `.cursor/rules/granola-review.mdc`
- `docs/agents/workflows/Granola_Review_Workflow.md`
- `docs/agents/templates/Granola_Paste_Template.md`

## Risks & Issues Identified

- None blocking. Future enhancements may include owner normalization and duplicate detection.

## Next Actions

- Dry-run the flow on the provided sample using `/granola-review <link> --write draft`.
- Optionally enable `--write global-todo` after confirming Global To‑Do issue fields.
- Consider de-duplication across TODO entries by title+owner+due hash.

## Signoff

- **Reviewer**: —
- **Status**: pending
- **Date**: 2025-10-02T00:00:00Z
- **Notes**: —
