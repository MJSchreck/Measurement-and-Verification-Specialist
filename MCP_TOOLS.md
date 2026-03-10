# MCP Tool Map — M&V Specialist

> **Model Context Protocol (MCP)** tool definitions for the M&V Specialist agent.
> Each tool below has a defined schema, required inputs, outputs, error modes,
> and tracing metadata. This is the canonical reference.

---

## Tool Index

| # | Tool Name | Module | Purpose |
|---|-----------|--------|---------|
| 1 | `parse_mv_report` | `tools/report_parser.py` | Extract structured data from M&V reports |
| 2 | `reconcile_savings` | `tools/savings_reconciler.py` | Compare guaranteed vs. actual savings |
| 3 | `analyze_contract` | `tools/contract_analyzer.py` | Review ESPC/UESC contract terms |
| 4 | `check_compliance` | `tools/compliance_checker.py` | Validate against policy requirements |
| 5 | `process_utility_data` | `tools/utility_processor.py` | Parse and normalize utility bills |

---

## Tool Schemas

### 1. `parse_mv_report`

**Purpose:** Parse an M&V report (PDF, Excel, or structured JSON) and extract
savings data, ECM details, measurement methodology, and adjustment factors.

```json
{
  "name": "parse_mv_report",
  "description": "Extract structured savings data from an M&V report file.",
  "input_schema": {
    "type": "object",
    "properties": {
      "file_path": {
        "type": "string",
        "description": "Path to the M&V report file (PDF, XLSX, or JSON)"
      },
      "report_type": {
        "type": "string",
        "enum": ["annual", "quarterly", "post_installation", "baseline"],
        "description": "Type of M&V report"
      },
      "ipmvp_option": {
        "type": "string",
        "enum": ["A", "B", "C", "D"],
        "description": "IPMVP measurement option used (if known)"
      }
    },
    "required": ["file_path"]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "ecms": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ecm_id": { "type": "string" },
            "description": { "type": "string" },
            "guaranteed_savings_kwh": { "type": "number" },
            "actual_savings_kwh": { "type": "number" },
            "guaranteed_savings_cost": { "type": "number" },
            "actual_savings_cost": { "type": "number" },
            "ipmvp_option": { "type": "string" },
            "measurement_period": { "type": "string" },
            "adjustments": { "type": "array" }
          }
        }
      },
      "total_guaranteed_kwh": { "type": "number" },
      "total_actual_kwh": { "type": "number" },
      "total_guaranteed_cost": { "type": "number" },
      "total_actual_cost": { "type": "number" },
      "variance_pct": { "type": "number" },
      "report_period": { "type": "string" },
      "facility_name": { "type": "string" },
      "warnings": { "type": "array" }
    }
  }
}
```

**Error modes:** `FileNotFoundError`, `ParseError` (unreadable format),
`SchemaValidationError` (missing required fields in report).

---

### 2. `reconcile_savings`

**Purpose:** Compare guaranteed savings from contract terms against actual
measured savings. Flag shortfalls, calculate variance, and generate
reconciliation notes.

```json
{
  "name": "reconcile_savings",
  "description": "Reconcile guaranteed vs. actual energy savings across ECMs.",
  "input_schema": {
    "type": "object",
    "properties": {
      "contract_id": {
        "type": "string",
        "description": "ESPC or UESC contract identifier"
      },
      "guaranteed_savings": {
        "type": "object",
        "description": "Guaranteed savings by ECM from contract"
      },
      "actual_savings": {
        "type": "object",
        "description": "Actual measured savings by ECM from M&V report"
      },
      "adjustment_factors": {
        "type": "object",
        "description": "Weather, occupancy, or operational adjustments"
      },
      "tolerance_pct": {
        "type": "number",
        "default": 5.0,
        "description": "Acceptable variance percentage before flagging"
      }
    },
    "required": ["contract_id", "guaranteed_savings", "actual_savings"]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "contract_id": { "type": "string" },
      "reconciliation_status": {
        "type": "string",
        "enum": ["PASS", "SHORTFALL", "EXCESS", "REVIEW_NEEDED"]
      },
      "total_guaranteed": { "type": "number" },
      "total_actual": { "type": "number" },
      "total_variance": { "type": "number" },
      "variance_pct": { "type": "number" },
      "ecm_results": { "type": "array" },
      "shortfall_ecms": { "type": "array" },
      "notes": { "type": "array" },
      "recommended_actions": { "type": "array" }
    }
  }
}
```

**Error modes:** `ContractNotFoundError`, `DataMismatchError` (ECM IDs don't
align between guaranteed and actual).

---

### 3. `analyze_contract`

**Purpose:** Extract and analyze key terms from an ESPC or UESC contract,
including performance period, savings guarantees, M&V methodology, and ESCO
obligations.

```json
{
  "name": "analyze_contract",
  "description": "Review ESPC/UESC contract terms and extract key provisions.",
  "input_schema": {
    "type": "object",
    "properties": {
      "contract_text": {
        "type": "string",
        "description": "Full contract text or relevant sections"
      },
      "contract_type": {
        "type": "string",
        "enum": ["ESPC", "UESC"],
        "description": "Type of performance contract"
      },
      "analysis_focus": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": [
            "savings_guarantees", "performance_period",
            "mv_methodology", "esco_obligations",
            "government_obligations", "termination_clauses",
            "escalation_rates", "ecm_descriptions"
          ]
        },
        "description": "Which aspects to focus analysis on"
      }
    },
    "required": ["contract_text", "contract_type"]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "contract_type": { "type": "string" },
      "performance_period_years": { "type": "number" },
      "total_guaranteed_savings": { "type": "number" },
      "annual_guaranteed_savings": { "type": "number" },
      "ecm_count": { "type": "integer" },
      "mv_options_used": { "type": "array" },
      "key_terms": { "type": "object" },
      "risks": { "type": "array" },
      "recommendations": { "type": "array" }
    }
  }
}
```

---

### 4. `check_compliance`

**Purpose:** Validate a facility or project against federal energy policy
requirements (EO 14057, EISA 2007, EPACT 2005, etc.).

```json
{
  "name": "check_compliance",
  "description": "Check project/facility compliance with federal energy policies.",
  "input_schema": {
    "type": "object",
    "properties": {
      "facility_data": {
        "type": "object",
        "description": "Facility energy data (EUI, renewables %, etc.)"
      },
      "policies": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": [
            "EO_14057", "EISA_2007", "EPACT_2005",
            "ENERGY_STAR", "ASHRAE_90_1", "10_CFR_433",
            "10_CFR_435", "GUIDING_PRINCIPLES"
          ]
        },
        "description": "Which policies to check against"
      },
      "project_type": {
        "type": "string",
        "enum": ["new_construction", "major_renovation", "existing_building", "lease"],
        "description": "Type of project or facility"
      }
    },
    "required": ["facility_data", "policies"]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "overall_status": {
        "type": "string",
        "enum": ["COMPLIANT", "NON_COMPLIANT", "PARTIAL", "INSUFFICIENT_DATA"]
      },
      "policy_results": { "type": "array" },
      "gaps": { "type": "array" },
      "remediation_steps": { "type": "array" }
    }
  }
}
```

---

### 5. `process_utility_data`

**Purpose:** Parse utility bill data, normalize units, calculate EUI, identify
anomalies, and prepare data for benchmarking.

```json
{
  "name": "process_utility_data",
  "description": "Parse and normalize utility billing data for analysis.",
  "input_schema": {
    "type": "object",
    "properties": {
      "utility_data": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "period": { "type": "string" },
            "utility_type": {
              "type": "string",
              "enum": ["electric", "natural_gas", "steam", "chilled_water", "fuel_oil", "propane"]
            },
            "consumption": { "type": "number" },
            "unit": { "type": "string" },
            "cost": { "type": "number" },
            "demand_kw": { "type": "number" }
          }
        }
      },
      "building_sqft": {
        "type": "number",
        "description": "Gross square footage for EUI calculation"
      },
      "weather_data": {
        "type": "object",
        "description": "HDD/CDD data for weather normalization"
      }
    },
    "required": ["utility_data"]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "normalized_consumption": { "type": "array" },
      "total_site_energy_kbtu": { "type": "number" },
      "eui_kbtu_sqft": { "type": "number" },
      "cost_per_sqft": { "type": "number" },
      "anomalies": { "type": "array" },
      "monthly_trend": { "type": "array" },
      "weather_adjusted": { "type": "boolean" }
    }
  }
}
```

---

## Adding New Tools

1. Create a new module in `src/mv_agent/tools/`
2. Define the function with type hints and the `@traced` decorator
3. Add input/output Pydantic models in `src/mv_agent/models/schemas.py`
4. Register the tool in `src/mv_agent/tools/__init__.py`
5. Add the schema to this file (MCP_TOOLS.md)
6. Write eval cases in `tests/eval_cases/`
7. Run `pytest tests/ -v` to validate

---

## Tracing Metadata

Every tool call automatically captures:

| Field | Type | Description |
|-------|------|-------------|
| `trace_id` | UUID | Unique trace identifier |
| `tool_name` | str | Which tool was called |
| `input_hash` | str | SHA-256 of serialized input |
| `output_hash` | str | SHA-256 of serialized output |
| `prompt_version` | str | Which prompt version triggered this call |
| `model` | str | LLM model used |
| `input_tokens` | int | Prompt tokens consumed |
| `output_tokens` | int | Completion tokens generated |
| `cost_usd` | float | Estimated cost |
| `latency_ms` | int | Wall-clock execution time |
| `success` | bool | Whether the call completed without error |
| `error` | str | Error message if failed |
| `timestamp` | datetime | When the call occurred |
