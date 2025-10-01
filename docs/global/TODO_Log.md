# TODO Log

- **Last Updated**: 2025-10-01T00:00:00Z
- **Session**: agent-offboarding
- **Owner**: slittle

## Completed

### Session: ticket-workflows-v1 (2025-10-01)

- [x] Create Ticket Workflow README with mermaid diagrams and rules
- [x] Document minimal `/ticket-*` commands with per-command docs
- [x] Add Promote & Validate gate to wizard/workflow docs
- [x] Create Ticket Validator Spec and resolve markdown lints
- [x] Link workflow README from tickets README

### Session: agent-offboarding (2025-10-01)

- [x] Create chat commands and rules for session closure and offboarding
- [x] Add read-only banner and separation notes for company docs
- [x] Normalize filenames; move non-draft data out of drafts
- [x] Add link checker, ISO timestamp validator, and pre-commit hooks
- [x] Create/Update session note and stage changes for review
- [x] Fix broken markdown links across repo; add example ADR; commit changes

### Session: template-pt-1 (2025-10-01)

- [x] Add `/onboard-next-agent` command documentation
- [x] Create `docs/global/GLOSSARY.md`
- [x] Add ADR template at `docs/prds/global/templates/agents/adr/ADR_Template.md`
- [x] Add Research Request template at `docs/global/templates/Research_Request_Template.md`
- [x] Update `docs/global/TODO_Log.md` to mark completed items

### Session: repo-cleanup-implementation (2025-01-27)

- [x] Fix naming inconsistency: GLB-TKT vs GBL-PRD prefixes (should be GBL-TKT for consistency)
- [x] Resolve duplicate ADR templates: docs/agents/templates/ADR_Template.md vs docs/prds/global/templates/agents/adr/ADR_Template.md
- [x] Resolve duplicate Research Request templates: docs/agents/templates/Research_Request_Template.md vs docs/global/templates/Research_Request_Template.md
- [x] Complete empty files: docs/raw/cost-of-manufacturing-offering-context.md (currently empty)
- [x] Populate APPROVED-GLOSSARY.md (currently minimal with only front matter)
- [x] Complete GLB-TKT_Best_Practices.md template (stops at line 77, incomplete sections)
- [x] Clean up stranded TODOs in RSM call notes files (rsm-call-notes-documentation.md, rsm-call-notes-organized.md)
- [x] Clean up stranded TODOs in LEG-63 work log (8 unchecked items in work-log/LEG-63-WORK-LOG.md)
- [x] Clean up stranded TODOs in SLF-78 draft ticket (multiple unchecked items in SLF-78-boxwood-means-acquisition-exploration-draft.md)
- [x] Resolve template location confusion: decide whether templates belong in docs/agents/templates/ or docs/global/templates/
- [x] Update Decision Docket open decisions: ADR template structure and Research Request template format are now resolved
- [x] Standardize front matter across all templates (some missing required fields like created/updated timestamps)
- [x] Fix inconsistent directory structure: docs/prds/global/templates/agents/adr/ is overly nested
- [x] Complete missing template files referenced in docs/agents/templates/README.md but not found
- [x] Remove obsolete files: linear/tickets/archive/obsolete/ directory contains outdated drafts

### Session: repo-cleanup-analysis (2025-01-27)

- [x] Conduct comprehensive repository analysis for uncertainties, conflicts, and stranded TODOs
- [x] Identify naming inconsistencies (GLB-TKT vs GBL-PRD prefixes)
- [x] Find duplicate templates (ADR and Research Request templates in multiple locations)
- [x] Locate empty/incomplete files requiring completion
- [x] Catalog stranded TODOs across various files (RSM notes, LEG-63 work log, SLF-78 draft)
- [x] Identify template location confusion and directory structure issues
- [x] Add 15 high-priority cleanup items to TODO Log organized by complexity

### Session: repo-cleanup (2025-01-27)

- [x] Fix ISO 8601 dates in session notes to include time
- [x] Delete empty duplicate PRD file (docs/prds/GBL-PRD_Best_Practices.md)
- [x] Fix broken relative links in templates README
- [x] Rename archived ticket file to match its id (LEG-TKT_Collect_Cost_of_Manufacturing_an_Offering_Inputs.md)
- [x] Remove .bak suffix from obsolete draft
- [x] Fix typo in shortcut filename and update references (try-shortcut-prompt-style-guide.md)

### Session: workflow-finalization (2025-10-01)

- [x] Define practical Background Agent Draft Review Workflow
- [x] Integrate Ticket Wizard rule into workflow
- [x] Create comprehensive ticket wizard alignment review
- [x] Define Global Work Log vs To-Do project process distinction
- [x] Establish file organization structure for drafts
- [x] Integrate safety checks into workflow phases
- [x] Create session note with offboarding checklist
- [x] Update Decision Docket with key decisions
- [x] Update TODO Log with carryover items

### Session: PRD-Best-Practices-Definition (2025-09-27)

- [x] Create /docs/global/ and /docs/prds/ directories
- [x] Define PRD best practices template aligned with Linear workflow
- [x] Create GBL-PRD_Best_Practices.md
- [x] Draft options for GBL-PRD_Best_Practices in chat for review
- [x] Decide PRD front matter schema and required fields
- [x] Create generative plan doc for Agent Artifacts & workflows in docs/raw/plans
- [x] Create generative plan doc for Pydantic Schema Review Agent in docs/raw/plans
- [x] Define lightweight offboarding process with rules and checklist
- [x] Update templates to follow datetime-format rule

## In Progress

- [ ] Propose Cursor rules and helpful commands to enhance workflows

## Pending

### Next Agent Session (Awaiting User Approval)

- [ ] Review and approve Background Agent Draft Review Workflow
- [ ] Review Ticket Wizard Alignment documentation
- [ ] Test workflow with next background agent session
- [ ] Create test draft ticket using ticket wizard process (all 5 phases)
- [ ] Validate quality checks catch issues before Linear creation
- [ ] Apply process to existing draft tickets in linear/tickets/drafts/
- [ ] Migrate content between SLF-73 and To-Do project per defined process
- [ ] Create automation opportunities for workflow
- [ ] Monitor workflow effectiveness and gather feedback

### General Backlog

- [x] Create blank GLOSSARY.md in /docs/global/
- [ ] Create LEG-PRD_Design_Economic_Transaction_Model.md from finalized template
- [x] Create LEG-PRD_Collect_Cost_of_Manufacturing_an_Offering_Inputs.md from finalized template
- [ ] Create LEG-PRD_Design_Cost_of_Manufacturing_an_Offering.md from finalized template
- [ ] Create LEG-PRD_Determine_Minimum_Check_Size.md from finalized template
- [ ] Decide folder and document taxonomy for docs/prds/global/templates/agents/adr
- [ ] Document agent artifacts framework (Role Card, Context Pack, Playbook, ADRs)
- [ ] Define onboarding and offboarding checklists for agents
- [ ] Define session note format and decision docket process
- [ ] Prepare example Agent Role Card and Session Note
- [x] Add ADR and Research Request markdown templates
- [ ] Publish agreed Best Practices into docs/global/GBL-PRD_Best_Practices.md

### Repository Cleanup (High Priority)

- [ ] Fix naming inconsistency: GLB-TKT vs GBL-PRD prefixes (should be GBL-TKT for consistency)
- [ ] Resolve duplicate ADR templates: docs/agents/templates/ADR_Template.md vs docs/prds/global/templates/agents/adr/ADR_Template.md
- [ ] Resolve duplicate Research Request templates: docs/agents/templates/Research_Request_Template.md vs docs/global/templates/Research_Request_Template.md
- [ ] Complete empty files: docs/raw/cost-of-manufacturing-offering-context.md (currently empty)
- [ ] Populate APPROVED-GLOSSARY.md (currently minimal with only front matter)
- [ ] Complete GBL-TKT_Best_Practices.md template (stops at line 77, incomplete sections)
- [ ] Clean up stranded TODOs in RSM call notes files (rsm-call-notes-documentation.md, rsm-call-notes-organized.md)
- [ ] Clean up stranded TODOs in LEG-63 work log (8 unchecked items in work-log/LEG-63-WORK-LOG.md)
- [ ] Clean up stranded TODOs in SLF-78 draft ticket (multiple unchecked items in SLF-78-boxwood-means-acquisition-exploration-draft.md)
- [ ] Resolve template location confusion: decide whether templates belong in docs/agents/templates/ or docs/global/templates/
- [ ] Update Decision Docket open decisions: ADR template structure and Research Request template format are now resolved
- [ ] Standardize front matter across all templates (some missing required fields like created/updated timestamps)
- [ ] Remove obsolete files: linear/tickets/archive/obsolete/ directory contains outdated drafts
- [ ] Fix inconsistent directory structure: docs/prds/global/templates/agents/adr/ is overly nested
- [ ] Complete missing template files referenced in docs/agents/templates/README.md but not found

## Blocked

- [ ] None currently

## Notes

- PRD templates are complete and ready for use
- Agent artifacts framework is planned but needs implementation
- Offboarding process is defined and ready for use

## Session History

- **2025-01-27**: repo-cleanup-analysis - Comprehensive repository analysis identifying 15 high-priority cleanup items including naming inconsistencies, duplicate templates, stranded TODOs, and structural issues
- **2025-01-27**: repo-cleanup - Fixed ISO dates, removed empty files, corrected broken links, renamed files to match IDs, fixed typos
- **2025-10-01**: workflow-finalization - Defined Background Agent Draft Review Workflow with ticket wizard integration, aligned with safety rules, created comprehensive documentation
- **2025-09-27**: PRD-Best-Practices-Definition - Defined PRD templates, front matter schema, and offboarding process
