<!-- markdownlint-disable MD013 -->

# /TODO-add

Append a TODO item to the canonical backlog and ensure CodeLens sidecars stay in sync.

## Synopsis

```bash
/TODO-add "Task description" --section Pending --owner slittle --tags a,b,c
```

## Behavior

- Writes a CodeLens-friendly TODO trigger line to `docs/global/TODO_Log.md` (or `TODO.md` if present) under the specified section:

  ```text
  - TODO: (LABELS) [PRIORITY] Title <!-- id: TODO-YYYYMMDD-### -->
    source: <relative-path>#<anchor>
    tags: <comma-or-list>
    notes: <optional 1-2 lines>
  ```

- Appends a stable id HTML comment to the line if the caller did not provide one: `<!-- id: TODO-YYYYMMDD-### -->`.
<!-- markdownlint-disable-next-line MD044 -->
- Invokes the sidecar sync generator to update `docs/global/TODO.codelens.todo`.

### Notes

- The id must be preserved on subsequent edits to keep Markdown and sidecars aligned.
- Sidecars are generated files; do not edit them by hand.

## Usage

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

## Notes

- Appends under "General Backlog > Open Work" by default (creates the section if missing).
- A convenience symlink exists at `00-key-docs/TODO_Log.md`.
- `--team` is limited to `global` to comply with safety rules (no writes to company Linear projects).

## Schema

```text
- TODO: (LABELS) [PRIORITY] Title <!-- id: TODO-YYYYMMDD-### -->
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
