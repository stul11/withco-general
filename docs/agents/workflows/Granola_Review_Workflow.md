# Granola Review Workflow (Paste-based, No API)

This workflow converts pasted Granola outputs into structured artifacts while staying within safety rules.

## Trigger

- Run the chat command: `/granola-review granola_link --write draft`
- Paste one or two blocks in the chat (auto-detected):
  - If only Actions_Template is pasted, proceed with actions/decisions/changes/risks.
  - If both Actions_Template and Auto-generated summary are pasted, also draft the executive summary.

## Normalization Rules

- Dates: ISO 8601 (YYYY-MM-DD) for due dates; `created`/`updated` timestamps with Z
- Priorities: P0–P3 only; others flagged for manual correction
- Owners: keep names as provided; add emails only if explicitly included
- Source: include transcript link and minimal quote; add timestamps if available
- Meeting slug: `YYYY-MM-DD-kebab-title`

## Outputs

- Session NOTE: `docs/agents/session-notes/SN_ISO_MEETINGSLUG.md`
- Decision Docket append: `docs/global/Decision_Docket.md`
- TODO Log append: `docs/global/TODO_Log.md`
- Ticket drafts: `linear/tickets/drafts/DATE_MEETINGSLUG.md`

## Modes

- `--write off`: preview-only in chat
- `--write draft`: write markdown files to the repo; no Linear writes
- `--write global-TODO`: after explicit approval, also create Global To‑Do issues (allowed)

## Review Checklist

- Due dates are ISO 8601; priorities within P0–P3
- Decisions include rationale and alternatives
- Ticket drafts include clear acceptance criteria (Given/When/Then)
- Risks list severity, likelihood, and next steps
- Sources and transcript URL are captured

## Safety

- Writes restricted to:
  - `docs/agents/session-notes/`
  - `docs/global/Decision_Docket.md`
  - `docs/global/TODO_Log.md`
  - `linear/tickets/drafts/`
- Company Linear projects are read-only; Notion updates are suggestions
- Keep an audit trail in the session NOTE (who triggered, when, write mode)
