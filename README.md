# withco-general Repository

This repository serves as a context-rich workspace for drafting and organizing product/work planning content with an AI agent before pushing into the Linear system.

## Purpose

The **withco-general** repository enables collaborative work between humans and AI agents to create well-structured plans, tickets, and documentation with proper safety controls and quality assurance.

## Key Features

- **AI Agent Integration**: Background agents assist with ticket creation, documentation, and workflow management
- **Safety-First Design**: Strict boundaries prevent unauthorized access to company Linear projects
- **Human-in-the-Loop**: All Linear operations require explicit user authorization
- **Quality Templates**: Standardized templates ensure consistency across all artifacts
- **Audit Trail**: Complete logging of all operations for compliance and troubleshooting

## Repository Structure

```
withco-general/
├── .cursor/rules/              # AI agent behavior rules and constraints
├── docs/
│   ├── agents/                 # Agent workflows, templates, and session notes
│   ├── global/                # Global standards, best practices, and tracking
│   ├── prds/                  # Product Requirements Documents
│   └── raw/                   # Planning documents and research
├── linear/
│   ├── docs/                  # Linear workflow documentation
│   ├── tickets/               # Draft tickets and archives
│   └── templates/             # Ticket templates
└── README.md                  # This file
```

## Core Workflows

### Background Agent Draft Review Workflow

1. **Draft Creation**: Agent creates comprehensive ticket using Ticket Wizard (5 phases)
2. **User Review**: Human reviews draft for completeness and accuracy
3. **Authorization**: User explicitly approves draft for Linear implementation
4. **Implementation**: Agent creates Linear issue in Global To-Do project with safety checks

### Safety Rules

- **Allowed**: Read-only access to company Linear projects, write access to Global To-Do project
- **Prohibited**: Any writes to company Linear projects, automatic Linear pushes
- **Required**: User authorization before all Linear operations, complete audit trail

## Key Documents

### Templates & Standards
- [PRD Best Practices](docs/global/GBL-PRD_Best_Practices.md)
- [Ticket Best Practices](docs/global/GLB-TKT_Best_Practices.md)
- [Agent Templates](docs/agents/templates/)

### Workflows
- [Background Agent Draft Review Workflow](docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md)
- [Agent Offboarding Checklist](docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md)

### Tracking
- [Decision Docket](docs/global/Decision_Docket.md)
- [TODO Log](docs/global/TODO_Log.md)

## Getting Started

1. **Review Safety Rules**: Understand the boundaries and constraints
2. **Familiarize with Templates**: Use appropriate templates for your work
3. **Follow Workflows**: Use the established processes for consistency
4. **Maintain Documentation**: Update tracking documents and session notes

## Safety & Compliance

This repository implements multiple layers of safety:

- **Pre-operation Checks**: Validate all operations before execution
- **User Authorization**: Require explicit approval for all Linear writes
- **Audit Logging**: Complete trail of all operations
- **Rollback Procedures**: Safe recovery from any issues
- **Continuous Monitoring**: Real-time violation detection

## Support

For questions or issues:
- Review the [Informal Glossary](docs/global/glossary/INFORMAL-GLOSSARY.md)
- Check the [Decision Docket](docs/global/Decision_Docket.md) for context
- Follow the [Background Agent Workflow](docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md)

---

**Remember**: Safety first, functionality second. When in doubt, ask for user approval.