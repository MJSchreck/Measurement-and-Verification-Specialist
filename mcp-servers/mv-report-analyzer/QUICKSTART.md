# M&V Report Analyzer - Quick Start Guide

## Overview

The M&V Report Analyzer MCP server provides tools for parsing and analyzing Measurement & Verification reports directly from Claude Desktop.

## Tools Available

| Tool | Purpose |
|------|---------|
| `parse_mv_report` | Parse raw M&V report text |
| `analyze_mv_file` | Analyze a report file from knowledge base |
| `check_performance_status` | Quick savings variance check |
| `list_mv_reports` | List all reports in knowledge base |
| `generate_mv_summary` | Create formatted summary for authorization |

## Installation

### 1. Install Dependencies
```bash
cd mcp-servers/mv-report-analyzer
pip install -r requirements.txt
```

### 2. Add to Claude Desktop Config

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "mv-report-analyzer": {
      "command": "python",
      "args": [
        "C:/path/to/repo/mcp-servers/mv-report-analyzer/server.py"
      ]
    }
  }
}
```

### 3. Restart Claude Desktop

## Usage Examples

### Parse Report Text
```
Parse this M&V report:

Contract No.: GS-07P-14-MK-C-0042
Performance Period: October 1, 2024 to September 30, 2025
Guaranteed Savings: $1,247,832.00
Verified Savings: $1,198,456.00
```

### Quick Performance Check
```
Check performance status for NDER2 LA:
- Guaranteed: $485,000
- Verified: $461,000
```

### Generate Authorization Summary
```
Generate M&V summary for payment authorization:
- Contract: ENABLE Detroit
- Period: Q2 2025
- Guaranteed: $125,000
- Verified: $128,500
```

## Adding Reports

Place M&V report files in:
```
knowledge-base/m-v-reports/
├── NDER2_LA_FY2025_Q2.txt
├── ENABLE_Detroit_Annual_2025.txt
└── ...
```

Supported formats: `.txt`, `.md` (PDF support coming soon)

## Output Example

```
================================================================================
                    M&V PERFORMANCE SUMMARY - NDER2_LA
================================================================================

PERFORMANCE PERIOD: Q2 2025
ANALYSIS DATE: February 03, 2026

SAVINGS ANALYSIS
----------------
Guaranteed Savings:     $485,000.00
Verified Savings:       $461,000.00
Variance:               $-24,000.00 (-4.95%)

PERFORMANCE STATUS: ⚠ WATCH LIST

MONITORING ACTIONS
------------------
☐ Request contractor remediation plan (30 days)
☐ Add to quarterly watch list
☐ Schedule follow-up review
================================================================================
```
