# /ticket-wizard

Run the 5‑phase guided conversation per `.cursor/rules/ticket-wizard.mdc`.

## Usage

```bash
/ticket-wizard
```

## Behavior

- Follows Phase 0..5 (Boot, Triage, Context, DoD+Plan, Risks/OOS, Output)
- Produces a "Beautiful Ticket" per best‑practices (chat only)
- Offer Promote & Validate Gate: `/ticket-promote` then `/ticket-validate`
- Ask before writing drafts to `linear/tickets/drafts/`

## Related

- `.cursor/rules/ticket-wizard.mdc`
- `docs/agents/workflows/Ticket_Workflow_README.md`
