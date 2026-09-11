# FORENSIC M&V SHORTFALL ANALYSIS — Contract 07: Ameresco HWSSC ESPC (GSP0517GB0001)

**Analysis date:** 2026-08-24 | **Analyst scope:** PY1–PY7 guarantee-vs-verified, ECM-level shortfall attribution, PY7 13-item review autopsy, PY8 government-dependency attribution
**PIID:** GS-P-05-17-GB-0001 under DOE ESPC IDIQ DE-AM36-09GO29029 | Site: Harold Washington Social Security Center, Chicago (SSA-delegated)
**Performance period:** 11/1/2018–10/31/2027 (9 years); currently in PY8 (month 10 of 12)
**Method:** Every figure below was traced to a primary source: the annual M&V report for each year PY1–PY7 (all seven located and read), the R5 verified-savings tracker, Mod PS22, File Memo PO21, the PY7 comment log, the 25-message consolidated-review Gmail thread, and the 5/5/2026 meeting transcript. Nothing is interpolated.

---

## 1. PY-by-PY Guarantee vs. Verified Table (PY1–PY7 complete; no missing years)

| PY | Period | Proposed $ | Guaranteed $ | Verified $ | Variance $ | Variance % | Cumulative variance | Source |
|---|---|---|---|---|---|---|---|---|
| PIR (constr.) | 10/28/16–10/31/18 | $361,078 | $353,856 | $361,697 | +$7,841 | +2.2% | — | R5 tracker HWSSA payment tab (1hldqNYgB-ZHIihlneNfuFqsDeniHF88DZM40lsj_Tec) |
| PY1 | 11/18–10/19 | $361,078 | $353,856 | $377,609 | +$23,753 | +6.7% | +$23,753 | PY1 Rev3 report Table 1.6 (10JXg50QmzrWjYsOAQviEYmQOevdHgEvg); tracker |
| PY2 | 11/19–10/20 | $364,691 | $357,397 | $381,222 final (report Rev1 shows $381,438) | +$23,825 | +6.7% | +$47,578 | PY2 Rev1 report Table 1.6 (1CIKvrANFE2oeIM63SPjhuPkgMLJm2eCU); final $ per PY7 Table 10 + tracker |
| PY3 | 11/20–10/21 | $368,335 | $360,968 | $379,805 final (Jan-2022 report copy shows $379,617) | +$18,837 | +5.2% | +$66,415 | PY3 report Table 1.6 (1GJf6qcUK2mL0IC6qn1Br1U6YjD84z7wE); final $ per PY7 Table 10 + tracker |
| PY4 | 11/21–10/22 | $372,009 | $364,569 | $380,152 | +$15,583 | +4.3% | +$81,998 | PY4 report Table 6 (1DBHxQLwaxGRveS_Gp2teGGh43nJkkC0-) |
| PY5 | 11/22–10/23 | $375,714 | $368,200 | $396,914 | +$28,714 | +7.8% | +$110,712 | PY5 report Table 6 (1_QPj_LWeWH_P7kbwZaqQ1WFLo5xKy0Rw) |
| PY6 | 11/23–10/24 | $379,450 | $371,861 | $399,656 | +$27,795 | +7.5% | +$138,507 | PY6 Final report Table 6 (1yO9Opa0n1EeN5Oa2yIXIPrYxuI-cSWJc) |
| PY7 | 11/24–10/25 | $383,217 | $375,553 | $401,087 | **+$25,534** (Table 6) / report Table 1 claims +$28,134 — see red flag §6.1 | +6.8% | +$164,041 | PY7 Rev.01 Final Tables 1, 6, 10 (1O5-YYntUZf73zzfY-2JsZFNcxQ6ZY11O; also in executed PS22, 1oxA9DKdEA1-kGulodRIgYM_sopczp0d6) |
| **Total PY1–7** | | | **$2,552,406** | **$2,716,446** | **+$164,040** | +6.4% | | PY7 Table 10 (rounding: per-year sum = $164,041) |

**Headline: the guarantee was met in all seven verified years. There has never been a payment-reducing shortfall on this task order.** File Memo PO21 (1_sQrAjSQFJkqQbyCMffqB5CCZmogaPc1, signed Parker 8/26/2025) confirms the mechanism — "Performance year obligation modifications are used to deduct money from the payments based on shortfalls reported on previous M&V reports if a shortfall is encountered" — and that no deduction has ever been required. PY8/PY9 not yet verified (PY8 report due ~Feb 2027).

**How "verified" is actually computed (the finding that frames everything else).** For PY1, PY4, PY5, PY6, and PY7 the arithmetic reconciles *exactly*:

> **Verified $ = Proposed (fixed eQUEST model, escalated) + ECM-3D OA-flow credit − any Ameresco-tagged deficiency**

- PY1: 361,078 + 16,531 = 377,609 ✔ exact
- PY4: 372,009 + 14,680 − 6,537 = 380,152 ✔ exact
- PY5: 375,714 + 21,200 = 396,914 ✔ exact
- PY6: 379,450 + 20,206 = 399,656 ✔ exact
- PY7: 383,217 + 17,870 = 401,087 ✔ exact
- PY2: bridge off by +$2,505; PY3: off by −$763 (unreconciled — see §7 gaps)

The annually "measured" quantities (chiller efficiency, boiler combustion efficiency, trend verifications) contribute **zero dollars** of year-to-year variance except when a deficiency is booked. The guarantee cushion is structural: guaranteed = proposed − ~2% ($7,222 rising to $7,664/yr). So every year's surplus above that fixed ~$7.5K cushion has come from **one adjustment: the ECM-3D outside-air reduction credit.** Corroborating detail: PY7 Table 10's Year-7 row prints electric quantities (7,573,242 kWh / 22,431 kW / −16,732 MMBtu gas) *identical to the digit* to the Year-1 row — consistent with PY7 reverting to the PIR-stipulated OA value, making PY7's verification effectively PY1's verification re-escalated.

---

## 2. Shortfall Inventory (every ECM-level verified-below-expected item, PY1–PY7)

No *annual* shortfall exists, so this inventory is at ECM level — every negative savings impact booked in any year's Table 6/7 (or Table 1.6/1.7 in early-year format):

| PY | ECM | Magnitude | Cause per report | Responsibility (as booked) | Disposition |
|---|---|---|---|---|---|
| PY1 | 3A | −$3,017 / −456 MMBtu | Operating hours more than proposed (Sunday housekeeping schedule added) | Government | Quantified, excluded from verified; absorbed by government |
| PY2 | 1B | −$216 / −9 MMBtu | Actual weighted-avg CHW setpoint 2.2°F below modeled | **Ameresco** | Deducted from verified ($381,438→$381,222); guarantee still met |
| PY2 | 3A | −$2,393 / −355 MMBtu | Hours 5% over proposed (Sundays 5am–8pm; housekeeping/COVID) | Government | Excluded from verified; absorbed |
| PY3 | 1B | −$2,796 / −139 MMBtu | Chiller-1 measured kW/ton underperformed target | **Ameresco** | Deducted from verified; guarantee still met |
| PY3 | 3A | −$1,607 / −234 MMBtu | Hours 4% over proposed (Sundays) | Government | Excluded; absorbed |
| PY4 | 1B | −$6,537 / −280 MMBtu | Chiller-1 efficiency below target (2nd consecutive year) | **Ameresco** | Deducted from verified; guarantee met by $903 ex-ECM-3D (see §6.3) |
| PY4 | 1B | −$3,594 / −256 MMBtu | CHW supply temp did not follow proposed reset schedule | Government | Excluded; absorbed. First appearance of the CHW-reset leak |
| PY4 | 3A | −$7,751 / −1,110 MMBtu | Hours 17% over proposed (housekeeping, occupancy, COVID; Sunday running) | Government | Excluded; absorbed. Largest gov hit of the contract |
| PY5 | 1B | −$5,799 / −21 MMBtu | Refrigerant leaks chiller-2/-3 reduced efficiency | Government (O&M is agency-side per RRPM) | Excluded; leak repair completed by PY6 (PY6 books +$264 gov credit for the fix) |
| PY5 | 1B | −$3,637 / −256 MMBtu | CHW reset 41–46°F vs proposed 42–53°F | Government | Excluded; "corrected in Year 6" per Ameresco, then broken again by PY7 |
| PY7 | 1B | −$3,725 / −256 MMBtu | CHW reset again 41–46°F vs proposed 42–53°F | Government | Excluded; uncured as of report acceptance; PY8 watch item #4 |
| PY7 | (1A implicit) | ~$0 booked | Boiler weighted efficiency 86.24% vs 86.25% target — met by 0.01 pt, down from 87–89% in PY4–PY6, on a substituted HWRT input | Not booked as deficiency | Closed as documentation note (Comment 9); real exposure carried to PY8 |

Notes: (a) PY6 booked *no* negative impacts — its two government items were positive (+$264 refrigerant fix, +$5,312 reduced hours), both excluded from verified. (b) PY5's ECM-3A hours item flipped positive (+$2,856, hours 6.2% *under* proposed), also excluded — see symmetry finding §6.5. (c) Government CHW-reset leakage recurs in PY4, PY5, PY7 at a stable ~−256 MMBtu / −$3.6–3.7K — the identical MMBtu figure across three years suggests a modeled (not measured) impact quantity.

---

## 3. The ECM-3D Adjustment Stream — the engine of every surplus

Every year, verified exceeds proposed because of a single Ameresco-responsible "operating enhancement": OA flow at AC-1/-3/-4 measured (or stipulated) below the modeled 28,761 CFM (22 cfm/person). The credit and its measurement basis by year:

| PY | ECM-3D credit | Claimed basis | Basis type |
|---|---|---|---|
| PIR | (built into PIR model) | eQUEST OA input reset 22 → **12.68 cfm/person** from post-install trends | Model recalibration at PIR |
| PY1 | +$16,531 | Y1 trends 13.41 cfm/person ≈ PIR value → **booked at PIR value** with ±1 cfm/person adjustment band (PY1 report §4.4.3) | PIR stipulation |
| PY2 | +$14,242 | "49.0% reduction of OA flow rates" | % reduction from trends |
| PY3 | +$15,029 | 22 → 14.75 cfm/person | cfm/person from trends |
| PY4 | +$14,680 | 22.00 → 14.85 cfm/person | cfm/person from trends |
| PY5 | +$21,200 | 28,761 → **16,000** CFM (suspiciously round) | CFM from trends |
| PY6 | +$20,206 | 28,761 → 17,333 CFM; "GSA requested… required CFM" basis | CFM from trends (new basis per GSA request) |
| PY7 | +$17,870 | 28,761 → 20,024 CFM **per PIR** — trend data lost in BAS upgrade | Reverted to PIR stipulation |
| **Total PY1–7** | **+$119,758** | | |

**$119,758 of the $164,040 cumulative surplus (73%) comes from this one adjustment.** The measurement basis has changed at least four times (PIR stipulation → % reduction → cfm/person → required-CFM → back to PIR stipulation), the underlying quantity has drifted from 12.68 to ~20,024-CFM-equivalent, yet the dollar credit stayed in a narrow $14.2–21.2K band. The PY7 review (Comment 12) established the deepest defect: the OA average was computed across **all hours including unoccupied** (~40% of records at/near 0% damper), which depresses average CFM and inflates the claimed reduction; the M&V Plan §5.2.2 / IGA B.1.2 stipulate a 7AM–7PM weekday occupied schedule. Ameresco's log response concedes the point flatly: "The average OA CFM analysis is based on the data set for both occupied and unoccupied hours." One mitigant noted for fairness: PY7's PIR-based 20,024 CFM yields a *smaller* credit than PY6's measured 17,333 CFM did, so the PY7 reversion was directionally conservative vs. PY6.

---

## 4. Attribution Ledger

Classification of every shortfall or disputed savings block, with evidence and confidence:

| # | Block | $ | Classification | Evidence & confidence |
|---|---|---|---|---|
| A | Chiller-1/CHW-setpoint underperformance, PY2–PY4 | −$9,549 (216 + 2,796 + 6,537) | **CONTRACTOR PERFORMANCE DEFICIENCY** | Booked by Ameresco itself against verified savings in each report; guarantee still met, so absorbed with no payment effect. Cured (no recurrence PY5+, though PY7 chiller data was too corrupt to test — see D). **High** |
| B | Government occupancy/schedule swings, ECM-3A: PY1 −3,017; PY2 −2,393; PY3 −1,607; PY4 −7,751; PY5 +2,856; PY6 +5,312 | net −$6,600 (−$14,768 neg / +$8,168 pos) | **GOVERNMENT-RESPONSIBLE ADJUSTMENT** | Housekeeping/COVID schedule changes documented each year; quantified but excluded from verified in both directions (symmetric — see §6.5). Absorbed by government as reduced realized savings; no payment effect. **High** |
| C | CHW supply reset leak (41–46°F vs 42–53°F), PY4/PY5/PY7 + refrigerant leaks PY5 | −$16,755 (3,594 + 3,637 + 3,725 + 5,799) | **GOVERNMENT-RESPONSIBLE ADJUSTMENT** — with an attribution caveat | Booked government per RRPM (agency holds O&M). Caveat: Ameresco stated in the comment log it is "unable to confirm whether the reset schedule was changed by GSA intentionally," and ECM-3 controls were Ameresco's own install — the government tag on the reset rests on an unverified assumption about who changed the programming. Zero payment effect either way (excluded from verified), but the recurring ~$3.7K/yr leak is being absorbed by the government on Ameresco's say-so. **Medium** |
| D | PY7 chiller efficiency verification void | $0 booked | **DISPUTED / UNDETERMINED** | 8.6% of PY7 chiller data physically impossible (CHWST > CHWRT); Ameresco excluded chiller data from the efficiency calc entirely ("the data was not enough to verify the efficiency of the chillers"). Result: chiller performance simply went *unverified* in PY7 with no deficiency bookable — the PY3/PY4 chiller-1 deduction mechanism could not fire. Resolved by: clean PY8 CHWST/CHWRT trend pairs. **High confidence in the fact; unknown $ exposure** |
| E | PY7 boiler HWRT substitution (3-yr average in lieu of measured) | $0 booked; margin to target 0.01 pt | **DISPUTED / UNDETERMINED** (methodology substitution, government-caused data loss, contractor-asserted conservatism) | Trend data lost in the *government-side* JCI BAS upgrade (URGENT recovery thread 19b27b308db967b5, Dec 2025). Ameresco's conservatism claim is circular (Matt, 4/28: prior years used the same averaging convention). Resolved by: PY8 ±5°F/±10°F sensitivity analysis + Helm spot readings + restored trends; retroactive recalculation committed if non-conservative. **High confidence in the gap; $ exposure unquantified until sensitivity analysis** |
| F | ECM-3D OA credit stream, PY1–PY7 | +$119,758 claimed | **BASELINE / METHODOLOGY** (introduced by Ameresco at PIR; basis accepted by GSA, including one basis change GSA itself requested in PY6) | See §3. PY7 portion (+$17,870) provisionally accepted only, with no-precedent language and reserved retroactive recalculation (comment log, MS 4/28/2026). Occupied-hours filtering in PY8 will likely *shrink* this credit (filtering out unoccupied zeros raises average CFM). **Medium confidence that some portion of the recent-year credits is overstated; High confidence the credit survives in some amount** |
| G | PY7 Table 1 variance figure $28,134 | +$2,600 phantom | **BASELINE / METHODOLOGY (report error, uncorrected)** | Table 1 states variance $28,134; Table 6 computes B−C = $25,534; tracker and comment history use $25,534. $28,134 matches no derivable quantity from the report's own numbers. Introduced by Ameresco; survived the 13-item review and is now incorporated into the contract via PS22 and quoted in the portfolio brief. **High** |

**Bottom-line attribution split:** Contractor-owed shortfall dollars: **$0** (the $9,549 of contractor deficiencies were self-deducted and the guarantee still cleared). Government-absorbed savings leakage (never charged to Ameresco, correctly or not): **~$31,523** of quantified negative impacts PY1–PY7 (offset by +$8,168 of government-favorable exclusions). Disputed/unquantified: the PY7 verification voids (blocks D/E) and whatever fraction of the $119,758 ECM-3D stream fails occupied-hours scrutiny (block F) — bounded in any single year by ~$18–21K, and in no scenario reviewed does the guarantee retroactively fail *on paper*, because the ~$7.5K structural cushion plus even a halved ECM-3D credit still clears it.

---

## 5. PY7 13-Item Consolidated Review — autopsy: did closure mask shortfall risk?

Issued 3/12/2026 (thread 19ce39989ac85a13, 25 messages); all items "Closed" in the log (1ilmoFlNEixjGDJy7sgQ4cUqFpFQA2Dbe-aEKBnBm1nE) by 5/5/2026; PS22 executed 5/6/2026. Item-by-item risk assessment:

| # | Item (reviewer) | Closure | Masked-shortfall risk? |
|---|---|---|---|
| 1 | Mods list missing PS20/PO21 (Parker) | Added in revision | None — clerical |
| 2 | §1.5.1 one-vs-two count (Parker) | Corrected | None — clerical |
| 3 | CHW reset verification (Berezovskiy) | Closed on admission reset is NOT working; "verify in Year 8" | **Yes, partially.** Closure certified the deficiency exists, not that it's fixed. ~$3,725/yr keeps leaking (government-absorbed). Recurrence of PY5 pattern |
| 4 | Negative chiller lift, 8.6% of data (Schreck) | Closed: data excluded from efficiency calc, "no financial impact" | **Yes.** "No financial impact" is true only because exclusion left chiller efficiency *unverified* — the mechanism that caught PY3/PY4 chiller deficiencies (−$9.3K) could not operate. An underperforming chiller in PY7 would have been invisible |
| 5 | CHWST 46°F max vs 53°F plan (Schreck) | Closed: actual operation modeled, not proposed schedule | Low — modeling actual is the correct M&V call; residual question is who changed the programming (see ledger C) |
| 6 | Figure 3 labeling (Berezovskiy) | Updated | None — presentation |
| 7 | HWRT 3-yr average substitution (Parker + Schreck) | Provisionally closed per CO direction; PY8 sensitivity + retro-recalc commitment | **Yes — the largest one.** Boiler efficiency passed by 0.01 pt on a substituted input whose "conservatism" is circular. If sensitivity analysis shows the average was optimistic, PY7's 86.24% could resolve below target retroactively |
| 8 | Combustion anomalies: stack temp 244°F vs 198°F at colder OAT; analyzer change; descaling unknown (Berezovskiy) | Closed "for this year"; PY8 to include PM log | **Yes, physically.** Rising stack temp at lower OAT is a classic fouling/scaling signature; "increased heating load" explanation was accepted without data; Ameresco doesn't know when boilers were last descaled. Degrading boiler = future real shortfall risk on ECM-1A |
| 9 | Boiler efficiency trend note 86.24% vs 86.25%, down from 87–89% (Schreck) | Closed as documentation note | Risk documented, not resolved — the 0.01-pt margin is the thinnest number on the contract |
| 10 | Helm calibration docs absent (Berezovskiy) | Closed; docs promised for Y8 | Moderate — PY7 combustion numbers rest on an uncalibrated-as-documented analyzer (which also drove the item-8 breakout change) |
| 11 | No Ameresco site inspection in PY7; did not accompany Helm (Berezovskiy) | Closed/accepted (GSA witnessed Helm) | **Yes, procedurally.** The ESCO performed no annual site inspection — an M&V Plan activity — and acceptance normalized it. Mitigated by GSA witnessing of the combustion test |
| 12 | OA averaging across unoccupied hours (Schreck) | Provisionally closed; PY8 occupied-hours demo; no precedent; retro-recalc reserved | **Yes** — goes to 73% of the cumulative surplus engine (§3) |
| 13 | §1.5.3 "reset now follows proposed schedule" contradiction | Closed 5/4 as "typo" | The sentence is verbatim boilerplate from the PY6 report §1.5.3 — evidence of copy-forward drafting, not a typo in the ordinary sense. Symptomatic, no direct $ |

**Verdict:** the review was genuinely rigorous (items 4, 7, 12 are exactly the right catches), but "13 of 13 closed" overstates resolution: **five closures (3, 4, 7, 8, 12) certify open risks rather than resolve them**, and all five were converted into the PY8 carry-forward list with GSA's leverage resting entirely on (a) the no-precedent/retro-recalc reservations and (b) getting real data in PY8 — which depends on the October 2026 possession window (§6.8).

---

## 6. Red-Flag Scan (per checklist)

1. **Internal variance discrepancy propagating into the contract file — $28,134 vs $25,534.** PY7 Table 1 "Savings variance $28,134" vs Table 6 "$25,534" (= 401,087 − 375,553). None of the 13 review items caught it; PS22 incorporated the report containing it; the portfolio brief now quotes +$28,134. The correct, derivable figure is **+$25,534**. 🟠
2. **Stipulated values changing year-over-year:** the ECM-3D OA basis changed ≥4 times (§3) with no single controlling methodology document cited; PY6's change was GSA-requested, the others Ameresco-initiated. Credit magnitude notably jumped +44% (PY4→PY5: $14,680→$21,200) on the switch from cfm/person to a round "16,000 CFM." 🟠
3. **Adjustments that exactly offset a would-be shortfall:** No year shows an exact offset — but **PY4 is a near-miss: without the ECM-3D credit, verified would have cleared guarantee by $903 (0.25%)**, because the contract's only large measured deficiency (chiller-1, −$6,537) nearly consumed the structural cushion. Every other year clears by exactly the ~$7.2–7.7K proposed-minus-guarantee cushion ex-ECM-3D — i.e., the guarantee has *never* been protected by measured performance, only by the fixed model plus the one adjustment. 🟠
4. **Methodology changes without explanation:** PY7 Gas Valve 1/2 efficiency breakout (analyzer swap, Bacharach → Helm) — explained only after GSA asked; HWRT measured→averaged — explained as data loss. Both flagged, both accepted. 🟡
5. **Asymmetric NRAs / government impacts: NOT found — treatment is symmetric.** Government impacts were excluded from verified in both directions: negative (PY1–5, PY7, −$31,523 total) and positive (PY5 +$2,856; PY6 +$5,576 total). This is the strongest pro-contractor-integrity fact in the record. 🟢
6. **"Did not affect savings" claims without traceable explanation:** Comment-4 closure ("no financial impact" from corrupt chiller data) is technically true and substantively hollow — the impact is unverifiability, not zero (ledger D). 🟠
7. **Cumulative negative trend:** none in dollars (surplus every year), but a real physical trend: boiler efficiency 87–89% (PY4–6) → 86.24% (PY7, margin 0.01 pt) on a softened input; stack temps rising; descaling history unknown; site drifted to a 4-boiler plant configuration (SSA, 2/2025). The dollar ledger is flat *because* the verification is simulation-anchored. 🟡
8. **Savings increases without ECM additions:** verified > proposed by 4.3–7.8% every year with zero added scope — entirely the ECM-3D credit (§3). 🟠
9. **GRAs invoked for normal operations:** ECM-3A "hours changed" items appear in six of seven years, in both directions — housekeeping/COVID schedule flux is arguably ordinary operation, but the quantifications were data-supported and symmetric, and none touched payments. Acceptable. 🟢
10. **Wrong contractual escalators:** the guarantee ladder ($353,856 → $383,027) is identical in PY1 Table 1.8, PY7 report §1.6, TO Schedules, and the tracker — consistent. One defect: PY1 report *narrative* (§1.4.2) states "Electricity 3.00%; Natural Gas 4.24%," contradicting its own multiplier table (~1.2%/1.8%, matching PS22's stated 1.2%/1.8%/3.0%). Narrative error only; no dollar effect found. 🟡
11. **Bonus reconciliation (resolves dossier Open Issue #7):** the $17,193,924.68 figure is the cumulative obligation **through PO19/PY7** per the tracker's running-total column; $17,573,197.68 is through PO21/PY8 (PS22); $17,727,105.68 is the ultimate total after the PY9 obligation ($153,908). All three are consistent; the portfolio brief was quoting a stale row, not a discrepancy. 🟢

---

## 7. PY8 Government-Dependency Attribution (Oct 1, 2026 possession date)

**The dependency chain:** All five PY8 carry-forward watch items (Helm calibration docs; boiler PM/descaling log; OA occupied-hours filtering; CHWST reset verification; HWRT trend restoration) require either BAS trend data or site records. Trend access is blocked until **GSA takes possession back 10/1/2026** (Parker, 5/5/2026 transcript: "nothing can be done until October 1st… which is last minute"). PY8 ends 10/31/2026 — a **31-day window** to pull trends, run combustion testing (Dairo offered to attend in October; November is already PY9 and "conceptually doesn't work" per Parker), and obtain the PM log. Compounding: CFM O&M contractor award projected 9/1/2026 with GSA assuming partial O&M, SSA BAS operating issues persisting with truncated warranty into FY27 (Corbett, 2/16/2026, thread 19c5724a4e830089).

**Attribution if PY8 savings verification degrades:**
- **Data-availability failures are government-responsible, and GSA has already pre-committed to the consequence.** The trend loss originated in the government-side JCI BAS upgrade (recovery campaign Dec 2025, thread 19b27b308db967b5; SSA "bureaucratic maze" flagged 2/18/2025). On 5/5/2026, on the record, Matt and David accepted in advance that if trend data remains unavailable, Ameresco "replicating last year's method" is acceptable (transcript 00:07:15–00:08:00). **Consequence: if the October window is missed, GSA cannot hold Ameresco in deficiency for a second consecutive stipulation-based report, and the retro-recalculation reservations on Comments 7/12 become practically unenforceable for PY7–PY8** — the government will have caused the very data gap those reservations depend on. The reservations survive on paper (no-precedent language is in the log), but their teeth are gone through PY8.
- **Physical savings degradation (CHW reset, boiler condition) is government-absorbed under the established RRPM pattern** — excluded from verified savings, so it cannot produce a paper shortfall or payment deduction; it produces real utility-bill losses to the government (~$3.7K/yr on CHW reset alone, plus unquantified boiler-degradation exposure).
- **Residual contractor-responsible territory in PY8:** performing the annual site inspection (skipped in PY7), delivering Helm calibration docs (already in hand per Ameresco), the sensitivity analysis on HWRT (computable without site access), and honest occupied-hours filtering *if* trends exist. A PY8 failure on any of these is Ameresco's regardless of possession.
- **Paper-shortfall probability for PY8: low.** Because verification is simulation-anchored (§1), a data-less PY8 mechanically reproduces ~proposed + ECM-3D ≈ +$25K over guarantee. The risk is not a guarantee miss; it is a third year of unverifiable savings heading into closeout, with the PY9 report (~Feb 2028) arriving after contract expiry (10/31/2027) — GSA's last practical leverage point over M&V rigor is the PY8 review cycle.

---

## 8. Findings (dollar- and PIID-anchored)

- 🔴 **F-1 (GSP0517GB0001, guards ~$119,758 cumulative / ~$18K/yr):** The October 1–31, 2026 possession window is a single point of failure for all five PY8 carry-forward items, and GSA has already pre-accepted the fallback (replicate PY7 stipulations) on the record. If the trend pull and October combustion testing don't happen, the retro-recalculation reservations on the HWRT and OA items are dead letters for PY7–PY8. Action: calendar and confirm the trend pull + Dairo site access with Randall/SSA **before 10/1**; send Ameresco the specific trend-point list (HWRT, OA damper + occupancy, CHWST reset, chiller CHWST/CHWRT pairs) now.
- 🔴 **F-2 (ECM-1A, margin $0 on a 0.01-pt efficiency pass):** Boiler efficiency passed at 86.24% vs 86.25% target on a substituted HWRT input with a circular conservatism argument, amid physical fouling indicators (stack 244°F at 20°F OAT vs 198°F at 40°F, descaling history unknown, 4-boiler config drift). Demand the PM/descaling log and the ±5°F/±10°F sensitivity analysis as hard conditions of PY8 report acceptance; a non-conservative result triggers the committed retroactive recalculation of PY7.
- 🟠 **F-3 ($2,600 phantom variance):** PY7 Table 1 claims +$28,134; the derivable figure is +$25,534 (Table 6; tracker). The wrong number is now in the PS22-incorporated report and the portfolio brief. Ask Ameresco to trace or correct it in the PY8 report's history table; use $25,534 in all GSA reporting.
- 🟠 **F-4 (73% of cumulative surplus from one adjustment):** $119,758 of $164,040 PY1–PY7 surplus is the ECM-3D OA credit, whose basis changed ≥4 times and which was computed on all-hours averaging at least in PY7 (admitted in the log). PY8 occupied-hours demonstration (7AM–7PM weekdays, IGA B.1.2 / M&V Plan §5.2.2) is the test of whether the credit is real; expect the credit to shrink, not vanish.
- 🟠 **F-5 (attribution of the recurring CHW reset leak, ~$3.7K/yr in PY4/PY5/PY7):** booked government-responsible, but Ameresco is "unable to confirm whether the reset schedule was changed by GSA intentionally" and the controls are Ameresco's ECM-3 install. Before absorbing it again in PY8, require the documented reset schedule and BAS change log to establish who changed it — and chase the programming fix through GSA O&M/CFM contractor either way.
- 🟠 **F-6 (PY7 chiller verification void):** "no financial impact" closure means chiller efficiency went unverified in PY7 (8.6% impossible data, dataset excluded) — the mechanism that booked −$9,333 of chiller deficiencies in PY3–PY4 could not operate. Clean CHWST/CHWRT pairs are a PY8 acceptance condition.
- 🟡 **F-7:** PY2/PY3 bridge gaps (+$2,505 / −$763 between report tables and final incorporated figures) and the Table 10 Yr-1 total (8,622 vs 8,662 MMBtu in the PY1 report) — minor, but worth a one-line reconciliation request with the PY8 submission. Also: PY1 narrative escalators (3.00%/4.24%) contradict the actual multiplier table (~1.2%/1.8%) — no dollar effect, note for the record.
- 🟡 **F-8:** PY8 payment-responsibility question (SSA→GSA O&M transition 9/1/2026; SSA flagged GSA may become responsible for the PY8 payment) needs an answer before the November 2026 payment cycle.
- 🟢 **F-9:** Guarantee met all seven verified years; cumulative +$164,040; government-impact accounting symmetric in both directions; withholding mechanism documented (File Memo PO21) and never needed; obligation ladder ties exactly to TO Schedules; the $17,193,924.68 / $17,573,197.68 / $17,727,105.68 figures reconcile as through-PO19 / through-PO21 / ultimate totals (resolves dossier Open Issue #7).

---

## 9. Sources & Gaps

**Drive files read (this analysis):**
- `HWSSC M&V Year 7 Rev. 01 Report_Final.pdf` — 1O5-YYntUZf73zzfY-2JsZFNcxQ6ZY11O (Tables 1, 2, 6, 7, 10; §1.5; §1.6 escalation; ECM sections)
- `FY20 - Y1 - Ameresco MV Report Year 1 Rev3 - HWSSA.pdf` — 10JXg50QmzrWjYsOAQviEYmQOevdHgEvg (Tables 1.6–1.9; §4.4.3 ECM-3D PIR adjustment)
- `FY21 - Y2 - Ameresco MV Report Year 2 Report Rev1 - …REDUCED SIZE.pdf` — 1CIKvrANFE2oeIM63SPjhuPkgMLJm2eCU (Tables 1.6–1.8)
- `Ameresco MV Year 3 Report - HWSSA.pdf` (Jan 2022 copy) — 1GJf6qcUK2mL0IC6qn1Br1U6YjD84z7wE (Tables 1.6–1.7)
- `230209-1b MV Year 4 Report - HWSSC.pdf` — 1DBHxQLwaxGRveS_Gp2teGGh43nJkkC0- (Tables 6–7)
- `240105-1b HWSSC M&V Year 5 Report_FINAL.pdf` — 1_QPj_LWeWH_P7kbwZaqQ1WFLo5xKy0Rw (Tables 6–7)
- `241230-1b COPY HWSSC M&V Year 6 Report Final.pdf` — 1yO9Opa0n1EeN5Oa2yIXIPrYxuI-cSWJc (Tables 1, 6–7; §1.5.3 boilerplate origin)
- `HWSSC M&V Y7 Review Comments` sheet — 1ilmoFlNEixjGDJy7sgQ4cUqFpFQA2Dbe-aEKBnBm1nE (all 13 dispositions + ESCO responses, read in full)
- R5 ALL ESPC Verified Savings & Payments Tracker — 1hldqNYgB-ZHIihlneNfuFqsDeniHF88DZM40lsj_Tec (HWSSA PY table: proposed/guaranteed/shortfall-taken/verified/surplus per year incl. PIR row; obligation running totals; payment ledger Pmts 1–27)
- `May 6 2026 signed SF30 GSP0517GB0001 PS22 PY7 Rpt r1.pdf` — 1oxA9DKdEA1-kGulodRIgYM_sopczp0d6 (read during dossier build; PS22 financials)
- `000 File Memo PO21.pdf` — 1_sQrAjSQFJkqQbyCMffqB5CCZmogaPc1 (shortfall-deduction mechanism; PY6 surplus/no-deduction; PS01–PO19 mod history)
- `HWSSC Final Report Comments Mtg - 260505 Notes by Gemini` — 1VZQxAv0hcFKFdaWUKtZ_5tBtdYUEC9XX_QFJvamspb4 (full notes + transcript: possession date, fallback pre-acceptance, October testing option)

**Gmail threads read:** 19ce39989ac85a13 (consolidated 13-item review, all 25 messages incl. original comment text, Ameresco responses, Matt's 4/28 dispositions, 5/1 watch list, 5/4 closures); 19b27b308db967b5 (trend-data recovery); 19c5724a4e830089 (PY7 review request + SSA transition); 19b04e5024275c1d, 19df9d0a23b1877d, 19dfd6e65a30d61d/19e17b97a02b77a1, 19fce1c316d2304e (context, via dossier build).

**Records searched for and NOT found (never interpolated):**
- A PY2 Rev2/final report showing $381,222 with a reconciled impact bridge (Rev1 shows $381,438; the −$216 delta matches the ECM-1B deficiency, but the Rev1's own internal bridge is off by ~$2.5K; no Rev2 located in Drive).
- A PY3 final report showing $379,805 (only the Jan-2022 copy at $379,617 located; the PS14 SF30 package `FY22 - Y3 - SF30 GSP0517GB0001 PS14 PY3 Rpt` — 1imLuiA0L6eFzCkfjYYqDH9RPmKTbzMvD — exists in Drive but was not opened in this pass; the final figure is corroborated independently by PY7 Table 10 and the tracker).
- Any PY1–PY7 withholding, deduction, or shortfall-payment record (none exists — consistent with File Memo PO21).
- Derivation of the $28,134 Table 1 figure (matches nothing in the report).
- PY7 CPARS final-submission confirmation (draft cleared 12/2025; no completion record).
- M&V Plan §5.2.2 and IGA B.1.2 source documents themselves (cited via the comment log and Matt's 4/28 email; the 2016 Final Proposal Vols I/II are in Drive but the specific occupied-schedule stipulation was not independently re-verified in this pass).
