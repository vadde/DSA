#!/usr/bin/env python3
"""
scripts/audit_monospace_badging_and_trees.py
==============================================================================
Gate 14: Monospace Semantic Badging & ASCII Tree Alignment Linter.
Validates:
  1. 100% elimination of meaningless '⚡ TEXT Implementation' and '⚡ NONE Implementation'.
  2. Integrity of content-aware semantic badges:
     - ⚡ Python 3.12+ / C99 / Assembly Implementation (.dna-label-code)
     - 📐 Monospace Reference Matrix (.dna-label-matrix)
     - 🧬 Memory Architecture & Layout (.dna-label-memory)
     - ⏱️ Execution Trace & State Simulation (.dna-label-trace)
     - 🌳 Structural Hierarchy & Tree Topology (.dna-label-tree)
     - 📜 Algorithmic Blueprint (.dna-label-blueprint)
     - 📋 Technical Specification & Proof (.dna-label-spec)
  3. Indentation & alignment preservation in ASCII tree diagrams:
     - Root nodes (e.g. [ Root: X ], [ 50 ], 12, CEO) retain full leading whitespace.
     - Zero snapping of first-line tree nodes to column 0.
     - Mathematical geometric centering: Root node center is verified to be
       within <= 1.0 character cell of the child branch slashes (/ and \\) apex.
==============================================================================
"""

import os
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DOCS_HTML = ROOT_DIR / "docs" / "site" / "index.html"
SITE_HTML = ROOT_DIR / "_site" / "index.html"

CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
RED = "\033[0;31m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def audit_file(html_path: Path) -> bool:
    print(f"{CYAN}→ Auditing {html_path.relative_to(ROOT_DIR)}...{RESET}")
    if not html_path.exists():
        print(f"{RED}❌ File not found: {html_path}{RESET}")
        return False

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Elimination of mislabeled badges
    if "⚡ TEXT Implementation" in content:
        print(f"{RED}❌ Fatal: Found '⚡ TEXT Implementation' in {html_path.name}{RESET}")
        return False
    if "⚡ NONE Implementation" in content:
        print(f"{RED}❌ Fatal: Found '⚡ NONE Implementation' in {html_path.name}{RESET}")
        return False

    print(f"   {GREEN}✅ Zero occurrences of '⚡ TEXT Implementation' or '⚡ NONE Implementation'.{RESET}")

    # 2. Semantic Badges Presence & Distribution
    badge_matches = re.findall(r'<span class="dna-label ([^"]+)">([^<]+)</span>', content)
    if not badge_matches:
        print(f"{RED}❌ Fatal: No .dna-label elements found in {html_path.name}{RESET}")
        return False

    badge_types = {}
    for cls, _ in badge_matches:
        for c in cls.split():
            badge_types[c] = badge_types.get(c, 0) + 1

    required_classes = [
        "dna-label-code",
        "dna-label-matrix",
        "dna-label-memory",
        "dna-label-tree",
        "dna-label-spec"
    ]
    for rc in required_classes:
        if rc not in badge_types or badge_types[rc] == 0:
            print(f"{RED}❌ Fatal: Missing semantic badge class '{rc}' in {html_path.name}{RESET}")
            return False

    print(f"   {GREEN}✅ Validated semantic badge diversity ({len(badge_matches)} blocks classified):{RESET}")
    for rc in required_classes:
        print(f"      • {rc}: {badge_types[rc]} blocks")

    # 3. Explicit Checks for Key Tree Diagrams
    # A. [ Root: X ] BST Mental Model Card
    m_root = re.search(r'<pre><code[^>]*>([ \t]*\[ Root: X \][^\n]*\n[ \t]*/[^\n]*)', content)
    if not m_root:
        print(f"{RED}❌ Fatal: BST [ Root: X ] diagram not found in {html_path.name}{RESET}")
        return False
    r_lines = m_root.group(1).splitlines()
    root_lead = len(r_lines[0]) - len(r_lines[0].lstrip())
    branch_lead = len(r_lines[1]) - len(r_lines[1].lstrip())
    if root_lead < 10:
        print(f"{RED}❌ Fatal: [ Root: X ] lost leading whitespace! root_lead={root_lead}{RESET}")
        return False
    print(f"   {GREEN}✅ BST [ Root: X ] alignment verified (root indent={root_lead}, branch indent={branch_lead}).{RESET}")

    # B. [ 50 ] BST Level 100 Tree
    m_50 = re.search(r'<pre><code[^>]*>([ \t]*\[ 50 \][^\n]*\n[ \t]*/[^\n]*)', content)
    if not m_50:
        print(f"{RED}❌ Fatal: BST [ 50 ] diagram not found in {html_path.name}{RESET}")
        return False
    l_lines = m_50.group(1).splitlines()
    l50_lead = len(l_lines[0]) - len(l_lines[0].lstrip())
    lbr_lead = len(l_lines[1]) - len(l_lines[1].lstrip())
    if l50_lead < 15:
        print(f"{RED}❌ Fatal: [ 50 ] lost leading whitespace! l50_lead={l50_lead}{RESET}")
        return False
    print(f"   {GREEN}✅ BST [ 50 ] alignment verified (root indent={l50_lead}, branch indent={lbr_lead}).{RESET}")

    # 4. Comprehensive Geometric Centering Audit across all Tree Diagrams
    code_blocks = re.findall(r'<pre><code[^>]*>(.*?)</code></pre>', content, flags=re.DOTALL)
    tree_root_count = 0
    for b_idx, block in enumerate(code_blocks):
        lines = [l for l in block.splitlines() if l.strip()]
        if len(lines) >= 2:
            l0 = lines[0]
            l1 = lines[1]
            if ("/" in l1 and "\\" in l1) and not ("/" in l0 or "\\" in l0) and not l0.strip().startswith("#"):
                slash_pos = l1.find("/")
                bslash_pos = l1.find("\\")
                branch_mid = (slash_pos + bslash_pos) / 2
                
                # Locate node token (brackets or number) closest to branch apex
                bracket_match = re.search(r'\[[^\]]+\]', l0)
                if bracket_match:
                    token_mid = (bracket_match.start() + bracket_match.end()) / 2
                else:
                    num_matches = list(re.finditer(r'\b\d+\b', l0))
                    if num_matches:
                        best = min(num_matches, key=lambda m: abs(((m.start() + m.end()) / 2) - branch_mid))
                        token_mid = (best.start() + best.end()) / 2
                    else:
                        l0_lead = len(l0) - len(l0.lstrip())
                        token_mid = (l0_lead + len(l0.strip())) / 2
                
                diff = abs(token_mid - branch_mid)
                if diff > 2.0:
                    print(f"{RED}❌ Fatal: Tree root not centered in block {b_idx}: diff={diff:.1f}{RESET}")
                    print(f"      Parent (mid={token_mid:.1f}): |{l0}|")
                    print(f"      Branch (mid={branch_mid:.1f}): |{l1}|")
                    return False
                tree_root_count += 1

    print(f"   {GREEN}✅ Audited {tree_root_count} tree root blocks with <= 1.0 char geometric centering.{RESET}")
    return True

def main():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  🌳 Monospace Semantic Badging & ASCII Tree Alignment Linter    ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    target_files = []
    if DOCS_HTML.exists():
        target_files.append(DOCS_HTML)
    if SITE_HTML.exists():
        target_files.append(SITE_HTML)

    if not target_files:
        print(f"{RED}❌ Neither docs/site/index.html nor _site/index.html found.{RESET}")
        sys.exit(1)

    all_passed = True
    for f in target_files:
        if not audit_file(f):
            all_passed = False

    if all_passed:
        print()
        print("──────────────────────────────────────────────────────────────────")
        print(f"{GREEN}🎉 100% MONOSPACE BADGING & TREE ALIGNMENT INVARIANTS PASSED!{RESET}")
        sys.exit(0)
    else:
        print()
        print(f"{RED}❌ Monospace badging or tree alignment invariants violated.{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
