# GSA Energy M&V Specialist

Cyborg Workflow System for GSA Energy Division Zone 7 M&V Lead.

## Overview

AI-assisted management of a $286M ESPC/UESC contract portfolio (16 contracts) using Claude Code integrated with Google Drive, Asana, Gmail, and Calendar.

## Quick Start

```bash
# 1. Run setup
chmod +x setup.sh && ./setup.sh

# 2. Start a project
cd projects/honeywell_7140_shortfall
claude "Search Drive for 7140 M&V report and analyze the $95K shortfall"
```

## Project Structure

```
├── CLAUDE.md                 # Main project context
├── corpus/                   # Document corpus for RAG
├── projects/                 # Task-specific workspaces
│   ├── honeywell_7140_shortfall/   # $95K shortfall analysis
│   ├── abm-anderson-battery/       # $6.68M BESS settlement
│   ├── fy26-mv-compliance/         # Portfolio compliance
│   └── easi-automation/            # Invoice/RR automation
└── shared_prompts/           # Reusable prompt templates
```

## Key Results

- 100% witnessing rate (vs 38% national average)
- Zero PPA violations
- 60% reduction in invoice processing time
- Knowledge continuity across sessions

## Documentation

See [CLAUDE.md](CLAUDE.md) for full project context, contacts, and workflows.
