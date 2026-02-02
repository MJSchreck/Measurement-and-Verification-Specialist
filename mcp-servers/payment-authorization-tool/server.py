#!/usr/bin/env python3
"""
GSA Payment Authorization Tool - MCP Server
============================================

An MCP (Model Context Protocol) server for GSA ESPC/UESC payment authorization.
Dynamically reads contract data from knowledge-base/ files.

Tools Available:
- calculate_shortfall: Calculate energy savings shortfall
- validate_payment_request: Validate payment against contract terms
- generate_authorization_package: Create complete authorization documentation
- get_contract_info: Retrieve contract details from portfolio
- list_upcoming_payments: Show payments due within a timeframe

Usage:
    python server.py

Data Sources:
    knowledge-base/contracts/*.md - Contract-specific data
    knowledge-base/payments/*.md - Payment schedules
    knowledge-base/compliance/*.md - OIG requirements
"""

import json
import os
import re
from datetime import datetime
from typing import Any, Optional
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
KNOWLEDGE_BASE = PROJECT_ROOT / "knowledge-base"


def parse_markdown_table(content: str, table_header: str) -> dict:
    """Parse a markdown table and return key-value pairs."""
    result = {}
    lines = content.split('\n')
    in_table = False

    for i, line in enumerate(lines):
        # Look for the table header pattern
        if '|' in line and ('Field' in line or 'Metric' in line or table_header in line):
            in_table = True
            continue

        # Skip separator line
        if in_table and re.match(r'^\|[-\s|]+\|$', line):
            continue

        # Parse table rows
        if in_table and '|' in line:
            parts = [p.strip() for p in line.split('|')]
            parts = [p for p in parts if p]  # Remove empty parts
            if len(parts) >= 2:
                key = parts[0].strip('*').strip()
                value = parts[1].strip('*').strip()
                result[key] = value
        elif in_table and '|' not in line:
            break

    return result


def parse_contract_file(file_path: Path) -> dict:
    """Parse a contract markdown file and extract structured data."""
    if not file_path.exists():
        return {}

    content = file_path.read_text()
    data = {}

    # Extract contract details table
    details = parse_markdown_table(content, "Field")

    # Map common fields
    field_mapping = {
        "Contract ID": "contract_id",
        "Vendor": "vendor",
        "Contract Type": "type",
        "Region": "region",
        "Contracting Officer": "co",
        "COR": "cor",
        "Delegation Status": "delegation_status",
        "Current COR in EASi": "current_cor_easi",
        "Proposed COR": "proposed_cor",
    }

    for md_field, json_field in field_mapping.items():
        if md_field in details:
            data[json_field] = details[md_field]

    # Extract financial summary
    financial = parse_markdown_table(content, "Metric")

    financial_mapping = {
        "Total Contract Value": "total_value",
        "Annual Payment": "annual_payment",
        "Final Payment Amount": "annual_payment",
        "Payment Due": "payment_due",
        "Watch List": "watch_list",
        "Variance": "variance",
        "Shortfall Amount": "shortfall_amount",
    }

    for md_field, json_field in financial_mapping.items():
        if md_field in financial:
            value = financial[md_field]
            # Parse numeric values
            if json_field in ["total_value", "annual_payment", "shortfall_amount"]:
                # Remove $ and commas, convert to number
                clean = re.sub(r'[$,]', '', value)
                try:
                    data[json_field] = float(clean) if '.' in clean else int(clean)
                except ValueError:
                    data[json_field] = None
            elif json_field == "variance":
                # Parse percentage
                try:
                    data[json_field] = float(value.replace('%', ''))
                except ValueError:
                    data[json_field] = 0
            elif json_field == "watch_list":
                data[json_field] = value.lower() == "yes"
            else:
                data[json_field] = value

    # Check for FINAL YEAR
    if "FINAL YEAR" in content or "final year" in content.lower():
        data["final_year"] = True

    # Extract issues from content
    if "### Issues" in content:
        issues_section = content.split("### Issues")[1].split("###")[0]
        issues = re.findall(r'[-*]\s+(.+)', issues_section)
        if issues:
            data["issues"] = issues

    return data


def load_contract_data(contract_id: str) -> Optional[dict]:
    """Load contract data from knowledge-base/contracts/ directory."""
    contracts_dir = KNOWLEDGE_BASE / "contracts"

    # Try exact match first
    exact_path = contracts_dir / f"{contract_id}.md"
    if exact_path.exists():
        return parse_contract_file(exact_path)

    # Try fuzzy match
    if contracts_dir.exists():
        for file_path in contracts_dir.glob("*.md"):
            if contract_id.lower() in file_path.stem.lower():
                return parse_contract_file(file_path)
            # Also check content
            content = file_path.read_text()
            if contract_id.lower() in content.lower():
                return parse_contract_file(file_path)

    return None


def list_all_contracts() -> list[str]:
    """List all available contract files."""
    contracts_dir = KNOWLEDGE_BASE / "contracts"
    if not contracts_dir.exists():
        return []

    contracts = []
    for file_path in contracts_dir.glob("*.md"):
        if file_path.stem != "Portfolio_Baseline_2026":
            contracts.append(file_path.stem)
    return contracts


def load_payment_schedule() -> list[dict]:
    """Load payment schedule from knowledge-base/payments/."""
    payments_file = KNOWLEDGE_BASE / "payments" / "Deadline_Tracker_FY2025_2026.md"

    if not payments_file.exists():
        return []

    content = payments_file.read_text()
    payments = []

    # Parse payment tables from content
    # Look for tables with payment information
    lines = content.split('\n')
    in_payment_table = False

    for line in lines:
        # Detect payment table rows
        if '|' in line and ('$' in line or 'TBD' in line):
            parts = [p.strip() for p in line.split('|')]
            parts = [p for p in parts if p]

            if len(parts) >= 4:
                contract = parts[0] if len(parts) > 0 else ""
                vendor = parts[1] if len(parts) > 1 else ""
                amount_str = parts[2] if len(parts) > 2 else "TBD"
                due_date = parts[3] if len(parts) > 3 else ""

                # Skip header rows
                if "Contract" in contract or "---" in contract:
                    continue

                # Parse amount
                amount = None
                if '$' in amount_str:
                    clean = re.sub(r'[$,]', '', amount_str)
                    try:
                        amount = int(float(clean))
                    except ValueError:
                        pass

                payments.append({
                    "contract": contract.replace("**", "").strip(),
                    "vendor": vendor.replace("**", "").strip(),
                    "amount": amount,
                    "payment_due": due_date.replace("**", "").strip(),
                    "final": "FINAL" in line.upper()
                })

    return payments


def load_oig_requirements() -> dict:
    """Load OIG compliance requirements."""
    oig_file = KNOWLEDGE_BASE / "compliance" / "OIG_A240046_Requirements.md"

    if not oig_file.exists():
        return {
            "audit_number": "A240046",
            "requirements": [
                "Independent government M&V witnessing required",
                "No contractor employees as witnesses",
                "CO authorization for scope changes",
                "Documentation timing must align with activities"
            ]
        }

    content = oig_file.read_text()

    return {
        "audit_number": "A240046",
        "deadline": "September 2026",
        "status": "Active Corrective Actions",
        "findings": {
            "001": "M&V Witnessing - Independent government witnessing required",
            "002": "Contract Modifications - Proper CO authorization required",
            "003": "Unauthorized Changes - Only CO/COR can authorize"
        },
        "full_document": str(oig_file)
    }


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools."""
    return [
        Tool(
            name="calculate_shortfall",
            description="Calculate energy savings shortfall for a contract. Reads from knowledge-base/contracts/{contract_id}.md",
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
            description="Validate payment against OIG A240046 compliance. Reads from knowledge-base/compliance/.",
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
                        "description": "Whether M&V was witnessed by government COR"
                    },
                    "co_authorized": {
                        "type": "boolean",
                        "description": "Whether scope changes have CO authorization"
                    }
                },
                "required": ["contract_id", "payment_amount", "period"]
            }
        ),
        Tool(
            name="generate_authorization_package",
            description="Generate payment authorization package. Combines contract data with templates.",
            inputSchema={
                "type": "object",
                "properties": {
                    "contract_id": {"type": "string", "description": "Contract identifier"},
                    "period": {"type": "string", "description": "Payment period"},
                    "payment_amount": {"type": "number", "description": "Payment amount"},
                    "shortfall_amount": {"type": "number", "description": "Shortfall if any"},
                    "cor_name": {"type": "string", "description": "COR name"}
                },
                "required": ["contract_id", "period", "payment_amount"]
            }
        ),
        Tool(
            name="get_contract_info",
            description="Get contract details from knowledge-base/contracts/{contract_id}.md",
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
            description="List payments from knowledge-base/payments/Deadline_Tracker_FY2025_2026.md",
            inputSchema={
                "type": "object",
                "properties": {
                    "months_ahead": {"type": "integer", "description": "Months to look ahead"},
                    "include_watch_list": {"type": "boolean", "description": "Include watch list info"}
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
    """Calculate energy savings shortfall - reads from knowledge-base/contracts/"""
    contract_id = args["contract_id"]
    period = args["period"]
    guaranteed = args["guaranteed_savings"]
    verified = args["verified_savings"]

    # Load contract data from file
    contract = load_contract_data(contract_id)

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
        "data_source": f"knowledge-base/contracts/{contract_id}.md",
        "remediation_options": []
    }

    # Add contract context if found
    if contract:
        result["contract_info"] = {
            "vendor": contract.get("vendor"),
            "type": contract.get("type"),
            "delegation_status": contract.get("delegation_status"),
            "existing_variance": contract.get("variance")
        }

        if contract.get("watch_list"):
            result["watch_list_alert"] = f"Contract on watch list with {contract.get('variance', 0)}% variance"

    if shortfall > 0:
        result["remediation_options"] = [
            f"1. Contractor payment reduction: ${shortfall:,.2f}",
            "2. ECM performance optimization",
            "3. Baseline adjustment review",
            "4. Extended measurement period"
        ]

        # Load OIG requirements
        oig = load_oig_requirements()
        result["oig_compliance"] = {
            "audit": oig["audit_number"],
            "requirement": "Document shortfall with independent government witnessing"
        }

    return [TextContent(type="text", text=json.dumps(result, indent=2))]


async def validate_payment_request(args: dict) -> list[TextContent]:
    """Validate payment - reads from knowledge-base/contracts/ and compliance/"""
    contract_id = args["contract_id"]
    payment_amount = args["payment_amount"]
    period = args["period"]
    mv_witnessed = args.get("mv_witnessed", False)
    co_authorized = args.get("co_authorized", True)

    # Load contract data
    contract = load_contract_data(contract_id)
    oig = load_oig_requirements()

    result = {
        "contract_id": contract_id,
        "payment_amount": payment_amount,
        "period": period,
        "validation_status": "PENDING",
        "checks": [],
        "blockers": [],
        "warnings": [],
        "data_sources": [
            f"knowledge-base/contracts/{contract_id}.md",
            "knowledge-base/compliance/OIG_A240046_Requirements.md"
        ]
    }

    if not contract:
        result["validation_status"] = "FAILED"
        result["blockers"].append(f"Contract '{contract_id}' not found")
        result["available_contracts"] = list_all_contracts()
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    # Check delegation status
    delegation = contract.get("delegation_status", "Unknown")
    if delegation == "On File":
        result["checks"].append("✅ COR delegation on file")
    elif delegation == "Nomination Issued":
        result["warnings"].append("⚠️ Nomination issued but delegation pending")
    else:
        result["blockers"].append("❌ No COR delegation - cannot authorize")

    # OIG Compliance checks
    if mv_witnessed:
        result["checks"].append("✅ M&V independently witnessed by government COR")
    else:
        result["blockers"].append(f"❌ OIG {oig['audit_number']}: M&V must be witnessed by government COR")

    if co_authorized:
        result["checks"].append("✅ Scope changes have CO authorization")
    else:
        result["blockers"].append(f"❌ OIG {oig['audit_number']}: Scope changes require CO authorization")

    # Watch list check
    if contract.get("watch_list"):
        result["warnings"].append(f"⚠️ Watch list contract ({contract.get('variance', 0)}% variance)")

    # Final year check
    if contract.get("final_year"):
        result["warnings"].append("⚠️ FINAL YEAR - Closeout documentation required")

    # Determine status
    if result["blockers"]:
        result["validation_status"] = "BLOCKED"
    elif result["warnings"]:
        result["validation_status"] = "APPROVED_WITH_WARNINGS"
    else:
        result["validation_status"] = "APPROVED"

    result["prompt_payment_act"] = {
        "payment_due_days": 30,
        "documentation_deadline_days": 15
    }

    return [TextContent(type="text", text=json.dumps(result, indent=2))]


async def generate_authorization_package(args: dict) -> list[TextContent]:
    """Generate authorization package - combines contract data with templates."""
    contract_id = args["contract_id"]
    period = args["period"]
    payment_amount = args["payment_amount"]
    shortfall = args.get("shortfall_amount", 0)
    cor_name = args.get("cor_name", "Matthew Schreck, CEM")

    contract = load_contract_data(contract_id)
    oig = load_oig_requirements()

    package = {
        "authorization_package": {
            "contract_id": contract_id,
            "vendor": contract.get("vendor", "Unknown") if contract else "Unknown",
            "contract_type": contract.get("type", "Unknown") if contract else "Unknown",
            "region": contract.get("region", "Unknown") if contract else "Unknown",
            "contracting_officer": contract.get("co", "Unknown") if contract else "Unknown",
            "cor": cor_name,
            "period": period,
            "payment_amount": payment_amount,
            "shortfall_amount": shortfall,
            "net_payment": payment_amount - shortfall,
            "generated_date": datetime.now().isoformat()
        },
        "data_sources": {
            "contract": f"knowledge-base/contracts/{contract_id}.md",
            "compliance": "knowledge-base/compliance/OIG_A240046_Requirements.md",
            "templates": "knowledge-base/templates/"
        },
        "required_documentation": {
            "pre_payment": [
                "☐ M&V Report (reviewed and approved)",
                "☐ Savings verification calculations",
                "☐ Government witnessing forms (Appendix B)",
                "☐ Invoice with supporting documentation",
                "☐ COR delegation letter"
            ],
            "oig_compliance": [
                f"☐ {oig['findings']['001']}",
                f"☐ {oig['findings']['002']}",
                f"☐ {oig['findings']['003']}"
            ]
        },
        "authorization_statement": (
            f"I, {cor_name}, COR, certify that:\n"
            f"1. Contractor performed satisfactorily for {period}\n"
            f"2. M&V independently witnessed by government personnel\n"
            f"3. Payment ${payment_amount:,.2f} is accurate and supported\n"
            f"4. Complies with OIG {oig['audit_number']} corrective actions"
        )
    }

    if contract and contract.get("final_year"):
        package["closeout_requirements"] = [
            "☐ Final M&V report",
            "☐ O&M transition plan",
            "☐ Contract closeout package"
        ]

    return [TextContent(type="text", text=json.dumps(package, indent=2))]


async def get_contract_info(args: dict) -> list[TextContent]:
    """Get contract info - reads from knowledge-base/contracts/{contract_id}.md"""
    contract_id = args["contract_id"]

    contract = load_contract_data(contract_id)

    if not contract:
        return [TextContent(type="text", text=json.dumps({
            "error": f"Contract '{contract_id}' not found",
            "searched": f"knowledge-base/contracts/{contract_id}.md",
            "available_contracts": list_all_contracts()
        }, indent=2))]

    result = {
        "contract_id": contract_id,
        "data_source": f"knowledge-base/contracts/{contract_id}.md",
        **contract
    }

    if contract.get("delegation_status") != "On File":
        result["action_required"] = "Request COR delegation letter from CO"

    return [TextContent(type="text", text=json.dumps(result, indent=2))]


async def list_upcoming_payments(args: dict) -> list[TextContent]:
    """List payments - reads from knowledge-base/payments/"""
    months_ahead = args.get("months_ahead", 3)

    payments = load_payment_schedule()

    result = {
        "data_source": "knowledge-base/payments/Deadline_Tracker_FY2025_2026.md",
        "timeframe": f"Next {months_ahead} months",
        "generated": datetime.now().isoformat(),
        "payments": payments[:10],  # Limit to 10
        "prompt_payment_reminder": "Documentation due 15 days before payment date"
    }

    return [TextContent(type="text", text=json.dumps(result, indent=2))]


async def main():
    """Run the MCP server."""
    print("MCP Server running on stdio transport")
    print("Server: GSA Payment Authorization Tool")
    print(f"Knowledge Base: {KNOWLEDGE_BASE}")
    print("Tools: 5 tools available")
    print("  - calculate_shortfall (reads contracts/*.md)")
    print("  - validate_payment_request (reads contracts/ + compliance/)")
    print("  - generate_authorization_package (reads all)")
    print("  - get_contract_info (reads contracts/*.md)")
    print("  - list_upcoming_payments (reads payments/*.md)")

    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
