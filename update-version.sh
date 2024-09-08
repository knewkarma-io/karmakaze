#!/bin/bash

# Check if version argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <version>"
  exit 1
fi

# Extract major, minor, and patch from version argument
VERSION=$1

# Get the absolute path of the current directory
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

# Define absolute file paths
PYPROJECT_TOML="$SCRIPT_DIR/pyproject.toml"

# Check if files exist
if [ ! -f "$PYPROJECT_TOML" ]; then
  echo "Error: $PYPROJECT_TOML not found!"
  exit 1
fi

# Update version in pyproject.toml
sed -i.bak "s/version = \".*\"/version = \"$VERSION\"/" "$PYPROJECT_TOML"

# Clean up backup files created by sed
rm "${PYPROJECT_TOML}.bak"

echo "Version updated to $VERSION in $PYPROJECT_TOML"

