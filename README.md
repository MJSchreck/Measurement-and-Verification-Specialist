# Measurement & Verification Specialist
## GSA Energy Contract Management System

**COR:** Matthew Schreck, CEM
**Role:** Energy Program Specialist / Zone C M&V Specialist
**Organization:** GSA Office of Facilities Management - Energy Division
**Portfolio:** $300M+ across 15+ ESPC/UESC contracts

---

## Overview

This repository contains the complete knowledge base and automation tools for GSA ESPC/UESC contract management, including:

- CPARS assessment templates and questionnaires
- Contract portfolio baseline and tracking
- COR delegation management
- Payment authorization workflows
- OIG A240046 compliance documentation
- MCP servers for AI-assisted automation

## Repository Structure

```
Measurement-and-Verification-Specialist/
├── README.md                                    # This file
├── GSA_AI_Assistant_Document_Index.md           # Master index for AI integration
│
├── # CPARS Assessment Templates
├── CPARS_QTR2_Questions.md                      # Generic CPARS questionnaire
├── CPARS_QTR2_ENABLE_Detroit_Honeywell.md       # ENABLE-specific (Honeywell R5)
├── CPARS_QTR2_NDER1_Chicago_Noresco.md          # NDER1-specific (Noresco R5)
│
├── # Portfolio Management
├── Contract_Portfolio_Baseline_2026.md          # Complete contract portfolio
├── Payment_Deadline_Tracker_FY2025_2026.md      # Payment calendar & deadlines
├── COR_Delegation_Request_Templates.md          # Email templates for delegations
│
└── # MCP Automation
    └── mcp-servers/
        ├── README.md
        └── payment-authorization-tool/
            ├── server.py                        # MCP server
            ├── requirements.txt
            └── QUICKSTART.md
```

## Quick Start

### For Documentation

All documents are in Markdown format and can be:
- Viewed directly on GitHub
- Imported into Notion, Obsidian, or other knowledge management tools
- Used with AI assistants (see `GSA_AI_Assistant_Document_Index.md`)

### For MCP Automation

```bash
# Install dependencies
cd mcp-servers/payment-authorization-tool
pip install -r requirements.txt

# Test the server
python server.py

# Configure Claude Desktop (see QUICKSTART.md)
```

## Contract Portfolio Summary

| Tier | Contracts | Status |
|------|-----------|--------|
| **Tier 1** | 4 contracts | Delegation On File |
| **Tier 2** | 5 contracts | Nomination Issued |
| **Tier 3** | 5+ contracts | Delegation Required |

**Key Contractors:**
- Honeywell (NDER2 SF/LA, ENABLE Detroit)
- Ameresco (NDER2 SD, Harold Washington)
- ABM Industries (LA ESPC, ENABLE R8)
- McKinstry (DFC & Mt Plains R8)
- Johnson Controls (PJKK - Final Year)
- Noresco (NDER1 Chicago)

## Compliance Framework

### OIG Audit A240046
Active corrective actions through September 2026:
- Independent government M&V witnessing required
- No contractor employees as government witnesses
- All scope changes require CO authorization
- Witnessing form timing must match activities

### FAR References
- FAR 42.1502 - Policy
- FAR 42.1503 - Procedures (CPARS ratings)
- 5 CFR 1315 - Prompt Payment Act

### DOE/FEMP Standards
- DOE FEMP M&V Guidelines v4.0
- IPMVP Protocol (2022)

## MCP Tools Available

| Tool | Purpose |
|------|---------|
| `calculate_shortfall` | Energy savings shortfall calculation |
| `validate_payment_request` | OIG compliance validation |
| `generate_authorization_package` | Payment documentation |
| `get_contract_info` | Portfolio queries |
| `list_upcoming_payments` | Payment calendar |

## Key Dates (FY2025)

| Date | Payment | Amount |
|------|---------|--------|
| April 1 | NDER2 SD (Ameresco) | $1,684,326 |
| May 1 | LA ESPC (ABM) | $3,821,698 |
| May 1 | UESC SD (SDG&E) | $586,201 |
| July 31 | PJKK (JCI) - FINAL | $236,941 |
| Dec 1 | UESC Sansome (PG&E) | $112,670 |
| Dec 31 | McKinstry R8 | TBD |

## Watch List

| Contract | Issue | Variance |
|----------|-------|----------|
| NDER2 LA | Shortfall | -7.5% |
| NDER2 SF | Shortfall | -4.5% |
| NDER2 SD | Actionable impact | -1.0% |
| McKinstry | Report submission | 0% |
| ABM ENABLE | Report submission | 0% |
| UESC Sansome | NCMMS | 0% |

## Integration

### With Claude Desktop
Configure MCP servers for automated payment processing.

### With Claude Code
Use repository documents as context for COR operations.

### With Notion/Asana
Import Markdown documents for project management.

### With Gmail
Use delegation templates for CO correspondence.

## Contributing

This is a personal COR operations repository. For GSA-wide process improvements, coordinate through Energy Division leadership.

## License

Internal GSA use only. Contains contract-sensitive information.

---

**Effective Date:** January 1, 2026
**Last Updated:** February 2026
