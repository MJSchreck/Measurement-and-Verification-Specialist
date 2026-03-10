# Observability Plan — M&V Specialist Agent

## Overview

This plan defines how we instrument, collect, and analyze telemetry from the
M&V agent so you can **see where prompts fail instead of guessing**.

---

## Three Pillars

### 1. Tracing (What Happened)

Every tool call and prompt execution is traced via the `@traced` decorator.

**What gets captured:**
- Trace ID (UUID) for correlation
- Tool name and prompt name/version
- Input hash and output hash (for diffing across versions)
- LLM model used
- Token counts (input + output)
- Cost in USD (calculated from model pricing)
- Wall-clock latency (milliseconds)
- Success/failure status
- Error message (if failed)
- Timestamp

**Where it lives:**
- In-memory buffer during execution (`observability/tracer.py`)
- Flushed to SQLite at `~/.mv_agent/traces.db` via `TraceStore`
- Queryable via dashboard or direct SQL

**How to use:**
```python
from mv_agent.observability.tracer import traced

@traced(tool_name="my_new_tool")
def my_new_tool(input_data: dict) -> dict:
    ...
```

### 2. Metrics (How It's Performing)

The `MetricsAggregator` computes derived metrics from raw traces:

| Metric | Level | Calculation |
|--------|-------|-------------|
| Success rate | Per tool, per prompt | success_count / total_calls |
| Avg latency | Per tool, per prompt | total_latency / total_calls |
| P50/P90/P95 latency | Per tool | Sorted percentile |
| Cost per call | Per model | Tokens × model pricing |
| Cumulative cost | Session, total | Sum of all call costs |
| Error rate by type | Per prompt version | Grouped error messages |

**Where to see them:** Eval dashboard → "Success Rates" and "Cost Analysis" pages.

### 3. Eval Results (Is It Correct)

Eval cases in `tests/eval_cases/` validate domain-specific correctness:

| Category | What it tests | Examples |
|----------|---------------|---------|
| Reconciliation | Savings math, shortfall detection | Does it flag ECM-002 at -16.7%? |
| Contract | Term extraction, risk flagging | Does it find the 20-year period? |
| Compliance | Policy threshold checks | Does it fail a 45% facility on EO 14057? |
| Utility | Unit conversions, EUI math | Does 100K kWh = 341,200 kBTU? |

Eval results are stored in the same SQLite database and visible in the
dashboard alongside trace data.

---

## Prompt Failure Analysis

This is the core value prop — when a prompt doesn't work, here's how to find out why:

### Step 1: Check the Dashboard

Open the eval dashboard and go to "Prompt Comparison." Select the failing
prompt and compare its current version against the previous one.

### Step 2: Review Trace Details

Click into any failing trace to see:
- What inputs triggered the failure
- What the model actually returned
- How long it took (latency spike = possible timeout)
- How many tokens were used (bloated = prompt needs trimming)

### Step 3: Compare Versions

The dashboard's prompt comparison view shows side-by-side:
- Success rate: v1 vs. v2
- Average latency: v1 vs. v2
- Cost per call: v1 vs. v2
- Error distribution: v1 vs. v2

### Step 4: Create a Regression Test

Once you identify the failure, add an eval case that captures it:
```python
def test_eval_specific_failure_scenario(self):
    """EVAL: [description of what broke]"""
    result = some_tool(...)
    assert result.expected_behavior
```

Run `pytest tests/eval_cases/ -v` to confirm the fix.

---

## Alert Conditions

The following conditions should trigger investigation:

| Condition | Threshold | Action |
|-----------|-----------|--------|
| Success rate drops | < 90% for any tool | Check recent prompt changes |
| Latency spike | P95 > 10s | Check model availability, input size |
| Cost spike | > 2x historical avg | Check token counts, model selection |
| New error type | Any | Add regression test, fix prompt |
| Eval failure | Any test fails | Block deployment, investigate |

---

## Data Retention

- **Traces:** Retained indefinitely in SQLite (lightweight)
- **Eval results:** Retained indefinitely
- **In-memory buffer:** Cleared on flush or process exit
- **Dashboard:** Reads from SQLite in real-time

---

## Adding Observability to New Components

1. Import `@traced` decorator
2. Add it to your function with `tool_name` or `prompt_name`
3. Add eval cases in `tests/eval_cases/`
4. Verify traces appear in the dashboard
5. Set up any custom alert thresholds in your monitoring

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    M&V Agent                             │
│                                                          │
│  ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Report   │  │ Savings │  │ Contract │  │Compliance│  │
│  │ Parser   │  │ Reconc. │  │ Analyzer │  │ Checker  │  │
│  └────┬─────┘  └────┬────┘  └────┬─────┘  └────┬─────┘  │
│       │             │            │              │         │
│       └─────────────┴────────────┴──────────────┘         │
│                         │                                 │
│                   @traced decorator                       │
│                         │                                 │
│              ┌──────────▼──────────┐                     │
│              │  In-Memory Buffer   │                     │
│              └──────────┬──────────┘                     │
│                         │ flush                          │
│              ┌──────────▼──────────┐                     │
│              │   SQLite TraceDB    │                     │
│              │  ~/.mv_agent/       │                     │
│              │    traces.db        │                     │
│              └──────────┬──────────┘                     │
│                         │                                │
└─────────────────────────┼────────────────────────────────┘
                          │
               ┌──────────▼──────────┐
               │  Streamlit Dashboard │
               │  - Prompt Comparison │
               │  - Trace Viewer      │
               │  - Cost Analysis     │
               │  - Success Rates     │
               └──────────────────────┘
```
