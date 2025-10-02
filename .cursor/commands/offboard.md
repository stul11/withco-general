# /offboard

Run the full offboarding checklist and close out the session according to repository rules.

## Usage

```
/offboard <task-id> [--dry-run] [--no-validate] [--auto]
```

- task-id: Short slug for this session (e.g., `workflow-finalization`).
- --dry-run: Show what will happen without writing files or staging.
- --no-validate: Skip link and timestamp validation.
- --auto: Create/update Session Note and stage changes without additional prompts (never auto-commit).

## When to use

- End of any substantive session with repo changes.
- You want full documentation and safety validations applied.

## Preconditions

- None. This command ensures all required artifacts are created/updated before ending the session.

## Behavior (what the agent will do)

1. Confirm intent to offboard.
2. Create or update a Session Note in `docs/agents/session-notes/` using `docs/agents/templates/Session_Note_Template.md`.
   - File name: `SN_YYYYMMDDHHMM_<task-id>.md` (24-hour UTC)
   - Prefill metadata and enumerate inputs, steps, outputs, citations, next actions.
3. Update `docs/global/Decision_Docket.md` with any decisions made.
4. Update `docs/global/TODO_Log.md` with completed, in-progress, and pending items (carryover clearly marked).
5. Validations:
   - `python3 scripts/check_markdown_links.py`
   - `python3 scripts/validate_iso_timestamps.py docs`
6. Prepare git changes:
   - Stage updated/created files for review
   - Propose commit message in the format:
     - `feat|chore|docs: <summary> - Session: <task-id>`
7. Provide final summary including safety notes and next actions.

### Agent runbook (non-interactive quick-run)

1. Detect changed docs (for note inputs/outputs):
   - `git status --porcelain docs/agents docs/global docs/prds`
2. Ensure session note exists and is populated:
   - Create `docs/agents/session-notes/SN_YYYYMMDDHHMM_<task-id>.md` if missing using `docs/agents/templates/Session_Note_Template.md`
   - Add all required sections: Inputs & Context, Full Findings, Steps Taken, Outputs (with file paths), Citations (file:lines), Risks & Issues Identified, Reasoning & Rationale, Next Actions
3. Update global trackers:
   - Append decisions to `docs/global/Decision_Docket.md`
   - Update status blocks in `docs/global/TODO_Log.md` (Completed/In Progress/Pending)
4. Validations:
   - If pre-commit is available: `pre-commit run --all-files`
   - Otherwise:
     - `python3 scripts/check_markdown_links.py`
     - `python3 scripts/validate_iso_timestamps.py docs`
5. Stage and propose commit:
   - `git add docs/agents/session-notes docs/global`
   - Suggested message: `feat|chore|docs: <summary> - Session: <task-id>`
6. Output a concise summary with file list and any validation errors.

## Safety & boundaries

- No writes to company Linear projects.
- Company docs remain read-only (e.g., `linear/docs/How_to_use_Linear.md`).
- If requirements are incomplete, the agent halts and requests guidance.

### Failure handling

- If link or timestamp validation fails, report errors and pause before commit.
- If session note cannot be created (naming conflict), write to a temp path and ask for guidance.

## Outputs

- Path to Session Note
- Docket and TODO updates
- Validation results (links/timestamps)
- Suggested commit message

## Example

```
/offboard workflow-finalization
```

Agent response summary:

- Created `docs/agents/session-notes/SN_20251001_workflow-finalization.md`
- Updated `docs/global/Decision_Docket.md` and `docs/global/TODO_Log.md`
- Validated links and timestamps (0 errors)
- Suggested commit:
  - `feat: define background agent draft review workflow - Session: workflow-finalization`

## Related

- `.cursor/rules/agent-offboarding.mdc`
- `.cursor/rules/agent-session-notes.mdc`
- `.cursor/rules/agent-chat-commands.mdc`
- `docs/agents/templates/Offboarding_Checklist_Template.md`
- `docs/agents/workflows/Agent_Offboarding_Implementation_Checklist.md`
