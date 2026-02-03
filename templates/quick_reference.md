# COR II / M&V Specialist Quick Reference Card

## Key Formulas

```
Savings = Baseline - Post-Install ± Adjustments

Performance Ratio = Verified Savings / Guaranteed Savings × 100%

Shortfall = Guaranteed Savings - Verified Savings (if positive)

Net Payable = Verified Savings - Shortfall Deduction

Simple Payback = Implementation Cost / Annual Savings
```

## IPMVP Options at a Glance

| Option | Name | When to Use | Metering |
|--------|------|-------------|----------|
| **A** | Partially Measured | Lighting, fixtures, stipulated values | Spot/sample |
| **B** | Retrofit Isolation | Single systems, equipment | Continuous |
| **C** | Whole Facility | Multiple ECMs, utility-level | Utility meters |
| **D** | Simulation | Complex interactions | Calibrated model |

## Statistical Thresholds (ASHRAE Guideline 14)

| Metric | Monthly | Daily | Hourly |
|--------|---------|-------|--------|
| CV(RMSE) | ≤15% | ≤25% | ≤30% |
| NMBE | ±5% | ±10% | ±10% |
| R² | >0.75 | >0.75 | >0.75 |

## Contract Escalation Rates (HW_7140)

| Utility | Annual Rate |
|---------|-------------|
| Electric | 2.3% |
| Natural Gas | 3.9% |
| Water | 3.5% |

## Key Deadlines

| Event | Deadline |
|-------|----------|
| M&V Report Due | 90 days after performance year end |
| GSA Review Period | 30 days from receipt |
| Deficiency Response | 30 days from request |
| Shortfall Payment | 30 days from acceptance letter |

## Deficiency Classification

| Type | Impact on Payment | Example |
|------|-------------------|---------|
| **HW-Responsible** | Reduces guarantee payment | Design flaw, installation error |
| **GSA-Responsible** | No payment impact | Operational deviation, schedule change |
| **As-Built** | Permanent reduction | Construction differs from IGA |

## Common ECM Types

| ECM Code | Description |
|----------|-------------|
| 3.x | Lighting retrofits |
| 4.x | HVAC equipment |
| 8.x | VFDs, motors, controls |
| 13.x | Water conservation |
| 17.x | Retro-commissioning |

## Red Flags in M&V Reports

- [ ] Savings consistently at exactly 100% of guarantee
- [ ] Missing or incomplete metering data (>10% gaps)
- [ ] Non-routine adjustments without documentation
- [ ] Baseline changes without justification
- [ ] Regression R² < 0.75
- [ ] Same deficiencies recurring 3+ years

## Payment Calculation Example

```
Guaranteed Savings:        $1,397,628
Verified Savings:          $1,172,688
                          -----------
Shortfall:                 ($224,940)

Breakdown:
  HW Deficiencies:         ($142,396)
  GSA Deficiencies:         ($82,544)  ← Not deducted

Payment Calculation:
  Verified Savings:        $1,172,688
  Less: Shortfall:         ($224,940)
                          -----------
  Net Payable:              $947,748
```

## Contact Quick List

| Role | For |
|------|-----|
| Contracting Officer | Disputes, modifications, escalations |
| ESCO Program Manager | Technical questions, deficiency responses |
| Regional Energy Manager | Portfolio decisions, budget |
| FEMP Support | Protocol interpretation |
| Building Manager | Operational issues, site access |

## Useful Commands (CLI Tool)

```bash
# Analyze M&V report
python cli.py data/report.json --easi

# Generate acceptance letter
python cli.py data/report.json --letter -o acceptance.md

# Batch process all reports
./scripts/analyze-all.sh

# View deficiency summary
python cli.py data/report.json --deficiencies
```

## Document Locations

| Document | Purpose |
|----------|---------|
| IGA | Baseline assumptions, ECM specifications |
| Task Order | Contract terms, guarantee schedule |
| Mods | Amendments (mitigation measures, etc.) |
| Prior M&V Reports | Trend analysis, recurring issues |

## Performance Status Categories

| Ratio | Status | Action |
|-------|--------|--------|
| ≥100% | Meeting/Exceeding | Standard acceptance |
| 95-99% | Marginal | Monitor closely |
| 85-94% | Underperforming | Require corrective plan |
| <85% | Significant Shortfall | Escalate to CO |

---

*Quick Reference v1.0 | GSA Region 9 | Updated February 2026*
