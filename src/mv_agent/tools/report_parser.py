"""Parse M&V reports and extract structured savings data."""

import logging
from pathlib import Path

from ..models.schemas import ReportData, ECMResult
from ..models.enums import ReportType, IPMVPOption
from ..observability.tracer import traced

logger = logging.getLogger(__name__)


@traced(tool_name="parse_mv_report")
def parse_mv_report(
    file_path: str,
    report_type: str | None = None,
    ipmvp_option: str | None = None,
) -> ReportData:
    """Extract structured data from an M&V report file.

    Args:
        file_path: Path to the M&V report (PDF, XLSX, or JSON).
        report_type: Type of report (annual, quarterly, etc.).
        ipmvp_option: IPMVP measurement option if known.

    Returns:
        ReportData with parsed ECMs, savings totals, and warnings.

    Raises:
        FileNotFoundError: If the report file doesn't exist.
        ValueError: If the file format is unsupported.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Report file not found: {file_path}")

    suffix = path.suffix.lower()
    if suffix not in {".pdf", ".xlsx", ".xls", ".json", ".csv"}:
        raise ValueError(f"Unsupported file format: {suffix}")

    logger.info("Parsing M&V report: %s (type=%s)", file_path, report_type)

    # Parse based on format
    if suffix == ".json":
        return _parse_json_report(path, report_type, ipmvp_option)
    elif suffix in {".xlsx", ".xls"}:
        return _parse_excel_report(path, report_type, ipmvp_option)
    elif suffix == ".csv":
        return _parse_csv_report(path, report_type, ipmvp_option)
    else:
        return _parse_pdf_report(path, report_type, ipmvp_option)


def _parse_json_report(
    path: Path, report_type: str | None, ipmvp_option: str | None
) -> ReportData:
    """Parse a JSON-formatted M&V report."""
    import json

    with open(path) as f:
        data = json.load(f)

    ecms = []
    for ecm_data in data.get("ecms", []):
        ecm = ECMResult(
            ecm_id=ecm_data.get("ecm_id", ""),
            description=ecm_data.get("description", ""),
            guaranteed_savings_kwh=ecm_data.get("guaranteed_savings_kwh", 0),
            actual_savings_kwh=ecm_data.get("actual_savings_kwh", 0),
            guaranteed_savings_cost=ecm_data.get("guaranteed_savings_cost", 0),
            actual_savings_cost=ecm_data.get("actual_savings_cost", 0),
            ipmvp_option=(
                IPMVPOption(ecm_data["ipmvp_option"])
                if "ipmvp_option" in ecm_data
                else None
            ),
            measurement_period=ecm_data.get("measurement_period", ""),
            adjustments=ecm_data.get("adjustments", []),
        )
        ecm.compute_variance()
        ecms.append(ecm)

    total_guaranteed = sum(e.guaranteed_savings_kwh for e in ecms)
    total_actual = sum(e.actual_savings_kwh for e in ecms)
    variance = ((total_actual - total_guaranteed) / total_guaranteed * 100) if total_guaranteed else 0

    warnings = []
    for ecm in ecms:
        if ecm.variance_pct < -10:
            warnings.append(
                f"ECM {ecm.ecm_id}: significant shortfall ({ecm.variance_pct:.1f}%)"
            )

    return ReportData(
        facility_name=data.get("facility_name", ""),
        report_type=ReportType(report_type) if report_type else ReportType.ANNUAL,
        report_period=data.get("report_period", ""),
        ecms=ecms,
        total_guaranteed_kwh=total_guaranteed,
        total_actual_kwh=total_actual,
        total_guaranteed_cost=sum(e.guaranteed_savings_cost for e in ecms),
        total_actual_cost=sum(e.actual_savings_cost for e in ecms),
        variance_pct=variance,
        warnings=warnings,
    )


def _parse_excel_report(
    path: Path, report_type: str | None, ipmvp_option: str | None
) -> ReportData:
    """Parse an Excel M&V report. Placeholder for openpyxl integration."""
    logger.warning("Excel parsing not yet implemented — returning empty ReportData")
    return ReportData(
        warnings=["Excel parsing requires openpyxl — install with: pip install openpyxl"]
    )


def _parse_csv_report(
    path: Path, report_type: str | None, ipmvp_option: str | None
) -> ReportData:
    """Parse a CSV M&V report."""
    logger.warning("CSV parsing not yet implemented — returning empty ReportData")
    return ReportData(warnings=["CSV parsing pending implementation"])


def _parse_pdf_report(
    path: Path, report_type: str | None, ipmvp_option: str | None
) -> ReportData:
    """Parse a PDF M&V report. Placeholder for PDF extraction."""
    logger.warning("PDF parsing not yet implemented — returning empty ReportData")
    return ReportData(
        warnings=["PDF parsing requires pymupdf — install with: pip install pymupdf"]
    )
