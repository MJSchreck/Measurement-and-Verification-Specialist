#!/usr/bin/env python3
"""
M&V Report Parser
=================
Extracts key data from Measurement & Verification reports for ESPC/UESC contracts.

Usage:
    python mv_parser.py <report_file>
    python mv_parser.py --dir <directory>

Author: GSA Zone C M&V Specialist Tools
"""

import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional, List
from datetime import datetime


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

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    def summary(self) -> str:
        """Generate a human-readable summary."""
        lines = [
            "=" * 60,
            "M&V REPORT SUMMARY",
            "=" * 60,
            f"Contract ID:      {self.contract_id or 'Not found'}",
            f"Contract Name:    {self.contract_name or 'Not found'}",
            f"Period:           {self.performance_period_start or '?'} to {self.performance_period_end or '?'}",
            "-" * 60,
            f"Guaranteed Savings:  ${self.guaranteed_savings:,.2f}" if self.guaranteed_savings else "Guaranteed Savings:  Not found",
            f"Verified Savings:    ${self.verified_savings:,.2f}" if self.verified_savings else "Verified Savings:    Not found",
        ]

        if self.variance_amount is not None:
            status = "SHORTFALL" if self.variance_amount < 0 else "SURPLUS"
            lines.append(f"Variance:            ${self.variance_amount:,.2f} ({self.variance_percent:+.2f}%) - {status}")

        if self.baseline_adjustments:
            lines.append("-" * 60)
            lines.append("BASELINE ADJUSTMENTS:")
            for adj in self.baseline_adjustments:
                lines.append(f"  - {adj.get('description', 'Unknown')}: ${adj.get('amount', 0):,.2f}")

        if self.parse_warnings:
            lines.append("-" * 60)
            lines.append("WARNINGS:")
            for warning in self.parse_warnings:
                lines.append(f"  ! {warning}")

        lines.append("=" * 60)
        return "\n".join(lines)


class MVReportParser:
    """
    Parser for M&V reports in text format.

    Extensible design - add new pattern matchers for different report formats.
    """

    # Common patterns for contract identifiers
    CONTRACT_ID_PATTERNS = [
        r'Contract\s*(?:No\.?|Number|#|ID)?[:\s]+([A-Z0-9\-]+)',
        r'Task\s*Order[:\s]+([A-Z0-9\-]+)',
        r'TO[:\s]+([A-Z0-9\-]+)',
        r'ESPC[:\s]+([A-Z0-9\-]+)',
        r'UESC[:\s]+([A-Z0-9\-]+)',
        r'GS-\d{2}[A-Z]-\d+[A-Z]?',  # GSA contract format
        r'47P[A-Z0-9]+',  # GSA PBS contract format
    ]

    # Patterns for performance periods
    PERIOD_PATTERNS = [
        r'Performance\s+Period[:\s]+(\w+\s+\d{1,2},?\s+\d{4})\s*(?:to|through|-)\s*(\w+\s+\d{1,2},?\s+\d{4})',
        r'Period[:\s]+(\d{1,2}/\d{1,2}/\d{2,4})\s*(?:to|through|-)\s*(\d{1,2}/\d{1,2}/\d{2,4})',
        r'(?:FY|Fiscal\s+Year)\s*(\d{4})',
        r'Year\s+(\d+)\s+of\s+(\d+)',
        r'Q(\d)\s+(\d{4})',  # Quarter format
    ]

    # Patterns for savings values
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

    # Patterns for baseline adjustments
    BASELINE_PATTERNS = [
        r'Weather\s+(?:Normalization\s+)?Adjustment[:\s]*\$?([\d,]+(?:\.\d{2})?)',
        r'Occupancy\s+Adjustment[:\s]*-?\$?([\d,]+(?:\.\d{2})?)',
        r'Rate\s+Adjustment[:\s]*\$?([\d,]+(?:\.\d{2})?)',
        r'Net\s+Baseline\s+Adjustment[:\s]*\$?([\d,]+(?:\.\d{2})?)',
    ]

    def __init__(self):
        self.data = MVReportData()

    def parse_currency(self, value: str) -> Optional[float]:
        """Convert currency string to float."""
        if not value:
            return None
        try:
            # Remove $ and commas
            cleaned = re.sub(r'[$,]', '', value.strip())
            return float(cleaned)
        except ValueError:
            return None

    def extract_contract_id(self, text: str) -> Optional[str]:
        """Extract contract identifier from text."""
        for pattern in self.CONTRACT_ID_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1) if match.lastindex else match.group(0)
        return None

    def extract_performance_period(self, text: str) -> tuple:
        """Extract performance period start and end dates."""
        for pattern in self.PERIOD_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                if match.lastindex == 2:
                    return match.group(1), match.group(2)
                elif match.lastindex == 1:
                    return match.group(1), None
        return None, None

    def extract_savings(self, text: str, savings_type: str) -> Optional[float]:
        """Extract guaranteed or verified savings amount."""
        patterns = self.SAVINGS_PATTERNS.get(savings_type, [])
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return self.parse_currency(match.group(1))
        return None

    def extract_baseline_adjustments(self, text: str) -> List[dict]:
        """Extract baseline adjustment entries."""
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
        """Extract contract or project name."""
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

    def parse_text(self, text: str, source_file: str = None) -> MVReportData:
        """
        Parse M&V report text and extract structured data.

        Args:
            text: The raw text content of the M&V report
            source_file: Optional source filename for reference

        Returns:
            MVReportData object with extracted values
        """
        self.data = MVReportData()
        self.data.source_file = source_file
        self.data.parse_date = datetime.now().isoformat()

        # Extract all fields
        self.data.contract_id = self.extract_contract_id(text)
        self.data.contract_name = self.extract_contract_name(text)

        start, end = self.extract_performance_period(text)
        self.data.performance_period_start = start
        self.data.performance_period_end = end

        self.data.guaranteed_savings = self.extract_savings(text, 'guaranteed')
        self.data.verified_savings = self.extract_savings(text, 'verified')

        self.data.baseline_adjustments = self.extract_baseline_adjustments(text)

        # Calculate variance
        self.data.calculate_variance()

        # Add warnings for missing critical data
        if not self.data.contract_id:
            self.data.parse_warnings.append("Contract ID not found")
        if not self.data.guaranteed_savings:
            self.data.parse_warnings.append("Guaranteed savings not found")
        if not self.data.verified_savings:
            self.data.parse_warnings.append("Verified savings not found")

        return self.data

    def parse_file(self, file_path: Path) -> MVReportData:
        """Parse an M&V report file."""
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"Report file not found: {file_path}")

        # Read file content
        text = file_path.read_text(encoding='utf-8', errors='replace')

        return self.parse_text(text, source_file=str(file_path))


def parse_directory(directory: Path, output_format: str = 'summary') -> List[MVReportData]:
    """Parse all text files in a directory."""
    directory = Path(directory)
    results = []
    parser = MVReportParser()

    for file_path in directory.glob('*.txt'):
        try:
            data = parser.parse_file(file_path)
            results.append(data)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    # Also check for .md files
    for file_path in directory.glob('*.md'):
        try:
            data = parser.parse_file(file_path)
            results.append(data)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Parse M&V reports and extract key data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python mv_parser.py report.txt
  python mv_parser.py --dir ./reports --output json
  python mv_parser.py report.txt --output json > data.json
        """
    )

    parser.add_argument('file', nargs='?', help='M&V report file to parse')
    parser.add_argument('--dir', '-d', help='Directory of reports to parse')
    parser.add_argument('--output', '-o', choices=['summary', 'json', 'both'],
                        default='summary', help='Output format (default: summary)')

    args = parser.parse_args()

    if not args.file and not args.dir:
        parser.print_help()
        return

    mv_parser = MVReportParser()

    if args.dir:
        results = parse_directory(Path(args.dir), args.output)
        for data in results:
            if args.output in ['summary', 'both']:
                print(data.summary())
                print()
            if args.output in ['json', 'both']:
                print(data.to_json())
                print()

    elif args.file:
        data = mv_parser.parse_file(Path(args.file))

        if args.output in ['summary', 'both']:
            print(data.summary())
        if args.output in ['json', 'both']:
            print(data.to_json())


if __name__ == '__main__':
    main()
