# /end-session

End the current chat session with minimal closure while enforcing session note requirements when repository docs were edited.

## Usage

```
/end-session <task-id> [--dry-run] [--no-validate] [--auto]
```

- task-id: Short slug for this session (e.g., `workflow-finalization`, `PRD-Best-Practices-Definition`).
- --dry-run: Show what will happen without writing files or staging.
- --no-validate: Skip link and timestamp validation.
- --auto: Create/update Session Note and stage changes without additional prompts (never auto-commit).

## When to use

- Quick sessions or read-only work.
- Sessions with light edits where a full offboarding is not required.

## Preconditions

- None. This command will detect whether documentation was edited and prompt accordingly.

## Behavior (what the agent will do)

1. Confirm intent to end the session.
2. Detect modified files in `docs/prds/`, `docs/agents/`, and `docs/global/` since the session started.
3. If any such docs were modified:
   - Require a Session Note per `.cursor/rules/agent-session-notes.mdc`.
   - Offer to create a new note from `docs/agents/templates/Session_Note_Template.md` in `docs/agents/session-notes/` using the provided `<task-id>`.
   - Prefill metadata (Agent, Owner, Date, Inputs, Outputs) and list changed files.
   - Validate the Session Note includes all required sections:
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
   - Offer to update `docs/global/Decision_Docket.md` and `docs/global/TODO_Log.md`.
4. Run validations (optional but recommended):
   - `python3 scripts/check_markdown_links.py`
   - `python3 scripts/validate_iso_timestamps.py docs`
5. Prepare a suggested git commit message and list of changed files. Do not commit automatically unless explicitly instructed.
6. Provide a concise completion summary and next steps (if any).

### Agent runbook (non-interactive quick-run)

1. Detect changed docs to decide whether a Session Note is required:
   - `git status --porcelain docs/agents docs/global docs/prds`
2. If docs changed, ensure a Session Note exists, follows the naming convention (`SN_YYYYMMDD-HHMM_<task-id>.md`, 24-hour UTC rounded down to the nearest 15 minutes), and includes every required section:
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
3. Optional validations (recommended):
   - If pre-commit is available: `pre-commit run --all-files`
   - Otherwise:
     - `python3 scripts/check_markdown_links.py`
     - `python3 scripts/validate_iso_timestamps.py docs`
4. Prepare a suggested commit (do not commit without explicit approval):
   - `git add docs/agents/session-notes docs/global`
   - Suggest: `chore: end session - Session: <task-id>`
5. Output summary of changes and any validation warnings.

## Safety & boundaries

- No Linear writes are performed.
- Company docs remain read-only (e.g., `linear/docs/How_to_use_Linear.md`).
- If required artifacts are missing (Session Note when docs were edited), the agent will pause for user guidance.

## Outputs

- Path to Session Note (created or confirmed).
- Optional diffs or file lists to aid commit review.
- Suggested commit message block.

## Example

```
/end-session workflow-finalization
```

Agent response summary:

- Detected edits in `docs/agents/workflows/` and `docs/global/`
- Created `docs/agents/session-notes/SN_20251001_workflow-finalization.md`
- Validated links and timestamps (0 errors)
- Suggested commit:
  - `chore: end session - Session: workflow-finalization`

## Related

- `.cursor/rules/agent-session-notes.mdc`
- `.cursor/rules/agent-offboarding.mdc`
- `.cursor/rules/agent-chat-commands.mdc`
- `docs/agents/templates/Offboarding_Checklist_Template.md`
