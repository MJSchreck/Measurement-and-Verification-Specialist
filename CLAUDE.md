# CLAUDE.md

## Project Overview

**Cyborg Workflow System** for Matt Schreck, GSA Energy Division Zone 7 M&V Lead.

This project supports AI-assisted management of a $286M ESPC/UESC contract portfolio (16 contracts) following an 80% team reduction. The system integrates Claude AI with Asana, Gmail, Google Drive, and Calendar to maintain 100% operational effectiveness as a solo COR.

## Role Context

- **User:** Matt Schreck
- **Position:** Zone 7 M&V Lead, GSA PBS Energy Division
- **Supervisor:** Nathan Ingersoll
- **Portfolio:** 16 contracts, $286M total value
- **Key Achievement:** 100% witnessing rate (vs 38% national average), zero PPA violations

## Contract Portfolio

### Primary Contracts (Zone 7)

| Contract | Vendor | Type | Status |
|----------|--------|------|--------|
| NDER2 SF | Honeywell | ESPC | Active - Year 6 M&V |
| NDER2 SD | Ameresco | ESPC | 4-year M&V delay, Years 5/6/7 pending |
| NDER2 LA | Honeywell | ESPC | Active |
| PJKK Hawaii | Johnson Controls | ESPC | Final year (Year 15), closeout prep |
| ABM LA Consolidated | ABM Industries | ESPC | BESS settlement $6.68M ongoing |
| McKinstry DFC | McKinstry | ESPC | PR mod issues |

### Contract Types

- **ESPC** - Energy Savings Performance Contract
- **UESC** - Utility Energy Service Contract
- **PPA** - Power Purchase Agreement

### Budget Activities

- **PG61** - Primary budget activity code for energy contracts

## Key Systems & Tools

| System | Purpose |
|--------|---------|
| **Pegasys** | GSA financial system, invoice processing |
| **EASi** | ESPC contract management system |
| **CPARS** | Contractor Performance Assessment Reporting System |
| **GSA-TRM** | Technical Review Meeting system |
| **Google Workspace** | Docs, Drive, Calendar, Gmail |
| **Asana** | Task and project management |

## Key Contacts

### GSA Internal
- **Nathan Ingersoll** - Supervisor (nathan.ingersoll@gsa.gov)
- **Patrick Chapman** - CO/M&V Lead, NDER2 SF (patrick.chapman@gsa.gov)
- **Felipe Jolles** - CO, NDER2 SD/McKinstry/ENABLE (felipe.jolles@gsa.gov)
- **Heidi Johnson** - CO, ABM LA (heidi.johnson@gsa.gov)
- **Kirk Doll** - M&V Team Lead, R4 (kirk.doll@gsa.gov)
- **Tyler Cooper** - R8 Lead (tyler.cooper@gsa.gov)
- **Sarah Wenninger** - PBS AI/Innovation (sarah.wenninger@gsa.gov)

### Contractors/Partners
- **David Frank** - EMP2, Honeywell contracts (david.frank@emp2.com)
- **David Berezovskiy** - EMP2, PJKK Hawaii (davidb@emp2.com)
- **Stacy Garvey** - Honeywell PM (stacy.garvey@honeywell.com)
- **Bryan Thomas** - ABM PM (bryan.thomas@abm.com)
- **Greg Caplan** - Ameresco (gcaplan@ameresco.com)
- **Delaney Crain** - JCI (delaney.crain@jci.com)

## Recurring Meetings

| Meeting | Frequency | Day/Time |
|---------|-----------|----------|
| Energy M&V Team Meet | Weekly | Mon 8:30 AM |
| ESPC Project Branch | Bi-weekly | Mon 9:30 AM |
| R8 NDER6 Weekly | Weekly | Tue 10:00 AM |
| NCR NDER 7.1 Weekly | Weekly | Tue 11:00 AM |
| Gap PF Services | Bi-weekly | Wed 11:00 AM |
| ABM Phase 2B | Weekly | Wed 12:00 PM |
| MUSE Office Hours | Weekly | Thu 9:00 AM |
| Matt/Nathan Check-In | Bi-weekly | Thu 12:00 PM |
| GSA-TRM and M&V Review | Weekly | Thu 1:00 PM |

## Domain Terminology

- **M&V** - Measurement and Verification (energy savings validation)
- **COR** - Contracting Officer's Representative
- **CO** - Contracting Officer
- **RR** - Receiving Report (invoice approval)
- **PY** - Performance Year
- **RIF** - Reduction in Force
- **FEMP** - Federal Energy Management Program
- **BESS** - Battery Energy Storage System
- **RCx** - Retrocommissioning
- **VAV** - Variable Air Volume

## Cyborg Workflow Principles

1. **AI does research/drafts, human makes decisions**
2. **Morning briefings generated automatically**
3. **Contract context pulled in seconds**
4. **Knowledge persists across sessions**
5. **60% reduction in invoice processing time**

## Project Structure

```
/
├── CLAUDE.md                 # Project instructions and context
├── README.md                 # Project description
├── corpus/                   # Document corpus for RAG
│   ├── raw_documents/        # Source documents (PDFs, DOCX, etc.)
│   ├── embeddings/           # Vector store (Chroma, Pinecone, etc.)
│   ├── index_builder.py      # One-time indexing script
│   └── query_service.py      # API to retrieve relevant chunks
└── projects/                 # Task-specific workspaces
    ├── espc_mv_analysis/     # M&V report analysis
    │   ├── CLAUDE.md         # Project context
    │   ├── retrieved_docs/   # Docs pulled from corpus
    │   └── outputs/          # Analysis results
    └── honeywell_contract_review/
        ├── CLAUDE.md         # Project context
        ├── retrieved_docs/   # Contract docs
        └── outputs/          # Review outputs
```

## Commands

### Corpus Indexing (one-time or periodic)
```bash
# Index all documents in the corpus
claude-code "Index all documents in /corpus/raw_documents using text-embedding-3-small"

# Re-index after adding new documents
claude-code "Update the corpus index with new documents added since last indexing"
```

### Project Workflows
```bash
# Query corpus and analyze in a project context
claude-code "Query the corpus for all M&V reports from 2024-2025,
             copy relevant docs to /retrieved_docs,
             then analyze savings shortfalls"

# Contract-specific queries
claude-code "Find all NDER2 SF Year 6 documents, summarize key findings"

# Generate outputs
claude-code "Review retrieved_docs and draft a memo on baseline adjustment issues"
```

### Build/Test
No build or test commands configured yet.

## Conventions

- **Branch naming:** `claude/<description>-<id>` for AI-assisted development branches
- **Git author:** MJSchreck (mattschreck.energy@gmail.com)
- **Fiscal Years:** FY runs Oct 1 - Sep 30 (FY2025 = Oct 2024 - Sep 2025)
- **AWS:** Alternate Work Schedule - every other Friday off
