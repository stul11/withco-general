# Agent Templates Directory

This directory contains templates for agent-related artifacts and workflows.

## Available Templates

### Core Templates

- **Session_Note_Template.md**: Template for documenting agent-assisted sessions
- **Decision_Docket_Template.md**: Template for decision tracking and rationale
- **TODO_Log_Template.md**: Template for task management and tracking

### Agent Artifacts

- **Agent_Role_Card_Template.md**: Template for defining agent roles, scope, and constraints
- **Context_Pack_Template.md**: Template for curated context collections
- **Playbook_Template.md**: Template for step-by-step procedures

### Process Templates

- **ADR_Template.md**: Architecture Decision Record template
- **Research_Request_Template.md**: Template for research project requests
- **Onboarding_Checklist_Template.md**: Template for agent onboarding procedures
- **Offboarding_Checklist_Template.md**: Template for agent offboarding procedures

## Usage Guidelines

### Template Selection

- Use **Session Note** template for documenting agent sessions
- Use **Role Card** template for defining new agent capabilities
- Use **Context Pack** template for preparing agent context
- Use **Playbook** template for documenting procedures
- Use **ADR** template for architectural decisions
- Use **Research Request** template for research projects

### Naming Conventions

- **Session Notes**: `SN_YYYYMMDD_<TaskId>.md`
- **Role Cards**: `ARC_<Name>.md`
- **Context Packs**: `CP_<Topic>.md`
- **Playbooks**: `PB_<Process>.md`
- **ADRs**: `[TEAM]-ADR_<Title>.md`
- **Research Requests**: `[TEAM]-RES_<Title>.md`

### Front Matter

All templates include standardized front matter with:

- ID, title, status, owner, reviewers
- Timestamps (ISO 8601 format)
- Tags, related documents, risk level
- Version tracking

## Related Documentation

- [Agent Artifacts Planning](/workspace/docs/agents/session-notes/SN_20251001_agent-offboarding.md)
- [Background Agent Workflow](/workspace/docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md)
- [Agent Offboarding Rule](/workspace/.cursor/rules/agent-offboarding.mdc)
- [Agent Chat Commands](/workspace/.cursor/rules/agent-chat-commands.mdc) — `/offboard`, `/end-session`, `/onboard-next-agent`
