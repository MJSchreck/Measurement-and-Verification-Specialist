# Eval Guide — Writing and Running Evaluations

## Philosophy

Every prompt change and tool modification must be validated by eval cases before
merging. Evals are not unit tests — they test domain correctness and expected
agent behavior under realistic conditions.

---

## Eval Types

### 1. Tool Evals (`tests/eval_cases/test_*_eval.py`)

Test that tool functions return correct domain results:

```python
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
```

**Naming convention:** `test_eval_<what_is_tested>`

### 2. Regression Tests (`tests/regression/test_*_regression.py`)

Test that existing behavior isn't broken by changes:

```python
def test_reg_output_schema(self):
    """REG: Reconciliation output must have all required fields."""
    result = reconcile_savings(...)
    assert hasattr(result, "reconciliation_status")
    assert hasattr(result, "total_guaranteed")
```

**Naming convention:** `test_reg_<what_must_not_change>`

### 3. Prompt Regression (`tests/regression/test_prompt_regression.py`)

Ensure prompts render correctly and all expected versions exist:

```python
def test_reg_reconciliation_has_v1_and_v2(self):
    """REG: reconciliation.analyze must have both v1 and v2 versions."""
    versions = prompt_registry.list_versions("reconciliation.analyze")
    version_ids = {v.version for v in versions}
    assert "v1" in version_ids
    assert "v2" in version_ids
```

---

## Running Evals

```bash
# All tests
pytest tests/ -v

# Eval cases only
pytest tests/eval_cases/ -v

# Regression tests only
pytest tests/regression/ -v

# Specific domain
pytest tests/eval_cases/test_reconciliation_eval.py -v

# With coverage
pytest tests/ -v --tb=short
```

---

## Writing New Evals

### When to write an eval:

1. You changed a prompt template → add/update eval for expected behavior
2. You added a new tool → add eval cases for all input scenarios
3. You found a bug → write an eval that reproduces it, then fix it
4. You changed domain logic → update affected evals

### Eval case structure:

```python
class TestMyDomainEval:
    """Evaluation suite for [domain area]."""

    def test_eval_happy_path(self):
        """EVAL: [what should happen in the normal case]."""
        result = my_tool(valid_input)
        assert result.status == expected_status

    def test_eval_edge_case(self):
        """EVAL: [what should happen with tricky input]."""
        result = my_tool(edge_input)
        assert result handles it correctly

    def test_eval_error_handling(self):
        """EVAL: [what should happen with bad input]."""
        with pytest.raises(ExpectedError):
            my_tool(bad_input)
```

### Rules:

1. Docstrings start with `EVAL:` or `REG:` prefix
2. One assertion per concept (but multiple asserts per test is fine)
3. Use fixtures from `conftest.py` for shared test data
4. Never mock domain logic — test the real implementation
5. Keep eval data realistic (use actual M&V terminology and values)

---

## CI Pipeline

The `.github/workflows/eval.yml` pipeline runs on every PR:

1. Install dependencies
2. Run `pytest tests/ -v`
3. Fail the PR if any test fails
4. Report results as PR comment

This ensures no prompt or tool change goes out without eval validation.
