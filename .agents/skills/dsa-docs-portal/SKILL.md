---
name: dsa-docs-portal
description: >-
  Authoritative engineering guide and automated testing protocol for the DSA Living Documentation Portal (https://vadde.github.io/DSA/). Covers Year 2500 cosmic liquid-glass design system, Aero Mica ambient halos, draggable sidebar resizer invariants, icon-only squircle navigation toggles, inter-pattern 24px spacing, floating back-to-top guider engine, commute gadget mobile drawer, zero-truncation titles, touch-overflow containment, 1:1 ScrollSpy sync with decoupled sidebar scrolling, Mermaid SVG layout rules, Safari WebKit flex sizing, sub-millisecond Theater mode workbench, KaTeX math typesetting, interactive SIFT simulator, Cmd+K fuzzy search, Unicode monospace box-drawing alignment engine, and the 16-gate automated headless audit suite.
---

# 📚 DSA Living Documentation Portal Engineering Skill

This skill is the **authoritative engineering protocol and single source of truth** for maintaining, styling, extending, and verifying the `vadde/DSA` Living Documentation Portal ([https://vadde.github.io/DSA/](https://vadde.github.io/DSA/)).

AI coding assistants and engineers must follow this guide whenever adding patterns, modifying CSS styles, rendering architecture diagrams, typesetting mathematical equations, building interactive simulator widgets, or testing on mobile and desktop viewports.

---

## 🏛️ Portal Architecture & File Map

The documentation portal is built with **zero build toolchain dependencies** (pure vanilla HTML5, CSS3, ES2022 JavaScript, and standard CDN libraries):

```
DSA/
├── Makefile                               # Canonical DevEx commands (docs-build, docs-serve, docs-test, test-zoom, test-links, etc.)
├── specs/
│   └── SPEC-001-dsa-futuristic-docs-portal.md # Ratified PRD & System Architecture Spec
├── docs/site/
│   ├── index.html                         # Hydrated Year 2500 Command Deck Shell
│   ├── style.css                          # Liquid glass tokens, Aero Mica halos, resizer, zoom engine, responsive layout
│   └── app.js                             # ScrollSpy, dynamic zoom, resizer, mobile drawer, search modal, lazy renderers
├── scripts/
│   ├── build-docs.py                      # Production catalog compiler (extracts metadata, problems, walkthroughs)
│   ├── build-docs.sh                      # Static bundle packaging script (outputs to _site/)
│   ├── test-docs.sh                       # 16-Gate automated headless verification suite
│   ├── audit_dynamic_zoom_engine.py       # Gate 16: Dynamic adaptive zoom & stage width fitting linter
│   ├── audit_links_and_anchors.py         # Gate 15: Universal hyperlink integrity & local path prevention linter
│   ├── audit_monospace_badging_and_trees.py # Gate 14: Monospace semantic badging & ASCII tree alignment linter
│   ├── audit_collapsible_elements.py      # Gate 13: Collapsible details & raw HTML block escaping linter
│   └── audit_ascii_boxes.py               # Gate 12: Unicode UAX #11 monospace box-drawing linter and formatter
├── .agents/skills/dsa-docs-portal/
│   └── SKILL.md                           # YOU ARE HERE — Authoritative design & engineering protocol
└── .github/workflows/
    ├── ci.yml                             # Parallel CI verification (Python AST, Ruff, Box Linter, 16-Gate Audit)
    └── docs-publish.yml                   # CD workflow deploying verified main pushes to GitHub Pages
```

---

## 🎨 Design System & Multi-Theme Engine

The portal uses a **deep cosmic liquid-glass design system with Aero Mica ambient halos** supporting 4 distinct themes:

### Color Palette Tokens

| Token | CSS Variable | Dark Hex / RGBA Value | Mica Light Equivalent | Purpose |
|---|---|---|---|---|
| **Canvas Deep Base** | `--bg-deep` | `#050813` | `#f8fafc` | Deep space background canvas |
| **Card Surface** | `--bg-card` | `rgba(13, 20, 39, 0.65)` | `rgba(255, 255, 255, 0.88)` | Glassmorphism card background |
| **Card Border** | `--bg-card-border` | `rgba(255, 255, 255, 0.08)` | `rgba(30, 41, 59, 0.15)` | Subtle translucent glass card edge |
| **Hover Border** | `--bg-card-border-glow` | `rgba(0, 242, 254, 0.35)` | `rgba(14, 165, 233, 0.35)` | Interactive element border focus |
| **Cyan Accent** | `--accent-cyan` | `#00f2fe` | `#0284c7` | Primary interactive focus, active items, SIFT highlights |
| **Violet Accent** | `--accent-violet` | `#a855f7` | `#7c3aed` | Diagram relational links, DNA skeleton badges |
| **Emerald Accent** | `--accent-emerald` | `#10b981` | `#059669` | Passing status, Easy difficulty badge |
| **Amber Accent** | `--accent-amber` | `#f59e0b` | `#d97706` | Medium difficulty badge, caution callouts |
| **Rose Accent** | `--accent-rose` | `#f43f5e` | `#e11d48` | Hard difficulty badge, Kill Mode alerts |
| **Primary Text** | `--text-main` | `#f1f5f9` | `#0f172a` | High-contrast body text and titles |
| **Muted Text** | `--text-muted` | `#94a3b8` | `#475569` | Subtitles, parameter descriptions |
| **Dim Text** | `--text-dim` | `#64748b` | `#64748b` | Captions, footnotes, table metadata |

### Theme Invariants:
1. **Liquid Glass (`[data-theme="liquid"]`)**: Default deep cosmic glass with vibrant cyan/violet edge glows and dark halo gradients.
2. **Aero Mica (`[data-theme="mica"]`)**:
   - **High-Contrast Code Blocks**: Code blocks MUST use dark text on bright frosted surface (`background: rgba(255, 255, 255, 0.95); color: #0f172a !important;`). Never leave white-on-white text!
   - **Frosted Theater Tool Buttons**: Must use high-contrast frosted pills (`background: rgba(255, 255, 255, 0.22); border: 1px solid rgba(255, 255, 255, 0.55); color: #ffffff !important;`) so that `+`, `−`, `100%`, and `Fit` buttons pop over the dark modal header.
   - **Floating Squircles**: `#floating-sidebar-toggle` and `#floating-back-to-top` use bright white glass (`background: rgba(255, 255, 255, 0.94); color: #0f172a; border-color: rgba(30, 41, 59, 0.25);`).
3. **Obsidian Dark (`[data-theme="obsidian"]`)**: Matte pure-black stealth palette with emerald accents.
4. **Cyberpunk Neon (`[data-theme="cyberpunk"]`)**: High-saturation hot-pink (`#ff007f`) and electric cyan (`#00f0ff`) contrast grid.

---

## 🔍 Dynamic Adaptive Content Zoom & Stage Width Engine (Gate 16)

The reading stage features a dynamic zoom and fitting engine that dynamically extends the main reading content to fit the available screen width across all form factors:

```
+------------------------------------------------------------------------+
| TOP HUD NAVIGATION BAR                                                 |
| [Menu] [Sidebar] DSA PATTERN BIBLE     [ - | 155% | + | Fit ]  [Search] |
+------------------------------------------------------------------------+
```

### 1. Mathematical Formulation & Available Width Calculation:
```javascript
const windowWidth = window.innerWidth;
const isCollapsed = document.body.classList.contains('sidebar-collapsed');
const sidebarEffectiveWidth = isCollapsed ? 0 : sidebarWidth;
const reservedGutter = isCollapsed ? 72 : 48; // Safe margin & floating icon clearance
const availWidth = Math.max(768, windowWidth - sidebarEffectiveWidth - reservedGutter);
const rawFitZoom = availWidth / BASE_STAGE_WIDTH; // BASE_STAGE_WIDTH = 1040px
```

### 2. Multi-Viewport Dynamic Step Synthesis:
The ladder dynamically synthesizes 1 to 4 punchy steps with $\sim 25\%$ increments tailored to the device screen:
- **Mobile Phone ($\le 768\text{px}$)**: Locked at $100\%$ safeguard (stepper hidden/disabled; prevents horizontal overflow).
- **14" Laptop ($1440\text{px}$)**: Fit = $127\%$, Steps: `[100, 127]` (1 click to fit).
- **16" MacBook Pro ($1728\text{px}$)**: Fit = $155\%$, Steps: `[100, 125, 155]` (2 clicks to fit).
- **1080p Desktop ($1920\text{px}$)**: Fit = $173\%$, Steps: `[100, 125, 150, 173]` (3 clicks to fit).
- **4K / Ultrawide ($2560\text{px}$)**: Fit = $200\%$, Steps: `[100, 125, 150, 175, 200]` (4 clicks to fit).

### 3. Sub-Pixel Focal Landmark Preservation (`captureViewportLandmark()`):
When zooming or resizing, the user must **never lose their reading place**:
- **Top-of-Page Zero-Drift Rule**: If $scrollY \le 10\text{px}$, anchor is locked to `{ el: null, isTop: true, scrollRatio: 0 }`. Toggling Fit or zooming while at the top pins scroll strictly to `top: 0` ($0.0\text{px}$ drift).
- **Atomic Leaf Proximity Sweep**: Evaluates leaf reading elements (`h1-h4, p, li, pre, table, tr, summary, .mermaid, .dna-card, .callout-glass, blockquote, td, th, code`) within active viewport bounds (`rect.bottom > 64 && rect.top < window.innerHeight`).
- **Container Wrapper Exclusion Invariant**: Never anchor to container wrappers whose boundaries exceed focal reading range (`DETAILS`, `.problem-card`, `.pattern-chapter`). Anchoring to $4{,}000\text{px}$-tall containers causes catastrophic downward drag when scaling!
- **Instant Scroll Halt**: Executes `window.scrollTo({ top: window.scrollY, behavior: 'instant' })` prior to reading coordinates, arresting in-flight smooth scroll animations from corrupting anchor positions.
- **Zero-Transition Stage Wrapper**: `.stage-wrapper` must specify `transition: none !important;`. Any CSS transition interpolation on `max-width` or `zoom` creates asynchronous layout drift during synchronous reflow computation.

### 4. Stepper HUD Controls & Shortcuts:
- Stepper elements: `#zoom-out-btn` (`−`), `#zoom-level-badge` (click to reset to 100%), `#zoom-in-btn` (`+`), and `#zoom-fit-btn` (`⤢ Fit` toggle).
- Global keyboard shortcuts:
  - `Alt+=` or `Alt++`: Zoom In to next adaptive step
  - `Alt+-` or `Alt+_`: Zoom Out to previous adaptive step
  - `Alt+0`: Reset to 100%
  - `Alt+F`: Toggle Dynamic Fit mode
- State persistence: `localStorage.getItem('dsa_content_zoom')`, `localStorage.getItem('dsa_content_fit')`.

---

## 🚀 Liquid-Glass Floating "Back-to-Top" Guider Engine

A fixed liquid-glass squircle button in the bottom-right corner of the viewport:

```html
<button class="floating-back-to-top" id="floating-back-to-top" aria-label="Back to top" title="Back to Top (Home)">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="m18 15-6-6-6 6"></path>
  </svg>
</button>
```

### Critical Operational Invariants:
1. **Geometry & Position**:
   - `width: 38px; height: 38px;` squircle matching `#floating-sidebar-toggle`.
   - `position: fixed; bottom: max(28px, env(safe-area-inset-bottom, 28px)); right: max(28px, env(safe-area-inset-right, 28px)); z-index: 85;`
2. **Scroll-Position Awareness**:
   - Monitored inside the unified `requestAnimationFrame` scroll loop in `app.js`.
   - Hidden at document top (`opacity: 0; visibility: hidden; pointer-events: none`).
   - Smoothly reveals when $scrollY > 350\text{px}$ (`opacity: 1; visibility: visible; pointer-events: auto; transform: translateY(0) scale(1);`).
3. **Decoupled Sidebar Scrolling & Smooth Scroll Immunity**:
   - **The Bug**: Native `targetGroup.scrollIntoView({ behavior: 'smooth' })` inside the sidebar scrollSpy hijacked and terminated the window's ongoing smooth scroll to top midway through execution (e.g. freezing scroll at 7,793px or 5,571px).
   - **The Fix**: Sidebar auto-scrolling must strictly operate on `#main-sidebar` via direct `scrollTop` adjustment (`sidebar.scrollTop += diff;`). It must **never** call `scrollIntoView()` on DOM elements, completely isolating sidebar scrolling from the global window viewport scroll engine.
4. **Anchor Telemetry & Programmatic Scroll Shield**:
   - Clicking sets `STATE.focalAnchor = null` and flags `STATE.isProgrammaticScroll = true`, silencing scrollSpy accordion events during transit.
   - Smoothly scrolls to `top: 0` (`window.scrollTo({ top: 0, behavior: 'smooth' })`).
   - Triggers synthetic tactile audio feedback via `HapticAudio.tap()`.
   - Releases programmatic scroll flag once $scrollY \le 5\text{px}$.

---

## ↔️ Interactive Draggable Sidebar Resizer & Collapsible Rail Standard

The navigation sidebar supports both continuous draggable resizing and full collapsible rail distraction-free mode:

```html
<header class="header-glass">
  <button class="sidebar-dock-toggle" id="sidebar-dock-toggle" aria-label="Toggle Navigation Sidebar" title="Toggle Sidebar (⌘B / [)">...</button>
</header>
<div class="layout-container">
  <button class="floating-sidebar-toggle" id="floating-sidebar-toggle" aria-label="Open Navigation Sidebar" title="Open Sidebar (⌘B / [)">...</button>
  <aside class="sidebar" id="main-sidebar">
    <div class="sidebar-search-row">
      <div class="sidebar-search-box">
        <input type="text" class="sidebar-search-input" id="sidebar-filter-input" ...>
      </div>
      <button class="sidebar-collapse-pill sidebar-close-btn" id="sidebar-close-btn" aria-label="Close navigation sidebar" title="Collapse sidebar (⌘B / [)">...</button>
    </div>
  </aside>
  <div class="sidebar-resizer" id="sidebar-resizer" role="separator" aria-orientation="vertical" aria-label="Resize navigation sidebar" title="Drag to adjust sidebar width (Double-click to reset)"></div>
  <main class="content-area">...</main>
</div>
```

### Operational Invariants:
1. **Icon-Only Floating Squircle**:
   - `#floating-sidebar-toggle` is styled as an **icon-only 38px squircle** (`width: 38px; height: 38px;`).
   - Omission of text label ("Navigation") recovers **98px of horizontal reading space**, allowing content to expand further toward the left edge.
2. **Safe Clearance Gutters**:
   - When sidebar is collapsed, `.content-area` enforces `padding-left: clamp(54px, 4vw, 72px)` to prevent main reading content from being occluded by the floating toggle tab.
3. **Bounds Clamping**: Resizing strictly clamped between `MIN_WIDTH = 240px` and `MAX_WIDTH = 560px`.
4. **Dragging Performance**: During drag, `body.resizing-sidebar` sets `cursor: col-resize !important; user-select: none !important;`.
5. **Persistence**: Width choice is saved to `localStorage.setItem('dsa_sidebar_width', width)`.
6. **Double-Click Reset**: Double-clicking resets `--sidebar-width` to default `330px`.
7. **Zero-Truncation Invariant**: Never clip navigation titles with single-line ellipses (`white-space: normal; word-break: break-word`).

---

## 📐 Inter-Pattern Tile Spacing ($24\text{px}$)

All 48 algorithmic pattern and theoretical foundation chapters are enclosed within `#all-pattern-chapters`:

```css
#all-pattern-chapters {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
```

### Spacing Invariants:
1. **Consistent Card Separation**: Guarantees an exact $24\text{px}$ visual breathing margin between all chapter squircle cards without collapsing margins.
2. **Zoom Immunity**: Spacing is contained within flex layout flow, scaling naturally and proportionally under CSS zoom factors ($100\%$ to $200\%$) without overlapping or text collisions.

---

## 📱 Commute Gadget Mobile Navigation Architecture

1. On viewports $\le 1024\text{px}$, sidebar transitions into an off-canvas slide-out drawer (`width: min(86vw, 360px)`).
2. **Stacking Context Invariant**: `#mobile-drawer-backdrop` (`z-index: 1100`) must be placed inside `.layout-container` right before `.sidebar` (`z-index: 1200`).
3. **Sticky Scroll Invariant**: **Never use `overflow-x: hidden` on `html` or `body`**. Always use `overflow-x: clip;` to prevent breaking `position: sticky`.
4. Wrap all `<table>` elements in `<div class="table-wrapper">` with horizontal touch scrolling and explicit min-width (`min-width: 520px`).

---

## 🎯 Universal Delegated In-Page Navigation

All in-page anchors (`a[href^="#"]`) use delegated event interception in `app.js`:
1. Intercepts click and cancels native jump.
2. Checks if target element or any ancestor is collapsed (`.pattern-chapter.is-collapsed` or closed `<details>`).
3. Automatically uncollapses containing chapters, opens `<details>`, and updates toggle buttons.
4. Forces synchronous layout flush (`targetEl.getBoundingClientRect()`).
5. Smoothly scrolls with exact 72px cushion:
   ```javascript
   const y = targetEl.getBoundingClientRect().top + window.pageYOffset - 72;
   window.scrollTo({ top: y, behavior: 'smooth' });
   ```
6. Applies a temporary flash focus highlight (`flash-focus`) for 1800ms to ground the user. Zero treasure hunting!

---

## ⚡ Sub-10ms "Expand All" SLA

When opening all 48 chapters and 374 `<details>` elements simultaneously:
- **Root-Cause Pitfall**: Synchronous execution of diagram render calls inside accordion `toggle` events freezes the CPU for 11+ seconds!
- **The Protocol**: Guard accordion `toggle` listeners with `STATE.isBatchExpanding`:
  ```javascript
  STATE.isBatchExpanding = true;
  document.querySelectorAll('.pattern-chapter').forEach(c => c.classList.remove('is-collapsed'));
  document.querySelectorAll('.problem-card, .theory-details').forEach(d => { d.open = true; });
  setTimeout(() => {
    STATE.isBatchExpanding = false;
    renderVisibleDiagrams();
  }, 50);
  ```
  This drops "Expand All" execution time from 11,500ms down to **5.1ms** (2,250x faster) while lazy observers handle offscreen diagrams.

---

## 📊 Mermaid Diagram & Safari WebKit Layout Rules

### 1. Isolated `mermaid.render()` Execution:
Never rely on uncoordinated `mermaid.run()`. Always use isolated, direct rendering:
```javascript
const { svg, bindFunctions } = await window.mermaid.render(renderId, code);
el.innerHTML = svg;
if (bindFunctions) bindFunctions(el);
```

### 2. The Safari WebKit Flex-SVG Sizing Invariant:
- **Never use `width: auto !important` on `.mermaid svg`** inside flex containers. In WebKit/Safari, an SVG with percentage width and `width: auto` collapses to `0px × 0px`!
- **CSS Rule**:
  ```css
  .mermaid svg {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    max-height: 580px !important;
    object-fit: contain;
    margin: 0 auto;
  }
  ```
- **Intrinsic Dimension Injection**:
  Extract `vbW` and `vbH` from the SVG's `viewBox` and inject explicit W3C attributes:
  ```javascript
  svgEl.setAttribute('width', vbW);
  svgEl.setAttribute('height', vbH);
  svgEl.style.aspectRatio = `${vbW} / ${vbH}`;
  ```

### 3. Escaping & Syntax Cleanliness:
- Escape `<` and `>` in node labels as `&lt;` / `&gt;` or `≤` / `≥`.
- Every diagram MUST have a globally unique `id="mermaid-diagram-{uid}"`.
- Proactively render visible diagrams on chapter expand (`renderVisibleDiagrams(chapter)`), backed by a passive `requestAnimationFrame` scroll watcher.

---

## 🔍 Fullscreen Theater Mode Workbench

The fullscreen theater view is implemented using native HTML5 `<dialog id="theater-modal">`:

### Critical Invariants:
1. **Sub-Millisecond Zoom/Pan SLA**:
   - `.theater-content-surface` MUST specify `transition: none !important;`. Any CSS transition interpolation on zoom/pan destroys responsiveness.
   - Cache `cachedVbW` and `cachedVbH` upon open to eliminate forced reflows during zoom.
   - Zoom In (`+`), Zoom Out (`−`), 100% Reset, and Fit execute in **0.00ms to 0.20ms**.
2. **Clear UX Distinction: `100%` vs `Fit`**:
   - `100%` (`theaterZoomReset`): Resets scale to **`1.0`** (true 1:1 native pixel design scale).
   - `Fit` (`theaterZoomFit`): Dynamically calculates exact scale based on live viewport boundaries and SVG `viewBox` (`scale = Math.min(availW / vbW, availH / vbH)`), reporting calculated value in the badge.
3. **Anti-Dismissal Rule (No Accidental Close)**:
   - Clicks or drag-releases on `.theater-viewport` or SVG canvas MUST NEVER close the modal!
   - **Only** the explicit Close button (`✕`) or the `Escape` key closes the theater.
4. **Diagram Text Selection**:
   - `.theater-content-surface svg text, foreignObject, span` must have `user-select: text !important; cursor: text;`.
   - In `pointerdown`, text elements are excluded from pan capture so users can freely select, highlight, and copy code and formulas.
5. **Exact Scroll Position Restoration**:
   - Save `scrollY` before modal open.
   - Restore with `window.scrollTo({ top: savedScrollY, behavior: 'instant' })` on close.
   - Highlight source diagram with `flash-focus` inside `requestAnimationFrame`.

---

## 📐 Unicode Monospace Box-Drawing Table & Card Alignment

ASCII and Unicode box-drawing tables and callout cards must align with 100% mathematical precision in all monospace environments.

### The Display-Width Rules (UAX #11):
- **Emojis & Wide Characters**: Width = **2 columns** (`🟢`, `🟡`, `🔴`, `🟣`, `🚗`, `🛑`, `🎯`, `✅`, `💥`, `⚡`, `⚠️`, `0x1F000`–`0x1FAFF`).
- **Combining Marks & Selectors**: Width = **0 columns** (`\uFE0F` variation selector, `\u200D` ZWJ, `Mn`, `Me`).
- **Mathematical & Box Characters**: Width = **1 column** (`Ω`, `Θ`, `≤`, `≥`, `➜`, `─`, `│`, `┌`, `┐`, `└`, `┘`, `├`, `┤`, `┬`, `┴`, `┼`).

### Automation Tool:
- Linter & Formatter: `scripts/audit_ascii_boxes.py`
  - `python3 scripts/audit_ascii_boxes.py --check`: Validates all boxes across repository markdown files.
  - `python3 scripts/audit_ascii_boxes.py --fix`: Realigns all tables, cards, and pills in place.
- Run via Makefile: `make test-boxes` or `make format-boxes`.

---

## 🔊 Curated Web Audio Haptic System (`HapticAudio`)

A tactile acoustic feedback engine built directly on the Web Audio API without external audio file dependencies. Synthesizes directional micro-transients for every user action:

| Action / Interaction | Synthesis Curve | Frequency / Duration | Aesthetic Sensation |
|---|---|---|---|
| **Expand (`expand`)** | Ascending exponential sine ramp | `540Hz → 880Hz` (`38ms`) | Mechanical switch unfolding / opening |
| **Collapse (`collapse`)** | Descending exponential sine ramp | `780Hz → 420Hz` (`38ms`) | Snappy mechanical tuck / folding shut |
| **Sidebar Open (`sidebarOpen`)** | Resonant ascending triangle glide | `440Hz → 760Hz` (`55ms`) | Smooth sliding panel reveal |
| **Sidebar Close (`sidebarClose`)** | Solid mechanical sine latch | `680Hz → 320Hz` (`45ms`) | Secure latch click |
| **Tactile Tap (`tap`)** | High-transient triangle pop | `920Hz → 560Hz` (`22ms`) | iOS-style segmented chip toggle & back-to-top |
| **Copy Code (`copySuccess`)** | Dual-tone arpeggiated chime | `C6 (1046Hz) + E6 (1318Hz)` (`90ms`) | Celebratory clipboard success chime |
| **Search Trigger (`searchOpen`)** | Holographic digital ping | `1180Hz → 1480Hz` (`40ms`) | Futuristic HUD activation |
| **Theme Change (`themeChange`)** | Cosmic frequency sweep | `600Hz → 1200Hz` (`60ms`) | Dimension / palette shift |
| **Theater Launch (`theaterOpen`)** | Low-frequency harmonic sine | `440Hz → 880Hz` (`70ms`) | Cinematic workbench focus |

### Acoustic Invariants:
1. **Directional Consistency**: Main content chapters, problem cards (`<details class="problem-card">`), theory cards (`<details class="theory-details">`), nested researcher accordions (`<details class="md-details">`), and sidebar tree headers share the exact same `HapticAudio.expand()` and `HapticAudio.collapse()` curves.
2. **Back-to-Top Audio**: Back-to-top button activation uses `HapticAudio.tap()`. Never invoke non-existent `HapticAudio.click()`!
3. **Batch Expansion Guard**: During "Expand All" and "Collapse All", `STATE.isBatchExpanding` strictly mutes individual accordion blips to eliminate audio distortion and DOM thread starvation.
4. **Audio Persistence**: State saved to `localStorage.getItem('dsa_audio_enabled')`, defaulting to ON for tactile mobile-like delight. Toggled via HUD `🔊 / 🔇`.

---

## 🧪 16-Gate Headless Automated Verification Suite

Run before every commit or push:
```bash
make docs-test
```

All 16 quality gates must pass deterministically:
1. **Core Assets Presence**: `index.html`, `style.css`, `app.js`, `catalog/manifest.json`.
2. **Catalog Completeness & Search Index**: 44 patterns, 288+ indexed problems.
3. **Mermaid Label Escaping**: No unescaped `<` or `>` inside node labels.
4. **CSS SVG Sizing Invariants**: No `width: auto !important` on `.mermaid svg`.
5. **KaTeX Integration**: Delimiters, styles, and auto-render execution.
6. **Draggable Sidebar Resizer**: Bounds clamping, `col-resize`, and `localStorage` persistence.
7. **Mobile Drawer & Anti-Clobbering**: Sticky-safe `overflow-x: clip;` and z-index hierarchy.
8. **Table & Touch Containment**: `.table-wrapper` with touch scrolling and `min-width: 520px`.
9. **Relative Path Invariants**: All asset links use relative addressing (`./`) for `/DSA/` GitHub Pages.
10. **Static Bundle Footprint**: Bundle size strictly $<25\text{MB}$.
11. **Mermaid ID Uniqueness & Clean Navigation**: 460 unique IDs, isolated rendering, zero legacy footer links.
12. **Unicode Monospace Box-Drawing Alignment**: 100% of ASCII and Unicode box tables and cards aligned.
13. **Collapsible Details & Zero Raw HTML Block Escaping**: Zero raw unrendered or escaped `&lt;details&gt;` / `&lt;summary&gt;` text; 100% semantic `<details class="md-details">` with `.md-summary` and `.md-details-body`.
14. **Monospace Semantic Badging & ASCII Tree Geometric Alignment**: Zero occurrences of `⚡ TEXT Implementation`; 100% content-aware semantic badges (`dna-label-code`, `dna-label-matrix`, `dna-label-memory`, `dna-label-trace`, `dna-label-tree`, `dna-label-blueprint`, `dna-label-spec`); mathematical geometric centering of ASCII tree root nodes over `/ \` branches with zero snapped roots.
15. **Universal Hyperlink Integrity & Local Path Prevention**: Zero `file://` or `/Users/` paths; zero raw `.md` or `.py` file links; zero external GitHub jumps for internal files; zero notebook-style previous/next/chapter footer navigation artifacts; 100% internal fragment anchor (`href="#..."`) resolution to on-page elements.
16. **Dynamic Adaptive Content Zoom, Stage Width Engine & Floating Controls**: Dynamic screen-width bounded zoom calculation ($Z_{\text{fit}} = W_{\text{avail}} / W_{\text{base}}$: $100\%$ on mobile, up to $175\%$ on MacBook Pro, up to $200\%$ on external 4K displays); adaptive step ladder synthesizing 2 to 4 punchy steps (e.g. 25% increments); segmented glass stepper pill (`#hud-zoom-stepper`) with `−`, current `%` badge, `+`, and one-click `⤢ Fit`; icon-only 38px squircle `#floating-sidebar-toggle` recovering 98px of horizontal reading space; `#floating-back-to-top` 38px squircle with scroll awareness ($scrollY > 350\text{px}$), anchor clearing, and decoupled sidebar scrolling immunity; safe clearance gutter on `.content-area` (`padding-left: clamp(54px, 4vw, 72px)`) when sidebar is collapsed; mobile scroll containment (locked to 100% on $\le 768\text{px}$).

---

## 🛠️ Canonical Developer Commands

| Command | Purpose |
|---|---|
| `make help` | Interactive targets menu |
| `make docs-build` | Compiles 44 patterns and generates hydrated static site in `_site/` |
| `make docs-serve` | Serves documentation locally on `http://localhost:4000/` |
| `make docs-test` | Runs the full 16-gate headless verification suite |
| `make test-zoom` | Audits dynamic adaptive content zoom and stage width fitting (Gate 16) |
| `make test-links` | Audits universal hyperlink integrity, SPA containment, and zero local path leaks (Gate 15) |
| `make test-trees` | Audits monospace semantic badges and ASCII tree alignments (Gate 14) |
| `make test-details` | Audits collapsible elements and raw HTML block invariants (Gate 13) |
| `make test-boxes` | Audits Unicode monospace box-drawing alignment (Gate 12) |
| `make format-boxes` | Realigns and formats all ASCII/Unicode boxes across the repository in place |
| `make test` | Runs AST syntax compilation across all Python implementations + box checks |
| `make lint` | Runs Ruff linter + box alignment check |
| `make clean` | Cleans `_site/` and pycache artifacts |
