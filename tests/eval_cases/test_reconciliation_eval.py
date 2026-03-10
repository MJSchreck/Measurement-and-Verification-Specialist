"""Eval cases for M&V reconciliation workflows."""

import pytest
from src.mv_agent.tools.savings_reconciler import reconcile_savings
from src.mv_agent.models.enums import ReconciliationStatus


class TestReconciliationEval:
    """Evaluation suite for savings reconciliation accuracy and behavior."""

    def test_eval_pass_within_tolerance(self):
        """EVAL: Reconciliation should PASS when all ECMs are within tolerance."""
        result = reconcile_savings(
            contract_id="EVAL-PASS-001",
            guaranteed_savings={"ECM-001": 100000, "ECM-002": 50000},
            actual_savings={"ECM-001": 101000, "ECM-002": 49500},
            tolerance_pct=5.0,
        )
        assert result.reconciliation_status == ReconciliationStatus.PASS
        assert abs(result.variance_pct) <= 5.0
        assert len(result.shortfall_ecms) == 0

    def test_eval_shortfall_detection(self):
        """EVAL: Should detect shortfall when actual < guaranteed beyond tolerance."""
        result = reconcile_savings(
            contract_id="EVAL-SHORT-001",
            guaranteed_savings={"ECM-001": 100000, "ECM-002": 100000},
            actual_savings={"ECM-001": 100000, "ECM-002": 80000},
            tolerance_pct=5.0,
        )
        assert result.reconciliation_status == ReconciliationStatus.SHORTFALL
        assert "ECM-002" in result.shortfall_ecms
        assert result.variance_pct < -5.0

    def test_eval_excess_savings(self):
        """EVAL: Should report EXCESS when actual significantly exceeds guaranteed."""
        result = reconcile_savings(
            contract_id="EVAL-EXCESS-001",
            guaranteed_savings={"ECM-001": 100000},
            actual_savings={"ECM-001": 120000},
            tolerance_pct=5.0,
        )
        assert result.reconciliation_status == ReconciliationStatus.EXCESS
        assert result.variance_pct > 5.0

    def test_eval_adjustment_factors_applied(self):
        """EVAL: Adjustment factors should modify actual savings correctly."""
        result = reconcile_savings(
            contract_id="EVAL-ADJ-001",
            guaranteed_savings={"ECM-001": 100000},
            actual_savings={"ECM-001": 90000},
            adjustment_factors={"ECM-001": 1.15},  # Weather adjustment
            tolerance_pct=5.0,
        )
        # 90000 * 1.15 = 103500 → within tolerance of 100000
        assert result.reconciliation_status == ReconciliationStatus.PASS
        assert any("adjustment factor" in note.lower() for note in result.notes)

    def test_eval_mismatched_ecms(self):
        """EVAL: Should handle ECM IDs that don't align between guaranteed and actual."""
        result = reconcile_savings(
            contract_id="EVAL-MISMATCH-001",
            guaranteed_savings={"ECM-001": 100000, "ECM-002": 50000},
            actual_savings={"ECM-001": 100000, "ECM-003": 30000},
        )
        # ECM-002 is in guaranteed but not actual → shortfall
        assert "ECM-002" in result.shortfall_ecms
        assert any("ECM-003" in note for note in result.notes)

    def test_eval_zero_guaranteed_no_division_error(self):
        """EVAL: Should handle zero guaranteed savings without division errors."""
        result = reconcile_savings(
            contract_id="EVAL-ZERO-001",
            guaranteed_savings={"ECM-001": 0},
            actual_savings={"ECM-001": 5000},
        )
        assert result is not None
        assert result.variance_pct == 0  # Can't compute variance with 0 base

    def test_eval_recommended_actions_on_shortfall(self):
        """EVAL: Shortfall results must include recommended actions."""
        result = reconcile_savings(
            contract_id="EVAL-ACTIONS-001",
            guaranteed_savings={"ECM-001": 100000},
            actual_savings={"ECM-001": 70000},
            tolerance_pct=5.0,
        )
        assert result.reconciliation_status == ReconciliationStatus.SHORTFALL
        assert len(result.recommended_actions) > 0
        assert any("ESCO" in action for action in result.recommended_actions)

    def test_eval_multiple_ecm_mixed_results(self):
        """EVAL: Handle portfolio with mix of passing and failing ECMs."""
        result = reconcile_savings(
            contract_id="EVAL-MIXED-001",
            guaranteed_savings={
                "ECM-001": 500000,  # Lighting — will pass
                "ECM-002": 300000,  # HVAC — will shortfall
                "ECM-003": 200000,  # Envelope — will pass
            },
            actual_savings={
                "ECM-001": 520000,
                "ECM-002": 200000,  # 33% shortfall
                "ECM-003": 210000,
            },
            tolerance_pct=5.0,
        )
        assert "ECM-002" in result.shortfall_ecms
        assert "ECM-001" not in result.shortfall_ecms
        assert "ECM-003" not in result.shortfall_ecms
        assert len(result.ecm_results) == 3
