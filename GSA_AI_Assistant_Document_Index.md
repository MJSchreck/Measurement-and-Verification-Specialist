# GSA AI Assistant - Document Index
## Measurement & Verification Specialist Knowledge Base

**Repository:** Measurement-and-Verification-Specialist
**Owner:** Matthew Schreck, CEM
**Role:** Energy Program Specialist / Zone C M&V Specialist
**Organization:** GSA Office of Facilities Management - Energy Division
**Last Updated:** February 2026

---

## Repository Structure

```
Measurement-and-Verification-Specialist/
├── README.md                              # Project overview
├── GSA_AI_Assistant_Document_Index.md     # This file
│
├── knowledge-base/
│   ├── contracts/                         # Contract-specific data
│   │   ├── Portfolio_Baseline_2026.md     # Master portfolio
│   │   ├── NDER2_LA_Honeywell.md
│   │   ├── NDER2_SD_Ameresco.md
│   │   ├── ENABLE_Detroit_Honeywell.md
│   │   └── PJKK_JCI.md
│   │
│   ├── payments/                          # Payment tracking
│   │   └── Deadline_Tracker_FY2025_2026.md
│   │
│   ├── templates/                         # Reusable templates
│   │   ├── cpars/
│   │   │   ├── Generic_Questions.md
│   │   │   ├── ENABLE_Detroit_Honeywell.md
│   │   │   └── NDER1_Chicago_Noresco.md
│   │   └── correspondence/
│   │       └── Delegation_Request_Templates.md
│   │
│   ├── compliance/                        # Regulatory requirements
│   │   └── OIG_A240046_Requirements.md
│   │
│   └── m-v-reports/                       # M&V report storage
│       └── (PDF files go here)
│
└── mcp-servers/                           # Automation tools
    └── payment-authorization-tool/
        ├── server.py
        ├── requirements.txt
        └── QUICKSTART.md
```

---

## Document Inventory

### Contract Data (`knowledge-base/contracts/`)

| File | Purpose | Key Data |
|------|---------|----------|
| `Portfolio_Baseline_2026.md` | Master portfolio | All 15+ contracts, $300M+ value |
| `NDER2_LA_Honeywell.md` | Contract details | -7.5% variance, watch list |
| `NDER2_SD_Ameresco.md` | Contract details | $53.6M, April payment |
| `ENABLE_Detroit_Honeywell.md` | Contract details | $24.6M, R5 transition |
| `PJKK_JCI.md` | Contract details | FINAL YEAR, July closeout |

### Payment Tracking (`knowledge-base/payments/`)

| File | Purpose | Key Data |
|------|---------|----------|
| `Deadline_Tracker_FY2025_2026.md` | Payment calendar | $6.4M+ scheduled payments |

### Templates (`knowledge-base/templates/`)

| File | Purpose |
|------|---------|
| `cpars/Generic_Questions.md` | Base CPARS questionnaire |
| `cpars/ENABLE_Detroit_Honeywell.md` | ENABLE-specific CPARS |
| `cpars/NDER1_Chicago_Noresco.md` | NDER1-specific CPARS |
| `correspondence/Delegation_Request_Templates.md` | 9 email templates |

### Compliance (`knowledge-base/compliance/`)

| File | Purpose | Key Data |
|------|---------|----------|
| `OIG_A240046_Requirements.md` | OIG audit compliance | Through Sept 2026 |

---

## AI Query Patterns

### Contract Queries
```
"What is the status of NDER2 LA?"
→ knowledge-base/contracts/NDER2_LA_Honeywell.md

"Show me all watch list contracts"
→ knowledge-base/contracts/Portfolio_Baseline_2026.md (Watch List section)

"What's the delegation status for ENABLE Detroit?"
→ knowledge-base/contracts/ENABLE_Detroit_Honeywell.md
```

### Payment Queries
```
"When is the next payment due?"
→ knowledge-base/payments/Deadline_Tracker_FY2025_2026.md

"What documentation is needed for NDER2 SD payment?"
→ knowledge-base/payments/Deadline_Tracker_FY2025_2026.md (April section)
```

### Template Queries
```
"Generate a CPARS for Honeywell"
→ knowledge-base/templates/cpars/ENABLE_Detroit_Honeywell.md

"Draft a delegation request for PJKK"
→ knowledge-base/templates/correspondence/Delegation_Request_Templates.md
```

### Compliance Queries
```
"What are the OIG requirements?"
→ knowledge-base/compliance/OIG_A240046_Requirements.md

"Can contractor employees witness M&V?"
→ knowledge-base/compliance/OIG_A240046_Requirements.md (Finding 001)
```

---

## MCP Tool Integration

### Available Tools

| Tool | Data Source |
|------|-------------|
| `calculate_shortfall` | Contract variance data |
| `validate_payment_request` | OIG compliance requirements |
| `generate_authorization_package` | Templates + contract data |
| `get_contract_info` | Contract files |
| `list_upcoming_payments` | Payment tracker |

### Tool-to-Document Mapping

| Tool Call | Documents Referenced |
|-----------|---------------------|
| `calculate_shortfall(NDER2_LA)` | `contracts/NDER2_LA_Honeywell.md` |
| `validate_payment_request(...)` | `compliance/OIG_A240046_Requirements.md` |
| `generate_authorization_package(...)` | All payment + template docs |

---

## Key Entities

### Contracting Officers

| CO | Contracts | Contact For |
|----|-----------|-------------|
| Felipe Jolles | NDER2 SD, UESC SD, McKinstry | Delegation requests |
| Heidi Johnson | NDER2 SF, NDER2 LA, LA ESPC | Delegation requests |
| Miles Conant | PJKK, NDER1 Battle Creek | Delegation requests |
| Krystal Blue | NDER1 Chicago, PF EMP2 | Delegation requests |
| Jerrud Parker | ENABLE Detroit, Harold Washington | Delegation requests |

### Contractors

| Contractor | Contracts | Key Contact |
|------------|-----------|-------------|
| Honeywell | NDER2 SF/LA, ENABLE Detroit | Stacy Garvey (TRM) |
| Ameresco | NDER2 SD, Harold Washington | Amanda Hustrulid |
| ABM | LA ESPC, ENABLE R8 | - |
| McKinstry | DFC & Mt Plains | Sarah Eldehni |
| Johnson Controls | PJKK | - |
| Noresco | NDER1 Chicago | - |

### COR Transitions

| From | To | Contract |
|------|----|---------|
| Joseph Blake | Matthew Schreck | ENABLE Detroit |
| Johnny Zuzic | Matthew Schreck | Harold Washington |
| Kendra Rudder | Matthew Schreck | NDER1 Chicago |
| Michelle Munroe | Matthew Schreck | NDER1 Battle Creek |

---

## Compliance Framework

### OIG A240046 (Active)
- **Deadline:** September 2026
- **Key File:** `knowledge-base/compliance/OIG_A240046_Requirements.md`
- **Requirements:**
  1. Independent government M&V witnessing
  2. No contractor witnesses
  3. CO authorization for scope changes
  4. Documentation timing alignment

### Referenced in ALL:
- Contract files
- Payment authorizations
- CPARS templates
- MCP tool validations

---

## Usage Guidelines

### For Claude.ai Projects
1. Upload entire `knowledge-base/` folder to Project Knowledge
2. Reference specific files in prompts
3. Use MCP tools for automated workflows

### For Claude Code
1. Open repository as working directory
2. Reference files with relative paths
3. Use MCP server for payment automation

### For Other AI Assistants
1. Import Markdown files as context
2. Follow query patterns above
3. Cross-reference using this index

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-02-02 | 1.0 | Initial structure |
| 2026-02-02 | 2.0 | Reorganized to knowledge-base structure |

---

*This index enables AI assistants to navigate the M&V Specialist knowledge base efficiently.*
