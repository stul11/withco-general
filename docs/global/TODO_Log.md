# TODO Log

- **Last Updated**: 2025-10-02T21:10:00Z
- **Session**: todo-log-normalization
- **Owner**: slittle

## Completed

### Session: linear-documentation-v0 (2025-10-02)

- [x] Create ANA/DATA project documentation example template with placeholders (brackets) <!-- id: TODO-20251002-301 -->
- [x] Create grouped-by-meaning project glossary template and usage guidance <!-- id: TODO-20251002-302 -->
- [x] Update ANA/DATA plan to reference example by filename and add glossary to folders <!-- id: TODO-20251002-303 -->
- [x] Capture Linear analytics capabilities to repo as 2024 snapshot <!-- id: TODO-20251002-304 -->
- [x] Aggregate Notion analytics items into grouped index for ANA triage <!-- id: TODO-20251002-305 -->

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

- TODO: (WORKFLOW) [MED] Propose Cursor rules and helpful commands to enhance workflows <!-- id: TODO-20251002-217 -->
  source: docs/global/TODO_Log.md#in-progress
  tags: cursor, workflows
  notes: ICE-lite (Impact 3, Confidence 0.6, Effort 2) -> 0.9. Improves discoverability of automation helpers for agents.

### ANA Documentation Follow-Ups

- [ ] Triage Tier 1 items in `linear/ANA/raw/notion-all-ANA.md` (KEEP/REFINE/ARCHIVE) <!-- id: TODO-20251002-306 -->
- [ ] Apply example/glossary templates to an active ANA project README <!-- id: TODO-20251002-307 -->
- [ ] Fill TBU items in `linear/ANA/raw/2024-analytics-capabilities.md` and add review cadence <!-- id: TODO-20251002-308 -->

### uv Migration (Planning → Implementation)

- TODO: (DEV) [HIGH] Create `pyproject.toml` and initialize `uv.lock` with core tools <!-- id: TODO-20251002-218 -->
  source: docs/agents/session-notes/SN_20251002-1200_uv-guidelines.md#next-actions
  tags: uv, tooling, dependencies
  notes: ICE-lite (Impact 3, Confidence 0.7, Effort 2) -> 1.05. Establishes reproducible dependency baseline for CI and local work.
- TODO: (DOCS) [MED] Replace `pip` references in `scripts/README.md` with `uv` equivalents <!-- id: TODO-20251002-219 -->
  source: docs/agents/session-notes/SN_20251002-1200_uv-guidelines.md#full-findings
  tags: uv, documentation, tooling
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Eliminates conflicting guidance for dependency management.
- TODO: (POLICY) [HIGH] Decide policy for `requirements.txt` (generated via `uv export` vs deprecate) <!-- id: TODO-20251002-220 -->
  source: docs/agents/session-notes/SN_20251002-1200_uv-guidelines.md#next-actions
  tags: uv, governance, dependencies
  notes: ICE-lite (Impact 2, Confidence 0.5, Effort 1) -> 1.0. Clarifies whether legacy requirements stay generated or are retired.
- TODO: (CI) [MED] Add checks to block `pip`/`poetry` usage and encourage `uv` <!-- id: TODO-20251002-221 -->
  source: docs/agents/session-notes/SN_20251002-1200_uv-guidelines.md#next-actions
  tags: uv, ci, enforcement
  notes: ICE-lite (Impact 3, Confidence 0.6, Effort 3) -> 0.6. Prevents regressions toward unsupported package managers.
- TODO: (DOCS) [HIGH] Document developer quickstart with `uv` commands <!-- id: TODO-20251002-222 -->
  source: docs/agents/session-notes/SN_20251002-1200_uv-guidelines.md#next-actions
  tags: uv, onboarding, documentation
  notes: ICE-lite (Impact 2, Confidence 0.7, Effort 1) -> 1.4. Speeds onboarding with uv-first setup guidance.

## Pending

### Next Agent Session (Awaiting User Approval)

- TODO: (AGENT) [HIGH] Test Background Agent Draft Review Workflow end-to-end with a live session <!-- id: TODO-20251002-401 -->
  source: docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md#workflow-phases
  tags: workflow, ticketing
  notes: Run Phase 0–5 conversation flow and capture reviewer feedback before authorization.

- TODO: (AGENT) [HIGH] Create sample ticket using full ticket wizard conversation (all five phases) <!-- id: TODO-20251002-402 -->
  source: .cursor/rules/ticket-wizard.mdc#conversation-flow
  tags: ticket-wizard, training
  notes: Produce draft in `linear/tickets/drafts/` and log learnings for command docs.

- TODO: (AGENT) [MED] Validate ticket quality checks catch template regressions before Linear creation <!-- id: TODO-20251002-403 -->
  source: docs/agents/workflows/Ticket_Validator_Spec.md#quality-checks
  tags: validation, workflow
  notes: Dry-run `/ticket-validate` against updated drafts and document gaps.

- TODO: (AGENT) [MED] Apply Background Agent workflow to existing drafts in `linear/tickets/drafts/` <!-- id: TODO-20251002-404 -->
  source: docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md#phase-1-draft-creation-background-agent
  tags: cleanup, ticketing
  notes: Normalize legacy drafts to template before next review cycle.

- TODO: (AGENT) [MED] Migrate overlapping content between SLF-73 and To-Do project per new process <!-- id: TODO-20251002-405 -->
  source: docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md#phase-2-user-review-human
  tags: slf-73, backlog
  notes: Ensure single canonical location for RSM notes.

- TODO: (AGENT) [LOW] Identify automation opportunities for draft review workflow <!-- id: TODO-20251002-406 -->
  source: docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md#phase-4-linear-implementation-background-agent
  tags: automation, workflow
  notes: Capture safe tasks for future scripts (e.g., promote/validate bundling).

- TODO: (AGENT) [LOW] Monitor workflow effectiveness and gather user feedback <!-- id: TODO-20251002-407 -->
  source: docs/agents/workflows/Background_Agent_Draft_Review_Workflow.md#overview
  tags: feedback, workflow
  notes: Track reviewer satisfaction and backlog throughput after rollout.

- TODO: (AGENT) [MED] Confirm `/ticket-validate` passes on normalized drafts saved this session <!-- id: TODO-20251002-408 -->
  source: linear/tickets/drafts/excel-cost-analysis-funnel-integration.md#reviewer-checklist
  tags: ticket-audit, validation
  notes: Run validator and log any remaining schema mismatches.

- TODO: (AGENT) [MED] Update SLF-73 Global Work Log with summarized RSM notes once reviewed <!-- id: TODO-20251002-409 -->
  source: linear/tickets/drafts/rsm-call-notes-documentation.md#plan-small-steps
  tags: rsm, documentation
  notes: Cross-link action items and transcript references after human review.

- TODO: (AGENT) [MED] Review standardized vendor list with finance/legal for missing providers <!-- id: TODO-20251002-410 -->
  source: linear/tickets/drafts/standardized-vendor-list.md#open-questions
  tags: vendor-list, leg-63
  notes: Confirm primary vs backup designations and escalate pricing gaps.

- TODO: (AGENT) [LOW] Offer to run `scripts/todos/sync_codelens.py` after backlog edits <!-- id: TODO-20251002-411 -->
  source: scripts/todos/sync_codelens.py
  tags: tooling, backlog
  notes: Coordinate with owner before executing to keep Markdown and sidecar in sync.

### General Backlog

_Outstanding backlog work is grouped below. Recently closed backlog items are cataloged in the "Backlog History"
reference for traceability._

#### Open Work

- TODO: (PRD) [MED] Create LEG-PRD_Design_Economic_Transaction_Model.md from finalized template <!-- id: TODO-20251002-201 -->
  source: docs/global/GBL-PRD_Best_Practices.md#project-structure-requirements
  tags: prd, LEG
  notes: ICE-lite (Impact 3, Confidence 0.5, Effort 3) -> 0.5. Fills remaining PRD gap for LEG program economics.
- TODO: (PRD) [MED] Create LEG-PRD_Design_Cost_of_Manufacturing_an_Offering.md from finalized template <!-- id: TODO-20251002-202 -->
  source: docs/global/GBL-PRD_Best_Practices.md#project-structure-requirements
  tags: prd, LEG
  notes: ICE-lite (Impact 3, Confidence 0.5, Effort 3) -> 0.5. Captures core manufacturing workflows for LEG offering.
- TODO: (PRD) [MED] Create LEG-PRD_Determine_Minimum_Check_Size.md from finalized template <!-- id: TODO-20251002-203 -->
  source: docs/global/GBL-PRD_Best_Practices.md#project-structure-requirements
  tags: prd, LEG
  notes: ICE-lite (Impact 3, Confidence 0.5, Effort 3) -> 0.5. Supports pricing decisions tied to LEG investor intake.
- TODO: (AGENT) [MED] Document folder and taxonomy expectations for `docs/agents/templates/` <!-- id: TODO-20251002-204 -->
  source: docs/raw/plans/2025-10-02_document-categorization-and-workflows.md#2-directory-taxonomy-option-a-refined
  tags: taxonomy, templates
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Clarifies structure ahead of template migrations.
- TODO: (AGENT) [LOW] Document agent artifacts framework (Role Card, Context Pack, Playbook, ADRs) <!-- id: TODO-20251002-205 -->
  source: docs/agents/templates/Agent_Role_Card_Template.md
  tags: agents, templates
  notes: ICE-lite (Impact 2, Confidence 0.5, Effort 3) -> 0.33. Captures guidance for artifact families after taxonomy set.
- TODO: (AGENT) [HIGH] Define onboarding and offboarding checklists for agents <!-- id: TODO-20251002-206 -->
  source: .cursor/commands/offboard.md#behavior-what-the-agent-will-do
  tags: agents, workflows
  notes: ICE-lite (Impact 3, Confidence 0.6, Effort 2) -> 0.9. Establishes guardrails for lifecycle transitions.
- TODO: (AGENT) [HIGH] Define session NOTE format and Decision Docket process <!-- id: TODO-20251002-207 -->
  source: .cursor/rules/agent-session-notes.mdc#required-actions
  tags: session-notes, docket
  notes: ICE-lite (Impact 3, Confidence 0.6, Effort 2) -> 0.9. Aligns recordkeeping across notes and decision tracking.
- TODO: (AGENT) [LOW] Prepare example Agent Role Card and Session NOTE <!-- id: TODO-20251002-208 -->
  source: docs/agents/templates/Agent_Role_Card_Template.md
  tags: examples, templates
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 3) -> 0.4. Provides reference material once standards finalize.
- TODO: (PRD) [HIGH] Publish agreed best practices into `docs/global/GBL-PRD_Best_Practices.md` <!-- id: TODO-20251002-209 -->
  source: docs/global/GBL-PRD_Best_Practices.md
  tags: prd, best-practices
  notes: ICE-lite (Impact 3, Confidence 0.7, Effort 2) -> 1.05. Moves consensus guidance into canonical reference.
- TODO: (AGENT) [HIGH] Consolidate reorganization Phase 01-02 session notes <!-- id: TODO-20251002-210 -->
  source: docs/agents/session-notes/SN_20251002-1045_reorganization-phase-1-2.md#session-note
  tags: session-notes, cleanup
  notes: Merge duplicate 10:45/10:52 entries and remove the empty 10:50 stub so one canonical NOTE remains. ICE-lite (Impact 3, Confidence 0.7, Effort 1) -> 2.1.
- TODO: (AGENT) [MED] Backfill Phase 02 sample items session notes <!-- id: TODO-20251002-211 -->
  source: docs/agents/session-notes/SN_20251002-1045_phase-02-sample-items.md#phase-02--sample-items
  tags: session-notes, templates
  notes: Populate the 10:45 and 10:56 placeholders with template-complete content or migrate into rollout plan hierarchy. ICE-lite (Impact 2, Confidence 0.6, Effort 1) -> 1.2.
- TODO: (AGENT) [MED] Standardize Phase 02 command docs check NOTE <!-- id: TODO-20251002-212 -->
  source: docs/agents/session-notes/SN_20251002-1045_phase-02-command-docs-check.md#phase-02--command-docs-check
  tags: session-notes, templates
  notes: Apply the session NOTE template so checklist output is captured consistently. ICE-lite (Impact 2, Confidence 0.6, Effort 1) -> 1.2.
- TODO: (AGENT) [MED] Reformat Oct 02 markdownlint implementation NOTE <!-- id: TODO-20251002-213 -->
  source: docs/agents/session-notes/SN_20251002-0745_markdownlint-implementation.md#session-note-markdownlint-implementation-and-fixes
  tags: session-notes, markdownlint
  notes: Add required front matter and align with the 2025-01-27 canonical NOTE. ICE-lite (Impact 2, Confidence 0.6, Effort 1) -> 1.2.
- TODO: (AGENT) [MED] Convert Phase 03 validation QA output into structured NOTE <!-- id: TODO-20251002-214 -->
  source: docs/agents/session-notes/SN_20251002-1135_phase-03-validation.md#phase-03--validation
  tags: session-notes, qa
  notes: Turn the raw link-check dump into a templated session NOTE or archive under QA logs. ICE-lite (Impact 3, Confidence 0.6, Effort 2) -> 0.9.
- TODO: (AGENT) [MED] Prevent drift in deprecated Linear ticket template copy <!-- id: TODO-20251002-215 -->
  source: linear/docs/templates/ticket-template.md#issue-title
  tags: templates, linear
  notes: Replace deprecated duplicate with a pointer or sync job to avoid divergence. ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6.
- TODO: (AGENT) [MED] Migrate Session NOTE template to canonical `docs/templates/session-NOTE.md`; update rule references; deprecate old path <!-- id: TODO-20251002-216 -->
  source: docs/raw/plans/2025-10-02_document-categorization-and-workflows.md#10-migration-plan-standard-and-gold
  tags: session-notes, templates, agents
  notes: ICE-lite (Impact 3, Confidence 0.5, Effort 3) -> 0.5. Confirm completion status noted in phase-04 implementation follow-ups.

#### Naming Conventions Rollout (New)

- TODO: (AGENT) [MED] Inventory NOTE files that miss `*_YYYYMMDD-HHMM_slug.md` pattern <!-- id: TODO-20251002-230 -->
  source: docs/agents/session-notes/SN_20251002-0000_filename-preferences-global.md#next-actions
  tags: naming, session-notes
  notes: ICE-lite (Impact 2, Confidence 0.7, Effort 2) -> 0.7. Provides baseline for rename batches.
- TODO: (AGENT) [MED] Prepare Standard migration plan steps for renames and link updates <!-- id: TODO-20251002-231 -->
  source: docs/raw/plans/2025-10-02_document-categorization-and-workflows.md#10-migration-plan-standard-and-gold
  tags: naming, migration
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Outlines sequencing before large-scale renames.
- TODO: (AGENT) [MED] Run link checker and timestamp validator after renames <!-- id: TODO-20251002-232 -->
  source: .cursor/commands/offboard.md#behavior-what-the-agent-will-do
  tags: validation, links, timestamps
  notes: ICE-lite (Impact 2, Confidence 0.7, Effort 2) -> 0.7. Ensures migrations do not break automation.

#### File Organization Enhancement Proposals (PROPOSALS - DO NOT IMPLEMENT)

- TODO: (PROPOSAL) [LOW] Add `docs/README.md` with "Start here" navigation links to Decision Docket and TODO Log <!-- id: TODO-20251002-233 -->
  source: docs/agents/session-notes/SN_20250127-1745_00-key-docs-creation.md#inputs-context
  tags: proposal, docs, navigation
  notes: ICE-lite (Impact 2, Confidence 0.3, Effort 2) -> 0.3. Delivered in SN_20251002-1300_phase-04-implementation-1; confirm if further iteration needed.
- TODO: (PROPOSAL) [LOW] Convert symlinks to physical file moves for Decision Docket and TODO Log <!-- id: TODO-20251002-234 -->
  source: docs/agents/session-notes/SN_20250127-1745_00-key-docs-creation.md#full-findings
  tags: proposal, docs, migration
  notes: ICE-lite (Impact 2, Confidence 0.4, Effort 4) -> 0.2. Retained for discussion; symlink approach currently stable.
- TODO: (PROPOSAL) [LOW] Implement MkDocs/Docusaurus docs site with controlled navigation <!-- id: TODO-20251002-235 -->
  source: docs/agents/session-notes/SN_20250127-1745_00-key-docs-creation.md#full-findings
  tags: proposal, docs, platform
  notes: ICE-lite (Impact 3, Confidence 0.2, Effort 5) -> 0.12. Large scope; keep parked until lightweight needs emerge.
- TODO: (PROPOSAL) [LOW] Create `docs/00-global/` directory structure to surface global documents <!-- id: TODO-20251002-236 -->
  source: docs/global/TODO_Log.md#file-organization-enhancement-proposals
  tags: proposal, docs, navigation
  notes: ICE-lite (Impact 2, Confidence 0.3, Effort 3) -> 0.2. Alternative to symlinks; evaluate only if symlink friction appears.
- TODO: (PROPOSAL) [LOW] Add automated symlink validation in CI/CD <!-- id: TODO-20251002-237 -->
  source: docs/global/TODO_Log.md#file-organization-enhancement-proposals
  tags: proposal, ci, validation
  notes: ICE-lite (Impact 2, Confidence 0.4, Effort 3) -> 0.27. Future enhancement if symlink drift surfaces in audits.
- TODO: (PROPOSAL) [MED] Create file organization ADR documenting canonical locations <!-- id: TODO-20251002-238 -->
  source: docs/agents/session-notes/SN_20250127-1745_00-key-docs-creation.md#next-actions
  tags: proposal, docs, governance
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Provides governance artifact if re-org decisions escalate.

#### Session Notes Workflow Enhancement Proposals (PROPOSALS - DO NOT IMPLEMENT)

- [x] **[PROPOSAL]** Fix `/offboard` command to list all 11 required session NOTE sections instead of just 5 (currently missing: Full Findings, Risks & Issues Identified, Reasoning & Rationale, Signoff)
- [x] **[PROPOSAL]** Add session NOTE validation checklist to ensure all required sections are populated before offboarding
- TODO: (PROPOSAL) [MED] Clarify `/granola-review` purpose vs meeting documentation <!-- id: TODO-20251002-239 -->
  source: docs/agents/session-notes/SN_20251002-0630_session-note-template-analysis.md#full-findings
  tags: proposal, granola, session-notes
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Prevents command overlap between meeting notes and agent sessions.
- TODO: (PROPOSAL) [MED] Create session NOTE categorization system (agent work vs meetings vs research) <!-- id: TODO-20251002-240 -->
  source: docs/agents/session-notes/SN_20251002-0630_session-note-template-analysis.md#full-findings
  tags: proposal, session-notes, taxonomy
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Groups templates for different documentation modes.
- TODO: (PROPOSAL) [MED] Standardize session NOTE naming convention across commands <!-- id: TODO-20251002-241 -->
  source: docs/agents/session-notes/SN_20251002-0630_session-note-template-analysis.md#full-findings
  tags: proposal, naming, session-notes
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 1) -> 1.2. Coordinate with TODO-20251002-230 inventory to avoid duplicate effort.
- TODO: (PROPOSAL) [LOW] Create session NOTE template variants for different use cases <!-- id: TODO-20251002-242 -->
  source: docs/agents/session-notes/SN_20251002-0630_session-note-template-analysis.md#full-findings
  tags: proposal, session-notes, templates
  notes: ICE-lite (Impact 2, Confidence 0.5, Effort 3) -> 0.33. Defer until core template stabilized.
- TODO: (PROPOSAL) [MED] Add session NOTE completeness scoring system <!-- id: TODO-20251002-243 -->
  source: docs/agents/session-notes/SN_20251002-0630_session-note-template-analysis.md#full-findings
  tags: proposal, session-notes, qa
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Enables quality tracking once baseline template adoption improves.
- TODO: (QA) [MED] Run `pre-commit run --all-files` for agent-offboarding staging area and capture failing hooks <!-- id: TODO-20251002-244 -->
  source: docs/agents/session-notes/SN_20251001-0000_agent-offboarding_handoff.md#todo-log-update
  tags: offboarding, qa, pre-commit
  notes: ICE-lite (Impact 2, Confidence 0.7, Effort 1) -> 1.4. Provides failure log before applying fixes.
- TODO: (QA) [MED] Execute `/offboard --dry-run`, `/end-session --dry-run`, and `/onboard-next-agent --dry-run` <!-- id: TODO-20251002-245 -->
  source: docs/agents/session-notes/SN_20251001-0000_agent-offboarding_handoff.md#todo-log-update
  tags: offboarding, qa, automation
  notes: ICE-lite (Impact 2, Confidence 0.7, Effort 2) -> 0.7. Verifies updated commands function across lifecycle scenarios.

#### Backlog History

- 2025-10-01: Created docs/global/GLOSSARY.md and added ADR / Research Request templates (see `template-pt-1` session summary).
- 2025-10-01: Captured LEG-PRD cost-input draft and background workflow updates (see `workflow-finalization` session summary).

> _The history entries retain context without re-opening completed tasks._

### Repository Cleanup (Resolved Scope)

_The dedicated cleanup backlog from the January 27 effort remains closed. Historical items are retained here for
reference while the active backlog now focuses on new follow-ups._

- [x] Naming consistency and template consolidation confirmed closed in `repo-cleanup-implementation` (`docs/agents/session-notes/SN_20250127-0000_repo-cleanup-implementation.md:26`).
- [x] Stranded TODO sweeps across RSM, LEG-63, and SLF-78 remain resolved (`docs/agents/session-notes/SN_20250127-0000_repo-cleanup-implementation.md:45`).
- [x] Directory structure and obsolete file cleanup verified complete (`docs/agents/session-notes/SN_20250127-0000_repo-cleanup-implementation.md:51`).
- [x] 2025-10-02 background audit reconfirmed no open repository-cleanup backlog items; follow-up work now tracks under general backlog sections (`docs/agents/session-notes/SN_20251002-0000_repo-background-cleanup.md:45`).

## Potential Future Work (Staged Implementation Plan)

### Phase 2: Short-term (Next 2 Weeks) - Enhanced Integration

- TODO: (LINT) [MED] Create custom markdownlint rules for project-specific needs <!-- id: TODO-20251002-246 -->
  source: docs/agents/session-notes/SN_20250127-2030_markdownlint-phase2-3-implementation.md#next-actions
  tags: markdownlint, linting, customization
  notes: ICE-lite (Impact 3, Confidence 0.5, Effort 3) -> 0.5. Extends lint coverage to workspace-specific conventions.
- TODO: (INTEGRATION) [LOW] Integrate markdownlint workflow with Linear ticket creation <!-- id: TODO-20251002-247 -->
  source: docs/global/TODO_Log.md#potential-future-work-staged-implementation-plan
  tags: markdownlint, linear, automation
  notes: ICE-lite (Impact 3, Confidence 0.4, Effort 4) -> 0.3. High effort automation; defer until workflow maturity improves.
- TODO: (CI) [MED] Add automated markdownlint fixing in CI/CD pipeline <!-- id: TODO-20251002-248 -->
  source: docs/agents/session-notes/SN_20250127-2030_markdownlint-phase2-3-implementation.md#next-actions
  tags: markdownlint, ci, automation
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 3) -> 0.4. Provides safety net once rule set stabilizes.

### Phase 3: Long-term (Next Month) - Advanced Features

- TODO: (LINT) [LOW] Explore additional custom markdownlint rules beyond Phase 2 scope <!-- id: TODO-20251002-249 -->
  source: docs/global/TODO_Log.md#phase-3-long-term-next-month---advanced-features
  tags: markdownlint, linting
  notes: ICE-lite (Impact 2, Confidence 0.4, Effort 3) -> 0.27. Optional polish once baseline adoption is complete.
- TODO: (CI) [LOW] Evaluate automated fixing in CI/CD for advanced workflows <!-- id: TODO-20251002-250 -->
  source: docs/global/TODO_Log.md#phase-3-long-term-next-month---advanced-features
  tags: markdownlint, ci, automation
  notes: ICE-lite (Impact 2, Confidence 0.4, Effort 3) -> 0.27. Only proceed if Phase 2 automation proves stable.
- TODO: (INTEGRATION) [LOW] Prototype Linear ticket creation integration for markdownlint outputs <!-- id: TODO-20251002-251 -->
  source: docs/global/TODO_Log.md#phase-3-long-term-next-month---advanced-features
  tags: markdownlint, linear, automation
  notes: ICE-lite (Impact 2, Confidence 0.3, Effort 4) -> 0.15. Future automation concept pending user approval.
- TODO: (DOCS) [LOW] Generate documentation from markdownlint results <!-- id: TODO-20251002-252 -->
  source: docs/global/TODO_Log.md#phase-3-long-term-next-month---advanced-features
  tags: markdownlint, documentation, automation
  notes: ICE-lite (Impact 2, Confidence 0.4, Effort 3) -> 0.27. Nice-to-have reporting after adoption data exists.
- TODO: (TRAINING) [MED] Deliver team training on markdownlint best practices <!-- id: TODO-20251002-253 -->
  source: docs/agents/session-notes/SN_20250127-2030_markdownlint-phase2-3-implementation.md#risks-issues-identified
  tags: markdownlint, training
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Addresses adoption risk flagged in session note.
- TODO: (PERFORMANCE) [LOW] Optimize markdownlint performance for large repositories <!-- id: TODO-20251002-254 -->
  source: docs/agents/session-notes/SN_20250127-2030_markdownlint-phase2-3-implementation.md#risks-issues-identified
  tags: markdownlint, performance
  notes: ICE-lite (Impact 2, Confidence 0.5, Effort 3) -> 0.33. Monitor CI timings before investing.
- TODO: (INTEGRATION) [LOW] Assess integration with Prettier, remark-lint, or textlint <!-- id: TODO-20251002-255 -->
  source: docs/global/TODO_Log.md#phase-3-long-term-next-month---advanced-features
  tags: markdownlint, tooling, integration
  notes: ICE-lite (Impact 2, Confidence 0.4, Effort 3) -> 0.27. Evaluate only if markdownlint gaps remain.

### Alternative Implementation Options (Not Chosen)

- TODO: (ALTERNATIVE) [LOW] Evaluate remark-lint integration as future option <!-- id: TODO-20251002-256 -->
  source: docs/global/TODO_Log.md#alternative-implementation-options-not-chosen
  tags: markdownlint, alternative, tooling
  notes: ICE-lite (Impact 2, Confidence 0.3, Effort 3) -> 0.2. Keep as research spike if markdownlint limits emerge.
- TODO: (ALTERNATIVE) [LOW] Evaluate textlint integration for prose rules <!-- id: TODO-20251002-257 -->
  source: docs/global/TODO_Log.md#alternative-implementation-options-not-chosen
  tags: markdownlint, alternative, tooling
  notes: ICE-lite (Impact 2, Confidence 0.3, Effort 3) -> 0.2. Optional expansion for specialized text linting.
- TODO: (ALTERNATIVE) [LOW] Evaluate Mega-Linter for multi-language enforcement <!-- id: TODO-20251002-258 -->
  source: docs/global/TODO_Log.md#alternative-implementation-options-not-chosen
  tags: linting, ci, alternative
  notes: ICE-lite (Impact 2, Confidence 0.2, Effort 4) -> 0.1. Heavy-weight option reserved for future scale needs.
- TODO: (ALTERNATIVE) [LOW] Evaluate SonarQube integration for enterprise reporting <!-- id: TODO-20251002-259 -->
  source: docs/global/TODO_Log.md#alternative-implementation-options-not-chosen
  tags: linting, reporting, alternative
  notes: ICE-lite (Impact 2, Confidence 0.2, Effort 5) -> 0.08. Consider only with significant quality governance demand.
- TODO: (ALTERNATIVE) [LOW] Evaluate Prettier + markdownlint hybrid workflow <!-- id: TODO-20251002-260 -->
  source: docs/global/TODO_Log.md#alternative-implementation-options-not-chosen
  tags: markdownlint, formatting, alternative
  notes: ICE-lite (Impact 2, Confidence 0.3, Effort 3) -> 0.2. Future experiment if formatting pain resurfaces.

## Blocked

- [ ] None currently

## Notes

- PRD templates are complete and ready for use; publish the finalized guidance via `GBL-PRD_Best_Practices.md` (tracked in General Backlog).
- Agent artifacts framework and onboarding/offboarding checklists remain open work items (see "General Backlog > Open Work").
- Offboarding process is defined and ready for use; `/offboard` follow-ups stay grouped under "Next Agent Session" for execution.

### 2025-10-02T00:00:00Z - repo-background-cleanup

- TODO: (WORKFLOW) [MED] Surface outstanding `/offboard` follow-ups from 2025-10-01 handoff NOTE <!-- id: TODO-20251002-261 -->
  source: docs/agents/session-notes/SN_20251001-0000_agent-offboarding_handoff.md#todo-log-update
  tags: offboarding, backlog, cleanup
  notes: ICE-lite (Impact 3, Confidence 0.6, Effort 2) -> 0.9. Consolidates QA, link, and dry-run tasks into primary backlog.
- TODO: (GLOSSARY) [MED] Decide merge vs promotion workflow for Approved vs Informal glossaries <!-- id: TODO-20251002-262 -->
  source: docs/global/glossary/APPROVED-GLOSSARY.md#top
  tags: glossary, governance, docs
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Prevents duplicate definitions across glossary variants.
- TODO: (DOCS) [MED] Link cost-of-manufacturing deliverables into TODO Log <!-- id: TODO-20251002-263 -->
  source: docs/raw/cost-of-manufacturing-offering-context.md#open-items
  tags: manufacturing, backlog, docs
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Tracks research checklist centrally for visibility.
- TODO: (TICKETS) [MED] Capture DoD tasks from `excel-cost-analysis-funnel-integration.md` <!-- id: TODO-20251002-264 -->
  source: linear/tickets/drafts/excel-cost-analysis-funnel-integration.md#definition-of-done
  tags: tickets, backlog, cleanup
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Ensures draft DoD items receive owners or closures.
- TODO: (WORKFLOW) [MED] Resolve "where does ad-hoc work go?" follow-up from Linear doc <!-- id: TODO-20251002-265 -->
  source: linear/docs/How_to_use_Linear.md#faq-and-troubleshooting
  tags: linear, guidance, backlog
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 1) -> 1.2. Clarifies routing guidance for contributors using read-only doc.
- TODO: (DOCS) [LOW] Consolidate overlapping cost context files <!-- id: TODO-20251002-266 -->
  source: docs/raw/economics-cost-structure-initial-context.md#top
  tags: manufacturing, docs, cleanup
  notes: ICE-lite (Impact 2, Confidence 0.5, Effort 3) -> 0.33. Reduces duplication once canonical source determined.
- TODO: (DOCS) [LOW] Replace TBD placeholders in `Deal_Structure_Model_Spec.md` fee table <!-- id: TODO-20251002-267 -->
  source: docs/Deal_Structure_Model_Spec.md#fee-table
  tags: deal-structure, docs, data
  notes: ICE-lite (Impact 2, Confidence 0.5, Effort 3) -> 0.33. Improves readiness of modeling spec for downstream work.

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
- TODO: (DOCS) [MED] Promote `Deal_Structure_Model_Spec.md` TBD fee defaults into tasks <!-- id: TODO-20251002-268 -->
  source: docs/Deal_Structure_Model_Spec.md#fee-table
  tags: deal-structure, docs, cleanup
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Clarifies ownership for remaining fee placeholders.
- TODO: (GLOSSARY) [MED] Consolidate `GLOSSARY.md` with Approved/Informal sources <!-- id: TODO-20251002-269 -->
  source: docs/global/GLOSSARY.md#top
  tags: glossary, cleanup, docs
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Reduces duplication across glossary references.
- TODO: (BACKLOG) [LOW] Clean stale references to removed template directories <!-- id: TODO-20251002-270 -->
  source: docs/agents/session-notes/SN_20251002-0000_repo-background-cleanup.md#full-findings
  tags: cleanup, backlog, docs
  notes: ICE-lite (Impact 2, Confidence 0.5, Effort 1) -> 1.0. Keeps backlog pointers current after cleanup.

### 2025-10-02T05:12:00Z - background-cleanup-priority-refresh-rerun

TODO

- [x] **HIGH (10-15 min)**: Re-run the repository cleanup reconciliation to confirm the backlog reflects only open work and that carryover notes point to the refreshed sections.
- TODO: (BACKLOG) [MED] Review `Notes`/cross-references for `/offboard` and glossary visibility <!-- id: TODO-20251002-271 -->
  source: docs/agents/session-notes/SN_20251002-0000_repo-background-cleanup.md#next-actions
  tags: backlog, documentation, navigation
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 1) -> 1.2. Keeps quick-links accurate for next agent handoff.

### 2025-10-02T05:50:00Z - pr-merge-followups

- [x] **LOW (5-10 min)**: Add scripts/README.md documenting `scripts/sync_agents_rules.py` usage and required dependencies (`pyyaml`) for new contributors.
- [x] **LOW (5-10 min)**: Create requirements.txt to pin Python tool versions and ease setup for contributors.

### 2025-10-02T06:10:00Z - granola-review-workflow-initial-implementation

TODO

- [x] Create docs-first paste-based Granola review workflow and command
- [x] Add normalization/safety rules and auto-detect one vs two paste blocks
- [x] Author workflow runbook and paste template; update linted docs
- TODO: (WORKFLOW) [MED] Run `/granola-review <link> --write draft` dry-run on sample content <!-- id: TODO-20251002-272 -->
  source: docs/agents/session-notes/SN_20251002-0000_granola-review-workflow-initial-implementation.md#next-actions
  tags: granola, workflow, qa
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Validates workflow output before broader rollout.
- TODO: (AGENT) [MED] Align `/offboard` required sections across commands <!-- id: TODO-20251002-273 -->
  source: docs/agents/session-notes/SN_20251002-0630_session-note-template-analysis.md#immediate-actions
  tags: session-notes, templates
  notes: ICE-lite (Impact 2, Confidence 0.6, Effort 2) -> 0.6. Keeps command outputs consistent with template requirements.
