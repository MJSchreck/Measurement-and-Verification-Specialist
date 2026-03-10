"""Prompt templates for M&V report reconciliation workflows."""

from .registry import prompt_registry

# --- Version 1: Basic reconciliation ---
prompt_registry.register(
    name="reconciliation.analyze",
    version="v1",
    template="""You are an M&V Specialist reviewing energy savings reconciliation data.

## Contract: {contract_id}

## Guaranteed Savings (from ESPC/UESC contract):
{guaranteed_savings}

## Actual Measured Savings (from M&V report):
{actual_savings}

## Task:
1. Compare guaranteed vs. actual savings for each ECM
2. Calculate variance percentages
3. Flag any ECMs with shortfalls exceeding {tolerance_pct}%
4. Identify potential causes for significant variances
5. Recommend specific actions for shortfall ECMs

## Output Format:
Provide a structured reconciliation summary with:
- Per-ECM comparison table
- Overall contract performance assessment
- Specific action items ranked by severity
- References to relevant IPMVP provisions

Use precise M&V terminology. Do not use "expected" — use "guaranteed."
Do not use "real" — use "actual measured."
""",
    description="Basic reconciliation analysis prompt",
    is_default=True,
    metadata={"domain": "reconciliation", "complexity": "standard"},
)

# --- Version 2: Detailed with adjustment analysis ---
prompt_registry.register(
    name="reconciliation.analyze",
    version="v2",
    template="""You are a senior M&V Specialist at a federal energy management agency
reconciling performance contract savings.

## Contract: {contract_id}
## Performance Period: Year {performance_year}

## Guaranteed Savings by ECM:
{guaranteed_savings}

## Actual Measured Savings by ECM:
{actual_savings}

## Adjustment Factors Applied:
{adjustments}

## Historical Context:
{historical_context}

## Task:
1. Compare guaranteed vs. actual savings for each ECM, noting adjustment impacts
2. Calculate variance percentages (pre- and post-adjustment)
3. Flag ECMs with shortfalls exceeding {tolerance_pct}%
4. Analyze whether adjustments are properly justified per IPMVP
5. Compare current year performance against historical trend
6. Assess whether ESCO remediation is warranted per contract Section H
7. Draft reconciliation memo for Contracting Officer review

## M&V Terminology Requirements:
- "Guaranteed savings" (not "expected")
- "Actual measured savings" (not "real" or "observed")
- "Baseline" (not "benchmark" in savings context)
- "Adjustment" (not "correction" or "normalization")
- Reference IPMVP Options (A/B/C/D) by their formal definitions

## Output:
Structured reconciliation with executive summary, per-ECM detail,
trend analysis, and recommended actions with priority levels.
""",
    description="Detailed reconciliation with adjustments and historical comparison",
    metadata={"domain": "reconciliation", "complexity": "advanced"},
)

# --- Reconciliation Summary ---
prompt_registry.register(
    name="reconciliation.summary",
    version="v1",
    template="""Summarize this M&V reconciliation for a portfolio briefing.

## Reconciliation Data:
{reconciliation_result}

## Requirements:
- 3-5 bullet executive summary
- Overall pass/fail status with total savings achieved
- Top risk items (if any)
- One-sentence recommendation
- Suitable for a non-technical audience (facility managers, COs)
""",
    description="Executive summary of reconciliation for briefings",
    is_default=True,
)
