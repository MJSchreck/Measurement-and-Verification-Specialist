# ESPC M&V Analysis Project

## Purpose

Analysis workspace for Energy Savings Performance Contract (ESPC) Measurement & Verification reviews across the Zone 7 portfolio.

## Scope

- Annual M&V report reviews
- Savings shortfall analysis
- Baseline adjustment evaluations
- ECM performance tracking

## Active Contracts

| Contract | Contract Number | Vendor | Current PY | Status |
|----------|-----------------|--------|------------|--------|
| NDER2 SF | GS-P-08-16-JE-7140 | Honeywell | Year 6 | Under review |
| NDER2 SD | DE-AM36-09GO29029/GS-P-08-15-JE-0008 | Ameresco | Years 5/6/7 | Backlog |
| NDER2 LA | DEAM3609GO29035/GS-P-08-16-JE-7081 | Honeywell | Active | Current |
| PJKK Hawaii | DE-AM36-97-EE73568/GS-P-09-08-KS-0044 | JCI | Year 15 | Final year |

## Document Retrieval

When searching Google Drive for M&V documents:

### By Contract
- `"7140" AND "M&V"` — NDER2 SF
- `"0008" AND "M&V"` — NDER2 SD
- `"7081" AND "M&V"` — NDER2 LA
- `"0044" AND "M&V"` — PJKK Hawaii

### By Type
- `"annual M&V report" AND "202X"` — Annual reports
- `"savings shortfall" OR "guarantee"` — Shortfall analysis
- `"baseline adjustment"` — Baseline issues

## Directory Structure

```
/espc_mv_analysis
├── CLAUDE.md           # This file
├── /retrieved_docs     # M&V reports pulled from Drive
├── /analysis           # Working calculations
└── /outputs            # Analysis results, reports, memos
```

## Workflow

1. Query corpus for relevant M&V reports and contract docs
2. Place retrieved documents in `/retrieved_docs`
3. Perform analysis
4. Generate outputs (summaries, recommendations, memos) in `/outputs`

## Key Metrics to Track

- Guaranteed vs. actual savings
- Shortfall amounts and causes
- Baseline adjustment justifications
- ECM-level performance
