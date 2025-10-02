# PRD Best Practices

- **Date**: 2025-09-27
- **Status**: Draft
- **Owner**: slittle

## Overview

This document defines best practices for Product Requirements Documents (PRDs) at WithCo, including two distinct templates based on whether the PRD will be migrated to Linear or kept repo-only.

> Scope: Personal drafting best practices for PRDs in this repo. Do not modify company Linear documentation; use `../../docs/company/linear/How_to_use_Linear.md` as read-only reference for company workflow.

## PRD Types

### Linear-Aligned PRDs

- **Purpose**: PRDs that will be migrated to Linear projects/initiatives
- **Scope**: Follows Linear Project structure exactly
- **Naming**: Team-based prefix (e.g., `PROD-PRD_`, `AM-PRD_`, `SLF-PRD_`, `ANA-PRD_`, `DATA-PRD_`)
- **Flag**: `repo_only: false`

### Repo-Only PRDs

- **Purpose**: PRDs that remain in the repository only
- **Scope**: Comprehensive documentation with additional context sections
- **Naming**: Team-based prefix or `GBL-PRD_` for global docs
- **Flag**: `repo_only: true`

## Front Matter Schema

All PRDs must include the following front matter:

```yaml
id: [TEAM-PRD_Title]
title: PRD Title
status: Backlog | Draft | In Review | Approved | Deprecated
stage: Planning | In Progress | Done
owner: slittle
people: [designer, engineer_lead] # Key contributors beyond formal roles
reviewers: [legal, analytics]
approver: exec
priority: High | Medium | Low
tags: [economics, prd, modeling]

# Linear Hierarchy
team: Legal | Product | Analytics | Data | Shelf | Asset Management
super_initiative: "TBD"
initiative: "TBD"
project: "TBD"
milestone: "TBD"
requirement: "TBD"
linear_project_link: "https://linear.app/withco/project/..."

# Timestamps & Versioning
created: 2025-09-27T14:30:00Z
updated: 2025-09-27T15:00:00Z
version: 0.1.0

# Context & Relationships
related_docs:
  - withco-general/docs/global/GBL-PRD_Best_Practices.md
risk_level: High | Medium | Low
repo_only: true | false
```

## Template 1: Linear-Aligned PRD

Use this template for PRDs that will be migrated to Linear:

```markdown
---
id: PROD-PRD_Design_Economic_Transaction_Model
title: Design Economic Transaction Model
status: Draft
stage: Planning
owner: slittle
people: [designer, engineer_lead]
reviewers: [legal, analytics]
approver: exec
priority: High
tags: [economics, prd, modeling]

# Linear Hierarchy
team: Product
super_initiative: "TBD"
initiative: "TBD"
project: "TBD"
milestone: "TBD"
requirement: "TBD"
linear_project_link: "https://linear.app/withco/project/..."

# Timestamps & Versioning
created: 2025-09-27T14:30:00Z
updated: 2025-09-27T15:00:00Z
version: 0.1.0

# Context & Relationships
related_docs:
  - withco-general/docs/global/GBL-PRD_Best_Practices.md
risk_level: High
repo_only: false
---

# [PRD Title]

## Problem

- **User**: [Who is affected]
- **Core pain point**: [What problem are we solving]
- **Key risks**: [What could go wrong]
- **Why now?**: [Timing rationale]

## Solution

- **Goal**: [What does success look like when this PRD is complete]
- **Assumptions & inputs**: [What we're assuming and what we need]
- **Explicitly out of scope**: [What we're NOT doing]
- **Solution outline**: [High-level approach]
```

## Template 2: Repo-Only PRD

Use this template for comprehensive PRDs that remain in the repository:

```markdown
---
id: GBL-PRD_Agent_Artifacts_Framework
title: Agent Artifacts Framework
status: Draft
stage: Planning
owner: slittle
people: [designer, engineer_lead]
reviewers: [legal, analytics]
approver: exec
priority: High
tags: [agents, prd, framework]

# Linear Hierarchy
team: Product
super_initiative: "TBD"
initiative: "TBD"
project: "TBD"
milestone: "TBD"
requirement: "TBD"
linear_project_link: "TBD"

# Timestamps & Versioning
created: 2025-09-27T14:30:00Z
updated: 2025-09-27T15:00:00Z
version: 0.1.0

# Context & Relationships
related_docs:
  - withco-general/docs/global/GBL-PRD_Best_Practices.md
risk_level: Medium
repo_only: true
---

# [PRD Title]

## Problem

- **User**: [Who is affected]
- **Core pain point**: [What problem are we solving]
- **Key risks**: [What could go wrong]
- **Why now?**: [Timing rationale]

## Solution

- **Goal**: [What does success look like when this PRD is complete]
- **Assumptions & inputs**: [What we're assuming and what we need]
- **Explicitly out of scope**: [What we're NOT doing]
- **Solution outline**: [High-level approach]

## Context & Background

- [Additional context that doesn't fit in Problem/Solution]
- [Historical decisions or precedents]
- [External factors or constraints]

## Success Metrics

- [How we'll measure success]
- [Key performance indicators]
- [Acceptance criteria]

## Dependencies

- [What this PRD depends on]
- [What depends on this PRD]
- [External dependencies or blockers]

## Implementation Considerations

- [Technical considerations]
- [Resource requirements]
- [Timeline considerations]
- [Risk mitigation strategies]

## Open Questions

- [What we still need to figure out]
- [Decisions that need to be made]
- [Research needed]

## Appendix

- [Additional references]
- [Detailed technical specs]
- [Research findings]
```

## Naming Conventions

### Team-Based PRD IDs

- **PROD-PRD\_**: Product team PRDs
- **AM-PRD\_**: Asset Management team PRDs
- **LEG-PRD\_**: Legal team PRDs
- **SLF-PRD\_**: Shelf team PRDs
- **ANA-PRD\_**: Analytics team PRDs
- **DATA-PRD\_**: Data team PRDs
- **GBL-PRD\_**: Global/cross-team PRDs

### File Naming

- Store in `withco-general/docs/prds/`
- Use kebab-case for filenames: `PROD-PRD_Design_Economic_Transaction_Model.md`

## Workflow

1. **Create PRD**: Choose appropriate template based on whether it will be migrated to Linear
2. **Fill Front Matter**: Complete all required fields, set `repo_only` flag appropriately
3. **Write Content**: Follow the template structure for your chosen type
4. **Review Process**: Use the reviewers and approver fields to track review status
5. **Linear Migration**: For Linear-aligned PRDs, manually copy content to Linear and link back to Git

## Quality Checklist

- [ ] Front matter is complete and valid
- [ ] PRD ID follows team naming convention
- [ ] `repo_only` flag is set correctly
- [ ] Problem section clearly defines the user and pain point
- [ ] Solution section includes goal, assumptions, scope, and outline
- [ ] For repo-only PRDs: additional sections provide necessary context
- [ ] Related docs are linked appropriately
- [ ] Risk level is assessed and documented

## Related Documents

- [How to use Linear](../company/linear/How_to_use_Linear.md)
- [Agent Artifacts Plan](../../docs/agents/session-notes/SN_20251001-0730_agent-offboarding.md)
