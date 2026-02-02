#!/usr/bin/env python3
"""
GSA Payment Authorization Tool - MCP Server
============================================

An MCP (Model Context Protocol) server for GSA ESPC/UESC payment authorization.
Provides tools for calculating shortfalls, validating payments, and generating
authorization packages.

Tools Available:
- calculate_shortfall: Calculate energy savings shortfall
- validate_payment_request: Validate payment against contract terms
- generate_authorization_package: Create complete authorization documentation
- get_contract_info: Retrieve contract details from portfolio
- list_upcoming_payments: Show payments due within a timeframe

Usage:
    python server.py

Integration:
    Add to Claude Desktop config (claude_desktop_config.json)
"""

import json
import os
import re
from datetime import datetime, timedelta
from typing import Any
from pathlib import Path

# MCP imports
try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    print("Error: MCP package not installed. Run: pip install mcp")
    raise

# Initialize the MCP server
server = Server("gsa-payment-authorization")

# Get the project root (two levels up from this file)
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Contract data (loaded from portfolio baseline)
CONTRACT_DATA = {
    "NDER2_SD_Ameresco": {
        "vendor": "Ameresco",
        "type": "ESPC NDER2",
        "region": "R9",
        "co": "Felipe Jolles",
        "total_value": 53687414,
        "annual_payment": 1684326,
        "payment_due": "April 1",
        "delegation_status": "No Delegation",
        "watch_list": True,
        "variance": -1.0
    },
    "NDER2_SF_Honeywell": {
        "vendor": "Honeywell",
        "type": "ESPC NDER2",
        "region": "R9",
        "co": "Heidi Johnson",
        "total_value": None,
        "annual_payment": None,
        "payment_due": "March 1",
        "delegation_status": "On File",
        "watch_list": True,
        "variance": -4.5,
        "shortfall_amount": 95000
    },
    "NDER2_LA_Honeywell": {
        "vendor": "Honeywell",
        "type": "ESPC NDER2",
        "region": "R9",
        "co": "Heidi Johnson",
        "total_value": None,
        "annual_payment": None,
        "payment_due": "March 1",
        "delegation_status": "No Delegation",
        "watch_list": True,
        "variance": -7.5,
        "shortfall_amount": 35000
    },
    "LA_ESPC_ABM": {
        "vendor": "ABM Industries",
        "type": "ESPC",
        "region": "R9",
        "co": "Heidi Johnson",
        "total_value": 143903595,
        "annual_payment": 3821698,
        "payment_due": "May 1",
        "delegation_status": "No Delegation",
        "watch_list": False,
        "variance": 0
    },
    "UESC_SD_SDGandE": {
        "vendor": "SDG&E",
        "type": "UESC",
        "region": "R9",
        "co": "Felipe Jolles",
        "total_value": 8384152,
        "annual_payment": 586201,
        "payment_due": "May 1",
        "delegation_status": "On File",
        "watch_list": False,
        "variance": 0
    },
    "PJKK_JCI": {
        "vendor": "Johnson Controls",
        "type": "ESPC",
        "region": "R9",
        "co": "Miles Conant",
        "total_value": None,
        "annual_payment": 236941,
        "payment_due": "July 31",
        "delegation_status": "Nomination Issued",
        "watch_list": False,
        "variance": 0,
        "final_year": True,
        "contract_end": "September 30, 2025"
    },
    "McKinstry_R8": {
        "vendor": "McKinstry",
        "type": "ESPC",
        "region": "R8",
        "co": "Felipe Jolles",
        "total_value": 18494626,
        "annual_payment": None,
        "payment_due": "December 31",
        "delegation_status": "On File",
        "watch_list": True,
        "variance": 0,
        "issue": "0% report submission"
    },
    "UESC_Sansome_PGE": {
        "vendor": "PG&E",
        "type": "UESC",
        "region": "R9",
        "co": "Felipe Jolles",
        "total_value": 11564801,
        "annual_payment": 112670,
        "payment_due": "December 1",
        "delegation_status": "No Delegation",
        "watch_list": True,
        "variance": 0,
        "issue": "0% NCMMS"
    },
    "ENABLE_Detroit_Honeywell": {
        "vendor": "Honeywell",
        "type": "ENABLE",
        "region": "R5",
        "co": "Jerrud Parker",
        "total_value": 24670720,
        "annual_payment": None,
        "payment_due": "March",
        "delegation_status": "Nomination Issued",
        "watch_list": False,
        "variance": 0
    },
    "NDER1_Chicago_Noresco": {
        "vendor": "Noresco",
        "type": "ESPC NDER1",
        "region": "R5",
        "co": "Krystal Blue",
        "total_value": None,
        "annual_payment": None,
        "payment_due": "July",
        "delegation_status": "Nomination Issued",
        "watch_list": False,
        "variance": 0
    },
    "ABM_ENABLE_R8": {
        "vendor": "ABM Industries",
        "type": "ENABLE",
        "region": "R8",
        "co": "Felipe Jolles",
        "total_value": 17906204,
        "annual_payment": None,
        "payment_due": "July 1, 2026",
        "delegation_status": "On File",
        "watch_list": True,
        "variance": 0,
        "issue": "0% report submission"
    }
}

# Payment schedule
PAYMENT_SCHEDULE = [
    {"month": "January", "contract": "NDER1_Battle_Creek", "vendor": "Trane", "amount": None},
    {"month": "March", "contract": "ENABLE_Detroit_Honeywell", "vendor": "Honeywell", "amount": None},
    {"month": "April 1", "contract": "NDER2_SD_Ameresco", "vendor": "Ameresco", "amount": 1684326},
    {"month": "May 1", "contract": "LA_ESPC_ABM", "vendor": "ABM", "amount": 3821698},
    {"month": "May 1", "contract": "UESC_SD_SDGandE", "vendor": "SDG&E", "amount": 586201},
    {"month": "July 31", "contract": "PJKK_JCI", "vendor": "JCI", "amount": 236941, "final": True},
    {"month": "July", "contract": "NDER1_Chicago_Noresco", "vendor": "Noresco", "amount": None},
    {"month": "November", "contract": "Harold_Washington", "vendor": "Ameresco", "amount": None},
    {"month": "December 1", "contract": "UESC_Sansome_PGE", "vendor": "PG&E", "amount": 112670},
    {"month": "December 31", "contract": "McKinstry_R8", "vendor": "McKinstry", "amount": None},
]


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools."""
    return [
        Tool(
            name="calculate_shortfall",
            description="Calculate energy savings shortfall for a contract period. Returns shortfall amount, percentage, and remediation options.",
            inputSchema={
                "type": "object",
                "properties": {
                    "contract_id": {
                        "type": "string",
                        "description": "Contract identifier (e.g., NDER2_LA_Honeywell)"
                    },
                    "period": {
                        "type": "string",
                        "description": "Assessment period (e.g., 2025-Q2)"
                    },
                    "guaranteed_savings": {
                        "type": "number",
                        "description": "Guaranteed savings amount in dollars"
                    },
                    "verified_savings": {
                        "type": "number",
                        "description": "Verified/actual savings amount in dollars"
                    }
                },
                "required": ["contract_id", "period", "guaranteed_savings", "verified_savings"]
            }
        ),
        Tool(
            name="validate_payment_request",
            description="Validate a payment request against contract terms, delegation status, and OIG compliance requirements.",
            inputSchema={
                "type": "object",
                "properties": {
                    "contract_id": {
                        "type": "string",
                        "description": "Contract identifier"
                    },
                    "payment_amount": {
                        "type": "number",
                        "description": "Requested payment amount in dollars"
                    },
                    "period": {
                        "type": "string",
                        "description": "Payment period (e.g., 2025-Q2)"
                    },
                    "mv_witnessed": {
                        "type": "boolean",
                        "description": "Whether M&V activities were independently witnessed by government COR"
                    },
                    "co_authorized": {
                        "type": "boolean",
                        "description": "Whether all scope changes have CO authorization"
                    }
                },
                "required": ["contract_id", "payment_amount", "period"]
            }
        ),
        Tool(
            name="generate_authorization_package",
            description="Generate a complete payment authorization package with all required documentation checklist.",
            inputSchema={
                "type": "object",
                "properties": {
                    "contract_id": {
                        "type": "string",
                        "description": "Contract identifier"
                    },
                    "period": {
                        "type": "string",
                        "description": "Payment period"
                    },
                    "payment_amount": {
                        "type": "number",
                        "description": "Payment amount"
                    },
                    "shortfall_amount": {
                        "type": "number",
                        "description": "Shortfall amount if any (default 0)"
                    },
                    "cor_name": {
                        "type": "string",
                        "description": "COR name for authorization"
                    }
                },
                "required": ["contract_id", "period", "payment_amount"]
            }
        ),
        Tool(
            name="get_contract_info",
            description="Retrieve detailed contract information from the portfolio baseline.",
            inputSchema={
                "type": "object",
                "properties": {
                    "contract_id": {
                        "type": "string",
                        "description": "Contract identifier or partial name"
                    }
                },
                "required": ["contract_id"]
            }
        ),
        Tool(
            name="list_upcoming_payments",
            description="List all payments due within a specified timeframe.",
            inputSchema={
                "type": "object",
                "properties": {
                    "months_ahead": {
                        "type": "integer",
                        "description": "Number of months to look ahead (default 3)"
                    },
                    "include_watch_list": {
                        "type": "boolean",
                        "description": "Include watch list status in output (default true)"
                    }
                },
                "required": []
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls."""

    if name == "calculate_shortfall":
        return await calculate_shortfall(arguments)
    elif name == "validate_payment_request":
        return await validate_payment_request(arguments)
    elif name == "generate_authorization_package":
        return await generate_authorization_package(arguments)
    elif name == "get_contract_info":
        return await get_contract_info(arguments)
    elif name == "list_upcoming_payments":
        return await list_upcoming_payments(arguments)
    else:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def calculate_shortfall(args: dict) -> list[TextContent]:
    """Calculate energy savings shortfall."""
    contract_id = args["contract_id"]
    period = args["period"]
    guaranteed = args["guaranteed_savings"]
    verified = args["verified_savings"]

    shortfall = guaranteed - verified
    shortfall_pct = (shortfall / guaranteed) * 100 if guaranteed > 0 else 0

    result = {
        "contract_id": contract_id,
        "period": period,
        "guaranteed_savings": guaranteed,
        "verified_savings": verified,
        "shortfall_amount": shortfall,
        "shortfall_percentage": round(shortfall_pct, 2),
        "status": "SHORTFALL" if shortfall > 0 else "MET_GUARANTEE",
        "remediation_options": []
    }

    if shortfall > 0:
        result["remediation_options"] = [
            f"1. Contractor payment reduction: ${shortfall:,.2f}",
            "2. ECM performance optimization required",
            "3. Baseline adjustment review (if conditions changed)",
            "4. Extended measurement period to verify savings"
        ]
        result["oig_compliance_note"] = (
            "Per OIG A240046: Document all shortfall calculations with independent "
            "government witnessing verification. Ensure no contractor employees "
            "served as witnesses for M&V activities."
        )

    # Check if contract is on watch list
    if contract_id in CONTRACT_DATA:
        contract = CONTRACT_DATA[contract_id]
        if contract.get("watch_list"):
            result["watch_list_alert"] = f"Contract is on watch list with {contract.get('variance', 0)}% variance"

    return [TextContent(type="text", text=json.dumps(result, indent=2))]


async def validate_payment_request(args: dict) -> list[TextContent]:
    """Validate payment request against requirements."""
    contract_id = args["contract_id"]
    payment_amount = args["payment_amount"]
    period = args["period"]
    mv_witnessed = args.get("mv_witnessed", False)
    co_authorized = args.get("co_authorized", True)

    validation_result = {
        "contract_id": contract_id,
        "payment_amount": payment_amount,
        "period": period,
        "validation_status": "PENDING",
        "checks": [],
        "blockers": [],
        "warnings": []
    }

    # Check contract exists
    contract = CONTRACT_DATA.get(contract_id)
    if not contract:
        # Try fuzzy match
        for key in CONTRACT_DATA:
            if contract_id.lower() in key.lower():
                contract = CONTRACT_DATA[key]
                contract_id = key
                break

    if not contract:
        validation_result["validation_status"] = "FAILED"
        validation_result["blockers"].append(f"Contract '{contract_id}' not found in portfolio")
        return [TextContent(type="text", text=json.dumps(validation_result, indent=2))]

    # Check 1: Delegation status
    delegation = contract.get("delegation_status", "Unknown")
    if delegation == "On File":
        validation_result["checks"].append("✅ COR delegation letter on file")
    elif delegation == "Nomination Issued":
        validation_result["warnings"].append("⚠️ Nomination issued but delegation pending - request letter before payment")
    else:
        validation_result["blockers"].append("❌ No COR delegation - cannot authorize payment")

    # Check 2: OIG Compliance - M&V Witnessing
    if mv_witnessed:
        validation_result["checks"].append("✅ M&V activities independently witnessed by government COR")
    else:
        validation_result["blockers"].append(
            "❌ OIG A240046 Violation: M&V activities must be witnessed by government COR "
            "(not contractor employees)"
        )

    # Check 3: CO Authorization for scope changes
    if co_authorized:
        validation_result["checks"].append("✅ All scope changes have CO authorization")
    else:
        validation_result["blockers"].append("❌ OIG A240046 Violation: Scope changes require CO authorization")

    # Check 4: Watch list status
    if contract.get("watch_list"):
        variance = contract.get("variance", 0)
        validation_result["warnings"].append(
            f"⚠️ Contract on watch list ({variance}% variance) - verify shortfall remediation"
        )

    # Check 5: Payment amount validation
    expected = contract.get("annual_payment")
    if expected and payment_amount > expected * 1.1:
        validation_result["warnings"].append(
            f"⚠️ Payment ${payment_amount:,.2f} exceeds expected annual amount ${expected:,.2f}"
        )

    # Check 6: Final year handling
    if contract.get("final_year"):
        validation_result["warnings"].append("⚠️ FINAL YEAR - Ensure closeout documentation prepared")

    # Determine overall status
    if validation_result["blockers"]:
        validation_result["validation_status"] = "BLOCKED"
    elif validation_result["warnings"]:
        validation_result["validation_status"] = "APPROVED_WITH_WARNINGS"
    else:
        validation_result["validation_status"] = "APPROVED"

    # Add prompt payment act reminder
    validation_result["prompt_payment_act"] = {
        "payment_due_days": 30,
        "documentation_deadline_days": 15,
        "late_payment_penalty": "Automatic interest accrual"
    }

    return [TextContent(type="text", text=json.dumps(validation_result, indent=2))]


async def generate_authorization_package(args: dict) -> list[TextContent]:
    """Generate complete payment authorization package."""
    contract_id = args["contract_id"]
    period = args["period"]
    payment_amount = args["payment_amount"]
    shortfall = args.get("shortfall_amount", 0)
    cor_name = args.get("cor_name", "Matthew Schreck, CEM")

    # Get contract info
    contract = CONTRACT_DATA.get(contract_id, {})

    package = {
        "authorization_package": {
            "contract_id": contract_id,
            "vendor": contract.get("vendor", "Unknown"),
            "contract_type": contract.get("type", "Unknown"),
            "region": contract.get("region", "Unknown"),
            "contracting_officer": contract.get("co", "Unknown"),
            "cor": cor_name,
            "period": period,
            "payment_amount": payment_amount,
            "shortfall_amount": shortfall,
            "net_payment": payment_amount - shortfall,
            "generated_date": datetime.now().isoformat()
        },
        "required_documentation": {
            "pre_payment": [
                "☐ M&V Report (reviewed and approved)",
                "☐ Savings verification calculations",
                "☐ Government witnessing forms (Appendix B) - signed by COR",
                "☐ Invoice with supporting documentation",
                "☐ COR delegation letter (on file)"
            ],
            "oig_compliance": [
                "☐ Independent government witnessing confirmed (no contractor witnesses)",
                "☐ Witnessing form signatures align with activity dates",
                "☐ All scope changes have CO authorization",
                "☐ No unauthorized contract modifications"
            ],
            "financial": [
                "☐ Invoice reconciled with M&V report",
                "☐ Shortfall calculations verified (if applicable)",
                "☐ Payment within Prompt Payment Act timeline",
                "☐ Budget availability confirmed"
            ]
        },
        "authorization_statement": (
            f"I, {cor_name}, Contracting Officer's Representative, hereby certify that:\n"
            f"1. The contractor has performed satisfactorily for period {period}\n"
            f"2. All M&V activities were independently witnessed by government personnel\n"
            f"3. The payment amount of ${payment_amount:,.2f} is accurate and supported\n"
            f"4. All documentation requirements have been met\n"
            f"5. This authorization complies with OIG A240046 corrective actions"
        ),
        "workflow": {
            "step_1": "COR completes documentation checklist",
            "step_2": "COR signs authorization statement",
            "step_3": f"Submit to CO ({contract.get('co', 'Unknown')}) for approval",
            "step_4": "CO reviews and approves payment",
            "step_5": "Finance processes payment within PPA timeline"
        }
    }

    if shortfall > 0:
        package["shortfall_handling"] = {
            "shortfall_amount": shortfall,
            "net_payment": payment_amount - shortfall,
            "action_required": "Document shortfall in M&V report with remediation plan",
            "contractor_notification": "Required per contract terms"
        }

    if contract.get("final_year"):
        package["closeout_requirements"] = {
            "note": "FINAL YEAR - Additional closeout documentation required",
            "items": [
                "☐ Final M&V report",
                "☐ O&M transition plan",
                "☐ Contract closeout package",
                "☐ Final inspection report",
                "☐ Release of claims"
            ]
        }

    return [TextContent(type="text", text=json.dumps(package, indent=2))]


async def get_contract_info(args: dict) -> list[TextContent]:
    """Get contract information."""
    contract_id = args["contract_id"]

    # Try exact match first
    contract = CONTRACT_DATA.get(contract_id)

    # Try fuzzy match
    if not contract:
        for key, value in CONTRACT_DATA.items():
            if contract_id.lower() in key.lower() or contract_id.lower() in value.get("vendor", "").lower():
                contract = value
                contract_id = key
                break

    if not contract:
        return [TextContent(type="text", text=json.dumps({
            "error": f"Contract '{contract_id}' not found",
            "available_contracts": list(CONTRACT_DATA.keys())
        }, indent=2))]

    result = {
        "contract_id": contract_id,
        **contract
    }

    # Add delegation action if needed
    if contract.get("delegation_status") != "On File":
        result["action_required"] = "Request COR delegation letter from CO"

    return [TextContent(type="text", text=json.dumps(result, indent=2))]


async def list_upcoming_payments(args: dict) -> list[TextContent]:
    """List upcoming payments."""
    months_ahead = args.get("months_ahead", 3)
    include_watch_list = args.get("include_watch_list", True)

    # Get current month
    current_month = datetime.now().month

    # Map month names to numbers for filtering
    month_map = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "April 1": 4, "May": 5, "May 1": 5, "June": 6,
        "July": 7, "July 31": 7, "August": 8, "September": 9,
        "October": 10, "November": 11, "November 1": 11,
        "December": 12, "December 1": 12, "December 31": 12
    }

    upcoming = []
    for payment in PAYMENT_SCHEDULE:
        month_str = payment["month"]
        month_num = month_map.get(month_str, 0)

        # Check if within range (simplified - doesn't handle year boundary)
        if month_num >= current_month and month_num <= current_month + months_ahead:
            entry = {
                "payment_due": month_str,
                "contract": payment["contract"],
                "vendor": payment["vendor"],
                "amount": f"${payment['amount']:,.2f}" if payment["amount"] else "TBD"
            }

            if payment.get("final"):
                entry["note"] = "FINAL PAYMENT"

            # Add watch list info
            if include_watch_list:
                contract_data = CONTRACT_DATA.get(payment["contract"], {})
                if contract_data.get("watch_list"):
                    entry["watch_list"] = True
                    entry["variance"] = contract_data.get("variance", 0)
                    if contract_data.get("issue"):
                        entry["issue"] = contract_data["issue"]

            upcoming.append(entry)

    result = {
        "timeframe": f"Next {months_ahead} months",
        "generated": datetime.now().isoformat(),
        "upcoming_payments": upcoming,
        "total_scheduled": sum(p.get("amount", 0) or 0 for p in PAYMENT_SCHEDULE if month_map.get(p["month"], 0) >= current_month),
        "prompt_payment_reminder": "Documentation due 15 days before payment date"
    }

    return [TextContent(type="text", text=json.dumps(result, indent=2))]


async def main():
    """Run the MCP server."""
    print("MCP Server running on stdio transport")
    print("Server: GSA Payment Authorization Tool")
    print("Tools: 5 tools available")
    print("  - calculate_shortfall")
    print("  - validate_payment_request")
    print("  - generate_authorization_package")
    print("  - get_contract_info")
    print("  - list_upcoming_payments")

    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
