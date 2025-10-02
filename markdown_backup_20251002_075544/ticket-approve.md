# /ticket-approve

Mark the draft as approved and freeze the DoD.

## Usage

```bash
/ticket-approve
```

## Behavior

- Set `status: Approved`, keep `stage: Planning`
- Freeze the DoD checklist and record approver
- Output next steps and ready-to-implement summary

## Related

- `.cursor/commands/ticket-implement.md`
- `docs/agents/workflows/Ticket_Workflow_README.md`
