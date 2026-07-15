# FY26 ESC Scorecard — Missing M&V Reports & Witnessing Tracking

Source: `ESC_Scorecard_2.xlsx` (national scorecard, `Active Projects` / `M&V Data` / `Intake Form Responses` tabs), cross-referenced with Google Drive, as of 2026-07-15. Filtered to contracts where **Contracting Officer Representative (COR) Designation = Matthew Schreck**.

## Contracts on this scorecard not yet in `contracts/`
These 3 show Matt as COR but have no context.md yet — flagged for a future Drive-extraction pass:
- **NDER1 Goodfellows** (Trane, GS-P-06-13-GZ-0005) — marked *Inactive* in FY26, nothing due
- **SSA Hagel Bldg** (Honeywell, GS-P-09-16-KS-7100) — Pre-Acceptance, nothing due
- **R7 OK G&E UESC** (OGE Energy, 47PH1120F0038) — active. Drive folders: `R7 OK UESC - OG&E` (id `1Lq8B6GXF0F4nKveP3idw3R32VLc_S0OS`), `Oklahoma Gas & Electric UESC` (id `1IXTQeAuLVAgnfXQxE3TiTDAD_nlQw6rJ`). Areawide 47PA0417D0001. CO: Patrick Chapman. Sites: OK0046CT, OK0072CT, OK0099CT, OK0101ZZ, OK0041ZZ.

## Data corrections to the scorecard itself
- **SDG&E San Diego UESC PIID**: scorecard shows `47PK0221F0046` — this is a **superseded pre-correction number**. Confirmed via SF30 Mod PA01 (3/2/2022, signed CO Carol Dones): correct current PIID is **`47PK0222F0014`** (matches repo).
- **NM Gas UESC (47PH1120F0039) PY4 witnessing**: this is a legitimate **terminal/closeout** item, not stale data. Contract was cancelled Aug 2025 (Mod PS0018, $8.25M buyout), but PY4 (11/1/24–10/31/25) was already in progress and had to be closed out. Magan Lersch (7PMD) conducted the site witnessing 8/25–26/25 and filed `App-A-2-Government-Witnessed-Inspection-Summary` (id `1cWfUM7IAtK3n0R5WBOgNWsmQ6WWuUBaL`) — signature field appears blank in the extracted text. **Action: confirm with Magan Lersch whether a signed/dated copy exists.**

## FY26 status by contract

### Genuine gaps (need real follow-up, not just filing)
| Contract | Item | Due | Action |
|---|---|---|---|
| PG&E SF (03_PGE_Sansome) | PY6 report + witnessing — both confirmed absent from Drive | 2/28/26 (late) | Escalate to ABM (Randa Meehan) |
| R7 OK G&E UESC | PY4 witnessing — no witnessing folder exists for this contract at all | 5/1/26 (late) | Schedule/conduct GSA-side site visit |
| McKinstry DFC | PY11 witnessing — real gap back to PY4 (last real form: 2018) | 2/28/26 (late) | Schedule site visit; part of a larger PY5–PY11 witnessing backlog |
| NDER2 San Diego (Ameresco) | PY8 witnessing — photos exist, no signed sign-off sheet found | 2/28/26 (late) | Confirm with Ameresco (Josh Fortman / Brett Perron) |
| NM Gas UESC | PY4 witnessing — signature status unconfirmed (closeout item, see above) | 1/29/26 (late) | Confirm with Magan Lersch |

### Scorecard is stale — docs exist, just need processing/portal submission
| Contract | Item | Status | Portal (Intake Form) submission history |
|---|---|---|---|
| McKinstry DFC | PY11 report | Exists (received 11/10/25, Drive file id `1vQ5M9b3MK4lVNHmUFUTcDV4LppAPlMpd`), but scanned/image PDF — figures not yet extracted | Only PY6 submitted (6/2/26). **PY7, 8, 9, 10, 11 all still need portal submission** (larger backlog, beyond just FY26) |
| NDER2 San Diego | PY8 report | Confirmed submitted on time by Ameresco (transmittal 12/31/25). Period 12/1/24–11/30/25. Proposed $1,717,496 / Guaranteed $1,685,118 / Verified $2,139,395 (+$454,277 above guarantee) / Agency-impact adj. -$68,000 / Net variance $386,277 | PY5 just submitted 7/14/26. **PY7 and PY8 both still missing from portal** |
| ABM LA (Phase I/IIA/IIB, `GS-09P-14-KS-C-0003` = same contract as `47PK0324C0001`) | PY11 report | Delivered by ABM (filed by Randa Meehan, April 2026) but receipt page never signed/accepted. Figures: Proposed $4,159,036 / Guaranteed $3,837,151 / Verified $5,502,641 / Excess $1,665,490 | Last submitted PY9 (Jan 2025). **PY11 needs formal acceptance before/when submitting** |
| ABM LA | PY11 witnessing | Signed forms confirmed for Roybal + Anderson (Jan 2026); Reagan/NLA/SSA not yet checked | — |
| NDER2 LA (Honeywell) | PY8 report | Already received (confirmed 6/1/26) and in GSA review | Already submitted via portal 6/2/26 — **no action** |
| NDER2 LA | PY8 witnessing | Exists, embedded in the Appendix PDF, mislabeled "Year 7" by Honeywell | Extract Section 2, file to dedicated Witnessing folder; send Honeywell a correction request before final acceptance |
| ABM ENABLE R8 | PY4 | — | Just submitted via portal 7/14/26 — **done** |

### Not yet due (FY26)
ABM ENABLE R8 PY5 (due 9/28/26), NDER2 SF PY7 (due 11/29/26), PJKK PY15 (due 10/29/26), SDG&E SD UESC PY2 (due 8/29/26).

## Ready-to-submit packet (Intake Form values)

**NDER2 San Diego — PY8** (`R9 - DE-AM36-09GO29029 / GS-P-08-16-JE-7074 (NDER2 San Diego)`)
- Performance Year: 8
- Period: 12/1/2024 – 11/30/2025
- Guaranteed Cost Savings: $1,685,118
- Verified Cost Savings: $2,139,395
- Source: `GSA Year 8 R00.pdf` (Drive id `1dcdRVrMbkugQW5mhHi55YTP6X4iA-4nZ`), transmittal 12/31/2025

**ABM LA — PY11** (`R9 - GS-09P-14-KS-C-0003 (Los Angeles Phase I, IIA, and IIB - ABM)`)
- Performance Year: 11
- Guaranteed Cost Savings: $3,837,151
- Verified Cost Savings: $5,502,641
- Source: `_GSA LA Consolidated MV Report_Year 05.pdf` (Drive id `1qhfxGfRqIydgv3Vn6p0VEQeZcftegCW9`)
- ⚠️ Caveat: the report's own receipt page is unsigned ("acknowledges receipt, not acceptance") — confirm you want to submit before formal GSA acceptance, or complete acceptance first

**McKinstry DFC — PY11**
- Figures not yet available: source PDF is 73.9MB and scanned/image-based, and exceeds the 10MB limit on the Drive download tool available in this session. Options: (a) open `GSA R8 ESPC MV Report Year 11 (RESCUED from ESCO personal drive) - 2026 07 13.pdf` (Drive id `1vQ5M9b3MK4lVNHmUFUTcDV4LppAPlMpd`) yourself and read off the guaranteed/verified savings table, or (b) tell me the numbers and I'll log them here and prep the submission text.

## Next: prior-year backlog (FY25 and earlier)
Per-contract "Missing M&V Report Years" / "Missing Witnessing Form Years" columns in the scorecard show a deeper backlog beyond FY26 — to be worked year-by-year after FY26 is current. Known so far:
- McKinstry: missing M&V 7–11, missing witnessing 1–3, 5, 6, 8–11
- NDER2 San Diego: missing M&V 7–8, missing witnessing 1, 5, 7, 8
- PJKK: missing witnessing 1–9 (M&V reports themselves current)
- ABM LA: missing witnessing 1, 2, 4, 5, 6, 10
