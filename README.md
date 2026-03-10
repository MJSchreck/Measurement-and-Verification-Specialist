# M&V Specialist — Agent-Ready Energy Management Toolkit

An agent-ready codebase for federal Measurement & Verification (M&V) workflows,
built for Energy Savings Performance Contracts (ESPCs), Utility Energy Service
Contracts (UESCs), energy audits, and policy compliance.

## What's in the box

| Component | Description |
|-----------|-------------|
| **AGENTS.md** | Agent instructions — tells Claude/GPT/Copilot how to navigate this codebase |
| **MCP_TOOLS.md** | Full MCP tool map with schemas for 5 domain tools |
| **Prompt templates** | 9 versioned prompts across 4 workflow areas |
| **Eval cases** | 32 domain-specific evaluation tests |
| **Regression tests** | 16 tests that catch prompt drift and schema changes |
| **Observability layer** | Tracing, cost tracking, metrics, SQLite store |
| **Streamlit dashboard** | Local dashboard for prompt comparison and trace analysis |
| **CI pipeline** | GitHub Actions workflow for automated eval runs |

## Quick start

```bash
# Install
pip install -e .

# Run all tests (48 total)
pytest tests/ -v

# Seed demo data and launch dashboard
python dashboard/seed_demo_data.py
streamlit run dashboard/app.py
```

## MCP Tools

| Tool | Purpose |
|------|---------|
| `parse_mv_report` | Extract structured data from M&V reports (PDF/Excel/JSON) |
| `reconcile_savings` | Compare guaranteed vs. actual savings, flag shortfalls |
| `analyze_contract` | Review ESPC/UESC terms, extract guarantees and risks |
| `check_compliance` | Validate against EO 14057, EISA, EPACT, ENERGY STAR |
| `process_utility_data` | Parse utility bills, calculate EUI, detect anomalies |

## Prompt templates

All prompts are versioned and A/B comparable:

- `reconciliation.analyze` (v1, v2) — M&V report reconciliation
- `reconciliation.summary` — Executive briefing summary
- `contract.analyze` — ESPC/UESC contract review
- `contract.compare` — Side-by-side contract comparison
- `audit.benchmark` — Facility benchmarking and ECM identification
- `audit.utility_analysis` — Utility billing trend analysis
- `compliance.assess` — Multi-policy compliance assessment
- `compliance.memo` — Leadership compliance memo

## Observability

Every tool call is automatically traced with:
- Input/output hashes, token counts, cost, latency
- Prompt name and version for A/B tracking
- Success/failure status with error capture

See `docs/OBSERVABILITY_PLAN.md` for the full strategy.

## Project structure

```
├── AGENTS.md                   # Agent navigation instructions
├── MCP_TOOLS.md                # MCP tool schemas
├── src/mv_agent/               # Core package
│   ├── tools/                  # 5 MCP tool implementations
│   ├── prompts/                # Versioned prompt registry
│   ├── models/                 # Pydantic domain models
│   └── observability/          # Tracing, metrics, storage
├── tests/
│   ├── eval_cases/             # 32 domain eval tests
│   └── regression/             # 16 regression tests
├── dashboard/                  # Streamlit eval dashboard
├── docs/                       # Observability plan, eval guide
└── .github/workflows/          # CI pipeline
```

## License

MIT
