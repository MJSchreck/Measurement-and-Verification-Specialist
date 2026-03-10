"""Shared test fixtures for M&V agent tests."""

import json
import tempfile
from pathlib import Path

import pytest

from src.mv_agent.agent import MVAgent
from src.mv_agent.observability.store import TraceStore
from src.mv_agent.observability.tracer import clear_trace_buffer


@pytest.fixture
def temp_db(tmp_path):
    """Create a temporary SQLite database for tests."""
    return tmp_path / "test_traces.db"


@pytest.fixture
def store(temp_db):
    """Create a TraceStore with a temp database."""
    return TraceStore(db_path=temp_db)


@pytest.fixture
def agent(temp_db):
    """Create an MVAgent instance with a temp database."""
    clear_trace_buffer()
    return MVAgent(trace_db_path=temp_db)


@pytest.fixture
def sample_report_path(tmp_path):
    """Create a sample M&V report JSON file."""
    report = {
        "facility_name": "Federal Building 101",
        "report_period": "FY2025",
        "ecms": [
            {
                "ecm_id": "ECM-001",
                "description": "LED Lighting Retrofit",
                "guaranteed_savings_kwh": 500000,
                "actual_savings_kwh": 520000,
                "guaranteed_savings_cost": 50000,
                "actual_savings_cost": 52000,
                "ipmvp_option": "B",
                "measurement_period": "Oct 2024 - Sep 2025",
            },
            {
                "ecm_id": "ECM-002",
                "description": "HVAC Controls Upgrade",
                "guaranteed_savings_kwh": 300000,
                "actual_savings_kwh": 250000,
                "guaranteed_savings_cost": 30000,
                "actual_savings_cost": 25000,
                "ipmvp_option": "C",
                "measurement_period": "Oct 2024 - Sep 2025",
            },
            {
                "ecm_id": "ECM-003",
                "description": "Building Envelope Improvements",
                "guaranteed_savings_kwh": 200000,
                "actual_savings_kwh": 210000,
                "guaranteed_savings_cost": 20000,
                "actual_savings_cost": 21000,
                "ipmvp_option": "A",
                "measurement_period": "Oct 2024 - Sep 2025",
            },
        ],
    }

    path = tmp_path / "sample_report.json"
    path.write_text(json.dumps(report, indent=2))
    return str(path)


@pytest.fixture
def sample_guaranteed_savings():
    """Sample guaranteed savings data for reconciliation tests."""
    return {
        "ECM-001": 500000,
        "ECM-002": 300000,
        "ECM-003": 200000,
    }


@pytest.fixture
def sample_actual_savings():
    """Sample actual savings data (ECM-002 has shortfall)."""
    return {
        "ECM-001": 520000,
        "ECM-002": 250000,
        "ECM-003": 210000,
    }


@pytest.fixture
def sample_facility_data():
    """Sample facility data for compliance checks."""
    return {
        "carbon_free_electric_pct": 45,
        "energy_reduction_pct": 35,
        "eui_reduction_pct": 25,
        "metered": True,
        "renewable_pct": 8.0,
        "energy_star_score": 72,
    }


@pytest.fixture
def sample_utility_data():
    """Sample 12-month utility billing data."""
    months = [
        "2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06",
        "2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12",
    ]
    kwh_values = [
        85000, 78000, 72000, 65000, 58000, 95000,
        105000, 110000, 98000, 70000, 75000, 82000,
    ]
    return [
        {
            "period": month,
            "utility_type": "electric",
            "consumption": kwh,
            "unit": "kwh",
            "cost": kwh * 0.10,
        }
        for month, kwh in zip(months, kwh_values)
    ]
