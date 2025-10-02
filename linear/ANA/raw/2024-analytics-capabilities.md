---
id: raw_2024_analytics_capabilities
title: 2024 Analytics Capabilities
status: Raw
stage: Raw
owner: slittle
people: []
reviewers: []
approver: slittle
priority: Medium
tags: [raw, analytics, capabilities, 2024]

# Linear Hierarchy
team: ANA
super_initiative: "SMB UW"
initiative: "SMB UW"
project: "Analytics Capabilities"
milestone: "Capability Documentation"
requirement: "Document analytics capabilities"
linear_issue_link: "https://linear.app/withco/document/analytics-cababilities-18d19bdb81b2"

# Timestamps & Versioning
created: 2025-01-27T21:00:00Z
updated: 2025-01-27T21:00:00Z
version: 1.0.0

# Context & Relationships
related_docs:
  - https://linear.app/withco/document/analytics-cababilities-18d19bdb81b2
risk_level: Low
repo_only: true
---

# 2024 Analytics Capabilities

_Source: [Linear Document - Analytics Capabilities](https://linear.app/withco/document/analytics-cababilities-18d19bdb81b2)_

## Overview

This document captures the analytics capabilities as documented in Linear. The capabilities are organized by functional area and include descriptions of workflows and outputs.

## Capabilities Matrix

| Capability                                                    | Workflow | Description                                                                                                                                       |
| ------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| CRE Pricing (Observable)                                      |          | CRE Pricing including outputs tying to appraisal-compliant methodologies (comps, income cap, cost)                                                |
| CRE Pricing (Black Box)                                       |          | CRE Pricing without ouputs tying to appraisal-compliant methodologies (comps, income cap, cost)                                                   |
| Fundamental SMB Reported Financials                           |          | Accounting based as-reported SMB historical financials                                                                                            |
| Fundamental SMB Financials                                    |          | Accounting based SMB historical financials, mapped from as-reported line items to industry convention line items.                                 |
| Fundamental SMB Financials                                    |          | Accounting based SMB historical financials, mapped from as-reported journal entries and atomic accounting data to industry convention line items. |
| Fundamental SMB Financial Ratios                              |          | Financial metrics calculation based on 3 statements (income statement, b/s,                                                                       |
| SMB Integrations                                              |          | Payroll (zenefits, adp, gusto, rippling)                                                                                                          |
| SMB Integrations                                              |          | Bank (Plaid)                                                                                                                                      |
| SMB Integrations                                              |          | eCommerce / POS (square, amazon, shopify, stripe, toast)                                                                                          |
| Corporate Hierarchy Identity Resolution                       |          | Collecting and matching / resolving POIs to legal entities, Brands (e.g., DBA at the company level)                                               |
| Corporate Hierarchy and Ownership Graph                       |          | Collect and resolve parent child and affiliate corporate hierarchies and ownership to graph                                                       |
| SMB Capital Structure — Liabilities                           |          | Collect and resolve company debt and liabilities and security hierarchy to a capital structure.                                                   |
| SMB Capital Structure — Equity                                |          | Collect and resolve company ownership to people, and classes of ownership, along with major economic terms and rights                             |
| Lease Abstract                                                |          | Normalize lease documents to standard schema                                                                                                      |
| Lease Obligations Projections                                 |          | Generate contractual lease obligations from the normalized lease abstract                                                                         |
| Fundamental SMB Financials Resolution                         |          | Resolve multiple sources of historical information to accounting                                                                                  |
| Corporate Tax Parsing                                         |          | Collect and resolve tax filings                                                                                                                   |
| Corporate Tax Parsing Resolution                              |          | Resolve tax documents to accounting                                                                                                               |
| SMB Financial Budgets and Estimates                           |          | Collect and ingest, and calculate SMB financial estimates                                                                                         |
| SMB Financials Estimates                                      |          | View and compare multiple sources of estimates against eachother (internal models, customer projections, etc.)                                    |
| SMB Financials \[Refraction\] — Operating Segment             |          | Split SMB financials by operating segment                                                                                                         |
| SMB Financials \[Refraction\] — Location                      |          | Split SMB financials by location                                                                                                                  |
| SMB Financials Consolidation                                  |          | Consolidate SMB financials and capital structuress within the corporate hierarchy to parent-level financials                                      |
| Alternative Data SMB Revenue Estimates                        |          | Use foot-traffic, web-traffic, other data to generate top-line SMB revenue estimates                                                              |
| CRE Ownership Graph — Legal                                   |          | Determine and resolve legal entity ownership to corporate hierarchy graoph                                                                        |
| CRE Ownership Graph — Beneficial                              |          | Determine and resolve CRE ownership beneficial ownership to a person.                                                                             |
| CRE Beneficial Ownership Portfolio                            |          | Join CRE data to beneficial owners to determine size and location of portfolio                                                                    |
| Landlord Asset Distress Indicators                            |          | Identify loans approaching maturity, assets with vacancy, changes in ownership.                                                                   |
| Landlord Portfolio Distress Indicators                        |          | Identify beneficial ownership distressed by evaluating portfolio-level assets vs. obligations                                                     |
| Leasing Market Rent Estimates (Current & Forecast)            |          | Determine expected leasing rates                                                                                                                  |
| CRE Performance Resolution                                    |          | Resolve Listings and other data to determine occupancy and tenancy of assets                                                                      |
| Macro Index Data                                              |          | Injest key economic data for use in estimates and other financial calculations (e.g., interest rate curves)                                       |
| Company News / Events                                         |          | Module Description                                                                                                                                |
| Location News / Events                                        |          | \[TBU\]                                                                                                                                           |
| Lease Recommendation Tool                                     |          | Compare Lease Obligation Projections to Current Leasing Market Estimates, based on lease abstract termination / renewal / purcahse options.       |
| Personal Financial Integrations — Bank                        |          | Based on personal financial integrations and inputs, other documentation calculate a personal financial statement                                 |
| Personal Financial Integrations — Stocks & Wealth Mgmt        |          | \[TBU\]                                                                                                                                           |
| Personal Financial Statement                                  |          | \[TBU\]                                                                                                                                           |
| Overlay Financing Options on Projections                      |          | Based on user preferences and financing option projections, compare and recommend an option to SMB customer                                       |
| Financing Options Recommendation                              |          | Calculate cash flows and fiancial returns estimates.                                                                                              |
| Buildout, Equipment, Startout Cost Planner and Cost estimator |          | \[TBU\]                                                                                                                                           |
| SMB Comparable Comparison and Relative Value                  |          | Compare normalized SMB metrics against eachother                                                                                                  |
| Risk-Return & Expected Value + Scenarios                      |          | Proabability-weighted expected returns                                                                                                            |
| Potential Lender Match                                        |          | \[TBU\]                                                                                                                                           |

## Capability Categories

### Financial Analysis

- Fundamental SMB Reported Financials
- Fundamental SMB Financials (mapped)
- Fundamental SMB Financial Ratios
- SMB Financial Budgets and Estimates
- SMB Financials Estimates
- SMB Financials Refraction (Operating Segment, Location)
- SMB Financials Consolidation
- Alternative Data SMB Revenue Estimates

### Corporate Structure & Ownership

- Corporate Hierarchy Identity Resolution
- Corporate Hierarchy and Ownership Graph
- SMB Capital Structure (Liabilities, Equity)
- CRE Ownership Graph (Legal, Beneficial)
- CRE Beneficial Ownership Portfolio

### Real Estate & Leasing

- CRE Pricing (Observable, Black Box)
- Lease Abstract
- Lease Obligations Projections
- Leasing Market Rent Estimates
- CRE Performance Resolution
- Lease Recommendation Tool

### Data Integration & Resolution

- SMB Integrations (Payroll, Bank, eCommerce/POS)
- Fundamental SMB Financials Resolution
- Corporate Tax Parsing & Resolution
- CRE Performance Resolution

### Risk & Distress Analysis

- Landlord Asset Distress Indicators
- Landlord Portfolio Distress Indicators
- Risk-Return & Expected Value + Scenarios

### Personal Finance

- Personal Financial Integrations (Bank, Stocks & Wealth Mgmt)
- Personal Financial Statement

### Market & Economic Data

- Macro Index Data
- Company News / Events
- Location News / Events

### Financing & Recommendations

- Overlay Financing Options on Projections
- Financing Options Recommendation
- SMB Comparable Comparison and Relative Value
- Potential Lender Match

### Cost Planning

- Buildout, Equipment, Startout Cost Planner and Cost estimator

## Notes

- Several capabilities are marked as "\[TBU\]" (To Be Updated)
- Workflow column is currently empty for all capabilities
- This represents the state of analytics capabilities as of 2024
- Capabilities span across SMB underwriting, CRE analysis, and personal finance domains

## Related Documents

- [Linear Document - Analytics Capabilities](https://linear.app/withco/document/analytics-cababilities-18d19bdb81b2)
- SMB UW Initiative documentation
- Project documentation templates and examples
