# MCP Servers for GSA Energy Contract Management

This directory contains Model Context Protocol (MCP) servers for automating GSA ESPC/UESC contract management workflows.

## Available Servers

### payment-authorization-tool

**Purpose**: Automate payment authorization workflow for ESPC/UESC contracts.

**Tools**:
| Tool | Description |
|------|-------------|
| `calculate_shortfall` | Calculate energy savings shortfall and remediation options |
| `validate_payment_request` | Validate payments against OIG compliance and delegation status |
| `generate_authorization_package` | Create complete authorization documentation package |
| `get_contract_info` | Query contract details from portfolio baseline |
| `list_upcoming_payments` | Show payments due within specified timeframe |

**Quick Start**: See `payment-authorization-tool/QUICKSTART.md`

---

### mv-report-analyzer

**Purpose**: Parse and analyze M&V reports to extract savings data, identify variances, and generate authorization summaries.

**Tools**:
| Tool | Description |
|------|-------------|
| `parse_mv_report` | Parse raw M&V report text and extract structured data |
| `analyze_mv_file` | Analyze a report file from the knowledge base |
| `check_performance_status` | Quick check of savings variance and performance status |
| `list_mv_reports` | List all M&V reports in the knowledge base |
| `generate_mv_summary` | Create formatted summary for payment authorization |

**Quick Start**: See `mv-report-analyzer/QUICKSTART.md`

## Architecture

```
mcp-servers/
├── README.md                          # This file
├── payment-authorization-tool/
│   ├── server.py                      # MCP server implementation
│   ├── requirements.txt               # Python dependencies
│   └── QUICKSTART.md                  # Setup guide
└── mv-report-analyzer/
    ├── server.py                      # M&V parsing and analysis
    ├── requirements.txt               # Python dependencies
    └── QUICKSTART.md                  # Setup guide
```

## Integration with Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "payment-authorization": {
      "command": "python",
      "args": ["/path/to/mcp-servers/payment-authorization-tool/server.py"]
    },
    "mv-report-analyzer": {
      "command": "python",
      "args": ["/path/to/mcp-servers/mv-report-analyzer/server.py"]
    }
  }
}
```

## Integration with Claude Code

MCP servers can also be used with Claude Code CLI:

```bash
claude mcp add --transport stdio payment-auth -- python /path/to/server.py
```

## Data Sources

The servers use data from these repository files:
- `Contract_Portfolio_Baseline_2026.md` - Contract details
- `Payment_Deadline_Tracker_FY2025_2026.md` - Payment schedules
- `GSA_AI_Assistant_Document_Index.md` - Cross-references

## OIG Compliance

All servers enforce OIG A240046 compliance:
- Independent government witnessing verification
- No contractor employees as witnesses
- Scope change CO authorization checks
- Delegation status validation

## Future Servers (Planned)

- `cpars-generator` - Automated CPARS assessment generation
- `compliance-monitor` - Real-time compliance tracking
- `delegation-tracker` - COR delegation status management

## Development

To create a new MCP server:

1. Create a new directory under `mcp-servers/`
2. Implement server using `mcp` Python package
3. Add `requirements.txt` with dependencies
4. Create `QUICKSTART.md` for setup instructions
5. Update this README

## Requirements

- Python 3.8+
- `mcp` package (pip install mcp)
- Claude Desktop or Claude Code CLI
