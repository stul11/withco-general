# Decision Docket

- **Last Updated**: 2025-10-01T00:00:00Z
- **Owner**: slittle

## Recent Decisions

### 2025-10-01

- **Decision**: Implement 4-phase Background Agent Draft Review Workflow (Draft → Review → Authorization → Implementation)
- **Context**: Need practical workflow for background agents to create draft tickets, get user approval, and implement in Linear safely
- **Options Considered**: Automatic Linear creation, Manual only, Review-then-approve workflow
- **Rationale**: User approval requirement ensures quality control and safety; phased approach provides clear structure and checkpoints; separates draft creation from Linear implementation
- **Impact**: All background agents must follow this workflow; no automatic Linear pushes allowed; explicit user authorization required before Linear creation
- **Links**: docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md, docs/agents/session-notes/SN_20251001_workflow-finalization.md
- **Owner**: slittle

### 2025-10-01

- **Decision**: Integrate Ticket Wizard rule into Background Agent workflow
- **Context**: Need to ensure draft tickets follow ticket wizard's 5-phase conversation script and quality standards
- **Options Considered**: Separate process, Integrated workflow, Optional compliance
- **Rationale**: Ticket wizard provides proven structure for quality ticket creation; 5-phase conversation ensures completeness; quality checks catch issues before Linear creation
- **Impact**: All draft creation must follow ticket wizard phases; agents must produce "Beautiful Ticket" + Reviewer Pack; 11 quality checks must be met
- **Links**: .cursor/rules/ticket-wizard.mdc, docs/agents/workflows/Ticket_Wizard_Alignment_Review.md
- **Owner**: slittle

### 2025-10-01

- **Decision**: Define clear distinction between Global Work Log (SLF-73) and To-Do & Planning project
- **Context**: Overlap between systems causing confusion and duplication; need clear process for work item placement
- **Options Considered**: Single system, Separate systems, Merged systems
- **Rationale**: Different purposes - Work Log for context/reference, To-Do for active work management; integration maintains connections while keeping purposes distinct
- **Impact**: Content placement rules defined; cross-reference pattern established; work items routed to appropriate system based on purpose
- **Links**: linear/tickets/drafts/global-work-log-to-do-process-definition.md
- **Owner**: slittle

### 2025-10-01

- **Decision**: Establish file organization structure for draft tickets (drafts/, archive/)
- **Context**: Need clear organization for draft tickets at different stages
- **Options Considered**: Single directory, Multiple directories, Tag-based organization
- **Rationale**: Separate directories for drafts, WIP, and archives improves organization and workflow clarity; naming conventions ensure consistency
- **Impact**: All drafts saved in linear/tickets/drafts/; completed tickets archived with Linear links; clear naming conventions required
- **Links**: docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
- **Owner**: slittle

### 2025-10-01

- **Decision**: Integrate safety checks directly into workflow phases
- **Context**: Need to ensure background agents operate safely within defined boundaries
- **Options Considered**: Post-operation checks, Pre-operation checks, Continuous monitoring
- **Rationale**: Pre-operation checks prevent violations proactively; integrated approach ensures compliance at every step; audit trail provides accountability
- **Impact**: All Linear operations include mandatory safety checks; only Global To-Do project allowed for writes; company Linear projects protected (read-only)
- **Links**: .cursor/rules/background-agent-safety.mdc, docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md
- **Owner**: slittle

### 2025-09-27

- **Decision**: Adopt V3 front matter schema with team-based PRD naming
- **Context**: Need standardized front matter for PRDs that aligns with Linear workflow
- **Options Considered**: Minimal schema, Standard schema, Extended schema
- **Rationale**: Standard schema provides good balance of structure without overhead; team-based naming (PROD-PRD*, AM-PRD*, etc.) provides clear organization
- **Impact**: All future PRDs must use this schema; affects PRD creation workflow
- **Links**: withco-general/docs/global/GBL-PRD_Best_Practices.md
- **Owner**: slittle

### 2025-09-27

- **Decision**: Create two distinct PRD templates (Linear-aligned vs Repo-only)
- **Context**: Need to distinguish between PRDs that migrate to Linear vs those that stay repo-only
- **Options Considered**: Single template, Multiple templates, Dynamic template
- **Rationale**: Different use cases require different levels of detail; repo-only PRDs can include more context sections
- **Impact**: Template selection based on migration intent; affects PRD authoring process
- **Links**: withco-general/docs/global/GBL-PRD_Best_Practices.md
- **Owner**: slittle

### 2025-09-27

- **Decision**: Implement lightweight offboarding process with Session Notes and Decision Docket
- **Context**: Need to properly close agent sessions and maintain continuity between conversations
- **Options Considered**: No offboarding, Manual process, Automated process, Hybrid approach
- **Rationale**: Hybrid approach provides structure without heavy automation; enables knowledge transfer between sessions
- **Impact**: All agent sessions must follow offboarding checklist; creates persistent TODO and decision tracking
- **Links**: .cursor/rules/agent-offboarding.mdc, docs/agents/templates/
- **Owner**: slittle

### 2025-09-27

- **Decision**: Use team-based PRD naming convention (PROD-PRD*, AM-PRD*, SLF-PRD*, ANA-PRD*, DATA-PRD*, GBL-PRD*)
- **Context**: Need clear identification of PRD ownership and scope
- **Options Considered**: Generic naming, Team prefixes, Functional prefixes
- **Rationale**: Team prefixes align with Linear team structure and provide immediate context
- **Impact**: All PRD IDs must follow this convention; affects file organization
- **Links**: withco-general/docs/global/GBL-PRD_Best_Practices.md
- **Owner**: slittle

## Open Decisions

- [ ] Which Cursor rules to implement for agent workflows
- [ ] ADR template structure and requirements
- [ ] Research Request template format

## Decision Patterns

- Prefer lightweight, human-in-the-loop approaches over heavy automation
- Align with existing Linear workflow and team structure
- Use templates and rules to ensure consistency without overhead
- Document decisions in Decision Docket for future reference
