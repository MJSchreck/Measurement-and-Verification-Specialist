# Quick Start Guide: MCP Payment Authorization Tool

**Goal**: Get your payment authorization tool running in Claude Desktop in 10 minutes.

## Prerequisites

1. Python 3.8 or higher installed
2. Claude Desktop app installed (download from claude.ai)
3. This project cloned/downloaded to your computer

## Step-by-Step Setup

### Step 1: Install Dependencies (2 minutes)

Open your terminal and run:

```bash
cd /path/to/your/project/mcp-servers/payment-authorization-tool
pip install -r requirements.txt
```

You should see:
```
Successfully installed mcp-1.1.0 python-dateutil-2.8.2
```

### Step 2: Test the Server (1 minute)

```bash
python server.py
```

Expected output:
```
MCP Server running on stdio transport
Server: GSA Payment Authorization Tool
Tools: 5 tools available
  - calculate_shortfall
  - validate_payment_request
  - generate_authorization_package
  - get_contract_info
  - list_upcoming_payments
```

Press `Ctrl+C` to stop the test.

### Step 3: Get Your Project Path (1 minute)

```bash
# macOS/Linux
pwd

# Windows
cd
```

Copy the full path. Example:
- macOS: `/Users/matt/Projects/Measurement-and-Verification-Specialist`
- Windows: `C:\Users\matt\Projects\Measurement-and-Verification-Specialist`

### Step 4: Configure Claude Desktop (3 minutes)

#### Find Your Config File

**macOS**:
```bash
open ~/Library/Application\ Support/Claude/
```

**Windows**:
```
%APPDATA%\Claude\
```

#### Edit claude_desktop_config.json

If the file doesn't exist, create it. Add this (replace the path):

```json
{
  "mcpServers": {
    "payment-authorization": {
      "command": "python",
      "args": [
        "/FULL/PATH/TO/YOUR/PROJECT/mcp-servers/payment-authorization-tool/server.py"
      ]
    }
  }
}
```

**CRITICAL**: Use the FULL path from Step 3 + `/mcp-servers/payment-authorization-tool/server.py`

Example (macOS):
```json
{
  "mcpServers": {
    "payment-authorization": {
      "command": "python",
      "args": [
        "/Users/matt/Projects/Measurement-and-Verification-Specialist/mcp-servers/payment-authorization-tool/server.py"
      ]
    }
  }
}
```

Example (Windows - note forward slashes):
```json
{
  "mcpServers": {
    "payment-authorization": {
      "command": "python",
      "args": [
        "C:/Users/matt/Projects/Measurement-and-Verification-Specialist/mcp-servers/payment-authorization-tool/server.py"
      ]
    }
  }
}
```

### Step 5: Restart Claude Desktop (1 minute)

1. Quit Claude Desktop completely (File -> Quit)
2. Reopen Claude Desktop
3. Look for the MCP indicator at the bottom of the interface

### Step 6: Test It! (2 minutes)

In Claude Desktop, try these:

**Test 1: List available tools**
```
Show me what MCP tools are available
```

**Test 2: Calculate a shortfall**
```
Calculate shortfall:
- Contract: NDER2_LA_Honeywell
- Period: 2025-Q2
- Guaranteed savings: $250,000
- Verified savings: $235,000
```

**Test 3: Validate a payment**
```
Validate payment request:
- Contract: NDER2_SD_Ameresco
- Amount: $1,684,326
- Period: 2025-Q2
- M&V witnessed: yes
- CO authorized: yes
```

**Test 4: Generate authorization package**
```
Generate payment authorization package:
- Contract: NDER2_SD_Ameresco
- Period: 2025-Q2
- Payment: $1,684,326
```

**Test 5: List upcoming payments**
```
List all payments due in the next 3 months
```

## Success Indicators

You'll know it's working when:
- MCP indicator appears in Claude Desktop
- Claude responds with structured JSON data
- Tool calls return contract-specific information

## Available Tools

| Tool | Purpose | Example Use |
|------|---------|-------------|
| `calculate_shortfall` | Calculate energy savings shortfall | Verify guaranteed vs actual savings |
| `validate_payment_request` | Check payment compliance | OIG compliance, delegation status |
| `generate_authorization_package` | Create authorization docs | Full payment package with checklists |
| `get_contract_info` | Retrieve contract details | Query portfolio by vendor/contract |
| `list_upcoming_payments` | Show payment calendar | Next 3 months of payments |

## Troubleshooting

### Problem: No MCP indicator appears

**Solution 1**: Check config file path
```bash
# macOS
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Windows
type %APPDATA%\Claude\claude_desktop_config.json
```

**Solution 2**: Check Claude Desktop logs
- macOS: `~/Library/Logs/Claude/`
- Windows: `%APPDATA%\Claude\logs\`

**Solution 3**: Try absolute Python path
```bash
# Find Python path
which python  # macOS/Linux
where python  # Windows
```

Use that in config:
```json
"command": "/usr/local/bin/python3",
```

### Problem: Import errors

**Solution**: Reinstall dependencies
```bash
pip install -r requirements.txt --force-reinstall
```

### Problem: Contract not found

**Solution**: Use exact contract IDs from this list:
- `NDER2_SD_Ameresco`
- `NDER2_SF_Honeywell`
- `NDER2_LA_Honeywell`
- `LA_ESPC_ABM`
- `UESC_SD_SDGandE`
- `PJKK_JCI`
- `McKinstry_R8`
- `UESC_Sansome_PGE`
- `ENABLE_Detroit_Honeywell`
- `NDER1_Chicago_Noresco`
- `ABM_ENABLE_R8`

## Contract Data

The tool includes your full portfolio baseline:

| Contract | Vendor | Value | Payment Due |
|----------|--------|-------|-------------|
| NDER2_SD_Ameresco | Ameresco | $53.6M | April 1 |
| LA_ESPC_ABM | ABM | $143.9M | May 1 |
| UESC_SD_SDGandE | SDG&E | $8.3M | May 1 |
| PJKK_JCI | JCI | Final | July 31 |
| McKinstry_R8 | McKinstry | $18.4M | Dec 31 |
| ENABLE_Detroit_Honeywell | Honeywell | $24.6M | March |

## OIG Compliance Features

All tools include OIG A240046 compliance checks:
- Independent government witnessing verification
- Scope change CO authorization
- Delegation status validation
- Watch list monitoring

## Next Steps

Once working, you can:

1. **Process real payments**: Use actual contract data
2. **Customize tools**: Edit `server.py` to add features
3. **Add more servers**: Create additional MCP tools
4. **Integrate with Claude Code**: Use both systems together

## Reference

- **Full README**: `/mcp-servers/README.md`
- **Project Overview**: `/README.md`
- **GSA AI Assistant Index**: `/GSA_AI_Assistant_Document_Index.md`
- **Portfolio Baseline**: `/Contract_Portfolio_Baseline_2026.md`

---

**Total Setup Time**: ~10 minutes
**Difficulty**: Easy
**Support**: Check Claude Desktop logs for detailed errors
