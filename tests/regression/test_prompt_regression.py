"""Regression tests for prompt templates — catch drift and breakage."""

import pytest
from src.mv_agent.prompts.registry import PromptRegistry, prompt_registry


class TestPromptRegistryRegression:
    """Ensure prompt registry behavior remains stable."""

    def test_reg_all_prompts_registered(self):
        """REG: All expected prompts must be registered at startup."""
        expected = [
            "reconciliation.analyze",
            "reconciliation.summary",
            "contract.analyze",
            "contract.compare",
            "audit.benchmark",
            "audit.utility_analysis",
            "compliance.assess",
            "compliance.memo",
        ]
        registered = prompt_registry.list_prompts()
        for name in expected:
            assert name in registered, f"Prompt '{name}' not registered"

    def test_reg_all_prompts_have_defaults(self):
        """REG: Every prompt must have a default version set."""
        for name in prompt_registry.list_prompts():
            prompt = prompt_registry.get(name)
            assert prompt is not None, f"No default for prompt '{name}'"
            assert prompt.is_default, f"Default flag not set for {name}"

    def test_reg_reconciliation_has_v1_and_v2(self):
        """REG: reconciliation.analyze must have both v1 and v2 versions."""
        versions = prompt_registry.list_versions("reconciliation.analyze")
        version_ids = {v.version for v in versions}
        assert "v1" in version_ids
        assert "v2" in version_ids

    def test_reg_prompt_render_no_missing_vars(self):
        """REG: All prompts should render without KeyError when given valid vars."""
        test_vars = {
            "contract_id": "TEST-001",
            "guaranteed_savings": "ECM-001: 100,000 kWh",
            "actual_savings": "ECM-001: 95,000 kWh",
            "tolerance_pct": "5",
            "reconciliation_result": "PASS — all ECMs within tolerance",
            "contract_text": "Sample contract text",
            "contract_type": "ESPC",
            "analysis_focus": "savings_guarantees, performance_period",
            "contract_a": "Contract A text",
            "contract_b": "Contract B text",
            "facility_name": "Building 101",
            "building_type": "Office",
            "sqft": 50000,
            "location": "Washington, DC",
            "utility_data": "Electric: 100,000 kWh/yr",
            "energy_star_score": 75,
            "median_eui": 80,
            "utility_records": "Jan: 85,000 kWh",
            "weather_data": "HDD: 4500, CDD: 1200",
            "facility_data": "EUI: 65 kBTU/sqft",
            "policies": "EO 14057, EISA 2007",
            "project_type": "existing_building",
            "compliance_results": "COMPLIANT — all checks passed",
            # v2 reconciliation extra vars
            "performance_year": "3",
            "adjustments": "Weather: 1.05x",
            "historical_context": "Year 1: PASS, Year 2: PASS",
        }

        for name in prompt_registry.list_prompts():
            versions = prompt_registry.list_versions(name)
            for pv in versions:
                try:
                    rendered = pv.render(**test_vars)
                    assert len(rendered) > 50, f"{name}@{pv.version} rendered too short"
                except KeyError as e:
                    pytest.fail(f"Prompt {name}@{pv.version} missing var: {e}")

    def test_reg_prompt_versions_are_immutable(self):
        """REG: Once registered, a prompt version's template should not change."""
        registry = PromptRegistry()
        registry.register("test_immutable", "v1", template="original {var}")
        original = registry.get("test_immutable", "v1").template

        # Register v2 — v1 should remain unchanged
        registry.register("test_immutable", "v2", template="updated {var}", is_default=True)
        assert registry.get("test_immutable", "v1").template == original
