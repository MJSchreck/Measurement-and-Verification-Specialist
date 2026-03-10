"""Prompt templates for policy compliance check workflows."""

from .registry import prompt_registry

# --- Compliance Assessment ---
prompt_registry.register(
    name="compliance.assess",
    version="v1",
    template="""You are a federal energy policy compliance specialist.

## Facility Data:
{facility_data}

## Policies to Check:
{policies}

## Project Type: {project_type}

## Task:
1. For each policy, check all applicable requirements
2. Mark each requirement as COMPLIANT, NON_COMPLIANT, or INSUFFICIENT_DATA
3. For non-compliant items, calculate the gap (current value vs. required)
4. Provide specific remediation steps with estimated timelines
5. Prioritize gaps by regulatory risk and implementation difficulty

## Key Policy References:
- EO 14057: 100% carbon-free electricity by 2030, net-zero by 2050
- EISA 2007 Sec 433: Fossil fuel reduction in new federal buildings
- EPACT 2005 Sec 103: Advanced metering in federal buildings
- 10 CFR 433/435: Federal building energy efficiency standards
- Guiding Principles: High-performance sustainable federal buildings

## Output:
Structured compliance report with:
- Executive summary (overall status)
- Per-policy detailed findings
- Gap analysis table
- Remediation roadmap with quick wins vs. long-term items
""",
    description="Multi-policy compliance assessment",
    is_default=True,
)

# --- Compliance Memo ---
prompt_registry.register(
    name="compliance.memo",
    version="v1",
    template="""Draft a compliance memo for leadership review.

## Compliance Results:
{compliance_results}

## Requirements:
- 1-page executive format
- Lead with overall status and key risks
- Include a compliance scorecard (policy | status | gap)
- Recommend top 3 priority actions
- Note any upcoming deadlines or reporting requirements
- Tone: professional, concise, action-oriented
""",
    description="Leadership compliance memo",
    is_default=True,
)
