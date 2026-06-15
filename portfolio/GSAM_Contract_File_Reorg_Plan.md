# GSAM-Compliant Contract File Reorganization Plan

**Portfolio:** GSA Energy Division — Zone 7 M&V Portfolio (15 contracts)
**COR:** Matthew Schreck
**Prepared:** 2026-06-15
**Scope:** Consolidate competing Google Drive contract-file hierarchies into a single, GSAM/PBS COR–compliant structure.

> **Method note:** This is an **audit + written reorganization plan**. The Drive tools available could read and create folders but had **no "move" operation**, so files must be re-filed manually in the Drive UI (drag-to-move) or by a Workspace admin. Do **not** copy files between hierarchies — copying creates duplicate records, which is the opposite of a clean contract file.

---

## 1. Finding: three competing hierarchies

The Shared Drive currently holds **at least three overlapping "Zone 7" contract hierarchies plus legacy folders**, each with different numbering for the same contracts. This duplication is itself the GSAM-compliance gap (a contract file must be single and authoritative — FAR 4.801/4.803, GSAM 504.8).

| Hierarchy | Folder ID | Created | Status |
|---|---|---|---|
| **`🌎 Zone 7 Contract Files`** | `1Z8y8bYHuIF3ngZ2n45LDyvaABMeZok-C` | 2026-05-20 | ✅ **CANONICAL** — keep |
| `Zone 7 M&V Portfolio` | `1NU6O040o8DP1EPgphs7exa2VV1SM-ZVr` | 2026-02-03 | ⛔ Retire after migration |
| `NEW - ZONE 7` | `1VY3HuXnkbMNpKwPX5EORZJHbbNoHapqL` | 2026-01-21 | ⛔ Retire after migration |
| Legacy R9 / scattered ABM (see §6) | various | 2025 | ⛔ Retire after migration |

---

## 2. Canonical structure (already GSAM/PBS-compliant)

`🌎 Zone 7 Contract Files` already implements the official **GSA COR electronic contract-file "Tab" structure** inside each contract (confirmed in `01 McKinstry DFC`). Apply this **uniformly to all 15 contracts**:

```
<NN Contractor Site PIID>/
├── 00 QuickRef
├── Tab 37 COR Pre-Award Administration
├── Tab 38 CPR Budget / Funding
├── Tab 39 COR Design Documents
├── Tab 40 COR Contract Documentation
├── Tab 41 COR Security Badging and Escorting
├── Tab 42 COR Submittals
├── Tab 43 COR Correspondence
├── Tab 44 COR Invoicing and Inspection Reports
├── Tab 45 COR Project Closeout
└── 99 Working Drafts
```

The master is in `TEMPLATE DO NOT USE` (`1_aORno4Fu9GbsVfq-kGp8PdJi4GCQyLc`) — replicate it into any contract folder that is missing tabs.

---

## 3. Crosswalk — your 8 working categories → COR Tabs

Your Gmail labels / mental model map onto the compliant Tab structure as follows:

| Working category (Gmail label) | → COR Tab folder |
|---|---|
| `01_Contract_Docs` | Tab 40 Contract Documentation (+ Tab 37 Pre-Award, Tab 39 Design Docs) |
| `02_Annual_M&V_Reports` | Reports → Tab 42 COR Submittals; **approval/acceptance documentation → Tab 44** |
| `03_Payments_PRs` | Tab 38 CPR Budget/Funding (+ Tab 44 Invoicing) |
| `04_Site_Visits` | **Inspection forms/reports → Tab 44**; **routine site-visit reports & meeting minutes → Tab 43 Correspondence** |
| `05_Correspondence` | Tab 43 COR Correspondence |
| `06_Performance_Issues` | Tab 40 (cure notices, CO final decisions, claims) + Tab 43 (related correspondence) |
| `07_CPARS` | **CO-owned — filed by the Contracting Officer in acquisition Tabs 31 & 36, *not* a COR tab.** Hand off to the CO; the COR keeps only a reference/working copy (do **not** treat COR Tab 45 as the system of record) |
| `08_HSPD-12` | Tab 41 COR Security Badging and Escorting |

> **Crosswalk notes (per GSA PBS External Agency COR Toolkit — *Example Documents for COR Files*):** annual M&V/PA *reports* live in Tab 42 but their *approval/acceptance* documentation files in Tab 44; *inspection* reports go to Tab 44 while routine site-visit reports/minutes are Tab 43 correspondence; **CPARS and releases of claims are CO acquisition-file items (Tabs 31 & 36), not COR-file items** — the COR's role is to provide input and hand off, so flag CPARS for the CO rather than filing it under closeout.

---

## 4. Canonical contract inventory (target folders)

All under `🌎 Zone 7 Contract Files` (`1Z8y8bYHuIF3ngZ2n45LDyvaABMeZok-C`):

| # | Contract | PIID | Folder ID |
|---|---|---|---|
| 00 | Portfolio Admin | — | `1EJoy1kWi3_WmcjQf-uIPAe5HrJDTExMb` |
| 01 | McKinstry DFC ESPC | 47PJ0024F0020 | `1OspoSTPFhyVXewYUeqAStmtgKF9QAyKB` |
| 02 | Ameresco San Diego ESPC | GS-P-08-16-JE-7074 | `1Xm1i2xPPcH_3aJCdPkOo6wzMDkJx5Wcf` |
| 03 | PG&E Sansome UESC | GS-P-09-17-KS-0009 | `15YomIaBcGxjKHSZ2Yxx4ftGFd6PTITWj` |
| 04 | SDG&E San Diego UESC | 47PK0222F0014 | `1ZAw7j1Y7hObN-RVael-crFTJx_Z3Xh6h` |
| 05 | ABM ENABLE R8 | 47PJ0019F0379 | `1ModJ2acxbuSrQ720xTvln_3t9iojV3UV` |
| 06 | Honeywell LA NDER2 ESPC | GS-P-08-16-JE-7081 | `1lamdzSPBf2Vu0bAgmrOWtUczCZEFoG1D` |
| 07 | Honeywell SF NDER2 ESPC | GS-P-08-16-JE-7140 | `1XEdSG1LZ9f5LzMREda2WQZmTEGbhRgTX` |
| 08 | Ameresco HWSSC Chicago ESPC | GS-P-05-17-GB-0001 | `1UGWBCrTvs2Yc2vxqjeP5qSy-fSaMqsQe` |
| 09 | Honeywell Detroit ESPC | 47PF0020F0671 | `1VnYysSQICaCqybMOrAVBex7ZsoQMV2at` |
| 10 | NORESCO Chicago NDER1 | 47PF0023F0723 | `1rX0ta_iV5bQgLdIjWaxSzpKBibWtgxGM` |
| 11 | Trane Battle Creek ESPC | 47PF0024F0107 | `1YMGQrtHJpHeMbbgTlZxHfp_JODDefYsC` |
| 12 | JCI PJKK ESPC | 47PK0223F0041 | `14WPHtP99-UHYkv2o4kxg0w4OBhYVQK-q` |
| 13 | EMP2 PE Support | 47PK0220F0064 | `1k77LgPQGFB6YNQKbpsXK-jltElQ3NYva` |
| 14 | ABM LA ESPC | 47PK0324C0001 | `11VyA4SulgLTT0t7fMoy1N6Pd932-Xbun` |

---

## 5. Migration procedure (per contract)

For each of the 15 contracts:

1. **Confirm tabs exist** — if the contract folder is missing any Tab 37–45 / 00 / 99 subfolder, copy them from `TEMPLATE DO NOT USE`.
2. **Pull from the duplicate hierarchies** — locate the same contract in `Zone 7 M&V Portfolio` and `NEW - ZONE 7` (see §6 mapping) and **move** (not copy) each file into the matching Tab using the §3 crosswalk.
3. **De-duplicate** — where the same document exists in multiple hierarchies, keep the most recent/most complete; delete the rest. Note conflicts in `99 Working Drafts` if unsure.
4. **Normalize file names per PBS file-naming requirements** — date as `YYYY MM DD`, the **complete PIID with no dashes**, and **no `_` or `-` separators** (use spaces). Example: `2026 06 15 47PK0324C0001 Mod PA0005 Obligation`. *(Per GSA PBS External Agency COR Toolkit — File-Naming Requirements; verify against the current toolkit page, which returned 403 to automated fetch.)*
5. **Verify** — each contract should end with documents in the correct Tab and an empty `99 Working Drafts` (or only true drafts).

---

## 6. Duplicate / legacy folders to retire (after migration)

Confirm every unique file has been moved into the canonical hierarchy, then **archive or delete**:

**`Zone 7 M&V Portfolio` children** — `01 ENABLE R8 ABM` (`18G-1nc9XcFx63gXTKBcvUwR_eytZeJFl`), `03 NDER2 San Diego Ameresco` (`1Du8XXC437qvNjTB-qiftHP4KhmurCsT7`), `06 Honeywell LA` (`1Kt-n19qRPQmVzHHGmD0jbueBVE2VLefF`), `07 NDER2 SF Honeywell` (`1XOhLeGoBPy1W3X0l48DWU4ld_1ixHVCU`), `10 ENABLE Detroit Honeywell` (`1AvzqhrcZoRb7x4LyPf7NCxa1QgxnuTVw`), `11 NDER1 Chicago Noresco` (`1TGxQ_GwwdiPgO-iTOELruSF61fYqmD4M`), `13 NDER1 Battle Creek Trane` (`1LE2oMnm3_nMmgxHhHwuxhQSAy364UGR6`), `NDER2 LA Honeywell Submissions` (`1F2TJUoGJPlbir1RN5qQG_UKIf6F0hY_d`), `08 LA Phase I IIA ABM` (`1TaYRdeBHImcl8xQafDiEg5CqywMaXCaJ`).

**`NEW - ZONE 7` children** — `01 ENABLE Detroit` (`1VyIkgfaUZxHNWUJS4q1KrYVGXXN0OxXF`), `03 NDER1 Chicago` (`1RB1jdgYoWFSv0g7B8jdCkJYkSrmRAN36`), `04 NDER1 HDI Battle Creek` (`1ZvknFSOMm9sEQIvZSUE60UKDCi98JgmA`), `05 ENABLE ABM` (`1Af4ugA47JPpfDsomuk8YQLxu48TQYpNm`), `07 NDER2 San Diego` (`1BDNnq6W0zrvW-cXm9ykN9hAjEdAlufxL`), `10 LA Phase I IIA ABM` (`1I-p30KjvAXnJxHGwufIGWZJ3VCBd5rth`), `11 NDER2 LA Honeywell` (`1i2eIsHLujWk1X5YxwIfljs9rIPIB10C4`), `12 NDER2 SF Honeywell` (`1AaZZUH4OEuYIeTbvl5iCBy3s8rLO0udb`).

**Legacy / scattered** — `R9 ABM ESPC LASC` (`1-kF4FZGcHHceIB8yf2xzJkIZIBcAutQ5`), `R9 Ameresco ESPC SFSC` (`1gla5JMV6vRFCXa11h70-6SrOxBK1rIur`), `R9 ABM UESC SFSC (PG&E)` (`1GhCXDYp0yJKDhnn3_3vvWqPP6hCu7uZz`), `ABM Descope BESS` (`1RD1cRkY-c05-Vduxf8KqP77VQkKfDNM_`), `ABM - LA Ph1 - 2` (`1CD6cMN6QQCmqucbtWGr2RQxeu5LPM4nM`), `ABM LA` (`1c0qd9pqRgvjVlVW8p9D7a5XC7oSCEutO`), `ESPC_Contracts/` (`1UAV9_WbNffpmjCNSivLk1wzLFmtVjHl-`), `ABM ESPC LASC — GSA COR FILE REORGANIZATION PLAN` (`1M3l_W5ek9EJRA9x57sW65QtWaspGPN3p`).

> ABM has the most scatter (BESS / Phase 2B / descope / buyout). Reconcile ABM LA (#14) and ENABLE R8 (#05) carefully — these are the highest-risk contracts in the portfolio.

---

## 7. Compliance checklist (per contract)

- [ ] Single authoritative folder under `🌎 Zone 7 Contract Files`; no live copies elsewhere
- [ ] All Tab 37–45 present (replicated from template)
- [ ] Contract/award docs & mods in Tab 40; design in Tab 39; pre-award in Tab 37
- [ ] Funding/PRs in Tab 38; invoices, receiving reports & **inspection** reports in Tab 44; **routine site-visit reports/minutes in Tab 43**
- [ ] Annual M&V/PA **reports in Tab 42**; their **approval/acceptance documentation in Tab 44**
- [ ] Correspondence in Tab 43; performance actions (cure notices, claims, CO final decisions) in Tab 40
- [ ] HSPD-12 / PIV / badging in Tab 41
- [ ] **CPARS handed off to the CO for acquisition Tabs 31 & 36 (not filed in COR Tab 45)**; closeout docs in Tab 45
- [ ] File names per PBS rule: `YYYY MM DD <PIID no dashes> <DocType>` (no `_` or `-`)
- [ ] `99 Working Drafts` emptied of finalized records
- [ ] Duplicate hierarchies (§6) archived/deleted

---

## 8. References
- FAR 4.801–4.805 — Government Contract Files (content & retention)
- GSAM 504.8 — Government Contract Files
- GSA PBS COR electronic file "Tab 37–45" convention (Energy/ESPC COR file)
- GSA PBS External Agency COR Toolkit — *Example Documents for COR Files* (tab placement of M&V approvals, site visits, CPARS)
- GSA PBS External Agency COR Toolkit — *File-Naming Requirements*
