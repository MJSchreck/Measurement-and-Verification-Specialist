"""Regression tests for tool implementations — catch behavioral changes."""

import json
import pytest
from src.mv_agent.tools.report_parser import parse_mv_report
from src.mv_agent.tools.savings_reconciler import reconcile_savings
from src.mv_agent.tools.compliance_checker import check_compliance
from src.mv_agent.tools.utility_processor import process_utility_data
from src.mv_agent.tools.contract_analyzer import analyze_contract
from src.mv_agent.agent import MVAgent
from src.mv_agent.observability.tracer import get_trace_buffer, clear_trace_buffer


class TestReportParserRegression:
    """Regression: report parser must maintain backward compatibility."""

    def test_reg_json_report_structure(self, sample_report_path):
        """REG: JSON report output must have all required fields."""
        result = parse_mv_report(sample_report_path)
        assert hasattr(result, "facility_name")
        assert hasattr(result, "ecms")
        assert hasattr(result, "total_guaranteed_kwh")
        assert hasattr(result, "total_actual_kwh")
        assert hasattr(result, "variance_pct")
        assert hasattr(result, "warnings")

    def test_reg_json_report_ecm_count(self, sample_report_path):
        """REG: Should parse all ECMs from sample report."""
        result = parse_mv_report(sample_report_path)
        assert len(result.ecms) == 3

    def test_reg_file_not_found_raises(self):
        """REG: Missing file must raise FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            parse_mv_report("/nonexistent/path/report.json")

    def test_reg_unsupported_format_raises(self, tmp_path):
        """REG: Unsupported file format must raise ValueError."""
        bad_file = tmp_path / "report.docx"
        bad_file.touch()
        with pytest.raises(ValueError, match="Unsupported"):
            parse_mv_report(str(bad_file))


class TestReconcilerRegression:
    """Regression: reconciler output schema must be stable."""

    def test_reg_output_schema(self, sample_guaranteed_savings, sample_actual_savings):
        """REG: Reconciliation output must have all required fields."""
        result = reconcile_savings(
            contract_id="REG-001",
            guaranteed_savings=sample_guaranteed_savings,
            actual_savings=sample_actual_savings,
        )
        assert hasattr(result, "reconciliation_status")
        assert hasattr(result, "total_guaranteed")
        assert hasattr(result, "total_actual")
        assert hasattr(result, "variance_pct")
        assert hasattr(result, "ecm_results")
        assert hasattr(result, "shortfall_ecms")
        assert hasattr(result, "recommended_actions")

    def test_reg_output_is_serializable(self, sample_guaranteed_savings, sample_actual_savings):
        """REG: Reconciliation result must be JSON-serializable."""
        result = reconcile_savings(
            contract_id="REG-002",
            guaranteed_savings=sample_guaranteed_savings,
            actual_savings=sample_actual_savings,
        )
        json_str = result.model_dump_json()
        parsed = json.loads(json_str)
        assert "contract_id" in parsed


class TestTracingRegression:
    """Regression: tracing must capture all tool calls."""

    def test_reg_tool_calls_traced(self, sample_guaranteed_savings, sample_actual_savings):
        """REG: Every tool call must produce a trace record."""
        clear_trace_buffer()
        reconcile_savings(
            contract_id="TRACE-001",
            guaranteed_savings=sample_guaranteed_savings,
            actual_savings=sample_actual_savings,
        )
        buffer = get_trace_buffer()
        assert len(buffer) >= 1
        trace = buffer[-1]
        assert trace.tool_name == "reconcile_savings"
        assert trace.success is True
        assert trace.latency_ms >= 0

    def test_reg_failed_tool_traced(self):
        """REG: Failed tool calls must also produce trace records."""
        clear_trace_buffer()
        try:
            parse_mv_report("/nonexistent/file.json")
        except FileNotFoundError:
            pass
        buffer = get_trace_buffer()
        assert len(buffer) >= 1
        trace = buffer[-1]
        assert trace.tool_name == "parse_mv_report"
        assert trace.success is False
        assert "not found" in trace.error.lower()


class TestAgentRegression:
    """Regression: agent orchestrator API must remain stable."""

    def test_reg_agent_lists_all_tools(self, agent):
        """REG: Agent must expose all 5 registered tools."""
        tools = agent.list_tools()
        assert len(tools) == 5
        assert "parse_mv_report" in tools
        assert "reconcile_savings" in tools
        assert "analyze_contract" in tools
        assert "check_compliance" in tools
        assert "process_utility_data" in tools

    def test_reg_agent_lists_all_prompts(self, agent):
        """REG: Agent must list all registered prompts."""
        prompts = agent.list_prompts()
        assert len(prompts) >= 8
        names = {p["name"] for p in prompts}
        assert "reconciliation.analyze" in names
        assert "compliance.assess" in names

    def test_reg_agent_unknown_tool_raises(self, agent):
        """REG: Running unknown tool must raise KeyError."""
        with pytest.raises(KeyError, match="Unknown tool"):
            agent.run_tool("nonexistent_tool")
