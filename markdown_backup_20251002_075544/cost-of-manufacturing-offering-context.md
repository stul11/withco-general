# Cost of Manufacturing an Offering - Context Document

**Created**: 2025-01-27T19:00:00Z  
**Last Updated**: 2025-01-27T19:00:00Z  
**Status**: Active Context  
**Owner**: slittle  
**Related**: LEG-63, Cost Structure Analysis

---

## Overview

**Canonical scope**: This document is the authoritative source for cost-of-manufacturing context, decisions, and vendor inventories. For the original intake narrative and broader economics planning brief, reference `/docs/raw/economics-cost-structure-initial-context.md`; summarize only major changes back there to keep the two files in sync.

This document provides comprehensive context for understanding the cost structure and economics of manufacturing Reg A+ offerings for small balance commercial real estate investments. This context supports the ongoing work on LEG-63 "Collect Cost of Manufacturing an Offering Inputs" and related economic modeling.

## Business Model Context

### Platform Structure

- **Vertical**: Small balance commercial real estate (1-10M properties)
- **Investment Vehicle**: Reg A+ (Tier II) crowdfunding platform
- **Target Users**: Small businesses (SMBs) as tenants, retail investors as capital providers
- **Innovation**: SMBs participate in property ownership and upside through innovative financial products

### Key Business Decisions Pending

1. **Structure Choice**: UPREIT vs Single LLC
2. **Minimum Check Size**: Impact on platform economics and investor accessibility
3. **Payment Rails**: ACH vs Credit Card cost implications
4. **Vendor Strategy**: Cost optimization across scale

## Cost Structure Framework

### Structure Comparison: UPREIT vs Single LLC

#### UPREIT Structure

- **Retail Investors**: REIT common interests with targeted 8% distribution (accrues if unpaid)
- **Withco Interests**: OP profit interests representing 20% of upside upon liquidation
- **SMB Interests**: OP profit interests representing up to 80% of upside, with incremental vesting over 10-year lease
- **Default Handling**: Unvested SMB upside reallocates to retail investors upon SMB default

#### Single LLC Structure

- **All Parties**: Retail investors, Withco, and SMB in single LLC
- **Tax Forms**: K-1 issuance per investor
- **Simpler Structure**: Lower upfront costs, higher ongoing investor filing costs

### Cost Categories

#### 1. Legal & Structuring Costs

- **Formation**: REIT + OP setup, profit interest plans, vesting schedules
- **Offering Documents**: Reg A+ Tier II documentation
- **Compliance**: REIT testing, ongoing legal maintenance
- **Scale Impact**: Fixed costs amortized across properties

#### 2. Technology Platform Costs

- **North Capital**: White-label investment platform (API, KYC/AML, escrow, e-sign)
- **Oscilar**: Risk and underwriting orchestration
- **Third-Party Data**: Enigma (KYB/Fimographic), Baselayer (KYB/Fraud/AML), Rutter (SMB cash flows)
- **Document Processing**: Extend (tax return parsing)
- **CRE Data**: Cherre (commercial real estate data)

#### 3. Regulatory & Compliance Costs

- **Reg A Audit**: Annual audit costs per offering
- **EDGAR Filing**: SEC filing service costs
- **Transfer Agent**: Investor management and communication
- **Tax Preparation**: 1099-DIV (REIT) vs K-1 (LLC) per investor
- **REIT Testing**: Ongoing compliance verification

#### 4. Property-Specific Costs

- **Appraisal**: CBRE/JLL restricted appraisals (Reg A complications)
- **Due Diligence**: Property Condition Reports, Environmental (Phase I/II), Zoning, Survey
- **Legal Transaction**: CRE counsel, lease documentation
- **Property Management**: Ongoing asset management
- **Insurance**: MSAs and brokerage (passed through to tenants)

#### 5. Investor Management Costs

- **KYC/AML**: Per-investor verification costs
- **Payment Processing**: ACH vs Credit Card fee differences
- **Investor Relations**: Support and communication costs
- **Distribution Management**: Cash flow distribution processing

## Scale Economics

### Cost Drivers by Scale

- **Per Investor**: KYC, tax forms, payment processing, IR support
- **Per Property**: Appraisal, due diligence, legal setup, property management
- **Per Transaction**: Offering costs, audit, EDGAR filing
- **Platform Fixed**: Technology infrastructure, compliance systems

### Break-Even Analysis

- **Minimum Check Size**: Function of per-investor costs vs acceptable yield drag
- **Property Economics**: Minimum deal size for platform viability
- **Investor Economics**: Gross-to-net yield impact of platform costs

## Vendor Landscape

### Current Contracts & Proposals

- **North Capital**: Signed contract for investment platform
- **Oscilar**: Signed contract for risk orchestration
- **Enigma**: Cost proposals for KYB/Fimographic data
- **Baselayer**: Cost proposals for KYB/Fraud/AML
- **Rutter**: Signed contract for SMB financial data
- **Extend**: Free tier for document parsing
- **Cherre**: Signed contract for CRE data

### Pending Vendor Decisions

- **Transfer Agent**: Budget allocated, vendor selection pending
- **Reg A Auditor**: Quote needed
- **EDGAR Service**: Quote needed
- **CRE Counsel**: National forms + local counsel strategy needed
- **Property Management**: In-house vs third-party decision pending

## Research Priorities

### Immediate Research Needs

1. **Two-Tiered Minimum Structures**: How platforms implement existing vs new investor tiers
2. **Cost Unit Scope Standardization**: Per SMB, Per Investor, Per Asset patterns
3. **Reg A+ Specific Costs**: Platform-specific cost patterns vs generic accounting
4. **Retail Platform Economics**: Cost structures across investor tiers

### Comparative Analysis

- **Arrived.com**: SFR fractional platform comparison
- **Mixed-Asset Platforms**: Fee structure benchmarks
- **REIT FinTech Hybrids**: Technology-enabled REIT models
- **Traditional Reg A Sponsors**: Cost structure precedents

## Decision Framework

### Key Metrics

- **Investor Net Yield**: Gross yield minus platform cost drag
- **Platform Margin**: Revenue minus cost of manufacturing
- **Minimum Viable Check Size**: Function of per-investor costs
- **Scale Break-Even**: Properties and investors needed for profitability

### Sensitivity Analysis

- **Structure Impact**: UPREIT vs LLC cost differences
- **Payment Rails**: ACH vs Credit Card cost implications
- **Scale Curves**: Cost reduction at 10/100/1k properties and 100/1k/10k investors
- **Vendor Swapping**: Cost optimization opportunities

## Implementation Context

### Current State

- **Excel Model**: Google Sheets with vendor data and cost calculations
- **Linear Integration**: LEG-63 work log and related tickets
- **Research Prompts**: Four research areas identified for ChatGPT analysis
- **Timeline**: Draft needed for Brian/Kevin review

### Next Steps

1. **Complete Cost BOM**: Comprehensive bill of materials for deal manufacturing
2. **Structure Decision**: UPREIT vs LLC comparison with full cost analysis
3. **Minimum Check Analysis**: Determine viable minimum check sizes
4. **Vendor Optimization**: Identify cost reduction opportunities
5. **Platform Economics**: Model platform-level profitability

## Related Documents

- **LEG-63 Work Log**: `/linear/tickets/work-log/LEG-63-WORK-LOG.md`
- **Economics Context**: `/docs/raw/economics-cost-structure-initial-context.md`
- **Research Prompts**: `/linear/tickets/drafts/research-prompts/`
- **Excel Model**: Google Sheets cost calculation model
- **RSM Call Notes**: RSM meeting insights and action items

## Key Assumptions

### High-Risk Assumptions (Need Validation)

- **A1**: RSM inputs available September 29
- **A2**: REIT compliance accountant identified by Minta/Goodwin
- **A3**: Current Excel model contains necessary vendor data
- **A4**: Two-tiered minimum structure is viable approach

### Business Assumptions

- **A5**: Reg A+ structure preferred over other investment vehicles
- **A6**: Small balance CRE (1-10M) is target market
- **A7**: SMB participation in upside is key differentiator
- **A8**: Technology-enabled platform provides cost advantages

## Success Criteria

### Immediate Deliverables

- [ ] Complete cost calculation draft for both UPREIT/LLC structures
- [ ] Key assumptions documented with pending inputs noted
- [ ] Draft ready for Brian/Kevin review
- [ ] Authoritative vendor/service list with enum mappings
- [ ] Provisional Cost Card schema v0.1

### Research Completion

- [ ] Two-tiered minimum structure analysis integrated
- [ ] Cost unit scope enums standardized
- [ ] Reg A+ offering cost patterns documented
- [ ] Retail investment platform cost structures analyzed

---

**Note**: This context document serves as the foundation for all cost-of-manufacturing analysis and should be updated as new information becomes available from RSM, vendor quotes, and research findings.
