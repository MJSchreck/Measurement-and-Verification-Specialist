"""Prompt templates for ESPC/UESC contract review workflows."""

from .registry import prompt_registry

# --- Contract Analysis ---
prompt_registry.register(
    name="contract.analyze",
    version="v1",
    template="""You are an energy contracting specialist reviewing a federal {contract_type} contract.

## Contract Text:
{contract_text}

## Analysis Focus:
{analysis_focus}

## Task:
1. Extract all savings guarantee amounts (annual and total)
2. Identify the performance period and key milestone dates
3. Document M&V methodology (IPMVP options specified)
4. List all ECMs with descriptions and individual guarantees
5. Flag risks: missing clauses, ambiguous terms, unfavorable escalation rates
6. Note government obligations and ESCO obligations separately
7. Identify any deviations from standard DOE ESPC IDIQ templates

## Output:
Structured analysis with:
- Contract overview (type, period, total value)
- Savings guarantee summary table
- M&V methodology assessment
- Risk register (severity: high/medium/low)
- Recommended negotiation points or amendments
""",
    description="Standard ESPC/UESC contract analysis",
    is_default=True,
)

# --- Contract Comparison ---
prompt_registry.register(
    name="contract.compare",
    version="v1",
    template="""Compare these two performance contracts and identify key differences.

## Contract A:
{contract_a}

## Contract B:
{contract_b}

## Focus Areas:
- Savings guarantee structures
- M&V methodology differences
- Risk allocation (government vs. ESCO)
- Escalation rate assumptions
- Performance period and payment terms

## Output:
Side-by-side comparison table with risk assessment for each difference.
""",
    description="Compare two ESPC/UESC contracts",
    is_default=True,
)
