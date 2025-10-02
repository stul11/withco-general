# TODO Log

- **Last Updated**: 2025-01-27T17:30:00Z
- **Session**: markdownlint-implementation
- **Owner**: slittle

## Completed

### Session: phase-04-implementation-1 (2025-10-02)

- [x] Resolve `.pre-commit-config.yaml` conflict; keep `sync-TODO-codelens` enabled <!-- id: TODO-20251002-211 -->
- [x] Add CI workflow to run lint, link, timestamp, and sidecar drift checks <!-- id: TODO-20251002-212 -->
- [x] Add docs/README and update docs/global/README with CodeLens usage <!-- id: TODO-20251002-213 -->
- [x] Add Session NOTE checklist to template and cross-link from AGENTS <!-- id: TODO-20251002-214 -->

### Session: codelens-to-do-integration (2025-10-02)

- [x] Update TODO template with stable ID and CodeLens guidance <!-- id: TODO-20251002-001 -->
- [x] Add `/TODO-add` behavior for ID assignment and sidecar sync <!-- id: TODO-20251002-002 -->
- [x] Add rule addendum for sidecar requirements <!-- id: TODO-20251002-003 -->
- [x] Wire pre-commit drift check for sidecars <!-- id: TODO-20251002-004 -->
- [x] Generate initial `docs/global/TODO.codelens.TODO` sidecar <!-- id: TODO-20251002-005 -->

### Session: python-data-analysis-rule-implementation (2025-01-27)

- [x] Create comprehensive Python data analysis cursor rule
- [x] Structure content following established workspace conventions
- [x] Include guidelines for pandas, matplotlib, seaborn, numpy, and Jupyter Notebooks
- [x] Add practical code examples and best practices
- [x] Create Session NOTE documenting implementation

### Session: uv-guidelines (2025-10-02)

- [x] Add `.cursor/rules/uv-guidelines.mdc` enforcing uv-only dependency management
- [x] Draft repo-wide uv compliance review plan: `docs/raw/plans/2025-10-02_uv-guidelines-compliance-review.md`
- [x] Create Session NOTE documenting decisions, findings, and next steps

### Session: markdownlint-phase2-3-implementation (2025-01-27)

- [x] Finalize .markdownlint.json baseline and .markdownlintignore entries
- [x] Apply staged fixes in docs/agents/templates with zero MD003/MD046/MD040
- [x] Resolve MD024 duplicates and safe MD013 wraps in templates
- [x] Apply staged fixes in docs/global with anchor-aware heading updates
- [x] Fix MD024/MD029 and add languages to code fences in global docs
- [x] Light-touch fixes in docs/agents/session-notes; prefer scoped disables
- [x] Apply pragmatic fixes in linear/docs and remaining markdown
- [x] Document custom rule decisions and when to use disable comments
- [x] Add GitHub Action to run markdownlint on PRs
- [x] Update contributor guide to require pre-commit install
- [x] Record remaining MD013 counts and exceptions per directory

### Session: markdownlint-implementation (2025-01-27)

- [x] Install markdownlint-cli globally
- [x] Create .markdownlint.json with relaxed initial rules
- [x] Add markdownlint to pre-commit hooks
- [x] Run markdownlint --fix on all existing files
- [x] Create cursor rules for markdown best practices
- [x] Create scripts/fix-markdown.sh command
- [x] Add VS Code settings for markdownlint integration
- [x] Test the complete markdownlint integration
- [x] Create comprehensive session NOTE documenting implementation
- [x] Update Decision Docket with markdownlint decision
- [x] Update TODO Log with completed items and potential future phases

### Session: 00-key-docs-creation (2025-01-27)

- [x] Create 00-key-docs directory at repository root
- [x] Add symlinks for Decision Docket and TODO Log
- [x] Commit changes with descriptive message
- [x] Verify symlink functionality and file explorer improvement
- [x] Create comprehensive session NOTE documenting file organization decision

### Session: repo-cleanup-and-merge (2025-01-27)

- [x] Review all commits and untracked files for commit readiness
- [x] Clean up Python virtual environment and cache files
- [x] Add .gitignore entries for Python cache files
- [x] Commit current changes with descriptive message
- [x] Merge all outstanding pull requests (#22, #23, #24)
- [x] Resolve merge conflicts in offboard command
- [x] Push all changes to origin/master
- [x] Clean up merged local branches
- [x] Create comprehensive session NOTE documenting all actions

### Session: sync-agent-rules (2025-10-02)

- [x] Review PR #19 and #20 for AGENTS sync automation
- [x] Set up Python virtual environment and run tests
- [x] Merge PR #20 (YAML parsing improvements) into base branch
- [x] Merge PR #19 (sync automation) into master
- [x] Verify master branch passes all tests and checks
- [x] Add follow-up items to TODO_Log.md
- [x] Create scripts/README.md documentation
- [x] Create requirements.txt for Python dependencies
- [x] Commit follow-up documentation changes

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
- [x] Create/Update session NOTE and stage changes for review
- [x] Fix broken markdown links across repo; add example ADR; commit changes

### Session: template-pt-1 (2025-10-01)

- [x] Add `/onboard-next-agent` command documentation
- [x] Create `docs/global/GLOSSARY.md`
- [x] Add ADR template (canonical location: `docs/agents/templates/ADR_Template.md`)
- [x] Add Research Request template (canonical location: `docs/agents/templates/Research_Request_Template.md`)
- [x] Update `docs/global/TODO_Log.md` to mark completed items

### Session: repo-cleanup-implementation (2025-01-27)

- [x] Fix naming inconsistency: GLB-TKT vs GBL-PRD prefixes (should be GBL-TKT for consistency)
- [x] Resolve duplicate ADR templates by consolidating on `docs/agents/templates/ADR_Template.md`
- [x] Resolve duplicate Research Request templates by consolidating on `docs/agents/templates/Research_Request_Template.md`
- [x] Complete empty files: docs/raw/cost-of-manufacturing-offering-context.md (currently empty)
- [x] Populate APPROVED-GLOSSARY.md (currently minimal with only front matter)
- [x] Complete GLB-TKT_Best_Practices.md template (stops at line 77, incomplete sections)
- [x] Clean up stranded TODOs in RSM call notes files (rsm-call-notes-documentation.md, rsm-call-notes-organized.md)
- [x] Clean up stranded TODOs in LEG-63 work log (8 unchecked items in work-log/LEG-63-WORK-LOG.md)
- [x] Clean up stranded TODOs in SLF-78 draft ticket (multiple unchecked items in SLF-78-boxwood-means-acquisition-exploration-draft.md)
- [x] Resolve template location confusion: decide whether templates belong in docs/agents/templates/ or docs/global/templates/
- [x] Update Decision Docket open decisions: ADR template structure and Research Request template format are now resolved
- [x] Standardize front matter across all templates (some missing required fields like created/updated timestamps)
- [x] Fix inconsistent directory structure by removing obsolete ADR subdirectories
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
- [x] Create session NOTE with offboarding checklist
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

### uv Migration (Planning → Implementation)

TODO

- [ ] Create `pyproject.toml` and initialize `uv.lock` with core tools
- [ ] Replace `pip` references in `scripts/README.md` with `uv` equivalents
- [ ] Decide policy for `requirements.txt` (generated via `uv export` vs deprecate)
- [ ] Add CI checks to block `pip`/`poetry` usage and encourage `uv`
- [ ] Document developer quickstart with `uv` commands

## Pending

### Next Agent Session (Awaiting User Approval)

TODO

- [x] Review and approve Background Agent Draft Review Workflow
- [x] Review Ticket Wizard Alignment documentation
- [ ] Test workflow with next background agent session
- [ ] Create test draft ticket using ticket wizard process (all 5 phases)
- [ ] Validate quality checks catch issues before Linear creation
- [ ] Apply process to existing draft tickets in linear/tickets/drafts/
- [ ] Migrate content between SLF-73 and To-Do project per defined process
- [ ] Create automation opportunities for workflow
- [ ] Monitor workflow effectiveness and gather feedback

### General Backlog

_Outstanding backlog work is grouped below. Recently-closed backlog items are cataloged in the "Backlog History" reference for traceability._

#### Open Work

- TODO: (PRD) [MED] Create LEG-PRD_Design_Economic_Transaction_Model.md from finalized template <!-- id: TODO-20251002-201 -->
  source: docs/global/GBL-PRD_Best_Practices.md#project-structure-requirements
  tags: prd, LEG

- TODO: (PRD) [MED] Create LEG-PRD_Design_Cost_of_Manufacturing_an_Offering.md from finalized template <!-- id: TODO-20251002-202 -->
  source: docs/global/GBL-PRD_Best_Practices.md#project-structure-requirements
  tags: prd, LEG

- TODO: (PRD) [MED] Create LEG-PRD_Determine_Minimum_Check_Size.md from finalized template <!-- id: TODO-20251002-203 -->
  source: docs/global/GBL-PRD_Best_Practices.md#project-structure-requirements
  tags: prd, LEG

- TODO: (AGENT) [LOW] Document folder and taxonomy expectations for docs/agents/templates/ <!-- id: TODO-20251002-204 -->
  source: docs/raw/plans/2025-10-02_document-categorization-and-workflows.md#2-directory-taxonomy-option-a-refined
  tags: taxonomy, templates

- TODO: (AGENT) [LOW] Document agent artifacts framework (Role Card, Context Pack, Playbook, ADRs) <!-- id: TODO-20251002-205 -->
  source: docs/agents/templates/Agent_Role_Card_Template.md
  tags: agents, templates

- TODO: (AGENT) [LOW] Define onboarding and offboarding checklists for agents <!-- id: TODO-20251002-206 -->
  source: .cursor/commands/offboard.md#behavior-what-the-agent-will-do
  tags: agents, workflows

- TODO: (AGENT) [LOW] Define session NOTE format and decision docket process <!-- id: TODO-20251002-207 -->
  source: .cursor/rules/agent-session-notes.mdc#required-actions
  tags: session-notes, docket

- TODO: (AGENT) [LOW] Prepare example Agent Role Card and Session NOTE <!-- id: TODO-20251002-208 -->
  source: docs/agents/templates/Agent_Role_Card_Template.md
  tags: examples, templates

- TODO: (PRD) [LOW] Publish agreed Best Practices into docs/global/GBL-PRD_Best_Practices.md <!-- id: TODO-20251002-209 -->
  source: docs/global/GBL-PRD_Best_Practices.md
  tags: prd, best-practices

- TODO: (AGENT) [MED] Consolidate reorganization Phase 01-02 session notes <!-- id: TODO-20251002-210 -->
  source: docs/agents/session-notes/SN_20251002-1045_reorganization-phase-1-2.md#session-NOTE
  tags: session-notes, cleanup
  notes: Merge the duplicate 10:45/10:52 entries and remove the empty 10:50 stub so one canonical NOTE remains.

- TODO: (AGENT) [LOW] Backfill Phase 02 sample items session notes <!-- id: TODO-20251002-211 -->
  source: docs/agents/session-notes/SN_20251002-1045_phase-02-sample-items.md#phase-02--sample-items
  tags: session-notes, templates
  notes: Populate the 10:45 and 10:56 placeholders with front matter + content or migrate them into the rollout plan hierarchy.

- TODO: (AGENT) [LOW] Standardize Phase 02 command docs check NOTE <!-- id: TODO-20251002-212 -->
  source: docs/agents/session-notes/SN_20251002-1045_phase-02-command-docs-check.md#phase-02--command-docs-check
  tags: session-notes, templates
  notes: Apply the session NOTE template (front matter, sections) so the checklist output is captured consistently.

- TODO: (AGENT) [LOW] Reformat Oct 02 markdownlint implementation NOTE <!-- id: TODO-20251002-213 -->
  source: docs/agents/session-notes/SN_20251002-0745_markdownlint-implementation.md#session-NOTE-markdownlint-implementation-and-fixes
  tags: session-notes, markdownlint
  notes: Add required front matter and align with the 2025-01-27 canonical NOTE instead of keeping a free-form narrative.

- TODO: (AGENT) [MED] Convert Phase 03 validation QA output into structured NOTE <!-- id: TODO-20251002-214 -->
  source: docs/agents/session-notes/SN_20251002-1135_phase-03-validation.md#phase-03--validation
  tags: session-notes, qa
  notes: Turn the raw link-check dump into a templated session NOTE or archive it under QA logs to avoid confusing readers.

- TODO: (AGENT) [LOW] Prevent drift in deprecated Linear ticket template copy <!-- id: TODO-20251002-215 -->
  source: linear/docs/templates/ticket-template.md#issue-title
  tags: templates, linear
  notes: Replace the deprecated duplicate with a minimal pointer or sync job so it cannot diverge from docs/templates/linear/ticket-template.md.

- TODO: (AGENT) [MED] Migrate Session NOTE template to canonical `docs/templates/session-NOTE.md`; update rule references; deprecate old path <!-- id: TODO-20251002-216 -->
  source: docs/raw/plans/2025-10-02_document-categorization-and-workflows.md#10-migration-plan-standard-and-gold
  tags: session-notes, templates, agents

<!-- moved to Completed in session phase-04-implementation-1 -->

#### Naming Conventions Rollout (New)

- [ ] (AGENT) [MED] Inventory existing NOTE files that don't match `*_YYYYMMDD-HHMM_slug.md` patterns
      source: docs/agents/session-notes/SN_20251002-0000_filename-preferences-global.md#next-actions
      tags: naming, session-notes
- [ ] (AGENT) [MED] Prepare Standard migration plan steps for renames and link updates
      source: docs/raw/plans/2025-10-02_document-categorization-and-workflows.md#10-migration-plan-standard-and-gold
      tags: naming, migration
- [ ] (AGENT) [MED] Run link checker and timestamp validator after renames to ensure integrity
      source: .cursor/commands/offboard.md
      tags: validation, links, timestamps

#### File Organization Enhancement Proposals (PROPOSALS - DO NOT IMPLEMENT)

- [ ] **[PROPOSAL]** Add `docs/README.md` with "Start here" navigation links to Decision Docket and TODO Log for GitHub/IDE discoverability
- [ ] **[PROPOSAL]** Convert symlinks to physical file moves: Move Decision Docket and TODO Log to `docs/` root and update all references repo-wide
- [ ] **[PROPOSAL]** Implement MkDocs/Docusaurus docs site with controlled navigation putting Decision Docket and TODO Log first in left-hand nav
- [ ] **[PROPOSAL]** Create `docs/00-global/` directory structure to surface global documents above agents/ in alphabetical listing
- [ ] **[PROPOSAL]** Add automated symlink validation in CI/CD to ensure symlinks remain functional across different environments
- [ ] **[PROPOSAL]** Create file organization ADR documenting canonical locations and access patterns for critical documents

#### Session Notes Workflow Enhancement Proposals (PROPOSALS - DO NOT IMPLEMENT)

- [x] **[PROPOSAL]** Fix `/offboard` command to list all 11 required session NOTE sections instead of just 5 (currently missing: Full Findings, Risks & Issues Identified, Reasoning & Rationale, Signoff)
- [ ] **[PROPOSAL]** Clarify `/granola-review` purpose: Should it create session notes or separate meeting notes? Currently conflates agent work sessions with meeting documentation
- [ ] **[PROPOSAL]** Create session NOTE categorization system: Agent Work Sessions vs Meeting Notes vs Process Documentation vs Research Sessions
- [x] **[PROPOSAL]** Add session NOTE validation checklist to ensure all required sections are populated before offboarding
- [ ] **[PROPOSAL]** Standardize session NOTE naming convention: Currently inconsistent between `SN_YYYYMMDD_` and `SN_YYYYMMDDHHMM_` patterns
- [ ] **[PROPOSAL]** Create session NOTE template variants for different use cases (agent work, meeting notes, research sessions)
- [ ] **[PROPOSAL]** Add session NOTE completeness scoring system to track quality and consistency over time
- [ ] **[High | ~10-15 min]** Run `pre-commit run --all-files` for the agent-offboarding staging area and capture any failing hooks before fixes.
- [x] **[High | ~15-20 min]** Resolve broken links identified in the agent-offboarding handoff (README offboarding link, SLF-78 try-shortcut references, workflow rule/template links) so link validation passes.
- [x] **[High | ~10-15 min]** Re-verify all `.cursor/rules/*` and `docs/agents/workflows/*` links after fixes to ensure navigation from rules to workflows succeeds.
- [ ] **[High | ~10-15 min]** Execute `/offboard --dry-run`, `/end-session --dry-run`, and `/onboard-next-agent --dry-run` to confirm the updated commands operate end-to-end.

#### Backlog History

- 2025-10-01: Created docs/global/GLOSSARY.md and added ADR / Research Request templates (see `template-pt-1` session summary).
- 2025-10-01: Captured LEG-PRD cost-input draft and background workflow updates (see `workflow-finalization` session summary).

> _The history entries retain context without re-opening completed tasks._

### Repository Cleanup (Resolved Scope)

_The dedicated cleanup backlog from the January 27 effort remains closed. Historical items are retained here for reference while the active backlog now focuses on new follow-ups._

- [x] Naming consistency and template consolidation confirmed closed in `repo-cleanup-implementation` (`docs/agents/session-notes/SN_20250127-0000_repo-cleanup-implementation.md:26`).
- [x] Stranded TODO sweeps across RSM, LEG-63, and SLF-78 remain resolved (`docs/agents/session-notes/SN_20250127-0000_repo-cleanup-implementation.md:45`).
- [x] Directory structure and obsolete file cleanup verified complete (`docs/agents/session-notes/SN_20250127-0000_repo-cleanup-implementation.md:51`).
- [x] 2025-10-02 background audit reconfirmed no open repository-cleanup backlog items; follow-up work now tracks under general backlog sections (`docs/agents/session-notes/SN_20251002-0000_repo-background-cleanup.md:45`).

## Potential Future Work (Staged Implementation Plan)

### Phase 2: Short-term (Next 2 Weeks) - Enhanced Integration

TODO

- [x] **Create cursor rules** for markdown best practices (COMPLETED in current session)
- [x] **Add VS Code settings** for team consistency (COMPLETED in current session)
- [x] **Implement staged fixing** (fix by directory)
- [x] **Add CI integration** for pull requests
- [ ] **Create custom rules** for project-specific needs
- [ ] **Integrate with Linear** ticket creation workflow
- [ ] **Add automated fixing** in CI/CD pipeline

### Phase 3: Long-term (Next Month) - Advanced Features

TODO

- [ ] **Custom rules** for your specific needs
- [ ] **Automated fixing** in CI/CD
- [ ] **Integration with Linear** ticket creation
- [ ] **Documentation generation** from linting results
- [ ] **Team training** on markdown best practices
- [ ] **Performance optimization** for large repositories
- [ ] **Integration with other tools** (Prettier, remark-lint, textlint)

### Alternative Implementation Options (Not Chosen)

TODO

- [ ] **remark-lint Integration** - Plugin-based markdown processor with 50+ linting plugins
- [ ] **textlint Integration** - Pluggable system with 100+ plugins for text issues
- [ ] **Mega-Linter Integration** - Runs 70+ linters simultaneously across all file types
- [ ] **SonarQube Integration** - Enterprise-grade code quality with 1000+ rules per language
- [ ] **Prettier + markdownlint Hybrid** - Prettier handles formatting, markdownlint handles content rules

## Blocked

- [ ] None currently

## Notes

- PRD templates are complete and ready for use; publish the finalized guidance via `GBL-PRD_Best_Practices.md` (tracked in General Backlog).
- Agent artifacts framework and onboarding/offboarding checklists remain open work items (see "General Backlog > Open Work").
- Offboarding process is defined and ready for use; `/offboard` follow-ups stay grouped under "Next Agent Session" for execution.

### 2025-10-02T00:00:00Z - repo-background-cleanup

TODO

- [x] **[High | ~10-15 min]** Reconcile the "Repository Cleanup" backlog section so the open checklist matches current status. (Resolved via "Repository Cleanup (Resolved Scope)" NOTE.)
- [ ] **[High | ~10-15 min]** Surface the outstanding `/offboard` follow-up tasks from the 2025-10-01 handoff NOTE in the main backlog (run pre-commit, fix link checker issues, verify rules links, dry-run commands).【F:docs/agents/session-notes/SN_20251001-0000_agent-offboarding_handoff.md†L23-L28】
- [ ] **[High | ~15-20 min]** Decide how to differentiate or merge `glossary/APPROVED-GLOSSARY.md` and `glossary/INFORMAL-GLOSSARY.md` so only one canonical definition list remains, or establish a promotion workflow between them.【F:docs/global/glossary/APPROVED-GLOSSARY.md†L1-L104】【F:docs/global/glossary/INFORMAL-GLOSSARY.md†L1-L77】
- [ ] **[Medium | ~15 min]** Link the open deliverables in `docs/raw/cost-of-manufacturing-offering-context.md` to TODO_Log (or mark progress) so the research and draft checklist is tracked centrally.【F:docs/raw/cost-of-manufacturing-offering-context.md†L175-L188】
- [ ] **[Medium | ~15-20 min]** Capture the DoD tasks in `linear/tickets/drafts/excel-cost-analysis-funnel-integration.md` as actionable backlog items or update their status if work is finished.【F:linear/tickets/drafts/excel-cost-analysis-funnel-integration.md†L74-L82】
- [ ] **[Medium | ~10 min]** Add follow-up to resolve the "where does ad-hoc work go?" TODO in `linear/docs/How_to_use_Linear.md`, since the source file is read-only in this repo.【F:linear/docs/How_to_use_Linear.md†L146-L148】
- [ ] **[Low | ~20-30 min]** Consolidate overlapping cost context between `docs/raw/economics-cost-structure-initial-context.md` and `docs/raw/cost-of-manufacturing-offering-context.md` (clarify canonical source, merge or cross-link appropriately).【F:docs/raw/economics-cost-structure-initial-context.md†L1-L85】【F:docs/raw/cost-of-manufacturing-offering-context.md†L155-L188】
- [ ] **[Low | ~20-30 min]** Replace TBD placeholders in `docs/Deal_Structure_Model_Spec.md` fee table with current assumptions or document ownership for supplying the values.【F:docs/Deal_Structure_Model_Spec.md†L58-L66】

### Session: background-cleanup-audit-implementation (2025-01-27)

- [x] **HIGH PRIORITY - Naming Inconsistency Resolution** (5-10 min): Fix remaining GLB-TKT vs GBL-TKT references in linear/docs/How_to_use_Linear.md and linear/docs/templates/ticket-template.md
- [x] **HIGH PRIORITY - Stranded TODOs Cleanup** (10-15 min): Clean up TBD placeholders in SLF-78 draft ticket (super_initiative, initiative, project, milestone, requirement fields)
- [x] **MEDIUM PRIORITY - Template Location Confusion** (15-20 min): Resolve template location confusion - docs/agents/templates/ vs docs/global/templates/ - decide on single location and migrate
- [x] **MEDIUM PRIORITY - Incomplete Template Completion** (20-30 min): Complete GBL-TKT_Best_Practices.md template (currently stops at line 77, missing DoD tiers and implementation sections)
- [x] **MEDIUM PRIORITY - Directory Structure Cleanup** (10-15 min): Remove obsolete ADR template directories to eliminate redundant nesting
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

TODO

- [x] **HIGH (10-15 min)**: Reconcile conflicting status entries in this log—`Repository Cleanup` items remain unchecked even though matching tasks are marked completed above. Normalize the open sections and refresh carryover notes for clarity.
- [ ] **HIGH (15-20 min)**: Promote the open `TBD` fee defaults and hierarchy placeholders in `docs/Deal_Structure_Model_Spec.md` into actionable tasks (or fill them) so the modeling spec is ready for implementation.
- [ ] **MEDIUM (15-20 min)**: Consolidate glossary sources—`docs/global/GLOSSARY.md` duplicates definitions from both Approved/Informal glossaries. Decide whether to merge or differentiate the files and align front matter statuses.
- [ ] **LOW (5-10 min)**: Clean stale backlog references (e.g., `docs/prds/global/templates/agents/adr/`) that point to non-existent directories or already-resolved template issues to avoid future confusion.

### 2025-10-02T05:12:00Z - background-cleanup-priority-refresh-rerun

TODO

- [x] **HIGH (10-15 min)**: Re-run the repository cleanup reconciliation to confirm the backlog reflects only open work and that carryover notes point to the refreshed sections.
- [ ] **MEDIUM (10-15 min)**: Review `Notes` and cross-reference sections to ensure future agents can quickly locate `/offboard` follow-ups and glossary consolidation tasks.

### 2025-10-02T05:50:00Z - pr-merge-followups

- [x] **LOW (5-10 min)**: Add scripts/README.md documenting `scripts/sync_agents_rules.py` usage and required dependencies (`pyyaml`) for new contributors.
- [x] **LOW (5-10 min)**: Create requirements.txt to pin Python tool versions and ease setup for contributors.

### 2025-10-02T06:10:00Z - granola-review-workflow-initial-implementation

TODO

- [x] Create docs-first paste-based Granola review workflow and command
- [x] Add normalization/safety rules and auto-detect one vs two paste blocks
- [x] Author workflow runbook and paste template; update linted docs
- [ ] Run a dry-run on sample content using `/granola-review <link> --write draft` and validate outputs
- [ ] (AGENT) [MED] Align /offboard required sections across commands
      source: docs/agents/session-notes/SN_20251002-0630_session-NOTE-template-analysis.md#immediate-actions
      tags: session-notes, templates
