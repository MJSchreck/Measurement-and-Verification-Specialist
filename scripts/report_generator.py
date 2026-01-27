#!/usr/bin/env python3
"""
GSA Zone C Portfolio Workload Tracker
Report Generator - Creates Exportable Reports for Leadership

Author: Matthew Schreck
Role: Energy Program Specialist / M&V Specialist, Zone C MVP Lead
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Import portfolio manager
from portfolio_manager import PortfolioManager, BASE_DIR, DATA_DIR, REPORTS_DIR


class ReportGenerator:
    """Generates various reports for leadership briefings."""

    def __init__(self):
        self.pm = PortfolioManager()
        self.reports_dir = REPORTS_DIR
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def _get_timestamp(self) -> str:
        """Get formatted timestamp for filenames."""
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def _get_date_formatted(self) -> str:
        """Get formatted date for reports."""
        return datetime.now().strftime("%B %d, %Y")

    # =========================================================================
    # EXECUTIVE SUMMARY REPORT
    # =========================================================================

    def generate_executive_summary(self) -> str:
        """Generate executive summary for leadership."""
        summary = self.pm.get_portfolio_summary()
        crisis = self.pm.crisis_data

        report = f"""
================================================================================
                    GSA ZONE C ESPC/UESC PORTFOLIO
                       EXECUTIVE SUMMARY REPORT
================================================================================

Prepared by: Matthew Schreck
Title: Energy Program Specialist / M&V Specialist
Role: Zone C MVP Lead
Date: {self._get_date_formatted()}

--------------------------------------------------------------------------------
                         PORTFOLIO OVERVIEW
--------------------------------------------------------------------------------

Total Contracts Managed:     {summary['total_contracts']}
  - ESPC Contracts:          {summary['espc_count']}
  - UESC Contracts:          {summary['uesc_count']}

Total Portfolio Value:       ${summary['total_value']:,.2f}
  - ESPC Value:              ${summary['espc_value']:,.2f}
  - UESC Value:              ${summary['uesc_value']:,.2f}

Active Contracts:            {summary['active_contracts']}

--------------------------------------------------------------------------------
                         WORKLOAD METRICS
--------------------------------------------------------------------------------

M&V Reviews Completed:       {summary['m_and_v_reviews_completed']}
Payments Processed:          {summary['payments_processed']}
Total Payment Value:         ${summary['payment_value']:,.2f}
Issues Resolved:             {summary['issues_resolved']}

--------------------------------------------------------------------------------
                      STAFFING SITUATION
--------------------------------------------------------------------------------

Staffing Reduction:          {summary['staffing_reduction']}%
Original Team Size:          {crisis.get('staffing_impact', {}).get('original_team_size', 'N/A')}
Current Team Size:           {crisis.get('staffing_impact', {}).get('current_team_size', 'N/A')}
Status:                      {crisis.get('crisis_overview', {}).get('status', 'N/A')}

--------------------------------------------------------------------------------
                      CONTRACTS BY STATUS
--------------------------------------------------------------------------------
"""
        for status, count in summary.get('contracts_by_status', {}).items():
            report += f"{status:30} {count}\n"

        report += """
--------------------------------------------------------------------------------
                           KEY POINTS
--------------------------------------------------------------------------------

1. Portfolio of {total} contracts worth ${value:,.0f}+ maintained through
   {reduction}% staffing reduction.

2. Continued delivery of M&V reviews and payment processing despite
   significant resource constraints.

3. All critical contract obligations being met.

--------------------------------------------------------------------------------
                         END OF REPORT
--------------------------------------------------------------------------------
""".format(
            total=summary['total_contracts'],
            value=summary['total_value'],
            reduction=summary['staffing_reduction']
        )

        # Save report
        filename = f"executive_summary_{self._get_timestamp()}.txt"
        filepath = self.reports_dir / filename
        with open(filepath, 'w') as f:
            f.write(report)

        print(f"Executive Summary saved to: {filepath}")
        return report

    # =========================================================================
    # CONTRACT DETAIL REPORT
    # =========================================================================

    def generate_contract_report(self) -> str:
        """Generate detailed contract listing report."""
        contracts = self.pm.get_all_contracts()

        report = f"""
================================================================================
                    GSA ZONE C CONTRACT PORTFOLIO
                       DETAILED CONTRACT LISTING
================================================================================

Prepared by: Matthew Schreck
Date: {self._get_date_formatted()}
Total Contracts: {len(contracts)}

"""
        for i, contract in enumerate(contracts, 1):
            report += f"""
--------------------------------------------------------------------------------
CONTRACT {i}: {contract.get('name', 'N/A')}
--------------------------------------------------------------------------------
Contract Number:        {contract.get('contract_number', 'N/A')}
Type:                   {contract.get('type', 'N/A')}
ESCO/Utility:           {contract.get('esco_utility_partner', 'N/A')}
Contract Value:         ${contract.get('contract_value', 0):,.2f}
Guaranteed Savings:     ${contract.get('guaranteed_savings', 0):,.2f}
Award Date:             {contract.get('award_date', 'N/A')}
Performance Period:     {contract.get('performance_period_start', 'N/A')} to {contract.get('performance_period_end', 'N/A')}
Current Year:           {contract.get('performance_year', 'N/A')} of {contract.get('total_performance_years', 'N/A')}
Status:                 {contract.get('status', 'N/A')}
M&V Schedule:           {contract.get('m_and_v_schedule', 'N/A')}
Last M&V Review:        {contract.get('last_m_and_v_review', 'N/A')}
Next M&V Due:           {contract.get('next_m_and_v_due', 'N/A')}
Payment Status:         {contract.get('payment_status', 'N/A')}
Open Issues:            {contract.get('issues_open', 0)}
Resolved Issues:        {contract.get('issues_resolved', 0)}
Facilities:             {', '.join(contract.get('facilities', [])) or 'N/A'}
Critical Flags:         {', '.join(contract.get('critical_flags', [])) or 'None'}
Notes:                  {contract.get('notes', 'N/A')}
"""

        report += """
================================================================================
                         END OF CONTRACT REPORT
================================================================================
"""

        # Save report
        filename = f"contract_detail_report_{self._get_timestamp()}.txt"
        filepath = self.reports_dir / filename
        with open(filepath, 'w') as f:
            f.write(report)

        print(f"Contract Detail Report saved to: {filepath}")
        return report

    # =========================================================================
    # WORKLOAD EVIDENCE REPORT
    # =========================================================================

    def generate_workload_evidence_report(self) -> str:
        """Generate workload evidence report for scope documentation."""
        metrics = self.pm.metrics_data
        crisis = self.pm.crisis_data
        summary = self.pm.get_portfolio_summary()

        report = f"""
================================================================================
                    GSA ZONE C MVP LEAD
                   WORKLOAD EVIDENCE REPORT
           Documentation of Scope and Accomplishments
================================================================================

Prepared by: Matthew Schreck
Title: Energy Program Specialist / M&V Specialist
Role: Zone C MVP Lead
Date: {self._get_date_formatted()}

--------------------------------------------------------------------------------
                      PURPOSE OF THIS REPORT
--------------------------------------------------------------------------------

This report documents the full scope of responsibilities, workload metrics,
and accomplishments for the Zone C MVP Lead position. It serves as evidence
for leadership briefings and resource allocation discussions.

--------------------------------------------------------------------------------
                      PORTFOLIO SCOPE
--------------------------------------------------------------------------------

Contracts Under Management:
  Total Contracts:               {summary['total_contracts']}
  ESPC Contracts:                {summary['espc_count']}
  UESC Contracts:                {summary['uesc_count']}
  Total Portfolio Value:         ${summary['total_value']:,.2f}

--------------------------------------------------------------------------------
                   M&V REVIEW WORKLOAD
--------------------------------------------------------------------------------

Total Reviews Completed:         {metrics.get('m_and_v_metrics', {}).get('total_reviews_completed', 0)}
Reviews This Fiscal Year:        {metrics.get('m_and_v_metrics', {}).get('reviews_this_fiscal_year', 0)}
Reviews Pending:                 {metrics.get('m_and_v_metrics', {}).get('reviews_pending', 0)}
Average Review Time (days):      {metrics.get('m_and_v_metrics', {}).get('average_review_time_days', 0)}

--------------------------------------------------------------------------------
                   PAYMENT PROCESSING WORKLOAD
--------------------------------------------------------------------------------

Total Payments Processed:        {metrics.get('payment_metrics', {}).get('total_payments_processed', 0)}
Total Payment Value:             ${metrics.get('payment_metrics', {}).get('total_payment_value', 0):,.2f}
Payments This Fiscal Year:       {metrics.get('payment_metrics', {}).get('payments_this_fiscal_year', 0)}
FY Payment Value:                ${metrics.get('payment_metrics', {}).get('payment_value_this_fy', 0):,.2f}
Payments On Hold:                {metrics.get('payment_metrics', {}).get('payments_on_hold', 0)}
Hold Value:                      ${metrics.get('payment_metrics', {}).get('hold_value', 0):,.2f}

--------------------------------------------------------------------------------
                   ISSUE RESOLUTION WORKLOAD
--------------------------------------------------------------------------------

Total Issues Identified:         {metrics.get('issue_resolution_metrics', {}).get('total_issues_identified', 0)}
Issues Resolved:                 {metrics.get('issue_resolution_metrics', {}).get('issues_resolved', 0)}
Issues Open:                     {metrics.get('issue_resolution_metrics', {}).get('issues_open', 0)}
Issues Escalated:                {metrics.get('issue_resolution_metrics', {}).get('issues_escalated', 0)}
Avg Resolution Time (days):      {metrics.get('issue_resolution_metrics', {}).get('average_resolution_time_days', 0)}

Issues by Category:
"""
        for category, count in metrics.get('issue_resolution_metrics', {}).get('issues_by_category', {}).items():
            report += f"  {category.replace('_', ' ').title():30} {count}\n"

        report += f"""
--------------------------------------------------------------------------------
                   SITE VISITS & CONTRACTOR ENGAGEMENT
--------------------------------------------------------------------------------

Total Site Visits:               {metrics.get('site_visit_metrics', {}).get('total_site_visits', 0)}
Site Visits This FY:             {metrics.get('site_visit_metrics', {}).get('visits_this_fiscal_year', 0)}
Travel Days:                     {metrics.get('site_visit_metrics', {}).get('travel_days', 0)}
Contractor Meetings:             {metrics.get('contractor_engagement', {}).get('contractor_meetings', 0)}
Disputes Handled:                {metrics.get('contractor_engagement', {}).get('disputes_handled', 0)}
Disputes Resolved:               {metrics.get('contractor_engagement', {}).get('disputes_resolved', 0)}

--------------------------------------------------------------------------------
                   DOCUMENTATION PRODUCED
--------------------------------------------------------------------------------

Annual Reports:                  {metrics.get('documentation_produced', {}).get('annual_reports', 0)}
M&V Reports:                     {metrics.get('documentation_produced', {}).get('m_and_v_reports', 0)}
Briefings Prepared:              {metrics.get('documentation_produced', {}).get('briefings_prepared', 0)}
Corrective Action Plans:         {metrics.get('documentation_produced', {}).get('corrective_action_plans', 0)}
Contract Modifications:          {metrics.get('documentation_produced', {}).get('contract_modifications', 0)}

--------------------------------------------------------------------------------
                   STAFFING CONTEXT
--------------------------------------------------------------------------------

This workload has been maintained despite:

Original Team Size:              {crisis.get('staffing_impact', {}).get('original_team_size', 'N/A')}
Current Team Size:               {crisis.get('staffing_impact', {}).get('current_team_size', 'N/A')}
Staffing Reduction:              {crisis.get('staffing_impact', {}).get('reduction_percentage', 'N/A')}%

Crisis Status:                   {crisis.get('crisis_overview', {}).get('status', 'N/A')}

--------------------------------------------------------------------------------
                         KEY ACCOMPLISHMENTS
--------------------------------------------------------------------------------

Despite {crisis.get('staffing_impact', {}).get('reduction_percentage', 80)}% staffing reduction:

✓ Maintained management of {summary['total_contracts']} contracts
✓ Portfolio value of ${summary['total_value']:,.0f}+ preserved
✓ Completed {metrics.get('m_and_v_metrics', {}).get('total_reviews_completed', 0)} M&V reviews
✓ Processed {metrics.get('payment_metrics', {}).get('total_payments_processed', 0)} payments totaling ${metrics.get('payment_metrics', {}).get('total_payment_value', 0):,.0f}
✓ Resolved {metrics.get('issue_resolution_metrics', {}).get('issues_resolved', 0)} contract issues
✓ Conducted {metrics.get('site_visit_metrics', {}).get('total_site_visits', 0)} site visits

================================================================================
                         END OF REPORT
================================================================================
"""

        # Save report
        filename = f"workload_evidence_report_{self._get_timestamp()}.txt"
        filepath = self.reports_dir / filename
        with open(filepath, 'w') as f:
            f.write(report)

        print(f"Workload Evidence Report saved to: {filepath}")
        return report

    # =========================================================================
    # CRISIS DOCUMENTATION REPORT
    # =========================================================================

    def generate_crisis_report(self) -> str:
        """Generate staffing crisis documentation report."""
        crisis = self.pm.crisis_data
        metrics = self.pm.metrics_data

        report = f"""
================================================================================
                    GSA ZONE C STAFFING CRISIS
                      DOCUMENTATION REPORT
================================================================================

Prepared by: Matthew Schreck
Date: {self._get_date_formatted()}
Classification: Internal Use - Leadership Briefing

--------------------------------------------------------------------------------
                      CRISIS OVERVIEW
--------------------------------------------------------------------------------

Crisis Name:             {crisis.get('crisis_overview', {}).get('crisis_name', 'N/A')}
Start Date:              {crisis.get('crisis_overview', {}).get('crisis_start_date', 'N/A')}
Type:                    {crisis.get('crisis_overview', {}).get('crisis_type', 'N/A')}
Severity:                {crisis.get('crisis_overview', {}).get('severity', 'N/A')}
Current Status:          {crisis.get('crisis_overview', {}).get('status', 'N/A')}

Summary:
{crisis.get('crisis_overview', {}).get('summary', 'N/A')}

--------------------------------------------------------------------------------
                      STAFFING IMPACT
--------------------------------------------------------------------------------

Original Team Size:      {crisis.get('staffing_impact', {}).get('original_team_size', 'N/A')}
Current Team Size:       {crisis.get('staffing_impact', {}).get('current_team_size', 'N/A')}
Reduction:               {crisis.get('staffing_impact', {}).get('reduction_percentage', 'N/A')}%

Positions Lost:
"""
        for pos in crisis.get('staffing_impact', {}).get('positions_lost', []):
            report += f"  - {pos}\n"

        report += """
Positions Retained:
"""
        for person in crisis.get('staffing_impact', {}).get('positions_retained', []):
            report += f"""
  Name:                  {person.get('name', 'N/A')}
  Title:                 {person.get('title', 'N/A')}
  Role:                  {person.get('role', 'N/A')}
  Workload Increase:     {person.get('workload_increase_percentage', 'N/A')}%
"""

        report += f"""
--------------------------------------------------------------------------------
                      WORKLOAD REDISTRIBUTION
--------------------------------------------------------------------------------

Contracts Redistributed:         {crisis.get('workload_redistribution', {}).get('contracts_redistributed', 'N/A')}
Original Contracts Managed:      {crisis.get('workload_redistribution', {}).get('original_contracts_managed', 'N/A')}
Current Contracts Managed:       {crisis.get('workload_redistribution', {}).get('current_contracts_managed', 'N/A')}

Additional Responsibilities Assumed:
"""
        for resp in crisis.get('workload_redistribution', {}).get('additional_responsibilities', []):
            report += f"  - {resp}\n"

        report += f"""
--------------------------------------------------------------------------------
                      PERFORMANCE DURING CRISIS
--------------------------------------------------------------------------------

Contracts Maintained:            {crisis.get('metrics_during_crisis', {}).get('contracts_maintained', 'N/A')}
M&V Reviews Completed:           {crisis.get('metrics_during_crisis', {}).get('m_and_v_reviews_completed', 'N/A')}
Payments Processed:              {crisis.get('metrics_during_crisis', {}).get('payments_processed', 'N/A')}
Issues Resolved:                 {crisis.get('metrics_during_crisis', {}).get('issues_resolved', 'N/A')}
On-Time Delivery Rate:           {crisis.get('metrics_during_crisis', {}).get('on_time_delivery_rate', 'N/A')}%
Critical Deadlines Met:          {crisis.get('metrics_during_crisis', {}).get('critical_deadlines_met', 'N/A')} of {crisis.get('metrics_during_crisis', {}).get('critical_deadlines_total', 'N/A')}

--------------------------------------------------------------------------------
                      DEPARTURE TIMELINE
--------------------------------------------------------------------------------
"""
        for event in crisis.get('staffing_impact', {}).get('departure_timeline', []):
            report += f"""
Date:        {event.get('date', 'N/A')}
Event:       {event.get('description', 'N/A')}
Impact:      {event.get('impact', 'N/A')}
"""

        report += """
--------------------------------------------------------------------------------
                      LEADERSHIP COMMUNICATIONS
--------------------------------------------------------------------------------
"""
        for comm in crisis.get('leadership_communications', []):
            report += f"""
Date:        {comm.get('date', 'N/A')}
Audience:    {comm.get('audience', 'N/A')}
Topic:       {comm.get('topic', 'N/A')}
Outcome:     {comm.get('outcome', 'N/A')}
Follow-up:   {'Yes' if comm.get('follow_up_required') else 'No'}
"""

        report += """
================================================================================
                         END OF CRISIS REPORT
================================================================================
"""

        # Save report
        filename = f"crisis_documentation_report_{self._get_timestamp()}.txt"
        filepath = self.reports_dir / filename
        with open(filepath, 'w') as f:
            f.write(report)

        print(f"Crisis Documentation Report saved to: {filepath}")
        return report

    # =========================================================================
    # TIMELINE REPORT
    # =========================================================================

    def generate_timeline_report(self) -> str:
        """Generate timeline from IG Audit to present."""
        timeline = self.pm.timeline_data
        milestones = timeline.get('key_milestones', {})
        phases = timeline.get('phases', [])
        events = sorted(timeline.get('events', []), key=lambda x: x.get('date', ''))

        report = f"""
================================================================================
                    GSA ZONE C MVP PROGRAM
                   TIMELINE: IG AUDIT TO PRESENT
================================================================================

Prepared by: Matthew Schreck
Date: {self._get_date_formatted()}

--------------------------------------------------------------------------------
                      KEY MILESTONES
--------------------------------------------------------------------------------

IG Audit Date:                   {milestones.get('ig_audit_date', 'N/A')}
IG Findings Released:            {milestones.get('ig_audit_findings_released', 'N/A')}
MVP Charter Established:         {milestones.get('mvp_charter_established', 'N/A')}
Zone C Lead Start Date:          {milestones.get('zone_c_lead_start_date', 'N/A')}
Staffing Crisis Start:           {milestones.get('staffing_crisis_start', 'N/A')}
Current Date:                    {milestones.get('current_date', 'N/A')}

--------------------------------------------------------------------------------
                      PROGRAM PHASES
--------------------------------------------------------------------------------
"""
        for phase in phases:
            report += f"""
{phase.get('name', 'N/A')}
  Phase ID:      {phase.get('phase_id', 'N/A')}
  Period:        {phase.get('start_date', 'N/A')} to {phase.get('end_date', 'N/A')}
  Team Size:     {phase.get('team_size', 'N/A')}
  Description:   {phase.get('description', 'N/A')}
"""

        report += """
--------------------------------------------------------------------------------
                      EVENT TIMELINE
--------------------------------------------------------------------------------
"""
        for event in events:
            report += f"""
[{event.get('date', 'N/A')}] {event.get('title', 'N/A')}
  Category:      {event.get('category', 'N/A')}
  Phase:         {event.get('phase', 'N/A')}
  Impact:        {event.get('impact', 'N/A')}
  Description:   {event.get('description', 'N/A')}
  Action Taken:  {event.get('action_taken', 'N/A')}
  Outcome:       {event.get('outcome', 'N/A')}
"""

        report += """
================================================================================
                         END OF TIMELINE REPORT
================================================================================
"""

        # Save report
        filename = f"timeline_report_{self._get_timestamp()}.txt"
        filepath = self.reports_dir / filename
        with open(filepath, 'w') as f:
            f.write(report)

        print(f"Timeline Report saved to: {filepath}")
        return report

    # =========================================================================
    # GENERATE ALL REPORTS
    # =========================================================================

    def generate_all_reports(self) -> List[str]:
        """Generate all available reports."""
        print("\n" + "=" * 60)
        print("GENERATING ALL REPORTS")
        print("=" * 60 + "\n")

        reports = []
        reports.append(self.generate_executive_summary())
        reports.append(self.generate_contract_report())
        reports.append(self.generate_workload_evidence_report())
        reports.append(self.generate_crisis_report())
        reports.append(self.generate_timeline_report())

        print("\n" + "=" * 60)
        print(f"ALL REPORTS GENERATED - Saved to: {self.reports_dir}")
        print("=" * 60 + "\n")

        return reports


def main():
    """Generate sample reports."""
    rg = ReportGenerator()
    rg.generate_all_reports()


if __name__ == "__main__":
    main()
