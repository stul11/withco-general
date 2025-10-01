# Linear Tickets Directory

This directory contains draft tickets and archived tickets for the withco-general repository.

## Directory Structure

```text
linear/
├── docs/                    # Linear workflow documentation
├── tickets/
│   ├── drafts/             # Active draft tickets pending review
│   └── archive/            # Completed and archived tickets
└── templates/              # Ticket templates
```

## Draft Tickets (`drafts/`)

Draft tickets are created by background agents using the Ticket Wizard workflow and are pending user review and approval before being implemented in Linear.

### Naming Conventions

- **Draft Tickets**: `{TEAM-ID}-{title-slug}-draft.md`
- **WIP Tickets**: `{descriptive-name}-wip.md`
- **Research Prompts**: `research-prompts/{topic-name}.md`

### Workflow

1. **Draft Creation**: Background agent creates draft using Ticket Wizard (5 phases)
2. **User Review**: Human reviews draft for completeness and accuracy
3. **Authorization**: User explicitly approves draft for Linear implementation
4. **Implementation**: Agent creates Linear issue in Global To-Do project
5. **Archival**: Draft moved to archive with Linear issue link

### Safety Rules

- Only Global To-Do project (`to-do-and-planning-e2ce95344374`) allowed for Linear writes
- Company Linear projects are read-only
- User authorization required before any Linear operations
- All operations logged for audit trail

## Archived Tickets (`archive/`)

Completed tickets are archived with their Linear issue links for reference.

### Archive Structure

- **Completed**: `{TEAM-ID}-{title-slug}.md`
- **Rejected**: `{TEAM-ID}-{title-slug}-rejected.md`
- **Obsolete**: `obsolete/` (for test files and outdated drafts)

## Related Documentation

- [Background Agent Draft Review Workflow](../../docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md)
- [Ticket Workflow README](../../docs/agents/workflows/Ticket_Workflow_README.md)
- [Ticket Wizard Rule](../../.cursor/rules/ticket-wizard.mdc)
- [Background Agent Safety Rules](../../.cursor/rules/background-agent-safety.mdc)
- [Ticket Best Practices](../../docs/global/GLB-TKT_Best_Practices.md)
- [How to use Linear](../docs/How_to_use_Linear.md) — Company documentation (READ-ONLY). Do not modify; use personal best practices in `docs/global/` instead.
