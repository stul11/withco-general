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

