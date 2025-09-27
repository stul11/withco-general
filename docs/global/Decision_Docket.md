# Decision Docket

- **Last Updated**: 2025-09-27T15:30:00Z
- **Owner**: slittle

## Recent Decisions

### 2025-09-27
- **Decision**: Adopt V3 front matter schema with team-based PRD naming
- **Context**: Need standardized front matter for PRDs that aligns with Linear workflow
- **Options Considered**: Minimal schema, Standard schema, Extended schema
- **Rationale**: Standard schema provides good balance of structure without overhead; team-based naming (PROD-PRD_, AM-PRD_, etc.) provides clear organization
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
- **Decision**: Use team-based PRD naming convention (PROD-PRD_, AM-PRD_, SLF-PRD_, ANA-PRD_, DATA-PRD_, GBL-PRD_)
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
