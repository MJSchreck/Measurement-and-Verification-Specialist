# Google Drive / GACA Compliance Build Plan

## GACA Compliance Requirements

Files must live in matthew.schreck@gsa.gov Drive (FedRAMP ATO). External contractor shares must go through GACA accounts — contractors view only, never create files inside your Drive.

## Folder Naming Convention (PBS EASi/EDMS September 2025)

- Start with narrative description — no PIID needed in filename
- No symbols: @ # $ / \ _ - all prohibited
- No "final" unless actual final submission
- Example compliant: `M&V Report PY7 Accepted March 2026.pdf`
- Example non-compliant: `HWSSC_PY7_MV_FINAL_v2.pdf`

## 14 Contract Folder Names (paste exactly into Drive)

```
01 ENABLE R8 ABM 47PJ0019F0379
02 DFC Mt Plains McKinstry 47PJ0024F0020
03 NDER2 San Diego Ameresco GS-P-08-16-JE-7074
04 UESC Sansome PGE GS-P-09-17-KS-0009
05 UESC San Diego SDG&E 47PK0222F0014
06 LA Phase I IIA ABM 47PK0324C0001
07 NDER2 LA Honeywell GSP0816JE7081
08 NDER2 SF Honeywell GSP0816JE7140
09 Harold Washington Ameresco GSP0517GB0001
10 ENABLE Detroit Honeywell 47PF0020F0671
11 NDER1 Chicago Noresco GS-P-05-12-HA-0035
12 PF EMP2 Services 47PK0220F0064
13 NDER1 Battle Creek Trane GS-P-05-09-HD-0011
14 PJKK Hawaii JCI 47PK0223F0041
```

## 8 Tabs Inside Each Contract Folder

```
00 Contract File Index
01 COR Authorization
02 Contract Documents
03 M&V Review
04 Payments
05 Correspondence LOC CPARS
06 Witnessing
07 HSPD-12
08 Government Impact Closeout
```

## Build Schedule

| Phase | Date | Action |
|-------|------|--------|
| Script build | Week Mar 30 | Claude Code script to auto-create all folders via Google Drive API |
| Initial creation | Apr 3 (AWS) | Run script + create 00 Index for contracts 08, 07, 06 |
| GACA verification | Apr 6–9 | Email itservicedesk@gsa.gov for GACA account verification (Stacy Garvey, Abayomi Dairo) |
| Migration | Apr 9–14 | Migrate + rename files for 5 critical contracts |
| Sharing | Apr 17 (AWS) | Set up GACA viewer shares — Tab 03 only — document in 00 Index GACA Sharing Log |
| Full migration | May | Full portfolio migration |

## 00 Index Content (Required per GSAM 504.802)

Each contract needs a Google Doc at 00 Contract File Index listing every required document, its status, and its location. Without this, every COR file fails a PMR inspection regardless of what else is in it.
