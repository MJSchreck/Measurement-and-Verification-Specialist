"""Eval cases for energy audit and utility processing workflows."""

import pytest
from src.mv_agent.tools.utility_processor import process_utility_data


class TestUtilityProcessingEval:
    """Evaluation suite for utility data processing accuracy."""

    def test_eval_kwh_to_kbtu_conversion(self):
        """EVAL: 1 kWh = 3.412 kBTU conversion must be exact."""
        result = process_utility_data(
            utility_data=[{
                "period": "2025-01",
                "utility_type": "electric",
                "consumption": 100000,
                "unit": "kwh",
                "cost": 10000,
            }]
        )
        assert result.total_site_energy_kbtu == 341200.0

    def test_eval_therms_to_kbtu_conversion(self):
        """EVAL: 1 therm = 100 kBTU conversion must be exact."""
        result = process_utility_data(
            utility_data=[{
                "period": "2025-01",
                "utility_type": "natural_gas",
                "consumption": 5000,
                "unit": "therms",
                "cost": 5000,
            }]
        )
        assert result.total_site_energy_kbtu == 500000.0

    def test_eval_eui_calculation(self):
        """EVAL: EUI = total kBTU / sqft must be accurate."""
        result = process_utility_data(
            utility_data=[{
                "period": "2025-01",
                "utility_type": "electric",
                "consumption": 100000,
                "unit": "kwh",
                "cost": 10000,
            }],
            building_sqft=50000,
        )
        expected_eui = 341200.0 / 50000  # 6.824
        assert result.eui_kbtu_sqft == round(expected_eui, 2)

    def test_eval_no_sqft_no_eui(self):
        """EVAL: EUI should be None when building_sqft is not provided."""
        result = process_utility_data(
            utility_data=[{
                "period": "2025-01",
                "utility_type": "electric",
                "consumption": 100000,
                "unit": "kwh",
                "cost": 10000,
            }]
        )
        assert result.eui_kbtu_sqft is None

    def test_eval_anomaly_detection(self, sample_utility_data):
        """EVAL: Should flag consumption anomalies (z-score > 2)."""
        # Add a spike month
        data = sample_utility_data + [{
            "period": "2025-13",
            "utility_type": "electric",
            "consumption": 300000,  # Extreme spike
            "unit": "kwh",
            "cost": 30000,
        }]
        result = process_utility_data(utility_data=data)
        assert len(result.anomalies) > 0
        assert any(a["period"] == "2025-13" for a in result.anomalies)

    def test_eval_multi_utility_aggregation(self):
        """EVAL: Should correctly aggregate multiple utility types."""
        result = process_utility_data(
            utility_data=[
                {
                    "period": "2025-01",
                    "utility_type": "electric",
                    "consumption": 100000,
                    "unit": "kwh",
                    "cost": 10000,
                },
                {
                    "period": "2025-01",
                    "utility_type": "natural_gas",
                    "consumption": 2000,
                    "unit": "therms",
                    "cost": 2000,
                },
            ]
        )
        expected = (100000 * 3.412) + (2000 * 100)
        assert result.total_site_energy_kbtu == expected

    def test_eval_monthly_trend_ordering(self, sample_utility_data):
        """EVAL: Monthly trend should be in chronological order."""
        result = process_utility_data(utility_data=sample_utility_data)
        periods = [t["period"] for t in result.monthly_trend]
        assert periods == sorted(periods)

    def test_eval_empty_data_handling(self):
        """EVAL: Should handle empty utility data gracefully."""
        result = process_utility_data(utility_data=[])
        assert result.total_site_energy_kbtu == 0.0
        assert result.eui_kbtu_sqft is None
        assert len(result.anomalies) == 0
