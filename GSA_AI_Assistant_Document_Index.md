# GSA AI Assistant - Document Index
## Measurement & Verification Specialist Knowledge Base

**Repository:** Measurement-and-Verification-Specialist
**Branch:** claude/cpars-qtr2-questions-FHm5Z
**Owner:** Matthew Schreck, CEM
**Role:** Energy Program Specialist / Zone C M&V Specialist
**Organization:** GSA Office of Facilities Management - Energy Division
**Last Updated:** February 2026

---

## PURPOSE

This index catalogs all documents in this repository for integration with GSA AI assistants. Each document serves a specific function in COR (Contracting Officer's Representative) operations for ESPC/UESC contract management.

---

## DOCUMENT INVENTORY

### 1. README.md
| Field | Value |
|-------|-------|
| **Purpose** | Repository description |
| **Type** | Administrative |
| **Size** | 61 bytes |
| **AI Use Case** | Repository identification |

---

### 2. CPARS_QTR2_Questions.md
| Field | Value |
|-------|-------|
| **Purpose** | Generic CPARS quarterly assessment questionnaire |
| **Type** | Assessment Template |
| **Size** | ~12 KB |
| **Framework** | CPARS 2023 Edition, FAR 42.1503 |

**Key Data Points for AI:**
- 5-tier rating scale (Exceptional → Unsatisfactory)
- 7 evaluation areas: Quality, Schedule, Cost Control, Management, Small Business, Regulatory, Other
- Supporting documentation checklists
- Assessment certification fields

**AI Use Cases:**
- Generate blank CPARS assessments
- Reference rating definitions
- Identify required documentation
- Structure performance evaluations

---

### 3. CPARS_QTR2_ENABLE_Detroit_Honeywell.md
| Field | Value |
|-------|-------|
| **Purpose** | Contract-specific CPARS for ENABLE Detroit |
| **Type** | Assessment Template (Contract-Specific) |
| **Contractor** | Honeywell |
| **Region** | R5 |
| **CO** | Jerrud Parker |
| **Value** | $24,670,720 |
| **Current COR** | Joseph Blake |

**Key Data Points for AI:**
- ENABLE program characteristics (streamlined M&V)
- Pre-populated contract metadata
- OIG A240046 compliance checkpoints
- COR transition tracking (from Joseph Blake)

**AI Use Cases:**
- Generate ENABLE-specific assessments
- Track COR transition status
- Monitor OIG compliance
- Reference ENABLE M&V procedures

---

### 4. CPARS_QTR2_NDER1_Chicago_Noresco.md
| Field | Value |
|-------|-------|
| **Purpose** | Contract-specific CPARS for NDER1 Chicago |
| **Type** | Assessment Template (Contract-Specific) |
| **Contractor** | Noresco |
| **Region** | R5 |
| **CO** | Krystal Blue |
| **Current COR** | Kendra Rudder |

**Key Data Points for AI:**
- NDER program characteristics (30%+ energy reduction target)
- Deep energy retrofit performance metrics
- ECM-by-ECM analysis structure
- Baseline adjustment requirements
- OIG A240046 compliance checkpoints

**AI Use Cases:**
- Generate NDER-specific assessments
- Calculate energy savings vs. targets
- Track deep retrofit performance
- Monitor ECM-level compliance

---

### 5. Contract_Portfolio_Baseline_2026.md
| Field | Value |
|-------|-------|
| **Purpose** | Complete COR contract portfolio baseline |
| **Type** | Portfolio Management |
| **Effective Date** | January 1, 2026 |
| **Portfolio Value** | $300M+ |
| **Contract Count** | 15+ |

**Key Data Points for AI:**
- Three-tier delegation structure:
  - Tier 1: Delegation On File (4 contracts)
  - Tier 2: Nomination Issued (5 contracts)
  - Tier 3: No Delegation (5 contracts)
- Payment calendar with amounts and due dates
- Watch list contracts with performance issues
- Key contacts (COs, CORs, contractors)
- OIG A240046 compliance requirements

**AI Use Cases:**
- Query contract details by vendor, region, or type
- Check delegation status for any contract
- Identify upcoming payment deadlines
- Flag watch list issues
- Route requests to correct CO/COR

**Contract Data Structure:**
```
For each contract:
- Vendor name
- Contract type (ESPC, UESC, ENABLE, NDER)
- Region (R5, R8, R9)
- Contracting Officer
- Total value
- Delegation status
- Payment due date
- Watch list status
- Action items
```

---

### 6. COR_Delegation_Request_Templates.md
| Field | Value |
|-------|-------|
| **Purpose** | Email templates for COR delegation requests |
| **Type** | Communication Templates |
| **Template Count** | 9 templates + follow-up |

**Key Data Points for AI:**
- Priority matrix (HIGH/MEDIUM/TRANSITION)
- 9 contract-specific templates
- Tracking log structure
- Follow-up template

**Template Coverage:**
| Priority | Contract | CO |
|----------|----------|----|
| HIGH | PJKK | Miles Conant |
| HIGH | NDER2 SD | Felipe Jolles |
| MEDIUM | NDER2 LA | Heidi Johnson |
| MEDIUM | LA ESPC | Heidi Johnson |
| MEDIUM | UESC Sansome | Felipe Jolles |
| TRANSITION | ENABLE Detroit | Jerrud Parker |
| TRANSITION | Harold Washington | Jerrud Parker |
| TRANSITION | NDER1 Chicago | Krystal Blue |
| TRANSITION | NDER1 Battle Creek | Miles Conant |

**AI Use Cases:**
- Generate delegation request emails
- Track delegation request status
- Identify priority delegation gaps
- Create follow-up reminders

---

### 7. Payment_Deadline_Tracker_FY2025_2026.md
| Field | Value |
|-------|-------|
| **Purpose** | Payment calendar with documentation deadlines |
| **Type** | Financial Tracking |
| **Fiscal Years** | FY2025-FY2026 |
| **Total FY2025 Payments** | $6,441,836+ |

**Key Data Points for AI:**
- Prompt Payment Act requirements (30-day rule)
- Documentation deadline formula (15 days before payment)
- Monthly payment calendar
- Per-payment task checklists
- Delegation status by payment
- Watch list payment impacts
- 90-day action queue

**AI Use Cases:**
- Query upcoming payment deadlines
- Generate payment preparation checklists
- Calculate documentation deadlines
- Flag payments at risk
- Track OIG compliance for payments

**Payment Data Structure:**
```
For each payment:
- Contract name
- Vendor
- Amount
- Payment due date
- Documentation deadline
- Delegation status
- Action items
- Status (pending/complete)
```

---

## AI ASSISTANT INTEGRATION GUIDE

### Query Patterns

**Contract Queries:**
- "What is the delegation status for [contract]?"
- "When is the next payment for [vendor]?"
- "What are the watch list issues for [contract]?"
- "Who is the CO for [contract]?"

**Deadline Queries:**
- "What payments are due this month?"
- "What documentation is due this week?"
- "When is the PJKK contract closeout?"

**Template Queries:**
- "Generate a delegation request for [contract]"
- "Create a CPARS assessment for [contractor]"
- "What are the OIG compliance requirements?"

**Portfolio Queries:**
- "Show all Tier 1 delegation contracts"
- "List all Honeywell contracts"
- "What is the total portfolio value?"

### Cross-Reference Map

| If user asks about... | Reference document(s) |
|-----------------------|----------------------|
| CPARS rating definitions | CPARS_QTR2_Questions.md |
| Contract-specific CPARS | CPARS_QTR2_[Contract].md |
| Delegation status | Contract_Portfolio_Baseline_2026.md |
| Request delegation | COR_Delegation_Request_Templates.md |
| Payment deadlines | Payment_Deadline_Tracker_FY2025_2026.md |
| OIG compliance | All documents (section: OIG A240046) |
| Watch list | Contract_Portfolio_Baseline_2026.md |
| Contact information | Contract_Portfolio_Baseline_2026.md |

### Key Entities

**Contracting Officers:**
| Name | Contracts |
|------|-----------|
| Felipe Jolles | NDER2 SD, UESC SD, UESC Sansome, ABM ENABLE, McKinstry |
| Heidi Johnson | NDER2 SF, NDER2 LA, LA ESPC |
| Miles Conant | PJKK, NDER1 Battle Creek |
| Krystal Blue | PF EMP2, NDER1 Chicago |
| Jerrud Parker | Harold Washington, ENABLE Detroit |

**Contractors:**
| Contractor | Contract Types |
|------------|----------------|
| Honeywell | NDER2 SF, NDER2 LA, ENABLE Detroit |
| Ameresco | NDER2 SD, Harold Washington |
| ABM Industries | LA ESPC, ABM ENABLE R8 |
| McKinstry | McKinstry DFC & Mt Plains |
| Johnson Controls | PJKK |
| Noresco | NDER1 Chicago |
| Trane | NDER1 Battle Creek |
| SDG&E | UESC San Diego |
| PG&E | UESC Sansome |

**Current CORs (Transition):**
| COR | Contract | Status |
|-----|----------|--------|
| Joseph Blake | ENABLE Detroit | Transitioning to Matt |
| Johnny Zuzic | Harold Washington | Transitioning to Matt |
| Kendra Rudder | NDER1 Chicago | Transitioning to Matt |
| Michelle Munroe | NDER1 Battle Creek | Transitioning to Matt |

---

## COMPLIANCE FRAMEWORK

### OIG Audit A240046
**Status:** Active Corrective Actions through September 2026

**Critical Requirements (apply to ALL documents):**
1. Independent government witnessing for M&V activities
2. No contractor employees as government witnesses
3. Witnessing form timing must match activities
4. All scope changes require CO authorization

### FAR References
- FAR 42.1502 - Policy (Performance evaluations)
- FAR 42.1503 - Procedures (CPARS ratings)
- 5 CFR 1315 - Prompt Payment Act

### DOE/FEMP Standards
- DOE FEMP M&V Guidelines v4.0
- IPMVP Protocol (2022)

---

## VERSION CONTROL

| Date | Version | Files Added/Modified | Commit |
|------|---------|---------------------|--------|
| 2026-02-02 | 1.0 | Initial: README.md | 2fb9c63 |
| 2026-02-02 | 1.1 | CPARS_QTR2_Questions.md | 8138410 |
| 2026-02-02 | 1.2 | Contract_Portfolio_Baseline_2026.md | b73a100 |
| 2026-02-02 | 1.3 | CPARS ENABLE Detroit, NDER1 Chicago, Delegation Templates, Payment Tracker, This Index | [Current] |

---

## FILE STATISTICS

| Metric | Value |
|--------|-------|
| Total Files | 8 |
| Total Size | ~50 KB |
| Document Types | 4 (Admin, Templates, Portfolio, Tracking) |
| Contracts Covered | 15+ |
| Templates Available | 12+ |

---

## MCP INTEGRATION OPPORTUNITIES

### Potential Custom Skills
1. **Payment Processor** - Query deadlines, generate checklists
2. **CPARS Generator** - Create contract-specific assessments
3. **Delegation Tracker** - Monitor and request delegations
4. **Compliance Monitor** - Track OIG A240046 requirements
5. **Portfolio Dashboard** - Real-time contract status

### Data Connections
- Gmail: Contractor correspondence
- Asana: Task management
- Notion: Strategic documentation
- Google Drive: Contract files
- Sentry: Error monitoring (for integrations)

---

*This index enables AI assistants to navigate the M&V Specialist knowledge base and provide accurate, context-aware responses for COR operations.*
