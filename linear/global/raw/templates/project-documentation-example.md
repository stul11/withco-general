---
id: template_project_documentation_example
title: Project Documentation Example
status: Example
stage: Example
owner: example
people: []
reviewers: []
approver: example
priority: Example
tags: [template, documentation, project, example]

# Linear Hierarchy
team: [DATA/ANA]
super_initiative: "[Super Initiative Name]"
initiative: "[Initiative Name]"
project: "[Project Name]"
milestone: "[Current Milestone]"
requirement: "[Current Requirement]"
linear_issue_link: "[Primary Linear Issue]"

# Timestamps & Versioning
created: [ISO 8601 timestamp]
updated: [ISO 8601 timestamp]
version: [Semantic version]

# Context & Relationships
related_docs:
  - [Related document 1]
  - [Related document 2]
risk_level: [Low/Medium/High]
repo_only: true
---

# [Project Name] - Project Documentation

## Value Creation & Impact

### Primary Value Delivered

- **[Value Type]**: [Quantified impact] (e.g., "Lease processing from ~2 hours to ~15 minutes")
- **[Value Type]**: [Quantified impact] (e.g., "Risk reduction: 90% accuracy in lease data extraction")
- **[Value Type]**: [Quantified impact] (e.g., "Operational efficiency: 50% reduction in manual review time")

### Definition of Done (Value-Focused)

- **[Value Metric]**: [Specific threshold] (e.g., "Processing time ≤ 15 minutes per lease")
- **[Value Metric]**: [Specific threshold] (e.g., "Accuracy ≥ 90% on key lease fields")
- **[Value Metric]**: [Specific threshold] (e.g., "Coverage ≥ 95% of common lease types")

## Context

### What is it?

[Describe what this project is and what it does]

### Why is it important?

[Explain the business justification and importance]

## Existing Functionality

### v[1.0]

- [We take "as-reported" financial statements from Rutter]
- [We map the SMB's "chart of accounts" to a standardized chart of accounts using LLM]
- [We determine a cutoff date]
- [We calculate Year-to-Date annualized EBTDARM from the income statement]
- [We do a back of envelope calculation to determine cash balance at the end of the cutoff date year]
- [These items are inputs into plane of transactability]

## Existing Issues

### v[1.0]

- [No correction or corroboration of historical financials.]
- [If corrected and corroborated this logic is still bare minimum and was created defensively when we decided the customer product would show a calendar year]
- [SMB customers and capital partners may not be familiar with our chart of accounts schema]

## Ideal Functionality

- [To Be Updated - describe ideal state]

## Risks & Challenges

### [📘 **Financial Statement Structure & Scope**]

- [**Entity scope:** The financial statements may represent one or more legal entities or locations.]
- [**Statement timeliness:** The financial statements may not be up to date.]
- [**Business line segmentation:** We do not understand the segments of business lines and what is attributable to a specific location vs. other locations vs online.]
- [**Chart of accounts granularity:** The as-reported chart of accounts may not provide specificity into the items required to appropriately make adjustments for the EBTDAR calculation]
- [**Chart of accounts variability:** Chart of accounts may change over time.]

---

### [🧮 **Accounting Practices & Methodology**]

- [**Tax vs accounting basis:** Certain Capital Providers require tax driven calculations, vs. accounting statements]
- [**SBA reconciliation requirement:** The SBA requires a reconciliation between accounting and tax information.]
- [**Accrual compliance:** Financial statements may not on proper accrual accounting standards]
- [Obscures timing of revenue and expenses, especially for businesses with significant accounts receivable or payable]
- [**Inventory cost accuracy:** Accounting may be inaccurate or non-existent impacting costs of goods sold and gross margin calculations]
- [**Capitalization vs expensing:** Assets may be expensed instead of capitalized or vice versa. Or depreciation may not follow standard methods.]
- [**Fixed vs variable costs:** The as reported chart of accounts may not provide specificity into fixed versus variable costs]
- [**Income tax formation dependence:** Income taxes are dependent on the legal formation]

---

### [📉 **Reported Performance vs. Economic Reality**]

- [**Performance misreporting:** Businesses may misreport the performance of the business e.g., to minimize taxes]
- [**Non-market salaries:** Business owners may be taking a non-market salary]
- [**One-time items:** There may be one-time items in the historicals that do not reflect the "normalized" state of the business.]
- [**Non-recurring vs recurring:** When only looking at the financial statements, we don't understand the nature of recurring revenue, contracts, or the concentration of the customer base.]
- [**Personal expenses:** Owners may run personal or discretionary expenses through the business]
- [**Historical period limitations:** Whichever period we choose may not reflect the future state of the business]

---

### [💸 **Liabilities & Capital Structure**]

- [**Liabilities and equity unknowns:** We do not understand the nature and terms of the liabilities equity of the business]
- [**Unrecorded liabilities:** There may be unrecorded or contingent liabilities.]
- **Intercompany ambiguity:** Intercompany transactions may not be correctly accounted for, or opaque.

---

### [💳 **Revenue Recognition & Payment Systems**]

- [**POS revenue timing:** POS integration may obfuscate the timing of revenues]
- [**Embedded finance revenue:** Embedded Finance providers such as Stripe may cause revenues to be underreported and include embedded interest]
- [**Alternative payment timing:** Venmo or other similar payment systems may create lumpiness in revenue recognition]

---

### [🧠 **Data Reliability & Analysis Challenges**]

- [**Projection quality:** These are potential problems we may face dealing with stay deals, before taking into account]
  - [**Garbage in garbage out:** These problems create garbage in, garbage out issues for projecting future business performance.]
  - [**Data integration strategy:** We need to use a combination of 1P, 3P data, ML, business logic, and documents to minimize the effort required by an SMB or a capital provider arrive at an appropriate calculations with transparency]
    - [**Atomic integration path:** We may need to integrate into POS systems or build up from atomic accounting info to address these issues.]

---

## Relevant Data & Resources

[Add links to relevant data sources, documentation, and resources]

## Opportunities

### v[Next]

**Value Creation & Impact** - [Quantified value delivery and definition of done]
**User & Consumer Focus** - [Who benefits and how their flow improves]
**Success Metrics & Specifications** - [Accuracy, coverage, confidence, speed, ops touchpoints]
**Goal**: [Full integration between the backend (Athena and Oscilar) and the withco application (pluotos).]  
**Assumptions & inputs**:

- [Key assumptions]

**Explicitly out of scope**:

- [What's not included]

- [What's not included]

**Milestones**

- Goal: [What we want to achieve]
- Requirements:
  - [Requirements]
    **Solution outline**:
- [Solution outline]

### v[Next]

**Value Creation & Impact** - [Quantified value delivery and definition of done]
**User & Consumer Focus** - [Who benefits and how their flow improves]
**Success Metrics & Specifications** - [Accuracy, coverage, confidence, speed, ops touchpoints]
**Goal**: Full integration between the backend (Athena and Oscilar) and the withco application (pluotos).  
**Assumptions & inputs**:

- [Key assumptions]

- [Key assumptions]

**Explicitly out of scope**:

- [What's not included]

**Milestones**

- Goal: [What we want to achieve]
- Requirements:
  - [Requirements]
  - [Requirements]

**Solution outline**:

- [Solution outline]

## Wishlist

[Add items that would be nice to have but are not currently prioritized]

## Historical Work & Context

### Previous Iterations

- [v1 accomplishments]
- [Lessons learned]

### Related Work

- [Links to related projects]
- [Dependencies]

## Resources & Links

### Notion

### External Resources

- [Google Drive links]
- [Documentation links]
- [Research materials]

### Code & Technical Resources

- [Repository links]
- [API documentation]
- [Technical specifications]

### Open Questions

---

## Usage Instructions

### How to Use This Example

1. **Copy this example** to your project folder as `README.md`
2. **Replace all bracketed placeholders** with actual project information
3. **Fill in each section** based on available information
4. **Update regularly** as the project progresses
5. **Archive completed sections** in the `archive/` folder

### Required Sections

- **Value Creation & Impact**: Quantified value delivery and definition of done
- **User & Consumer Focus**: Who benefits and how their flow improves
- **Success Metrics & Specifications**: Accuracy, coverage, confidence, speed, ops touchpoints
- **Scope & Phasing**: V1 vs V2+ scope for 10/27 milestone
- **Operational Hooks & Human Correction**: Tools for correcting model outputs
- **Dependencies & Milestones**: Phased steps with dates for Gantt tracking

### Optional Sections

- Historical Work & Context (if applicable)
- Decision Log (for complex projects)
- Risk Assessment (for high-risk projects)
- Technical Implementation (for technical stakeholders)

### Maintenance Schedule

- **Weekly**: Update status and next steps
- **Monthly**: Review and update resources
- **Quarterly**: Comprehensive review and archive
