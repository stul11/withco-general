# Phase 02 — Command Docs Check

## Results
- [x] .cursor/commands/toplan-add.md present with Usage, schema, examples
- [x] .cursor/commands/todo-add.md present with Usage, schema, examples

## Snippets

### toplan-add Usage

Usage: /toplan-add --title "<Title>" --priority <LOW|MED|HIGH> --labels "POTENTIAL,DECISION" --team <TEAM|global> --source <path#anchor> [--tags "tag1,tag2"] [--notes "..."]

Behavior:

- Appends a multi-line TOPLAN item to `00-key-docs/TOPLAN.md` (global) or `linear/{TEAM}/TOPLAN.md` (team) with schema:

```
- [ ] (LABELS) [PRIORITY] Title
  source: <relative-path>#<anchor>
  tags: <comma-or-list>
  notes: <optional 1-2 lines>
```

Rules:

- Require `source:` for all automated/template workflows
- Allow multiple labels (comma-separated): POTENTIAL, AGENT, RESEARCH, DECISION, BLOCKED
- Confirm name/slug when creating any related NOTE

Examples:

- /toplan-add --title "Evaluate pricing granola scope" --priority HIGH --labels "POTENTIAL,DECISION" --team PROD --source docs/granola/GR_20251002-1015_pricing-page-rewrite-research.md#recommendations --tags "granola,pricing" --notes "Prepare 2 scenarios"


### todo-add Usage

Usage: /todo-add --title "<Title>" --priority <LOW|MED|HIGH> --labels "AGENT" --team <TEAM|global> --source <path#anchor> [--tags "tag1,tag2"] [--notes "..."]

Behavior:

- Appends a multi-line TODO item to `00-key-docs/TODO.md` (global) or `linear/{TEAM}/TODO.md` (team) with schema:

```
- [ ] (LABELS) [PRIORITY] Title
  source: <relative-path>#<anchor>
  tags: <comma-or-list>
  notes: <optional 1-2 lines>
```

Rules:

- Require `source:` for all automated/template workflows
- Allow multiple labels (comma-separated): POTENTIAL, AGENT, RESEARCH, DECISION, BLOCKED
- Confirm name/slug when creating any related NOTE

Examples:

- /todo-add --title "Align /offboard required sections" --priority MED --labels "AGENT" --team global --source docs/agents/session-notes/SN_20251002-0630_session-NOTE-template-analysis.md#immediate-actions --tags "session-notes,templates"
