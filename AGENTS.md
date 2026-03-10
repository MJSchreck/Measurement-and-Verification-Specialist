# AGENTS.md — M&V Specialist Agent Instructions

> **Purpose:** This file tells any AI agent (Claude, GPT, Codex, Copilot) how to
> navigate, build, and extend this codebase. Drop into the repo root so agents
> discover it automatically.

---

## Project Overview

**Measurement & Verification (M&V) Specialist** is an agent-ready toolkit for
federal energy management workflows. It provides:

- **MCP tools** for parsing M&V reports, reconciling savings, auditing ESPC/UESC
  contracts, and checking policy compliance
- **Prompt templates** for common analyst tasks
- **An eval + observability layer** so you can compare prompt versions, track
  tool-call traces, measure cost/latency, and monitor task success rates
- **A Streamlit dashboard** for visual analysis of all the above

### Domain Context

This system supports the work of a **Certified Energy Manager** at the GSA who:
- Administers Energy Savings Performance Contracts (ESPCs) and Utility Energy
  Service Contracts (UESCs)
- Reconciles Measurement & Verification reports against guaranteed savings
- Runs energy audits, benchmarking studies, and portfolio briefings
- Ensures compliance with Executive Orders (EO 14057, etc.), EISA, and EPACT

---

## Repository Structure

```
├── AGENTS.md                   # You are here
├── MCP_TOOLS.md                # Full MCP tool map with schemas
├── README.md                   # Human-readable project overview
├── pyproject.toml              # Python project config
├── requirements.txt            # Pinned dependencies
│
├── src/mv_agent/
│   ├── __init__.py
│   ├── config.py               # Environment + model config
│   ├── agent.py                # Core agent orchestrator
│   │
│   ├── tools/                  # MCP tool implementations
│   │   ├── __init__.py
│   │   ├── report_parser.py    # Parse M&V reports (PDF/Excel)
│   │   ├── savings_reconciler.py  # Compare guaranteed vs actual savings
│   │   ├── contract_analyzer.py   # ESPC/UESC contract review
│   │   ├── compliance_checker.py  # Policy/EO compliance validation
│   │   └── utility_processor.py   # Utility bill data processing
│   │
│   ├── prompts/                # Versioned prompt templates
│   │   ├── __init__.py
│   │   ├── registry.py         # Prompt version registry
│   │   ├── reconciliation.py   # M&V report reconciliation prompts
│   │   ├── contract_review.py  # ESPC/UESC analysis prompts
│   │   ├── audit_support.py    # Energy audit prompts
│   │   └── compliance.py       # Policy compliance prompts
│   │
│   ├── models/                 # Data models
│   │   ├── __init__.py
│   │   ├── schemas.py          # Pydantic models for all domain objects
│   │   └── enums.py            # Shared enumerations
│   │
│   └── observability/          # Logging, tracing, metrics
│       ├── __init__.py
│       ├── tracer.py           # Tool-call and prompt tracing
│       ├── cost_tracker.py     # Token usage and cost calculation
│       ├── metrics.py          # Success rate, latency aggregation
│       └── store.py            # SQLite-backed trace storage
│
├── tests/
│   ├── conftest.py             # Shared fixtures
│   ├── eval_cases/             # Evaluation test cases
│   │   ├── test_reconciliation_eval.py
│   │   ├── test_contract_eval.py
│   │   ├── test_audit_eval.py
│   │   └── test_compliance_eval.py
│   ├── regression/             # Regression tests
│   │   ├── test_prompt_regression.py
│   │   └── test_tool_regression.py
│   └── fixtures/               # Test data files
│       └── sample_report.json
│
├── dashboard/                  # Streamlit eval dashboard
│   ├── app.py                  # Main dashboard entry
│   ├── pages/
│   │   ├── prompt_comparison.py
│   │   ├── trace_viewer.py
│   │   ├── cost_analysis.py
│   │   └── success_rates.py
│   └── components/
│       └── charts.py
│
├── docs/
│   ├── OBSERVABILITY_PLAN.md   # Full observability strategy
│   └── EVAL_GUIDE.md           # How to write and run evals
│
└── .github/workflows/
    └── eval.yml                # CI pipeline for regression tests
```

---

## Agent Instructions

### When working on this codebase, follow these rules:

1. **Always check `MCP_TOOLS.md`** before adding or modifying tools. It is the
   single source of truth for tool schemas, input/output contracts, and which
   tools are available.

2. **Prompt templates are versioned.** Never edit a prompt in-place. Create a
   new version via `PromptRegistry.register()` and update the default pointer.
   Old versions must remain accessible for A/B comparison.

3. **Every tool call gets traced.** Use the `@traced` decorator from
   `observability/tracer.py` on all tool functions. This captures input, output,
   latency, token count, and cost automatically.

4. **Write eval cases for every prompt change.** If you modify a prompt, add or
   update a test in `tests/eval_cases/` that validates expected behavior. Run
   `pytest tests/eval_cases/ -v` before committing.

5. **Domain terminology matters.** Use precise M&V language:
   - "Guaranteed savings" vs "Actual savings" (never "expected" vs "real")
   - "ECM" = Energy Conservation Measure
   - "IPMVP" = International Performance Measurement and Verification Protocol
   - "Option A/B/C/D" = IPMVP measurement options
   - "Baseline" = pre-retrofit energy usage
   - "Post-installation" = after ECM implementation
   - "Adjustment" = normalized corrections to baseline

6. **Keep the SQLite trace store portable.** The dashboard reads from
   `~/.mv_agent/traces.db`. Never change this path without updating both
   `observability/store.py` and `dashboard/app.py`.

7. **Cost tracking uses real pricing.** Update `observability/cost_tracker.py`
   when model pricing changes. Current defaults are for Claude Sonnet and GPT-4.

---

## Common Agent Tasks

| Task | Command | Notes |
|------|---------|-------|
| Run all tests | `pytest tests/ -v` | Includes eval + regression |
| Run evals only | `pytest tests/eval_cases/ -v` | Domain-specific validation |
| Run regression | `pytest tests/regression/ -v` | Catches prompt drift |
| Launch dashboard | `streamlit run dashboard/app.py` | Opens on port 8501 |
| Add a new tool | See MCP_TOOLS.md "Adding Tools" section | |
| Version a prompt | See `src/mv_agent/prompts/registry.py` | |

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | For Claude | Claude API access |
| `OPENAI_API_KEY` | For GPT | OpenAI API access |
| `MV_AGENT_MODEL` | No | Default model (default: `claude-sonnet-4-20250514`) |
| `MV_AGENT_TRACE_DB` | No | Trace DB path (default: `~/.mv_agent/traces.db`) |
| `MV_AGENT_LOG_LEVEL` | No | Logging level (default: `INFO`) |

---

## Code Style

- Python 3.11+, type hints on all public functions
- Pydantic v2 for data models
- `ruff` for linting, `black` for formatting
- Docstrings on all public classes and functions (Google style)
- No `print()` — use the `logging` module
