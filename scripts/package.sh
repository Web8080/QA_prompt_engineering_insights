#!/bin/bash

# Package script - Creates zip archive of entire project
# Excludes development artifacts and sensitive files

set -e

PROJECT_NAME="qa-prompt-engineering"
VERSION=$(date +%Y%m%d_%H%M%S)
PACKAGE_DIR="packages"
ZIP_NAME="${PROJECT_NAME}_${VERSION}.zip"

echo "=========================================="
echo "Packaging QA Prompt Engineering Project"
echo "=========================================="
echo "Version: $VERSION"
echo ""

# Create packages directory if it doesn't exist
mkdir -p "$PACKAGE_DIR"

# Create temporary directory for packaging
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo "Copying project files..."

# Copy project files (excluding git, venv, etc.)
rsync -av --exclude='.git' \
          --exclude='__pycache__' \
          --exclude='*.pyc' \
          --exclude='.pytest_cache' \
          --exclude='venv' \
          --exclude='env' \
          --exclude='.env' \
          --exclude='*.log' \
          --exclude='coverage' \
          --exclude='.coverage' \
          --exclude='packages' \
          --exclude='*.zip' \
          --exclude='.DS_Store' \
          --exclude='.idea' \
          --exclude='.vscode' \
          . "$TEMP_DIR/$PROJECT_NAME"

# Create zip archive
echo "Creating zip archive..."
cd "$TEMP_DIR"
zip -r "$ZIP_NAME" "$PROJECT_NAME" > /dev/null
cd - > /dev/null

# Move zip to packages directory
mv "$TEMP_DIR/$ZIP_NAME" "$PACKAGE_DIR/"

# Get file size
FILE_SIZE=$(du -h "$PACKAGE_DIR/$ZIP_NAME" | cut -f1)

echo ""
echo "=========================================="
echo "Package created successfully!"
echo "=========================================="
echo "File: $PACKAGE_DIR/$ZIP_NAME"
echo "Size: $FILE_SIZE"
echo ""
echo "Package contents:"
echo "  - Development code"
echo "  - QA test framework"
echo "  - OWASP penetration tests"
echo "  - Production placeholders"
echo "  - Configuration files"
echo "  - Documentation"
echo ""

