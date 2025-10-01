# /onboard-next-agent

Prepare a copy-paste onboarding brief for the next agent to start exactly where we left off.

## Usage

```
/onboard-next-agent <task-id> [--auto] [--dry-run]
```

- <task-id>: The workstream or session identifier to carry forward
- --auto: Generate the brief without additional prompts (never commits)
- --dry-run: Show what will be generated without writing files

## Behavior (what the agent will do)

1. Gather context from the latest Session Note (`docs/agents/session-notes/SN_*_<task-id>.md` or the most recent note) and current trackers (`Decision_Docket.md`, `TODO_Log.md`).
2. Produce a structured onboarding brief with:
   - TL;DR (3 bullets)
   - Required Reading (ordered list, with paths)
   - Current State (one paragraph)
   - Next Agent First Tasks (checklist of 3–7 items)
   - Open Decisions and Risks (bullets)
   - Related Files (paths)
3. Write the brief to `docs/agents/session-notes/SN_<YYYYMMDD>_<task-id>_handoff.md` and print it to chat for copy/paste.
4. Offer to append the brief’s “Next Agent First Tasks” into `docs/global/TODO_Log.md` (Pending or In Progress) without committing.

## Output format (example)

```
# Onboarding Brief: <task-id>

## TL;DR
- <one-line>
- <one-line>
- <one-line>

## Required Reading (in order)
1. docs/agents/session-notes/SN_20251001_agent-offboarding.md
2. docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
3. .cursor/rules/agent-chat-commands.mdc

## Current State
<3–6 sentences summarizing where we are and what changed last.>

## Next Agent First Tasks
- [ ] <task 1>
- [ ] <task 2>
- [ ] <task 3>

## Open Decisions and Risks
- <decision/risk>

## Related Files
- <path>
```

## Notes

- No Linear writes; read-only company docs remain unchanged.
- Never auto-commit; user reviews and commits.

## Related

- `.cursor/rules/agent-session-notes.mdc`
- `.cursor/rules/agent-offboarding.mdc`
- `.cursor/rules/agent-chat-commands.mdc`
