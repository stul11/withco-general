---
id: GBL-GLS_Informal_Glossary
title: Informal Glossary Workflow
status: Active
stage: Operational
owner: slittle
people: []
reviewers: []
approver: exec
priority: Medium
tags: [glossary, informal, workflow]

# Linear Hierarchy
team: Product
super_initiative: "TBD"
initiative: "TBD"
project: "TBD"
milestone: "TBD"
requirement: "TBD"
linear_project_link: "TBD"

# Timestamps & Versioning
created: 2025-09-27T16:30:00Z
updated: 2025-01-27T19:00:00Z
version: 1.1.0

# Context & Relationships
related_docs:
  - docs/global/glossary/APPROVED-GLOSSARY.md
risk_level: Low
repo_only: true
---

## Informal Glossary Workflow

> Working space for capturing candidate terminology before it is promoted into the [Approved Glossary](./APPROVED-GLOSSARY.md).

## Purpose

The informal glossary holds **draft** definitions, feedback, and supporting references while a term is under review. It ensures we have a single canonical list (the approved glossary) while still giving contributors a lightweight place to propose or refine language.

## Promotion Steps

1. **Propose** a term in the working queue table below. Include a concise draft definition, links to source material, and who is sponsoring the addition.
2. **Review & Iterate** by tagging stakeholders or adding review notes in the `Feedback / Next Action` column. Clarify outstanding questions before promotion.
3. **Decision**:
   - When approved, move the definition into `APPROVED-GLOSSARY.md`, update the queue row status to `Approved`, and link to the canonical entry.
   - If rejected or deprioritized, update the status accordingly and capture rationale.
4. **Clean Up** after promotion by archiving resolved comments and ensuring the approved glossary version is incremented as part of the pull request.

## Working Terms Queue

| Term                                                 | Draft Definition | Status | Feedback / Next Action | Owner | Linkage |
| ---------------------------------------------------- | ---------------- | ------ | ---------------------- | ----- | ------- |
| _(add new rows below this line as proposals arrive)_ |                  |        |                        |       |         |

## Tips for Contributors

- Keep draft definitions short (1–2 sentences) and avoid duplicating content from the approved glossary.
- Use the `Linkage` column to reference Linear issues, docs, or meeting notes that justify the term.
- If a term affects multiple teams, tag representatives in the pull request and record their sign-off in the queue.

---

**Version**: 1.1.0  
**Last Updated**: 2025-01-27T19:00:00Z  
**Owner**: slittle  
**Reviewers**: Glossary Working Group
