# GSA Zone C Portfolio Workload Tracker

**Owner:** Matthew Schreck
**Title:** Energy Program Specialist / M&V Specialist
**Role:** Zone C MVP Lead
**Portfolio:** 15 ESPC/UESC Contracts | $300M+

---

## Overview

Comprehensive tracking system for GSA Zone C ESPC/UESC contract portfolio. Documents workload from IG Audit through present, including crisis staffing documentation and evidence for leadership briefings.

## Quick Start

```bash
# View portfolio dashboard
python scripts/dashboard.py

# Generate all reports
python scripts/report_generator.py

# View data entry template
python scripts/data_entry.py
```

## System Structure

```
├── data/
│   ├── contracts_database.json    # Master contract database (15 contracts)
│   ├── timeline_events.json       # IG Audit → MVP Charter → Present
│   ├── workload_metrics.json      # M&V reviews, payments, issues
│   └── crisis_documentation.json  # 80% staffing loss documentation
│
├── scripts/
│   ├── portfolio_manager.py       # Core data management
│   ├── report_generator.py        # Exportable reports for leadership
│   ├── dashboard.py               # Real-time portfolio status
│   └── data_entry.py              # Quick data population utilities
│
├── reports/                       # Generated reports (gitignored)
│
├── voice_profiles/
│   └── voice_calibration.json     # Communication tone/style profiles
│
└── templates/                     # Report templates
```

## Data Entry

### 1. Set Key Dates

```python
from scripts.data_entry import *

pm = PortfolioManager()

set_key_dates(pm,
    ig_audit="YYYY-MM-DD",
    ig_findings="YYYY-MM-DD",
    mvp_charter="YYYY-MM-DD",
    lead_start="YYYY-MM-DD",
    crisis_start="YYYY-MM-DD"
)
```

### 2. Configure Staffing Crisis

```python
set_staffing_crisis(pm,
    original_team=5,
    current_team=1,
    crisis_date="YYYY-MM-DD",
    positions_lost=["Position 1", "Position 2"],
    additional_responsibilities=["Responsibility 1", "Responsibility 2"]
)
```

### 3. Add Contracts

```python
quick_add_contract(pm,
    name="Contract Name",
    contract_number="GS-XXX-XXXX",
    contract_type="ESPC",  # or "UESC"
    partner="ESCO/Utility Name",
    value=25000000,
    status="Active - Performance Period",
    award_date="YYYY-MM-DD",
    perf_start="YYYY-MM-DD",
    perf_end="YYYY-MM-DD",
    perf_year=6,
    total_years=20,
    facilities=["Facility 1", "Facility 2"],
    notes="Notes here"
)
```

### 4. Update Workload Totals

```python
update_workload_totals(pm,
    m_and_v_reviews=45,
    payments_processed=120,
    payment_value=15000000,
    issues_resolved=23,
    site_visits=18,
    contractor_meetings=36
)

pm.save_all()
```

## Available Reports

| Report | Description | Audience |
|--------|-------------|----------|
| Executive Summary | High-level portfolio overview | Senior Leadership |
| Contract Detail | Full listing of all 15 contracts | Program Management |
| Workload Evidence | Scope documentation with metrics | HR/Resource Allocation |
| Crisis Documentation | Staffing reduction impact | Leadership Briefings |
| Timeline Report | IG Audit → Present history | Audit Response |

## Contract Statuses

- Pre-Award
- Active - Construction
- Active - Performance Period
- Post-Acceptance
- Closeout
- Terminated
- On Hold

## Voice Calibration

The system includes voice/tone profiles for drafting communications. Provide sample emails to calibrate:

- Leadership (formal)
- ESCO Contractors (professional-direct)
- Utility Partners (collaborative)
- Internal Team (collegial)
- Facility Managers (approachable)
- Auditors/Compliance (formal-precise)

---

## Data Status

**CURRENT STATUS: PLACEHOLDER DATA**

Populate with actual contract information using the data entry utilities.

---

*System built for GSA Zone C MVP Lead portfolio management and leadership briefings.*
