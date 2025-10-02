# Decision Docket

- **Last Updated**: 2025-10-01T00:00:00Z
- **Owner**: slittle

## Recent Decisions

### 2025-01-27 (B)

- **Decision**: Resolve ADR template structure and Research Request template format
- **Context**: Duplicate templates existed in multiple locations with different formats; needed to establish canonical versions
- **Options Considered**: Keep both versions, Choose one format, Merge formats
- **Rationale**: Single canonical template per type ensures consistency; comprehensive format in docs/agents/templates/ provides better structure
- **Impact**: ADR and Research Request templates now have single canonical versions; duplicate templates removed; template location confusion resolved
- **Links**: docs/agents/templates/ADR_Template.md, docs/agents/templates/Research_Request_Template.md
- **Owner**: slittle

### 2025-01-27 (A)

- **Decision**: Convert draft ticket to PRD format for cost of manufacturing research
- **Context**: Existing draft ticket had comprehensive content suitable for PRD structure
- **Options Considered**: Keep as ticket, convert to PRD, create new PRD from scratch
- **Rationale**: PRD format provides better structure for research requirements and comprehensive documentation
- **Impact**: Established pattern for converting suitable drafts to PRDs; improved documentation structure
- **Links**: docs/prds/LEG-PRD_Collect_Cost_of_Manufacturing_an_Offering_Inputs.md
- **Owner**: slittle

### 2025-10-01 (A)

- **Decision**: Establish minimal-argument ticket command suite and visual README
- **Context**: Need a simpler, consistent path from best-practices drafts to minimal `ticket-template.md`
- **Options Considered**: Keep wizard only, Add promote/validate gates, Full automation
- **Rationale**: Promote & Validate gate ensures simplicity and consistency; per-command docs reduce cognitive load
- **Impact**: New `/ticket-*` command docs; diagrams and state model unify the flow; validator spec enforces headings/timestamps
- **Links**: docs/agents/workflows/Ticket_Workflow_README.md, docs/agents/workflows/Ticket_Validator_Spec.md, .cursor/commands/ticket.md
- **Owner**: slittle

### 2025-10-01 (B)

- **Decision**: Implement 4-phase Background Agent Draft Review Workflow (Draft → Review → Authorization → Implementation)
- **Context**: Need practical workflow for background agents to create draft tickets, get user approval, and implement in Linear safely
- **Options Considered**: Automatic Linear creation, Manual only, Review-then-approve workflow
- **Rationale**: User approval requirement ensures quality control and safety; phased approach provides clear structure and checkpoints; separates draft creation from Linear implementation
- **Impact**: All background agents must follow this workflow; no automatic Linear pushes allowed; explicit user authorization required before Linear creation
- **Links**: docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md, docs/agents/session-notes/SN_20251001_workflow-finalization.md
- **Owner**: slittle

### 2025-10-01 (C)

- **Decision**: Integrate Ticket Wizard rule into Background Agent workflow
- **Context**: Need to ensure draft tickets follow ticket wizard's 5-phase conversation script and quality standards
- **Options Considered**: Separate process, Integrated workflow, Optional compliance
- **Rationale**: Ticket wizard provides proven structure for quality ticket creation; 5-phase conversation ensures completeness; quality checks catch issues before Linear creation
- **Impact**: All draft creation must follow ticket wizard phases; agents must produce "Beautiful Ticket" + Reviewer Pack; 11 quality checks must be met
- **Links**: .cursor/rules/ticket-wizard.mdc, docs/agents/workflows/Ticket_Wizard_Alignment_Review.md
- **Owner**: slittle

### 2025-10-01 (D)

- **Decision**: Introduce chat commands for session closure and offboarding
- **Context**: Need fast, reliable, and repeatable way to end chat sessions and perform full offboarding with documentation and safety checks
- **Options Considered**: Manual instructions, Single command, Two-tier commands (minimal vs full)
- **Rationale**: Two commands map to common usage: quick end vs full offboarding with compliance. Keeps safety and documentation enforcement clear and lightweight
- **Impact**: New commands `/end-session` and `/offboard` available; agents must follow rules for session notes, link/timestamp validations, and staging before commit
- **Links**: .cursor/commands/end-session.md, .cursor/commands/offboard.md, .cursor/rules/agent-chat-commands.mdc
- **Owner**: slittle

### 2025-10-01 (E)

- **Decision**: Resolve repository-wide broken markdown links and enforce validations
- **Context**: Link checker flagged multiple broken links across README, templates, workflows, and archived tickets
- **Options Considered**: Selective fixes, Remove references, Comprehensive fix with validation
- **Rationale**: Comprehensive fix ensures documentation integrity and future maintainability; validations prevent regressions
- **Impact**: All links now resolve; added example ADR to satisfy template references; enabled reliable offboarding workflow
- **Links**: docs/agents/session-notes/SN_20251001_agent-offboarding.md, scripts/check_markdown_links.py, scripts/validate_iso_timestamps.py
- **Owner**: slittle

### 2025-10-01 (F)

- **Decision**: Define clear distinction between Global Work Log (SLF-73) and To-Do & Planning project
- **Context**: Overlap between systems causing confusion and duplication; need clear process for work item placement
- **Options Considered**: Single system, Separate systems, Merged systems
- **Rationale**: Different purposes - Work Log for context/reference, To-Do for active work management; integration maintains connections while keeping purposes distinct
- **Impact**: Content placement rules defined; cross-reference pattern established; work items routed to appropriate system based on purpose
- **Links**: docs/global/Global_Work_Log_vs_To_Do_Process.md
- **Owner**: slittle

### 2025-10-01 (G)

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

### 2025-09-27 (A)

- **Decision**: Adopt V3 front matter schema with team-based PRD naming
- **Context**: Need standardized front matter for PRDs that aligns with Linear workflow
- **Options Considered**: Minimal schema, Standard schema, Extended schema
- **Rationale**: Standard schema provides good balance of structure without overhead; team-based naming (PROD-PRD*, AM-PRD*, etc.) provides clear organization
- **Impact**: All future PRDs must use this schema; affects PRD creation workflow
- **Links**: withco-general/docs/global/GBL-PRD_Best_Practices.md
- **Owner**: slittle

### 2025-09-27 (B)

- **Decision**: Create two distinct PRD templates (Linear-aligned vs Repo-only)
- **Context**: Need to distinguish between PRDs that migrate to Linear vs those that stay repo-only
- **Options Considered**: Single template, Multiple templates, Dynamic template
- **Rationale**: Different use cases require different levels of detail; repo-only PRDs can include more context sections
- **Impact**: Template selection based on migration intent; affects PRD authoring process
- **Links**: withco-general/docs/global/GBL-PRD_Best_Practices.md
- **Owner**: slittle

### 2025-09-27 (C)

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

### 2025-10-02 (A)

- **Decision**: Establish canonical calculator structures for UPREIT vs K‑1 package
- **Context**: Original TSV calculators contained brittle references and inline comments that broke parsing; Excel paste caused locked/misaligned refs
- **Options Considered**: Keep existing TSV formulas; re-index formulas; build selector-based single-sheet; generate per-scenario tabs
- **Rationale**: Selector-based, transposed calculator avoids sheet protection issues and ensures reliable references; corrected 06/07 blocks align with inputs
- **Impact**: A stable workbook with INDEX and per-scenario tabs; one-sheet calculator artifact for copy/paste; documented formula corrections
- **Links**: linear/tickets/drafts/research-prompts/tax-upreit-llc-k1-vs-1099-div-20251001/tax-upreit-llc-k1-vs-1099-div-20251001-response/Tax_UPREIT_LLC_K1_vs_1099DIV_Enhanced_With_Scenarios.xlsx; docs/agents/session-notes/SN_202510020338_tax-upreit-llc-k1-vs-1099-div.md
- **Owner**: slittle

## Decision Patterns

- Prefer lightweight, human-in-the-loop approaches over heavy automation
- Align with existing Linear workflow and team structure
- Use templates and rules to ensure consistency without overhead
- Document decisions in Decision Docket for future reference
