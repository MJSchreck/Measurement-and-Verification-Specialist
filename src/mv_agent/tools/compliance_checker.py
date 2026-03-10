"""Validate facilities/projects against federal energy policy requirements."""

import logging

from ..models.schemas import ComplianceResult, PolicyCheckResult
from ..models.enums import ComplianceStatus
from ..observability.tracer import traced

logger = logging.getLogger(__name__)

# Policy requirement thresholds
POLICY_REQUIREMENTS = {
    "EO_14057": {
        "description": "Executive Order 14057 — Federal Sustainability Plan",
        "checks": [
            {
                "name": "Carbon-free electricity",
                "field": "carbon_free_electric_pct",
                "threshold": 100,
                "by_year": 2030,
                "unit": "%",
            },
            {
                "name": "Net-zero emissions",
                "field": "net_zero",
                "threshold": True,
                "by_year": 2050,
            },
            {
                "name": "Energy efficiency improvement",
                "field": "energy_reduction_pct",
                "threshold": 50,
                "baseline_year": 2003,
                "unit": "%",
            },
        ],
    },
    "EISA_2007": {
        "description": "Energy Independence and Security Act of 2007",
        "checks": [
            {
                "name": "Energy reduction target",
                "field": "eui_reduction_pct",
                "threshold": 30,
                "baseline_year": 2003,
                "unit": "%",
            },
            {
                "name": "Fossil fuel reduction (new buildings)",
                "field": "fossil_fuel_reduction_pct",
                "threshold": 55,
                "unit": "%",
                "applies_to": "new_construction",
            },
        ],
    },
    "EPACT_2005": {
        "description": "Energy Policy Act of 2005",
        "checks": [
            {
                "name": "Metering requirement",
                "field": "metered",
                "threshold": True,
            },
            {
                "name": "Renewable energy",
                "field": "renewable_pct",
                "threshold": 7.5,
                "unit": "%",
            },
        ],
    },
    "ENERGY_STAR": {
        "description": "ENERGY STAR Certification",
        "checks": [
            {
                "name": "Portfolio Manager score",
                "field": "energy_star_score",
                "threshold": 75,
            },
        ],
    },
}


@traced(tool_name="check_compliance")
def check_compliance(
    facility_data: dict,
    policies: list[str],
    project_type: str = "existing_building",
) -> ComplianceResult:
    """Check project/facility compliance with federal energy policies.

    Args:
        facility_data: Dict of facility metrics (EUI, renewables %, etc.).
        policies: List of policy identifiers to check against.
        project_type: Type of project (new_construction, existing_building, etc.).

    Returns:
        ComplianceResult with per-policy status, gaps, and remediation steps.
    """
    logger.info("Checking compliance for %d policies, project_type=%s", len(policies), project_type)

    policy_results = []
    all_gaps = []
    all_remediation = []

    for policy_id in policies:
        if policy_id not in POLICY_REQUIREMENTS:
            policy_results.append(PolicyCheckResult(
                policy=policy_id,
                status=ComplianceStatus.INSUFFICIENT_DATA,
                details=f"Unknown policy: {policy_id}",
            ))
            continue

        policy_def = POLICY_REQUIREMENTS[policy_id]
        check_results = []
        policy_compliant = True
        has_data = False

        for check in policy_def["checks"]:
            # Skip checks that don't apply to this project type
            if "applies_to" in check and check["applies_to"] != project_type:
                continue

            field = check["field"]
            threshold = check["threshold"]

            if field not in facility_data:
                check_results.append(f"MISSING: {check['name']} — no data for '{field}'")
                policy_compliant = False
                continue

            has_data = True
            value = facility_data[field]

            if isinstance(threshold, bool):
                meets = bool(value) == threshold
            else:
                meets = value >= threshold

            if meets:
                check_results.append(f"PASS: {check['name']} = {value}")
            else:
                check_results.append(
                    f"FAIL: {check['name']} = {value} (required: {threshold})"
                )
                policy_compliant = False
                all_gaps.append(f"{policy_id}: {check['name']} — current {value}, required {threshold}")
                all_remediation.append(
                    f"Bring {check['name']} to {threshold}{check.get('unit', '')} "
                    f"to meet {policy_id} requirements"
                )

        if not has_data:
            status = ComplianceStatus.INSUFFICIENT_DATA
        elif policy_compliant:
            status = ComplianceStatus.COMPLIANT
        else:
            status = ComplianceStatus.NON_COMPLIANT

        policy_results.append(PolicyCheckResult(
            policy=policy_id,
            status=status,
            details=policy_def["description"],
            requirements=[c["name"] for c in policy_def["checks"]],
            findings=check_results,
        ))

    # Overall status
    statuses = [r.status for r in policy_results]
    if all(s == ComplianceStatus.COMPLIANT for s in statuses):
        overall = ComplianceStatus.COMPLIANT
    elif any(s == ComplianceStatus.NON_COMPLIANT for s in statuses):
        overall = ComplianceStatus.NON_COMPLIANT
    elif any(s == ComplianceStatus.INSUFFICIENT_DATA for s in statuses):
        overall = ComplianceStatus.INSUFFICIENT_DATA
    else:
        overall = ComplianceStatus.PARTIAL

    return ComplianceResult(
        overall_status=overall,
        policy_results=policy_results,
        gaps=all_gaps,
        remediation_steps=all_remediation,
    )
