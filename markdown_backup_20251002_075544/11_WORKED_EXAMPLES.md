# 11_WORKED_EXAMPLES.md

Below are four end‑to‑end examples. For each, we list the triggered forms, minimum TurboTax tier, and **paste‑ready** inputs to run through the calculators:

---

## 1) Single K‑1, one state, no sale (K‑1 Property LLC)

**Facts:** One in‑state real‑estate LLC K‑1 with rental income; no foreign items; no sale; no 199A limitations beyond K‑1 reporting.

**Triggered forms:** Schedule E; possibly Form 8582 (if a passive loss).  
**Minimum TurboTax tier:** **Premium** (K‑1 required).

**Software calculator (06) — paste into A1**
Name Value
TT_Online_Free 0
TT_Online_Deluxe 79
TT_Online_Premium 99
TT_State_AddOn 39
TT_State_Efile_Fee 0
Num_K1 1
Num_States 1
Has_1099DIV FALSE
DIV_Over_1500 FALSE
DIV_Box5_199A FALSE
DIV_Box2a_CapGains FALSE
Foreign_Tax_Box7 FALSE
Has_Sales_1099B FALSE
Has_K3_Foreign FALSE

**Professional calculator (07) — paste into A1**
Name Value
Pro_Base_1040 306
Pro_Per_SchedB 60
Pro_Per_SchedD 118
Pro_Per_K1 100
Pro_Per_State_NR 200
Pro_Form1116 150
Pro_Form8582 200
Pro_Form461 200
Pro_Form6251 150
Pro_Form4797 300
Pro_Form6252 200
Num_K1 1
Num_States 1
Has_1099DIV FALSE
DIV_Over_1500 FALSE
DIV_Box2a_CapGains FALSE
Has_Sales_1099B FALSE
Foreign_Tax_Box7 FALSE
Has_K3_Foreign FALSE
Has_1231_or_4797 FALSE
Has_Installment_Sale FALSE
Excess_Business_Loss FALSE
Needs_AMT FALSE
Needs_PAL_8582 FALSE

---

## 2) Two K‑1s, multi‑state; nonresident filing required; no sale

**Facts:** Two partnerships; property in two states; passive income; no K‑3.

**Triggered forms:** Schedule E; two **nonresident** state returns; Form 8582 if losses.  
**Minimum TurboTax tier:** **Premium** (K‑1s).

**Software calculator (06) — paste**
Name Value
TT_Online_Free 0
TT_Online_Deluxe 79
TT_Online_Premium 99
TT_State_AddOn 39
TT_State_Efile_Fee 0
Num_K1 2
Num_States 2
Has_1099DIV FALSE
DIV_Over_1500 FALSE
DIV_Box5_199A FALSE
DIV_Box2a_CapGains FALSE
Foreign_Tax_Box7 FALSE
Has_Sales_1099B FALSE
Has_K3_Foreign FALSE

**Professional calculator (07) — paste**
Name Value
Pro_Base_1040 306
Pro_Per_SchedB 60
Pro_Per_SchedD 118
Pro_Per_K1 100
Pro_Per_State_NR 200
Pro_Form1116 150
Pro_Form8582 200
Pro_Form461 200
Pro_Form6251 150
Pro_Form4797 300
Pro_Form6252 200
Num_K1 2
Num_States 2
Has_1099DIV FALSE
DIV_Over_1500 FALSE
DIV_Box2a_CapGains FALSE
Has_Sales_1099B FALSE
Foreign_Tax_Box7 FALSE
Has_K3_Foreign FALSE
Has_1231_or_4797 FALSE
Has_Installment_Sale FALSE
Excess_Business_Loss FALSE
Needs_AMT FALSE
Needs_PAL_8582 FALSE

---

## 3) UPREIT investor: one K‑1 (OP units) **and** 1099‑DIV with Box 5 (199A) and Box 2a (capital gains)

**Facts:** Investor holds OP units (K‑1) and REIT shares (1099‑DIV). 1099‑DIV shows Box 5 and Box 2a. No foreign taxes.

**Triggered forms:** Schedule E; Form 8995 (199A for REIT dividends); **Schedule D** (Box 2a).  
**Minimum TurboTax tier:** **Premium** (K‑1 + Schedule D).

**Software calculator (06) — paste**
Name Value
TT_Online_Free 0
TT_Online_Deluxe 79
TT_Online_Premium 99
TT_State_AddOn 39
TT_State_Efile_Fee 0
Num_K1 1
Num_States 1
Has_1099DIV TRUE
DIV_Over_1500 FALSE
DIV_Box5_199A TRUE
DIV_Box2a_CapGains TRUE
Foreign_Tax_Box7 FALSE
Has_Sales_1099B FALSE
Has_K3_Foreign FALSE

**Professional calculator (07) — paste**
Name Value
Pro_Base_1040 306
Pro_Per_SchedB 60
Pro_Per_SchedD 118
Pro_Per_K1 100
Pro_Per_State_NR 200
Pro_Form1116 150
Pro_Form8582 200
Pro_Form461 200
Pro_Form6251 150
Pro_Form4797 300
Pro_Form6252 200
Num_K1 1
Num_States 1
Has_1099DIV TRUE
DIV_Over_1500 FALSE
DIV_Box2a_CapGains TRUE
Has_Sales_1099B FALSE
Foreign_Tax_Box7 FALSE
Has_K3_Foreign FALSE
Has_1231_or_4797 FALSE
Has_Installment_Sale FALSE
Excess_Business_Loss FALSE
Needs_AMT FALSE
Needs_PAL_8582 FALSE

**Key sources:** 1099‑DIV instructions; 8995/8995‑A instructions; K‑1 requirement for TT Premium.

---

## 4) Sale year with return‑of‑capital history, unrecaptured §1250 component, and §1061 adjustment

**Facts:** REIT investor had prior **ROC (Box 3)** reducing basis. Sells shares (1099‑B); capital gain includes an **unrecaptured §1250** amount; investor is a service provider with **carried interest** subject to **§1061**.

**Triggered forms:** **Form 8949 + Schedule D**; §1250/28% worksheets (within Schedule D); §1061 recharacterization on **Form 8949**; possibly Schedule E if also holding OP units.  
**Minimum TurboTax tier:** **Premium** (investment sales & advanced capital categories).

**Software calculator (06) — paste**
Name Value
TT_Online_Free 0
TT_Online_Deluxe 79
TT_Online_Premium 99
TT_State_AddOn 39
TT_State_Efile_Fee 0
Num_K1 0
Num_States 1
Has_1099DIV TRUE
DIV_Over_1500 FALSE
DIV_Box5_199A FALSE
DIV_Box2a_CapGains TRUE
Foreign_Tax_Box7 FALSE
Has_Sales_1099B TRUE
Has_K3_Foreign FALSE

**Professional calculator (07) — paste**
Name Value
Pro_Base_1040 306
Pro_Per_SchedB 60
Pro_Per_SchedD 118
Pro_Per_K1 100
Pro_Per_State_NR 200
Pro_Form1116 150
Pro_Form8582 200
Pro_Form461 200
Pro_Form6251 150
Pro_Form4797 300
Pro_Form6252 200
Num_K1 0
Num_States 1
Has_1099DIV TRUE
DIV_Over_1500 FALSE
DIV_Box2a_CapGains TRUE
Has_Sales_1099B TRUE
Foreign_Tax_Box7 FALSE
Has_K3_Foreign FALSE
Has_1231_or_4797 FALSE
Has_Installment_Sale FALSE
Excess_Business_Loss FALSE
Needs_AMT FALSE
Needs_PAL_8582 FALSE

**Key sources:** 1099‑DIV (Boxes 2a/2b/2d & 3 ROC); Schedule D instructions (unrecaptured §1250 & 28% collectibles); 8949 instructions referencing **§1061** reporting.
