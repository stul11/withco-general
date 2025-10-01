# Global Documentation Directory

This directory contains global standards, best practices, and shared documentation for the withco-general repository.

## Directory Structure

```
docs/global/
├── GBL-PRD_Best_Practices.md    # PRD standards and templates
├── GBL-TKT_Best_Practices.md    # Ticket standards and templates
├── Decision_Docket.md           # Key decisions and rationale
├── TODO_Log.md                  # Task tracking and carryover
└── glossary/                    # Terminology and definitions
    ├── APPROVED-GLOSSARY.md     # Official terminology
    └── INFORMAL-GLOSSARY.md     # Working terms
```

## Key Documents

### Best Practices

- **GBL-PRD_Best_Practices.md**: Comprehensive guide for Product Requirements Documents
  - Two template formats: Linear-aligned vs repo-only
  - Standardized front matter schema
  - Team-based naming conventions (PROD-PRD*, AM-PRD*, etc.)

- **GBL-TKT_Best_Practices.md**: Standards for ticket creation and management
  - Required sections and structure
  - 3-tier DoD (Fast/Standard/Gold)
  - Quick commands for efficient drafting

### Tracking Documents

- **Decision_Docket.md**: Rolling log of key decisions with:
  - Context and rationale
  - Options considered
  - Impact assessment
  - Links to related documents

- **TODO_Log.md**: Persistent task tracking with:
  - Completed, in-progress, and pending items
  - Session history
  - Carryover items between sessions

### Glossary

- **APPROVED-GLOSSARY.md**: Official terminology (currently minimal)
- **INFORMAL-GLOSSARY.md**: Working terms and definitions
  - Agent & automation terms
  - Document types
  - Workflow terms
  - Safety & process terms

## Usage Guidelines

### Document Creation

- Follow naming conventions: `[TEAM]-[TYPE]_[Title].md`
- Use standardized front matter with ISO 8601 timestamps
- Include proper tags and related document links
- Update Decision Docket for significant decisions

### Maintenance

- Update TODO Log at session end
- Promote informal glossary terms to approved when stable
- Keep Decision Docket current with rationale
- Archive completed work appropriately

## Related Documentation

- [Agent Templates](../agents/templates/)
- [Background Agent Workflow](../agents/workflows/)
- [Cursor Rules](../../.cursor/rules/)
- [Linear Integration](../../linear/)