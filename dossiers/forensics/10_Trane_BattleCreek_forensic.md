# Forensic M&V Shortfall Analysis — Trane NDER1 HDI Battle Creek ESPC
**PIID 47PF0024F0107** (converted 11/2023 from GS-P-05-13-GA-0018 / GS-P-05-16-GA-7149, PDN PJ3EB1460) | DOE IDIQ DE-AM36-09GO29044
**Acceptance 1/1/2015 · TO end 12/31/2034 · Pending FY26 early buyout (PS0006)**
**Prepared:** 2026-08-24 for Matt Schreck, COR / Zone 7 M&V Lead
**Method:** Read-only forensic pass over Drive (PY11 report + comment log, PY10 report, PS22/PA21 legacy SF30s, buyout MFRs, R5 tracker) and Gmail (PY11 review threads). Every figure is cited. Nothing was modified or sent.

---

## 1. PY-by-PY Table — Guaranteed vs Verified

Primary source for PY1–PY11: **PY11 Report Table 6** ("Verified Savings for Post-Acceptance Performance Period To-Date"), HDI PY11 Report_20260227 (Drive Doc `15kBBdKaQp2-B7OgD1qqRqgeUGmTKTyLmj2xSIMdaI2w`; PDF `1ALztmAe-OX-kM9HFWAgbITZmFsp63yBG`), cross-checked against the **R5 ALL ESPC Verified Savings & Payments Tracker** HDI table (Sheet `1hldqNYgB-ZHIihlneNfuFqsDeniHF88DZM40lsj_Tec`, Shawna Ramthun) and **PS22** (PY2 acceptance mod SF30, Drive `1I6soc4KOpm-VnYI6dDkzJcWM2StYjENy`). Guarantee years run calendar years from 1/1/2015 (PY *n* = CY 2014+*n*).

| PY | Period | Guaranteed $ | Verified $ | Variance $ | Variance % | Cumulative variance | Annual payment (TO-3) | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | CY2015 | 537,356 | 573,636 | **+36,280** | +6.8% | +36,280 | 496,567 (paid 7/29/2016 per tracker; #02 2/11/2015 per tracker mod col) | Payment net of $40,689 Y1 PPE withheld (tracker note); PPE later deobligated via PA21 |
| 2 | CY2016 | 548,838 | 545,845 | **−2,993** | −0.55% | +33,287 | 507,195 (net of $41,543.47 Y2 PPE withheld) | **Only guarantee-level shortfall in contract history.** PS22 pp. 9–10: "PY2 Verified savings fall short of the Guaranteed savings by $2,993," responsibility Trane |
| 3 | CY2017 | 560,576 | 617,871 | +57,295 | +10.2% | +90,582 | 562,858 (= 560,476.44 + $2,382 residual Y2 PPE released, PA21/tracker) | |
| 4 | CY2018 | 572,577 | 613,066 | +40,489 | +7.1% | +131,071 | 572,477 | |
| 5 | CY2019 | 584,845 | 624,612 | +39,767 | +6.8% | +170,838 | 584,745 | |
| 6 | CY2020 | 597,388 | 632,170 | +34,782 | +5.8% | +205,620 | 597,288 | Boiler 2 stack economizer damper stuck open episodes (per PY10 review log) |
| 7 | CY2021 | 610,212 | 645,466 | +35,254 | +5.8% | +240,874 | 610,112 | |
| 8 | CY2022 | 623,323 | 662,982 | +39,659 | +6.4% | +280,533 | 623,223 | |
| 9 | CY2023 | 636,728 | 674,580 | +37,852 | +5.9% | +318,385 | 636,628 | HHW pump power +14% over proposed (per PY10 comment log) |
| 10 | CY2024 | 650,435 | 689,618 | +39,183 | +6.0% | +357,568 | 650,335 | Trane deficiency drag −$9,405; PY10 report Rev2 accepted via PS0003 |
| 11 | CY2025 | 664,449 | 696,716 | **+32,267** | +4.9% | **+389,833** | 664,349 (paid 2/13/2025 per tracker) | Trane deficiency drag −$17,745 (nearly doubled vs PY10); accepted via PS0005 7/6/2026 |
| 12 | CY2026 (stub to buyout) | 678,779 (full-yr; pro-rated per M&V Plan on cancellation) | **not yet verified** — final M&V report due 30 days after PS0006 | — | — | — | 678,679.40 obligated PA0004 12/17/2025; $678,679.41 disbursed 3/1/2026 | Building closure ~5/1/2026; BAS overrides removed 4/2026; proposed mod language waives shortfall remedy beyond verified findings |
| 13–20 | CY2027–2034 | remaining guarantee (see §5) | **extinguished by buyout** | — | — | — | 5,325,937.41 total (TO-3, tracker) | |

**To-date totals (PY1–11, report Table 6):** verified **$6,976,562** vs guaranteed **$6,586,729** = **+$389,833 cumulative surplus**. Payments to ESCO PY1–11 per Table 6: $6,505,779.

Record status: PY1 and PY2 figures independently confirmed in PS22 Table 6; PY3–PY10 figures come from the PY11 report Table 6 and the R5 tracker, which agree to the dollar for every year. Individual PY3–PY9 report files exist in the legacy archive (mod SF30s incorporate them) but were not each re-opened; no interpolation was used anywhere.

**Structural note on the recurring "~$100" difference:** Guaranteed savings exceed the TO-3 contractual payment by ≈$99.6–$100.3 in every observed year (PY1: 537,356 vs 537,255.72; PY2: 548,838 vs 548,738.07; PY11: 664,449 vs 664,349.44; PY12: 678,779 vs 678,679.40). **The "$99.60 PA0004 variance" flagged as unreconciled in the 8/4/2026 Payment Status MFR is therefore almost certainly not an error** — $678,779 is the PY12 *guaranteed-savings* figure and $678,679.40 is the PY12 *payment* figure. See finding 🟢-1.

---

## 2. Shortfall Inventory (every year and ECM where verified < guaranteed/proposed)

### 2.1 Guarantee-level shortfall — PY2 only
- **PY2 (CY2016): −$2,993 vs guarantee** (verified $545,845 vs $548,838). Source: PS22 pp. 9–10 (`1I6soc4KOpm-VnYI6dDkzJcWM2StYjENy`); tracker note "reported PY2 shortfall $2,993."
  - Report-stated causes (PS22 Table 4): ECM 2.2 **CEP Chilled Water Reset not verified −$7,752 (Trane)**; ECM 2.2 Free Cooling not utilized −$8,561 (GSA — informational, not deducted). Pump-power baseline understatement (ECM 1.2 ratio 1.44, ECM 2.3 ratio 1.33) also dragged verified savings; PS22 states this "will likely continue throughout the entirety of the performance period, and result in a shortfall of savings for the ECM."
  - **Disposition:** Contemporaneous with a **GSA deduction letter dated 1/30/2017** and mod **PA21 (5/18/2017)**, which permanently deobligated **$79,850.50** from Trane's Post-Acceptance Performance Period Expense lines (Y1 PPE $40,689.00 in full; Y2 PPE $39,161.47 of $41,543.47, the residual $2,382.00/$2,382.47 released with the PY3 payment). PA21 SF30 (`17NjSOzSzTj1ZdNypDFzibglzjUDMjBA3`). The deduction letter itself was **not found** in Drive/Gmail, so whether the $2,993 savings shortfall was *explicitly* collected inside that $79,850.50, separately collected, or absorbed cannot be confirmed from available records. What is certain: the government retained $79,850.50 that would otherwise have been paid to Trane in the same era, and no subsequent record treats the PY2 shortfall as outstanding.

### 2.2 ECM-level deficiencies (verified below proposed/target while the total stayed above guarantee)
These were deducted from Trane's verified savings each year (self-liquidating), so they never became amounts owed — but they are the **open deficiency conditions** the 8/4/2026 disposition MFR requires PS0006 to address.

| ECM | Deficiency | PY10 impact | PY11 impact | Trend / persistence | Source |
|---|---|---:|---:|---|---|
| 1.1 Boiler Replacements | Measured efficiency 84.74% vs proposed 88.5% (PY10: 86.67%); verified savings adjusted per IGA TC 1.1: energy-side $10,208 verified vs $23,263 proposed (56.1% haircut) | −$6,193 | **−$13,055** | Efficiency declining since PY5 peak 92.4% → 84.74%; **impact more than doubled year-over-year**; Trane attributes to equipment degradation "within expected range"; boilers never descaled (GSA/CMC responsibility per Trane); no numerical tolerance threshold defined — carried as PY12 action item | PY11 comment log #1, #3, #12 (`1629emR9UwJeDDrOR17touDJ2vF9krL5wC71KrKkR7LA`); PY11 report Table 4; PY10 report Table 4 (`13kpwxMttLk4PnRWVDLs3aA0UVwzb61fZ`) |
| 1.2 HHW Pumping | Actual 100% pump power exceeds modeled baseline (PY10: +51%, −21% savings; PY9: +14%) | −$1,826 | +$367 surplus in PY11 (verified $9,144 vs $8,777 — sample-dependent) | Root cause identified in **PS22 (PY2, 2017)** as baseline model values set below field reality — "will likely continue throughout the entirety of the performance period." Rotating 6-of-11 sample makes annual magnitude noisy | PS22 J-10.2.3.B; PY10 report/review log (`1b6FWtxc98pOPncZ6sJ1rTgfiJj6YrBKB`) |
| 2.3 CHW Pumping | Same baseline-understatement mechanism (PS22 ratio 1.33; PY10 +13%/−7%; PY11 weighted avg power +43%, −22% savings) | −$1,386 | **−$4,690** | **Persistent every documented year PY2→PY11**; rotating 5-of-9 sample; "inherent to the equipment — no operational adjustments GSA needs to make" | PS22 J-10.2.3.E; PY10/PY11 reports Table 4 |
| 2.2 Chiller plant | PY2: CHW reset not verified (−$7,752 Trane). PY11: CHW supply temp sensor reads 1–1.5°F low (reset 44–48°F vs plan 45–50°F) — accepted with calibration recommendation, no impact calculated | −7,752 (PY2) | $0 booked | Sensor calibration deferred to "next performance period" that will now never occur | PS22 Table 4; PY11 comment log #5–6 |
| 3.1 Night Setback | Setback hours below 108-hr/wk target (AHU 102, isolation valves 99, zones 105) — schedules **overridden to 24/7** (Jan–Feb, Jun–Aug 2025) | −$9,598 | **−$31,030** (−11,602 −16,137 −3,291) | Classified **Government** (extended hours/overrides); *not* deducted from verified savings per RRM; overrides reverted for PY12 (comment #9) and BAS override harvest/removal completed April 2026 | PY11 report Table 4; comment log #9 |
| 3.3 Snow melt / Control Seq. Opt. | Snow melt system damaged during GSA groundwork, off at GSA request since ~PY1/PY5, never repaired; Trane claims full $11,767/yr | $0 booked | $0 booked | Full proposed savings validated on avoided-baseline-consumption rationale after Matt's Option B / disaggregation challenge (comment #14); Trane flagged intent to book a *positive* GSA impact in PY12 | PY11 comment log #10, #11, #14 |
| 13.1 Water | GSA fixture swaps to higher-GPF units, clogged fixtures | −$586 | −$603 | Government; informational only | PY10/PY11 reports Table 4 |

**PY11 net drags:** Trane-responsibility **−$17,745/yr** (deducted from verified savings); Government-responsibility **−$4,639 net** (informational: −$31,030 extended hours −$603 fixtures +$26,995 Bldg 2C reduced hours; added back per RRM, yielding "net variance to government" +$27,628).

---

## 3. Attribution Ledger

| # | Item | $ | Classification | Evidence | Confidence |
|---|---|---:|---|---|---|
| A1 | PY2 guarantee shortfall | −2,993 (one-time) | **CONTRACTOR PERFORMANCE DEFICIENCY** (ECM 2.2 CHW reset not verified; pump baseline drag) | PS22 pp. 9–10 & Table 4: variance to guarantee assigned "Trane" per M&V Plan/RRPM matrix | High |
| A2 | Pump-power drag, ECM 1.2/2.3, PY2→PY11 (PY11 −$4,690; PY10 −$3,212; PY2 order −$10K combined) | ~−2K to −5K/yr each | **BASELINE / METHODOLOGY — introduced by Trane, charged to Trane** | PS22 J-10.2.3.B/E: modeled baseline kW set below field-measured values; Trane's own reports classify as "Trane Deficiency" and deduct from verified savings every year | High |
| A3 | Boiler efficiency decline, ECM 1.1 (PY11 −$13,055; PY10 −$6,193) | −6K→−13K/yr, worsening | **CONTRACTOR PERFORMANCE DEFICIENCY** (equipment Trane installed underperforming proposed 88.5%) — with an **undetermined government-O&M contributor** (boilers never descaled; CMC/GSA own maintenance per Trane, comment #3) | PY11 Table 4 assigns Trane; comment #12 confirms 56.1% savings haircut correctly applied per IGA TC 1.1 | High on classification; Med on cause split (degradation vs. deferred GSA maintenance never quantified) |
| A4 | Setback-hour losses PY11 (−$31,030) and PY10 (−$9,598) | −31,030 (PY11) | **GOVERNMENT-RESPONSIBLE ADJUSTMENT** (24/7 schedule overrides, extended occupancy hours) | PY11 Table 4 "Government — Extended hours"; comment #9: overrides in Jan–Feb/Jun–Aug, reverted for PY12; April 2026 override harvest | High |
| A5 | Bldg 2C Floor 2 reduced hours (+$26,995 PY11; +$22,753 PY10) | +26,995 | **GOVERNMENT-RESPONSIBLE ADJUSTMENT (favorable)** — surplus *not* claimed by Trane, mirroring A4 non-deduction: RRM treatment symmetric | PY11/PY10 Table 4 | High |
| A6 | Snow melt full-savings claim, ECM 3.3 ($11,767/yr embedded in verified) | 11,767/yr retained by Trane | **GOVERNMENT-RESPONSIBLE ADJUSTMENT** (GSA damaged system in groundwork, elected non-repair/non-operation since ≥PY5, per Robert Potter 2/27/2020 quote) — challenged as Option-D-style logic under an Option B ECM, then accepted on avoided-baseline rationale with EMCS zero-operation trend documentation required | Comment log #10/#11/#14; acceptance condition in Matt's 6/24 comment | Med — acceptance is reasoned and documented, but the underlying TRACE disaggregation was never produced |
| A7 | 2017 PPE deductions (Y1 $40,689.00 + Y2 $39,161.47) | −79,850.50 **collected from Trane** | **CONTRACTOR PERFORMANCE DEFICIENCY (recovered)** — deduction letter 1/30/2017; context (M&V plan not final until PS13 9/2016, PIR accepted 10/2016, PY1 report accepted 1/2017) implies performance-period services not delivered as scheduled in Y1–Y2 | PA21 SF30; tracker notes; deduction letter itself not found | Med (mechanism certain, stated cause not in hand) |
| A8 | PY2 government impacts (free cooling not utilized −$8,561; PY2 gov total −$8,565) | −8,565 | **GOVERNMENT-RESPONSIBLE ADJUSTMENT** (informational) | PS22 Tables 3–4 | High |
| A9 | PY12 stub savings degradation (building closure eff. ~5/1/2026; overrides pre-removal) | unquantified until final report | **NON-ROUTINE ADJUSTMENT / GOVERNMENT** — closure is a disposition decision; proposed PS0006 language caps remedies at "verified findings" for the stub | 8/4 Payment Status MFR (`1s40OTkSOlOasnFp2p-NXnzJG81A-8amo`); 8/14 MFR §8(f) (`1E2aJ_mUQ4SAJ8k2P16j3AmjmwQADh6F8NHAz4EHqosA`) | High |
| A10 | Stipulated O&M savings block ($184,787 in PY11, escalating 2.1%/yr; ~27% of annual savings) | 150,112→184,787/yr | **BASELINE / METHODOLOGY (stipulated at award, both parties)** — FTE-reduction savings booked at full value every year, never re-measured; note PY11 surplus (+$32,267) is *smaller* than this stipulated block | PY11 report Tables 2/3/6; ECM 1.1 savings sources "reduction of FTE personnel and boiler efficiency increases" | High (as a structural observation, not an allegation) |

**Headline split (life-to-date):** Contractor-caused shortfall vs guarantee: **$2,993 (PY2, resolved/absorbed by 2017)**. Contractor-caused ECM drag: deducted from verified savings annually (PY11 run rate **−$17,745/yr**), fully absorbed inside above-guarantee performance — **$0 currently owed**. Government-absorbed impacts: informational only (never deducted; PY11 net −$4,639), plus **$79,850.50 recovered FROM the contractor** in 2017. Disputed/open: **$0 in dollars** — but three PY11 conditional documentation items and the PS0006 deficiency-disposition decision remain open (see §5).

---

## 4. Red-Flag Scan (per checklist)

| Flag | Finding |
|---|---|
| Stipulated values changing YoY | **Clean.** O&M/FTE stipulated block escalates only at the contractual 2.1%; utility escalators match TO (1.8% elec / 2.9% gas / 3.0% water) in PY2 and PY11 reports. |
| Methodology changes without explanation | **Two hits.** (1) ECM 1.2: trend-line-derived kW substituted for measured kW when pumps don't hit 100% speed — Trane says "the M&V Plan has been updated since the IGA"; Matt's acceptance carried a written-confirmation condition that the manufacturer-data comparison per the current plan is on file (comment #13). Never delivered before buyout notice. (2) ECM 3.3: TRACE-model reasoning inside an Option B ECM (comment #14) — resolved on avoided-baseline rationale, EMCS zero-operation trends required. |
| Baseline adjustments that exactly offset shortfalls | **None found.** The opposite pattern exists: baseline understatement on pumps *hurts* Trane and is deducted annually. |
| Asymmetric NRAs / GRAs | **Substantially symmetric** — government-favorable (+$26,995 Bldg 2C) and government-adverse (−$31,030 setbacks) impacts are both excluded from verified savings. **One watch item:** Trane's 5/28/2026 call note that PY12 will book a *positive* snow-melt impact ("avoided baseline consumption") — a government non-operation being converted into contractor-claimable surplus in the terminal stub year. Verify in the final report. |
| "Did not affect savings" claims without traceable explanation | Trane's O&M-issues boilerplate says GSA deficiencies "did not affect the verified savings" — accurate mechanically (they're added back per RRM), but the $31,030 PY11 magnitude deserved the explicit override attribution it eventually got in comment #9. Traceable; not concealed. |
| Cumulative negative trend | **Real and material:** surplus margin 6–10% of guarantee in PY3–PY5 era → **4.9% in PY11**; Trane deficiency drag doubled PY10→PY11 (−$9,405→−$17,745); boiler efficiency in monotonic decline since PY5. At the PY10→PY11 deterioration rate, the guarantee margin (+$32,267) would have inverted around **PY13–PY14** absent correction. The buyout forecloses that test. |
| Savings increases without ECM additions | ECM 5.1 lighting (+$6,174 over proposed) and 13.1 water (+$464) surpluses rest on **one-time post-installation measurements** re-booked every year since ~PY1 — permitted by the plan, but these are 2015-era measurements carrying a 2025 claim. Not challenged in any review read. |
| GRAs invoked for normal operations | Setback overrides (A4) are genuinely government-caused (BAS override harvest confirms), not normal-ops relabeling. **Clean.** |
| Wrong contractual escalators | **None** — rates tie PY2→PY11 at contractual escalators. |
| Mod-table integrity | Trane's PY11 report Table 1 conflicts with the legacy archive on legacy mod numbering (report: PS-07 "Removal of Task Lighting" 2/5/15, PS-09 "Extension of Contract Expiration"; archive/COR records: PS07 = TO Schedules 1/27/2015) and dates PA0004 "1-Jan-2026" (executed 12/17/2025) and PS0003 "10-Sep-2025". Cosmetic but sloppy; relevant only because PS07 is the controlling schedule set for the buyout. |
| Acceptance-date ambiguity | PY11 report J-10.1.1.D: "project was accepted by GSA on **October 13, 2016** through... PS14," while guarantee years and the buyout O&M-credit math run from **1/1/2015**. This feeds directly into the unresolved guarantee-year anniversary convention (Jan-1 vs Mar-1) worth $8K–$8.5K of credit swing in the settlement (8/14 MFR §7). |

---

## 5. Buyout Forensics — deficiency disposition and walked-away M&V value

**What the two PY11 comment rounds actually disputed (forensic target 1):** There was **no initial shortfall and no top-line revision** — verified savings were $696,716 (+$32,267 over guarantee) in the 2/27/2026 original and unchanged in Rev1 (6/4/2026); PS0005 accepted the report with the comment cycle closed 6/30/2026 (Gmail 19c9fcbe67744ef9, 19cb12c14e0c63d9). The two rounds were a **methodology-and-evidence fight, not a dollars fight**: round 1 (3/30, 15 comments — DB 10, Matt 3, Miles 1 + Frank participation) probed boiler efficiency decline, PM/descaling records, HWP trend-line kW substitution, CHW sensor discrepancy, chiller sequencing, setback-hour losses, and snow melt; Trane's 4/13 responses were thin (e.g., one-line "Trane confirms normal operation" on HHWP-2A); round 2 (5/5, IGA-cross-referenced) forced: the full boiler savings-adjustment math (56.1% haircut per IGA TC 1.1 — confirming the deficiency *was* priced into verified savings), the 300-reading basis for the 2.07 kW HHWP-2A value, the Option B vs TRACE reconciliation on ECM 3.3, and override admissions on setbacks. Three conditional items survived acceptance: **(1)** numerical boiler-efficiency tolerance threshold to be defined in writing (PY12 action), **(2)** written confirmation the manufacturer-data pump comparison per the updated M&V plan is on file, **(3)** EMCS trend documentation of zero snow-melt operation. None had been delivered as of 8/24/2026.

**Earlier-year record (forensic target 2):** PY1–PY10 fully reconstructed above. **One shortfall year in eleven (PY2, −$2,993, 0.55%)**; every other year +4.9% to +10.2% over guarantee; cumulative +$389,833. The 2017 enforcement action ($79,850.50 PPE deduction) is the only money ever taken from Trane.

**Open deficiencies and savings exposure entering PS0006 (forensic target 3):**

| Open item | Annual exposure | Buyout treatment status |
|---|---:|---|
| ECM 1.1 boiler efficiency decline (tolerance undefined) | −$13,055/yr and worsening | In Matt's proposed final-report language as a PY11 conditional item; **no credit in Trane's quotes** |
| ECM 2.3 (± 1.2) pumping deficiency (permanent baseline error) | −$4,690/yr (PY11) | Same — self-liquidates only if final report deducts it from stub verified savings |
| ECM 2.2 CHW sensor calibration | unquantified | Deferred to a PY12 that ends 9/10/2026; effectively extinguished |
| Snow melt EMCS documentation / PY12 positive-impact claim | ±$11,767/yr | Watch the final report for the asymmetric surplus claim |
| CHLR-1/PFHX-1 flow meter | $0 (abandoned-in-place, COR decision 4/14/2026, no ESPC performance impact) | Dispositioned pre-buyout |

Pro-rated to a 9/10/2026 settlement (253/365 of the year), the Trane-deficiency run rate implies roughly **$12.3K of stub-period savings drag** that the final M&V report should deduct from verified stub savings if it applies PY11 rigor — this is the concrete dollar content of the "deficiency disposition" item.

**Does the buyout price account for unresolved M&V value? No — and it isn't supposed to, which is why the disposition item exists.** The quotes ($4,266,995.59 / $4,283,210.17) tie **to the penny** to Annex I outstanding financing (8/14 MFR §§2–3) and contain: no prepaid-O&M credit (COR-quantified at **$15,692–$23,959 gross, ~$10,000–$15,500 floor** if Trane claims the $17,965.38 M&V line as earned by the final report), no deficiency credit, and no valuation of the three conditional items. The 8/4 disposition MFR (`1ptbn1ilAbAqQYIs41dTmQJcUjGskR5At`) gives the CO three lawful outs: correct before settlement, credit against the proposal, or a **written no-residual-value determination** — option 3 is defensible given the facility's disposal (deficiency corrections on equipment in a closing building have near-zero residual value to GSA), but it must be *written*, not silent.

**What M&V value is being walked away from:** (a) **PY12 stub verification** — pro-rated guarantee ≈ $470K (253/365 × $678,779) against savings that will be dominated by the government's own closure; the proposed mod language deliberately waives shortfall remedies "beyond the report's verified findings," which is rational (closure is a GRA) but should be recognized as a waiver. (b) **PY13–PY20 guarantee coverage:** remaining life-of-contract guaranteed savings ≈ **$7,285,741** ($13,872,470 life guarantee − $6,586,729 guaranteed PY1–11), against remaining payments of **$5,325,937** (TO-3 PY13–20) — coverage that lapses with the TO. On the PY11 run rate GSA was netting ~$32K/yr of verified savings above payments, *declining*; with the building closing, forward savings are largely illusory, so the walked-away M&V value is small and shrinking — the buyout economics (avoiding $5.33M of payments on an empty building for $4.27M, below the TO-5 GY12 ceiling of $4,353,148 by $86,152.41) are sound *provided* the O&M credit and deficiency disposition land in PS0006.

---

## 6. Findings

- 🔴 **F-1 (PS0006 must carry the deficiency disposition — $17,745/yr run-rate items).** Trane's quotes contain no deficiency value and the settlement will otherwise extinguish the boiler (−$13,055/yr), CHW pumping (−$4,690/yr) and three PY11 conditional documentation items silently. Execute one of the three options in the 8/4 MFR **in the mod text** — most defensibly a written no-residual-value determination given disposal, plus mandatory application of the PY11 deficiency deductions to stub-period verified savings in the final report (~$12.3K effect). PIID 47PF0024F0107; owner CO Conant, drafted by COR.
- 🔴 **F-2 (Prepaid O&M credit $15,692–$23,959 gross / $10,000–$15,500 floor not in the quotes).** The 3/1/2026 payment prepaid $51,139.88 of GY12 services; Annex I confirms the O&M stream is outside the assigned debt service. Net it in PS0006; confirm the guarantee-year anniversary convention first (Jan-1 vs Mar-1 swings the credit ~$8.3K) — note the PY11 report's own "accepted 10/13/2016 via PS14" line muddies the acceptance-date basis and should be rebutted from the 8/14/2026 MFR record (acceptance 1/1/2015).
- 🟠 **F-3 (Boiler tolerance threshold, pump manufacturer-data confirmation, snow-melt EMCS trends — all still undelivered).** These are the PY11 acceptance conditions; fold all three into the final-M&V-report requirement in PS0006 (Matt's proposed §8(f) language covers item 1 explicitly — add 2 and 3).
- 🟠 **F-4 (Watch the final report for an asymmetric snow-melt surplus claim).** Trane's 5/28/2026 call note signals a PY12 *positive* "avoided baseline consumption" impact from GSA's non-operation. Having accepted symmetric RRM treatment all contract (gov impacts excluded both ways), a terminal-year government-favorable-decision-turned-contractor-surplus should be rejected or offset.
- 🟡 **F-5 (Stub-period verification rigor).** The final report covers 1/1–~9/10/2026 with closure (~5/1) and pre-removal overrides inside the window. Require Option B EMCS trends through the effective date (already in proposed language) and the same Table 4 responsibility split, so the record shows the stub degradation is government/closure-driven, not contractor-hidden.
- 🟢 **F-6 ($99.60 "variance" resolved).** Guarantee exceeds payment by ≈$99.6–$100.3 in every year of the contract (PY1, PY2, PY11, PY12 all confirmed). PA0004's $678,679.40 obligation matches the TO-3 payment; $678,779 is the guarantee figure. Recommend closing dossier Open Issue #7 with a one-line MFR rather than chasing a reconciliation.
- 🟢 **F-7 (Contract genuinely performed).** One shortfall in eleven years (−$2,993, PY2, resolved by the 2017 deduction-letter era actions), +$389,833 cumulative surplus, symmetric RRM administration, deficiencies priced into verified savings annually, and a comment process (especially PY10–PY11) that demonstrably forced methodology onto the IGA. The negative signal is the **trend** (margin 10%→4.9%, deficiency drag doubling), which the buyout renders moot.
- 🟡 **F-8 (One-time measurement surpluses).** Lighting/water surpluses (+$6,638/yr combined in PY11) ride on 2015-era one-time measurements. Immaterial to the buyout; note for doctrine on other contracts.

---

## 7. Sources & Gaps

**Drive files read (IDs):**
- HDI PY11 Report_20260227 — Google Doc `15kBBdKaQp2-B7OgD1qqRqgeUGmTKTyLmj2xSIMdaI2w` (exec summary, Tables 2/3/4/6, ECM sections; ~30% of 155K chars read in targeted chunks) ; PDF copy `1ALztmAe-OX-kM9HFWAgbITZmFsp63yBG` (metadata/snippet only)
- PY11 comment log (final, all 15 comments all rounds) — Sheet `1629emR9UwJeDDrOR17touDJ2vF9krL5wC71KrKkR7LA` (read in full); interim ESCO-response copies `1Di8fBWj9cLhlt7yqVNx4lEZVsfY21Mps` (.xlsx 5/21), `1HI_h--1tnGlBB003I_11sGrOGXfsAWcC1Nw61QHNNcI` (COR-file copy) — identified, not separately re-read
- 250808-1b HDI PY10 Report Rev1.pdf — `13kpwxMttLk4PnRWVDLs3aA0UVwzb61fZ` (Table 4 + performance/O&M sections extracted)
- HDI PY10 Report Review FINAL.pdf — `1b6FWtxc98pOPncZ6sJ1rTgfiJj6YrBKB` (content snippet: HHW 51%/21%, PY9 14%, tolerance discussion origin)
- PS22 PY2 report acceptance SF30 (108 pp) — `1I6soc4KOpm-VnYI6dDkzJcWM2StYjENy` (PY2 Tables 2–6, ECM 1.2/2.3 deficiency language; ~15% read in targeted chunks)
- PA21 deobligation SF30 — `17NjSOzSzTj1ZdNypDFzibglzjUDMjBA3` (read in full)
- R5 ALL ESPC Verified Savings & Payments Tracker — `1hldqNYgB-ZHIihlneNfuFqsDeniHF88DZM40lsj_Tec` (HDI payment/savings table + mod ledger extracted from 181K chars; HDI-relevant sections read)
- 2026-08-14 Buyout Verification MFR — `1E2aJ_mUQ4SAJ8k2P16j3AmjmwQADh6F8NHAz4EHqosA` (full)
- 2026-08-04 M&V Performance Deficiency Disposition MFR — `1ptbn1ilAbAqQYIs41dTmQJcUjGskR5At` (full)
- 2026-08-04 Payment & Performance Status MFR — `1s40OTkSOlOasnFp2p-NXnzJG81A-8amo` (full)
- Buyout Action Register — `14kNJXGuKtFHARlBsajg5ZHTqweA1ZNSlWtrHTV-_3fs` (full)
- HDI PY10 CPARS Performance Evaluation — `10PYRVstzENGTvqzex4rpOZdsxjMKKDm4NMxFBqbfeaw` (snippet: PY9 process detail, PY9 surplus $37,852)
- Legacy mod archive folder `17ai_geNMgweoAMt8fDkj0XWa4hbIQuu1` — full listing (~45 SF30s PA01–PA0004) inventoried

**Gmail threads read:** 19c9fcbe67744ef9 (PY11 submission → Rev1 → closure, incl. Matt's 3/26 review email with $696,716/$664,449/+$32,267 and the deficiency framing; round-1 4/13 and round-2 5/21 transmittals); 19cb12c14e0c63d9 (Y11 comment-cycle coordination, 6/24 comment-status email naming Matt's comments 12/13/14, 6/30 closure and Miles's move to PS0005).

**Records searched for and NOT found (never interpolated):**
- The **1/30/2017 deduction letter** to Trane (basis and itemization of the $79,850.50 PPE deduction) — referenced in PA21 only. Its absence leaves the exact PY2-shortfall collection mechanism undetermined (§2.1, A7).
- Individual PY1 and PY3–PY9 annual M&V report bodies (figures taken from PY11 Table 6 + tracker + acceptance-mod SF30 inventory; PS16/PS24/PS28/PS32/PS35/PS38/PS40/PS0001/PS0003 SF30s exist in the archive but were not each opened).
- Any PY3–PY10 ECM-level Table 4 other than PY10 (so the Trane-deficiency drag series is complete only for PY2, PY10, PY11).
- PS0005 executed SF30 body (execution date/coverage taken from dossier + Gmail 19f38bbd7cefb0b3 reference; not re-opened).
- The R5 tracker contains **no PY1 verified-savings entry** for HDI (blank cell) — PY1 verified $573,636 is sourced solely from PY11/PS22 Table 6.
- Any record explicitly reconciling the $611 difference between the PY2 shortfall ($2,993) and the $2,382 Y2-PPE residual released with the PY3 payment.
