# Research Prompt: Cost Unit Scope Enums and Standardization

## Objective

Research how investment platforms and financial services companies standardize cost unit scopes, particularly for real estate offerings and Reg A+ structures.

## Key Research Areas

### 1. Cost Unit Scope Categories

- **Per SMB** (Small/Medium Business)
- **Per Investor** (Individual investor basis)
- **Per Asset** (Property/asset basis)
- **Per Offering** (Entire offering basis)
- **Per Transaction** (Individual transaction basis)
- **Per Platform** (Platform-wide basis)

### 2. Standardization Patterns

- How do platforms categorize different cost types?
- What naming conventions are used?
- How are cost scopes defined and documented?
- What metadata is typically associated with cost scopes?

### 3. Real Estate Specific Considerations

- How do REITs structure cost allocations?
- What are common cost unit scopes for property management?
- How are offering costs allocated across assets?
- What about investor-specific costs vs. asset-specific costs?

### 4. Reg A+ Specific Patterns

- How do Reg A+ offerings typically structure costs?
- What are SEC requirements for cost disclosure?
- How do platforms handle cost allocation in offering documents?
- What are common cost unit scopes for compliance?

### 5. Platform Implementation

- How do platforms technically implement cost unit scopes?
- What database schemas are used?
- How are costs calculated and allocated?
- What reporting requirements exist?

## Specific Questions to Answer

1. **What are the most common cost unit scope categories used by investment platforms?**
2. **How do platforms handle costs that span multiple scopes (e.g., both per-investor and per-asset)?**
3. **What naming conventions and standards exist for cost unit scopes?**
4. **How do REITs specifically structure cost allocations?**
5. **What are the technical implementation patterns for cost unit scopes?**

## Expected Outputs

- **Standardized enum list** with definitions and use cases
- **Naming convention recommendations** for cost unit scopes
- **Implementation patterns** for cost allocation logic
- **REIT-specific considerations** for cost structuring
- **Technical schema recommendations** for cost unit scopes

## Context for Withco

- We have an existing Excel model with ~50 vendor/service rows
- Need to standardize Cost_Unit_Scope enums
- Supporting both UPREIT and LLC structures
- Must integrate with Cost Card schema v0.1
- Focus on Reg A+ offering compliance

## Research Depth

- **Primary sources**: Platform documentation, API schemas, offering documents
- **Secondary sources**: Industry standards, financial services documentation
- **Focus on**: Real estate investment platforms and REIT structures
- **Avoid**: Generic cost accounting that doesn't apply to investment platforms

## Technical Considerations

- **Database design** for cost unit scopes
- **API structure** for cost allocation
- **Reporting requirements** for different scopes
- **Integration patterns** with existing systems
- **Scalability considerations** for multiple offerings
