# /ticket-new

Start a best‑practices ticket draft with minimal input.

## Usage

```bash
/ticket-new "Title"
```

## Behavior

- Prompts for missing essentials (team, due date, DoD target)
- Operates in chat only; does not write files without confirmation
- Seeds `GLB-TKT_Best_Practices.md` structure in the working draft

## Related

- `.cursor/rules/ticket-wizard.mdc`
- `docs/agents/workflows/Ticket_Workflow_README.md`
