---
id: GBL-GLS_Informal_Glossary
title: Informal Glossary
status: Draft
stage: Planning
owner: slittle
people: []
reviewers: []
approver: exec
priority: Medium
tags: [glossary, informal]

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
updated: 2025-09-27T16:30:00Z
version: 0.1.0

# Context & Relationships
related_docs: []
risk_level: Low
repo_only: true
---

# Informal Glossary

> Working terms captured quickly; promote to Approved once reviewed.

## Agent & Automation Terms

**Background Agent**: An AI agent that operates in the background to assist with personal work management, constrained by safety rules to only access Global To-Do project and specific directories.

**Ticket Wizard**: A 5-phase conversational workflow for creating comprehensive tickets, including triage, context collection, DoD definition, risk assessment, and output generation.

**Context Pack**: A curated collection of documents and information needed for a specific agent session or task, including required docs, allowed data, and session boundaries.

**Role Card**: A document defining an agent's purpose, scope, inputs/outputs, constraints, and success criteria.

**Playbook**: A step-by-step procedure for executing specific processes, including preconditions, steps with approval gates, and error handling.

## Document Types

**PRD**: Product Requirements Document - defines what to build and why, with two formats: Linear-aligned (team-prefixed) and repo-only (comprehensive).

**ADR**: Architecture Decision Record - documents important architectural decisions with context, options considered, and rationale.

**Session Note**: Documentation of an agent-assisted session, including objectives, steps taken, outputs, and decisions made.

**Decision Docket**: A rolling log of key decisions with rationale, maintained in `docs/global/Decision_Docket.md`.

## Workflow Terms

**DoD**: Definition of Done - typically structured as 3 tiers (Fast/Standard/Gold) with binary, evidence-backed checks.

**Global To-Do**: The Linear project (`to-do-and-planning-e2ce95344374`) where background agents can create and manage work items.

**SLF-73**: The Global Work Log Linear issue used for context, meeting notes, and reference materials.

**Draft Directory**: `linear/tickets/drafts/` where ticket drafts are created before review and Linear implementation.

## Safety & Process Terms

**Safety Checks**: Pre-operation validations that ensure agents only access allowed projects and directories.

**User Authorization**: Explicit approval required before agents can create Linear issues or perform write operations.

**Cross-Reference Pattern**: Standard way of linking work between SLF-73 (Global Work Log) and Linear issues using proper Linear formatting.

**Offboarding**: Process for properly closing agent sessions, including documentation, cleanup, and handoff preparation.
