# New Mexico UESC (GSA Region 7)

## Identifiers
- **Contract/PIID:** GS-00P-15-BSD-1140 (Region 7 Areawide Utility Contract), Task Order **47PH1120F0039** (also referenced as EP-47PH1120F0039 / PDN)
- **EASi/PR reference:** EQ7PMD-20-0062
- **Utility (Contract holder):** New Mexico Gas Company, Inc. (NMGC), 7120 Wyoming NE Ste 20, Albuquerque, NM 87109; CAGE 8R9S8; UEI CLQFKDU3ZGM4
- **ESCO/Subcontractor:** Energy Systems Group, LLC (ESG) — installs/commissions ECMs on NMGC's behalf. ("ESG" in the Drive folder name "R7 New Mexico UESC - ESG" refers to this subcontractor, not a separate contract.)
- **Type:** UESC (Utility Energy Service Contract), Firm Fixed Price
- **Region:** GSA Region 7 (Fort Worth, TX contracting office; sites in NM) — **not** Region 9, correcting the prior stub
- **Contracting Officer:** Patrick L. Chapman Sr., Sr. Contracting Officer, GSA R7 PBS Energy Acquisition Support Branch (7PQD), patrick.chapman@gsa.gov, (817) 301-2461 / 978-7012
- **COR:** Diana Kersey (7PSAB), 505-301-8435, diana.kersey@gsa.gov (site-level correspondence); Shannon Steward (7PMD) also listed as COR on portfolio tracker
- **Sites (original 10 buildings):** Albuquerque Federal Building & U.S. Courthouse (Chavez FB, NM0030ZZ), Pete Domenici U.S. Courthouse (NM0050ZZ), Albuquerque Federal Parking Garage (NM0037ZZ), FSS Warehouse (NM0511AA — **removed from scope** via Mod PS0004, 6/16/2021, due to planned disposal), BLM Building (NM0512AA), Gallup Federal Building (NM0038ZZ), Roswell Federal Building & USCH (NM0035ZZ), Montoya Federal Building (NM0032SN, Santa Fe), Campos U.S. Courthouse (NM0015SN, Santa Fe), and the Albuquerque Federal Building/USCH itself (NM0502ZZ / "421 Gold Avenue")
- **Utilities:** Primary electric — PNM; Primary natural gas — New Mexico Gas Company; Primary water — City of Albuquerque
- **Award date:** 9/29/2020; **Performance Period start:** 11/1/2021; **Original completion date:** 12/31/2044 (24.67-year term) — superseded by early cancellation, see Status below
- **Original financials:** Total Implementation Price ~$9,762,170 (final Sept 2020 TO Schedules); Total Amount Financed (Principal) $8,719,418; Base and All Options Value (Total Contract Value) **$14,397,417**; Estimated Savings % Overall from Baseline: 40.1%

## Status (as of context build 2026-07-15)
- **Status: CONTRACT CANCELLED — Early Cancellation/Buyout executed August 2025 (Mod PS0018).** This is a major development not reflected in the prior stub, which only flagged the warranty issue.
- On **July 14, 2025**, GSA (Heidi Johnson, CO, Energy Division) issued an Early Cancellation Buyout Proposal request to NMGC/ESG. GSA determined **all 10 remaining buildings** in the task order are **"no longer core assets"** — part of a broader FY25 GSA portfolio disposition effort (BA61 funding push; ~$10M obligated 7/10/2025 to buy out three ESPC/UESC projects: this NM UESC — covering the Albuquerque Warehouse Depot & BLM building — plus the Ribicoff building (CT) and LaBranch Federal Building (TX)).
- **Modification PS0018** (executed by CO Patrick Chapman, ~8/19–8/28/2025; also a "Revised" version adding Paragraph 6) invoked **FAR 52.217-2, Cancellation Under Multi-Year Contracts**, cancelling Task Order 47PH1120F0039 **in its entirety**.
- **Cancellation Buyout Obligation: $8,249,640.44**, comprising: Principal Buyout (unamortized debt service balance) $8,123,671.12 + Financing Termination Fee $121,855.07 + Contractor Termination Fee $4,114.25. Base and All Options Value reduced from $14,397,417 to $8,249,640.44 (a $6,147,776.56 reduction). Payment was due 9/30/2025 (invoiced by NMGC 8/31/2025).
- The Drive folder named **"R7 New Mexico UESC (Cancelled)"** (id `1rdrI7-oD4nU3fdqCmrUwxjitC61SaTX5`) is the correct/authoritative contract folder — the "(Cancelled)" suffix accurately reflects this August 2025 cancellation, it is **not** a stray/duplicate folder.
- **Percent complete at cancellation:** CPARS as of 12/9/2024 showed only 15% contract complete (this was a 24-year performance contract; only ~3 years of the ~20+ year performance period had elapsed).
- **Open question for legal/COR follow-up:** it is not confirmed in the indexed files whether Modification PS0018 / the buyout settlement included an explicit release of GSA's warranty claims against NMGC/ESG for the unresolved chiller and BAS defects (see below), or whether GSA retains a live claim post-cancellation. No release/settlement document specific to the warranty dispute was found alongside the cancellation package.

## Warranty / Liability Issue (CRITICAL — origin of portfolio flag)
- **Full Project Acceptance** for all ECMs was issued **April 12, 2024** (some internal emails say "April 11"; formal CO letters consistently cite 4/12/2024). This started the **FAR 52.246-21 One (1)-Year Warranty of Construction**, which GSA calculates as expiring **4/12/2025** — the date the prior tracker stub referenced.
- **Dispute over warranty start date:** NMGC/ESG's position is that ECM 2.1 (Domenici chillers) and ECM 2.2 (Albuquerque CH/421 Gold Ave chillers) each had their own **Certificates of Substantial Completion dated July 19–20, 2022**, which under FAR 52.246-21 started a 1-year warranty that **already expired in July 2023** — well before the chiller defects were reported. NMGC has repeatedly noted repairs performed since then were "not done due to any contractual obligation."
- **GSA's position** (Contracting Officer letters dated 9/12/2024 and a **FINAL NOTICE dated 3/13/2025**): the warranty clock for **all** accepted ECMs runs from **Full Project Acceptance (4/12/2024)**, not from individual ECM certificates, making NMGC liable through 4/12/2025 for the chiller and BAS defects. GSA Region 7 Legal Counsel (LD7) concurred with this reading in both letters.
- **Legal referral:** On 8/2/2024, CO Patrick Chapman formally requested legal advice from GSA LD7 (Jonathon Hunter, cc Angelina Calloway) on enforceability of the construction warranty — "GSA has been waiting for well over a month" on the contractor's position at that point.
- **Specific defects in dispute:**
  - Refrigerant leaks in Domenici Courthouse Chillers 1 & 2 (ECM 2.1) and Albuquerque CH/421 Gold Ave Chillers 1 & 2 (ECM 2.2), plus a bad expansion valve / bad processor on Domenici Chiller 1.
  - BAS/controls (ECM 3.0) issues at Domenici and Albuquerque CH: incorrect graphics/labeling, chiller sequencing logic errors ("Chiller #4" referenced but doesn't exist), AHUs running outside occupied schedule, VAV static-pressure/airflow problems, snow-melt system cycling issues, remote BAS access problems. A detailed **72-item Domenici warranty punch list** and a parallel **10-item Albuquerque CH (421 Gold Ave) list** were tracked (`App-D-3-UESC-Warranty-Items-10Dec24.xlsx`); most controls/graphics items were closed out by ESG through Sept–Nov 2024, but the **chiller refrigerant leak items remained flagged "Pending Legal Review" as of 10/24/2024**.
  - Wireless programmable thermostat issues at Gallup and Santa Fe (Montoya/Campos) buildings, addressed under warranty May 2024.
- **NMGC's 4/24/2025 settlement proposal:** NMGC/ESG (via Travers Mechanical) had already repaired Domenici Chiller 2 and Gold Ave Chiller 2 leaks at a cost of $36,020.30 (framed as goodwill, not an admission of contractual obligation), and proposed a cost-split for the remaining Chiller 1 repairs: **GSA to fund** the Domenici Chiller 1 repair (~$10,913.26, excluding refrigerant) and **NMGC/ESG to fund** the Gold Ave Chiller 1 repair (~$9,710.26, excluding refrigerant). NMGC requested a full release to close the project.
- **No confirmed final resolution was located in the indexed files** — the CO's 3/13/2025 letter was a "FINAL NOTICE" demanding a response by 3/17/2025 reasserting NMGC's full liability; NMGC's counter-proposal followed on 4/24/2025. Whether GSA accepted the cost-split, pursued the warranty claim further, or folded it into the August 2025 cancellation settlement is **unresolved in the file — recommend COR/legal confirm final disposition of the chiller warranty claim before closing this item.**
- CPARS for the 10/1/23–9/30/24 period (filed 12/6/2024) rated the contract Satisfactory/Very Good overall but explicitly noted under Schedule: **"Delays in following up with warranties on some Energy Conservation Measure."**

## ECMs
- **ECM 1.0** — Boiler Improvements (Domenici Courthouse)
- **ECM 2.1** — Chiller Improvements, Domenici Courthouse (Smardt oil-free centrifugal chillers; 12/18-month standard mfr. parts/labor warranty)
- **ECM 2.2** — Chiller Improvements, Albuquerque Federal Building & Courthouse (421 Gold Ave)
- **ECM 3.0** — Controls/BAS Upgrades (Tridium/JACE-based platform; multiple sites)
- **ECM 5.0** — Lighting Improvements (multiple sites — largest single savings driver, ~$296,855/yr proposed Yr1)
- **ECM 6** — (referenced in Yr3 savings-by-building data alongside ECM 5, appears to be a secondary lighting/controls measure at most sites)
- **ECM 11.0 / 11.1** — Renewables Installation (Solar PV — Montoya Federal Building)
- **ECM 13.1** — Xeriscaping Application (water conservation, Roswell/Albuquerque CH)
- **ECM 13.2** — Water Conservation measures (multiple sites)

## Performance Year Savings History
Proposed Year 1 total annual cost savings (per Schedule 1, TO award): **$411,417** ($409,737 energy + $1,680 water/sewer), against Year 1 payment obligation of $387,104. Full projected 24-year Performance Period total: $13,292,955 in cost savings vs. $12,197,452 in payments.

| PY | Report Period | Proposed | Verified/Notes | Status |
|----|---------------|----------|-----------------|--------|
| Yr 0 (Implementation) | through 11/1/2021 | Debt Service $94,098.24 | — | Funded (Mod PA0006) |
| Yr 1 | 11/1/2021–10/31/2022 | $411,417 | M&V payment funded via Mod PA0011 (9/23/2022) | Funded; PIR issued/revised 1/18/2023 |
| Yr 2 | 11/1/2022–10/31/2023 | $421,570 | — | Funded |
| Yr 3 | 11/1/2023–10/31/2024 | $431,986 | Verified savings reported in `GSA-NM-R7-Year-3-Annual-PA-Report.pdf` (1/17/2024, updated 1/21/2025); building-level breakout shows ~$228K electric energy + ~$160K electric demand + water/sewer/meter-size savings verified across the 9 remaining sites (natural gas totals had spreadsheet formula errors in the source file and could not be totaled reliably) | Verified/Accepted |
| Yr 4+ | 11/1/2024 onward | $442,670+ (escalating ~2.3%/yr on energy, ~4%/yr water per contract escalation schedule) | Not reached — contract cancelled before Yr 4 annual report cycle completed | **N/A — contract cancelled 8/2025** |

Note: A detailed Principal/Interest/M&V payment schedule by building and performance year (through PY24) exists in `xGSA R7 ECM Breakout by Year-Building-ECM.xlsx` and the P&I/M&V annual totals workbook — useful for reconciling final buyout payment against the amortization schedule if needed.

## Open Issues / Flags
- **CRITICAL (historical, now largely superseded by cancellation):** Warranty of Construction dispute — GSA asserted NMGC/ESG liable under FAR 52.246-21 for Domenici & Albuquerque CH chiller refrigerant leaks and related BAS defects, with warranty expiring 4/12/2025; NMGC disputed the warranty start date and proposed a cost-split (4/24/2025). **No confirmed resolution/release document found — verify whether the August 2025 cancellation/buyout settlement (Mod PS0018) resolved or preserved this claim.** Recommend confirming with CO Patrick Chapman or GSA R7 Legal (LD7) directly.
- **Contract cancelled effective ~8/2025** — all 10 sites determined "no longer core assets" as part of a GSA portfolio disposition/BA61 funding initiative; $8,249,640.44 buyout paid to NMGC. Confirm no further GSA obligations remain (final invoice reconciliation, CPARS closeout evaluation still needed for the final performance period).
- Central plant (Domenici) had chronic setpoint/T&B (test-and-balance) disputes throughout 2023 — GSA (Aaron Bollinger) argued issues were controls/installation defects, not T&B, citing a 32-36% YoY utility consumption increase not explained by weather; ESG maintained T&B was a pre-existing condition. This dispute is the likely root cause of the later chiller/BAS warranty claims.
- Tenant comfort complaints (courtroom/chambers temperature issues) were recurring at Domenici and Albuquerque CH throughout 2023–2025, feeding into the BAS warranty punch list.
- No FY26+ funding/payment schedule applies — contract is closed out; confirm this project is removed from active R7 ESPC/UESC payment tracking spreadsheets going forward.

## Key Reviewers/Contacts
- Patrick L. Chapman Sr. — Sr. Contracting Officer, GSA R7 PBS Energy Acquisition Support Branch (7PQD), patrick.chapman@gsa.gov, (817) 301-2461
- Heidi Johnson — Contracting Officer, Facilities Management/Energy Division, executed the 2025 cancellation modification, heidi.johnson@gsa.gov, (303) 880-0284
- Diana Kersey — COR, Contract Administration Branch, Greater Southwest Region PBS, diana.kersey@gsa.gov, 505-301-8435
- Shannon Steward (7PMD) — COR listed on portfolio tracker
- Kirk Doll (7PMD) — Project Manager/Designee on cancellation Findings of Fact
- Aaron Bollinger — Chief, Energy & Sustainability Branch (7PMD), aaron.bollinger@gsa.gov
- Steve Rutledge — GSA R7 Performance Contract Program Manager, steve.rutledge@gsa.gov
- Jonathon Hunter / Angelina Calloway — GSA Region 7 Legal (LD7), warranty legal advice
- Kate Healy / Lesley Uhr — GSA Office of General Counsel, Real Property Law Division (LR) — legal sufficiency review for the 2025 cancellation
- Tommy Trujillo — NMGC Energy Contracts Manager, tommy.trujillo@nmgco.com, 575-625-6393
- Gerald C. Weseen — NMGC VP, Regulatory, Strategy & External Affairs (signed warranty correspondence)
- Dan Hill / Ertun Reshat / Gary Jorgensen / Dan Harsh — Energy Systems Group (ESG) project/engineering contacts

## Drive Folder Structure (Shared Drive)
- **`R7 New Mexico UESC (Cancelled)`** (id `1rdrI7-oD4nU3fdqCmrUwxjitC61SaTX5`) — primary/authoritative contract folder; contains modification SF30s (PA0006, PA0011, PS0004, etc.), Feasibility Study Volume 2 (TO Schedules).
- **`R7 New Mexico UESC - ESG`** (id `1ijhx0KAphBVkFaGSMOaFOrf1XPtg8ul7`) — Feasibility Study Volumes 1–3 (incl. Appendix C Performance Assurance Plan), Task Order award package, Post-Installation Report (revised 1/18/2023); subfolder `R7 UESC NM Year 3` (id `1klbC49pJLihKPMKMJ_xPf5Q6JKvscv4j`) contains the Year 3 Annual PA Report and supporting appendices (chiller/BAS savings calcs, warranty items tracker, savings-by-building breakout, Full Project Acceptance letter).
- **`UESC New Mexico`** (id `18bnR_Ss5Zndb9ifXrjFqxcFA0vYFcIHp`) — umbrella working folder with subfolders:
  - `NMGC/ESG Early Cancellation/Buy Out` (id `1y685NYFyWwyVNrOYKPffAnzvTmy9vnvD`) — 2025 cancellation package: Mod PS0018 SF30s, Modification Decision Document, Findings of Fact (GSA Form 2437), termination fee details, buyout invoice, cancellation letter; subfolders `EMAILs & RFP Info- NMGC/ESG Early Cancellation/Buy Out`, `Purchase Request Mods. (PRs) for Early Buyout`
  - `UESC New Mexico NMGC CPARS` (id `1aKcntXhOw0WkTTTp4xYUyfIGu-4v6dm6`) — CPARS evaluations FY21–FY24
  - `UESC NM Warranty of Construction Letter and Response` (id `1K8QRzZQOH71Fo1zFbepKuCkhNygOKTmP`) — full warranty dispute correspondence trail (CO letters, NMGC responses, legal advice request, chiller warranty specs); subfolders `Draft CO Notice of Resolution Warranty Chiller 1 - 2025 March`, `COs Response to Warranty Letter - 2024 September`, `Past Emails - Domenici Chiller 2 issues or Complaints`, `Copy of Acquisition Plan 2020 09 11`
  - `UESC New Mexico Task Order (Task Order Award)`, `UESC NM Payment & Mod Record`, `UESC NM - MFR Payment Justification and Overview`, `CEMS - Commissioning BAS Upgrades - Pete Domenici Courthouse`, `Utility Bills - Info`, `UESC New Mexico T.O. Schedules`, `UESC New Mexico Modifications / Reviews`

## Source Documents Indexed
- `New Mexico UESC TO Schedules 1-5A as of 9-25-2020.pdf` (id `1aOtJb-3WVpficGETNSUIXRBqd9r4_vdA`) — final award TO Schedules (Basic Summary, Schedule 1 Cost Savings/Payments, escalation rates)
- `TO SCHEDULES - NM UESC - Extracted from Award Doc.pdf` — Schedule 1 payment table (24-year projection)
- `47PH1120F0039__UESC_NM_For_Signature_2020 09 29.pdf` — full executed Task Order (Scope of Work, GSA300)
- `Volume 1.pdf`, `Volume 2.pdf`, `Volume 3.pdf` / `Appendix C- GSA R7 PA Plan.pdf` — Feasibility Study (Aug/Sept 2020) with Performance Assurance Plan and proposed ECM savings tables
- `GSA R7 NM PIR Revised.pdf` (1/18/2023) — Revised Post-Installation Report (Year 1 expected savings, construction period savings)
- `GSA-NM-R7-Year-3-Annual-PA-Report.pdf` (1/17/2024, rev. 1/21/2025) plus appendices: `App-A-3...Full-Project-Acceptance-2024-04-12.pdf`, `App-A-4-Savings-Breakout-by-Building.xlsx`, `App-D-3-UESC-Warranty-Items-10Dec24.xlsx` (full warranty punch list), `App-C-2-Domenici-Chiller-Plant-Savings-Calc.xlsx`, `App-D-1-New-Sequence-of-Ops-GSA-NM-Domenici.pdf`
- Modifications: `Mod 0004 T34_FSS Warehouse Mod PS0004` (6/16/2021, scope reduction), `Mod 0006 T34_SF30 Mod PA0006 Debt Service` (11/8/2021), `Mod 0011 T34_SF30 PA0011 Year 1 M&V & Yr 2 Funding` (9/23/2022)
- Cancellation package (Aug 2025): `T34_MDD - Early Cancellation Buyout 47PH1120F0039 PS0018 Overview` (Modification Decision Document), `T34 SF30 Mod PS0018 NM UESC Early Cancellation Buyout 1.pdf` / `Revised UESC NM Cancellation SF30 ... Added Paragraph 6.pdf`, `UESC NM Cancellation Buyout 2437 Findings of Fact 2025 08 19.pdf` (GSA Form 2437), `GSA Region 7 New Mexico UESC Early Cancellation Buyout - Termination Fees Details (7.28.2025) Attachment 2.pdf`, `NMGC - GSA invoice for 9-30-25 Early Cancellation Buyout Payment.pdf`, `UESC New Mexico NMGC & ESG Letter - Early Cancellation Buyout 2025 07 14.pdf`
- Warranty dispute correspondence: `EMail LD7 Legal Advise Requested for UESC NM Warranty Issues.pdf` (8/2/2024), `R7 UESC NM CO Response Warranty of Construction 2024 09 06` (CO letter 9/12/2024), `GSA_-_Letter_regarding_Chiller_Warranty_Issue.pdf` (NMGC letter 8/6/2024), `R7 UESC NM CO Notice Warranty Chiller 2 Domenici 2025 03 13` (CO Final Notice), `2025.04.24 - 47PH1120F0039 - NMGC Letter re Proposal to Resolve Chiller Issues.pdf`, `ECM 2.1 Smardt Chiller Warranty.pdf`, `ECM-2.0 Equipment Submittal_Warranty.pdf`
- CPARS: `T31_NMGC CPARS NM UESC 10-1-20 to 9-30-21.pdf`, `...10-1-21 to 9-30-22.pdf`, `...10-1-22 to 9-30-23.pdf`, `...10-1-23 to 9-30-24.pdf`
- `xGSA R7 ECM Breakout by Year-Building-ECM.xlsx` — full P&I and M&V annual payment totals by building through PY24 (pre-cancellation projection)
