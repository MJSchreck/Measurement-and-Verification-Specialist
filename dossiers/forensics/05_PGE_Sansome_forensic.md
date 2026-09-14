# FORENSIC M&V ANALYSIS — 05 PG&E UESC Sansome | GS-P-09-17-KS-0009

**Prepared for:** Matt Schreck, CEM — GSA Zone 7 COR / M&V Lead (matthew.schreck@gsa.gov)
**Compiled:** 2026-08-24. Read-only forensic pass over Drive + Gmail. Every figure cited. Nothing interpolated.
**Companion dossier:** `dossiers/05_PGE_Sansome_GSP0917KS0009.md`

---

## 0. The Contractual Frame — What Was Actually Owed (read this first)

This is a **UESC with a Performance Assurance (PA) Plan, not a savings guarantee.** The analysis below is run against the actual commitment, not a manufactured guarantee:

- **TO Section 3:** PG&E provides PA reporting + annual on-site inspection for **five (5) years following acceptance (6/30/2020)**. Five PA reports owed; **five delivered** (Year 5 received 1/15/2025; comments resolved 3/28/2025). The reporting commitment is **fully discharged** (validated by COR MFR 8/14/2026, Drive `1qtiLGFyASw8QPzMXNi6g17FXnJsQ3pcW`).
- **PA Plan, Attachment A (quoted verbatim from the Year 5 report, p.19, Drive `1TI3HHMkHsxsT674HgcfevuALuUWrSBe3`):** *"The Customer acknowledges that PG&E does not guarantee any level of savings from the ECMs and agrees that unrealized savings or cost reductions are not a basis for failing to make payments under the contract."* And: *"The Customer will be responsible for implementing corrective actions at its sole cost."*
- **Consequence:** every shortfall dollar identified below was **structurally absorbed by the Government** — no withholding, true-up, or payment-reduction mechanism exists. The PY3 Instructional Memo reconciliation sheet (Drive `1X7hk4PPu5W5B4-VNHeAb811UTnVSo6Iz`) records "Payment Adjustment Needed: **N**" for every year, annotated "NA this is a UESC w/o a guarantee."
- All ECMs: **IPMVP Option A** (Retrofit Isolation, Key Parameter Measurement) with stipulated values. Every ECM section of every PA report states **"No physical measurements were taken"** for the performance year (one-time pre/post measurements existed only for lighting and water at install).

So the forensic question is not "does contractor owe money" (it cannot, by contract) — it is: **(a) did estimated savings materialize, (b) what caused the gaps, (c) who is responsible, and (d) what did the Government's own review record accept.**

---

## 1. PY-by-PY Table — Proposed vs. Reported ("Calculated") Savings

Sources: Year 1 report (Drive `1uu9MV2_rzmCnBRUrLKoTyDUBFGFfcWTZ`), Year 2 report (`1c1-hFq0rKRUTKDFpd80s3dfZ4Gknl65r`), Year 4 report (`1ewHO32oAoflLUYyVt15NdASh48l3t3Zf`, carries Y3 columns), Year 5 report (`1TI3HHMkHsxsT674HgcfevuALuUWrSBe3`, Table 5 "Savings to Date"), PY3 Instructional Memo reconciliation (`1X7hk4PPu5W5B4-VNHeAb811UTnVSo6Iz`).

| PY | Period | Proposed $ | Reported $ | Variance $ | % Realized | Cumulative Variance |
|---|---|---|---|---|---|---|
| 1 | 12/1/2019–11/30/2020 | $178,934 | $173,405 | −$5,529 | 96.9% | −$5,529 |
| 2 | 12/1/2020–11/30/2021 | $182,811 | $174,927 | −$7,884 | 95.7% | −$13,413 |
| 3 | 12/1/2021–11/30/2022 | $186,772 | $174,936 | −$11,836 | 93.7% | −$25,249 |
| 4 | 12/1/2022–11/30/2023 | $190,820 | $176,235 | −$14,585 | 92.4% | −$39,834 |
| 5 | 12/1/2023–11/30/2024 | $194,954 | $185,515 * | −$9,439 | 95.2% | **−$49,273** |
| **Total** | | **$934,291** | **$885,018** | **−$49,273** | **94.7%** | |

\* Year 5 comment resolution (Drive `1rc3f39yfXqwH0m7TrcJGOQjKrvbiq8S-7hGmz3UyGBM`): ABM's water rate used the **electric** escalator (1.62%) instead of the contractual **3.00%** water escalator; corrected Year 5 savings = **$186,527** (+$1,012), and prior-year "Savings to Date" would also rise. The report itself was never re-issued with the correction — it lives only in the comment workbook.

Notes on this table:
- These are **"reported/calculated"** figures, not verified-by-measurement figures — see Section 4. There was no annual measurement to verify against.
- The Y1 report period begins 12/1/2019, **seven months before final acceptance (6/30/2020)** — the reporting clock ran from the end of the 30-day performance period (11/12/2019), not from acceptance. Nobody in the record flags this; it is a benign generosity (an extra reporting-covered period), noted for completeness.
- Y1–Y3 reconciliation totals independently confirmed by the PY3 Instructional Memo Attachment 4 table: −$5,529 / −$7,884 / −$11,836, total −$25,249, "Payment Adjustment Needed: N."
- **No PA report exists for any period after 11/30/2024** — none is owed. Savings performance 12/1/2024 → 12/1/2036 (11 more payment years, ~$1.2M+ of remaining payments) is contractually **unmonitored**.

## 2. Shortfall Inventory — Every ECM, Every Year

Per-ECM proposed values: Y1/Y5 from those reports' Table 2; Y2/Y3 from the PY3 Instructional Memo "Savings Spreadsheet" tab; Y4 from Y4 report Table 2. Reported values: each year's Table 3 / Y5 Table 5.

### 2.1 ECM 4.1 Chiller Replacement — the dominant shortfall (−$53,056 over 5 years; 8.3% realized)

| PY | Proposed | Reported | Variance |
|---|---|---|---|
| 1 | $11,085 | $2,567 | −$8,518 |
| 2 | $11,326 | $770 | −$10,556 (−93.2%) |
| 3 | $11,571 | $439 | −$11,132 (−96.2%) |
| 4 | $11,822 | $193 | −$11,629 (−98.4%) |
| 5 | $12,078 | $857 | −$11,221 (−92.9%) |
| **Σ** | **$57,882** | **$4,826** | **−$53,056** |

What the record says caused it:
- **ABM, Year 5 comment response (verbatim):** *"The shortfall is due to a grossly overstated cooling load on the building during the IGA. There is no way to mitigate that shortfall."* Baseline was built from a **2012 commissioning report** (187,122 kWh = stipulated 5% of building use; 142,547 ton-hr/yr assumed) with no field verification before design (Steve Lee's Y1 comment #14 said exactly this in 2021).
- Actual Year 5 load: **11,478 ton-hours, 209 run-hours** — 8% of the assumed baseline load (Y5 report §2.3).
- **GSA-directed change order:** 110-ton design upsized to **150 tons at GSA's request** to serve a future 10th-floor lab build-out **that was never built** (Y5 report §2.1, comment workbook). The upsize further degraded turndown/variable-flow performance (also drags ECM 8.1).
- COVID-era load collapse (Y1 report §2.3: "if chiller load actually decreased by 73.6%, this points to reduced occupancy… during the COVID pandemic") plus interactive effects from lighting/BAS/fume-hood ECMs reducing cooling load.
- **Critical methodology note that runs in the Government's favor:** the raw Option A stipulation would have produced a *claimed* Y5 saving of 178,236 kWh (stipulated baseline minus actual use). ABM instead **voluntarily adjusted the baseline down to actual delivered ton-hours**, reporting only 6,185 kWh. PF Stevens (Y4 comment #9) observed this "seems to artificially make the savings numbers look bad, even though the equipment by all reports is operating well"; ABM: *"It was mutually agreed [Year 1, with GSA/PG&E] not to over inflate savings based on an incorrect assumption and post Covid building operations."* The new chiller **meets its 0.7742 kW/ton spec**; the machine performs, the baseline was fiction.
- Disposition: never cured (cannot be), never offset, never withheld against — **absorbed**. CO Tue Tran's Y2 acceptance letter (Drive `1dLG87S1UCy9eY0hJY11pegbVOqqWUODf`) attributed shortfalls generically to "operational decisions and utility service disruptions" and asked COR/CO to "collaboratively address this issue from recurring" — no follow-up action found in the record.

### 2.2 ECM 7.1 Steam Isolation Valves — total loss (−$23,934; 0% realized, all 5 years)

| PY | Proposed | Reported |
|---|---|---|
| 1–5 | $4,584 / $4,683 / $4,785 / $4,888 / $4,994 = **$23,934** | **$0 every year** |

- Root cause per ABM's own Y1 comment response: *"Review of the original documentation and calculations suggest this to have been a poor assumption."* Baseline assumed boilers ran **24/7**; they actually ran **8 h/day** pre-retrofit — so the isolation-valve savings never existed. Post-retrofit, site staff run boilers 24/7 anyway ("detrimental to shut down steam boilers," agreed with then-GSA John Palmer per Y5 comments).
- **Responsibility is contractually pinned:** Y4 review comment #19 quotes the Risk & Responsibility Matrix §2.a — *"Contractor is responsible for assessing existing operating hours, validating those hours, and for mistakes if those hours were assessed and validated incorrectly."* ABM's answer: identified with all stakeholders, agreed no savings claimed. Y3 review comment #31 (Steve Lee): "**Remove ECM 7.1 … due to descoping of this work. There is no energy savings to report.**" ABM: "Ok."
- Disposition: contractor self-zeroed the claim (honest reporting), but the Government **paid full price for a non-performing ECM** with no price adjustment — absorbed. The valves themselves work; the *savings concept* was invalid at IGA.

### 2.3 ECM 8.1 CHW Pump VFDs — chronic underperformance (−$12,846; ~15% realized)

| PY | Proposed | Reported | Variance |
|---|---|---|---|
| 1 | $2,840 | **($280)** | −$3,120 (negative!) |
| 2 | $2,902 | $538 | −$2,364 (−81.5%) |
| 3 | $2,964 | $515 | −$2,449 (−82.6%) |
| 4 | $3,029 | $537 | −$2,492 |
| 5 | $3,094 | $673 | −$2,421 |
| **Σ** | **$14,829** | **$1,983** | **−$12,846** |

- Y1 report: during a service call ABM *"discovered much of the original programming had been altered. ABM has not determined the timing or reasoning for these changes"* — someone (unidentified; O&M-side access) de-tuned the VFD programming; ABM restored original design. Y1 savings were negative.
- Structural cap: during the GSA-requested chiller upsize *"it was determined that variability of the chilled water flow will be limited"* (Y5 comments) — pumps trend **>72% speed** continuously; bypass valve open most of the period (Y5 review, deferred item).
- Y3 review: no trend data available Jan–Jun 2022. Y4 review comment #15: **no trend data Jan–Aug 2023**; Veolia later confirmed "no data previous to Dec 8, 2023" — i.e., the Y4 claim was computed from a partial-year data set. Accepted anyway.
- Disposition: absorbed; VFD trend verification is one of the five items deferred to GSA O&M (Section 5).

### 2.4 The offsets — ECMs reported ABOVE proposal (net +$40,563)

| ECM | Σ Proposed (Y1–5) | Σ Reported | Σ Variance |
|---|---|---|---|
| 4.2 Fume Hood Controls | $166,203 | $196,821 | **+$30,618** |
| 5.1 Lighting & Controls | $497,054 | $500,928 | +$3,874 |
| 13.1 Water & Sewer | $90,359 | $95,421 | +$5,062 |
| 3.1 BAS Upgrade | $84,029 | $85,038 | +$1,009 |

These offsets are what keep the project at 94.7% overall — and **the largest one does not withstand scrutiny**:

- **Fume Hoods (+$30,618): the equipment is broken and overridden, yet the claim runs above proposal and grew.** The record simultaneously establishes: TEL controllers fail into default values weekly, O&M power-cycles them, some dampers locked, TEL abandoned the product line, hoods run **24/7 under a Washington-DC directive** (vs. the design basis of 12h/50% + 12h/5% utilization) — and Y5 claimed savings of $43,498 vs. $34,681 proposed, up >10% YOY. When Stevens challenged this (Y5 comments), ABM answered: *"**I do not believe we analyzed fume hood operation** once the on-site staff informed me the fume hoods were overridden to operate 24/7… Savings comes from AHU energy, not fume hoods."* The claim is an AHU-CFM trend artifact (15th-floor AHU usage "drastically reduced"), not verification of the installed measure. EMP2 accepted the response. **Report states X (savings above proposal); the evidence implies Y (the ECM as designed is not functioning and the savings source migrated to a different mechanism that was never part of the ECM baseline).**
- **Lighting (+$3,874): the fixture retrofit is real; the controls layer is dead and the number never moved.** Savings = one-time pre/post wattage × stipulated burn hours, held constant Y1→Y5 (746,091 kWh, identical every year). Meanwhile: Encelium never delivered trending/analytics despite the ECM scope, sensors corrode/fail, "insufficient nodes for program transmission," client manual overrides, Room 720 dead to Encelium. Of the claim, **56,387 kWh/yr (~$7,800/yr) is attributed to lighting controls** — stipulated, never re-verified, and the physical evidence says the controls degrade year over year. Y3 review comment #29 asked exactly this ("if sensor failures result in failing in the on position, wouldn't this constitute [an adjustment]?"); ABM: pre/post measurement "will hold true for the life of the contract" — accepted. Daylight-harvesting savings were never claimed (a genuine conservatism partially offsetting this).
- **Water (+$5,062): probably UNDERSTATED, oddly.** Twice in the record (Y1 water bills; Y3 analysis for John Palmer) actual water rates ran **higher** than the escalated contract rate, meaning real cost avoidance exceeded reported. No bills provided after Y3. Plus the Y5 escalator error (electric 1.62% applied instead of water 3.00%) further understated Y5. Flushometer kits all failed at year 2 and were replaced under warranty (cured). GSA's June 2024 aerator flushing is a Government action that "will impact consumption."
- **BAS (+$1,009): pure stipulation.** 7.5% of chiller/fan electric + 5% of gas baseline, from IGA engineering judgment; annual "verification" = trend review only. Y5 issues log: HW lead-lag faults and **lab hot-water boilers not working** — reported with no savings impact assessed.

## 3. Attribution Ledger

Each shortfall (or disputed savings block) classified with evidence and confidence. Reminder: no dollar here is recoverable — the PA Plan bars withholding — so "contractor-responsible" means *reputationally/CPARS-relevant and lesson-learned-relevant*, not collectible.

| # | Block | $ (5-yr) | Classification | Evidence | Confidence |
|---|---|---|---|---|---|
| A1 | Steam Isolation Valves — savings never existed | −$23,934 | **BASELINE / METHODOLOGY (contractor-introduced)** | ABM in writing: "poor assumption" (Y1 comments); RRPM §2.a assigns operating-hours validation errors to Contractor (Y4 comment #19). Introduced by PG&E/ABM at IGA. | **High** |
| A2 | Chiller — baseline cooling load grossly overstated at IGA | ~−$35–40K of the −$53,056 | **BASELINE / METHODOLOGY (contractor-introduced)** | ABM: "grossly overstated cooling load… during the IGA"; 2012 Cx report used without field check (flagged by Steve Lee, Y1 #14); actual load 8% of assumed. | **High** |
| A3 | Chiller — GSA change order 110→150-ton for lab build-out that never happened; COVID occupancy collapse | remainder of −$53,056 (~−$13–18K) | **GOVERNMENT-RESPONSIBLE ADJUSTMENT** | Y5 report §2.1 (GSA requested upsize + 2 lab spaces); Y1 report §2.3 (73.6% load reduction, COVID); expansion "not been realized." Magnitude cannot be separated from A2 with data on file — ABM itself says the factors were never definitively decomposed. | **Med** (existence High; split Low) |
| A4 | CHW Pump VFDs — turndown limited by the Government-directed chiller upsize | ~−$8–10K of −$12,846 | **GOVERNMENT-RESPONSIBLE ADJUSTMENT** | "During the change order to increase the chiller size… variability of the chilled water flow will be limited" (Y5 comments); pumps >72% speed by design consequence. | **Med** |
| A5 | CHW Pump VFDs — original programming altered by unknown party (Y1 negative savings) | ~−$3K (Y1) | **DISPUTED / UNDETERMINED** | Y1 report: ABM "has not determined the timing or reasoning"; ABM restored settings. Resolution would require BAS audit-trail logs from 2019–20 (likely gone — Veolia keeps no data pre-12/2023). | **Low** |
| A6 | Fume-hood claimed savings above proposal while ECM non-functional; hoods 24/7 by DC mandate | +$30,618 claimed (at-risk block, not a shortfall) | **Split: GOVERNMENT-RESPONSIBLE (24/7 mandate, agency directive) + CONTRACTOR M&V-RIGOR DEFICIENCY (savings claimed without analyzing the measure; TEL controls defective — "Controls do not work, and the issue is with the contractor," Y5 report §3.2.A)** | Y5 comments (ABM: did not analyze fume hood operation); Y5 issues log; TEL product abandoned. | **High** that the block is unverified; **Med** on the split |
| A7 | Lighting-controls portion of lighting claim, stipulated flat while controls degraded | ~$7.8K/yr claimed (~$39K over 5 yrs, at-risk block) | **CONTRACTOR PERFORMANCE DEFICIENCY (Encelium scope under-delivered: no trending/analytics ever; sensors failing under warranty-era complaints) — savings never adjusted** | Y5 report §4.3 (56,387 kWh controls-attributed); Y3 #29, #43; Y4 #13; warranty table (Encelium parts warranty to 7/29/2024 while failures mounted from Y2). GSA client overrides are a Government contribution. | **Med** |
| A8 | Water savings understated (rates + Y5 escalator error) | +$1,012 Y5 corrected; unquantified upside Y1–4 | **BASELINE / METHODOLOGY (contractor error, favored Government)** | Y5 comment #1 (ABM concedes wrong escalator, corrects to $186,527); Y1/Y3 rate analyses. Symmetry note: the one clean calc error in the record ran **against** the contractor. | **High** |
| A9 | Y1 training not performed; Y1/Y3 witnessing forms not produced | services value, unquantified | **CONTRACTOR PERFORMANCE DEFICIENCY (PA services under-delivery, later partially cured)** | Y1 comments #3 ("No witness forms were gathered"), #5 (GSA: "recommend either performing services or providing a credit for services not rendered" — no credit ever documented); Y3 #47 ("No witness form provided"). Y2 documented; Y5 properly signed (Bogni, 11/23/2024). | **High** |

**Bottom line of the ledger:** of the −$49,273 net 5-year gap, roughly **−$60–65K gross is contractor-introduced baseline/methodology error** (steam + chiller-baseline + rigor items), **−$20–25K gross is Government-responsible** (change order, COVID/occupancy, operational overrides, 24/7 mandates) — partially masked by **+$40,563** of offsetting over-reported/over-performing ECMs, of which the $30.6K fume-hood block is itself unverified. 100% of the net was **absorbed by the Government by contract design**; $0 was withheld, cured-with-credit, or offset by the contractor.

## 4. The Meta-Finding: What "Verification" Meant Here

Stated plainly, per the template's instruction: **the five PA reports contain no measured verification of savings.** Every ECM, every year: "No physical measurements were taken." Savings derive from IGA stipulations, one-time 2018–19 pre/post samples (lighting, water), stipulated burn hours, TMY bin models, and BAS trend inspection. Payments (fixed by the PS11 amortization schedule) never depended on any of it. The reports are best understood as **annual equipment-condition inspections with an accounting exhibit attached** — genuinely useful ones (they documented the TEL/Encelium failures, boiler realities, and honest ABM self-corrections that a pure paper exercise would have hidden), but not savings measurement. This is a UESC M&V-rigor finding, not a compliance violation: it is exactly what the CO-approved PA Plan called for. The rigor consequence: **for the remaining ~$1.2M / 11 years of payments there is no contractual mechanism, and no data stream, that will ever tell GSA whether the ECMs are saving anything.** The five deferred technical items (below) are the only bridge, and they belong to GSA now.

## 5. Deficiencies Handed to O&M — the Five Deferred Items + Encelium, with Savings Exposure

The Year 5 review deferred these to a "next performance report" **that was never owed**; the 8/14/2026 MFR re-routed them to GSA R9 O&M / Energy Management (Government responsibility per the PA Plan and roles matrix; CO concurrence requested, outstanding as of 8/24/2026). No routing confirmation exists in Gmail.

| Deferred item | Underlying claimed-savings stream at risk (Y5 basis) | Nature of risk |
|---|---|---|
| 1. CHWST reset verification (CHWST observed 55–65°F vs. 45–50°F design; flagged since Y1 comment #30) | Part of BAS $17,957/yr + chiller $857/yr | Reset not operating → BAS stipulated savings partly illusory; higher pump/fan energy |
| 2. Chiller turndown / load-bin anomaly (91% of hours <5 tons on a 150-ton machine) | Chiller $857/yr (and explains the permanent $11K+/yr gap) | Structural — oversized unit; monitor for short-cycling wear |
| 3. CHW pump VFD trend data (pumps >72% speed; trend gaps 2022, 2023) | VFD $673/yr vs. $3,094 proposed | Cannot demonstrate modulation = cannot demonstrate the ECM works |
| 4. Bypass valve position (open most of period; variable-primary min-flow logic in doubt) | Interacts with items 2–3 | Open bypass defeats variable flow |
| 5. Fume-hood/AHU operation (24/7 DC mandate; TEL controllers failing weekly; Lab 1471 sensor reading 32°F) | FH $43,498/yr claimed | Largest single at-risk stream; also a life-safety-adjacent controls issue |
| + Encelium/TEL controls deficiencies generally (Gov responsibility per matrix) | ~$7,800/yr controls-attributed lighting savings | Degrades silently; no trending exists to detect it |

**Aggregate annual claimed-savings stream riding on deferred/unverified items: roughly $60–70K/yr** of the $185K total — against a fixed payment of $107,981 (FY26) escalating to ~$113K. If these items rot, the building simply loses the energy benefit; the payments continue regardless. Getting a named O&M owner in writing (dossier Next Action #4) is the only remaining lever.

## 6. Witnessing Record (all five years)

| PY | Site visit | Witnessing record | Status |
|---|---|---|---|
| 1 | ABM on-site (fume hoods, CHW plant) | **None** — "No witness forms were gathered for this performance period" (ABM, Y1 comment #3) | Gap (COVID era). |
| 2 | Yes | Documented — Y2 report Attachment K p.64 | OK |
| 3 | 11/17/2022 (Mike Debeaune) | **Form has blank Government Staff field; Y3 review: "No witness form provided"** across all ECMs (Y3 checklist) | Gap. Rachel Kwan (8/20/2026, thread `19ffc528ddb70983`) can attest ABM was on site but has no documentation. |
| 4 | 12/29/2023 | Seven forms list **Fara Akrami (Pundir Group O&M contractor) as "Government Staff"** — impermissible under PBS policy / OIG A240046 | Defective. Same Kwan attestation, no documentation. |
| 5 | 11/23/2024 | **Properly signed by Danielle Bogni** | Clean. ABM's "last site visit and end of reporting" (E49). |

Mitigation: with Option A/stipulated M&V and no physical measurements, witnessing had nothing quantitative to witness — the exposure is procedural (A240046 file-completeness), not savings-integrity. Matt's stated disposition (document PY3/PY4 as gaps; don't backfill signatures) is the defensible one.

## 7. Red-Flag Scan (per checklist)

| Flag | Finding |
|---|---|
| Stipulated values changing year-over-year | **Inverse flag:** stipulations *never* changed — proposed kWh identical all 5 years (1,054,383 kWh) and lighting "actual" identical all 5 years (746,091 kWh) while the underlying controls demonstrably degraded. Static ≠ safe. |
| Methodology changes without explanation | None hidden. The chiller adjusted-baseline method was explained, agreed with GSA in Y1, and **reduced** the claim (anti-inflation). 🟢 |
| Baseline adjustments that exactly offset shortfalls | Not present — the opposite: the Y4 reviewer noted the adjustment made numbers *worse* and ABM declined to paper over it ("no way to mitigate that shortfall"). 🟢 |
| Asymmetric NRAs | No NRAs were ever booked. Candidate events that could have justified contractor-favorable NRAs (COVID occupancy collapse, DC 24/7 fume-hood mandate, GSA aerator flushing, client overrides) were **narratively disclosed but never monetized** in either direction. Symmetric by omission. |
| "Did not affect savings" claims without traceable explanation | **Present, recurring:** lighting sensor failures ruled non-impactful because pre/post stipulation "holds true for the life of the contract" (Y3 #29); BAS lead-lag/lab-boiler faults reported with no savings impact assessed; FH savings claimed while admitting the measure wasn't analyzed. 🟠 |
| Cumulative negative trend | Yes — realization fell monotonically Y1→Y4 (96.9→92.4%), "recovering" in Y5 only via the +$8.8K fume-hood claim jump that ABM could not substantiate as measure performance. 🟠 |
| Savings increases without ECM additions | The Y5 fume-hood jump (+16% over Y4 claim, +25% over proposal) with hoods overridden 24/7. 🔴 (see A6) |
| GRAs invoked for normal operations | Not invoked at all (no guarantee to relieve). The Government-responsibility language was used only to route corrective-action *cost* to GSA — which is what the PA Plan says. |
| Wrong contractual escalators | **Yes — Y5 water used the electric escalator (1.62% vs 3.00%)**; error favored the Government; corrected in comments only, never in a reissued report. Also note Y5 report Table 4 prints the *uncorrected* $22.394/kgal. 🟡 |
| Data availability | Trend-history black holes: no BAS data Jan–Jun 2022 (Y3), Jan–Aug 2023 (Y4, Veolia: nothing before 12/8/2023); Encelium never produced any historical data in 5 years. Claims accepted anyway. 🟠 |

## 8. Findings — Tagged

- 🔴 **F1. $49,273 (5.3%) five-year estimated-vs-reported savings gap, 100% absorbed by the Government by contract design** (GS-P-09-17-KS-0009; PA Plan bars withholding). Dominated by two contractor-introduced IGA baseline errors ABM itself admitted in writing: chiller cooling-load overstatement (−$53,056) and steam boiler 24/7 operating-hours assumption (−$23,934, 0% realized every year). Actionable use: CPARS narrative, IGA-review doctrine for future UESCs (field-verify baselines; no 10-year-old Cx reports), and the zone UESC tracker audit.
- 🔴 **F2. The largest "over-performing" ECM is unverified.** Fume-hood claim ($43,498 in Y5, +$30,618 cumulative over proposal) rests on AHU trend artifacts while the installed measure is overridden 24/7 (DC mandate) and its TEL controls are failed/abandoned — ABM: "I do not believe we analyzed fume hood operation." EMP2 accepted. Had this block been reported honestly as indeterminate, the project's headline realization would be materially below 94.7%.
- 🔴 **F3. No savings visibility for the remaining 11 payment years (~$1.2M).** PA term complete; no measurement infrastructure survives (Veolia retains no data pre-12/2023; Encelium never functional). The five deferred O&M items + Encelium (~$60–70K/yr of claimed-savings streams) have no confirmed GSA owner. This is the single live money-adjacent risk on the contract.
- 🟠 **F4. Question for CO/contractor file:** Y1 PA services under-delivery — training not performed in Y1 and no witness forms gathered; GSA's own reviewer proposed "a credit for services not rendered" (Y1 comments) and no credit or resolution memo appears anywhere in the record. Worth one line in the closeout/CPARS file; not collectible now.
- 🟠 **F5. Question for CO:** Y2 acceptance letter (CO **Tue Tran**, 1/5/2023 — a CO name absent from the dossier's CO chain) directed COR/CO to "collaboratively address" the kW/ton data gap and shortfall recurrence; no responsive action found. Also confirms Y2/Y3-era acceptance letters exist under 9PQ3S — strengthens the ask for missing Y1/Y4/Y5 letters.
- 🟡 **F6. Watch:** Y5 report was never reissued with the corrected water escalator ($186,527, not $185,515) — if any downstream system (scorecard, ePB, zone tracker) ingests the report figure, it carries the stale number. Berezovskiy's 8/18/2026 scorecard correction should be spot-checked for which savings figure it holds.
- 🟡 **F7. Watch:** witnessing file dispositions for PY1/PY3/PY4 (gap memo + Kwan attestation) remain undone; A240046 exposure is procedural given Option A, but the file should say so explicitly.
- 🟢 **F8. Confirms expected:** the contractual commitment — 5 PA reports + inspections — was fully delivered, comment-responsive, and closed (5 of 5; final 1/15/2025; comments resolved 3/28/2025). ABM's M&V engineer repeatedly *declined* to inflate claims (chiller baseline-down adjustment; steam zero-claim; daylight harvesting never claimed; water error against own interest). Within the limits of an Option A/stipulated UESC, the contractor's reporting integrity was above average — the structural problems live in the 2017 IGA and the PA Plan's no-guarantee architecture, not in the annual reporting.

**Headline attribution split (per template):** Contractor-owed: **$0** (structurally impossible under the PA Plan — and correctly so per the MFR). Government-absorbed: **−$49,273 net** (−$89,836 gross shortfall on chiller/steam/VFD, offset by +$40,563 of over-reported/over-performing ECMs). Disputed/unverified blocks inside the "offsets": ~$30,618 (fume hood) + ~$39K (lighting-controls stipulation) claimed-but-unverifiable. Contractor-introduced baseline error is the largest causal family (High confidence); Government actions (chiller upsize order, 24/7 mandates, overrides, COVID occupancy) are the second (Med confidence on dollar split).

## 9. Sources & Gaps

**Drive files read for this forensic pass (beyond the dossier's source list):**
- `PGE GSA SF UESC - Yr 1 PA 20210202.pdf` — `1uu9MV2_rzmCnBRUrLKoTyDUBFGFfcWTZ` (read in full)
- `PGE GSA SF UESC - Yr 2 PA report.pdf` — `1c1-hFq0rKRUTKDFpd80s3dfZ4Gknl65r` (read: delivery receipt, exec summary tables, rates; ECM sections sampled)
- `PGE GSA SF UESC - Yr 4 PA report.pdf` — `1ewHO32oAoflLUYyVt15NdASh48l3t3Zf` (read: exec summary, Tables 2/3, ECM summaries)
- `PGE GSA SF UESC - Yr 5.pdf` — `1TI3HHMkHsxsT674HgcfevuALuUWrSBe3` (read in full incl. PA Plan, issues log, attachments)
- `SF UESC Yr 1 PA Comments 08Feb2022 FINAL Accepted.xlsx` — `1jEacUxvs8FG-FjP9YTU89LmRNGxFc17r` (read in full)
- `SF ABM UESC Yr 2 Performance Assurance Review_FINAL Accepted 1.5.23.pdf` — `1XVN6nEbFZFMaktt6t0WyHKhjg7B0Vgul` / `1wRcggYUpTmrTsJcgJpTFEp8P8JvakNPL` (read: snippet-level, both copies)
- `SF ABM UESC Yr 3 Performance Assurance Review 9.13.23 (FINAL).pdf` — `16-5XeQ_4RbQy7EoVwa6tRoyUBRj8P5nz` (read in full)
- `GSA SF ABM UESC Yr 4 Performance Assurance Review 11.20.24 - FINAL` — `1rKdh3uNJZc1BP_jeWhgLAWULExNvEpLklRtwsIT7310` (read in full; note: its Project Info tab still carries stale "Yr 3 / 2-1-2024" header text)
- `SF ABM UESC Yr 5 Performance Assurance Review 1.16.25` — `1rc3f39yfXqwH0m7TrcJGOQjKrvbiq8S-7hGmz3UyGBM` (+ copy `1_OUP1ujDYT3q7iyDlduVpSSRk55ikpXeHwCVe_klRH8`) (read in full)
- `GSA R9 SF UESC PGE PY3 PA Review Instructional Memo 3.1.2023.xlsx` — `1X7hk4PPu5W5B4-VNHeAb811UTnVSo6Iz` (read in full — R&R matrix, Y3 checklists, reconciliation table Y1–Y3, per-ECM variance sheets Y2–Y3)
- `CO Acceptance Letter - Yr 2 PAR (1.5.2023).pdf` — `1dLG87S1UCy9eY0hJY11pegbVOqqWUODf` (read in full; CO Tue Tran)
- `PAR Deadline Adjustment Letter (12.16.2022).pdf` — `1HW6YR8OrL6Z6wxGqSFEpHW8yX-aL4CpL` (read in full; CO Carol Dones; predecessor to Mod PS17)
- Folder listings: legacy `04 UESC Sansome…` (`1b-w8rqO2rFagFsGtOK3cS2sVNErJ16xI`) incl. `03 MV Review` subfolders (Facility/CO/Contractor — all empty) and `Matthew Schreck - UESC Sansome COR Files` (`1gGrHe0MzoU_2ELabWmRbJ2rvZfo2WpKT`, the working PA-record folder).

**Gmail threads consulted:** `195c917eb7e4a677` (Y5 comments chase/resolution), `19ffbeac6304170c` (phantom-deliverable BLUF), `1a00245fe1a0187c` (MFR transmittal), `1a001b5220ac095c` (scorecard corrections), `19ffc528ddb70983` (witnessing/Kwan), `196460820e8bd971` (R9 latest-M&V-on-file sweep, Apr 2025 — no Sansome shortfall claim), plus a fresh sweep for `Sansome (savings OR shortfall OR "performance assurance")` — 18 threads, no savings-shortfall claim beyond the record above.

**Records searched for and NOT found (do not infer their contents):**
- **Year 3 PA report PDF itself** — the Y3 review workbook, Y3 checklist, and Y4 report's "last year" columns fully reconstruct Y3 numbers ($186,772 proposed / $174,936 reported), but the underlying report file was not located in Drive.
- CO acceptance letters for PA Years 1, 4, and 5 (Y2 letter found; a Y3-era letter is asserted in the dossier as on file but was not located in this pass).
- Any documented resolution of the Y1 "credit for services not rendered" suggestion.
- Any revised/reissued Y5 report carrying the corrected $186,527.
- BAS/VFD audit trail identifying who altered the pump programming pre-Y1.
- Any post-11/30/2024 savings or equipment-performance data (none is owed; none exists).
- "R5 ALL ESPC Verified Savings & Payments Tracker" (`1hldqNYgB-ZHIihlneNfuFqsDeniHF88DZM40lsj_Tec`): not opened — it is an R5 ESPC tracker; Sansome is an R9 UESC and its year-by-year numbers were obtained from the primary reports directly.
- PIR (Post-Installation Report) with the chiller change-order adjustment referenced in Y1/Y5 reports ("See PIR for original adjustment") — not located in Drive.
