# Session Note

- **Task ID**: ticket-workflows-v1
- **Agent**: Background Agent (Cursor)
- **Owner**: slittle
- **Date**: 2025-10-01T00:00:00Z
- **Duration**: —

## Inputs

- docs/agents/workflows/Ticket_Workflow_README.md
- docs/agents/workflows/Ticket_Validator_Spec.md
- docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
- .cursor/commands/ticket.md
- .cursor/commands/ticket-new.md
- .cursor/commands/ticket-wizard.md
- .cursor/commands/ticket-simplify.md
- .cursor/commands/ticket-promote.md
- .cursor/commands/ticket-validate.md
- .cursor/commands/ticket-draft.md
- .cursor/commands/ticket-review.md
- .cursor/commands/ticket-approve.md
- .cursor/commands/ticket-implement.md
- .cursor/commands/ticket-archive.md
- .cursor/rules/ticket-wizard.mdc
- linear/tickets/README.md

## Steps Taken

- Created Ticket Workflow README with sequence/state mermaid diagrams and rules
- Added per-command docs for the `/ticket-*` suite (minimal arguments)
- Updated wizard and background workflow docs with Promote & Validate gate
- Added Ticket Validator Spec for template/timestamp checks
- Linked workflow README from the tickets README
- Resolved markdown lint warnings across new/updated docs

## Outputs

- Created: docs/agents/workflows/Ticket_Workflow_README.md
- Created: docs/agents/workflows/Ticket_Validator_Spec.md
- Updated: docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
- Updated: .cursor/rules/ticket-wizard.mdc
- Updated: linear/tickets/README.md
- Created: per-command docs under .cursor/commands/

## Citations

- docs/agents/workflows/Ticket_Workflow_README.md
- docs/agents/workflows/Ticket_Validator_Spec.md
- .cursor/commands/ticket.md

## Risks Identified

- Command behavior not yet automated; docs-first approach requires discipline
- Potential drift between best-practices draft and minimal template if Promote step skipped

## Next Actions

- Dry-run the flow on a small test draft using `/ticket-wizard` → `/ticket-promote` → `/ticket-validate` → `/ticket-draft`
- Add lightweight helpers for template normalization and timestamp autofix
- Consider shortcuts/aliases (`/t ...`) in the agent command parser

## Signoff

- **Reviewer**: —
- **Status**: pending
- **Date**: 2025-10-01T00:00:00Z
- **Notes**: —
