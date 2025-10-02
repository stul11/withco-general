# /TODO-add

### Usage

```bash
/TODO-add \
  --title "TITLE" \
  --priority LOW|MED|HIGH \
  --labels "AGENT" \
  --team global \
  --source path#anchor \
  [--tags "tag1,tag2"] \
  [--notes "..."]
```

### Behavior

- Appends a multi-line TODO item to the canonical `docs/global/TODO_Log.md`.
- A convenience symlink exists at `00-key-docs/TODO_Log.md`.
- Inserts under "General Backlog > Open Work" (creates the section if missing).
- `--team` is limited to `global` to comply with safety rules (no writes to company Linear projects).

### Schema

```text
- [ ] (LABELS) [PRIORITY] Title
  source: <relative-path>#<anchor>
  tags: <comma-or-list>
  notes: <optional 1-2 lines>
```

### Rules

- Require `--source` for automated/template workflows.
- Allow multiple labels (comma-separated): POTENTIAL, AGENT, RESEARCH, DECISION, BLOCKED.
- Keep titles short and action-oriented (imperative mood).
- Do not write to company Linear files; global TODO Log only.

### Examples

```bash
/TODO-add --title "Align /offboard required sections" \
  --priority MED \
  --labels "AGENT" \
  --team global \
  --source docs/agents/session-notes/SN_20251002-0000_phase-01-scaffolding-verification.md#immediate-actions \
  --tags "session-notes,templates" \
  --notes "Unify 11 required sections across commands"

/TODO-add --title "Consolidate glossary sources" \
  --priority MED \
  --labels "DECISION,RESEARCH" \
  --team global \
  --source docs/global/TODO_Log.md#general-backlog \
  --tags "glossary" \
  --notes "Decide merge vs promotion workflow"
```

### Non-interactive runbook (Agent)

1. Validate args: `--title`, `--priority`, `--labels`, `--team`, `--source`.
2. Locate `docs/global/TODO_Log.md`; create target subsection "General Backlog > Open Work" if missing.
3. Append the schema block with provided fields.
4. Stage file for review: `git add docs/global/TODO_Log.md`.
5. Echo the inserted block and file path for confirmation.

### Safety & Boundaries

- Writes only to `docs/global/TODO_Log.md` (or its symlink at `00-key-docs/TODO_Log.md`).
- No writes to company Linear projects or templates.
