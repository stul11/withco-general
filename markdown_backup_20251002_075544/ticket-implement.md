# /ticket-implement

Create a Linear issue in the Global To‑Do project (with explicit approval).

## Usage

```bash
/ticket-implement
```

## Behavior

- Requires explicit user approval and safety checks
- Only targets Global To‑Do (`to-do-and-planning-e2ce95344374`)
- Back‑link the created Linear issue into the draft

## Related

- `docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md`
- `.cursor/rules/background-agent-safety.mdc`
