# EASi Receiving Report Automation

## Purpose

Streamline the EASi receiving report creation and Pegasys validation process for ESPC/UESC invoice processing. Goal: Reduce manual data entry errors and accelerate payment cycles.

## Current Pain Points

1. Manual transcription of invoice data into EASi fields
2. Pegasys validation failures requiring troubleshooting
3. Aging invoice notifications (25-day warnings)
4. Multiple PR modifications needed for payment schedule changes

## Key Reference Documents

Retrieve from Drive:
```
"SOP" AND "EASi" AND "ESPC"
"receiving report" AND "procedure"
"Pegasys" AND "validation"
```

Primary SOP: https://docs.google.com/document/d/1TwM2Upff57_FbVn1_SggkwCqZP0ZRkeWVueJRmFzbJs/edit

## Workflow to Automate

### Current Manual Process
1. Receive invoice from contractor/financier
2. Open EASi and create new RR
3. Manually enter:
   - Contract number
   - PR number
   - CLIN/SLIN
   - Amount
   - Period of performance
   - Certification statement
4. Submit for Pegasys validation
5. If validation fails → troubleshoot and resubmit
6. Route for approval

### Target Automated Process
1. Drop invoice PDF into intake folder
2. Script extracts key fields via OCR/parsing
3. Generates EASi-ready data file
4. User reviews and submits
5. Automated validation check before submission

## Technical Approach

### Option A: PDF Parsing Script
```python
# Pseudocode
def process_invoice(pdf_path):
    # Extract text from PDF
    text = extract_pdf_text(pdf_path)

    # Parse key fields
    invoice_data = {
        'contract_number': find_pattern(text, CONTRACT_REGEX),
        'invoice_number': find_pattern(text, INVOICE_REGEX),
        'amount': find_pattern(text, AMOUNT_REGEX),
        'period': find_pattern(text, PERIOD_REGEX),
    }

    # Validate against PR data
    validate_against_pr(invoice_data)

    # Generate EASi input
    return format_for_easi(invoice_data)
```

### Option B: Claude-Assisted Processing
Use Claude to read invoice PDFs and extract structured data, then validate against contract terms before EASi entry.

## Invoice Types to Handle

| Type | Frequency | Complexity |
|------|-----------|------------|
| Debt Service (Principal + Interest) | Annual | Medium |
| Performance Period Payment | Annual | High (M&V dependent) |
| Construction Progress | As incurred | Low |
| Modifications | As needed | Variable |

## Validation Rules

Before submitting to Pegasys, verify:
- [ ] Contract number matches active contract
- [ ] PR number exists and has available funds
- [ ] CLIN/SLIN matches payment schedule
- [ ] Amount matches invoice exactly
- [ ] Period of performance is valid
- [ ] No duplicate RR for same invoice

## Common Pegasys Errors

| Error | Cause | Fix |
|-------|-------|-----|
| "Invalid obligation" | PR funds exhausted | Request PR mod |
| "Period closed" | Fiscal year mismatch | Adjust dates |
| "Duplicate document" | RR already exists | Check history |
| "Amount exceeds limit" | Over PR ceiling | Split or modify |

## Gmail Monitoring

Set up search for invoice notifications:
```
from:zone3.receiving.reports@gsa.gov
subject:"Days Old Invoice"
from:easi.admin@gsa.gov subject:"Validation Failed"
```

## Directory Structure

```
/easi-automation
├── CLAUDE.md           # This file
├── /retrieved_docs     # SOPs, templates, sample invoices
└── /scripts            # Automation scripts
    ├── invoice_parser.py
    ├── rr_generator.py
    ├── pegasys_validator.py
    └── status_tracker.py
```

## Deliverables

1. [ ] Invoice field extraction script
2. [ ] Validation rules engine
3. [ ] EASi data formatter
4. [ ] Error handling procedures
5. [ ] User guide

## Testing

Test with recent invoices:
- MassMutual $1M (NDER2 LA)
- TRM monthly invoice
- McKinstry RR (today's task)
