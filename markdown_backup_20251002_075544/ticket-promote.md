# /ticket-promote

Transform best‑practices → minimal template (`ticket-template.md`) with a single DoD list.

## Usage

```bash
/ticket-promote [--tier standard|fast|gold]
```

## Behavior

- Default DoD tier is `standard` if not provided
- Collapses ladder into one DoD checklist
- Sets `created` (once) and updates `updated` (ISO 8601 UTC)
- Previews transformed content; asks before writing

## Related

- `linear/docs/templates/ticket-template.md`
- `docs/agents/workflows/Ticket_Validator_Spec.md`
- `.cursor/commands/ticket-validate.md`
