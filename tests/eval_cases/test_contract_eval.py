"""Eval cases for contract analysis workflows."""

import pytest
from src.mv_agent.tools.contract_analyzer import analyze_contract
from src.mv_agent.models.enums import ContractType


class TestContractEval:
    """Evaluation suite for contract analysis accuracy."""

    SAMPLE_ESPC = """
    ENERGY SAVINGS PERFORMANCE CONTRACT
    Contract Number: ESPC-2024-001

    Performance Period of 20 years commencing from the date of acceptance.

    Annual Guaranteed Savings of $1,500,000 in energy and related costs.

    ECM 1: LED Lighting Retrofit (IPMVP Option B)
    ECM 2: HVAC System Replacement (IPMVP Option C)
    ECM 3: Building Automation System (IPMVP Option C)
    ECM 4: Solar PV Installation (IPMVP Option A)

    Escalation rate of 2.5% per year applied to guaranteed savings.

    The ESCO shall provide annual M&V reports within 90 days of each
    performance period anniversary. Termination for convenience clause
    included per FAR 52.249-2.
    """

    SAMPLE_UESC = """
    UTILITY ENERGY SERVICE CONTRACT
    Agreement Number: UESC-2024-005

    Performance Period: 15 years

    Guaranteed Annual Savings: $800,000

    ECM 1: Chiller Replacement (Option B)
    ECM 2: Lighting Controls (Option A)

    Utility rate schedule: GS-1 Commercial
    """

    def test_eval_espc_period_extraction(self):
        """EVAL: Should extract performance period from ESPC."""
        result = analyze_contract(self.SAMPLE_ESPC, "ESPC")
        assert result.performance_period_years == 20

    def test_eval_espc_savings_extraction(self):
        """EVAL: Should extract annual guaranteed savings."""
        result = analyze_contract(self.SAMPLE_ESPC, "ESPC")
        assert result.annual_guaranteed_savings == 1_500_000

    def test_eval_espc_total_savings_calculation(self):
        """EVAL: Total savings should equal annual * period."""
        result = analyze_contract(self.SAMPLE_ESPC, "ESPC")
        assert result.total_guaranteed_savings == 1_500_000 * 20

    def test_eval_espc_ipmvp_detection(self):
        """EVAL: Should detect IPMVP options mentioned in contract."""
        result = analyze_contract(
            self.SAMPLE_ESPC, "ESPC",
            analysis_focus=["mv_methodology"]
        )
        assert len(result.mv_options_used) > 0

    def test_eval_espc_risk_flags(self):
        """EVAL: Should flag escalation rate as a risk item."""
        result = analyze_contract(self.SAMPLE_ESPC, "ESPC")
        assert any("escalation" in risk.lower() for risk in result.risks)

    def test_eval_uesc_contract_type(self):
        """EVAL: Should correctly identify UESC contract type."""
        result = analyze_contract(self.SAMPLE_UESC, "UESC")
        assert result.contract_type == ContractType.UESC

    def test_eval_uesc_recommendations(self):
        """EVAL: UESC should include rate schedule alignment recommendation."""
        result = analyze_contract(self.SAMPLE_UESC, "UESC")
        assert any("rate" in rec.lower() for rec in result.recommendations)

    def test_eval_contract_with_no_termination(self):
        """EVAL: Should flag missing termination clause as risk."""
        bare_contract = "Performance Period of 10 years. Guaranteed Annual Savings of $500,000."
        result = analyze_contract(bare_contract, "ESPC")
        assert any("termination" in risk.lower() for risk in result.risks)
