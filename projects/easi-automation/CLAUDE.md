# EASi Automation

## Context

Automation scripts for EASi (ESPC contract management system) workflows, focusing on Receiving Report (RR) and invoice processing.

### Goal
60% reduction in invoice processing time through automated field extraction and validation.

## Document Retrieval

Search Google Drive for:
- `"SOP" AND "EASi"` — Standard operating procedures
- `"GSA PBS ESPC EASi Procedures"`
- `"receiving report" AND "template"`
- `"Pegasys" AND "validation"`

## Directory Structure

```
/easi-automation
├── CLAUDE.md           # This file
├── /retrieved_docs     # SOPs, templates, examples
└── /scripts            # Automation scripts
```

## Key Systems

| System | Purpose |
|--------|---------|
| **EASi** | ESPC contract management, RR creation |
| **Pegasys** | GSA financial system, invoice processing |

## Automation Opportunities

### Invoice Processing
- Extract vendor, amount, period from invoice PDF
- Generate EASi RR fields based on SOP
- Validate against contract terms

### RR Workflow
- Pre-fill receiving report from invoice data
- Flag validation failures (like stuck RR EC2025123000147)
- Track processing status

## Scripts to Build

- [ ] `invoice_parser.py` — Extract fields from invoice PDFs
- [ ] `rr_generator.py` — Generate EASi RR field values
- [ ] `pegasys_validator.py` — Check for Pegasys validation issues
- [ ] `status_tracker.py` — Track RR/invoice pipeline

## Reference: Common Validation Failures

- Duplicate invoice numbers
- Mismatched contract/task order numbers
- Period of performance errors
- Amount discrepancies
