# TODO Log

- **Last Updated**: 2025-10-02T04:45:00Z
- **Session**: background-cleanup-priority-refresh
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
- [ ] **[High | ~10-15 min]** Run `pre-commit run --all-files` for the agent-offboarding staging area and capture any failing hooks before fixes.
- [ ] **[High | ~15-20 min]** Resolve broken links identified in the agent-offboarding handoff (README offboarding link, SLF-78 try-shortcut references, workflow rule/template links) so link validation passes.
- [ ] **[High | ~10-15 min]** Re-verify all `.cursor/rules/*` and `docs/agents/workflows/*` links after fixes to ensure navigation from rules to workflows succeeds.
- [ ] **[High | ~10-15 min]** Execute `/offboard --dry-run`, `/end-session --dry-run`, and `/onboard-next-agent --dry-run` to confirm the updated commands operate end-to-end.

### Repository Cleanup (High Priority)

- [ ] Fix naming inconsistency: GLB-TKT vs GBL-PRD prefixes (should be GBL-TKT for consistency)
- [ ] Resolve duplicate ADR templates: docs/agents/templates/ADR_Template.md vs docs/prds/global/templates/agents/adr/ADR_Template.md
- [ ] Resolve duplicate Research Request templates: docs/agents/templates/Research_Request_Template.md vs docs/global/templates/Research_Request_Template.md
- [ ] Complete empty files: docs/raw/cost-of-manufacturing-offering-context.md (currently empty)
- [x] Populate APPROVED-GLOSSARY.md (currently minimal with only front matter) (RESOLVED: glossary is comprehensive with 99 lines of definitions)
- [x] Complete GBL-TKT_Best_Practices.md template (stops at line 77, incomplete sections) (RESOLVED: template is complete, goes to line 165)
- [ ] Clean up stranded TODOs in RSM call notes files (rsm-call-notes-documentation.md, rsm-call-notes-organized.md)
- [ ] Clean up stranded TODOs in LEG-63 work log (8 unchecked items in work-log/LEG-63-WORK-LOG.md)
- [ ] Clean up stranded TODOs in SLF-78 draft ticket (multiple unchecked items in SLF-78-boxwood-means-acquisition-exploration-draft.md)
- [x] Resolve template location confusion: decide whether templates belong in docs/agents/templates/ or docs/global/templates/ (RESOLVED: templates are in docs/agents/templates/, docs/global/templates/ doesn't exist)
- [ ] Update Decision Docket open decisions: ADR template structure and Research Request template format are now resolved
- [x] Standardize front matter across all templates (some missing required fields like created/updated timestamps) (RESOLVED: all templates have required fields)
- [x] Fix inconsistent directory structure: docs/prds/global/templates/agents/adr/ is overly nested (RESOLVED: directory doesn't exist, templates are in docs/agents/templates/)
- [ ] Complete missing template files referenced in docs/agents/templates/README.md but not found

## Blocked

- [ ] None currently

## Notes

- PRD templates are complete and ready for use
- Agent artifacts framework is planned but needs implementation
- Offboarding process is defined and ready for use

### 2025-10-02T00:00:00Z - repo-background-cleanup

- **[High | ~10-15 min]** Reconcile the "Repository Cleanup" backlog section to remove or mark the items already completed in earlier sessions so the open checklist matches current status.【F:docs/global/TODO_Log.md†L120-L143】
- **[High | ~10-15 min]** Surface the outstanding `/offboard` follow-up tasks from the 2025-10-01 handoff note in the main backlog (run pre-commit, fix link checker issues, verify rules links, dry-run commands).【F:docs/agents/session-notes/SN_20251001_agent-offboarding_handoff.md†L23-L28】
- **[High | ~15-20 min]** Decide how to differentiate or merge `glossary/APPROVED-GLOSSARY.md` and `glossary/INFORMAL-GLOSSARY.md` so only one canonical definition list remains, or establish a promotion workflow between them.【F:docs/global/glossary/APPROVED-GLOSSARY.md†L1-L104】【F:docs/global/glossary/INFORMAL-GLOSSARY.md†L1-L77】
- **[Medium | ~15 min]** Link the open deliverables in `docs/raw/cost-of-manufacturing-offering-context.md` to TODO_Log (or mark progress) so the research and draft checklist is tracked centrally.【F:docs/raw/cost-of-manufacturing-offering-context.md†L175-L188】
- **[Medium | ~15-20 min]** Capture the DoD tasks in `linear/tickets/drafts/excel-cost-analysis-funnel-integration.md` as actionable backlog items or update their status if work is finished.【F:linear/tickets/drafts/excel-cost-analysis-funnel-integration.md†L74-L82】
- **[Medium | ~10 min]** Add follow-up to resolve the "where does ad-hoc work go?" TODO in `linear/docs/How_to_use_Linear.md`, since the source file is read-only in this repo.【F:linear/docs/How_to_use_Linear.md†L146-L148】
- **[Low | ~20-30 min]** Consolidate overlapping cost context between `docs/raw/economics-cost-structure-initial-context.md` and `docs/raw/cost-of-manufacturing-offering-context.md` (clarify canonical source, merge or cross-link appropriately).【F:docs/raw/economics-cost-structure-initial-context.md†L1-L85】【F:docs/raw/cost-of-manufacturing-offering-context.md†L155-L188】
- **[Low | ~20-30 min]** Replace TBD placeholders in `docs/Deal_Structure_Model_Spec.md` fee table with current assumptions or document ownership for supplying the values.【F:docs/Deal_Structure_Model_Spec.md†L58-L66】

### Session: background-cleanup-audit-implementation (2025-01-27)

- [x] **HIGH PRIORITY - Naming Inconsistency Resolution** (5-10 min): Fix remaining GLB-TKT vs GBL-TKT references in linear/docs/How_to_use_Linear.md and linear/docs/templates/ticket-template.md
- [x] **HIGH PRIORITY - Stranded TODOs Cleanup** (10-15 min): Clean up TBD placeholders in SLF-78 draft ticket (super_initiative, initiative, project, milestone, requirement fields)
- [x] **MEDIUM PRIORITY - Template Location Confusion** (15-20 min): Resolve template location confusion - docs/agents/templates/ vs docs/global/templates/ - decide on single location and migrate
- [x] **MEDIUM PRIORITY - Incomplete Template Completion** (20-30 min): Complete GBL-TKT_Best_Practices.md template (currently stops at line 77, missing DoD tiers and implementation sections)
- [x] **MEDIUM PRIORITY - Directory Structure Cleanup** (10-15 min): Remove overly nested docs/prds/global/templates/agents/adr/ directory structure (currently empty)
- [x] **LOW PRIORITY - Empty File Population** (5-10 min): Populate APPROVED-GLOSSARY.md (currently minimal with only front matter)
- [x] **LOW PRIORITY - Cross-Reference Updates** (10-15 min): Update broken references to try-shortcut-prompt-style-guide.md in SLF-78 files
- [x] **LOW PRIORITY - Front Matter Standardization** (15-20 min): Standardize front matter across all templates (some missing required fields like created/updated timestamps)

## Session History

- **2025-01-27**: background-cleanup-audit - Comprehensive repository audit identifying 8 prioritized cleanup items including naming inconsistencies, stranded TODOs, template location confusion, and structural issues
- **2025-01-27**: repo-cleanup-analysis - Comprehensive repository analysis identifying 15 high-priority cleanup items including naming inconsistencies, duplicate templates, stranded TODOs, and structural issues
- **2025-01-27**: repo-cleanup - Fixed ISO dates, removed empty files, corrected broken links, renamed files to match IDs, fixed typos
- **2025-10-01**: workflow-finalization - Defined Background Agent Draft Review Workflow with ticket wizard integration, aligned with safety rules, created comprehensive documentation
- **2025-09-27**: PRD-Best-Practices-Definition - Defined PRD templates, front matter schema, and offboarding process

### 2025-10-02T04:05:19Z - background-cleanup-priority-refresh

- **HIGH (10-15 min)**: Reconcile conflicting status entries in this log—`Repository Cleanup` items remain unchecked even though matching tasks are marked completed above. Normalize the open sections and refresh carryover notes for clarity. 
- **HIGH (15-20 min)**: Promote the open `TBD` fee defaults and hierarchy placeholders in `docs/Deal_Structure_Model_Spec.md` into actionable tasks (or fill them) so the modeling spec is ready for implementation.
- **MEDIUM (15-20 min)**: Consolidate glossary sources—`docs/global/GLOSSARY.md` duplicates definitions from both Approved/Informal glossaries. Decide whether to merge or differentiate the files and align front matter statuses.
- **LOW (5-10 min)**: Clean stale backlog references (e.g., `docs/prds/global/templates/agents/adr/`) that point to non-existent directories or already-resolved template issues to avoid future confusion.
