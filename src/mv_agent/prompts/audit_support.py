"""Prompt templates for energy audit support workflows."""

from .registry import prompt_registry

# --- Benchmarking Analysis ---
prompt_registry.register(
    name="audit.benchmark",
    version="v1",
    template="""You are an energy auditor analyzing facility benchmarking data.

## Facility: {facility_name}
## Building Type: {building_type}
## Square Footage: {sqft:,}
## Location: {location}

## Utility Data (12-month):
{utility_data}

## ENERGY STAR Score: {energy_star_score}
## National Median EUI for {building_type}: {median_eui} kBTU/sqft

## Task:
1. Calculate site EUI and source EUI
2. Compare against national median for this building type
3. Identify the top 3 energy conservation opportunities
4. Estimate potential savings (kWh/therms and cost) for each opportunity
5. Recommend appropriate IPMVP option for each ECM
6. Prioritize by simple payback period

## Output:
Structured audit findings with:
- Energy performance summary (EUI, ENERGY STAR ranking)
- ECM recommendations with estimated savings
- Implementation priority matrix
- Recommended next steps (investment-grade audit, ESPC feasibility)
""",
    description="Facility benchmarking and ECM identification",
    is_default=True,
)

# --- Utility Bill Analysis ---
prompt_registry.register(
    name="audit.utility_analysis",
    version="v1",
    template="""Analyze this facility's utility billing data and identify patterns.

## Facility: {facility_name}
## Utility Records:
{utility_records}

## Task:
1. Plot monthly consumption trend (describe in text)
2. Calculate average monthly cost and consumption
3. Identify seasonal patterns
4. Flag any billing anomalies (spikes, estimated reads, rate changes)
5. Calculate weather-normalized consumption if HDD/CDD provided
6. Estimate annual energy cost baseline

## Weather Data (if available):
{weather_data}
""",
    description="Utility billing trend analysis",
    is_default=True,
)
