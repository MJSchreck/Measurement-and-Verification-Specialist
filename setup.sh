#!/bin/bash
# Setup script for M&V Specialist Cyborg Workflow System

set -e

echo "Setting up M&V Specialist workspace..."

# Create directory structure
mkdir -p corpus/{raw_documents,embeddings}
mkdir -p projects/espc_mv_analysis/{retrieved_docs,analysis,outputs}
mkdir -p projects/honeywell_contract_review/{retrieved_docs,analysis,outputs}
mkdir -p projects/honeywell_7140_shortfall/{retrieved_docs,analysis}

echo "Directory structure created."

# Check for required tools
echo "Checking dependencies..."

if command -v claude &> /dev/null; then
    echo "✓ Claude CLI found"
else
    echo "✗ Claude CLI not found - install from https://claude.ai/code"
fi

if command -v python3 &> /dev/null; then
    echo "✓ Python 3 found"
else
    echo "✗ Python 3 not found"
fi

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Add documents to corpus/raw_documents/"
echo "  2. Run: claude \"Index all documents in /corpus/raw_documents\""
echo "  3. Start a project: cd projects/honeywell_7140_shortfall"
echo "  4. Query: claude \"Search Drive for 7140 M&V report and analyze shortfalls\""
