# M&V Doctrine & Standard Operating Procedures

## Core Principles

### 1. Guarantee Protection
GSA's primary objective is ensuring the government receives guaranteed energy savings or appropriate shortfall payments. All M&V activities support this goal.

### 2. Deficiency Classification
Deficiencies must be correctly classified to ensure proper payment calculation:

| Type | Definition | Payment Impact |
|------|------------|----------------|
| **ESCO-Responsible** | Design, installation, or performance guarantee issues | Reduces guarantee payment |
| **GSA-Responsible** | Operational deviations from IGA assumptions | No payment impact (but lost savings) |
| **As-Built** | Permanent construction differences from IGA | Permanent guarantee reduction |

### 3. Documentation Standards
All decisions must be documented with:
- Technical justification
- Dollar impact calculation
- Supporting data/evidence
- Date and reviewer signature

## M&V Report Review Standards

### Acceptance Criteria
Reports must meet these minimum requirements:

- [ ] Submitted within 90 days of performance year end
- [ ] All buildings and ECMs addressed
- [ ] Baseline calculations match IGA
- [ ] Adjustments documented and justified
- [ ] Savings calculations verifiable
- [ ] Deficiencies identified and classified

### Statistical Thresholds (ASHRAE Guideline 14)

| Metric | Monthly | Acceptable |
|--------|---------|------------|
| CV(RMSE) | ≤15% | ≤25% |
| NMBE | ±5% | ±10% |
| R² | >0.75 | >0.70 |

### Red Flags Requiring Investigation
- Savings at exactly 100% of guarantee
- Missing metering data (>10% gaps)
- Unexplained non-routine adjustments
- Baseline changes without documentation
- Same deficiencies recurring 3+ years

## Payment Processing

### Net Payable Calculation
```
Net Payable = Verified Savings - Shortfall Deduction
```

Where:
- Verified Savings = Calculated savings after all adjustments
- Shortfall = Guarantee - Verified Savings (if positive)

### EASI Documentation Requirements
1. Signed acceptance letter
2. M&V report (accepted)
3. Deficiency summary
4. Invoice from ESCO
5. Receiving report

## Escalation Protocol

### When to Escalate to CO
1. Contractor disputes deficiency classification
2. Report submission >30 days late
3. Shortfall payment not received within 60 days
4. Pattern of recurring issues (3+ years)
5. Contractor requests mitigation measures
6. Potential contract modification needed

### Escalation Process
1. Document issue with all supporting evidence
2. Prepare briefing memo (1 page max)
3. Schedule meeting with CO
4. Present options and recommendation
5. Document CO decision

## Timeline Standards

| Event | Standard | Maximum |
|-------|----------|---------|
| M&V Report Submission | 90 days after year end | — |
| GSA Review Completion | 30 days from receipt | 45 days |
| Deficiency Response Request | Within 5 days of review | — |
| ESCO Response | 30 days from request | — |
| Shortfall Payment | 30 days from acceptance | 60 days |

## Quality Assurance

### Review Checklist
Use standardized checklist for all reviews (see templates/mv_review_checklist.md)

### Peer Review
Complex issues or disputes should receive peer review before escalation

### Documentation Retention
- All M&V reports: Contract duration + 6 years
- Correspondence: Contract duration + 3 years
- Payment records: Per FAR requirements

## IPMVP Application

### Option Selection Guidelines

| Option | Use When | Typical ECMs |
|--------|----------|--------------|
| A | Savings predictable, parameters stable | Lighting, water fixtures |
| B | Single system, isolation possible | Chillers, VFDs, motors |
| C | Multiple ECMs, whole-building analysis | Building-wide retrofits |
| D | Complex interactions, modeling required | Rare post-construction |

### Adjustment Standards

**Routine Adjustments:**
- Weather normalization using TMY3 or actual data
- Occupancy changes (if metered)
- Production changes (industrial)

**Non-Routine Adjustments:**
- Must be individually documented
- Require technical justification
- Subject to GSA approval
- Cannot exceed 10% of savings without CO notification

## Communication Standards

### ESCO Communications
- Professional and documented
- Response within 5 business days
- Technical disputes in writing
- Copy CO on significant issues

### Acceptance Letters
Use standard template (see templates/acceptance_letter_template.md)
Include:
- Performance summary
- Deficiency summary
- Payment determination
- Outstanding issues
- Next steps and deadlines

---

*GSA Region 9 M&V Doctrine v1.0*
*Effective: February 2026*
