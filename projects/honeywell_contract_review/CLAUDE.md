# Honeywell Contract Review Project

## Purpose

Dedicated workspace for managing Honeywell ESPC contracts (NDER2 SF and NDER2 LA).

## Contracts

| Contract | Contract Number | Location | CO | EMP2 Support |
|----------|-----------------|----------|----|--------------|
| NDER2 SF | GS-P-08-16-JE-7140 | San Francisco | Patrick Chapman | David Frank |
| NDER2 LA | DEAM3609GO29035, Order GS-P-08-16-JE-7081 | Los Angeles | Patrick Chapman | David Frank |

## Key Contacts

- **Stacy Garvey** - Honeywell PM (stacy.garvey@honeywell.com)
- **Aamer Athar** - Honeywell (aamer.athar@honeywell.com)
- **Patrick Chapman** - GSA CO (patrick.chapman@gsa.gov)
- **David Frank** - EMP2 (david.frank@emp2.com)

## Document Retrieval

When searching Google Drive for contract documents:

### NDER2 SF (7140)
- `"7140" AND "M&V report"`
- `"Honeywell" AND "annual report" AND "2024 OR 2025"`
- `"NDER2 SF" AND "Year 6"`
- `"GS-P-08-16-JE-7140"`

### NDER2 LA (7081)
- `"7081" AND "M&V report"`
- `"NDER2 LA" AND "Honeywell"`
- `"DEAM3609GO29035"`

## Directory Structure

```
/honeywell_contract_review
├── CLAUDE.md           # This file
├── /retrieved_docs     # M&V reports pulled from Drive
├── /analysis           # Working calculations
└── /outputs            # Review notes, action items, memos
```

## Current Issues

### NDER2 SF
- Year 6 M&V review in progress
- Annual billing restructure proposal (eliminate monthly Pegasys validations)
- Known shortfalls: $95K total (801 I St RCx $6,421, Ryan VAV $4,205)
- Stuck RR EC2025123000147 ($12,543.59) - duplicate invoice deletion

### NDER2 LA
- Active monitoring
- Standard M&V cycle

## Recurring Meetings

- **GSA-TRM and M&V Review** - Weekly, Thursday 1:00 PM
  - Attendees: Patrick Chapman, Stacy Garvey, David Frank

## Workflow

1. Query corpus for Honeywell-specific documents
2. Place in `/retrieved_docs`
3. Review and analyze
4. Document findings in `/outputs`
