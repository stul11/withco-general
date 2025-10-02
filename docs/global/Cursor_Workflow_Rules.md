# Cursor Workflow Guardrails & Helpers

## Overview

Cursor rules and slash-commands keep background agents aligned with documented workflows. The recommendations below group the guardrails that should stay active, propose small additions that cover recurring gaps, and collect the high-leverage commands agents should keep handy while working in this repo.

## Recommended Rule Set

### Active guardrails (already available)

| Rule file | Purpose | Scope |
| --- | --- | --- |
| `.cursor/rules/agent-session-notes.mdc` | Require a session note whenever PRDs, agent docs, or global standards are edited so changes stay auditable. | `docs/prds/**`, `docs/agents/**`, `docs/global/**` |
| `.cursor/rules/todo-cursor.mdc` | Force use of the TODO sidecar tooling so Markdown logs and CodeLens stay synchronized. | `docs/global/TODO_Log.md`, `docs/global/TODO.codelens.todo` |
| `.cursor/rules/planning-mode.mdc` & `.cursor/rules/planning-mode-md.mdc` | Keep agents in planning mode when work is uncertain and route discovery docs into `docs/raw/plans/`. | Repository-wide |
| `.cursor/rules/uv-guidelines.mdc` | Guard Python dependency work so agents default to `uv` and avoid `pip`/`poetry`. | `scripts/**`, Python tooling |
| `.cursor/rules/markdown-best-practices.mdc` & `.cursor/rules/datetime-format.mdc` | Enforce formatting and timestamp standards in shared docs. | Markdown docs with front matter |

### Proposed lightweight additions

| Proposed rule | Description | Trigger | Payoff |
| --- | --- | --- | --- |
| `.cursor/rules/workspace-orientation.mdc` | Prompt agents to review `docs/global/README.md` and the current TODO sidecar before editing global standards. | `docs/global/**` (excluding generated files) | Smooth hand-offs and reduces context loss. |
| `.cursor/rules/ticket-draft-safety.mdc` | Remind agents drafting ticket content to attach Decision Docket links and validate checklists prior to promotion. | `linear/tickets/drafts/**` | Prevents orphaned tickets and captures approvals early. |
| `.cursor/rules/session-note-quality.mdc` | Build on `agent-session-notes` by checking for required sections (summary, decisions, follow-ups) in new session notes. | `docs/agents/session-notes/**` | Raises the quality floor of session documentation. |

## Helpful Commands

### Existing commands to keep pinned in Cursor

| Command | When to use | Key behavior |
| --- | --- | --- |
| `/sync-help` | Before wrapping a session or when branch drift is uncertain. | Runs the audited sync script that reviews changes, pulls, commits, and pushes safely. |
| `/todo-add` | When capturing follow-up work during or after a session. | Writes canonical TODO entries and regenerates the CodeLens sidecar. |
| `/toplan-add` | While planning exploratory work that needs a raw plan stub. | Generates a dated plan shell under `docs/raw/plans/` and links it in the log. |
| `/ticket-wizard` | To scaffold a five-phase ticket draft aligned with the new ticket workflow. | Produces the ticket skeleton plus checklist reminders. |
| `/sync-help-impl` | When investigating how `/sync-help` runs or debugging issues. | Opens implementation notes so agents can review guardrails quickly. |

### Proposed quick helpers

| Proposed command | Sketch | Expected impact |
| --- | --- | --- |
| `/todo-sidecar-open` | Open `docs/global/TODO.codelens.todo` in a split pane and focus the matching Markdown log. | Cuts friction when triaging TODOs and keeps CodeLens visible. |
| `/session-note-bootstrap` | Prompt for session metadata then create a pre-filled note in `docs/agents/session-notes/` with required sections. | Prevents blank or inconsistent notes and accelerates compliance with rules. |
| `/cursor-rules-refresh` | List all rules matching the current file and print the short description before edits begin. | Reinforces guardrails without manual directory browsing. |

## Adoption Checklist

1. Enable the proposed rules inside `.cursor/rules/` and verify they do not conflict with existing automation.
2. Implement or script the proposed commands (shell snippets or Cursor JSON) and publish them under `.cursor/commands/` with documentation.
3. Update `docs/global/AGENTS.md` after syncing rules so agents see the new guidance inside Cursor.
4. Announce the changes in the Decision Docket and include a quick screencast or walkthrough during the next background-agent session.
