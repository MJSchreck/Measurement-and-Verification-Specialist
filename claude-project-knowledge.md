# Claude.ai Project Knowledge — GSA M&V Reference

> **Copy everything below the line into your Claude.ai Project Knowledge field (or upload this file directly).**

---

## GSA Energy Program Context

GSA manages ~8,700 federal buildings (~370 million SF). Energy projects are delivered through:

- **ESPC (Energy Savings Performance Contracts)** — Long-term contracts with ESCOs, savings-guaranteed
- **UESC (Utility Energy Service Contracts)** — Through local utilities
- **Direct-funded projects** — Appropriated funds for energy improvements

M&V proves the savings are real. If savings fall short, the ESCO pays the difference (in ESPC). Your M&V work protects the government.

## IPMVP Options Quick Reference

| Option | Name | Use Case | Method |
|--------|------|----------|--------|
| A | Retrofit Isolation: Key Parameter | Single ECM, one key parameter measured, others stipulated | Spot or short-term measurement |
| B | Retrofit Isolation: All Parameters | Single ECM, continuous measurement of all parameters | Continuous metering |
| C | Whole Facility | Multiple ECMs, utility meter level | Regression on whole-building data |
| D | Calibrated Simulation | Complex projects, no baseline data | Energy model calibrated to actuals |

## ASHRAE Guideline 14 Statistical Thresholds

For **monthly** data:
- CV(RMSE) ≤ 15%
- NMBE ≤ ±5%

For **hourly** data:
- CV(RMSE) ≤ 30%
- NMBE ≤ ±10%

## Common ECMs in GSA Buildings

1. **LED lighting retrofits** — Typically Option A (stipulated hours, measured wattage)
2. **HVAC upgrades** — Chillers, boilers, RTUs — Option B or C
3. **Building Automation System (BAS) upgrades** — Option C or D
4. **Variable Frequency Drives (VFDs)** — Option A or B
5. **Envelope improvements** — Windows, insulation, air sealing — Option C or D
6. **Solar PV** — Option B (metered production)
7. **Water conservation** — Low-flow fixtures, smart irrigation — Option A

## Weather Normalization

- Use **TMY3 (Typical Meteorological Year)** data for baseline normalization
- Source: NOAA / NSRDB weather stations
- Calculate **HDD** (Heating Degree Days) and **CDD** (Cooling Degree Days)
- Common base temperatures: 65°F (standard), or optimize via regression
- Three-parameter (3P) and five-parameter (5P) change-point models are standard

## Key Formulas

**Energy Savings:**
```
Savings = Baseline Adjusted Energy − Post-Installation Energy ± Non-Routine Adjustments
```

**CV(RMSE):**
```
CV(RMSE) = [√(Σ(yi − ŷi)² / (n − p))] / ȳ × 100%
```

**NMBE:**
```
NMBE = [Σ(yi − ŷi) / ((n − p) × ȳ)] × 100%
```

**EUI (Energy Use Intensity):**
```
EUI = Total Source Energy (kBtu) / Gross Floor Area (SF)
```

## GSA Deliverable Types

- **M&V Plan** — Pre-installation, defines approach per ECM
- **Baseline Report** — Documents pre-retrofit conditions and baseline model
- **Annual M&V Report** — Calculates year-over-year savings
- **Post-Installation Report** — Confirms ECMs installed as designed
- **Savings Summary** — Executive-level table of guaranteed vs. actual savings

## Federal Energy Goals (Current)

- 50% energy intensity reduction by 2032 (from 2003 baseline)
- 100% clean electricity by 2030
- Net-zero emissions federal buildings by 2045
- Annual 2.5% energy intensity reduction target
- All new construction/major renovation to net-zero by 2030

## Portfolio Manager / Benchmarking

- All GSA buildings >5,000 SF must be benchmarked in ENERGY STAR Portfolio Manager
- Track: site EUI, source EUI, ENERGY STAR score, water use
- Data sources: utility bills, interval data, building characteristics
- Target: ENERGY STAR score ≥ 75 for GSA buildings
