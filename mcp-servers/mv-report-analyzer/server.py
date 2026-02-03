#!/usr/bin/env python3
"""
M&V Report Analyzer MCP Server
==============================
FastMCP server for analyzing Measurement & Verification reports.

Provides tools for:
- Parsing M&V reports (text and PDF)
- Extracting savings data and variances
- Identifying performance issues
- Generating summaries for payment authorization

Author: GSA Zone C M&V Specialist Tools
"""

import re
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, asdict

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("Error: mcp package not installed. Run: pip install mcp")
    raise

# Initialize FastMCP server
mcp = FastMCP("M&V Report Analyzer")

# Base path for knowledge base
KNOWLEDGE_BASE = Path(__file__).parent.parent.parent / "knowledge-base"
MV_REPORTS_DIR = KNOWLEDGE_BASE / "m-v-reports"
CONTRACTS_DIR = KNOWLEDGE_BASE / "contracts"


@dataclass
class MVReportData:
    """Structured data extracted from an M&V report."""
    contract_id: Optional[str] = None
    contract_name: Optional[str] = None
    performance_period_start: Optional[str] = None
    performance_period_end: Optional[str] = None
    guaranteed_savings: Optional[float] = None
    verified_savings: Optional[float] = None
    variance_amount: Optional[float] = None
    variance_percent: Optional[float] = None
    baseline_adjustments: List[dict] = None
    ecm_summary: List[dict] = None
    source_file: Optional[str] = None
    parse_date: Optional[str] = None
    parse_warnings: List[str] = None
    performance_status: Optional[str] = None

    def __post_init__(self):
        if self.baseline_adjustments is None:
            self.baseline_adjustments = []
        if self.ecm_summary is None:
            self.ecm_summary = []
        if self.parse_warnings is None:
            self.parse_warnings = []

    def calculate_variance(self):
        """Calculate variance if both savings values are present."""
        if self.guaranteed_savings and self.verified_savings:
            self.variance_amount = self.verified_savings - self.guaranteed_savings
            if self.guaranteed_savings != 0:
                self.variance_percent = (self.variance_amount / self.guaranteed_savings) * 100
                # Determine performance status
                if self.variance_percent >= 0:
                    self.performance_status = "SURPLUS"
                elif self.variance_percent >= -3:
                    self.performance_status = "ACCEPTABLE"
                elif self.variance_percent >= -5:
                    self.performance_status = "WATCH_LIST"
                else:
                    self.performance_status = "SHORTFALL"

    def to_dict(self) -> dict:
        return asdict(self)


class MVReportParser:
    """Parser for M&V reports in text format."""

    CONTRACT_ID_PATTERNS = [
        r'Contract\s*(?:No\.?|Number|#|ID)?[:\s]+([A-Z0-9\-]+)',
        r'Task\s*Order[:\s]+([A-Z0-9\-]+)',
        r'TO[:\s]+([A-Z0-9\-]+)',
        r'ESPC[:\s]+([A-Z0-9\-]+)',
        r'UESC[:\s]+([A-Z0-9\-]+)',
        r'GS-\d{2}[A-Z]-\d+[A-Z]?',
        r'47P[A-Z0-9]+',
    ]

    PERIOD_PATTERNS = [
        r'Performance\s+Period[:\s]+(\w+\s+\d{1,2},?\s+\d{4})\s*(?:to|through|-)\s*(\w+\s+\d{1,2},?\s+\d{4})',
        r'Period[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})\s*(?:to|through|-)\s*(\d{1,2}/\d{1,2}/\d{2,4})',
        r'(?:FY|Fiscal\s+Year)\s*(\d{4})',
        r'Year\s+(\d+)\s+of\s+(\d+)',
        r'Q(\d)\s+(\d{4})',
    ]

    SAVINGS_PATTERNS = {
        'guaranteed': [
            r'Guaranteed\s+Savings[:\s]*\$?([\d,]+(?:\.\d{2})?)',
            r'Annual\s+Guaranteed[:\s]*\$?([\d,]+(?:\.\d{2})?)',
            r'Contractual\s+Savings[:\s]*\$?([\d,]+(?:\.\d{2})?)',
        ],
        'verified': [
            r'Verified\s+Savings[:\s]*\$?([\d,]+(?:\.\d{2})?)',
            r'Actual\s+Savings[:\s]*\$?([\d,]+(?:\.\d{2})?)',
            r'Measured\s+Savings[:\s]*\$?([\d,]+(?:\.\d{2})?)',
            r'Achieved\s+Savings[:\s]*\$?([\d,]+(?:\.\d{2})?)',
        ]
    }

    BASELINE_PATTERNS = [
        r'Weather\s+(?:Normalization\s+)?Adjustment[:\s]*\$?([\d,]+(?:\.\d{2})?)',
        r'Occupancy\s+Adjustment[:\s]*-?\$?([\d,]+(?:\.\d{2})?)',
        r'Rate\s+Adjustment[:\s]*\$?([\d,]+(?:\.\d{2})?)',
        r'Net\s+Baseline\s+Adjustment[:\s]*\$?([\d,]+(?:\.\d{2})?)',
    ]

    ECM_PATTERN = r'ECM[-\s]*(\d+)[:\s]*([^\n]+?)(?:\n|$).*?Guaranteed[:\s]*\$?([\d,]+).*?Verified[:\s]*\$?([\d,]+)'

    def parse_currency(self, value: str) -> Optional[float]:
        if not value:
            return None
        try:
            cleaned = re.sub(r'[$,]', '', value.strip())
            return float(cleaned)
        except ValueError:
            return None

    def extract_contract_id(self, text: str) -> Optional[str]:
        for pattern in self.CONTRACT_ID_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1) if match.lastindex else match.group(0)
        return None

    def extract_performance_period(self, text: str) -> tuple:
        for pattern in self.PERIOD_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                if match.lastindex == 2:
                    return match.group(1), match.group(2)
                elif match.lastindex == 1:
                    return match.group(1), None
        return None, None

    def extract_savings(self, text: str, savings_type: str) -> Optional[float]:
        patterns = self.SAVINGS_PATTERNS.get(savings_type, [])
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return self.parse_currency(match.group(1))
        return None

    def extract_baseline_adjustments(self, text: str) -> List[dict]:
        adjustments = []
        adjustment_types = ['Weather Normalization', 'Occupancy', 'Rate', 'Net Baseline']
        for i, pattern in enumerate(self.BASELINE_PATTERNS):
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                amount = self.parse_currency(match.group(1))
                if amount:
                    adjustments.append({
                        'description': adjustment_types[i],
                        'amount': amount
                    })
        return adjustments

    def extract_contract_name(self, text: str) -> Optional[str]:
        patterns = [
            r'Project\s*(?:Name)?[:\s]+([^\n]+)',
            r'Building[:\s]+([^\n]+)',
            r'Facility[:\s]+([^\n]+)',
            r'Site[:\s]+([^\n]+)',
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return None

    def extract_ecm_summary(self, text: str) -> List[dict]:
        """Extract individual ECM performance data."""
        ecms = []
        # Look for ECM sections
        ecm_blocks = re.findall(
            r'ECM[-\s]*(\d+)[:\s]*([^\n]+).*?Guaranteed[:\s]*\$?([\d,]+(?:\.\d{2})?).*?Verified[:\s]*\$?([\d,]+(?:\.\d{2})?)',
            text, re.IGNORECASE | re.DOTALL
        )
        for block in ecm_blocks:
            guaranteed = self.parse_currency(block[2])
            verified = self.parse_currency(block[3])
            variance = (verified - guaranteed) if guaranteed and verified else None
            ecms.append({
                'ecm_number': block[0],
                'description': block[1].strip(),
                'guaranteed': guaranteed,
                'verified': verified,
                'variance': variance
            })
        return ecms

    def parse_text(self, text: str, source_file: str = None) -> MVReportData:
        data = MVReportData()
        data.source_file = source_file
        data.parse_date = datetime.now().isoformat()

        data.contract_id = self.extract_contract_id(text)
        data.contract_name = self.extract_contract_name(text)

        start, end = self.extract_performance_period(text)
        data.performance_period_start = start
        data.performance_period_end = end

        data.guaranteed_savings = self.extract_savings(text, 'guaranteed')
        data.verified_savings = self.extract_savings(text, 'verified')
        data.baseline_adjustments = self.extract_baseline_adjustments(text)
        data.ecm_summary = self.extract_ecm_summary(text)

        data.calculate_variance()

        if not data.contract_id:
            data.parse_warnings.append("Contract ID not found")
        if not data.guaranteed_savings:
            data.parse_warnings.append("Guaranteed savings not found")
        if not data.verified_savings:
            data.parse_warnings.append("Verified savings not found")

        return data


# Global parser instance
parser = MVReportParser()


@mcp.tool()
def parse_mv_report(report_text: str, source_name: str = "direct_input") -> Dict[str, Any]:
    """
    Parse an M&V report and extract key data.

    Args:
        report_text: The full text content of the M&V report
        source_name: Optional name/identifier for the report source

    Returns:
        Extracted data including contract ID, savings, variance, and status
    """
    data = parser.parse_text(report_text, source_file=source_name)
    return data.to_dict()


@mcp.tool()
def analyze_mv_file(file_path: str) -> Dict[str, Any]:
    """
    Analyze an M&V report file from the knowledge base.

    Args:
        file_path: Path to the M&V report file (relative to knowledge-base/m-v-reports/)

    Returns:
        Extracted data including contract ID, savings, variance, and analysis
    """
    # Try multiple paths
    full_path = Path(file_path)
    if not full_path.exists():
        full_path = MV_REPORTS_DIR / file_path
    if not full_path.exists():
        full_path = KNOWLEDGE_BASE / file_path

    if not full_path.exists():
        return {"error": f"File not found: {file_path}"}

    try:
        text = full_path.read_text(encoding='utf-8', errors='replace')
        data = parser.parse_text(text, source_file=str(full_path))
        return data.to_dict()
    except Exception as e:
        return {"error": f"Failed to parse file: {str(e)}"}


@mcp.tool()
def check_performance_status(
    guaranteed_savings: float,
    verified_savings: float,
    contract_id: str = "Unknown"
) -> Dict[str, Any]:
    """
    Quick check of M&V performance status.

    Args:
        guaranteed_savings: Contractual guaranteed savings amount ($)
        verified_savings: Actual verified savings from M&V ($)
        contract_id: Contract identifier for reference

    Returns:
        Performance status, variance details, and recommended actions
    """
    if guaranteed_savings <= 0:
        return {"error": "Guaranteed savings must be positive"}

    variance_amount = verified_savings - guaranteed_savings
    variance_percent = (variance_amount / guaranteed_savings) * 100

    # Determine status
    if variance_percent >= 0:
        status = "SURPLUS"
        action = "No action required. Contractor exceeding guarantee."
    elif variance_percent >= -3:
        status = "ACCEPTABLE"
        action = "Performance within acceptable range. Continue monitoring."
    elif variance_percent >= -5:
        status = "WATCH_LIST"
        action = "Add to watch list. Request contractor remediation plan."
    else:
        status = "SHORTFALL"
        action = "CRITICAL: Calculate shortfall payment per contract terms. Notify CO."

    return {
        "contract_id": contract_id,
        "guaranteed_savings": guaranteed_savings,
        "verified_savings": verified_savings,
        "variance_amount": variance_amount,
        "variance_percent": round(variance_percent, 2),
        "performance_status": status,
        "recommended_action": action,
        "payment_adjustment_required": status == "SHORTFALL",
        "analysis_date": datetime.now().isoformat()
    }


@mcp.tool()
def list_mv_reports() -> Dict[str, Any]:
    """
    List all M&V reports in the knowledge base.

    Returns:
        List of available M&V report files
    """
    if not MV_REPORTS_DIR.exists():
        return {"reports": [], "message": "M&V reports directory not found"}

    reports = []
    for ext in ['*.txt', '*.md', '*.pdf']:
        for file_path in MV_REPORTS_DIR.glob(ext):
            reports.append({
                "filename": file_path.name,
                "path": str(file_path.relative_to(KNOWLEDGE_BASE)),
                "size_kb": round(file_path.stat().st_size / 1024, 2),
                "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
            })

    return {
        "reports": reports,
        "total_count": len(reports),
        "directory": str(MV_REPORTS_DIR)
    }


@mcp.tool()
def generate_mv_summary(
    contract_id: str,
    performance_period: str,
    guaranteed_savings: float,
    verified_savings: float,
    baseline_adjustments: str = "",
    ecm_notes: str = ""
) -> Dict[str, Any]:
    """
    Generate a formatted M&V summary for payment authorization.

    Args:
        contract_id: Contract identifier
        performance_period: Period covered (e.g., "Q2 2025" or "FY2025")
        guaranteed_savings: Contractual guaranteed savings ($)
        verified_savings: Actual verified savings ($)
        baseline_adjustments: Optional notes on baseline adjustments
        ecm_notes: Optional notes on ECM performance

    Returns:
        Formatted summary suitable for COR authorization package
    """
    variance_amount = verified_savings - guaranteed_savings
    variance_percent = (variance_amount / guaranteed_savings) * 100 if guaranteed_savings else 0

    if variance_percent >= 0:
        status = "SURPLUS"
        status_icon = "✓"
    elif variance_percent >= -3:
        status = "ACCEPTABLE"
        status_icon = "✓"
    elif variance_percent >= -5:
        status = "WATCH LIST"
        status_icon = "⚠"
    else:
        status = "SHORTFALL"
        status_icon = "✗"

    summary = f"""
================================================================================
                    M&V PERFORMANCE SUMMARY - {contract_id}
================================================================================

PERFORMANCE PERIOD: {performance_period}
ANALYSIS DATE: {datetime.now().strftime('%B %d, %Y')}

SAVINGS ANALYSIS
----------------
Guaranteed Savings:     ${guaranteed_savings:,.2f}
Verified Savings:       ${verified_savings:,.2f}
Variance:               ${variance_amount:,.2f} ({variance_percent:+.2f}%)

PERFORMANCE STATUS: {status_icon} {status}

"""
    if baseline_adjustments:
        summary += f"""BASELINE ADJUSTMENTS
--------------------
{baseline_adjustments}

"""
    if ecm_notes:
        summary += f"""ECM PERFORMANCE NOTES
---------------------
{ecm_notes}

"""
    if status == "SHORTFALL":
        summary += """ACTION REQUIRED
---------------
☐ Calculate shortfall payment per contract terms
☐ Prepare shortfall invoice request
☐ Notify Contracting Officer
☐ Document in contract file

"""
    elif status == "WATCH LIST":
        summary += """MONITORING ACTIONS
------------------
☐ Request contractor remediation plan (30 days)
☐ Add to quarterly watch list
☐ Schedule follow-up review

"""
    else:
        summary += """AUTHORIZATION
-------------
☐ M&V report reviewed and validated
☐ Savings verification complete
☐ Ready for payment authorization

"""
    summary += "================================================================================"

    return {
        "contract_id": contract_id,
        "period": performance_period,
        "status": status,
        "variance_percent": round(variance_percent, 2),
        "formatted_summary": summary,
        "ready_for_payment": status in ["SURPLUS", "ACCEPTABLE"]
    }


if __name__ == "__main__":
    print("Starting M&V Report Analyzer MCP Server...")
    print(f"Knowledge Base: {KNOWLEDGE_BASE}")
    print(f"M&V Reports Dir: {MV_REPORTS_DIR}")
    mcp.run()
