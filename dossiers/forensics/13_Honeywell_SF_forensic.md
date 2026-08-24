# Forensic M&V Shortfall Analysis — Contract 13: Honeywell NDER2 San Francisco ESPC

**PIID:** GS-P-08-16-JE-7140 (under DOE IDIQ DE-AM36-09GO29035) | **ESCO:** Honeywell International Inc.
**Vehicle:** $40.8M ESPC (corrected to $38,869,532.89 post-Menlo), awarded 9/23/2016, performance period 3/1/2020–1/31/2038 (Mod AS11)
**Prepared:** 2026-08-24 for Matt Schreck (COR). Read-only forensic reconstruction; every figure cited. Where a record could not be found it is marked **record not found** — nothing is interpolated.

---

## 0. Executive frame

This contract has missed its annual savings guarantee **every performance year since Year 2** and the misses are structural: ~$221–227K/yr of contractor-responsibility "as-built impact" (dominated by a Dellums ECM 4.1 HVAC descope of ~$99–101K/yr) is baked into the spread between proposed/as-built savings and the TO-1 guarantee. The Government has been made whole for the ESCO-responsible portion through payment offsets under TO §C.4.6 — but the recovery ledger runs on a *different basis* (the EMP2 Instructional Memo "verified contractual" numbers) than the accepted M&V reports' shortfall figures, and the difference (up to $56,907/yr) is not explained anywhere in the record. Three dollar disputes remain live (TRM credit month, ~$32K termination-date interest, $2,022.62 TO-1 discrepancy), all riding on Mod PS30.

---

## 1. PY-by-PY table

Two official streams exist and they do not match. Both are shown; discrepancies are analyzed in §4.

### 1a. Per the accepted Year 6 M&V Report V04, Table 3 (Honeywell's cumulative history — "report basis")

Source: "GSA EQM SF Year 6 M&V REPORT V04_2026_03_13.pdf", Drive ID `17U6fgrMP-fG0r4wWkZ6QdJw1qk6ZiqqO`, p.10 Table 3 (identical table in Year 5 V2 report, Drive ID `1xIRtrkMlBt9qqmN-h6gOGs0JHdquVslU`, p.11).

| PY | Contractual period (per V04 label) | Data period | Verified $ | Guarantee $ (TO-1) | Variance $ | Variance % | Cumulative |
|---|---|---|---|---|---|---|---|
| Constr. | — | through 5/31/2019 | $1,159,515 | $713,317 (IM) / $0 (V04 shows in Y1 combined) | +$446,198 | — | +$446,198 |
| 1 | 3/1/2020–2/28/2021 (AS11) — report labeled "Year 1: 9/1/2019–8/31/2020" | 9/1/2019–8/31/2020 | $1,019,109* | $1,214,745 (annual; $1,928,063 shown combined w/ construction) | −$195,636* (V04 shows +$250,531 combined w/ construction) | −16.1% | +$250,531 (HW presentation) |
| 2 | ~3/1/2021–2/28/2022 | ~9/1/2020–8/31/2021 | $1,181,646 (incl. $149,074 rebates) | $1,411,948 | **−$230,302** | −16.3% | +$20,229 |
| 3 | ~3/1/2022–2/28/2023 | ~9/1/2021–8/31/2022 | $1,061,553 | $1,295,238 | **−$233,685** | −18.0% | −$213,456 |
| 4 | ~3/1/2023–2/28/2024 | ~9/1/2022–8/31/2023 | $1,121,394 | $1,330,664 | **−$209,269** | −15.7% | −$422,725 |
| 5 | "Reporting period 3/1/2023–2/28/2024" per report p.5; letter says 9/1/2022–8/31/2023 (see §4 flag) | 9/1/2023–8/31/2024 | $1,137,874 | $1,363,722 | **−$225,848** | −16.6% | −$648,542 (per Y5 Table 3) |
| 6 | 3/1/2025–2/28/2026 | 9/1/2024–8/31/2025 | $1,168,311 | $1,397,628 | **−$229,317** | −16.4% | **−$877,860** (per Y6 Table 3 total) |
| 7 | 3/1/2026–2/28/2027 | 9/1/2025–8/31/2026 (expected) | **record not found — PY running; report not yet due** | ~$1.43M (escalated; confirm on corrected PS30 TO-1) | — | — |

\* Year 1 as originally reported (Y1 report V3, 3/5/2021, Drive ID `1J6gCfCb5EZoqgnSnuCg4vJdaVgEnuTdG`): verified **$1,061,472** (Tables 7/8) or **$1,074,455** (Table 1 — a $12,983 internal inconsistency the GSA FY20 reviewer flagged), guarantee $1,214,745, shortfall **−$153,273** (Tables 7/8 basis) / −$140,290 (Table 1 basis). Later history tables restate Y1 verified down to $1,019,109 with no explanation found in the record. Period labels for Y2–Y4 are inferred from the Y5/Y6 labeling convention — marked "~"; the reports for Y2–Y4 were not located in Drive (see §6).

### 1b. Per the EMP2/David Frank PY6 Instructional Memo, Attachment #4 "Reconciliation of Annual Savings and Payments" ("contractual basis")

Source: "GSA R9 San Fran ESPC PY6 ESPC Instructional Memo.xlsx", Drive ID `16tMuKzTLVdE-Sx9WwhnMel0JL02NaeuI` (filed 1/30/2026). Note its governing rule, quoted: *"There is no carry-over savings allowed from year to year… since payment is in advance… it is necessary to recover over-payments by reducing future payments."*

| Year | Guarantee (TO-1) | "Verified Contractual" | Over/(Under) | Payment made to ESCO | IM note |
|---|---|---|---|---|---|
| 0 (Constr.) | $713,317.00 | $1,159,515.00 | +$446,198.00 | $713,316.00 | No adjustment; excess NOT carried over |
| 1 | $1,214,745.08 | $1,019,019.00 | **−$195,726.08** | $1,019,019.00 | Paid at verified — shortfall never over-paid |
| 2 | $1,411,946.00 | $1,238,553.00 | **−$173,393.00** | $1,411,945.00 | Paid full guarantee → over-payment to recover |
| 3 | $1,295,237.62 | $1,084,243.00 | **−$210,994.62** | $1,295,236.62 | Paid full guarantee; "Pending final review" |
| 4 | $1,330,664.00 | $1,121,394.00 | **−$209,270.00** | NA (netted at invoice) | |
| 5 | $1,363,722.00 | $1,182,967.00 | **−$180,755.00** | NA (netted at invoice) | |
| 6 | $1,397,628.00 | $1,172,688.00 | **−$224,940.00** | NA (offset pending PS30) | |

**Basis gap (report verified vs IM "verified contractual"):** Y2 +$56,907, Y3 +$22,690, Y4 $0, Y5 +$45,093, Y6 +$4,377. These add-backs (presumably government-responsibility items credited to Honeywell for guarantee-comparison purposes per the RRPM matrix) are nowhere derived in the record — see Red Flag R2.

### 1c. The recovery ledger (what was actually deducted, when)

| Event | Amount | Covers | Source |
|---|---|---|---|
| Y1 payment made at verified level ($1,019,019 vs $1,214,745 guarantee) | $195,726 never over-paid | Y1 | IM Attachment #4 (`16tMuKzTLVdE…`) |
| Jul 2024 — deduction on invoice **F6290DE070224A** | **$223,594.00** | Year 3 ($233,685 less $10,091 residual) | Kris Okonski 5/2/2025, Gmail thread `1968e3360a9aa44a` |
| Y2 recovery ($173,393) | **asserted but not independently verified** | Year 2 | Danielle Bogni 5/6/2025 (same thread): "We applied the shortfalls for Year 2 and 3 against the Years 3 and Year 4 payments" — supporting RRs/Sapir 6/6/2024 summary are embedded images, unreadable |
| Jan 2025 — Year 6 annual P&I invoice **F6290DE013025A** billed $886,684.94 vs schedule P&I $1,286,799.94 (Mod AA25: P $760,501.61 + I $526,298.33) | implied deduction **$400,115.00** | Reconstructs to **Y4 $209,270 + Y5 $180,755 (IM basis) + Y3 residual $10,091 = $400,116** ($1 rounding) | Mod AA25 (Drive `1g5ZXykrWIaYgNk6LcBbpwMas_0rR9eY7`); invoice amount per aging alerts (dossier); decomposition is COR reconstruction — verify against invoice PDF |
| Pending — Year 7 P&I offset per §C.4.6 | **$229,317** | Year 6 | Y6 Acceptance Letter w/ COR-inserted disposition paragraph (Drive `1fIXy2p7NKncnAPYzmcFCZvqtLaOWU1n7`); accepted 3/17/2026; issues with PS30 |

Note the December 2024 "$384,387 PY3/PY4 offset" in prior briefings resolves as **row-counting confusion**: Jason Cawthorne's 12/17/2024 question read "Years 3 and 4" off the IM Attachment #4 where row 0 is the construction period. **$384,387.62 = Year 2 ($173,393.00) + Year 3 ($210,994.62) on the IM contractual basis** — exact to the dollar. Source: Cawthorne→Hustrulid 12/17/2024, forwarded to Matt 3/18/2025, Gmail thread `195ab453fcff2e23`. Amanda Hustrulid's same-day reply confirms the mechanism ("We deduct the shortfall from the following year's invoice… reports were multiple years behind so they were paid before verification occurred") and does NOT document an executed December 2024 deduction.

---

## 2. Shortfall inventory (year and ECM level)

### Year 1 (data 9/1/2019–8/31/2020) — shortfall $153,273 (as reported) / $195,726 (as restated)
- Verified $1,061,472 vs guarantee $1,214,745 (Y1 report V3 Tables 7/8). GSA FY20 national review (Drive sheet "M_V Shortfall Review", `1LypOSuQTZi0B_WpnL8a6cAJf9ktIvW1jvB_aIAhvqw4`) recorded: overall variance **−$153,273**, government impact **−$23,485**, plus −$27,517 O&M impact, and flagged the Table 1 vs Table 7/8 inconsistency ($1,074,455 vs $1,061,472).
- Disposition: payment made at verified level per IM — shortfall absorbed by paying less, not by later clawback. Construction-period surplus (+$446,198) was NOT paid out and per the IM cannot be carried over — but Honeywell's Table 3 in every subsequent report presents Y1+construction as a **+$250,531 surplus**, netting the two. See Red Flag R1.

### Year 2 — shortfall $230,302 (report basis) / $173,393 (IM basis)
- Verified $1,181,646 **including $149,074 of one-time rebates** — without rebates the operating shortfall was ~$379K. ECM detail: **record not found** (Y2 report not located; FY21 row of the national shortfall review reads "Not yet received by GSA" — the Y2 report was still outstanding in late 2021, part of the late-delivery era).
- Disposition: paid at full guarantee ($1,411,945); recovery asserted against the Year-3-year payment (Bogni) — **recovery event not independently verified** (evidence is image attachments in thread `1968e3360a9aa44a`).

### Year 3 — shortfall $233,685 (report basis) / $210,995 (IM basis)
- ECM detail: **report not located**; review-comment traces show disputes over Coyle ECM 3.1 EMCS (IT setpoint, ~$4K), Matsui 17.1 Retro-Cx (HW reset $126→$6,900 anomaly), Peckham 3.1 (fan schedules/SAT reset/economizer ~$30K/yr claimed with deficiency later contested). Sources: Y5 review sheet `15oVNr71KhwSVMZGEQNn6BM1s4VOtiL7uweZvLysFvtg`; Y6 comment log `1YQh6jlJhOgcc-S-CsENR4jFFg_Sg-RrOiX8YT-QnwM4`.
- Disposition: paid at full guarantee; $223,594 recovered 7/2024 (invoice F6290DE070224A); $10,091 residual recovered on the Jan 2025 Y6 invoice (reconstruction, §1c). CO Chung's 5/1/2025 challenge ("We are showing a shortfall of ($233,685)… Honeywell shows ($10,091)") was resolved as already-deducted, not disputed savings. Thread `1968e3360a9aa44a`.

### Year 4 — shortfall $209,269 (both bases)
- ECM detail: **report not located.** Value identical in Y5 V2 and Y6 V04 Table 3 and IM Attachment #4.
- Disposition: recovered via the $400,115 net deduction on the Jan 2025 Year 6 invoice (reconstruction, §1c).

### Year 5 (data 9/1/2023–8/31/2024) — shortfall $225,848 (acceptance letter) / $180,755 (IM recovery basis)
- Verified $1,137,874 vs guarantee $1,363,722. Accepted V2 5/29/2025 (Chung letter, Drive `1jctBjlNNPCIqOxHANQJswCniUTKpz2Qq`; Gmail `1971e4fba38bef5f`).
- Composition (Y5 V2 Table 4): HW as-built impacts **−$220,955**; HW performance impacts **−$18,378**; government operational impact **−$60,542** (excluded from guarantee variance). Largest line items (Y5 Table 8): Dellums 4.1 HVAC as-built **−$98,714** ("reduced scope and rates") + $469 GSA HWP item; Menlo as-built **−$24,282**; lighting-post-measurement reductions across sites.
- Attribution fights documented in the review sheet (`15oVNr71…`): Frank rejected HW's attempt to book a $7,300 xeriscaping "GSA shortfall" without 30-day proof-of-performance; CW-pump savings flipped to "full GSA shortfall" absent trends; chiller savings claimed as government impact while operating as proposed — i.e., HW repeatedly proposed government-responsibility labels that reviewers pushed back to HW or required data for.
- Disposition: **recovered at $180,755, not $225,848** — the IM contractual basis nets a $45,093 add-back. The derivation of that add-back is **record not found**. See Red Flag R2.

### Year 6 (contractual 3/1/2025–2/28/2026; data 9/1/2024–8/31/2025) — shortfall $229,317 (16.4%)
Verified $1,168,311 vs guarantee $1,397,628; V01 12/1/2025 → V04 3/13/2026, accepted 3/17/2026. Full decomposition (V04 Table 4): proposed $1,411,447 − as-built impacts $226,579 (Honeywell) − performance impacts $16,557 (Honeywell) = verified $1,168,311; guarantee cushion (proposed − guarantee) only $13,819. **Government operational impacts of $77,162 are additional and are NOT counted against the guarantee** (GSA absorbs them: net variance to Government −$306,480).

ECM-by-ECM (V04 Table 8, "As-Built / Performance / Operational" = HW / HW / GSA):

| Site | ECM | HW as-built | HW performance | GSA operational | Cause per report |
|---|---|---|---|---|---|
| **Dellums** | 4.1 HVAC Upgrades | **−$101,385** | — | — | "Reduced scope and revised demand rates" — the single largest driver, structural since installation |
| Peckham | 3.1 EMCS | −$32,769 | — | — | No OA-economizer trends; scope removal of SAT reset + fan scheduling |
| Matsui | 2.1/5.1/6.1/17.1 | −$30,755 | −$991 | — | Lighting post-measurements; CWPs not modulating to 85%; no CHWP trends |
| Moss | 5.1/12.1/17.1/8.1 etc. | −$30,578 | −$1,225 | −$925 | Lighting re-measurement −$16,509; transformers −$8,052; OA levels high on 3/21 AHUs |
| **Menlo (USGS)** | 5.1/8.1/12.1 | **−$24,824** | **−$4,490** | — | Lighting −$24,544; no trend data for CT fan VFDs (removed from contract 8/1/2025 mid-year) |
| SFFB | 5.1/13.1/13.6 | −$21,128 | −$373 | −$19,328 | Lighting scope; GSA: Year-6 flow-rate driven water reductions |
| Burton | 8.1/12.1/13.1/17.1 | −$8,999 | — | −$8,281 | Retro-Cx DCV/OA-economizer removal; GSA: PH-14 at 60% for lower space setpoint |
| Ryan | 8.1/12.1/13.1/13.6 | −$6,797 | −$2,143 | −$8,371 | HW: AC5 fan min speed; GSA: **xeriscaping controls removed by O&M** (−$7,761) |
| Cottage Way | 12.1/13.1/13.6 | −$5,516 | −$8,172 | −$1,536 | HW: no irrigation meter readings, no savings claimable |
| Shea | 2.1/12.1/13.1/13.6 | +$937 | +$7,401* | −$14,261 | HW: chiller data insufficient −$5,156; GSA: increased irrigation vs Year 5 baseline −$14,653 |
| Coyle | 3.1/5.1/8.1 | +$34,326 | −$6,564 | −$23,513 | Lighting +$34,029 offsets; GSA: 7/16 AHUs off-schedule, min-OA dampers high; EF#10 |
| Browning | 12.1/13.1 | +$343 | — | −$948 | |
| 801 1st St | 5.1 | +$2,421 | — | — | |
| **Total** | | **−$226,578** | **−$16,557** | **−$77,162** | −$320,298 all-in |

- Verified-by-site (acceptance letter Table 1, Drive `1fIXy2p7NKncnAPYzmcFCZvqtLaOWU1n7`): Coyle $353,285 (~30% of portfolio — COR flagged for verification), Moss $144,945, USGS Menlo $126,627 ($160/MBtu outlier — COR flagged), SFFB $111,523.
- Disposition: full $229,317 deducted from Year 7 P&I per §C.4.6, memorialized in the acceptance letter packaged with PS30 (COR-drafted disposition paragraph, review memo 5/22/2026, thread `19e5076f96bca7ab`). GSA remedies expressly preserved (Schedule G / IDIQ) if offset is insufficient.
- Note: the Cawthorne brief of 8/5/2026 (Drive `1nAdx-jqA30xFBKh4adS4Rnc8cDvYcTdgZC5Bd_5kxwU`) characterizes the split as "~$39K GSA-operational, ~$12K Honeywell-performance"; the accepted V04 states $77,162 GSA-operational and $16,557 HW-performance. The brief's figures do not tie to the accepted report — see Red Flag R8.

### Year 7 — running
PY7 = 3/1/2026–2/28/2027. Guarantee to be confirmed on corrected PS30 TO-1. Y6 comment log pre-commits Year 7 items: lighting re-measurement or **credit due to GSA** (measurements skipped in Year 5 — "If not provided in Year 7, see a credit for this," 3/13/26); Coyle courtroom VAV validation else HW shortfall; HydraMetrics averages worksheet. Source: `1YQh6jlJhOgcc-S-CsENR4jFFg_Sg-RrOiX8YT-QnwM4`.

---

## 3. Attribution ledger

| # | Item | $ | Classification | Evidence | Confidence |
|---|---|---|---|---|---|
| A1 | Recurring as-built impact, Y5 $220,955 / Y6 $226,579 (of which Dellums 4.1 HVAC ≈ $99–101K/yr; Peckham 3.1 ≈ $33K; lighting re-measurement reductions across sites) | ~$221–227K/yr, every year | **CONTRACTOR PERFORMANCE DEFICIENCY** (as-built scope not delivering proposed savings; report's own RRPM column says "Honeywell") — with a **BASELINE/METHODOLOGY** overlay: the TO-1 guarantee was never re-set after the as-built scope reductions, so the same gap recurs annually by construction | V04/V2 Table 4 & Table 8; IM's own warning: "If the graph continuously shows a shortfall… a permanent reduction in payments may be in order" | High |
| A2 | Performance impacts (trend/data failures, fans/VFDs not modulating, no CT-fan trends, missing irrigation meters) Y5 $18,378 / Y6 $16,557 | ~$16–18K/yr | **CONTRACTOR PERFORMANCE DEFICIENCY** — many are "no data to prove savings" defaults after GSA reviewers refused unverified full-savings claims | Table 8 rows; comment logs showing reviewer-forced reclassifications | High |
| A3 | Government operational impacts Y5 $60,542 / Y6 $77,162 (PH-14 at 60% for space comfort, AHU schedules, min-OA overrides, irrigation usage up, xeriscaping controls removed by O&M, chiller-4 night operation) | ~$60–77K/yr absorbed by GSA (excluded from guarantee) | **GOVERNMENT-RESPONSIBLE ADJUSTMENT** — but several items are contested attributions the reviewers only partially accepted (xeriscaping POP never demonstrated; min-OA COVID-era settings never released) | Table 8; Y5/Y6 comment logs | Medium (individual items vary) |
| A4 | IM-vs-report basis gap: Y2 $56,907, Y3 $22,690, Y5 $45,093, Y6 $4,377 added back to Honeywell's verified before computing the recovery amount | $129,067 cumulative reduction in recoveries vs letter-stated shortfalls | **DISPUTED / UNDETERMINED** — no derivation found for the add-backs; Y4 got $0 add-back while every neighbor year got one. Resolve with: EMP2 worksheets behind IM Attachment #4 for each year | IM `16tMuKzTLVdE…` vs V04/V2 Table 3 / acceptance letters | High that gap exists; Low on its justification |
| A5 | Year 1 shortfall $153,273–195,726 netted (in Honeywell's cumulative tables) against construction surplus $446,198 | ~$196K presentation | **BASELINE/METHODOLOGY** (introduced by Honeywell's Table 3 presentation). Actual payment was correctly reduced (paid $1,019,019); the offense is the "+$250,531 surplus" framing that persists in every annual report despite the IM's no-carry-over rule | Y1 report; IM Attachment #4; V04 Table 3 | High |
| A6 | Menlo (USGS) pre-removal underperformance: Y5 −$24,282 as-built; Y6 −$24,824 as-built + −$4,490 performance | ~$25–29K/yr within A1/A2 totals | **CONTRACTOR PERFORMANCE DEFICIENCY** — yes, pre-removal Menlo contributed to both Y5 and Y6 shortfalls. Removed 8/1/2025 (PS26) yet still carried $126,627 verified savings in Y6 (data year straddles removal). Post-PS30, Menlo exits guarantee; termination value restated $1,897,982.31 → **$1,685,165** (Matt's 8/13/2026 reconstruction within $95: 11.21% Menlo savings ratio on capital balance net of buy-down ≈ $14,546,745 basis) — favors GSA ~$212,817 | Y5/Y6 Table 8; PS30 thread `19fc7c7d5ecae8a3`; dossier 8/11–8/13 entries | High |
| A7 | TRM credit dispute: $917.94/mo Menlo services delta; effective date 8/1/2025 (PS26) vs Honeywell's 9/1/2025 → GSA position $6,425.28 (7 mo) vs HW schedules $5,507.64 (6 mo); plus the "wash": TRM credit offset by Early Termination Payment rising $388,923 → $394,439 (+$5,516) on the 4/28/26 schedules — credit received then immediately paid back | **$917.94 direct; $5,516 wash exposure**; monthly TRM corrected $8,204.27 → $7,286.33 go-forward | **DISPUTED** (payment-side, not savings): Honeywell schedule error, GSA position documented and preserved as a remedy carve-out in the PS30 release clause. Not a savings/guarantee item — no effect on verified-vs-guaranteed | Chapman 4/30 line-items (`19ddff67b9c5bb41`); Pitts 37-min reply + Chapman 5/12 wash analysis (quoted in full, thread `19e039bdc835088a`); Frank 8/11: credit unchanged in accepted schedules | High |
| A8 | Termination payment misdated 4/1/2026 vs actual Aug 2025 escrow receipt → ~$32,000 unsupported interest accrual to GSA in HW schedules | ~$32,000 | **CONTRACTOR (schedule error)** — cured via the 8/10 schedules/termination-value restatement; verify in executed PS30 | 5/21/2026 consolidated comment letter (dossier; thread `19e039bdc835088a`) | Medium (verify final PS30) |
| A9 | $2,022.62 unexplained TO-1 variance ("manual adjustments John made at the beginning that don't link") | $2,022.62 | **CONTRACTOR** — Honeywell accepted responsibility in writing; CO added cell note 8/21/2026; PS31 full rebuild Q4 2026 | Pitts 8/10/2026 (`19fc7c7d5ecae8a3`) | High |
| A10 | 2021 quarterly M&V credits in Honeywell's "M&V Cost and Expense Breakdown – GSA NDER2 SF" — Frank: "not sure if this was modified or not?" | **unquantified** (workbook attachment; no reply on thread as of 8/24) | **DISPUTED / UNDETERMINED** — resolve by opening the SF xlsx (Gmail thread `1a0252315b074108`, 8/21/2026) and tying 2021 M&V credit lines to mods and to the Pegasys payment history; connects to the AS11 M&V-stream misalignment (Chapman 1/30/2026: Year 1 never invoiced as such; labels off by one year; no overpayment identified — but that reconciliation predates Frank's credit observation) | Thread `1a0252315b074108`; billing review thread `19c11215d99aaaf0` | — |

**Headline split (dollars through PY6, report basis):**
- **Contractor-responsible and recovered/scheduled:** $223,594 (7/2024) + $400,115 (1/2025 invoice net, reconstructed) + $229,317 (Y7 offset pending PS30) = **$853,026**, plus Y1's $195,726 avoided by paying at verified. Y2's $173,393 recovery asserted but unverified.
- **Government-absorbed (operational impacts excluded from guarantee):** ~$77,162 (Y6) + $60,542 (Y5) + at least $23,485 (Y1) per year-of-record documents; Y2–Y4 equivalents **record not found** — reasonable estimate $50–70K/yr, not booked.
- **Disputed/undetermined:** $129,067 of IM-basis add-backs (A4); TRM $917.94 + $5,516 wash (A7); $2,022.62 (A9); 2021 quarterly M&V credits (A10, unquantified).

---

## 4. Red-flag scan

- **R1 — Surplus netting against the no-carry-over rule.** Honeywell's Table 3 (every report) presents Y1+construction as +$250,531, netting a construction surplus the IM says cannot carry over, against a Y1 shortfall that was actually resolved by reduced payment. Cosmetic in payment terms, but it understates the cumulative shortfall optics by ~$446K and has survived four GSA report acceptances. (V04 p.10; IM Attachment #4.)
- **R2 — Recovery basis ≠ acceptance-letter basis.** Y5 letter says shortfall $225,848; the recovery taken was $180,755. Y3 letter-equivalent $233,685; IM basis $210,995 (recovery actually executed at $223,594 + $10,091 = the report basis!). Y6 letter directs the full report-basis $229,317. Three different conventions across three years — each defensible alone, indefensible as a set. Ask EMP2 for the add-back worksheets (A4) and standardize in the SF Instructional Memo.
- **R3 — Year 1 verified restated** from $1,061,472 (accepted Y1 report Tables 7/8) to $1,019,109/$1,019,019 (all later history tables) — a $42K downward restatement with no documented explanation. (Also the original Y1 report's $12,983 Table 1 vs Table 7/8 self-inconsistency.)
- **R4 — Period-label chaos.** The Y5 acceptance letter states report period "September 1, 2022–August 31, 2023"; the Y5 report itself says reporting period 3/1/2023–2/28/2024, data period 9/1/2023–8/31/2024; the Y6 report says contractual period 3/1/2025–2/28/2026, data period 9/1/2024–8/31/2025. The signed Y5 letter's period is wrong by any convention (it names Y4's data year), and the "reporting period" label jumps two years between Y5 and Y6 with no labeled report covering 3/1/2024–2/28/2025 (data periods are contiguous, so no data gap — but the guarantee-year mapping should be re-confirmed against the corrected PS30 TO-1). This is the mechanical residue of the AS11 realignment and of the late-report era (Hustrulid 12/17/2024: "reports were multiple years behind so they were paid before verification occurred"). The task-brief's "Year 6 report ~4 years late" could not be reproduced literally from the record; the reproducible fact is that Y1–Y4 payments were made at guarantee years before verification, and the Y5 report (data through 8/31/2024) was not accepted until 5/29/2025.
- **R5 — Guarantee series non-monotonic.** Y2 guarantee $1,411,948 > Y3 $1,295,238 (drop of $116,710). Likely the one-time guaranteed rebates embedded in Y2 (Y2 verified includes $149,074 rebates) — confirm against TO-1 so the comparison base is clean.
- **R6 — Attribution pressure toward "GSA impact."** Documented reviewer reversals: xeriscaping $7,300 "GSA shortfall" claimed without the required proof-of-performance (Frank, Y5 log); CW pumps flipped to full-GSA without trend support then reversed; chiller "government impact" while operating as proposed; Peckham 3.1 deficiency (~$30K/yr) claimed as "None" in Y5 until challenged (SAT-reset removal ~$12,800 forced back out). NRA symmetry itself is clean — V04 states "No baseline adjustments have been made during this performance year" — the game here is played in the RRPM responsibility column instead.
- **R7 — Five defective schedule deliveries (4/28, 6/5, 6/28, 8/7-slipped, 8/10) misstated payment-side dollars, not M&V savings:** 4/28 — TRM effective-date error, credit understated $917.94/mo, PS26 not incorporated, TO-1/TO-3 gap $1,903,489.95; Chapman 5/12 found TO-1 total payments *increased* $216,039 ($221,546.27 with the questionable credit) in a mod that should reduce the contract; 6/5 — payments pushed 3 months, termination payment still misdated (+~$32K interest to GSA), #REF! workbook; Frank 6/15: TO-5a J121 showed $1,851,585 vs $1,897,982 settlement; 6/28 — errors (referenced in 8/5 brief; transmittal not located); 8/10 — $2,022.62 unexplained variance, admitted untraceable. None changed verified savings; all of them, however, delayed the Y6 acceptance letter and the $229,317 offset (payments held pending PS30), i.e., the true-up mechanism itself was hostage to defective deliverables. Sources: `19ddff67b9c5bb41`, `19e039bdc835088a`, `19fc7c7d5ecae8a3`, PS30 Findings Summary `18JT16A6blRpdFRvTFsNiX-D-83AyoKGsY00ts6h-0XA`.
- **R8 — Internal GSA numbers drift.** The 8/5/2026 Cawthorne brief's "~$39K GSA-operational / ~$12K HW-performance" does not tie to the accepted V04 ($77,162 / $16,557). Correct before the next Service Center briefing.
- **R9 — "Savings increase without ECM addition" check:** Ryan 8.1 VFD savings +18% vs Year 3 questioned by Frank (Y5 log, attributed to O&M-cost recategorization after Year 3) — watch that O&M savings lines don't quietly absorb energy shortfalls.
- **R10 — Misfiled records in the COR file:** "GSA year 6-10 summary (4).pdf" in the SF submissions folder is a **McKinstry** document; "GSA Year 5 REV03.pdf" is the **San Diego Ameresco** Y5 report. Both invite cross-contract citation errors (A240046 exposure).

---

## 5. Findings

- 🔴 **F1 (Material):** Year 6 shortfall **$229,317** (verified $1,168,311 vs guarantee $1,397,628) is accepted and must be recovered in full against the Year 7 P&I payment via PS30's acceptance letter (§C.4.6). PS30 is not yet executed — until it is, the Government's only protection is held payments. PIID GS-P-08-16-JE-7140.
- 🔴 **F2 (Material):** Recovery-basis inconsistency (R2): Y5 recovered $45,093 less than the letter-stated shortfall; cumulative IM add-backs $129,067 (Y2/Y3/Y5/Y6) have no derivation on file. If the add-backs are not defensible government-responsibility credits, up to $129,067 is under-recovered from Honeywell.
- 🔴 **F3 (Material):** The structural as-built gap (~$226K/yr, Dellums 4.1 ≈ $101K) guarantees a PY7 shortfall of similar size. The IM's own doctrine calls for considering a **permanent payment reduction** when the graph shows a continuous shortfall — six consecutive shortfall years qualifies. Raise with CO Chapman as a PS31-era action.
- 🟠 **F4 (Question for CO/contractor):** Confirm the actual deductions on invoice **F6290DE070224A** ($223,594) and **F6290DE013025A** (implied $400,115 = Y4 $209,270 + Y5 $180,755 + Y3 residual $10,091, $1 rounding) against the invoice PDFs and Pegasys, and locate the Year 2 ($173,393) recovery event. The Rajesh Shandal 2017–2025 payment pivot (thread `195d3c46f7776ca4`, xlsx attachment) is the tie-out source.
- 🟠 **F5 (Question):** David Frank's 8/21/2026 flag — 2021 quarterly M&V credits in the SF cost/expense breakdown, "not sure if this was modified or not" — unanswered as of 8/24. Open the SF workbook, tie each 2021 credit to a mod; reconcile against Chapman's 1/30/2026 AS11 billing realignment (which found labels off by one year and Year 1 M&V never invoiced).
- 🟠 **F6 (Question):** The signed Y5 acceptance letter states the wrong report period (9/1/2022–8/31/2023). Correct the record (memo to file) and confirm the guarantee-year mapping on the corrected PS30 TO-1 so the Y7 offset lands against the right year.
- 🟠 **F7 (Question):** TRM credit — hold the 8/1/2025 effective date ($6,425.28 = 7 × $917.94) and written confirmation that the credit is not washed into the Early Termination Payment (+$5,516 pattern from the 4/28 schedules). Both are preserved as GSA remedies in the PS30 release carve-outs; verify in the executed mod.
- 🟡 **F8 (Watch PY7):** Pre-committed Year 7 items: lighting measurements or credit to GSA; Coyle courtroom VAV/WSHP validation else HW shortfall; Dellums meter, Shea CHW sensor, Matsui/Coyle/Peckham trend gaps (data gaps convert to HW deficiencies under the review team's "no data, no savings" doctrine — keep that leverage). Menlo exits the guarantee: expect guarantee ≈ reduced on corrected TO-1; confirm the Y7 guarantee figure.
- 🟡 **F9 (Watch):** Honeywell's Table 3 "+$250,531 Year 1" surplus presentation and the restated Y1 verified — require correction or a footnote in the Year 7 report.
- 🟢 **F10 (Confirms expected):** The §C.4.6 offset machinery, when it runs, does recover ESCO-responsible dollars (verified for Y3/Y4 within $1 of the invoice math), government witnessing/site visits are current (2026 complete), and the Menlo termination restatement to $1,685,165 was independently reconstructed by the COR within $95 and favors GSA by ~$212,817.

---

## 6. Sources & gaps

### Read for this analysis (Drive)
| Doc | ID |
|---|---|
| Year 6 M&V Report V04 (3/13/2026) — Tables 3, 4, 8, site tables | `17U6fgrMP-fG0r4wWkZ6QdJw1qk6ZiqqO` |
| Year 5 M&V Report V2 (5/16/2025) — Tables 3, 4, 8 | `1xIRtrkMlBt9qqmN-h6gOGs0JHdquVslU` |
| Year 1 M&V Report V3 (3/5/2021) | `1J6gCfCb5EZoqgnSnuCg4vJdaVgEnuTdG` |
| PY6 ESPC Instructional Memo (EMP2/Frank) incl. Attachment #4 | `16tMuKzTLVdE-Sx9WwhnMel0JL02NaeuI` |
| Y5 acceptance letter (signed 5/29/2025) | `1jctBjlNNPCIqOxHANQJswCniUTKpz2Qq` |
| Y6 Acceptance Letter — COR Redline (v2, 5/22/2026) | `1fIXy2p7NKncnAPYzmcFCZvqtLaOWU1n7` (also `1erRDtkd6w5Lpm-TGcvgXeu5kyYMejNaOi5RIQ0yUoOg`) |
| SF HW Yr 6 M&V Review Comments — 2-5-26 FINAL | `1YQh6jlJhOgcc-S-CsENR4jFFg_Sg-RrOiX8YT-QnwM4` |
| SF HW Yr 5 M&V Review Discussion | `15oVNr71KhwSVMZGEQNn6BM1s4VOtiL7uweZvLysFvtg` |
| Mod AA25 (Year 6 payment obligation $1,397,626.03) | `1g5ZXykrWIaYgNk6LcBbpwMas_0rR9eY7` |
| M_V Shortfall Review (national FY20/FY21 sheet; SF Y1 row) | `1LypOSuQTZi0B_WpnL8a6cAJf9ktIvW1jvB_aIAhvqw4` |
| Cawthorne Status Brief 8/5/2026 | `1nAdx-jqA30xFBKh4adS4Rnc8cDvYcTdgZC5Bd_5kxwU` |
| PS30 Findings Summary / Walk-Through Cell Map | `18JT16A6blRpdFRvTFsNiX-D-83AyoKGsY00ts6h-0XA` / `1Jh-E5Ymf1S2b8mJblms2fXfvGBvoA5DPWmNb0deY6sE` |
| R5 tracker (checked — Region 5 only, **no SF rows**) | `1hldqNYgB-ZHIihlneNfuFqsDeniHF88DZM40lsj_Tec` |

### Read for this analysis (Gmail threads)
`1968e3360a9aa44a` (Y3 shortfall verification, full thread); `195ab453fcff2e23` (Cawthorne/Hustrulid 12/17/2024 $384,387); `1971e4fba38bef5f` (Y5 acceptance); `19e039bdc835088a` (TRM adjustment; Chapman 5/12 wash analysis quoted); `19ddff67b9c5bb41` (Chapman 4/30 schedule review); `19d250832d5be14a` (financier vetting chase); `19fc7c7d5ecae8a3` (PS30 master; Pitts 8/10 $2,022.82[sic] admission); `1a0252315b074108` (Frank 8/21 quarterly-credits flag); `19e5076f96bca7ab` (Y6 acceptance reminder/COR memo); `19ed1d0b6d9b8c45` (red-lined Y6 letter); `19ac0ea339bfaf2f` (Y6 V1 submission 11/26/2025; Frank comments 12/22/2025); `195d3c46f7776ca4` (2017–2025 expenditure pivot request).

### Records sought and NOT found (do not infer beyond what is written above)
1. **Year 2, Year 3, Year 4 M&V reports** — not located in Drive (SF year-folders under the misidentified "M&V Year N" tree belong to St. Croix; SF Y2–Y4 PDFs not found). Y2 ECM detail therefore unavailable.
2. **Shahar Sapir 6/6/2024 agreed-shortfall summary and the 2024 RRs** — exist only as image attachments in Danielle Bogni's 5/6/2025 email (thread `1968e3360a9aa44a`); not machine-readable here.
3. **Invoice PDFs F6290DE070224A and F6290DE013025A** — amounts known from correspondence; line-item deduction breakdowns unverified (F4).
4. **The joint HW/GSA shortfalls spreadsheet** (Bogni 5/6/2025: "Dave may have it or Stacy Garvey can share") — not located in Drive.
5. **Derivation of IM Attachment #4 "verified contractual" add-backs** (A4/F2) — record not found.
6. **Frank's 8/21/2026 "M&V Cost and Expense Breakdown – GSA NDER2 SF.xlsx"** — Gmail attachment; no attachment-download tool available in this session; unquantified (F5).
7. **Rajesh Shandal payment-history xlsx** (4/3/2025) — same limitation.
8. **A "December 2024 offset" transaction for $384,387** — no payment record found; the figure traces to the IM table (Y2+Y3 contractual basis) and Cawthorne's question, not to an executed deduction.
9. **Year 7 guarantee on corrected schedules** — pending PS30 execution.
10. **Explanation for the Y1 verified restatement** ($1,061,472 → $1,019,109/$1,019,019) — record not found.
11. The task-brief's "Year 6 report ~4 years late" — not reproducible from dated records (see R4); the documented lateness pattern is Hustrulid's "reports were multiple years behind so they were paid before verification occurred" (12/17/2024) plus the Y5 timeline (data through 8/31/2024; accepted 5/29/2025).
