"""Seed the trace database with realistic demo data for the dashboard.

Run: python dashboard/seed_demo_data.py
"""

import sys
import random
from pathlib import Path
from datetime import datetime, timedelta, timezone
from uuid import uuid4

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.mv_agent.observability.store import TraceStore
from src.mv_agent.models.schemas import TraceRecord, EvalResult

TOOLS = [
    "parse_mv_report",
    "reconcile_savings",
    "analyze_contract",
    "check_compliance",
    "process_utility_data",
]

MODELS = [
    "claude-sonnet-4-20250514",
    "claude-haiku-3.5",
    "gpt-4o",
    "gpt-4o-mini",
]

PROMPT_CONFIGS = [
    ("reconciliation.analyze", ["v1", "v2"]),
    ("reconciliation.summary", ["v1"]),
    ("contract.analyze", ["v1"]),
    ("compliance.assess", ["v1"]),
    ("audit.benchmark", ["v1"]),
]

ERRORS = [
    "FileNotFoundError: Report file not found",
    "ParseError: Unable to read PDF structure",
    "SchemaValidationError: Missing required field 'ecm_id'",
    "TimeoutError: LLM request timed out after 30s",
    "ValueError: Unsupported file format",
]


def seed_traces(store: TraceStore, count: int = 500):
    """Generate realistic trace records."""
    now = datetime.now(timezone.utc)
    traces = []

    for i in range(count):
        tool = random.choice(TOOLS)
        model = random.choice(MODELS)
        prompt_name, versions = random.choice(PROMPT_CONFIGS)
        version = random.choice(versions)

        success = random.random() > 0.08  # ~92% success rate

        # Vary latency by tool
        base_latency = {
            "parse_mv_report": 200,
            "reconcile_savings": 50,
            "analyze_contract": 1500,
            "check_compliance": 80,
            "process_utility_data": 30,
        }
        latency = max(5, int(random.gauss(base_latency.get(tool, 100), base_latency.get(tool, 100) * 0.4)))

        # Token counts
        input_tokens = random.randint(500, 8000)
        output_tokens = random.randint(200, 4000)

        # Cost based on model
        cost_rates = {
            "claude-sonnet-4-20250514": (0.003, 0.015),
            "claude-haiku-3.5": (0.001, 0.005),
            "gpt-4o": (0.005, 0.015),
            "gpt-4o-mini": (0.00015, 0.0006),
        }
        in_rate, out_rate = cost_rates.get(model, (0.003, 0.015))
        cost = (input_tokens / 1000) * in_rate + (output_tokens / 1000) * out_rate

        trace = TraceRecord(
            trace_id=uuid4(),
            timestamp=now - timedelta(hours=random.uniform(0, 720)),
            tool_name=tool,
            prompt_name=prompt_name,
            prompt_version=version,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_usd=round(cost, 6),
            latency_ms=latency,
            success=success,
            error=random.choice(ERRORS) if not success else "",
            input_hash=f"in_{uuid4().hex[:8]}",
            output_hash=f"out_{uuid4().hex[:8]}",
        )
        traces.append(trace)

    store.save_traces(traces)
    print(f"Seeded {len(traces)} traces")


def seed_evals(store: TraceStore, count: int = 100):
    """Generate realistic eval results."""
    now = datetime.now(timezone.utc)

    eval_names = [
        "test_eval_pass_within_tolerance",
        "test_eval_shortfall_detection",
        "test_eval_excess_savings",
        "test_eval_kwh_to_kbtu_conversion",
        "test_eval_eui_calculation",
        "test_eval_full_compliance",
        "test_eval_eo14057_non_compliant",
        "test_eval_espc_period_extraction",
        "test_eval_espc_savings_extraction",
        "test_eval_anomaly_detection",
    ]

    for i in range(count):
        name = random.choice(eval_names)
        version = random.choice(["v1", "v2"])
        passed = random.random() > 0.12  # ~88% pass rate

        result = EvalResult(
            eval_id=f"eval_{uuid4().hex[:8]}",
            eval_name=name,
            prompt_version=version,
            passed=passed,
            score=random.uniform(0.7, 1.0) if passed else random.uniform(0.0, 0.5),
            expected="Expected value" if not passed else "",
            actual="Actual value" if not passed else "",
            details=f"Run at {now - timedelta(hours=random.uniform(0, 720))}",
            trace_id=uuid4(),
            timestamp=now - timedelta(hours=random.uniform(0, 720)),
        )
        store.save_eval(result)

    print(f"Seeded {count} eval results")


if __name__ == "__main__":
    store = TraceStore()
    seed_traces(store, 500)
    seed_evals(store, 100)
    stats = store.get_stats()
    print(f"Database stats: {stats}")
    print(f"Database path: {store.db_path}")
