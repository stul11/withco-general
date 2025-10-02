# /ticket-validate

Validate that the current draft matches the minimal template and timestamp policy.

## Usage

```bash
/ticket-validate
```

## Behavior

- Check headings and order against `ticket-template.md`
- Validate front matter keys exist
- Ensure `created`/`updated` are ISO 8601 UTC
- Offer auto‑fix for minor issues

## Related

- `docs/agents/workflows/Ticket_Validator_Spec.md`
- `linear/docs/templates/ticket-template.md`
