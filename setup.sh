#!/bin/bash
# Claude Code GSA Energy Projects Setup Script
# Run this to create the project structure on your machine

set -e

echo "Setting up Claude Code projects for GSA Energy Portfolio..."

# Base directory
BASE_DIR="$HOME/claude-projects"
mkdir -p "$BASE_DIR"

# Create project directories
PROJECTS=(
    "gsa-energy-central"
    "honeywell-7140-shortfall"
    "abm-anderson-battery"
    "fy26-mv-compliance"
    "easi-automation"
)

for project in "${PROJECTS[@]}"; do
    PROJECT_DIR="$BASE_DIR/$project"
    mkdir -p "$PROJECT_DIR"
    mkdir -p "$PROJECT_DIR/retrieved_docs"
    mkdir -p "$PROJECT_DIR/analysis"
    mkdir -p "$PROJECT_DIR/outputs"
    echo "Created $project"
done

# Create shared resources in central project
mkdir -p "$BASE_DIR/gsa-energy-central/shared_prompts"
mkdir -p "$BASE_DIR/gsa-energy-central/corpus/raw_documents"
mkdir -p "$BASE_DIR/gsa-energy-central/corpus/embeddings"

# Create scripts directory for easi-automation
mkdir -p "$BASE_DIR/easi-automation/scripts"

echo ""
echo "Project structure created at: $BASE_DIR"
echo ""
echo "Next steps:"
echo "1. Copy the CLAUDE.md files to each project directory"
echo "2. Run 'cd $BASE_DIR/gsa-energy-central && claude init'"
echo "3. Test with: claude 'What documents do I need for the 7140 analysis?'"
echo ""
echo "Project locations:"
for project in "${PROJECTS[@]}"; do
    echo "  - $BASE_DIR/$project"
done
