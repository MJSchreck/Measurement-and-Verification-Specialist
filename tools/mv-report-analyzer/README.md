# M&V Report Analyzer

Python tool for parsing Measurement & Verification reports from ESPC/UESC energy performance contracts.

## Features

- Extract key contract data from text-based M&V reports
- Support for multiple report formats and naming conventions
- JSON output for integration with other tools
- Batch processing of report directories

## Extracted Data

| Field | Description |
|-------|-------------|
| Contract ID | GS contract number, Task Order, etc. |
| Performance Period | Start and end dates |
| Guaranteed Savings | Contractual savings amount ($) |
| Verified Savings | Actual measured savings ($) |
| Variance | Difference and percentage |
| Baseline Adjustments | Weather, occupancy, rate adjustments |

## Usage

### Single File
```bash
python mv_parser.py report.txt
python mv_parser.py report.txt --output json
```

### Directory Batch
```bash
python mv_parser.py --dir ./reports
python mv_parser.py --dir ./reports --output json > all_reports.json
```

### Output Formats
- `summary` - Human-readable summary (default)
- `json` - Structured JSON for programmatic use
- `both` - Both formats

## Example Output

```
============================================================
M&V REPORT SUMMARY
============================================================
Contract ID:      GS-07P-14-MK-C-0042
Contract Name:    Federal Building Energy Retrofit - Detroit
Period:           October 1, 2024 to September 30, 2025
------------------------------------------------------------
Guaranteed Savings:  $1,247,832.00
Verified Savings:    $1,198,456.00
Variance:            $-49,376.00 (-3.96%) - SHORTFALL
------------------------------------------------------------
BASELINE ADJUSTMENTS:
  - Weather Normalization: $18,432.00
  - Occupancy: $-12,500.00
  - Rate: $4,200.00
============================================================
```

## Integration

### With Knowledge Base
Output JSON can be saved to `knowledge-base/m-v-reports/` for use with the MCP Payment Authorization Tool.

### With MCP Server
```python
from mv_parser import MVReportParser

parser = MVReportParser()
data = parser.parse_file("report.txt")

# Use in payment validation
if data.variance_percent and data.variance_percent < -3.0:
    print(f"WARNING: {data.contract_id} has {data.variance_percent:.2f}% shortfall")
```

## Extending for PDFs

Future PDF support will use `pdfplumber` or `PyPDF2`. The parser is designed for extension:

```python
class PDFMVParser(MVReportParser):
    def parse_pdf(self, file_path: Path) -> MVReportData:
        # Extract text from PDF
        text = extract_pdf_text(file_path)
        return self.parse_text(text, source_file=str(file_path))
```

## Requirements

- Python 3.8+
- No external dependencies for text parsing
- For PDF support (future): `pdfplumber>=0.9.0`
