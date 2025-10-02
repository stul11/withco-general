# /ticket-review

Mark the draft ready for review and generate a Reviewer Pack.

## Usage

```bash
/ticket-review
```

## Behavior

- Set `status: In Review`, keep `stage: Planning`
- Generate TL;DR (3 bullets) and review checklist
- Echo links and file path for reviewers

## Related

- `docs/agents/workflows/Ticket_Workflow_README.md`
- `.cursor/commands/ticket-approve.md`
