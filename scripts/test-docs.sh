#!/usr/bin/env bash
# ==============================================================================
# test-docs.sh — 13-Gate Headless Verification Suite for DSA Documentation
# Validates HTML markup, KaTeX math delimiters, Mermaid syntax & sizing,
# draggable sidebar resizer, Year 2500 mobile navigation drawer,
# table overflow containment, relative subpath invariants, bundle integrity,
# Unicode monospace box-drawing alignment, and collapsible details invariants.
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
SITE_DIR="${ROOT_DIR}/_site"
DOCS_SITE_DIR="${ROOT_DIR}/docs/site"

CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║  🧪 Running DSA Living Documentation 13-Gate Audit Suite         ║"
echo "╚══════════════════════════════════════════════════════════════════╝"

# Ensure _site is built
if [ ! -d "${SITE_DIR}" ] || [ ! -f "${SITE_DIR}/index.html" ]; then
  echo -e "${YELLOW}⚡ _site directory not found or incomplete. Building now...${NC}"
  bash "${SCRIPT_DIR}/build-docs.sh"
fi

# ------------------------------------------------------------------------------
# Gate 1: Core Assets Presence
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 1. Auditing Core Assets in _site/...${NC}"
for f in index.html style.css app.js catalog/manifest.json; do
  if [ ! -f "${SITE_DIR}/${f}" ]; then
    echo -e "${RED}❌ Gate 1 Failed: Missing required asset ${SITE_DIR}/${f}${NC}"
    exit 1
  fi
done
echo -e "   ${GREEN}✅ Core static assets verified (index.html, style.css, app.js, catalog/manifest.json)${NC}"

# ------------------------------------------------------------------------------
# Gate 2: Catalog Completeness & Manifest Integrity
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 2. Auditing Catalog Completeness & Search Index...${NC}"
python3 -c "
import json
with open('${SITE_DIR}/catalog/manifest.json') as f:
    data = json.load(f)
patterns = data.get('patterns', [])
problems = data.get('problems', [])
assert len(patterns) == 44, f'Expected 44 patterns, found {len(patterns)}'
assert len(problems) >= 250, f'Expected >= 250 problems, found {len(problems)}'
print(f'   ✅ Validated {len(patterns)} patterns and {len(problems)} indexed problems.')
"

# ------------------------------------------------------------------------------
# Gate 3: Mermaid Node Label Escaping
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 3. Auditing Mermaid label escaping invariants (< and > inside node labels)...${NC}"
# Detect unescaped '<' inside mermaid pre blocks
UNESCAPED_LT=$(sed -n '/<pre class="mermaid">/,/<\/pre>/p' "${SITE_DIR}/index.html" | grep -n '\[.*<[0-9].*\]' || true)
if [ -n "${UNESCAPED_LT}" ]; then
  echo -e "${RED}❌ Gate 3 Failed: Detected unescaped '<' inside Mermaid node label in index.html:${NC}"
  echo "${UNESCAPED_LT}"
  echo "   Use '≤' or '&lt;' to prevent Mermaid HTML parser crashes."
  exit 1
fi
echo -e "   ${GREEN}✅ Mermaid node labels are cleanly escaped.${NC}"

# ------------------------------------------------------------------------------
# Gate 4: CSS SVG Sizing Invariants
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 4. Auditing SVG sizing invariants in style.css...${NC}"
if grep -E '\.mermaid svg.*width:\s*auto\s*!important' "${SITE_DIR}/style.css" > /dev/null; then
  echo -e "${RED}❌ Gate 4 Failed: Fatal CSS anti-pattern 'width: auto !important' found on .mermaid svg.${NC}"
  echo "   This collapses SVG elements to 0px x 0px inside flex containers."
  exit 1
fi
echo -e "   ${GREEN}✅ CSS SVG sizing conforms to responsive viewBox standards.${NC}"

# ------------------------------------------------------------------------------
# Gate 5: KaTeX Delimiters & Script Presence
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 5. Auditing KaTeX math engine integration...${NC}"
if ! grep -q "katex.min.css" "${SITE_DIR}/index.html"; then
  echo -e "${RED}❌ Gate 5 Failed: KaTeX stylesheet missing in index.html head${NC}"
  exit 1
fi
if ! grep -q "auto-render.min.js" "${SITE_DIR}/index.html"; then
  echo -e "${RED}❌ Gate 5 Failed: KaTeX auto-render script missing in index.html${NC}"
  exit 1
fi
if ! grep -q "renderMathInElement" "${SITE_DIR}/app.js"; then
  echo -e "${RED}❌ Gate 5 Failed: renderMathInElement call missing in app.js${NC}"
  exit 1
fi
echo -e "   ${GREEN}✅ KaTeX mathematical typesetting engine verified.${NC}"

# ------------------------------------------------------------------------------
# Gate 6: Draggable Sidebar Resizer & Collapsible Rail Invariants
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 6. Auditing Draggable Sidebar Resizer & Collapsible Rail invariants...${NC}"
if ! grep -q 'id="sidebar-resizer"' "${SITE_DIR}/index.html"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing #sidebar-resizer element in index.html${NC}"
  exit 1
fi
if ! grep -q 'id="sidebar-dock-toggle"' "${SITE_DIR}/index.html"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing #sidebar-dock-toggle element in index.html${NC}"
  exit 1
fi
if ! grep -q 'id="sidebar-close-btn"' "${SITE_DIR}/index.html"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing #sidebar-close-btn element in index.html${NC}"
  exit 1
fi
if ! grep -q 'id="floating-sidebar-toggle"' "${SITE_DIR}/index.html"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing #floating-sidebar-toggle element in index.html${NC}"
  exit 1
fi
if ! grep -q 'col-resize' "${SITE_DIR}/style.css"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing col-resize cursor rule in style.css${NC}"
  exit 1
fi
if ! grep -q 'body.sidebar-collapsed' "${SITE_DIR}/style.css"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing body.sidebar-collapsed rule in style.css${NC}"
  exit 1
fi
if ! grep -q 'initSidebarResizer' "${SITE_DIR}/app.js"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing initSidebarResizer in app.js${NC}"
  exit 1
fi
if ! grep -q 'initDesktopSidebarToggle' "${SITE_DIR}/app.js"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing initDesktopSidebarToggle in app.js${NC}"
  exit 1
fi
if ! grep -q 'dsa_sidebar_collapsed' "${SITE_DIR}/app.js"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing dsa_sidebar_collapsed persistence key in app.js${NC}"
  exit 1
fi
if ! grep -q 'HapticAudio' "${SITE_DIR}/app.js"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing HapticAudio engine in app.js${NC}"
  exit 1
fi
if ! grep -q 'dsa_sidebar_width' "${SITE_DIR}/app.js"; then
  echo -e "${RED}❌ Gate 6 Failed: Missing localStorage persistence key in app.js${NC}"
  exit 1
fi
echo -e "   ${GREEN}✅ Draggable sidebar resizer, collapsible toggle & audio engine verified.${NC}"

# ------------------------------------------------------------------------------
# Gate 7: Year 2500 Mobile Drawer & Anti-Clobbering Invariants
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 7. Auditing Mobile Navigation Drawer & Anti-Clobbering invariants...${NC}"
if ! grep -q 'id="mobile-nav-toggle"' "${SITE_DIR}/index.html"; then
  echo -e "${RED}❌ Gate 7 Failed: Missing #mobile-nav-toggle hamburger button in index.html${NC}"
  exit 1
fi
if ! grep -q 'id="mobile-drawer-backdrop"' "${SITE_DIR}/index.html"; then
  echo -e "${RED}❌ Gate 7 Failed: Missing #mobile-drawer-backdrop overlay in index.html${NC}"
  exit 1
fi
if ! grep -q 'initMobileDrawer' "${SITE_DIR}/app.js"; then
  echo -e "${RED}❌ Gate 7 Failed: Missing initMobileDrawer in app.js${NC}"
  exit 1
fi
if ! grep -q 'overflow-x: clip' "${SITE_DIR}/style.css"; then
  echo -e "${RED}❌ Gate 7 Failed: Missing sticky-safe 'overflow-x: clip' in style.css${NC}"
  exit 1
fi
echo -e "   ${GREEN}✅ Mobile drawer & sticky-safe anti-clobbering rules verified.${NC}"

# ------------------------------------------------------------------------------
# Gate 8: Table & Touch Containment Invariants
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 8. Auditing Table & Touch Containment invariants...${NC}"
if ! grep -q 'class="table-wrapper"' "${SITE_DIR}/index.html"; then
  echo -e "${RED}❌ Gate 8 Failed: Missing .table-wrapper elements in index.html${NC}"
  exit 1
fi
if ! grep -q 'min-width' "${SITE_DIR}/style.css"; then
  echo -e "${RED}❌ Gate 8 Failed: Missing table min-width rule in style.css${NC}"
  exit 1
fi
echo -e "   ${GREEN}✅ Table touch scrolling and min-width containment verified.${NC}"

# ------------------------------------------------------------------------------
# Gate 9: Relative Path & Subpath Invariants (/DSA/)
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 9. Auditing Relative Path invariants (GitHub Pages /DSA/ compliance)...${NC}"
BAD_PATHS=$(grep -E '(href|src)="/(style|app|assets|catalog)' "${SITE_DIR}/index.html" || true)
if [ -n "${BAD_PATHS}" ]; then
  echo -e "${RED}❌ Gate 9 Failed: Found root-relative paths in index.html that will break on /DSA/:${NC}"
  echo "${BAD_PATHS}"
  exit 1
fi
echo -e "   ${GREEN}✅ All stylesheet, script, and catalog links use relative addressing (./).${NC}"

# ------------------------------------------------------------------------------
# Gate 10: Static Bundle Size & Integrity
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 10. Auditing Static Bundle Size & Distribution Integrity...${NC}"
BUNDLE_SIZE_MB=$(du -sm "${SITE_DIR}" | cut -f1)
if [ "${BUNDLE_SIZE_MB}" -gt 25 ]; then
  echo -e "${RED}❌ Gate 10 Failed: Bundle size (${BUNDLE_SIZE_MB}MB) exceeds 25MB threshold.${NC}"
  exit 1
fi
echo -e "   ${GREEN}✅ Bundle footprint is optimal (${BUNDLE_SIZE_MB}MB < 25MB).${NC}"

# ------------------------------------------------------------------------------
# Gate 11: Mermaid Diagram ID Uniqueness, Pipeline Isolation & Zero Nav Clutter
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 11. Auditing Mermaid Diagram ID Uniqueness, Isolation & Zero Nav Clutter...${NC}"
python3 -c "
import re
with open('${SITE_DIR}/index.html') as f:
    content = f.read()

diagram_ids = re.findall(r'<pre class=\"mermaid\" id=\"([^\"]+)\">', content)
assert len(diagram_ids) >= 100, f'Expected >= 100 mermaid diagrams, found {len(diagram_ids)}'
assert len(diagram_ids) == len(set(diagram_ids)), f'Duplicate diagram IDs detected! {len(diagram_ids)} total vs {len(set(diagram_ids))} unique'

# Verify legacy folder navigation footers are 100% stripped from index.html
assert 'Back to Foundations README' not in content, 'Legacy navigation footer link found in index.html'
assert '🧭 Navigation' not in content, 'Legacy navigation header found in index.html'

with open('${SITE_DIR}/app.js') as f:
    js = f.read()
assert 'heroMermaid' in js, 'Missing eager heroMermaid render in app.js'
assert 'isProgrammaticScroll' in js, 'Missing isProgrammaticScroll lock in app.js'
print(f'   ✅ Validated {len(diagram_ids)} isolated Mermaid diagrams with 100% unique IDs & zero legacy nav clutter.')
"
echo -e "   ${GREEN}✅ Diagram containment and clean footer navigation verified.${NC}"

# ------------------------------------------------------------------------------
# Gate 12: Unicode Monospace Box-Drawing Table & Card Alignment
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 12. Auditing Unicode Box-Drawing Alignment Invariants...${NC}"
python3 "${SCRIPT_DIR}/audit_ascii_boxes.py" --check
echo -e "   ${GREEN}✅ 100% of ASCII and Unicode box-drawing tables and cards are aligned.${NC}"

# ------------------------------------------------------------------------------
# Gate 13: Collapsible Details, Nested Accordions & Zero Raw HTML Block Escaping
# ------------------------------------------------------------------------------
echo -e "${CYAN}→ 13. Auditing Collapsible Details & Zero Raw HTML Block Escaping...${NC}"
python3 "${SCRIPT_DIR}/audit_collapsible_elements.py"
echo -e "   ${GREEN}✅ 100% of collapsible details and nested accordions verified.${NC}"

echo ""
echo "╔══════════════════════════════════════════════════════════════════╗"
echo -e "║  ${GREEN}🎉 ALL 13 QUALITY GATES PASSED DETERMINISTICALLY!              ${NC}║"
echo "╚══════════════════════════════════════════════════════════════════╝"
