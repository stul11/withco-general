# /prep-session

Kick off a working session by gathering repository context, outstanding work items, and recent history.

## Usage

```
/prep-session [--dry-run] [--limit <n>] [--since <iso-datetime>]
```

- `--dry-run`: Print the plan without modifying files or staging.
- `--limit`: Limit surfaced TODO and NOTE entries (default 5).
- `--since`: ISO 8601 timestamp filter for recent Session NOTES (defaults to 7 days).

## When to use

- Beginning of any focused session.
- Picking up a handoff or resuming background work.
- Before triaging backlog to ensure you have current context.

## Behavior

1. Report current git branch and divergence (`git status -sb`).
2. List unstaged changes grouped by directory.
3. Surface the top backlog items from `docs/global/TODO_Log.md` matching priority cues (H/M/L).
4. Summarize the newest Session NOTES from `docs/agents/session-notes/` since `--since`.
5. Highlight any open `/offboard` follow-ups documented in recent NOTES.
6. Suggest next actions (e.g., run `/status-sweep`, update specific TODOs, open relevant files).

## Output

- Human-readable summary plus `json` block containing key arrays (`todos`, `notes`, `changes`).
- Direct file path links for quick navigation inside Cursor.
- Reminder checklist for prerequisites (pending TODO updates, missing NOTE sections).

## Safety

- Read-only command; never edits or stages files.
- Prompts user when repository has untracked files outside writable roots.

## Related

- `.cursor/rules/cursor-workflow-enhancements.mdc`
- `.cursor/commands/status-sweep.md`
- `.cursor/commands/onboard-next-agent.md`
