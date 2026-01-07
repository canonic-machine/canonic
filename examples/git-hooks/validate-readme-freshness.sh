#!/bin/bash
# validate-readme-freshness.sh
# Syntactic validation: Check if README.md is stale relative to source files
# Implements self-documenting property from CANON.md

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default to current directory
TARGET_DIR="${1:-.}"

echo "🔍 Validating README freshness in: $TARGET_DIR"
echo ""

# Check if required files exist
if [ ! -f "$TARGET_DIR/CANON.md" ]; then
  echo -e "${YELLOW}⚠️  CANON.md not found - skipping validation${NC}"
  exit 0
fi

if [ ! -f "$TARGET_DIR/VOCABULARY.md" ]; then
  echo -e "${YELLOW}⚠️  VOCABULARY.md not found - skipping validation${NC}"
  exit 0
fi

if [ ! -f "$TARGET_DIR/README.md" ]; then
  echo -e "${RED}❌ README.md not found${NC}"
  echo "Violation: Triad requirement - README.md must exist"
  exit 1
fi

# Get modification timestamps (seconds since epoch)
# Use different stat syntax for macOS vs Linux
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS
  CANON_TIME=$(stat -f %m "$TARGET_DIR/CANON.md" 2>/dev/null || echo 0)
  VOCAB_TIME=$(stat -f %m "$TARGET_DIR/VOCABULARY.md" 2>/dev/null || echo 0)
  README_TIME=$(stat -f %m "$TARGET_DIR/README.md" 2>/dev/null || echo 0)
else
  # Linux
  CANON_TIME=$(stat -c %Y "$TARGET_DIR/CANON.md" 2>/dev/null || echo 0)
  VOCAB_TIME=$(stat -c %Y "$TARGET_DIR/VOCABULARY.md" 2>/dev/null || echo 0)
  README_TIME=$(stat -c %Y "$TARGET_DIR/README.md" 2>/dev/null || echo 0)
fi

# Convert timestamps to human-readable dates
if [[ "$OSTYPE" == "darwin"* ]]; then
  CANON_DATE=$(date -r $CANON_TIME '+%Y-%m-%d %H:%M:%S' 2>/dev/null || echo "unknown")
  VOCAB_DATE=$(date -r $VOCAB_TIME '+%Y-%m-%d %H:%M:%S' 2>/dev/null || echo "unknown")
  README_DATE=$(date -r $README_TIME '+%Y-%m-%d %H:%M:%S' 2>/dev/null || echo "unknown")
else
  CANON_DATE=$(date -d "@$CANON_TIME" '+%Y-%m-%d %H:%M:%S' 2>/dev/null || echo "unknown")
  VOCAB_DATE=$(date -d "@$VOCAB_TIME" '+%Y-%m-%d %H:%M:%S' 2>/dev/null || echo "unknown")
  README_DATE=$(date -d "@$README_TIME" '+%Y-%m-%d %H:%M:%S' 2>/dev/null || echo "unknown")
fi

echo "File timestamps:"
echo "  CANON.md:      $CANON_DATE"
echo "  VOCABULARY.md: $VOCAB_DATE"
echo "  README.md:     $README_DATE"
echo ""

# Check if README is stale
STALE=false

if [ $README_TIME -lt $CANON_TIME ]; then
  echo -e "${RED}❌ README.md is older than CANON.md${NC}"
  echo "   README needs regeneration"
  STALE=true
fi

if [ $README_TIME -lt $VOCAB_TIME ]; then
  echo -e "${RED}❌ README.md is older than VOCABULARY.md${NC}"
  echo "   README needs regeneration"
  STALE=true
fi

if [ "$STALE" = true ]; then
  echo ""
  echo "Violation: Documentation protocol"
  echo "README.md must be regenerated when CANON.md or VOCABULARY.md changes"
  echo ""
  echo "To fix:"
  echo "  1. Regenerate README.md from sources"
  echo "  2. Update README.md to reflect latest constraints and terminology"
  echo "  3. Commit both source changes and README together"
  echo ""
  exit 1
fi

echo -e "${GREEN}✅ README.md is fresh${NC}"
echo ""
exit 0
