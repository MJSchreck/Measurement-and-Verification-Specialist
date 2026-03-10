"""MCP tool implementations for M&V workflows."""

from .report_parser import parse_mv_report
from .savings_reconciler import reconcile_savings
from .contract_analyzer import analyze_contract
from .compliance_checker import check_compliance
from .utility_processor import process_utility_data

TOOL_REGISTRY = {
    "parse_mv_report": parse_mv_report,
    "reconcile_savings": reconcile_savings,
    "analyze_contract": analyze_contract,
    "check_compliance": check_compliance,
    "process_utility_data": process_utility_data,
}

__all__ = [
    "parse_mv_report",
    "reconcile_savings",
    "analyze_contract",
    "check_compliance",
    "process_utility_data",
    "TOOL_REGISTRY",
]
