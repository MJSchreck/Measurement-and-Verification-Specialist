#!/usr/bin/env python3
"""
GSA Zone C Portfolio Workload Tracker
Data Entry Helper - Quick data population utilities

Author: Matthew Schreck
Role: Energy Program Specialist / M&V Specialist, Zone C MVP Lead
"""

import json
from datetime import datetime
from pathlib import Path
from portfolio_manager import PortfolioManager, DATA_DIR


def quick_add_contract(pm: PortfolioManager,
                       name: str,
                       contract_number: str,
                       contract_type: str,
                       partner: str,
                       value: float,
                       status: str = "Active - Performance Period",
                       award_date: str = "",
                       perf_start: str = "",
                       perf_end: str = "",
                       perf_year: int = 0,
                       total_years: int = 0,
                       facilities: list = None,
                       notes: str = "") -> str:
    """Quickly add a contract with common defaults."""

    contract = {
        "contract_number": contract_number,
        "name": name,
        "type": contract_type,
        "esco_utility_partner": partner,
        "contract_value": value,
        "guaranteed_savings": 0,
        "award_date": award_date,
        "performance_period_start": perf_start,
        "performance_period_end": perf_end,
        "performance_year": perf_year,
        "total_performance_years": total_years,
        "status": status,
        "facilities": facilities or [],
        "region": "Zone C",
        "critical_flags": [],
        "notes": notes,
        "m_and_v_schedule": "Annual",
        "last_m_and_v_review": "",
        "next_m_and_v_due": "",
        "payment_status": "Current",
        "issues_open": 0,
        "issues_resolved": 0
    }

    return pm.add_contract(contract)


def batch_add_contracts(pm: PortfolioManager, contracts_data: list) -> list:
    """Add multiple contracts from a list of dictionaries."""
    contract_ids = []
    for contract in contracts_data:
        contract_id = quick_add_contract(pm, **contract)
        contract_ids.append(contract_id)
        print(f"Added: {contract_id} - {contract.get('name', 'Unknown')}")
    return contract_ids


def set_key_dates(pm: PortfolioManager,
                  ig_audit: str = "",
                  ig_findings: str = "",
                  mvp_charter: str = "",
                  lead_start: str = "",
                  crisis_start: str = "") -> None:
    """Set all key milestone dates at once."""

    if ig_audit:
        pm.set_milestone('ig_audit_date', ig_audit)
    if ig_findings:
        pm.set_milestone('ig_audit_findings_released', ig_findings)
    if mvp_charter:
        pm.set_milestone('mvp_charter_established', mvp_charter)
    if lead_start:
        pm.set_milestone('zone_c_lead_start_date', lead_start)
    if crisis_start:
        pm.set_milestone('staffing_crisis_start', crisis_start)

    pm.set_milestone('current_date', datetime.now().strftime('%Y-%m-%d'))
    print("Key dates updated.")


def set_staffing_crisis(pm: PortfolioManager,
                        original_team: int,
                        current_team: int,
                        crisis_date: str,
                        positions_lost: list = None,
                        additional_responsibilities: list = None) -> None:
    """Configure staffing crisis documentation."""

    pm.update_crisis_staffing(original_team, current_team)
    pm.crisis_data['crisis_overview']['crisis_start_date'] = crisis_date
    pm.crisis_data['crisis_overview']['status'] = 'Ongoing'

    if positions_lost:
        pm.crisis_data['staffing_impact']['positions_lost'] = positions_lost

    if additional_responsibilities:
        pm.crisis_data['workload_redistribution']['additional_responsibilities'] = additional_responsibilities

    print(f"Crisis data configured: {original_team} → {current_team} ({pm.crisis_data['staffing_impact']['reduction_percentage']}% reduction)")


def update_workload_totals(pm: PortfolioManager,
                           m_and_v_reviews: int = 0,
                           payments_processed: int = 0,
                           payment_value: float = 0,
                           issues_resolved: int = 0,
                           site_visits: int = 0,
                           contractor_meetings: int = 0) -> None:
    """Update cumulative workload metrics."""

    pm.metrics_data['m_and_v_metrics']['total_reviews_completed'] = m_and_v_reviews
    pm.metrics_data['payment_metrics']['total_payments_processed'] = payments_processed
    pm.metrics_data['payment_metrics']['total_payment_value'] = payment_value
    pm.metrics_data['issue_resolution_metrics']['issues_resolved'] = issues_resolved
    pm.metrics_data['site_visit_metrics']['total_site_visits'] = site_visits
    pm.metrics_data['contractor_engagement']['contractor_meetings'] = contractor_meetings

    print("Workload metrics updated.")


def print_data_entry_template():
    """Print a template for data entry."""

    template = """
================================================================================
                    DATA ENTRY TEMPLATE
================================================================================

Copy and modify this Python code to add your contracts:

--------------------------------------------------------------------------------
from data_entry import *

pm = PortfolioManager()

# 1. SET KEY DATES
set_key_dates(pm,
    ig_audit="2023-03-15",           # When IG Audit occurred
    ig_findings="2023-06-01",         # When findings released
    mvp_charter="2023-09-01",         # When MVP Charter established
    lead_start="2023-10-01",          # Your start date as Zone C Lead
    crisis_start="2024-01-15"         # When staffing crisis began
)

# 2. SET STAFFING CRISIS
set_staffing_crisis(pm,
    original_team=5,
    current_team=1,
    crisis_date="2024-01-15",
    positions_lost=[
        "Senior M&V Specialist",
        "Energy Program Analyst",
        "Contract Specialist",
        "Program Support"
    ],
    additional_responsibilities=[
        "Assumed all M&V reviews for Zone C",
        "Took over payment processing",
        "Managing contractor relationships",
        "Site visit coordination"
    ]
)

# 3. ADD CONTRACTS (repeat for each of 15 contracts)
quick_add_contract(pm,
    name="Federal Building ESPC",
    contract_number="GS-XXX-XXXX",
    contract_type="ESPC",           # or "UESC"
    partner="Ameresco",             # ESCO or Utility name
    value=25000000,                 # Contract value in dollars
    status="Active - Performance Period",
    award_date="2018-06-15",
    perf_start="2019-01-01",
    perf_end="2039-12-31",
    perf_year=6,
    total_years=20,
    facilities=["Main Federal Building", "Annex A"],
    notes="Year 6 of 20. Annual M&V review due Q2."
)

# 4. UPDATE WORKLOAD TOTALS
update_workload_totals(pm,
    m_and_v_reviews=45,
    payments_processed=120,
    payment_value=15000000,
    issues_resolved=23,
    site_visits=18,
    contractor_meetings=36
)

# 5. SAVE ALL DATA
pm.save_all()

print("Data entry complete!")
--------------------------------------------------------------------------------

Contract Status Options:
- "Pre-Award"
- "Active - Construction"
- "Active - Performance Period"
- "Post-Acceptance"
- "Closeout"
- "Terminated"
- "On Hold"

Contract Types:
- "ESPC"
- "UESC"
- "ENABLE"

================================================================================
"""
    print(template)


def main():
    """Show data entry template and instructions."""
    print_data_entry_template()


if __name__ == "__main__":
    main()
