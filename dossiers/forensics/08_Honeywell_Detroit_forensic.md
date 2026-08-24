# FORENSIC M&V ANALYSIS — Contract 08: Honeywell ENABLE Detroit ESPC
## PIID 47PF0020F0671 (IDV 47QSWA18D0057) | Theodore Levin US Courthouse, McNamara FB, 985 Michigan Ave Garage | Performance Period 3/1/2022–2/28/2038

**Prepared:** 2026-08-24, for Matt Schreck (COR / M&V Lead, Zone 7)
**Scope:** PY1–PY4 (3/1/2022–2/28/2026) + construction-period savings. Read-only forensic reconstruction from Drive + Gmail; no interpolation — every figure cited.
**Framing question (per tasking):** This contract *always* beats guarantee on paper. Is the surplus REAL — or an artifact of stipulation?

---

## Executive answer

**The surplus is arithmetic, not measurement.** Verified savings on this contract are computed from **physical quantities that have been 100% identical in all four performance years** (fixed at the Post-Installation Report), multiplied by **contract-stipulated escalated rates** (electric 1.55%/yr, gas & steam 3.41%/yr, water 2.00%/yr). The guarantee is set at **exactly 97.0% of the Schedule-1 estimate** in every year. Therefore verified savings exceed guarantee by ~2.8–2.9% every year *by construction*, and the "growing surplus" (+$34,417 → +$38,838) grows at exactly the escalation rate. The annual M&V consists only of pass/fail checks (boiler combustion spot tests against manufacturer curves; lighting visual walk-throughs) that have never triggered an adjustment. No annual quantity has ever been re-measured. That is what the accepted M&V Plan (Mod PS0008, Option A) requires — this is not a false claim by Honeywell — but the surplus should **not** be briefed as measured outperformance, and a real under-delivery of up to ~3% of the proposal would be **invisible** to this M&V design.

The one year the claim was NOT purely mechanical — PY2 — Honeywell's spreadsheet **over-claimed by $14,719** (wrong escalated gas rates + misapplied $7,344 gas fixed charge), caught only by CO line-item review and corrected in the accepted Ver3. That is the empirical answer to "is the number trustworthy without checking": no.

---

## 1. PY-by-PY table (guaranteed vs verified)

| Year | Period | Guaranteed $ | Verified $ (accepted) | Variance $ | Variance % | Cumulative variance | Source |
|---|---|---|---|---|---|---|---|
| CP (Yr 0) | Jul 2020 – Feb 2022 | 342,007 | 366,195 | **+24,188** | +7.1% | +24,188 | PY1 report §1.3 (file 1a-RrQNYWxiUQkMNp2XoAfQFDqavUKuUg); PS0005 |
| PY1 | 3/1/2022–2/28/2023 | 1,211,316 | 1,245,550 → **restated 1,245,733** (fall 2024) | +34,234 → **+34,417** | +2.84% | +58,605 (incl. CP) | PY1 Rev.01 report (1a-RrQNY…); restatement documented in PY3 report pp.15–16 (PS0017 attachment, 10ntU1grKI3nI11ps15p5JDIj6bXL_LHS) |
| PY2 | 3/1/2023–2/29/2024 | 1,252,045 | initially claimed **1,302,602**; accepted (Ver3) **1,287,883** | claimed +50,557; accepted **+35,838** | +2.86% | +94,443 | Initial Yr02 report Table 2 (1NFUFyZ-Aa3WSTv4pjrIMxYYwJYhSiJbS); accepted value per PY3/PY4 Table 3; PS0015 |
| PY3 | 3/1/2024–2/28/2025 | 1,294,154 | **1,331,465** | **+37,311** | +2.88% | +131,754 | PY3 report Rev1 (attached to PS0017, 10ntU1grK…); PS0017 eff. 6/2/2025 |
| PY4 | 3/1/2025–2/28/2026 | 1,337,689 | **1,376,527** | **+38,838** | +2.90% | +170,592 | PY4 report Tables 2–3 (1bIbtj660T-C40bQkNlwSif9n4cYYo4L6 / Doc 1izs2vY_bJ…); PS0019 exec. 6/18/2026 |
| **PY1–PY4 total** | | **5,095,204** | **5,241,608** | **+146,404** | +2.87% | (+170,592 incl. CP) | PY4 report Table 3 |

Payments each year = guaranteed − $1 (Schedule 1, column f/g); PY payments $1,211,315 / $1,252,044 / $1,294,153 / $1,337,688 / PY5 $1,382,697 obligated via PO0018. **No year required a shortfall credit, withholding, or make-good.** No record of any year with verified < guaranteed was found — and none is marked "record not found": all four PY reports (PY2 via mod-incorporated restatements) were located and read.

**The structural identity (verified from source documents):**
- Guarantee = 0.970 × Schedule-1 estimate, exactly, every year (e.g., 1,248,779 × 0.97 = 1,211,316; 1,379,060 × 0.97 = 1,337,689). Schedule 1, reproduced in every annual report.
- Verified = Proposed + fixed as-built (PIR) net delta. PY4: 1,379,060 + (1,385 − 8,584 + 3,220 + 1,446) = 1,379,060 − 2,533 = 1,376,527. Exact.
- Surplus = 3.0% guarantee margin − ~0.2% as-built net shortfall ≈ 2.8–2.9%/yr, escalating at ~3.38%/yr blended. The PY1→PY4 surplus growth (34,417→38,838) is pure escalation arithmetic, **not** improving performance.

## 2. ECM-level breakdown — verified $ by year, and what is stipulated vs measured

| ECM | PY1 (accepted / restated) | PY2 (initial claim)* | PY3 | PY4 | Annually measured? | What is actually stipulated |
|---|---|---|---|---|---|---|
| 1.1 Levin Boilers | 652,893 / 652,897 | 682,290* | 697,747 | 721,318 | Combustion-efficiency spot test only (3 boilers × 20/40/80% firing) | Steam savings 23,132 MBtu/yr (BIN model, TMY3, fixed at PIR); gas penalty −23,914 MBtu; electric −1,592 kWh; water 1,387 kgal (from ONE January-2020 metering exercise, IGA pp.10–13); all rates (Table 6) |
| 1.2 PVM Boilers | 523,380 / 523,559 | 549,874* | 562,277 | 582,660 | Combustion-efficiency spot test only (8 boilers) | Steam savings 20,650 MBtu/yr; gas penalty −17,803 MBtu; electric −1,313,142 kWh (as-built electric DHW); all fixed since PIR |
| 2.1 Levin Lighting | 20,686 / 20,686 | 21,034* | 21,332 | 21,663 | Visual walk-through only ("no changes" → as-built booked) | kWh 330,089; kW 32.8/mo; operating hours — all from 2021 As-built IGA Tool |
| 2.2 985 Garage Lighting | 48,591 / 48,591 | 49,406* | 50,109 | 50,886 | Visual walk-through only | kWh 738,442; kW 82.3/mo; hours — all from 2021 As-built IGA Tool |
| **Total** | 1,245,550 / **1,245,733** | 1,302,602* → **1,287,883 accepted** | **1,331,465** | **1,376,527** | | |

\* PY2 per-ECM figures shown are from the **initial** (April 2024) submission, which contained rate errors; the accepted Ver3 total is $1,287,883 but its per-ECM breakdown could not be located in Drive (Ver3-Final PDF not filed — see Gaps).

**Physical quantities are identical in every year** (project totals: 1,225 MBtu, −246,203 kWh, 709.5 kW-mo, −41,717 MBtu gas, +43,783 MBtu steam, 1,387 kgal — PY1 Table 2 = PY4 Table 2 = PY4 Table 3 rows for all four years). **~94.5% of gross savings dollars is purchased-steam elimination that is never re-measured** — the district steam service is disconnected, so there is no meter against which to verify; the quantity is a 1989-method ASHRAE bin model output calibrated once, pre-construction. The only instrumented annual measurement on the contract is the boiler combustion test, and per the M&V Plan it is a **one-way check**: "Recalculate savings if the average measured thermal efficiency is below the average manufacturer's thermal efficiency" (M&V Plan p.4, quoted in YR2 comment log #10). Measured ≥ curve → book as-built numbers unchanged. It has passed all four years (PY1: Levin +0.17%, PVM +0.60%; PY2: Levin +2.72%, PVM +0.53%; PY4: Levin +0.30%, PVM +0.44%).

## 3. Shortfall inventory

**Years with verified < guaranteed: none (PY1–PY4).** There are therefore no true shortfall dollars to attribute. The forensically relevant blocks are the places where *claimed* savings were wrong, where performance ran below *proposal*, or where the record is internally inconsistent:

| # | Block | Magnitude | What happened | Disposition |
|---|---|---|---|---|
| S-1 | PY2 initial over-claim | **+$14,719 claimed above the correct number** ($1,302,602 vs $1,287,883) | Wrong escalated gas rates (rounding drift: $5.11/5.30 vs correct $5.102/5.276) and a $7,344 PVM natural-gas **fixed charge misapplied** ("A fix charge of $7,344 in N.G. Savings … not used correctly" — Honeywell's own words, YR2 log #13/14). CO caught it by noting verified savings escalating 4.50%/5.06% YoY when rates only escalate 3.38%/3.56% (YR2 log #11/13) | Cured — Ver3-Final (10/25/2024) accepted at $1,287,883 via PS0015 after an Oct 10, 2024 meeting resolving the fixed-charge treatment (applies independently per building) |
| S-2 | PY1 mis-statement | **−$183 net** (accepted $1,245,550; corrected $1,245,733) | Same rate/fixed-charge errors flowed through PY1; PY1 report was NOT resubmitted — correction documented in the PY3 report ("Adjustment – Update to Year One (PY01) Verified Savings, per Government Comments," PY3 report p.15) | Absorbed/documented; direction favored the Government trivially |
| S-3 | ECM 1.2 as-built deviation | **−$8,584/yr (PY4 dollars; −$8,928 PY1)** below proposal, in perpetuity | Honeywell installed **electric** DHW heaters at PVM instead of the gas units proposed in the IGA — a contractor design deviation that raises the electric penalty (−1,313,142 kWh vs proposed −888,198) more than it cuts the gas penalty | Absorbed inside the 3% guarantee margin; never charged to Honeywell; partially offset by favorable as-built deltas on ECM 1.1 (+$1,385), 2.1 (+$3,220), 2.2 (+$1,446, elevator lighting descoped) |
| S-4 | PY1 warranty defects | $0 booked | Levin exhaust duct/pipe misaligned (condensate leak; W.J. O'Neal realigned under warranty); condensate neutralizers non-performing at BOTH buildings — **condensate at pH 3–5 discharged to building drains**; PVM replaced fall 2022, Levin July 2023 | Cured under warranty at contractor expense. **Initially omitted from the PY1 report; disclosed only after GSA comments 20/21/25 forced the narrative in** (YR1 comment log). "No savings impact" is plausible (savings are not computed from anything the neutralizers touch) but was asserted, not demonstrated |
| S-5 | PY4 latent O&M items | $0 booked | RL Deppmann tech noted Levin **Boiler #3 fan-housing vibration** ("recommended that the issue be investigated before it causes a failure") and that boiler **maintenance timers had not been reset** at last service (PY4 report §2.1.2); one 985 stairwell LED burnt out (warranty claim pending) | Open. Not carried into the report's Table 4/5 issues tables, which state "no issues." Government owns all O&M/repair/replacement — a Boiler #3 failure would be a **government-responsible** savings loss under the Risk & Responsibility Matrix |

## 4. Attribution ledger

No shortfall dollars exist to split; the ledger below classifies every disputed/notable savings block. Headline: **contractor-owed $0 · government-absorbed $0 · disputed $0** in cash terms — with the caveat that the M&V design cannot surface a sub-3% real shortfall, so "zero" is partly unfalsifiable.

| Block | Classification | Evidence | Confidence |
|---|---|---|---|
| PY2 +$14,719 initial over-claim (S-1) | **BASELINE / METHODOLOGY** — contractor-introduced calculation errors (escalator rounding + fixed-charge misapplication), not a performance issue; government reviewer (CO Parker) introduced the correction | YR2 comment log #4, 5, 11, 13, 14, 15 (Sheet 1eseLtjbW2oWJCRSvIc7diugkmpS0LA6kXDZvfpUIlSo); PS0015 | High |
| PY1 −$183 restatement (S-2) | **BASELINE / METHODOLOGY** — same root cause; corrected transparently in PY3 report rather than resubmission (CO-approved shortcut) | PY3 report p.15 (PS0017 attachment); YR2 log #16 | High |
| ECM 1.2 electric-DHW deviation, −$8.6–8.9k/yr vs proposal (S-3) | **CONTRACTOR PERFORMANCE DEFICIENCY** (install deviation from IGA design) — permanently reduces savings vs proposal; cost the Government nothing only because the 97% guarantee margin absorbs it | PIR Rev.04 (PS0009); every annual report §1.1 as-built variance bullets | High |
| PY1 neutralizer/duct defects (S-4) | **CONTRACTOR PERFORMANCE DEFICIENCY** (install defects) — fully cured under warranty at contractor expense; $0 savings impact claim accepted | YR1 comment log #20/21/25 (1cpwb2Zh3eRGHlGmtz2FMIE13Bc7RSMofyqIupAu8LeA); PY1 report §2.1.2/2.2.2 | High |
| The +$146,404 cumulative "surplus" itself | **BASELINE / METHODOLOGY artifact** — savings are contractually defined (stipulated quantities × stipulated escalated rates against a 97%-of-estimate guarantee), not measured. Introduced by the contract/M&V Plan structure both parties signed (IGA 7/13/2020; M&V Plan PS0008) — not misconduct, but not evidence of outperformance either | Sections 1–2 above; Schedule 1; M&V Plan one-way adjustment rule | High |
| PY4 M&V activity dates (report: 4/7–4/8/2026; COR record/calendar/schedule emails: 3/23–3/25/2026) | **DISPUTED / UNDETERMINED** — the accepted PY4 report's §2.x.2 dates conflict with Matt's own 5/20/2026 COR review email and the confirmed schedule. Resolution: pull the signed/dated combustion test strips and witnessing forms in PY4 report Appendix §3.1–3.4 and RL Deppmann's service records; confirm which dates are real and whether a second (April) visit occurred | PY4 report §2.1.2/2.2.2/2.3.2/2.4.2 vs Gmail 19d01a47dd04e986 (Kinne 3/18: "All confirmed for 3/23–3/24"), Matt's 19e45cabb1570cfc (5/20: "McNamara 3/23, Levin+985 3/24"), calendar notice 19d1980bdc6ead4e | Medium (that it is a documentation error rather than a phantom visit) |
| PVM boilers 7 & 8 anomalous 95–96% efficiency readings (PY2) | **DISPUTED → resolved as data-quality watch** — readings "significantly higher" than physically expected; disposition was an agreement to re-check readings going forward, not a re-test | YR2 log #17; PY3/PY4 running issues item 1 | Medium |

## 5. Red-flag scan (checklist per tasking)

| Checklist item | Finding |
|---|---|
| Stipulated values changing year-over-year | **YES — rates, not quantities.** Gas escalated-rate values and the $7,344 fixed-charge treatment changed between PY1/PY2-initial and PY2-Ver3/PY3+ (documented, CO-driven, net correction *reduced* Honeywell's claim by $14,719). Quantities have never moved. As-built variance narrative dollars were also restated twice (PY2, PY3) due to "missing or incorrect workbook links" — Honeywell's own admission, twice (YR3 log #1) |
| Methodology changes without explanation | None found. All changes ran through the comment logs and are traceable |
| Baseline adjustments that exactly offset shortfalls | None — no shortfalls, no baseline adjustments, no NRAs in any year ("There are no savings adjustments for this year," §1.5, all four reports) |
| Asymmetric NRAs | No NRAs at all. **But the boiler-efficiency mechanism is structurally one-way**: measured-below-curve reduces savings; measured-above-curve changes nothing — and the test has never failed, once with implausibly high readings (boilers 7&8). The asymmetry is in the *pass/fail evidence*, not in dollars |
| "Did not affect savings" claims without traceable explanation | **Pattern present.** PY1 as-built extra works "did not impact energy and cost savings" (accepted without quantification); PY1 warranty defects initially omitted entirely; PY4 Table 4/5 say "no issues" while §2.1.2 records Boiler #3 fan vibration and unreset maintenance timers. Claims are *plausible* under the stipulated method (which is precisely the problem — nothing operational can affect "savings") |
| Cumulative negative trend | None. Positive trend — but the growth is exactly the escalator, i.e., informationally empty |
| Savings increases without ECM additions | Verified $ rises ~3.38%/yr with zero scope change — by design (deemed rates). Not an anomaly under this contract; must not be briefed as improvement |
| GRAs invoked for normal operations | Never invoked — zero government impacts claimed in four years. (Notable in the other direction: GSA carries all O&M risk, so future GRA claims (e.g., a Boiler #3 failure) are the live exposure) |
| Wrong contractual escalators | PY1/PY2-initial used mis-rounded gas rates (caught, corrected to $4.933 base / 3-decimal convention); steam base-rate question resolved as a unit conversion ($29.64/klb = $32.078/MMBtu at 1.0823 MBtu/klb). PY3/PY4 rate tables recompute correctly (0.0366×1.0155⁴=0.0389; 32.078×1.0341⁴=36.682 ✓) |
| (Additional) Record hygiene | PY4 report is a recycled workbook/document: embedded PDF title "GSA R5 Detroit ESPC Enable **Yr02**", TOC section header "Verified **Third** Year Savings", §1.4 text "no issues with **Yr03**" — in the *accepted* PY4 record. Consistent with the broken-links history; raises the odds of silent carry-forward errors |

## 6. Findings (tagged, dollar- and PIID-anchored)

- 🔴 **The +$146,404 (PY1–PY4) surplus on 47PF0020F0671 is contractually manufactured, not measured.** Quantities static since the PIR; guarantee = 97.0% of estimate; rates deemed. A real under-delivery of up to ~$41k/yr (3% of proposal) would be invisible to the accepted M&V design. Action: brief leadership/CPARS with "verified per Option A stipulations" language, never "outperformed guarantee"; at the next natural checkpoint (PY5 report or the FY27 IGA-tool refresh conversation) request a one-time reconciliation of modeled gas penalty vs actual DTE gas bills at Levin/PVM — the gas account is metered and WOULD reveal boiler-plant drift.
- 🔴 **PY2 demonstrated the claim can be materially wrong: initial submission over-stated verified savings by $14,719 (1.13%)** from spreadsheet errors alone; only CO line-item review caught it. The same workbook produced link errors again in PY3. Action: require the calculation workbook (not just the PDF) with the PY5 submission and diff the rate cells against Table 6b.
- 🟠 **PY4 M&V dates in the accepted report (4/7–4/8/2026) conflict with the Government's own witnessing record (3/23–3/24/2026)** — Matt's 5/20/2026 email, the CO's schedule thread, and calendar entries all say March. Ask Honeywell (Kinne) and CO Parker to reconcile against the signed test strips in Appendix 3.1–3.4; if the March walks are the real ones, the report's dates are wrong in an accepted contractual record (and if April visits happened, the CORs' witnessing record is incomplete). Either way it compounds the already-documented "M&V performed outside the PY" issue (CO comment #2, YR4 log).
- 🟠 **PVM boilers 7 & 8 posted physically implausible 95–96% combustion readings in PY2** — the only instrumented annual measurement on the contract produced suspect data and the resolution was contractor self-checking. Action: at PY5 witnessing, have the GSA witness photograph analyzer readouts and initial each test strip; readings above ~91% (condensing limit at observed RWTs) get re-run on the spot.
- 🟡 **Levin Boiler #3 fan-housing vibration + unreset maintenance timers (PY4 report §2.1.2) — Government owns O&M.** If it fails, the savings loss is government-responsible and Honeywell will be entitled to a GRA. Cheap insurance: task Levin O&M now (Blake) and log the repair; watch the PY5 report for the first-ever GRA on this contract.
- 🟡 **One warranty item open:** 985 Garage stairwell LED (PY4 report §2.4.2) — small, but it is the only open contractor-side item; confirm replacement before PY5 report acceptance.
- 🟢 **No NRAs, no government-impact claims, no withholdings, no make-goods in four years; payments exactly per Schedule 1 (guaranteed − $1); escalators verified correct from PY3 onward; PY1/PY2 corrections were documented transparently and net in the Government's favor.** The CO's (Parker) YR1/YR2 reviews were genuinely rigorous — comment logs show 27 and 20 numbered comments respectively with multiple "Not accepted" rounds; the review muscle, not the M&V design, is what protects this contract.
- 🟢 **Construction-period savings also verified above guarantee** (+$24,188: $366,195 vs $342,007), consistent with the pattern.

## 7. Sources & gaps

**Drive documents read (full or targeted-complete):**
- PY4 Annual M&V Report (submitted 4/22–24/2026): Google Doc conversion 1izs2vY_bJ-gajt7ZuUTOcu6-lpvK4M6SHwrguHyOHf0 (read in full, 1,109 extracted lines) — PDF originals 1bIbtj660T-C40bQkNlwSif9n4cYYo4L6, 17naxIDLbormlk6ZsyC1rlmuYVNxcYJQ5, rev copy 1VBtCJN4hEx7Ia2doJkVTGiPQ4I4GoK5I (headline/metadata).
- PY1 Report Rev.01 (Aug 2023): 1a-RrQNYWxiUQkMNp2XoAfQFDqavUKuUg — read summary, all tables, ECM 1.1/1.2 sections; lighting/appendix scanned.
- PY2 Report initial (Apr 2024): 1NFUFyZ-Aa3WSTv4pjrIMxYYwJYhSiJbS — summary, Tables 1–5, ECM M&V dates (1/30–31/2024), per-ECM verified table.
- PY3 Report Rev1 (5/20/2025) via Mod PS0017 SF30 package: 10ntU1grKI3nI11ps15p5JDIj6bXL_LHS — summary, PY2/PY1 restatement sections, Tables 1–5, M&V dates (1/28–30/2025).
- Comment logs: YR1 1cpwb2Zh3eRGHlGmtz2FMIE13Bc7RSMofyqIupAu8LeA (27 comments, 5 review rounds, to 10/25/2023); YR2 1eseLtjbW2oWJCRSvIc7diugkmpS0LA6kXDZvfpUIlSo (20 comments, 6 rounds, to 10/29/2024); YR3 17LU1hqNo7I782YATN3dFyBSEydDYVnYZ_nMm6HQ8MZQ (3 comments); YR4 1fZS4e915j1eus9rVuVgx5Q-Tut5rXbmAUZ2bPPn1yDw (3 entries, closed 6/15/2026) — all read in full.
- COR-to-CO PY4 acceptance memo 6/10/2026: 1WYk7InBAIUy5ja7kPONQQo_qJhz5-muOH6vLei6chEQ — read in full.
- Mod folder (J. Parker) 1yGeLwXXgUxb_iaQihhTrxr4xQ_rI5prK — full listing (PS0001–PO0018 SF30 copies).
- R5 ALL ESPC Verified Savings & Payments Tracker 1L84H7mzSRkaf1qWrhiG6Yw444UcKF4YCwI5bCtSIlW0 — Detroit rows (cadence/payment verification dates only; no independent savings figures).

**Gmail threads read:** 19d01a47dd04e986 (PY4 M&V schedule confirmed 3/23–3/25, Kinne/Parker/Russell, 3/18/2026); 19dba32dad23f31f (PY4 report circulation + Matt's 5/20/2026 consolidated COR review stating witnessing 3/23–3/24, "no deficiencies"); 19dba1d3af238242 (Kinne submission 4/22/2026 + Matt's 4/27 ack of $38,838 excess); 19dcf9971c28a73c (PY4 CPARS review, Blake 4/28, Matt concur 5/18); 19d1980bdc6ead4e (calendar witnessing notice 3/23–3/24). Targeted search for any Detroit M&V reschedule traffic 3/20–4/15/2026: none found.

**Records searched for and NOT found (explicit gaps — do not infer):**
- **PY1 accepted Rev.03 PDF** (10/24/2023, incorporated by PS0012) — only Rev.01 and the initial Yr01a in Drive; Rev.03 content reconstructed from YR1 comment log dispositions.
- **PY2 accepted Ver3-Final PDF** (10/25/2024, incorporated by PS0015) — not in Drive; accepted total ($1,287,883) taken from PY3/PY4 Table 3; **per-ECM accepted PY2 breakdown unavailable**.
- Standalone PY3 report file — exists only inside the PS0017 SF30 package.
- Signed PY4 witnessing forms / combustion test strips for the 3/23–3/24/2026 walks (needed to resolve the date conflict) — referenced in the dossier and report appendix but images not extractable from the PDF text layer.
- Any per-ECM decomposition of the *guarantee* (guarantee exists only at project level in Schedule 1) — ECM-level shortfall-vs-guarantee analysis is therefore not contractually possible.
- Any reconciliation, in any year, of stipulated savings vs actual utility bills (gas, electric, water) — no such analysis has ever been performed on this contract.
- R5 tracker year-by-year verified-savings figures for Detroit (tracker holds cadence dates only). The alternate tracker ID from the tasking template (1hldqNYgB…) was not queried separately; the dossier-cited tracker was used.

---
*Method note: no contractor claim was accepted at face value; every headline number above was re-derived from table-level source data (guarantee = 0.97 × estimate; verified = proposed + PIR deltas; rate tables recomputed against contract escalators). Where the report says X but the arithmetic implies Y, both are stated.*
