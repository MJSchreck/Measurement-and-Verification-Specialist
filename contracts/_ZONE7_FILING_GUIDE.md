# Zone 7 M&V Drive Filing Guide (your existing standard)

Source: "Zone7_MV Drive Filing Guide" in Drive, last updated 3/2/2026 by Matt Schreck. **This is the real, already-in-use filing system — not a proposal.** It supersedes both my earlier inferred GSAMS/FAR structure and should be read alongside `_GSA_COR_TAB_STRUCTURE.md` (EASi's own tab numbering) as the two operate at different layers: EASi tabs are the official government-of-record system; this Drive structure is your working filing layer on top of it.

## Root structure
`Zone 7 M&V Portfolio` (shared drive, owner: Matthew Schreck) → two sections:
- `00_Portfolio_Admin` — cross-contract files
- `01`–`14` — one folder per contract (numbering below)

## Contract folder numbering (matches this repo's `contracts/` folders)
| # | Drive folder name | Region | This repo's folder |
|---|---|---|---|
| 01 | McKinstry_DFC (47PJ0024F0020) | R8 | McKinstry-DFC-MtPlains |
| 02 | Ameresco_SanDiego (GS-P-08-16-JE-7074) | R9 | Ameresco-NDER2-SD |
| 03 | PGE_Sansome (GS-P-09-17-KS-0009) | R9 | ABM-UESC-SFSC |
| 04 | SDGE_SanDiego (47PK0222F0014) | R9 | SDGE-San-Diego |
| 05 | ABM_LA (47PK0324C0001) | R9 | ABM-LA-PhaseI-IIA |
| 06 | Honeywell_LA (GSP0816JE7081) | R9 | Honeywell-NDER2-LA |
| 07 | Honeywell_SF (GSP0816JE7140) | R9 | Honeywell-NDER2-SF |
| 08 | Ameresco_HaroldWashington (GSP0517GB0001) | R5 | Ameresco-ENABLE-HaroldWashington |
| 09 | Honeywell_Detroit (47PF0020F0671) | R5 | Honeywell-ENABLE-Detroit |
| 10 | Noresco_Chicago (47PF0023F0723) | R5 | Noresco-Chicago |
| 11 | Trane_BattleCreek (47PF0024F0107) | R5 | Trane-NDER1-BattleCreek |
| 12 | JCI_PJKK (47PK0223F0041) | R9 | PJKK-Johnson-Controls |
| 13 | EMP2_R9 (47PK0220F0064) | R9 | EMP2 |
| 14 | Ameresco_NDER6 (R8, new award) | R8 | NDER6-R8 — **not yet a repo folder with this identity confirmed; verify** |

**This confirms your portfolio really is 14 contracts** (matching the COR Master Tracker header from earlier), and gives exact PIID-to-nickname mapping for all of them — including R8 NDER6 (Ameresco), which I have as a stub under a different working name.

## Standard 7-subfolder template (applies to every contract folder 01–14)
1. `00_Contract_Admin` — COR appointment memo, mod packages, base contract docs, HSPD-12 verification, CO correspondence, delegation letters
2. `01_MV_Reports` — annual M&V reports, one subfolder per PY (`PY##`). Naming: `PY##_[Contractor]_[Location]_MV_Report_YYYYMMDD.pdf`
3. `02_Invoices_RRs` — invoices + EASi Receiving Reports together. Naming: `YYYYMMDD_[Contractor]_[Location]_Invoice_[#]_RR_[EC#].pdf`
4. `03_Correspondence` — emails-as-PDF, MFRs, concern letters, cure notices, meeting notes. Naming: `YYYYMMDD_MFR_[Subject]_[Contract].docx`
5. `04_Site_Visits` — witnessing logs, site visit reports, photos. Naming: `YYYYMMDD_[Contract]_SiteVisit_[Facility].pdf`
6. `05_CPARS` — CPARS drafts/finals. Naming: `FY##_CPARS_[Contractor]_[Contract#]_[Draft|Final].pdf`
7. `06_Issues` — active disputes, shortfall trackers, cure notices, defaults, BESS/settlement docs

**Rule: never save documents directly in the root contract folder.**

## Global naming rules
- Always `YYYYMMDD` date prefix on anything dated
- No spaces — underscores only
- Contract number goes at the END of the filename, never the start
- Version drafts as `_v1`, `_v2`, `_FINAL` — never "Copy of" or "(1)"
- PDF for final/signed docs, DOCX for working drafts
- `PY##` = two-digit performance year (PY01, PY14 — not PY1)
- When a payment completes, move Invoice+RR into a `FY##_Paid` subfolder within `02_Invoices_RRs`

## Contractor abbreviations
JCI (Johnson Controls/PJKK), HW (Honeywell — LA/SF/Detroit), ABM (ABM — LA), MCK (McKinstry — Denver Fed Center), AMR (Ameresco — SD/Harold Washington/NDER6), NOR (Noresco — Chicago), TRN (Trane — Battle Creek/HDI), EMP2 (R9 Project Facilitator)

## 00_Portfolio_Admin contents
- `Dashboards`: Zone 7 M&V Portfolio Tracker (master Excel), Payment Status Matrix, M&V Report Review Status Log, ESC Scorecard (NDER1 St Croix), Annual Funding Spreadsheet (Rajesh Shandal), CPARS Weekly Notification Spreadsheets
- `Templates`: MFR template, RR Checklist, M&V Review Comment Letter, Site Visit/Witnessing Log, COR Recommendation Letter, Letter of Concern/Cure Notice
- `Training_Certs`: FAC-COR Level II cert, CEM cert, GSA IT Security training (was due ~4/1/2026), COR Nomination Tool confirmations, ethics/acquisition training records
- `Weekly_Reports`: Weekly status to Nathan Ingersoll, FY2025 Portfolio Review Report

## ⚠️ Snapshot of CRITICAL/HIGH items as of 3/2/2026 (may be stale — verify current status)
These were flagged in the guide as needing immediate filing/action as of early March 2026. Several match issues this session independently rediscovered from live Drive data months later — worth checking whether they were ever actually resolved or just went quiet:

**CRITICAL:**
- PJKK Yr15 Invoice #137029 ($1,721/mo) — needed filing in 12_JCI_PJKK/02_Invoices_RRs
- **Honeywell SF duplicate RR EC2026012200170 — flagged for a payment stop.** (We independently found ongoing RR/Pegasys friction on this contract in the Honeywell drive pass — worth confirming this specific duplicate was resolved.)
- **ABM LA cure notice draft, PIR due 3/7/2026** — matches the BESS cure notice we found independently in the ABM LA ESPC drive; this guide shows it was already in motion back in Feb/March.
- **McKinstry DFC $768K payment overdue 40+ days** — we found later (FY26 tracker) that this appeared to clear by 2/6/26 ESCO receipt; worth reconciling the timeline since this guide's "overdue" entry predates that.
- **EMP2 R9 Project Facilitator expired 9/28/25, unresolved as of 2/25/26** — matches the EMP2 contract-end-date discrepancy we flagged independently. Still worth a definitive status check since this has now been an open question across multiple sources for many months.

**HIGH:**
- ABM Cure Notice Package draft (Cure Notice, COR Recommendation, PIR Crosswalk)
- SDG&E UESC PA review meeting notes (3/2/2026) — ties to the "21 comments still open" PA report review we found independently
- NDER2 LA Honeywell Yr9 PR EQPMCDB-26-0004 ($1.1M)
- Ameresco NDER2 SD Yr9 Invoice 54347 ($1.7M)
- HDI (Trane Battle Creek) PY11 M&V Report (2/27/2026)
- PJKK Yr14 M&V Report, Revised (2/27/2026)

## What this means for the earlier GSAMS/FAR task
Retire my inferred `00_Award_Documents` / `01_IGA_Baseline` proposal entirely. **This Zone 7 guide is the real standard** — it's simpler (7 subfolders, not 10), already has buy-in, already has 14 contract folders live, and already encodes FAR-relevant categories (CPARS = performance, Contract_Admin = award/mod/HSPD-12, Issues = disputes/cure notices) without needing to mirror EASi's full 36-tab structure 1:1. The EASi tabs remain the system-of-record layer underneath; this Drive structure is the practical working layer on top, and mapping between them is mostly: `00_Contract_Admin` ↔ Tabs 22/26/33/34; `02_Invoices_RRs` ↔ Tab 30; `03_Correspondence` ↔ Tab 33 (and COR-specific Tab 43 per GSA's public COR toolkit); `05_CPARS` ↔ Tab 31; `06_Issues` ↔ Tab 32.
