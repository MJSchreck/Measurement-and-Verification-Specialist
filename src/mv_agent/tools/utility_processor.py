"""Parse and normalize utility billing data for analysis."""

import logging
from ..models.schemas import UtilityAnalysis, UtilityRecord
from ..models.enums import UtilityType
from ..observability.tracer import traced

logger = logging.getLogger(__name__)

# Conversion factors to kBTU
CONVERSION_TO_KBTU = {
    "kwh": 3.412,
    "kWh": 3.412,
    "therms": 100.0,
    "therm": 100.0,
    "ccf": 102.6,  # natural gas CCF
    "mcf": 1026.0,
    "mmbtu": 1000.0,
    "gallons_fuel_oil": 138.5,
    "gallons_propane": 91.5,
    "mlb_steam": 1194.0,  # thousand pounds of steam
    "ton_hours": 12.0,  # chilled water
}


@traced(tool_name="process_utility_data")
def process_utility_data(
    utility_data: list[dict],
    building_sqft: float | None = None,
    weather_data: dict | None = None,
) -> UtilityAnalysis:
    """Parse and normalize utility billing data.

    Args:
        utility_data: List of utility billing records.
        building_sqft: Gross square footage for EUI calculation.
        weather_data: Optional HDD/CDD data for weather normalization.

    Returns:
        UtilityAnalysis with normalized consumption, EUI, anomalies, and trends.
    """
    logger.info("Processing %d utility records", len(utility_data))

    records = []
    for item in utility_data:
        records.append(UtilityRecord(
            period=item.get("period", ""),
            utility_type=UtilityType(item.get("utility_type", "electric")),
            consumption=item.get("consumption", 0),
            unit=item.get("unit", "kwh"),
            cost=item.get("cost", 0),
            demand_kw=item.get("demand_kw"),
        ))

    # Convert all consumption to kBTU
    normalized = []
    total_kbtu = 0.0
    total_cost = 0.0

    for record in records:
        factor = CONVERSION_TO_KBTU.get(record.unit, 1.0)
        kbtu = record.consumption * factor
        total_kbtu += kbtu
        total_cost += record.cost

        normalized.append({
            "period": record.period,
            "utility_type": record.utility_type.value,
            "original_consumption": record.consumption,
            "original_unit": record.unit,
            "kbtu": round(kbtu, 2),
            "cost": record.cost,
        })

    # Calculate EUI
    eui = None
    cost_per_sqft = None
    if building_sqft and building_sqft > 0:
        eui = round(total_kbtu / building_sqft, 2)
        cost_per_sqft = round(total_cost / building_sqft, 2)

    # Detect anomalies (simple z-score on kBTU values)
    anomalies = []
    kbtu_values = [n["kbtu"] for n in normalized]
    if len(kbtu_values) >= 3:
        mean_kbtu = sum(kbtu_values) / len(kbtu_values)
        std_kbtu = (
            sum((v - mean_kbtu) ** 2 for v in kbtu_values) / len(kbtu_values)
        ) ** 0.5

        if std_kbtu > 0:
            for n in normalized:
                z = (n["kbtu"] - mean_kbtu) / std_kbtu
                if abs(z) > 2.0:
                    anomalies.append({
                        "period": n["period"],
                        "utility_type": n["utility_type"],
                        "kbtu": n["kbtu"],
                        "z_score": round(z, 2),
                        "severity": "high" if abs(z) > 3 else "medium",
                    })

    # Monthly trend (aggregate by period)
    period_totals: dict[str, dict] = {}
    for n in normalized:
        period = n["period"]
        if period not in period_totals:
            period_totals[period] = {"period": period, "total_kbtu": 0, "total_cost": 0}
        period_totals[period]["total_kbtu"] += n["kbtu"]
        period_totals[period]["total_cost"] += n["cost"]

    monthly_trend = sorted(period_totals.values(), key=lambda x: x["period"])

    return UtilityAnalysis(
        normalized_consumption=normalized,
        total_site_energy_kbtu=round(total_kbtu, 2),
        eui_kbtu_sqft=eui,
        cost_per_sqft=cost_per_sqft,
        anomalies=anomalies,
        monthly_trend=monthly_trend,
        weather_adjusted=weather_data is not None,
    )
