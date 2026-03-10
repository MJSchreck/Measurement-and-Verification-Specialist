"""Reconcile guaranteed vs. actual energy savings across ECMs."""

import logging

from ..models.schemas import ReconciliationResult, ECMResult
from ..models.enums import ReconciliationStatus
from ..observability.tracer import traced

logger = logging.getLogger(__name__)


@traced(tool_name="reconcile_savings")
def reconcile_savings(
    contract_id: str,
    guaranteed_savings: dict[str, float],
    actual_savings: dict[str, float],
    adjustment_factors: dict[str, float] | None = None,
    tolerance_pct: float = 5.0,
) -> ReconciliationResult:
    """Reconcile guaranteed vs. actual energy savings.

    Args:
        contract_id: ESPC or UESC contract identifier.
        guaranteed_savings: Dict mapping ECM IDs to guaranteed savings (kWh).
        actual_savings: Dict mapping ECM IDs to actual measured savings (kWh).
        adjustment_factors: Optional weather/occupancy adjustments by ECM.
        tolerance_pct: Acceptable variance percentage before flagging.

    Returns:
        ReconciliationResult with status, variances, and recommended actions.
    """
    adjustment_factors = adjustment_factors or {}
    ecm_results = []
    shortfall_ecms = []
    notes = []

    all_ecm_ids = set(guaranteed_savings.keys()) | set(actual_savings.keys())

    for ecm_id in sorted(all_ecm_ids):
        guaranteed = guaranteed_savings.get(ecm_id, 0.0)
        actual = actual_savings.get(ecm_id, 0.0)

        # Apply adjustment factor if available
        adj_factor = adjustment_factors.get(ecm_id, 1.0)
        adjusted_actual = actual * adj_factor

        ecm = ECMResult(
            ecm_id=ecm_id,
            guaranteed_savings_kwh=guaranteed,
            actual_savings_kwh=adjusted_actual,
        )
        ecm.compute_variance()
        ecm_results.append(ecm)

        if ecm_id not in guaranteed_savings:
            notes.append(f"ECM {ecm_id}: found in actuals but not in contract guarantees")
        elif ecm_id not in actual_savings:
            notes.append(f"ECM {ecm_id}: guaranteed but no actual measurement reported")
            shortfall_ecms.append(ecm_id)
        elif ecm.variance_pct < -tolerance_pct:
            shortfall_ecms.append(ecm_id)
            notes.append(
                f"ECM {ecm_id}: shortfall of {abs(ecm.variance_pct):.1f}% "
                f"(guaranteed={guaranteed:,.0f} kWh, actual={adjusted_actual:,.0f} kWh)"
            )

        if adj_factor != 1.0:
            notes.append(
                f"ECM {ecm_id}: adjustment factor {adj_factor:.3f} applied "
                f"(raw actual={actual:,.0f}, adjusted={adjusted_actual:,.0f})"
            )

    total_guaranteed = sum(guaranteed_savings.values())
    total_actual = sum(
        actual_savings.get(eid, 0.0) * adjustment_factors.get(eid, 1.0)
        for eid in guaranteed_savings
    )
    total_variance = total_actual - total_guaranteed
    variance_pct = (total_variance / total_guaranteed * 100) if total_guaranteed else 0

    # Determine status
    if not shortfall_ecms and abs(variance_pct) <= tolerance_pct:
        status = ReconciliationStatus.PASS
    elif variance_pct < -tolerance_pct:
        status = ReconciliationStatus.SHORTFALL
    elif variance_pct > tolerance_pct:
        status = ReconciliationStatus.EXCESS
    else:
        status = ReconciliationStatus.REVIEW_NEEDED

    # Build recommended actions
    actions = []
    if status == ReconciliationStatus.SHORTFALL:
        actions.append(
            f"Overall shortfall of {abs(variance_pct):.1f}%. "
            "Review ESCO obligations per contract Section H."
        )
        for ecm_id in shortfall_ecms:
            actions.append(f"Investigate ECM {ecm_id} — request ESCO root cause analysis.")
    elif status == ReconciliationStatus.REVIEW_NEEDED:
        actions.append("Some ECMs have individual shortfalls. Review per-ECM details.")
    elif status == ReconciliationStatus.EXCESS:
        actions.append(
            f"Savings exceed guarantee by {variance_pct:.1f}%. "
            "Document for annual report and portfolio briefing."
        )

    logger.info(
        "Reconciliation for %s: status=%s, variance=%.1f%%",
        contract_id, status.value, variance_pct
    )

    return ReconciliationResult(
        contract_id=contract_id,
        reconciliation_status=status,
        total_guaranteed=total_guaranteed,
        total_actual=total_actual,
        total_variance=total_variance,
        variance_pct=variance_pct,
        ecm_results=ecm_results,
        shortfall_ecms=shortfall_ecms,
        notes=notes,
        recommended_actions=actions,
    )
