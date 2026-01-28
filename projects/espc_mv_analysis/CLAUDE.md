# ESPC M&V Analysis Project

## Purpose

Analysis workspace for Energy Savings Performance Contract (ESPC) Measurement & Verification reviews across the Zone 7 portfolio.

## Scope

- Annual M&V report reviews
- Savings shortfall analysis
- Baseline adjustment evaluations
- ECM performance tracking

## Active Contracts

| Contract | Vendor | Current PY | Status |
|----------|--------|------------|--------|
| NDER2 SF | Honeywell | Year 6 | Under review |
| NDER2 SD | Ameresco | Years 5/6/7 | Backlog |
| NDER2 LA | Honeywell | Active | Current |
| PJKK Hawaii | JCI | Year 15 | Final year |

## Directory Structure

```
/espc_mv_analysis
├── CLAUDE.md           # This file
├── /retrieved_docs     # Relevant docs pulled from corpus
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
