"""Analyze ESPC/UESC contracts and extract key provisions."""

import logging
import re

from ..models.schemas import ContractAnalysis
from ..models.enums import ContractType, IPMVPOption
from ..observability.tracer import traced

logger = logging.getLogger(__name__)


@traced(tool_name="analyze_contract")
def analyze_contract(
    contract_text: str,
    contract_type: str = "ESPC",
    analysis_focus: list[str] | None = None,
) -> ContractAnalysis:
    """Review ESPC/UESC contract terms and extract key provisions.

    Args:
        contract_text: Full contract text or relevant sections.
        contract_type: "ESPC" or "UESC".
        analysis_focus: Which aspects to focus on. Defaults to all.

    Returns:
        ContractAnalysis with extracted terms, risks, and recommendations.
    """
    ct = ContractType(contract_type)
    focus = set(analysis_focus or [
        "savings_guarantees", "performance_period",
        "mv_methodology", "esco_obligations",
    ])

    logger.info("Analyzing %s contract (%d chars), focus: %s", ct.value, len(contract_text), focus)

    key_terms = {}
    risks = []
    recommendations = []
    mv_options = []

    text_lower = contract_text.lower()

    # Extract performance period
    if "performance_period" in focus:
        period_match = re.search(
            r"performance\s+period\s*(?:of|:)?\s*(\d+)\s*(?:year|yr)", text_lower
        )
        if period_match:
            key_terms["performance_period_years"] = int(period_match.group(1))

    # Extract savings guarantees
    if "savings_guarantees" in focus:
        savings_patterns = [
            r"guaranteed\s+(?:annual\s+)?savings\s*(?:of|:)?\s*\$?([\d,]+(?:\.\d+)?)",
            r"annual\s+guaranteed\s+savings\s*(?:of|:)?\s*\$?([\d,]+(?:\.\d+)?)",
        ]
        for pattern in savings_patterns:
            match = re.search(pattern, text_lower)
            if match:
                key_terms["annual_guaranteed_savings"] = float(
                    match.group(1).replace(",", "")
                )
                break

    # Detect IPMVP options
    if "mv_methodology" in focus:
        for option in IPMVPOption:
            if f"option {option.value.lower()}" in text_lower or f"ipmvp {option.value}" in text_lower:
                mv_options.append(option)

    # Risk analysis
    if "escalation" in text_lower:
        risks.append("Contract contains escalation rate provisions — verify rates match current projections")
    if "termination" not in text_lower:
        risks.append("No termination clause found — review for government exit provisions")
    if not mv_options:
        risks.append("No IPMVP option specified — M&V methodology unclear")
        recommendations.append("Request ESCO clarification on measurement methodology per IPMVP")

    # Recommendations
    if ct == ContractType.ESPC:
        recommendations.append("Verify ESCO annual M&V report submission schedule")
        recommendations.append("Confirm savings guarantee shortfall remedy provisions")
    elif ct == ContractType.UESC:
        recommendations.append("Verify utility rate schedule alignment with contract assumptions")

    performance_years = key_terms.get("performance_period_years", 0)
    annual_savings = key_terms.get("annual_guaranteed_savings", 0)

    return ContractAnalysis(
        contract_type=ct,
        performance_period_years=performance_years,
        total_guaranteed_savings=annual_savings * performance_years,
        annual_guaranteed_savings=annual_savings,
        ecm_count=text_lower.count("ecm") // 2,  # rough heuristic
        mv_options_used=mv_options,
        key_terms=key_terms,
        risks=risks,
        recommendations=recommendations,
    )
