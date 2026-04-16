# Contract Portfolio Master

> **Source:** Notion Database `c4fef6054c274c6385c6563714b117ac`
> **Data Source:** `collection://84c11586-4da1-4cc5-b9d2-5d770b44f65e`
> **Snapshot Date:** April 16, 2026

---

## Schema

| Property | Type | Options / Format |
|---|---|---|
| Contract Name | Title | — |
| Contract Number | Text | — |
| PIID | Text | — |
| IDV | Text | — |
| Type | Select | ESPC, UESC, ENABLE, Services |
| Vendor | Select | Honeywell, Ameresco, ABM Industries, Johnson Controls, McKinstry, PG&E, SDG&E, Noresco, Trane, EMP2 |
| Region | Select | R5, R8, R9, R10 |
| Status | Select | Active, Watchlist, Critical, Closeout |
| Risk Level | Select | Green, Yellow, Red |
| Lifecycle Stage | Select | Administration, Development/Implementation, Closeout, Partial Termination, Full Cancellation |
| Deadline Type | Select | M&V Report Due, Payment Due, Mod Execution, Comment Response, Invoice RR, COR Action Required, Budget/PR Action |
| M&V Status | Select | Pending Report, Under Review, Comments Submitted, Accepted, Disputed |
| Contracting Officer | Text | — |
| Current PY | Text | — |
| Award Date | Date | — |
| Contract End | Date | — |
| M&V Report Due | Date | — |
| Next Deadline | Date | — |
| Next Payment Due | Date | — |
| Annual Value | Number | Dollar |
| Total Contract Value | Number | Dollar |
| Obligated | Number | Dollar |
| Performance | Number | Percent |
| PPA Days Left | Number | — |
| COR Delegation | Checkbox | — |
| Nomination Letter | Checkbox | — |
| Purchase Request | Text | — |
| Critical Issues | Text | — |
| Agent Notes | Text | — |
| Last Agent Scan | Date | — |

---

## Records

| # | Contract Name | Contract Number | PIID | IDV | Type | Vendor | Region | Status | Risk Level | Lifecycle Stage | CO | Current PY | Award Date | Contract End | TCV | Obligated | Deadline Type | M&V Status | COR Delegation | Nomination Letter |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | ENABLE R8 (ABM) | 47PJ0019F0379 | 47PJ0019F0379 | GS-07F-5542P (47QSMS24D002A) | ENABLE | ABM Industries | R8 | Active | — | Administration | Felipe Jolles | — | 2019-09-25 | 2036-11-16 | $17,906,204 | $5,611,354 | — | — | Yes | Yes |
| 02 | DFC & Mt Plains (McKinstry) | GS-P-08-13-JA-0065 | GS-P-08-13-JA-0065 (EASi# GS-P-08-16-JA-7093) (NEW EASi# 47PJ0024F0020) | DE-AM36-09GO29038 | ESPC | McKinstry | R8 | Critical | — | Administration | Felipe Jolles | — | 2013-09-27 | 2035-11-30 | $18,494,626 | $9,533,175 | — | — | Yes | Yes |
| 03 | NDER2 San Diego (Ameresco) | GS-P-08-16-JE-7074 | GS-P-08-16-JE-7074 | DE-AM36-09GO29029 | ESPC | Ameresco | R9 | Critical | — | Administration | Felipe Jolles | — | 2016-04-07 | — | $53,687,414 | $16,889,078 | Budget/PR Action | — | No | No |
| 04 | UESC Sansome (PG&E) | GS-P-09-17-KS-0009 | GS-P-09-17-KS-0009 | GS-00P-14-BSD-1137 | UESC | PG&E | R9 | Watchlist | Yellow | Administration | Felipe Jolles | — | 2017-05-19 | 2036-12-01 | $11,564,801 | — | — | — | No | No |
| 05 | UESC San Diego (SDG&E) | 47PK0222F0014 | 47PK0222F0014 | 47PA0421D0019 | UESC | SDG&E | R9 | Watchlist | — | Administration | Felipe Jolles | — | 2022-02-18 | 2035-05-01 | $8,384,152 | $2,180,377 | Payment Due | — | Yes | Yes |
| 06 | LA Phase I & IIA (ABM) | 47PK0324C0001 | 47PK0324C0001 (GS-09-P-16-KS-D-7146) | NA | ESPC | ABM Industries | R9 | Active | — | Administration | Heidi Johnson | — | 2024-06-04 | 2038-05-01 | $143,903,595 | — | Payment Due | — | No | No |
| 07 | NDER2 Los Angeles (Honeywell) | GSP0816JE7081 | GSP0816JE7081 | DE-AM36-09GO29035 | ESPC | Honeywell | R9 | Critical | — | Partial Termination | Heidi Johnson | — | 2016-05-09 | — | — | — | Payment Due | — | No | No |
| 08 | NDER2 San Francisco (Honeywell) | GSP0816JE7140 | GSP0816JE7140 | DE-AM36-09GO29035 | ESPC | Honeywell | R9 | Critical | — | Administration | Heidi Johnson | — | — | — | — | — | — | — | Yes | No |
| 09 | Harold Washington SSC (Ameresco) | GSP0517GB0001 | GSP0517GB0001 | DE-AM36-09GO29029 | ENABLE | Ameresco | R5 | Active | — | Administration | Jerrud Parker | PY7/PY8 | 2016-10-28 | 2027-10-31 | $17,727,106 | $17,193,925 | Comment Response | Under Review | No | Yes |
| 10 | ENABLE Detroit (Honeywell) | 47PF0020F0671 | 47PF0020F0671 | 47QSWA18D0057 | ESPC | Honeywell | R5 | Active | — | Administration | Jerrud Parker | — | 2020-07-15 | 2038-02-28 | $24,670,720 | $5,845,569 | — | — | No | Yes |
| 11 | NDER1 Chicago (Noresco) | GS-P-05-12-HA-0035 | GS-P-05-12-HA-0035 | DE-AM36-09GO29034 | ESPC | Noresco | R5 | Active | — | Administration | Krystal Blue | — | — | — | — | — | — | — | No | No |
| 12 | PF EMP2 Services | 47PK0220F0064 | 47PK0220F0064 | — | Services | EMP2 | R9 | Active | — | Administration | Krystal Blue | — | — | — | — | — | — | — | No | No |
| 13 | NDER1 HDI Battle Creek (Trane) | GS-P-05-09-HD-0011 | GS-P-05-09-HD-0011 | DE-AM36-09GO29034 | ESPC | Trane | R5 | Active | — | Administration | Miles Conant | — | — | — | — | — | — | — | No | No |
| 14 | PJKK Hawaii (Johnson Controls) | 47PK0223F0041 | 47PK0223F0041 | 47QSWA18D0058 | ESPC | Johnson Controls | R9 | Closeout | — | Closeout | Miles Conant | PY15 | 2023-09-06 | 2025-09-30 | $4,117 | $4,117 | Invoice RR | Under Review | Yes | Yes |

### Additional Records (from secondary data set)

| Contract Name | Contract Number | Vendor | Type | Region | Status | Lifecycle Stage | CO | M&V Status |
|---|---|---|---|---|---|---|---|---|
| NDER2 SF Service Center ESPC | GS-P-08-16-JE-7140 | Honeywell | ESPC | R9 | Active | Administration | Patrick Chapman | Under Review |
| NDER2 LA ESPC | GS-P-08-16-JE-7081 | Honeywell | ESPC | R9 | Active | Administration | Patrick Chapman | Under Review |
| ABM ESPC LA | 47PK0324C0001 | ABM Industries | ESPC | R9 | Watchlist | Development/Implementation | Joshua Chung | — |
| R8 McKinstry ESPC | 47PJ0024F0020 | McKinstry | ESPC | R8 | Active | Administration | Felipe Jolles | — |
| Detroit ENABLE ESPC | — | Honeywell | ENABLE | R5 | Active | Administration | Jerrud Parker | Pending Report |
| HWSSA ESPC | — | Ameresco | ESPC | R9 | Watchlist | Administration | Jerrud Parker | Under Review |
| PG&E UESC | GS-00P-14-BSD-1137/GS-P-09-17-KS-0009 | PG&E | UESC | R9 | Watchlist | Administration | Felipe Jolles | — |
| PJKK Hawaii ESPC | 47PK0223F0041 | Johnson Controls | ESPC | R9 | Active | Administration | Miles Conant | Under Review |
| Battle Creek ESPC | DE-AM36-09GO29044 | Trane | ESPC | R5 | Active | Administration | Miles Conant | Under Review |
