#!/usr/bin/env bash
# ==============================================================================
# build-docs.sh — Package Static Living Documentation Portal
# Compiles patterns and generates _site/ for GitHub Pages and local serving.
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
DOCS_SITE_DIR="${ROOT_DIR}/docs/site"
SITE_DIR="${ROOT_DIR}/_site"

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║  📚 Building DSA Living Documentation Portal                     ║"
echo "╚══════════════════════════════════════════════════════════════════╝"

# 1. Clean and initialize _site directory
rm -rf "${SITE_DIR}"
mkdir -p "${SITE_DIR}"
mkdir -p "${SITE_DIR}/catalog"
mkdir -p "${SITE_DIR}/assets"
mkdir -p "${DOCS_SITE_DIR}/catalog"

# 2. Compile catalog and generate hydrated HTML
echo "  → Executing Python catalog compiler..."
python3 "${SCRIPT_DIR}/build-docs.py"

# 3. Copy static site assets to _site
echo "  → Packaging static assets into _site/..."
cp -r "${DOCS_SITE_DIR}/"* "${SITE_DIR}/"

# 4. Verify distribution integrity
for f in index.html style.css app.js; do
  if [ ! -f "${SITE_DIR}/${f}" ]; then
    echo "❌ Error: Required static asset missing in ${SITE_DIR}/${f}" >&2
    exit 1
  fi
done

if [ ! -f "${SITE_DIR}/catalog/manifest.json" ]; then
  echo "❌ Error: Search manifest missing in ${SITE_DIR}/catalog/manifest.json" >&2
  exit 1
fi

TOTAL_FILES=$(find "${SITE_DIR}" -type f | wc -l | tr -d ' ')
TOTAL_SIZE=$(du -sh "${SITE_DIR}" | cut -f1)

echo "✅ DSA Living Documentation built successfully!"
echo "  • Output path: ${SITE_DIR}"
echo "  • Total files: ${TOTAL_FILES}"
echo "  • Total size:  ${TOTAL_SIZE}"
echo ""
echo "To serve locally:"
echo "  make docs-serve"
echo "  or: python3 -m http.server 4000 --directory _site"
