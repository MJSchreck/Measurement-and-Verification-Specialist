#!/usr/bin/env python3
"""
GSA Zone C Portfolio Workload Tracker
Dashboard - Real-time portfolio status view

Author: Matthew Schreck
Role: Energy Program Specialist / M&V Specialist, Zone C MVP Lead
"""

import json
from datetime import datetime
from pathlib import Path
from portfolio_manager import PortfolioManager


def display_dashboard():
    """Display the main portfolio dashboard."""

    pm = PortfolioManager()
    summary = pm.get_portfolio_summary()
    contracts = pm.get_all_contracts()
    metrics = pm.metrics_data
    crisis = pm.crisis_data
    timeline = pm.timeline_data

    # Clear screen effect with spacing
    print("\n" * 2)

    # Header
    print("╔" + "═" * 78 + "╗")
    print("║" + " GSA ZONE C PORTFOLIO WORKLOAD TRACKER ".center(78) + "║")
    print("║" + " Matthew Schreck - Energy Program Specialist / M&V Specialist ".center(78) + "║")
    print("╠" + "═" * 78 + "╣")
    print("║" + f" Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ".ljust(78) + "║")
    print("╚" + "═" * 78 + "╝")

    # Portfolio Overview
    print("\n┌─ PORTFOLIO OVERVIEW " + "─" * 57 + "┐")
    print(f"│  Total Contracts:        {summary['total_contracts']:>10}                                      │")
    print(f"│  ESPC Contracts:         {summary['espc_count']:>10}                                      │")
    print(f"│  UESC Contracts:         {summary['uesc_count']:>10}                                      │")
    print(f"│  Total Value:            ${summary['total_value']:>14,.0f}                              │")
    print(f"│  Active Contracts:       {summary['active_contracts']:>10}                                      │")
    print("└" + "─" * 78 + "┘")

    # Staffing Status
    reduction = crisis.get('staffing_impact', {}).get('reduction_percentage', 0)
    original = crisis.get('staffing_impact', {}).get('original_team_size', 'N/A')
    current = crisis.get('staffing_impact', {}).get('current_team_size', 'N/A')
    status_indicator = "🔴" if reduction >= 50 else "🟡" if reduction >= 25 else "🟢"

    print(f"\n┌─ STAFFING STATUS {status_indicator} " + "─" * 57 + "┐")
    print(f"│  Original Team:          {str(original):>10}                                      │")
    print(f"│  Current Team:           {str(current):>10}                                      │")
    print(f"│  Reduction:              {reduction:>9.1f}%                                      │")
    print(f"│  Status:                 {'CRITICAL - UNDERSTAFFED':>25}                        │" if reduction >= 50 else f"│  Status:                 {'Monitoring':>25}                        │")
    print("└" + "─" * 78 + "┘")

    # Workload Metrics
    m_and_v = metrics.get('m_and_v_metrics', {})
    payments = metrics.get('payment_metrics', {})
    issues = metrics.get('issue_resolution_metrics', {})

    print("\n┌─ WORKLOAD METRICS " + "─" * 58 + "┐")
    print(f"│  M&V Reviews Completed:  {m_and_v.get('total_reviews_completed', 0):>10}                                      │")
    print(f"│  Reviews Pending:        {m_and_v.get('reviews_pending', 0):>10}                                      │")
    print(f"│  Payments Processed:     {payments.get('total_payments_processed', 0):>10}                                      │")
    print(f"│  Payment Value:          ${payments.get('total_payment_value', 0):>14,.0f}                              │")
    print(f"│  Issues Resolved:        {issues.get('issues_resolved', 0):>10}                                      │")
    print(f"│  Issues Open:            {issues.get('issues_open', 0):>10}                                      │")
    print("└" + "─" * 78 + "┘")

    # Key Milestones
    milestones = timeline.get('key_milestones', {})
    print("\n┌─ KEY MILESTONES " + "─" * 60 + "┐")
    print(f"│  IG Audit:               {milestones.get('ig_audit_date', 'Not Set'):>20}                          │")
    print(f"│  MVP Charter:            {milestones.get('mvp_charter_established', 'Not Set'):>20}                          │")
    print(f"│  Zone C Lead Start:      {milestones.get('zone_c_lead_start_date', 'Not Set'):>20}                          │")
    print(f"│  Staffing Crisis Start:  {milestones.get('staffing_crisis_start', 'Not Set'):>20}                          │")
    print("└" + "─" * 78 + "┘")

    # Contracts by Status
    print("\n┌─ CONTRACTS BY STATUS " + "─" * 55 + "┐")
    status_counts = summary.get('contracts_by_status', {})
    if status_counts:
        for status, count in status_counts.items():
            bar = "█" * min(count * 3, 30)
            print(f"│  {status[:30]:30} {count:>3}  {bar:<30}   │")
    else:
        print("│  No contracts loaded                                                         │")
    print("└" + "─" * 78 + "┘")

    # Contract List (abbreviated)
    print("\n┌─ CONTRACT LIST " + "─" * 61 + "┐")
    print("│  ID          │ Type  │ Status                    │ Value              │")
    print("├" + "─" * 14 + "┼" + "─" * 7 + "┼" + "─" * 27 + "┼" + "─" * 20 + "┤")

    for contract in contracts[:10]:  # Show first 10
        cid = contract.get('id', 'N/A')[:12]
        ctype = contract.get('type', 'N/A')[:5]
        cstatus = contract.get('status', 'N/A')[:25]
        cvalue = contract.get('contract_value', 0)
        print(f"│  {cid:<12} │ {ctype:<5} │ {cstatus:<25} │ ${cvalue:>15,.0f}  │")

    if len(contracts) > 10:
        print(f"│  ... and {len(contracts) - 10} more contracts                                              │")

    if not contracts:
        print("│  No contracts loaded - use data_entry.py to add contracts                    │")

    print("└" + "─" * 78 + "┘")

    # Quick Actions
    print("\n┌─ QUICK ACTIONS " + "─" * 61 + "┐")
    print("│  python scripts/data_entry.py        - Show data entry template                │")
    print("│  python scripts/report_generator.py  - Generate all reports                    │")
    print("│  python scripts/dashboard.py         - Refresh this dashboard                  │")
    print("└" + "─" * 78 + "┘")

    # Data Status Warning
    metadata = pm.contracts_data.get('metadata', {})
    if 'PLACEHOLDER' in str(metadata.get('data_status', '')):
        print("\n⚠️  DATA STATUS: PLACEHOLDER DATA - Populate with actual contract information")

    print()


def display_contract_detail(contract_id: str):
    """Display detailed view of a single contract."""

    pm = PortfolioManager()
    contract = pm.get_contract(contract_id)

    if not contract:
        print(f"Contract {contract_id} not found.")
        return

    print("\n" + "=" * 80)
    print(f" CONTRACT DETAIL: {contract.get('name', 'N/A')}")
    print("=" * 80)

    fields = [
        ('Contract ID', 'id'),
        ('Contract Number', 'contract_number'),
        ('Type', 'type'),
        ('ESCO/Utility Partner', 'esco_utility_partner'),
        ('Contract Value', 'contract_value'),
        ('Guaranteed Savings', 'guaranteed_savings'),
        ('Award Date', 'award_date'),
        ('Performance Start', 'performance_period_start'),
        ('Performance End', 'performance_period_end'),
        ('Current Year', 'performance_year'),
        ('Total Years', 'total_performance_years'),
        ('Status', 'status'),
        ('M&V Schedule', 'm_and_v_schedule'),
        ('Last M&V Review', 'last_m_and_v_review'),
        ('Next M&V Due', 'next_m_and_v_due'),
        ('Payment Status', 'payment_status'),
        ('Open Issues', 'issues_open'),
        ('Resolved Issues', 'issues_resolved'),
    ]

    for label, field in fields:
        value = contract.get(field, 'N/A')
        if field in ['contract_value', 'guaranteed_savings'] and isinstance(value, (int, float)):
            value = f"${value:,.2f}"
        print(f"  {label:25} {value}")

    print(f"\n  {'Facilities':25}")
    for facility in contract.get('facilities', []):
        print(f"    - {facility}")

    print(f"\n  {'Critical Flags':25}")
    flags = contract.get('critical_flags', [])
    if flags:
        for flag in flags:
            print(f"    ⚠️  {flag}")
    else:
        print("    None")

    print(f"\n  {'Notes':25}")
    print(f"    {contract.get('notes', 'None')}")

    print("\n" + "=" * 80)


def main():
    """Display the dashboard."""
    display_dashboard()


if __name__ == "__main__":
    main()
