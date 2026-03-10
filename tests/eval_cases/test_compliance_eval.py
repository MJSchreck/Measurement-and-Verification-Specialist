"""Eval cases for policy compliance check workflows."""

import pytest
from src.mv_agent.tools.compliance_checker import check_compliance
from src.mv_agent.models.enums import ComplianceStatus


class TestComplianceEval:
    """Evaluation suite for compliance checking accuracy."""

    def test_eval_full_compliance(self):
        """EVAL: Fully compliant facility should get COMPLIANT status."""
        facility = {
            "carbon_free_electric_pct": 100,
            "net_zero": True,
            "energy_reduction_pct": 55,
            "eui_reduction_pct": 35,
            "metered": True,
            "renewable_pct": 10.0,
            "energy_star_score": 80,
        }
        result = check_compliance(
            facility_data=facility,
            policies=["EO_14057", "EISA_2007", "EPACT_2005", "ENERGY_STAR"],
        )
        assert result.overall_status == ComplianceStatus.COMPLIANT
        assert len(result.gaps) == 0

    def test_eval_eo14057_non_compliant(self):
        """EVAL: Facility below EO 14057 thresholds should be NON_COMPLIANT."""
        facility = {
            "carbon_free_electric_pct": 45,
            "energy_reduction_pct": 30,
        }
        result = check_compliance(
            facility_data=facility,
            policies=["EO_14057"],
        )
        assert result.overall_status == ComplianceStatus.NON_COMPLIANT
        assert len(result.gaps) > 0

    def test_eval_missing_data_status(self):
        """EVAL: Missing facility data should return INSUFFICIENT_DATA."""
        result = check_compliance(
            facility_data={},
            policies=["ENERGY_STAR"],
        )
        assert result.overall_status == ComplianceStatus.INSUFFICIENT_DATA

    def test_eval_gap_remediation_steps(self, sample_facility_data):
        """EVAL: Non-compliant items must have remediation steps."""
        # This facility has energy_star_score=72, below the 75 threshold
        result = check_compliance(
            facility_data=sample_facility_data,
            policies=["ENERGY_STAR"],
        )
        if result.overall_status == ComplianceStatus.NON_COMPLIANT:
            assert len(result.remediation_steps) > 0

    def test_eval_multiple_policy_check(self, sample_facility_data):
        """EVAL: Should check all requested policies independently."""
        result = check_compliance(
            facility_data=sample_facility_data,
            policies=["EO_14057", "EISA_2007", "EPACT_2005", "ENERGY_STAR"],
        )
        assert len(result.policy_results) == 4
        policy_names = [r.policy for r in result.policy_results]
        assert "EO_14057" in policy_names
        assert "EISA_2007" in policy_names

    def test_eval_unknown_policy_handling(self):
        """EVAL: Unknown policy should be flagged as INSUFFICIENT_DATA."""
        result = check_compliance(
            facility_data={"metered": True},
            policies=["NONEXISTENT_POLICY_42"],
        )
        assert any(
            r.policy == "NONEXISTENT_POLICY_42" and r.status == ComplianceStatus.INSUFFICIENT_DATA
            for r in result.policy_results
        )

    def test_eval_epact_metering_compliant(self):
        """EVAL: Metered facility should pass EPACT metering requirement."""
        result = check_compliance(
            facility_data={"metered": True, "renewable_pct": 8.0},
            policies=["EPACT_2005"],
        )
        epact_result = next(r for r in result.policy_results if r.policy == "EPACT_2005")
        assert epact_result.status == ComplianceStatus.COMPLIANT

    def test_eval_partial_compliance(self):
        """EVAL: Mix of compliant and non-compliant policies should be NON_COMPLIANT overall."""
        facility = {
            "metered": True,
            "renewable_pct": 8.0,
            "energy_star_score": 50,  # Below 75 threshold
        }
        result = check_compliance(
            facility_data=facility,
            policies=["EPACT_2005", "ENERGY_STAR"],
        )
        # EPACT should pass, ENERGY_STAR should fail
        assert result.overall_status == ComplianceStatus.NON_COMPLIANT
