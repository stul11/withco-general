# /onboard-next-agent

Prepare a copy‑paste onboarding brief for the next agent and save a handoff note.

## Usage

```bash
/onboard-next-agent <task-id> [--auto] [--dry-run]
```

- **`<task-id>`**: Workstream or session identifier to carry forward
- **--auto**: Generate the brief without additional prompts (never commits)
- **--dry-run**: Show what will be generated without writing files

## When to use

- At the end of a session when handing off to a future agent
- After offboarding to produce a concise next‑agent brief

## Behavior (what the agent will do)

1. Collect recent context from:
   - `docs/agents/session-notes/` (latest Session Note)
   - `docs/global/Decision_Docket.md`
   - `docs/global/TODO_Log.md`
2. Generate a structured onboarding brief containing:
   - TL;DR (3 bullets)
   - Required Reading (ordered list with links)
   - Current State
   - Next Tasks (actionable bullets)
   - Risks & Constraints
   - Related Files/Docs
3. Write a handoff note to:
   - `docs/agents/session-notes/SN_<YYYYMMDDHHMM>_<task-id>_handoff.md` (24‑hour UTC)
4. Echo the brief in chat for copy‑paste convenience
5. Offer to append “Next Agent First Tasks” into `docs/global/TODO_Log.md` (Pending or In Progress) without committing

## Output format (example)

```markdown
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

## Outputs

- Path to generated handoff note
- Rendered onboarding brief (TL;DR, Required Reading, Next Tasks, Risks)

## Safety & boundaries

- No writes to company Linear projects
- Company docs remain read‑only; only personal docs in this repo are edited
- If required inputs are missing, the agent pauses and asks for guidance

## Example

```bash
/onboard-next-agent agent-offboarding
```

Agent response summary:

- Created `docs/agents/session-notes/SN_20251001_agent-offboarding_handoff.md`
- Included TL;DR, Required Reading, Next Tasks, Risks, and Related Files
- Ready for the next agent to begin immediately

## Related

- `.cursor/rules/agent-chat-commands.mdc`
- `.cursor/rules/agent-session-notes.mdc`
- `.cursor/rules/agent-offboarding.mdc`
- `docs/agents/session-notes/`
