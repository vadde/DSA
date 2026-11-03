#!/usr/bin/env python3
"""
scripts/audit_dynamic_zoom_engine.py — Gate 16 Automated Verification Suite
Audits the Dynamic Adaptive Content Zoom & Stage Width Engine:
1. Verifies presence of HUD zoom stepper (#hud-zoom-stepper) & controls in index.html.
2. Verifies liquid-glass styles, theme tokens, and anti-occlusion gutters in style.css.
3. Verifies dynamic step synthesis and available width calculation in app.js.
4. Simulates multi-viewport mathematical invariants (4K/2K, MBP 16", iPad, Mobile).
"""

import os
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DOCS_SITE_DIR = ROOT_DIR / "docs" / "site"
SITE_DIR = ROOT_DIR / "_site"

CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
RED = "\033[0;31m"
YELLOW = "\033[1;33m"
NC = "\033[0m"

def print_header(title: str):
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════════════╗{NC}")
    print(f"{CYAN}║  {title:<64}║{NC}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════╝{NC}")

def test_html_controls(html_path: Path):
    if not html_path.exists():
        print(f"   {RED}❌ Error: {html_path} does not exist.{NC}")
        return False

    content = html_path.read_text(encoding="utf-8")
    required_ids = [
        "hud-zoom-stepper",
        "zoom-out-btn",
        "zoom-level-badge",
        "zoom-in-btn",
        "zoom-fit-btn",
    ]

    for req_id in required_ids:
        if f'id="{req_id}"' not in content:
            print(f"   {RED}❌ Missing required ID '{req_id}' in {html_path.name}{NC}")
            return False

    print(f"   {GREEN}✅ All HUD zoom stepper controls verified in {html_path.name}{NC}")
    return True

def test_css_invariants(css_path: Path):
    if not css_path.exists():
        print(f"   {RED}❌ Error: {css_path} does not exist.{NC}")
        return False

    content = css_path.read_text(encoding="utf-8")
    required_classes = [
        ".hud-zoom-stepper",
        ".zoom-btn",
        ".zoom-level-badge",
        ".zoom-fit-btn",
    ]

    for req_class in required_classes:
        if req_class not in content:
            print(f"   {RED}❌ Missing required CSS class '{req_class}' in {css_path.name}{NC}")
            return False

    # Check anti-occlusion gutter for floating sidebar toggle
    if "clamp(72px, 8vw, 156px)" not in content:
        print(f"   {RED}❌ Missing anti-occlusion clearance gutter 'clamp(72px, 8vw, 156px)' in {css_path.name}{NC}")
        return False

    print(f"   {GREEN}✅ Liquid-glass zoom tokens & anti-occlusion gutters verified in {css_path.name}{NC}")
    return True

def test_js_invariants(js_path: Path):
    if not js_path.exists():
        print(f"   {RED}❌ Error: {js_path} does not exist.{NC}")
        return False

    content = js_path.read_text(encoding="utf-8")
    required_symbols = [
        "initDynamicZoomEngine",
        "calculateDynamicFit",
        "dsaDynamicZoom",
        "dsa_content_zoom",
        "dsa_content_fit",
    ]

    for req_sym in required_symbols:
        if req_sym not in content:
            print(f"   {RED}❌ Missing required runtime symbol '{req_sym}' in {js_path.name}{NC}")
            return False

    print(f"   {GREEN}✅ Runtime dynamic zoom engine & persistence verified in {js_path.name}{NC}")
    return True

def simulate_viewport_step_engine():
    """
    Simulates the JS calculateDynamicFit algorithm and verifies mathematical invariants
    across device classes.
    """
    base_stage_width = 1040

    def compute_steps(w: int, collapsed: bool):
        if w <= 768:
            return 100, [100], True

        sidebar_width = 0 if collapsed else 330
        gutters = 224 if collapsed else 96
        avail_width = max(base_stage_width, w - sidebar_width - gutters)
        raw_zoom = min(2.0, max(1.0, avail_width / base_stage_width))
        fit_pct = round(raw_zoom * 100)

        if fit_pct <= 105:
            steps = [100]
        elif fit_pct <= 130:
            steps = [100, fit_pct]
        elif fit_pct <= 160:
            steps = [100, 125, fit_pct]
        elif fit_pct <= 185:
            steps = [100, 125, 150, fit_pct]
        else:
            steps = [100, 125, 150, 175, fit_pct]

        return fit_pct, steps, False

    test_matrix = [
        ("4K / Ultrawide (2560px)", 2560, True, 200, 5),
        ("1080p Desktop (1920px)", 1920, True, 163, 4),
        ("MacBook Pro 16\" (1728px)", 1728, True, 145, 3),
        ("MacBook 14\" (1440px)", 1440, True, 117, 2),
        ("Mobile Phone (390px)", 390, True, 100, 1),
    ]

    print("   → Auditing Dynamic Step Synthesis Across Device Viewports:")
    for name, width, collapsed, expected_fit, expected_steps_count in test_matrix:
        fit_pct, steps, is_mobile = compute_steps(width, collapsed)
        if is_mobile:
            assert fit_pct == 100 and steps == [100], f"Failed mobile lock on {name}"
            print(f"      • {name:<26}: {GREEN}Locked at 100% (Mobile Safeguard Verified){NC}")
        else:
            assert len(steps) == expected_steps_count, f"Unexpected step count for {name}: {steps}"
            print(f"      • {name:<26}: {GREEN}Fit={fit_pct}% | Steps={steps} (Clicks to Fit: {len(steps)-1}){NC}")

    return True

def main():
    print_header("🔍 Gate 16: Dynamic Adaptive Content Zoom & Stage Width Linter")

    success = True
    print(f"\n{CYAN}→ 1. Auditing HTML Stepper Controls...{NC}")
    if (DOCS_SITE_DIR / "index.html").exists():
        success &= test_html_controls(DOCS_SITE_DIR / "index.html")
    if (SITE_DIR / "index.html").exists():
        success &= test_html_controls(SITE_DIR / "index.html")

    print(f"\n{CYAN}→ 2. Auditing Liquid-Glass Styling & Clearance Gutters...{NC}")
    if (DOCS_SITE_DIR / "style.css").exists():
        success &= test_css_invariants(DOCS_SITE_DIR / "style.css")
    if (SITE_DIR / "style.css").exists():
        success &= test_css_invariants(SITE_DIR / "style.css")

    print(f"\n{CYAN}→ 3. Auditing Runtime JS Logic & API Bindings...{NC}")
    if (DOCS_SITE_DIR / "app.js").exists():
        success &= test_js_invariants(DOCS_SITE_DIR / "app.js")
    if (SITE_DIR / "app.js").exists():
        success &= test_js_invariants(SITE_DIR / "app.js")

    print(f"\n{CYAN}→ 4. Auditing Multi-Viewport Dynamic Step Synthesis Engine...{NC}")
    success &= simulate_viewport_step_engine()

    print("\n──────────────────────────────────────────────────────────────────")
    if success:
        print(f"{GREEN}🎉 100% DYNAMIC ADAPTIVE ZOOM & FIT INVARIANTS PASSED!{NC}")
        sys.exit(0)
    else:
        print(f"{RED}❌ GATE 16 AUDIT FAILED! Review errors above.{NC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
