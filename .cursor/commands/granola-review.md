---
title: /granola-review
description: Paste-based Granola meeting ingestion (no API). Normalizes action items, decisions, PRD/ticket changes, and drafts artifacts.
---

Usage:

- /granola-review <granola_link> --write draft

Arguments:

- granola_link: Granola note link for reference only
- --write: off | draft | global-todo
  - off: preview-only messages in chat
  - draft: write markdown files, no Linear writes
  - global-todo: after approval, create issues in Global To-Do project (allowed)

Workflow:

1. User pastes one or two blocks in chat (auto-detected):
   - If only Actions_Template is pasted, agent proceeds with actions/decisions/changes/risks.
   - If both Actions_Template and Auto-generated summary are pasted, agent also drafts the executive summary.
2. Agent normalizes with ISO dates and preserves source quotes + URL.
3. Agent presents a preview bundle; on approval and allowed write mode, it writes:
   - docs/agents/session-notes/SN_ISO_MEETINGSLUG.md
   - docs/global/Decision_Docket.md (append)
   - docs/global/TODO_Log.md (append)
   - linear/tickets/drafts/DATE_MEETINGSLUG.md
4. Company Linear remains read-only; Notion updates are suggestions only.

Safety:

- Enforce Background Agent Safety Rules; only Global To-Do writes are permitted.
- Use ISO 8601 for created/updated and due dates.
- Store transcript link and minimal quotes for traceability.

Prompts to run (copy/paste into Granola chat when needed):

- Action Items: extract table with title, owner, due_date (YYYY-MM-DD), priority (P0–P3), confidence, dependencies, source quote.
- Decisions: list decisions with rationale, alternatives, owners, date, and source quotes.
- PRD Changes: for each target doc/section, provide current text summary and proposed replacement text with rationale.
- Ticket Changes: provide title, description, acceptance criteria (GWT), dependencies, priority.

Review Checklist:

- Are due dates ISO 8601? Are priorities within P0–P3?
- Do decisions include rationale and alternatives?
- Do ticket drafts include clear acceptance criteria?
- Are sources and transcript URL captured?
