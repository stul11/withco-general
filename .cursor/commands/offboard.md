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
   - Validate all 11 required sections are populated:
     - [ ] **Metadata**: Task ID, Agent, Owner, Date, Duration
     - [ ] **Inputs & Context**: Key Documents/Files Provided, Context & Requirements, Relevant Prior Work
     - [ ] **Full Findings**: Summary of Findings, Detailed Findings with Description/File(s)/Line Numbers/Reasoning/Supporting Evidence
     - [ ] **Steps Taken**: Major Actions, Key Decisions, Tools/Methods Used
     - [ ] **Outputs**: Files Created/Modified, Key Deliverables, Documented Decisions
     - [ ] **Citations**: All sources referenced with precise file paths and line numbers
     - [ ] **Risks & Issues Identified**: Potential Issues, Mitigation Strategies
     - [ ] **Reasoning & Rationale**: Explanation of reasoning behind major actions/decisions
     - [ ] **Next Actions**: Immediate Follow-ups, For Next Session, Pending Approvals/Decisions
     - [ ] **Signoff**: Reviewer, Status, Date, Notes
3. Update `docs/global/Decision_Docket.md` with any decisions made.
4. Update `docs/global/TODO_Log.md` with completed, in-progress, and pending items (carryover clearly marked).
5. Validations:
   - **Session Note Completeness**: Verify all 11 required sections are populated (halt if incomplete)
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
   - Validate all 11 required sections are populated:
     - [ ] **Metadata**: Task ID, Agent, Owner, Date, Duration (lines 13-17)
     - [ ] **Inputs & Context**: Key Documents/Files Provided, Context & Requirements, Relevant Prior Work (lines 21-29)
     - [ ] **Full Findings**: Summary of Findings, Detailed Findings with Description/File(s)/Line Numbers/Reasoning/Supporting Evidence (lines 32-43)
     - [ ] **Steps Taken**: Major Actions, Key Decisions, Tools/Methods Used (lines 46-54)
     - [ ] **Outputs**: Files Created/Modified, Key Deliverables, Documented Decisions (lines 57-65)
     - [ ] **Citations**: All sources referenced with precise file paths and line numbers (lines 68-72)
     - [ ] **Risks & Issues Identified**: Potential Issues, Mitigation Strategies (lines 75-81)
     - [ ] **Reasoning & Rationale**: Explanation of reasoning behind major actions/decisions (lines 84-87)
     - [ ] **Next Actions**: Immediate Follow-ups, For Next Session, Pending Approvals/Decisions (lines 90-98)
     - [ ] **Signoff**: Reviewer, Status, Date, Notes (lines 101-107)
3. Update global trackers:
   - Append decisions to `docs/global/Decision_Docket.md`
   - Update status blocks in `docs/global/TODO_Log.md` (Completed/In Progress/Pending)
4. Validations:
   - **Session Note Completeness**: Verify all 11 required sections are populated (halt if incomplete)
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

- If session note validation fails (missing required sections), report missing sections and halt until completed
- If link or timestamp validation fails, report errors and pause before commit
- If session note cannot be created (naming conflict), write to a temp path and ask for guidance

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
