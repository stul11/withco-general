---
id: Deal_Structure_Model_Spec
title: Deal Structure, Fees, and Modeling Inputs (SMB • Withco Manager • Investor)
status: Draft
stage: Planning
owner: slittle
people: []
reviewers: []
approver: KS
priority: High
tags: [modeling, deal-structure, fees, capital-accounts, nav]

# Linear Hierarchy
team: Product
super_initiative: "TBD"
initiative: "TBD"
project: "TBD"
milestone: "TBD"
requirement: "TBD"
linear_issue_link: "TBD"

# Timestamps & Versioning
created: 2025-10-01T00:00:00Z
updated: 2025-10-01T00:00:00Z
version: 0.1.0

# Context & Relationships
related_docs:
  - linear/tickets/drafts/excel-cost-analysis-funnel-integration.md
  - docs/raw/docs/withco-reit-and-op-high-level-term-sheet.md
  - docs/raw/docs/brian-email-to-mb.md
  - docs/raw/docs/fee_examples.md
risk_level: Medium
repo_only: true
---

## Purpose

Create a single reference for how we will model the offering economics across the three parties — SMB, Withco Manager, and Investor — including fees, Sources & Uses at close, ongoing costs, capital accounts, and a GAV/NAV calculator. This doc also defines the inputs we need to collect to operationalize the model on the `Funnel` sheet of the workbook `cost_of_manufacturing_offering_v3`.

## Parties & Entities

- SMB: Tenant/operating partner; may receive profit interests (up to 80% of upside) with vesting and forfeiture per lease compliance.
- Withco Manager: Management entity; receives profit interests (target 20% of upside) and may earn platform/management fees where applicable.
- Investor (Retail): REIT common interests; targeted distribution 8% that accrues if unpaid; principal and accrued prefs are senior in liquidation waterfall.
- Issuer structure (per latest term sheet): REIT issuer (Delaware LLC) with an Operating Partnership (OP). OP Units may be issued to property sellers; OP Units can convert to REIT common after seasoning.

## High‑Level Flow

1. Capital raised at the REIT; cash downstreamed to OP to acquire assets and fund uses at close.
2. Ongoing NOI and fees flow at OP/asset level. Cash distributable is upstreamed to REIT for investor distributions.
3. Capital accounts track each party’s contributed capital, accrued pref, distributions, and residual upside participation.

## Fees, Toggles, and Defaults

All fees can be toggled ON/OFF and parameterized. Unless noted, amounts are modeled at OP/asset level. See Fee Examples for market context.

| Fee                           | Toggle Key   | Default                  | Calc Base                           | Timing  | Paid By                  | Receives       | Accounting Treatment                                    |
| ----------------------------- | ------------ | ------------------------ | ----------------------------------- | ------- | ------------------------ | -------------- | ------------------------------------------------------- |
| Acquisition Fee               | fee_acq      | 1.00%                    | Purchase Price                      | Close   | OP/REIT                  | Withco Manager | Capitalized into S&U                                    |
| Offering & Organization (O&O) | fee_oo       | 3.00% cap at actual cost | Gross Proceeds                      | Close   | REIT                     | Manager/3P     | Capitalized; cap at cost                                |
| Investor Processing Fee       | fee_inv_proc | $X per investor (TBD)    | Per investor/event                  | Raise   | Investor (paid directly) | TA/3P          | Not capitalized to issuer; research gross→net treatment |
| Annual Asset Mgmt Fee         | fee_am       | 0.60%/yr                 | Purchase Price (or AUM policy, TBD) | Ongoing | OP/REIT                  | Withco Manager | Expense to OP (reduces NOI)                             |
| Monthly Property Mgmt Fee     | fee_pm       | e.g., 5%–8% EGI (TBD)    | EGI/NOI policy                      | Ongoing | OP/Asset                 | Manager/3P     | Expense to OP                                           |
| Disposition Fee (Internal)    | fee_disp_int | 1.00%                    | Gross Sale Price                    | Exit    | OP/REIT                  | Withco Manager | Reduces sale proceeds                                   |
| Disposition Fee (External)    | fee_disp_ext | Market broker % (TBD)    | Gross Sale Price                    | Exit    | OP/REIT                  | Broker         | Reduces sale proceeds                                   |

Notes

- Investor Processing Fee treatment varies by platform. Two modeling modes will be supported:
  - Mode A (excluded): Treat as investor‑paid, excluded from issuer proceeds and from gross→net return calc at the vehicle level (recommended default when investors pay third party directly).
  - Mode B (included as drag): Treat as reduction to investor gross proceeds for IRR calc or as an external investor‑level cash outflow tracked in “gross→net” bridges.

## Sources & Uses at Close (S&U)

S&U must attribute by party: Investor (REIT), Withco Manager, SMB. For reporting simplicity, cash sources are typically Investor equity (REIT), plus any SMB/Manager contributions if applicable. Uses include:

- Purchase Price (asset)
- Acquisition Fee (toggle `fee_acq`, capitalized)
- O&O Costs (toggle `fee_oo`, capitalized; capped at actual invoices)
- Reg/filing, escrow, transfer agent setup, legal (subset capitalized if directly attributable to the offering vehicle and meets capitalization policy)
- Working Capital/Reserves

Output tables:

- S&U by Party at Close (Investor/Manager/SMB columns)
- Per‑unit summary if needed (by investor, by SMB claim, etc.)

## Mapping Funnel Costs → S&U vs Ongoing

Use the `Funnel` sheet’s rows to assign each cost to:

- When Incurred: PLATFORM, ONBOARDING, ROADSHOW, OFFERING, SUCCESSFUL OFFERING, CLOSED OFFERING, POST CLOSE, DISPOSITION
- Recognition:
  - Capitalized to S&U at Close (if incurred pre‑close and policy allows, e.g., Acquisition Fee, Offering Docs/O&O, certain diligence)
  - Ongoing Expense (post‑close ops: property mgmt, transfer agent baseline, accounting, filings, etc.)
- Payer: SMB, Withco Manager, OP/REIT, Investor (direct)

Add the following helper columns on `Funnel` (no new sheets):

- `Who_Pays` ∈ {SMB, Withco_Manager, Investor, OP/REIT}
- `Recognition` ∈ {Capitalized_Close, Ongoing}
- `Toggle_Key` (link to fee table where applicable)
- `When_Incurred` (existing) and `Cumulative_Flag` (for reporting)

## Capital Accounts (by Party)

Track a separate capital account ledger for each party.

- Investor Capital Account (REIT)
  - Begins with contributions; accrues preferred return (target 8% simple accrual unless/until policy set otherwise); decreases with distributions; settles at liquidity events before upside splits.
- Withco Manager Capital/Carry Ledger
  - Tracks any contributed capital (if any), fees earned (as income, not capital), and participation in upside via profit interests (target 20%).
- SMB Capital/Carry Ledger
  - Tracks any contributed capital (if any) and profit interests up to 80% subject to vesting (6‑month increments; forfeiture on default). Include accelerated participation logic for interim follow‑on offering, then reset vesting per term sheet concept.

Recommended columns

- `opening_balance`, `contributions`, `pref_accrual`, `distributions`, `closing_balance`
- For SMB/Manager: `vested_carry_pct`, `unvested_carry_pct`, `carry_realized`, `carry_remaining`

Preferred Return Accrual

- Annual target example: 8% accrues if unpaid. Implement monthly/quarterly accrual consistent with investor distribution cadence. Include a gross→net bridge to reflect any investor‑level drags (processing fees, if Mode B).

## GAV / NAV Calculator

Assume periodic appraisal determines FMV.

- GAV = Appraised FMV of property(ies) + Cash + Other Operating Assets
- Liabilities = Debt + Accrued payables + Deferred O&O reimbursement (if any)
- NAV (Vehicle) = GAV − Liabilities
- NAV per Unit = NAV / Units Outstanding (REIT share count or OP units as applicable)

Assumption: Cash distributable is sent up to the REIT before measuring investor distributions.

Inputs needed

- Latest appraisal value per asset
- Cash balance (OP and REIT, to avoid double counting)
- Outstanding debt principal and accrued interest
- Accrued but unpaid expenses/fees
- Units outstanding (REIT and any OP unit classes)

## Property Improvements (CapEx) Framework

Track CapEx projects and who funded them. Default behavior does not credit SMB’s capital account; provide a toggle to enable SMB crediting when SMB pays.

Data fields (add to `Funnel` rows or a dedicated CapEx block on `Funnel`):

- `Improvement_ID`, `Description`, `Date`, `Amount`, `Category` (e.g., TI, equipment, build‑out), `Payer` ∈ {SMB, Withco_Manager, OP/REIT}, `Capitalized_Flag` (default TRUE), `Useful_Life` (if depreciation tracked elsewhere)

Toggles and mechanics

- `toggle_credit_smb_capex` (default FALSE): if TRUE and `Payer=SMB`, then increase SMB capital account by `Amount` at payment date; if FALSE, treat as off‑book to vehicle capital accounts (still optionally reflected in gross→net or SMB side ledger).
- Include CapEx in GAV as part of asset book where capitalized; ensure cash source is modeled (follow‑on equity, operating cash, or SMB payor).

Outputs

- CapEx roll‑forward by payer and cumulative; reconciliation to S&U (if at close) and to NAV (if post close).

## Follow‑On Offering (Appraisal‑Triggered Framework)

Assume a follow‑on can be triggered based on a fresh appraisal that sets NAV per unit. Proceeds may fund property improvements, distributions, or growth.

Inputs/controls

- `toggle_follow_on_enabled` (TRUE/FALSE)
- `follow_on_date`
- `follow_on_raise_target` (absolute or % of NAV)
- `issue_price_policy` (NAV per unit at appraisal, or premium/discount %) and `issue_costs` (brokerage/filing if any)

Mechanics

- Compute NAV/unit from GAV/NAV section at `follow_on_date`.
- Determine units to issue = `net_proceeds / issue_price`.
- Update cap table and capital accounts (Investor) for new contributions; allocate proceeds to CapEx, working capital, or distributions per policy.
- If SMB vesting acceleration applies at interim event, update `vested_carry_pct` per policy and reset vesting schedule thereafter.

Validation

- Units outstanding before/after reconcile; S&U for the event ties to cash movement; NAV/unit impact shown pre/post.

## Investor Tax Modeling (Before vs After‑Tax)

Model end‑investor returns on both pre‑tax and after‑tax bases.

Inputs

- `tax_marginal_rate_ordinary` (e.g., 37%)
- `tax_rate_qualified_dividends` (if applicable)
- `tax_rate_capital_gains`
- `taxable_portion_of_distributions` (policy or estimate; portion of distribution taxed vs return of capital)
- `tax_basis_initial` and basis adjustments from return of capital

Mechanics

- For each distribution period: split distribution into taxable portion and return of capital based on policy; compute tax outflow using applicable rate; reduce investor basis for return of capital.
- On disposition: compute capital gain = proceeds − adjusted basis; apply `tax_rate_capital_gains`.
- Produce two cash flow series at investor level: `pre_tax_cf` and `after_tax_cf = pre_tax_cf − tax_outflows`.
- Report IRR and MOIC for both series; show gross→net bridge including fee drags (if Mode B selected for investor processing fees).

Validation

- Basis never below zero (unless policy allows and tracks negative basis); sum of taxable + ROC equals total distributions.

## Inputs Checklist (to model in `Funnel`)

- For each cost row: `Cost Group`, `Cost Item`, `Cost/Unit`, `Event Scope`, `Funnel Stage`, `Funnel Event Volume`
- Helper fields to add/confirm: `Who_Pays`, `Recognition`, `Toggle_Key`
- Fee parameters (can be constants or named cells):
  - Acquisition Fee rate
  - O&O % cap and invoice total
  - Investor Processing Fee per investor (and Mode A vs Mode B selection)
  - Asset Mgmt Fee base policy (Purchase Price vs AUM) and rate (default 0.60%)
  - Property Mgmt Fee policy (EGI% or tariff) and rate(s)
  - Disposition fee(s) rate(s) and internal/external toggle
- Capital account settings: investor pref rate, compounding convention, distribution priority
- Appraisal and balance sheet inputs for GAV/NAV

Additional inputs for new frameworks

- CapEx: project attributes, payer, capitalization flag, SMB credit toggle
- Follow‑on: trigger date, raise target, pricing policy, issuance costs
- Taxes: investor tax rates, taxable distribution portion policy, initial basis

## Excel Implementation Notes (on `Funnel` only)

- Per‑event costs: `Cost_Per_Event = Cost_Per_Unit × Event_Volume`
- When `Recognition=Capitalized_Close`, aggregate into S&U by party.
- When `Recognition=Ongoing`, aggregate into period P&L and reduce available cash flow for distributions.
- Toggles: Use named cells (TRUE/FALSE) like `toggle_fee_acq`, `toggle_fee_oo`, etc., and drive formulas with `IF(toggle, calc, 0)`.
- Reporting views: `When Incurred` vs `Cumulative` controlled by a named toggle; use running sums for cumulative.

CapEx and Follow‑On on `Funnel`

- Add a CapEx block (rows) with payer and toggle‑driven SMB crediting; aggregate into GAV and (if funded by follow‑on) tie to event S&U lines.
- Follow‑on calculations: compute NAV/unit, units issued, and update totals via named ranges; avoid new sheets.

## Gross → Net Considerations (Investor Processing Fee)

Research path

- Examine Fee Examples (`docs/raw/docs/fee_examples.md`) for TA/processing norms.
- Compare Arrived (TA/processing charged to platform/manager vs series) and Fundrise/RealtyMogul disclosures.

Modeling recommendation

- Default Mode A (excluded): Do not reduce issuer gross proceeds; treat as a separate investor‑level outflow for personal IRR if needed.
- Provide Mode B (include as drag) as an alternate view; show sensitivity on net to investors and pref accrual timing.

## Validation Checks

- Tie‑outs: S&U Uses = Sources; Capitalized fees in S&U equal toggled formulas.
- NAV: GAV − Liabilities = NAV; NAV per unit reconciles to cap table.
- Capital Accounts: opening + contributions + pref − distributions − realized carry = closing.
- Funnel totals: Sum(one‑time + annual + per‑event) matches section totals; toggles correctly zero a fee.

## Open Questions

1. Confirm fee bases (AM on Purchase Price vs AUM; PM fee policy by market).
2. Confirm O&O invoices included in 3% cap and capitalization policy.
3. Select Investor Processing Fee treatment (Mode A vs Mode B) for official reporting.
4. Confirm vesting schedule specifics and interim follow‑on acceleration mechanics.
5. Confirm disposition fee policies and broker engagement scenarios.

## Next Steps

1. Add helper columns on `Funnel`; wire named toggles and fee parameters.
2. Build S&U by party pivot and ongoing P&L views on `Funnel`.
3. Stand up capital account ledgers and pref accrual.
4. Implement GAV/NAV calc and NAV per unit.
5. Validate with KS/BF and iterate.
