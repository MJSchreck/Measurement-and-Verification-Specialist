# Forensic M&V Shortfall Analysis — 06 SDG&E UESC San Diego | 47PK0222F0014

**Prepared:** 2026-08-24 | Analyst: forensic review for Matt Schreck (COR / Zone 7 M&V Lead)
**Contract:** 47PK0222F0014 (formerly 47PK0221F0046, renumbered via Mod PA01) — UESC, SDG&E, 5 facilities (Carter-Keep Courthouse; Otay Mesa LPOE Customhouse & Amistad; Tecate LPOE & Customhouse). Performance payback 5/1/2023–5/1/2035.
**Scope of this review:** Years 1–4 PA cycle (all reported to date), baseline/escalation error quantification, 6/24/26 Y4 findings package, PV data-gap verification-integrity analysis, escalator cross-check.

---

## 0. THE UESC FRAME — What the actual performance commitment is

This is **not a guaranteed-savings contract**. There is **no ESPC-style savings guarantee** and no contractual payment-withholding remedy tied to annual verified savings. The actual commitments are:

- **Government pays a fixed Schedule 5 annual payment** (principal + interest + M&V) each May 1, escalating per the amortization of the $6,434,888 financed principal at 2.98% — total scheduled payments $7,919,170.85. Payment is owed **regardless of annual verified-savings variance**. EMP2 (Le Tran, 4/15/26 email, Gmail 19d933bbd11e34f0): *"with this being a UESC, normally full payments are required regardless. This would be a decision for GSA to make internally."*
- **SDG&E/IES's commitment is a Performance Assurance (PA) plan** (IGA & PA Plan dated 2/11/2022, Drive folder "R9 SD UESC - SDG&E" 1J7yh7vFt2zisA5W8M-sdnfqHY6r6k5Xp): deliver an annual PA report comparing Verified Savings (measured kWh/therms × actual utility rates) against the **Proposed Savings benchmark** — TO Schedule V03 base $554,205 escalated at the contractual **2.54% fixed annual rate** (NIST EERC, 2018 rates; Schedule 5 header).
- Consequence: every "shortfall" below is an **information/benchmark variance**, not a collectible dollar. The government's protections are (a) PA report accuracy, (b) the ability to demand correction/repair of non-performing ECMs, and (c) the acceptance/record trail. Analysis throughout is against that commitment — no guarantee is manufactured.

---

## 1. PY-by-PY Table

Corrected Proposed benchmark = V03 base $554,205 × 1.0254^(N−1) (Le Tran 4/15/26 corrected table; COR Memo CLEAN 6/24/26, Drive 1ADGz9XRcGx6zUu-Ws45CH_9XrlLOG6H5PMyjfQuGfeI). Verified $ = IES "GSA APPENDIX A YEAR-4 Verified Savings 20260528.xlsx" (Drive 1BbLkr3LFFQFuz84D9jvQIPLe8mmgR6nD), ACCRUED SAVINGS tab.

| PY | Period | Corrected Proposed (V03 @2.54%) | Proposed as used by IES | Verified $ | Variance vs corrected | % | Cumulative | Schedule 5 payment / status |
|---|---|---|---|---|---|---|---|---|
| 1 | 5/1/2022–5/1/2023 (report labels "January to May 1st, 2023") | $554,205 | Original: flat $554,205; Jan-2026 revision: $582,716 per Yr1 tab (also cited as $560,147 in 3/2/26 briefing — matches no clean derivation) | $11,232 | **−$542,973** | −98.0% | −$542,973 | $557,519 due 5/1/23 — **payment execution not evidenced in Drive/Gmail** (3/2/26 briefing asked CO to confirm) |
| 2 | 5/2/2023–5/1/2024 | $568,282 | Original: flat $554,205; revision: $582,716 (off-by-one = V03 Y3) | $362,534 (briefing cited $362,578 from earlier version) | **−$205,748** | −36.2% | −$748,721 | $571,679.98 due 5/1/24 — **payment not evidenced** (same open CO confirmation) |
| 3 | 5/2/2024–5/1/2025 | $582,716 | Original: flat $554,205; revision: $597,517 (off-by-one = V03 Y4) | $575,495 | **−$7,221** | −1.24% | −$755,942 | $586,200.65 — invoice 4307-003 paid after funding-doc fix; Mod PA0013 +$2.63; RR EC2025062500193 appr. 6/25/25 |
| 4 | 5/2/2025–5/1/2026 | $597,517 | First submission 5/28/26: **$612,648** (≈ corrected **Y5** value $612,694 − $46) | $590,713 | **−$6,804** | −1.14% (IES reported −3.58%/−$21,935 vs its wrong baseline) | −$762,746 | $601,090.15 — Mod PA0016 obligated $601,090.00 4/23/26; RR EC2026042700141 appr. 4/27/26; paid ~5/1/26 (Gmail 19de42599198a50b) |
| 5–13 | 5/2/2026 → 5/1/2035 | $612,694 → $748,842 (13-yr total $8,411,716) | — | record not applicable yet | — | — | — | Next payment $616,357.84 due 5/1/27 |

**Cumulative position through Y4:** Verified accrued **$1,539,973** vs corrected proposed **$2,302,720** → −$762,747 (−33%), of which **$748,721 (98%) is Years 1–2 construction-period timing**. Payments made Y1–4 total **$2,316,489.78** — i.e., the government has paid **~$776,516 more than verified savings to date**. Under the UESC structure that is contractual, not recoverable; it is stated here because the question "did payments over- or under-pay the utility" must be answered against the actual commitment (Section 3, item L-6).

---

## 2. Shortfall Inventory (every year and ECM where verified < benchmark)

**Y1 — −$542,973 (−98%).** Cause per record: government (Kory Swanson era) **directed IES to align PA Year 1 with Payment #1 date (5/1/2023)** while construction was still in progress; Carter-Keep ECMs captured only 16–22 days of savings, HVAC/PV 0%. IES: *"Normally these savings would be tracked as 'construction period' savings… we were specifically tasked with this change… by the customer"* (Yr1 Comments tab, workbook 1a-9xceA3HQuvPeSn3g_iI5vLrSnAaCj8z7QB1Tj1O1I / 1pgmOgVJn0M3xXw0aKJIzDceYWLMoRnUf). Disposition: absorbed — full $557,519 payment scheduled anyway. Not cured, not withheld against. Note: original Y1 Table 5 understated verified as $4,653; corrected to $11,234 on Le Tran's comment ($11,232 in final accrued table).

**Y2 — −$205,748 (−36.2%).** Same construction-period cause (IES report header: construction still in progress in Y2). HVAC at Customhouse/Amistad only 46% of year, Tecate PV 79%, Customhouse PV 38%, Amistad PV 0% (Y4 workbook NOTES tab). 3/2/26 briefing recommendation: **accept with documented MFR caveat** — "the data is the data. Year 3 is the first meaningful comparison." Disposition: absorbed; acceptance still not formalized (no acceptance letter found).

**Y3 — −$7,221 (−1.24%).** First full-year data point. No specific ECM failure attributed by reviewer; residual variance within normal range (briefing: "well within acceptable range"). Absorbed via full payment. IES's off-by-one baseline had inflated this to −$22,022 (−3.69%).

**Y4 — −$6,804 (−1.14%) against corrected baseline; IES reported −$21,935 (−3.58%).** Site-level splits (Y4 Appendix A, Savings Comparison rows):
- Carter-Keep Courthouse: verified $202,917 vs proposed $206,907 → **−$3,990 (−1.9%)**
- Otay Mesa Customhouse: verified $101,088 vs proposed $117,913 → **−$16,825 (−14.3%)** — largest single-site shortfall; includes 87,150 kWh and 315-therm gaps; not explained in records read — question for IES.
- Otay Mesa Amistad: verified $174,147 vs $168,458 → **+$5,689 (+3.4%)** (partial offset)
- Tecate: verified $112,561 vs $119,370 → **−$6,809 (−5.7%)**
Disposition: report unaccepted; COR findings package with CO 6/24/26, no CO response through 8/24/26.

**Cross-cutting — PV "verified" savings are not verified in ANY year.** All three PV ECMs are carried at Helioscope *expected* values because generation data was never delivered: Y4 amounts Tecate RCM-1 $86,319, Customhouse RCM-1A $36,017, Amistad RCM-1A $109,538 = **$231,874, i.e., 39.3% of the Y4 "verified" total**, each flagged "\* Expected savings, not verified" (Y4 Appendix A). Same treatment in Y2–Y3 (Y3 SDG&E response 12/12/25: "Unfortunately there are no PV meter data yet"). Workbook note: *"Verified savings will remain zero until data are provided, per verification method stipulated in PA plan"* — yet the summary tables report expected values inside the verified totals rather than zero. See ledger item L-5.

---

## 3. Attribution Ledger

| # | Block | $ | Classification | Evidence / confidence |
|---|---|---|---|---|
| L-1 | Y1–Y2 construction-period variance | **−$748,721** | **GOVERNMENT-RESPONSIBLE ADJUSTMENT** | Government directed PA-year alignment to the payment schedule despite ongoing construction (IES responses, Yr1 tab; briefing Decision 4). Beneficial-use dates 5/17/23–5/3/24 postdate PY1. Confidence: **High** for the schedule-alignment cause; the counterfactual (savings would have accrued as construction-period savings under a normal PA sequence) means this is timing, not lost value — but the record contains no reconciliation showing those savings were ever recaptured. |
| L-2 | Proposed Savings baseline errors, Y1–4 (flat, then off-by-one, then Y4 $612,648) | $0 cash / reporting distortion up to **±$28,511/yr** (see Section 4 table) | **BASELINE / METHODOLOGY — introduced by IES** (savings computation entity for SDG&E) | Le Tran comments 8/16/25 & 12/9/25; IES admission 1/13/26 ("The proposed savings rate is not escalated. Is it requested to escalate…?"); EMP2 confirmation 4/15/26 (Gmail 19d933bbd11e34f0); COR memos 4/1, 4/15, 6/24/26. Confidence: **High**. Note direction: the original flat baseline **favored IES/SDG&E optics** (understated benchmark by $14,077 in Y2 and $28,511 in Y3); the revised off-by-one **disfavored them** ($14,434–$15,131/yr overstated); no evidence of intent — pattern is consistent with confusion between rate-table escalation (done correctly) and benchmark anchoring. |
| L-3 | Y3 residual shortfall | −$7,221 | CONTRACTOR PERFORMANCE (minor), absorbed under UESC | 1.24%, no ECM-level cause identified; within reviewer tolerance. Confidence: Med. |
| L-4 | Y4 residual shortfall, concentrated at Otay Mesa Customhouse (−$16,825 / −14.3% site-level; net −$6,804 project) | −$6,804 net | **DISPUTED / UNDETERMINED** | Would be resolved by: IES ECM-level variance narrative for Customhouse (ECM 8 chiller / ECM 10-11 boiler-VFD / lighting runtime) in the corrected Y4 resubmittal. Confidence: n/a — evidence outstanding. |
| L-5 | PV expected-values inside "verified" totals ($231,874 in Y4; similar in Y3; partial Y2) | up to **$231,874/yr unverifiable** | **GOVERNMENT-RESPONSIBLE (data provision) + contractor presentation issue** | PA plan makes recording/archiving/transmitting PV generation data a **customer (GSA) responsibility** (Y2 report language quoted in Yr2 comments tab). GSA installed EMON/DMON meters but never connected them to the GSA network; devices overwrite after ~2 months, so early-year data is **permanently lost** (Kory Swanson 7/23/25, Gmail 19837adf1a8e0677: Tecate connected ~mid-2025, Otay "should be connected by September [2025]"). No evidence of completion found through 8/24/26, and the Y4 workbook (5/28/26) still carries all PV as expected values. Secondary issue (contractor): totals labeled "verified" embed expected values with only an asterisk, contrary to the PA-plan statement that verified PV = 0 until data provided. Confidence: **High** on responsibility; **Undetermined** on actual PV performance (could be higher or lower than the $231,874/yr booked). |
| L-6 | Payments vs savings position | payments exceed verified savings by ~$776,516 through Y4; and Schedule 5 payments exceed even the corrected proposed benchmark by $3,314→$3,573/yr (**~$50,304 over 13 yrs**) | **BASELINE / METHODOLOGY (structural)** — V03 (8/2024) cut the benchmark to $554,205 but the TO Schedule/payment stream was never restated | 3/2/26 briefing Decision 3; V03 removed-scope costs "already refunded" per briefing (double-recovery check assigned to CO, no determination found). Under the UESC no overpayment claim arises from paying Schedule 5 amounts; the $50,304 is a benchmark-vs-payment gap, not an invoice error. Confidence: High on the numbers; CO determination **pending**. |
| L-7 | V03 baseline adjustments (five scope corrections totaling $9,639/yr: Customhouse OCM-1 $1,821, Tecate ECM-5 $1,494, Customhouse ECM-3 $944, Tecate ECM-9A $3,064, Customhouse ECM-8 chiller $2,316) | −$9,639/yr benchmark; costs refunded | **BASELINE / METHODOLOGY — legitimate, symmetric** | PIR V03 Review tab; Y4 workbook zeroes the removed ECMs on both verified and proposed sides ("BASELINE ADJUSTMENT APPLIED"). Reduced the PIR-stage expected shortfall $12,476 → $2,836. Confidence: High. |

**No NON-ROUTINE ADJUSTMENTS were claimed in any year** — no NRA symmetry issue exists on this contract to date.

---

## 4. Baseline-Error Impact — who benefited, which direction, year by year

The error moved **reported optics only**; zero dollars changed hands because UESC payments are fixed. Impact on the *reported variance* (positive = IES made to look better than reality; negative = worse):

| PY | Correct benchmark | IES benchmark (original reports, flat) | Distortion | IES benchmark (Jan-2026 revision / Y4 first submission) | Distortion |
|---|---|---|---|---|---|
| 1 | $554,205 | $554,205 | $0 | $582,716 (Yr1 tab; briefing also cites $560,147) | **−$28,511** (or −$5,942) — IES looked worse |
| 2 | $568,282 | $554,205 | **+$14,077** — IES looked better | $582,716 | **−$14,434** — worse |
| 3 | $582,716 | $554,205 | **+$28,511** — IES looked better (would have shown a +$21,290 *surplus* instead of the true −$7,221 shortfall) | $597,517 | **−$14,801** — worse (−3.69% reported vs true −1.24%) |
| 4 | $597,517 | — | — | $612,648 (≈ corrected Y5) | **−$15,131** — worse (−3.58% reported vs true −1.14%) |

Net read: the **original flat baseline favored the utility** (benchmark frozen while verified savings rode escalating actual rates — Le Tran 12/9/25: "the Verified Savings just looks better by at least 2.54% every year"); the **botched fix over-corrected against the utility**. Correcting to the right schedule *helps* SDG&E's current reported position (briefing: "The ESCO has zero reason to push back"). **Payments made on the wrong basis neither over- nor under-paid the utility** — the payment stream is Schedule 5, which was never touched by the PA-report error. The only payment-adjacent exposure is L-6's $50,304 Schedule-5-vs-V03 structural gap plus confirmation that Y1–Y2 payments ($1,129,199) were actually disbursed.

**Escalation rate itself is applied correctly everywhere checked.** The Y4 workbook RATE ESC tab compounds 1.0254 cleanly across all years/sites (e.g., Courthouse $0.2680 → $0.3621/kWh); the CLEAN memo confirms "the rate engine compounds cleanly at 2.54% per year. The error is in the Proposed Savings baseline figures." The error is anchoring (which year's value), not arithmetic. Note the rate-table convention (2022 base = index 1.0000, Year 1 = 2023 = 1.0254) is the likely root of the off-by-one: Schedule 5 Note (2) says Year-1 savings already incorporate implementation-period escalation, so Year N = base × 1.0254^(N−1), not ^N.

**Does the escalator error appear anywhere else?**
- **This contract's payment side:** No. PA0016 obligated $601,090.00 vs Schedule 5 $601,090.15; PA0013 added $2.63 for the Y3 rounding gap — cent-level only.
- **Portfolio:** One adjacent pattern found — GSA R2 MLK/Pirnie Y11 (different vendor/region; comment file "260407-1b … MV Report Comments 1-30-26 GH_MBrevise.xlsx", Drive 1cb7Sv-s2Cbh2uthVGvsGTaBu_Iaq-ytZ): ESCO admits TO-4/TO-1 savings "did not escalate uniformly each year even though utility rates are supposed to escalate uniformly… a result of rounding error during contract writing," so apparent utility rates are back-calculated yearly (1.8% vs 1.4% drift). Same failure mode (escalation anchoring in TO schedules) — watch item for whoever owns that file. NORESCO Chicago NDER Y10 was explicitly escalation-checked clean by Jerrud Parker 7/31/26 (Gmail 19fb8e5ff75a5825). No SDG&E-style flat-baseline instance found on Matt's other contracts in records searched.

---

## 5. The 6/24/26 Year-4 Findings Package — every finding, classified

Source: Matt → Felipe Jolles, 6/24/26 (Gmail 19efbb9d91cbd8d7, single message, **no CO reply on thread through 8/24/26**); status note to Kory same day (Gmail 19e713c5128123a9); CLEAN COR memo (Drive 1ADGz9XRcGx6zUu-Ws45CH_9XrlLOG6H5PMyjfQuGfeI).

| # | Finding | Class | Owner | Tag |
|---|---|---|---|---|
| F-1 | Wrong PIID on report cover (Y3 had the same defect inverted — cover showed 47PK022F0014 vs 47PK0221F0046) | Document integrity — mechanical | IES/SDG&E | 🟠 |
| F-2 | Conflicting Year-4 performance-period dates within the report | Document integrity — mechanical (but M&V-relevant: period definition drives pro-rating) | IES/SDG&E | 🟠 |
| F-3 | Embedded editor markup left in the final PDF | QC defect | IES/SDG&E | 🟠 |
| F-4 | **Appendix B (government witnessing) missing/unsigned** — recurring: Y1 Appendix B listed in TOC, never received (open since Le's Yr1 R7 comment); Y3 claimed "Included as Appendix B" | M&V rigor / OIG A240046 file-completeness exposure | IES deliverable + GSA witnessing program | 🔴 |
| F-5 | **Baseline finding:** Y4 §1.3.1 (p.41) compares verified against $612,648; corrected V03 Y4 value is $597,517 (~$15k overstated); reported "3.6% under proposed" is wrong — true variance −1.14% | BASELINE / METHODOLOGY | IES | 🔴 |
| F-6 | Requested CO actions: (a) concur/authorize transmitting defect comments to SDG&E; (b) determine bilateral SF30 to restate TO Schedule to V03 baseline ($554,205 / $8,411,716); (c) document the UESC full-payment determination; (d) require Y1–4 restatement + side-by-side | CO action items — all **unanswered through 8/24/26**; PMO annual-reporting intake held by COR meanwhile | Felipe Jolles (CO) | 🔴 |

---

## 6. Red-Flag Scan

| Checklist item | Result |
|---|---|
| Stipulated values changing year-over-year | 🔴 **Yes** — the Proposed Savings benchmark has now taken four different values for the same years across report versions (flat $554,205 → $560,147/$582,716/$597,517 off-by-one set → $612,648 in Y4) with no contract modification authorizing any of them. Also "static values"/hard-coded savings numbers in Appendix A flagged by Le Tran repeatedly (Y2, Y3 comment tabs) — reviewers cannot trace savings from calculations. |
| Methodology changes without explanation | 🟠 IES's 1/13/26 response ("we understand that we are being directed to escalate the proposed savings rate each year to match the rate used for verified savings") implemented a *different* methodology than directed — evidence the entity computing savings did not understand the benchmark construct; they also stated they had **never seen the TO Schedules** they are measured against (Bottomley 1/28/26, quoted in 3/2/26 briefing). |
| Baseline adjustments that exactly offset shortfalls | 🟢/🟡 V03's $9,639 adjustment cut the PIR expected shortfall from $12,476 (2.2%) to $2,836 (0.5%) — large convenient improvement, but each of the five items has documented scope rationale and costs were refunded; symmetric application confirmed in the Y4 workbook. Watch, not actionable. |
| Asymmetric NRAs | 🟢 No NRAs claimed in any year. |
| "Did not affect savings" claims without traceable explanation | 🟡 Amistad ECM-5: expected savings raised from proposed 14,746 kWh/yr to 105,703 kWh/yr (~7×) via post-award re-evaluation of baseline **hours of operation** ("re-evaluated to be in line with typical exterior lighting"), with only 7 added fixtures. Accepted by reviewer, but this is a post-award baseline-assumption change that inflates reported savings without added scope — the kind of change that should carry documentation. |
| Cumulative negative trend | 🟢 Full-year shortfall is small and stable/narrowing: −1.24% (Y3) → −1.14% (Y4) against the corrected benchmark. |
| Savings increases without ECM additions | 🟡 Same as ECM-5 item above; also Y2 demand savings appeared (567.7 kW) after a comment, with reviewer noting "It would be nice if we had the information to verify this number." |
| GRAs invoked for normal operations | 🟢 None invoked. |
| Wrong contractual escalators | 🔴 Core finding (Section 4). Rate arithmetic correct; benchmark anchoring wrong in every report version to date, still uncorrected in the field. |
| Proposed-values-booked-as-verified | 🔴 PV: $231,874 (39.3%) of the Y4 "verified" total is Helioscope expected values, four years running, because GSA never connected the meters. Compounding risk: early-generation data is unrecoverable (2-month device buffer), so Years 2–4 PV performance can **never** be retroactively verified; the record will rest permanently on stipulated values unless the CO documents that disposition. |

---

## 7. Findings (dollar- and PIID-anchored)

- 🔴 **F-A (47PK0222F0014):** Proposed Savings baseline wrong in all four PA report cycles; corrected schedule is $554,205 base / 13-yr $8,411,716. Y4 uses $612,648 vs correct $597,517. CO determinations (IES restatement of Y1–4, SF30 vs file-correction, UESC payment determination) requested 4/1/26, 4/15/26, and 6/24/26 — **no CO response found through 8/24/26**; PMO annual-reporting submittal held; Y2/Y3/Y4 acceptances all stalled behind it.
- 🔴 **F-B:** PV verification void — $231,874/yr (39.3% of Y4 verified total) booked from expected values; GSA-side meter connection incomplete ~3 years after installation; pre-connection data permanently overwritten. Responsibility: government (PA plan assigns data provision to customer). Needed: connection status confirmation from region, and a CO-documented disposition for the unverifiable Y2–Y4 PV block.
- 🔴 **F-C:** Witnessing record (Appendix B) missing for Y1 and Y4 — A240046 file-completeness exposure on a contract whose acceptance letters (Y2–Y4) also don't exist yet.
- 🟠 **F-D:** Otay Mesa Customhouse Y4 site shortfall −$16,825 (−14.3%) — unexplained in records read; require ECM-level variance narrative in the Y4 resubmittal.
- 🟠 **F-E:** Y1–Y2 payment execution ($557,519 + $571,679.98 = $1,129,199) still unevidenced; CO asked 3/2/26 to confirm the $1,715,400 Y1–3 total was paid. Confirm for Tab 39.
- 🟠 **F-F:** Schedule 5 vs V03 structural gap $3,314→$3,573/yr (~$50,304/13 yr): government pays against the pre-V03 baseline. Briefing recommendation "likely accept as-is" contingent on confirming V03 refunds prevent double-recovery — that confirmation is not in the record.
- 🟡 **F-G:** Amistad ECM-5 baseline-hours re-evaluation (7× expected-savings increase) and Y2 demand-savings appearance — verify supporting data next PY.
- 🟡 **F-H:** Escalation-anchoring failure mode recurs on GSA R2 MLK/Pirnie (rounding-driven non-uniform TO escalation) — portfolio-level watch; Matt's other contracts show no SDG&E-style instance in records searched.
- 🟢 **F-I:** Verified-side measurement (actual kWh/therms × actual rates) has never been in dispute for non-PV ECMs; Y3/Y4 full-year performance is within ~1.2% of the corrected benchmark — the underlying project is performing essentially as proposed.
- 🟢 **F-J:** V03 baseline adjustments applied symmetrically with costs refunded; no NRA games detected.

---

## 8. Sources & Gaps

**Drive files read:**
- SDG&E Briefing Document, CO direction mtg 3/2/26 — 1n20v0VbWHTKlC87d45qfy9TsMH9ZIc9eU0gMRqGc0ZM
- SDGE UESC-Escalation Mod COR Memo V1/V2 (4/1 + 4/15/26) — 1mj6Ivzr0ebKDM7bfXm6ZR083wq3EarNaMO28cteEa88
- SDGE_UESC_Escalation_Baseline_COR_Memo_CLEAN_2026-06-24 — 1ADGz9XRcGx6zUu-Ws45CH_9XrlLOG6H5PMyjfQuGfeI
- SDGE UESC Performance Assurance Report Comments (Kory's live sheet, Yr1/Yr2/Yr3 tabs + PIR V03 Review tab) — 1a-9xceA3HQuvPeSn3g_iI5vLrSnAaCj8z7QB1Tj1O1I
- SDGE UESC (Year 3) Performance Assurance Report Comments_1-30-26.xlsx — 1pgmOgVJn0M3xXw0aKJIzDceYWLMoRnUf and 1-SMCUee_P-DpttqmH66gcg4FmZcbIh6P (metadata/snippet incl. 1/30/26 GSA responses)
- GSA APPENDIX A YEAR-4 Verified Savings 20260528.xlsx — 1BbLkr3LFFQFuz84D9jvQIPLe8mmgR6nD (NOTES, YEAR-4 SAVINGS, Savings Comparison, ACCRUED SAVINGS, BASE ADJ, RATE ESC tabs)
- 260407-1b GSA R2 MLK and Pirnie Y11 MV Report Comments (escalation cross-check) — 1cb7Sv-s2Cbh2uthVGvsGTaBu_Iaq-ytZ

**Gmail threads read:** 19e713c5128123a9 (Y4 PA report submittal + review status, 9 msgs, full); 19efbb9d91cbd8d7 (6/24/26 COR findings package to CO — single message, unanswered); 19d933bbd11e34f0 (Le Tran 4/15/26 root-cause correction + corrected 13-yr table, full); search results across 19837adf1a8e0677 (PV/EMON-DMON 7/23/25), 1984237b027c5a26 (static values 7/25/25), 1994fb31af06ba32 (Y1+2 responses 9/15/25), 19fb8e5ff75a5825 (NORESCO Chicago escalation check), plus portfolio escalation search (201 hits scanned at snippet level).

**Records sought and NOT found (never interpolated):**
- Y1 (5/1/23) and Y2 (5/1/24) payment execution evidence — open CO confirmation since 3/2/26.
- Any CO (Felipe Jolles) response to the 4/1, 4/15, or 6/24/26 COR memos; any SF30 baseline mod; any UESC payment determination.
- Acceptance letters for PA Years 2, 3, 4 (folder exists, no letters).
- Y1 Appendix B and Y4 Appendix B (witnessing) — never delivered.
- Evidence that Otay Mesa EMON/DMON meters (and SMA inverters) were connected to the GSA network after Kory's "by September" 2025 estimate — none; Y4 workbook confirms still no PV data at 5/28/26.
- IES's restated Y1–4 side-by-side (Action 2 of the CLEAN memo) — not yet produced.
- "GSA Post-Install Report Appendix A REV6.xlsx" — referenced by IES 1/13/26; Le couldn't locate it (open item 17).
- "R5 ALL ESPC Verified Savings & Payments Tracker" (1hldqNYgB-ZHIihlneNfuFqsDeniHF88DZM40lsj_Tec) — not read: it is a Region 5 ESPC tracker; this is a Region 9 UESC outside its scope. Noted as unconsulted rather than checked-empty.
- IES Y1 revised baseline discrepancy ($560,147 per briefing vs $582,716 per 1/30/26 Yr1 tab) — both cited to source; which figure appears in which table of the 1/23/26 revision could not be resolved without the revised Y1 report PDF itself (not located in Drive under a distinct title).
