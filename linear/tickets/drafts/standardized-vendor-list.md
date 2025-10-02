# Standardized Vendor List & Cost Unit Scope Enums

**Created:** 2025-01-27T17:30:00Z  
**Status:** Draft v0.1  
**Purpose:** Authoritative vendor/service list with standardized enums for LEG-63 cost model

---

## 🏗️ **COST UNIT SCOPE ENUMS**

### **Primary Scopes**

| Enum                     | Definition                                     | Use Case                                      | Example                           |
| ------------------------ | ---------------------------------------------- | --------------------------------------------- | --------------------------------- |
| `PER_INVESTOR`           | Cost scales with number of investors           | KYC/AML, tax forms, investor communications   | $5 per investor for KYC/AML       |
| `PER_ASSET`              | Cost scales with number of properties/assets   | Property management, appraisals, insurance    | $2,500 per property for appraisal |
| `PER_OFFERING`           | Fixed cost per offering regardless of scale    | Reg A+ filing, legal structuring, audit setup | $50,000 for Reg A+ filing         |
| `PER_PRIMARY_OFFERING`   | Cost per primary (initial) offering            | Initial Reg A+, TA onboarding                 | $75,000 primary setup             |
| `PER_SECONDARY_OFFERING` | Cost per secondary offering / follow-on raises | Supplementary offering statement, marketing   | $25,000 per secondary raise       |
| `PER_TRANSACTION`        | Cost per individual transaction                | ACH transfers, DocuSign envelopes, escrow     | $0.25 per ACH transfer            |
| `PER_SMB`                | Cost per Small/Medium Business partner         | SMB onboarding, program management            | $10,000 per SMB onboarding        |
| `PER_PLATFORM`           | Platform-wide fixed cost                       | Platform infrastructure, compliance systems   | $100,000 annual platform license  |

### **Secondary Scopes**

| Enum         | Definition                            | Use Case                            | Example                  |
| ------------ | ------------------------------------- | ----------------------------------- | ------------------------ |
| `PER_API`    | Cost per API call to external service | Data services, credit checks        | $0.10 per API call       |
| `PER_YEAR`   | Annual recurring cost                 | Annual audits, compliance reporting | $25,000 annual audit fee |
| `PER_FILING` | Cost per regulatory filing            | SEC filings, state registrations    | $2,500 per SEC filing    |

### **Composite Scopes**

| Enum                              | Definition                      | Use Case                          | Example                       |
| --------------------------------- | ------------------------------- | --------------------------------- | ----------------------------- |
| `PER_INVESTOR_PER_YEAR`           | Annual cost per investor        | Ongoing investor management       | $50 per investor per year     |
| `PER_ASSET_PER_YEAR`              | Annual cost per asset           | Property management, insurance    | $1,000 per asset per year     |
| `PER_OFFERING_PER_YEAR`           | Annual cost per offering        | Ongoing compliance, reporting     | $15,000 per offering per year |
| `PER_PRIMARY_OFFERING_PER_YEAR`   | Annual cost per primary raise   | Ongoing Reg A+ compliance         | $20,000 per year              |
| `PER_SECONDARY_OFFERING_PER_YEAR` | Annual cost per secondary raise | Ongoing secondary compliance      | $10,000 per year              |
| `PER_PLATFORM_PER_YEAR`           | Annual cost per platform        | Platform infrastructure, licenses | $120,000 per year             |

### **One-time Composite Scopes**

| Enum                              | Definition                        | Use Case                        | Example                   |
| --------------------------------- | --------------------------------- | ------------------------------- | ------------------------- |
| `PER_INVESTOR_ONE_TIME`           | One-time cost per investor        | Initial KYC bundle              | $7 per investor one-time  |
| `PER_ASSET_ONE_TIME`              | One-time cost per asset           | Initial appraisal/survey        | $3,000 per asset one-time |
| `PER_OFFERING_ONE_TIME`           | One-time cost per offering        | Offering docs, EDGAR setup      | $50,000 one-time          |
| `PER_PRIMARY_OFFERING_ONE_TIME`   | One-time cost per primary raise   | Primary setup (TA onboarding)   | $75,000 one-time          |
| `PER_SECONDARY_OFFERING_ONE_TIME` | One-time cost per secondary raise | Follow-on offering statement    | $25,000 one-time          |
| `PER_PLATFORM_ONE_TIME`           | One-time cost per platform        | Initial platform implementation | $250,000 one-time         |

---

## 🏢 **STANDARDIZED VENDOR LIST**

### **Core Platform Vendors**

| Vendor            | Category                | Primary Services                      | Cost Unit Scope                 | Notes                     |
| ----------------- | ----------------------- | ------------------------------------- | ------------------------------- | ------------------------- |
| **North Capital** | Platform Infrastructure | White-label platform, investor portal | `PER_OFFERING` + `PER_INVESTOR` | Primary platform provider |
| **Oscilar**       | Compliance              | KYC/AML, investor verification        | `PER_INVESTOR`                  | Per-investor verification |
| **Enigma**        | Data Services           | Property data, market analytics       | `PER_API`                       | Data API calls            |
| **Baselayer**     | Infrastructure          | Cloud infrastructure, security        | `PER_PLATFORM`                  | Platform-wide service     |
| **Rutter**        | Financial Data          | Banking data aggregation              | `PER_API`                       | Financial data API        |
| **Extend**        | Document Management     | Document storage, retrieval           | `PER_TRANSACTION`               | Per document transaction  |
| **Cherre**        | Property Data           | Property intelligence, valuations     | `PER_API`                       | Property data API         |

### **Regulatory & Compliance**

| Vendor                         | Category             | Primary Services                | Cost Unit Scope                    | Notes                           |
| ------------------------------ | -------------------- | ------------------------------- | ---------------------------------- | ------------------------------- |
| **Transfer Agent**             | Investor Services    | Share registry, distributions   | `PER_INVESTOR` + `PER_TRANSACTION` | Per investor + per distribution |
| **EDGAR Service**              | SEC Compliance       | SEC filing, EDGAR submissions   | `PER_FILING`                       | Per SEC filing                  |
| **Auditor**                    | Financial Compliance | Annual audit, quarterly reviews | `PER_OFFERING_PER_YEAR`            | Annual audit per offering       |
| **REIT Compliance Accountant** | Tax Compliance       | REIT testing, tax compliance    | `PER_OFFERING_PER_YEAR`            | Annual REIT compliance          |
| **CRE Counsel**                | Legal Services       | Property legal, compliance      | `PER_OFFERING` + `PER_ASSET`       | Setup + per property            |

### **Property Services**

| Vendor                  | Category           | Primary Services                | Cost Unit Scope      | Notes                  |
| ----------------------- | ------------------ | ------------------------------- | -------------------- | ---------------------- |
| **Appraisal Vendors**   | Property Valuation | Property appraisals, valuations | `PER_ASSET`          | Per property appraisal |
| **Property Management** | Asset Management   | Day-to-day property management  | `PER_ASSET_PER_YEAR` | Annual per property    |
| **Special Servicer**    | Asset Management   | Distressed asset management     | `PER_ASSET`          | Per distressed asset   |
| **Insurance Providers** | Risk Management    | Property insurance, liability   | `PER_ASSET_PER_YEAR` | Annual per property    |

### **Technology & Operations**

| Vendor                     | Category            | Primary Services        | Cost Unit Scope   | Notes                        |
| -------------------------- | ------------------- | ----------------------- | ----------------- | ---------------------------- |
| **DocuSign**               | Document Management | Electronic signatures   | `PER_TRANSACTION` | Per signature transaction    |
| **ACH Providers**          | Payment Processing  | ACH transfers, payments | `PER_TRANSACTION` | Per ACH transaction          |
| **Credit Card Processors** | Payment Processing  | Credit card payments    | `PER_TRANSACTION` | Per credit card transaction  |
| **Data Centers**           | Infrastructure      | Server hosting, backup  | `PER_PLATFORM`    | Platform-wide infrastructure |

---

## 📊 **COST CARD SCHEMA v0.1**

### **Core Fields**

```yaml
cost_card:
  id: string # Unique identifier
  vendor: string # Vendor name
  service: string # Specific service description
  cost_unit_scope: enum # Primary cost unit scope
  secondary_scope: enum # Optional secondary scope
  unit_price: number # Price per unit
  minimum_commitment: number # Minimum quantity/amount
  step_tiers: array # Tiered pricing structure
  payer: enum # Who pays (Company, REIT, Investor, SMB)
  timing: enum # When paid (pre-close, at-close, ongoing)
  accounting: enum # Expensed vs capitalized
  amortization_period: number # If capitalized, amortization period
  scalability_note: string # What unlocks better pricing
  replacement_candidates: array # Alternative vendors
  switching_costs: number # Cost to switch vendors
  stage_activation: array # Which offering stages this applies to
  upreit_specific: boolean # UPREIT-specific cost
  llc_specific: boolean # LLC-specific cost
  reg_a_required: boolean # Required for Reg A+ compliance
```

### **Enums for Cost Card Schema**

```yaml
payer_options:
  - COMPANY
  - REIT
  - LLC
  - INVESTOR
  - SMB

timing_options:
  - AT_ONBOARDING
  - AT_IOI
  - AT_OFFERING
  - POST_CLOSE

timing_scope:
  - ONE_TIME
  - ANNUAL

accounting_options:
  - EXPENSED
  - CAPITALIZED

stage_activation_options:
  - IOI
  - COMMITTED_OFFERING
  - SPECIFIC_OFFERING
  - CLOSED_OFFERING
```

### **Cost Card Modeling Format (scales and outputs)**

```yaml
cost_card_model:
  # Standard scale points used for scenario tables
  scales:
    property_counts: [1, 10, 100, 1000]
    investor_counts: [100, 1000, 10000]
  # Base describes the contracted pricing terms for this cost card
  base:
    unit_scope: enum # e.g., PER_OFFERING, PER_ASSET, PER_INVESTOR, PER_PLATFORM, PER_PRIMARY_OFFERING
    timing_scope: enum # ONE_TIME | ANNUAL
    unit_price: number
    minimum_commitment: number
  # Derived outputs normalize any base into all reporting views below
  outputs:
    per_investor:
      per_year: # computed for each scale
        by_properties:
          { "1": number, "10": number, "100": number, "1000": number }
        by_investors: { "100": number, "1000": number, "10000": number }
      one_time:
        by_properties:
          { "1": number, "10": number, "100": number, "1000": number }
        by_investors: { "100": number, "1000": number, "10000": number }
    per_property:
      per_year:
        by_properties:
          { "1": number, "10": number, "100": number, "1000": number }
      one_time:
        by_properties:
          { "1": number, "10": number, "100": number, "1000": number }
    per_offering:
      per_year:
        by_properties:
          { "1": number, "10": number, "100": number, "1000": number }
      one_time:
        by_properties:
          { "1": number, "10": number, "100": number, "1000": number }
    per_platform:
      per_year:
        total: number
      one_time:
        total: number
  # Reference formulas (engine-agnostic) using n_properties, n_investors
  formulas:
    # Examples for converting any base to per-investor-per-year
    PER_OFFERING_PER_YEAR_to_PER_INVESTOR_PER_YEAR: "unit_price / n_investors"
    PER_ASSET_PER_YEAR_to_PER_INVESTOR_PER_YEAR: "(unit_price * n_properties) / n_investors"
    PER_PLATFORM_PER_YEAR_to_PER_INVESTOR_PER_YEAR: "unit_price / n_investors"
    PER_OFFERING_ONE_TIME_to_PER_INVESTOR_ONE_TIME: "unit_price / n_investors"
    PER_ASSET_ONE_TIME_to_PER_INVESTOR_ONE_TIME: "(unit_price * n_properties) / n_investors"
```

---

## 🔄 **STAGE ACTIVATION MAPPING**

### **Offering Lifecycle Stages**

| Stage                  | Description                         | Key Cost Categories               | Primary Vendors                        |
| ---------------------- | ----------------------------------- | --------------------------------- | -------------------------------------- |
| **IOI**                | Initial investor interest           | Platform setup, legal structuring | North Capital, CRE Counsel             |
| **Committed Offering** | Investor commitments                | KYC/AML, compliance setup         | Oscilar, Transfer Agent                |
| **Specific Offering**  | Specific property offering          | Property services, due diligence  | Appraisal Vendors, Property Management |
| **Closed Offering**    | Offering closed, ongoing management | Ongoing services, reporting       | Property Management, Auditor           |

### **Cost Allocation by Stage**

```yaml
stage_costs:
  IOI:
    - Platform setup (North Capital)
    - Legal structuring (CRE Counsel)
    - Initial compliance (EDGAR Service)

  COMMITTED_OFFERING:
    - Investor verification (Oscilar)
    - Transfer agent setup (Transfer Agent)
    - Reg A+ filing (EDGAR Service)

  SPECIFIC_OFFERING:
    - Property appraisal (Appraisal Vendors)
    - Due diligence (Cherre, Enigma)
    - Property management setup (Property Management)

  CLOSED_OFFERING:
    - Ongoing property management (Property Management)
    - Annual audit (Auditor)
    - Investor reporting (Transfer Agent)
```

---

## 🎯 **NEXT STEPS**

### **Immediate (Today)**

1. **Review Excel Model** - Map existing ~50 vendor rows to standardized list
2. **Validate Enums** - Ensure all cost unit scopes are captured
3. **Document Gaps** - NOTE missing vendors or services
4. **Prepare for Review** - Package for Brian/Kevin review tomorrow

### **Tomorrow (Post-Review)**

1. **Refine Schema** - Update based on review feedback
2. **Complete Mapping** - Full vendor/service mapping
3. **Cost Calculations** - Apply to UPREIT vs LLC analysis
4. **Two-Tiered Integration** - Integrate with LEG-9 minimum check work

---

## 📝 **ASSUMPTIONS & NOTES**

- **Pending Inputs**: RSM inputs (Sep 29), REIT compliance accountant (Minta/Goodwin)
- **Provisional**: This is v0.1 - will be refined based on review feedback
- **Scope**: Focus on Reg A+ offering compliance and two-tiered minimum structure
- **Integration**: Must work with existing Excel model and LEG-9 analysis

---

## 🔗 **REFERENCES**

- [LEG-63: Collect Cost of Manufacturing an Offering Inputs](https://linear.app/withco/issue/LEG-63/collect-cost-of-manufacturing-an-offering-inputs)
- [LEG-9: Determine Minimum Check Size](https://linear.app/withco/issue/LEG-9/determine-minimum-check-size)
- [Existing Excel Model](https://docs.google.com/spreadsheets/d/195wUpk6d5dZS61sf5MbemVhean0FWf5YK3o6v8nctlE/edit?usp=drive_link)
- `withco-general/docs/raw/economics-cost-structure-initial-context.md`
