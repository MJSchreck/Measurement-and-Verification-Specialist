#!/usr/bin/env python3
"""
GSA Zone C Portfolio Workload Tracker
Portfolio Manager - Core Data Management Module

Author: Matthew Schreck
Role: Energy Program Specialist / M&V Specialist, Zone C MVP Lead
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any

# Base paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"


class PortfolioManager:
    """Manages the GSA Zone C ESPC/UESC contract portfolio."""

    def __init__(self):
        self.contracts_file = DATA_DIR / "contracts_database.json"
        self.timeline_file = DATA_DIR / "timeline_events.json"
        self.metrics_file = DATA_DIR / "workload_metrics.json"
        self.crisis_file = DATA_DIR / "crisis_documentation.json"

        self.contracts_data = self._load_json(self.contracts_file)
        self.timeline_data = self._load_json(self.timeline_file)
        self.metrics_data = self._load_json(self.metrics_file)
        self.crisis_data = self._load_json(self.crisis_file)

    def _load_json(self, filepath: Path) -> Dict:
        """Load JSON data from file."""
        if filepath.exists():
            with open(filepath, 'r') as f:
                return json.load(f)
        return {}

    def _save_json(self, data: Dict, filepath: Path) -> None:
        """Save JSON data to file."""
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    def save_all(self) -> None:
        """Save all data files."""
        self._save_json(self.contracts_data, self.contracts_file)
        self._save_json(self.timeline_data, self.timeline_file)
        self._save_json(self.metrics_data, self.metrics_file)
        self._save_json(self.crisis_data, self.crisis_file)
        print("All data saved successfully.")

    # =========================================================================
    # CONTRACT MANAGEMENT
    # =========================================================================

    def add_contract(self, contract: Dict) -> str:
        """Add a new contract to the portfolio."""
        contract_id = f"CONTRACT-{len(self.contracts_data.get('contracts', [])) + 1:03d}"
        contract['id'] = contract_id
        contract['date_added'] = datetime.now().isoformat()

        if 'contracts' not in self.contracts_data:
            self.contracts_data['contracts'] = []

        self.contracts_data['contracts'].append(contract)
        self._update_metadata()
        return contract_id

    def update_contract(self, contract_id: str, updates: Dict) -> bool:
        """Update an existing contract."""
        for i, contract in enumerate(self.contracts_data.get('contracts', [])):
            if contract['id'] == contract_id:
                self.contracts_data['contracts'][i].update(updates)
                self.contracts_data['contracts'][i]['last_updated'] = datetime.now().isoformat()
                return True
        return False

    def get_contract(self, contract_id: str) -> Optional[Dict]:
        """Get a specific contract by ID."""
        for contract in self.contracts_data.get('contracts', []):
            if contract['id'] == contract_id:
                return contract
        return None

    def get_all_contracts(self) -> List[Dict]:
        """Get all contracts."""
        return self.contracts_data.get('contracts', [])

    def get_contracts_by_status(self, status: str) -> List[Dict]:
        """Get contracts filtered by status."""
        return [c for c in self.get_all_contracts() if c.get('status') == status]

    def get_contracts_by_type(self, contract_type: str) -> List[Dict]:
        """Get contracts filtered by type (ESPC/UESC)."""
        return [c for c in self.get_all_contracts() if c.get('type') == contract_type]

    def _update_metadata(self) -> None:
        """Update portfolio metadata."""
        contracts = self.get_all_contracts()
        self.contracts_data['metadata']['total_contracts'] = len(contracts)
        self.contracts_data['metadata']['total_portfolio_value'] = sum(
            c.get('contract_value', 0) for c in contracts
        )
        self.contracts_data['metadata']['last_updated'] = datetime.now().isoformat()

    # =========================================================================
    # TIMELINE MANAGEMENT
    # =========================================================================

    def add_event(self, event: Dict) -> str:
        """Add a timeline event."""
        event_id = f"EVT-{len(self.timeline_data.get('events', [])) + 1:03d}"
        event['event_id'] = event_id
        event['created_at'] = datetime.now().isoformat()

        if 'events' not in self.timeline_data:
            self.timeline_data['events'] = []

        self.timeline_data['events'].append(event)
        return event_id

    def get_events_by_phase(self, phase: str) -> List[Dict]:
        """Get events for a specific phase."""
        return [e for e in self.timeline_data.get('events', []) if e.get('phase') == phase]

    def get_events_by_category(self, category: str) -> List[Dict]:
        """Get events by category."""
        return [e for e in self.timeline_data.get('events', []) if e.get('category') == category]

    def get_events_in_range(self, start_date: str, end_date: str) -> List[Dict]:
        """Get events within a date range."""
        events = []
        for event in self.timeline_data.get('events', []):
            event_date = event.get('date', '')
            if start_date <= event_date <= end_date:
                events.append(event)
        return sorted(events, key=lambda x: x.get('date', ''))

    def set_milestone(self, milestone_name: str, date: str) -> None:
        """Set a key milestone date."""
        if 'key_milestones' not in self.timeline_data:
            self.timeline_data['key_milestones'] = {}
        self.timeline_data['key_milestones'][milestone_name] = date

    # =========================================================================
    # METRICS MANAGEMENT
    # =========================================================================

    def update_metrics(self, category: str, metrics: Dict) -> None:
        """Update workload metrics for a category."""
        if category in self.metrics_data:
            self.metrics_data[category].update(metrics)
        else:
            self.metrics_data[category] = metrics
        self.metrics_data['metadata']['last_updated'] = datetime.now().isoformat()

    def increment_metric(self, category: str, metric_name: str, amount: int = 1) -> None:
        """Increment a specific metric."""
        if category in self.metrics_data and metric_name in self.metrics_data[category]:
            self.metrics_data[category][metric_name] += amount

    def log_m_and_v_review(self, contract_id: str, review_date: str, details: Dict = None) -> None:
        """Log an M&V review completion."""
        self.increment_metric('m_and_v_metrics', 'total_reviews_completed')
        self.increment_metric('m_and_v_metrics', 'reviews_this_fiscal_year')

        # Update contract-specific tracking
        if 'reviews_by_contract' not in self.metrics_data['m_and_v_metrics']:
            self.metrics_data['m_and_v_metrics']['reviews_by_contract'] = {}

        if contract_id not in self.metrics_data['m_and_v_metrics']['reviews_by_contract']:
            self.metrics_data['m_and_v_metrics']['reviews_by_contract'][contract_id] = []

        self.metrics_data['m_and_v_metrics']['reviews_by_contract'][contract_id].append({
            'date': review_date,
            'details': details or {}
        })

    def log_payment(self, contract_id: str, amount: float, date: str) -> None:
        """Log a payment processed."""
        self.increment_metric('payment_metrics', 'total_payments_processed')
        self.metrics_data['payment_metrics']['total_payment_value'] += amount
        self.increment_metric('payment_metrics', 'payments_this_fiscal_year')
        self.metrics_data['payment_metrics']['payment_value_this_fy'] += amount

    def log_issue(self, category: str, resolved: bool = False) -> None:
        """Log an issue identified or resolved."""
        self.increment_metric('issue_resolution_metrics', 'total_issues_identified')
        if resolved:
            self.increment_metric('issue_resolution_metrics', 'issues_resolved')
        else:
            self.increment_metric('issue_resolution_metrics', 'issues_open')

        if category in self.metrics_data['issue_resolution_metrics']['issues_by_category']:
            self.metrics_data['issue_resolution_metrics']['issues_by_category'][category] += 1

    # =========================================================================
    # CRISIS DOCUMENTATION
    # =========================================================================

    def update_crisis_staffing(self, original_size: int, current_size: int) -> None:
        """Update staffing crisis numbers."""
        self.crisis_data['staffing_impact']['original_team_size'] = original_size
        self.crisis_data['staffing_impact']['current_team_size'] = current_size
        self.crisis_data['staffing_impact']['reduction_percentage'] = round(
            ((original_size - current_size) / original_size) * 100, 1
        )

    def add_crisis_event(self, date: str, description: str, impact: str) -> None:
        """Add an event to the crisis timeline."""
        if 'departure_timeline' not in self.crisis_data['staffing_impact']:
            self.crisis_data['staffing_impact']['departure_timeline'] = []

        self.crisis_data['staffing_impact']['departure_timeline'].append({
            'date': date,
            'description': description,
            'impact': impact
        })

    def add_leadership_communication(self, date: str, audience: str, topic: str,
                                      outcome: str, follow_up: bool = False) -> None:
        """Log a leadership communication."""
        self.crisis_data['leadership_communications'].append({
            'date': date,
            'audience': audience,
            'topic': topic,
            'outcome': outcome,
            'follow_up_required': follow_up
        })

    # =========================================================================
    # PORTFOLIO SUMMARY
    # =========================================================================

    def get_portfolio_summary(self) -> Dict:
        """Generate a comprehensive portfolio summary."""
        contracts = self.get_all_contracts()

        espc_contracts = [c for c in contracts if c.get('type') == 'ESPC']
        uesc_contracts = [c for c in contracts if c.get('type') == 'UESC']

        return {
            'as_of_date': datetime.now().isoformat(),
            'portfolio_lead': self.contracts_data.get('metadata', {}).get('portfolio_lead', 'Matthew Schreck'),
            'total_contracts': len(contracts),
            'espc_count': len(espc_contracts),
            'uesc_count': len(uesc_contracts),
            'total_value': sum(c.get('contract_value', 0) for c in contracts),
            'espc_value': sum(c.get('contract_value', 0) for c in espc_contracts),
            'uesc_value': sum(c.get('contract_value', 0) for c in uesc_contracts),
            'active_contracts': len([c for c in contracts if 'Active' in c.get('status', '')]),
            'contracts_by_status': self._count_by_field(contracts, 'status'),
            'm_and_v_reviews_completed': self.metrics_data.get('m_and_v_metrics', {}).get('total_reviews_completed', 0),
            'payments_processed': self.metrics_data.get('payment_metrics', {}).get('total_payments_processed', 0),
            'payment_value': self.metrics_data.get('payment_metrics', {}).get('total_payment_value', 0),
            'issues_resolved': self.metrics_data.get('issue_resolution_metrics', {}).get('issues_resolved', 0),
            'staffing_reduction': self.crisis_data.get('staffing_impact', {}).get('reduction_percentage', 0)
        }

    def _count_by_field(self, items: List[Dict], field: str) -> Dict[str, int]:
        """Count items by a specific field value."""
        counts = {}
        for item in items:
            value = item.get(field, 'Unknown')
            counts[value] = counts.get(value, 0) + 1
        return counts


def main():
    """Demo/test the portfolio manager."""
    pm = PortfolioManager()

    print("=" * 60)
    print("GSA ZONE C PORTFOLIO WORKLOAD TRACKER")
    print("=" * 60)
    print(f"\nPortfolio Lead: Matthew Schreck")
    print(f"Role: Energy Program Specialist / M&V Specialist")
    print(f"Zone: C")
    print(f"\nCurrent Portfolio Status:")

    summary = pm.get_portfolio_summary()
    print(f"  Total Contracts: {summary['total_contracts']}")
    print(f"  Portfolio Value: ${summary['total_value']:,.2f}")
    print(f"  M&V Reviews Completed: {summary['m_and_v_reviews_completed']}")
    print(f"  Payments Processed: {summary['payments_processed']}")
    print(f"  Issues Resolved: {summary['issues_resolved']}")
    print(f"  Staffing Reduction: {summary['staffing_reduction']}%")

    print("\n" + "=" * 60)
    print("DATA STATUS: PLACEHOLDER - POPULATE WITH ACTUAL DATA")
    print("=" * 60)


if __name__ == "__main__":
    main()
