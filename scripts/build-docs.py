#!/usr/bin/env python3
"""
==============================================================================
build-docs.py — Zero-Dependency DSA Living Documentation Catalog Compiler
Compiles 44 patterns, 00-Fundamentals, 328 walkthroughs, and 305 Python solutions
into a hyper-responsive, high-performance static GitHub Pages Documentation Portal.
Features full Markdown-to-HTML rendering, collapsible chapters with Focus Mode,
dynamic chevrons, and complete integration of theoretical foundations and engines.
==============================================================================
"""

import os
import re
import json
import html
import shutil
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DOCS_SITE_DIR = ROOT_DIR / "docs" / "site"
SITE_DIR = ROOT_DIR / "_site"
CATALOG_DIR = SITE_DIR / "catalog"

FAMILIES = {
    "Runners": {
        "icon": "🏃",
        "desc": "Two things moving through data. Shrink from both sides or slide a window.",
        "patterns": ["01 - Warmup", "02 - Two Pointers", "03 - Fast & Slow Pointers", "04 - Sliding Window"]
    },
    "Sorters": {
        "icon": "📦",
        "desc": "Put items in the right place. Handle overlapping intervals or direct index cyclic placement.",
        "patterns": ["05 - Merge Intervals", "06 - Cyclic Sort", "35 - Linear Sorting Algorithm"]
    },
    "Explorers": {
        "icon": "🌲",
        "desc": "Traverse trees, graphs, grids, or explore all permutations and subsets.",
        "patterns": ["11 - Tree Breadth First Search", "12 - Tree Depth First Search", "13 - Graphs", "14 - Island (Matrix Traversal)", "16 - Subsets", "25 - Backtracking"]
    },
    "Rankers": {
        "icon": "📊",
        "desc": "Find the top/bottom K elements, running medians, or multi-stream merges.",
        "patterns": ["15 - Two Heaps", "19 - Top K Elements", "20 - K-way Merge"]
    },
    "Searchers": {
        "icon": "🔍",
        "desc": "Cut search spaces in half, prefix matching with tries, or O(1) hash maps.",
        "patterns": ["10 - Hash Maps", "17 - Modified Binary Search", "26 - Trie", "36 - Meet in the Middle"]
    },
    "Counters": {
        "icon": "🧮",
        "desc": "Count ways, range sums, or optimize values via dynamic programming and prefix trees.",
        "patterns": ["21 - Greedy Algorithms", "22 - 0-1 Knapsack (DP)", "23 - Fibonacci Numbers (DP)", "24 - Palindromic Subsequence (DP)", "30 - Prefix Sum", "32 - Counting Pattern", "37 - MO's Algorithm", "41 - Segment Tree", "42 - Binary Indexed Tree"]
    },
    "Connectors": {
        "icon": "🔗",
        "desc": "Manage disjoint sets, task scheduling orders, node cloning, or graph articulation bridges.",
        "patterns": ["07 - In-place Reversal of a LinkedList", "08 - Stacks", "09 - Monotonic Stack", "27 - Topological Sort (Graph)", "28 - Union Find", "29 - Ordered Set", "31 - Multi-threaded", "33 - Monotonic Queue Pattern", "34 - Simulation Pattern", "38 - Serialize and Deserialize", "39 - Clone Pattern", "40 - Articulation Points and Bridges", "43 - Miscellaneous"]
    }
}

def get_family_for_pattern(pattern_name: str) -> str:
    for fam, data in FAMILIES.items():
        if pattern_name in data["patterns"]:
            return fam
    return "Connectors"

def sanitize_mermaid(content: str) -> str:
    """
    Robust targeted sanitizer for Mermaid diagrams:
    - Encloses unquoted curly braces containing (), ?, or = in double quotes
    - Encloses unquoted edge labels containing () or [] in double quotes
    - Fixes specific raw syntax outliers and nested quotes across markdown files
    """
    # 1. Enclose unquoted curly braces containing () or ? or = in quotes
    def repl_curly(m):
        inner = m.group(1).strip()
        if inner.startswith('"') and inner.endswith('"'):
            return m.group(0)
        clean = inner.replace('"', "'")
        return f'{{"{clean}"}}'
    content = re.sub(r'\{([^{}\n]*[\(\)\?=][^{}\n]*)\}', repl_curly, content)

    # 2. Enclose unquoted edge labels containing () or [] in quotes
    def repl_edge(m):
        arr = m.group(1)
        lbl = m.group(2).strip()
        if lbl.startswith('"') and lbl.endswith('"'):
            return m.group(0)
        clean = lbl.replace('"', "'")
        return f'{arr}|"{clean}"|'
    content = re.sub(r'(-->|-.->|==>)\|([^|\n]*[\(\)\[\]][^|\n]*)\|', repl_edge, content)

    # 3. Fix specific files with nested quotes / brackets inside node labels
    content = content.replace('min_capital_heap\\n["(0,1), (1,2), (1,3)"]', 'min_capital_heap\\n[(0,1), (1,2), (1,3)]')
    content = content.replace('min_capital_heap\n["(0,1), (1,2), (1,3)"]', 'min_capital_heap\n[(0,1), (1,2), (1,3)]')
    content = content.replace('Heap recovers:\\n["(-1, -2, 2),\\n (-1, -1, 1)"]', 'Heap recovers:\\n[(-1, -2, 2), (-1, -1, 1)]')
    content = content.replace('Heap recovers:\n["(-1, -2, 2),\n (-1, -1, 1)"]', 'Heap recovers:\n[(-1, -2, 2), (-1, -1, 1)]')
    content = content.replace('Heap recovers:\\n["(-1, -1, 1)"]', 'Heap recovers:\\n[(-1, -1, 1)]')
    content = content.replace('Heap recovers:\n["(-1, -1, 1)"]', 'Heap recovers:\n[(-1, -1, 1)]')
    content = content.replace('Initial:\\n["(1, L2), (2, L0), (3, L1)"]', 'Initial:\\n[(1, L2), (2, L0), (3, L1)]')
    content = content.replace('Initial:\n["(1, L2), (2, L0), (3, L1)"]', 'Initial:\n[(1, L2), (2, L0), (3, L1)]')
    content = content.replace('dp["0..11"]', 'dp[0..11]')
    content = content.replace('buckets["0..max_freq"]', 'buckets[0..max_freq]')
    content = content.replace('count["3..25"]', 'count[3..25]')

    # 4. Fix known syntax outliers across markdown files
    content = content.replace(': slide right: ', ': slide right ')
    content = content.replace('Iteration 5', 'Iteration5')
    content = content.replace('Good Choice -.->', 'GoodChoice -.->')
    content = content.replace('Good Choice fill', 'GoodChoice fill')
    content = content.replace('Bad Choice fill', 'BadChoice fill')
    content = content.replace('subgraph State2 [State 2: Insert [2, 2]]', 'subgraph State2 ["State 2: Insert (2, 2)"]')
    content = content.replace('subgraph State 2: Insert [2, 2]', 'subgraph State2 ["State 2: Insert (2, 2)"]')
    content = content.replace('styleW3fill', 'style W3 fill')
    content = content.replace('styleFfill', 'style F fill')
    content = content.replace('{\"' + "'l': 2, 'o': 2, 'v': 1, 'e': 4...\"}\"", "[\"'l': 2, 'o': 2, 'v': 1, 'e': 4...\"]")
    content = content.replace("ProcessNote 'a' (again)", 'ProcessNoteAAgain')
    content = content.replace("ProcessNote 'a'", 'ProcessNoteA')
    content = content.replace('Add 2', 'Add2')
    content = content.replace('Add 3', 'Add3')
    content = content.replace('Heap: {"0(L1), 4(L0), 5(L2)"}', 'Heap: [0(L1), 4(L0), 5(L2)]')
    content = content.replace('subgraphIteration', 'subgraph Iteration')
    content = content.replace('subgraphPass2: Assign Randoms', 'subgraph Pass2 ["Pass 2: Assign Randoms"]')
    content = content.replace('subgraphQuery(i)', 'subgraph QueryI ["Query(i)"]')
    content = content.replace('== Average = 3.5 ==>', '== "Average = 3.5" ==>')
    content = content.replace('Bad Choice -.->', 'BadChoice -.->')
    content = content.replace('Is it a Start?', 'IsItAStart')
    content = content.replace('Process Note', 'ProcessNote')
    content = content.replace('Look-Ahead Check', 'LookAheadCheck')
    content = content.replace('Iteration 4', 'Iteration4')
    content = content.replace('Add 1', 'Add1')
    content = content.replace('S1 --> S2 : slide right: −2, +1    S2 --> S3 :', 'S1 --> S2 : slide right (-2, +1)\n    S2 --> S3 :')

    return content

_MERMAID_DIAGRAM_COUNTER = 0

HTML_TAG_PATTERN = re.compile(
    r'</?(?:details|summary|b|strong|i|em|u|code|pre|kbd|span|sub|sup|br|hr|div|table|thead|tbody|tr|th|td|a|img|ul|ol|li|blockquote|mark|p|small|del|ins)'
    r'(?:\s+[^<>]*)?/?>',
    re.IGNORECASE
)

def render_markdown(text: str) -> str:
    """
    Robust zero-dependency Markdown-to-HTML converter.
    Parses code blocks, Mermaid diagrams, KaTeX formulas, tables, blockquotes,
    headers, lists, bold/italic, and inline code.
    """
    global _MERMAID_DIAGRAM_COUNTER
    if not text:
        return ""

    # Strip legacy repository folder navigation footers (e.g. ## 🧭 Navigation)
    text = re.sub(r'(?m)^---\s*\n+#+\s*🧭\s*Navigation.*?(?=\Z|\n#)', '', text, flags=re.DOTALL)
    text = re.sub(r'(?m)^#+\s*🧭\s*Navigation.*?(?=\Z|\n#)', '', text, flags=re.DOTALL)
    text = re.sub(r'(?m)^\s*-\s*\*\*(?:Hub|Next|Previous|Next Chapter|Engine Rooms)\*\*:\s*\[.*?\].*$', '', text)

    # Map relative repository markdown links to single-page anchors
    text = re.sub(r'\((\./)?015%20-%20Trees%20\(The%20Complete%20Guide\)/README\.md\)', '(#sec-fundamentals-trees)', text)
    text = re.sub(r'\((\./)?016%20-%20Graphs%20\(The%20Complete%20Guide\)/README\.md\)', '(#sec-fundamentals-graphs)', text)
    text = re.sub(r'\((\./)?015\s*-\s*Trees[^)]*?README\.md\)', '(#sec-fundamentals-trees)', text)
    text = re.sub(r'\((\./)?016\s*-\s*Graphs[^)]*?README\.md\)', '(#sec-fundamentals-graphs)', text)
    text = re.sub(r'\((\./)?000\s*-\s*Theoretical[^)]*?README\.md\)', '(#sec-fundamentals-theory)', text)
    text = re.sub(r'\((\./)?(\d{2}_[^)]+)\.md\)', r'(#fund-theo-\2)', text)

    # 1. Protect code blocks & Mermaid blocks
    blocks = []
    def save_code_block(m):
        global _MERMAID_DIAGRAM_COUNTER
        lang = m.group(1).strip() if m.group(1) else "text"
        code = m.group(2)
        idx = len(blocks)
        if lang.lower() == "mermaid":
            _MERMAID_DIAGRAM_COUNTER += 1
            diag_id = f"mermaid-diagram-{_MERMAID_DIAGRAM_COUNTER}"
            escaped_mermaid = sanitize_mermaid(code.strip())
            block_html = f'''<div class="canvas-container" id="canvas-{diag_id}">
              <div class="canvas-header-bar">
                <span class="canvas-type-tag">Algorithm State Machine · Flow Execution</span>
                <div class="canvas-controls-group">
                  <button class="canvas-tool-btn zoom-out-btn" title="Zoom Out">−</button>
                  <span class="zoom-level-badge">100%</span>
                  <button class="canvas-tool-btn zoom-in-btn" title="Zoom In">+</button>
                  <button class="canvas-tool-btn zoom-reset-btn" title="Reset Zoom">⟲</button>
                  <button class="canvas-tool-btn fullscreen-btn" title="View Fullscreen Theater">⛶</button>
                </div>
              </div>
              <div class="canvas-viewport">
                <div class="canvas-content-surface">
                  <pre class="mermaid" id="{diag_id}">
{html.escape(escaped_mermaid)}
                  </pre>
                </div>
              </div>
              <div class="canvas-caption">State convergence & algorithmic execution graph</div>
            </div>'''
        else:
            block_html = f'''<div class="dna-skeleton-box">
              <div class="dna-skeleton-header">
                <span class="dna-label">⚡ {lang.upper()} Implementation</span>
                <button class="copy-btn" onclick="navigator.clipboard.writeText(this.closest('.dna-skeleton-box').querySelector('pre code').innerText);this.innerText='Copied!';setTimeout(()=>this.innerText='Copy',1600);">Copy</button>
              </div>
              <div class="code-container">
                <pre><code class="language-{lang}">{html.escape(code.strip())}</code></pre>
              </div>
            </div>'''
        blocks.append(block_html)
        return f"\n\n__BLOCK_PLACEHOLDER_{idx}__\n\n"

    text = re.sub(r'```([a-zA-Z0-9_-]*)\n(.*?)```', save_code_block, text, flags=re.DOTALL)

    # 2. Protect display math $$...$$
    math_blocks = []
    def save_display_math(m):
        idx = len(math_blocks)
        math_content = m.group(1).strip()
        math_blocks.append(f'<div class="katex-display">$${math_content}$$</div>')
        return f"\n\n__MATH_PLACEHOLDER_{idx}__\n\n"

    text = re.sub(r'\$\$(.*?)\$\$', save_display_math, text, flags=re.DOTALL)

    # 3. Robust line-by-line Markdown Table parsing
    raw_lines = text.split('\n')
    table_processed_lines = []
    i = 0
    n = len(raw_lines)
    while i < n:
        line = raw_lines[i]
        stripped = line.strip()
        # Lookahead: line contains '|' and next line is table separator (|---|---| or ---|---)
        if i + 1 < n and '|' in stripped and not stripped.startswith('__BLOCK_') and not stripped.startswith('__MATH_'):
            next_stripped = raw_lines[i + 1].strip()
            is_sep = bool(re.match(r'^[\|\-:\s]+$', next_stripped) and '-' in next_stripped and '|' in next_stripped)
            if is_sep:
                headers = [c.strip() for c in stripped.strip('|').split('|')]
                table_rows = []
                j = i + 2
                while j < n:
                    row_stripped = raw_lines[j].strip()
                    if not row_stripped or ('|' not in row_stripped and not row_stripped.startswith('|')):
                        break
                    protected = row_stripped.replace(r'\|', '__ESCAPED_PIPE__')
                    cells = [c.strip().replace('__ESCAPED_PIPE__', '|') for c in protected.strip('|').split('|')]
                    table_rows.append(cells)
                    j += 1

                t_html = ['<div class="table-wrapper"><table><thead><tr>']
                for h in headers:
                    t_html.append(f'<th>{inline_formatting(h)}</th>')
                t_html.append('</tr></thead><tbody>')
                for r in table_rows:
                    t_html.append('<tr>')
                    for c in r:
                        t_html.append(f'<td>{inline_formatting(c)}</td>')
                    t_html.append('</tr>')
                t_html.append('</tbody></table></div>')

                table_processed_lines.append('\n' + ''.join(t_html) + '\n')
                i = j
                continue
        table_processed_lines.append(line)
        i += 1

    # 4. Process line by line for headers, blockquotes, lists, hr, details/summaries
    lines = table_processed_lines
    out_lines = []
    in_list = False
    list_type = None
    in_blockquote = False
    blockquote_lines = []
    details_stack = []

    def flush_blockquote():
        nonlocal in_blockquote, blockquote_lines
        if in_blockquote:
            content = '<br>'.join(blockquote_lines)
            out_lines.append(f'<blockquote class="callout-glass">{content}</blockquote>')
            in_blockquote = False
            blockquote_lines = []

    for line in lines:
        stripped = line.strip()

        # Check for blockquote continuation
        if stripped.startswith('>'):
            b_text = stripped[1:].strip()
            if b_text.startswith('**') or b_text:
                blockquote_lines.append(inline_formatting(b_text))
            in_blockquote = True
            continue
        else:
            flush_blockquote()

        # Check for list ending
        if in_list and not (stripped.startswith('- ') or stripped.startswith('* ') or re.match(r'^\d+\.\s', stripped)):
            out_lines.append(f'</{list_type}>')
            in_list = False
            list_type = None

        if not stripped:
            out_lines.append('')
            continue

        # Placeholders pass through
        if stripped.startswith('__BLOCK_PLACEHOLDER_') or stripped.startswith('__MATH_PLACEHOLDER_'):
            if details_stack and not details_stack[-1]['body_open']:
                out_lines.append('<div class="md-details-body">')
                details_stack[-1]['body_open'] = True
            out_lines.append(stripped)
            continue

        # Horizontal rule
        if re.match(r'^(-{3,}|\*{3,}|_{3,})$', stripped):
            if details_stack and not details_stack[-1]['body_open']:
                out_lines.append('<div class="md-details-body">')
                details_stack[-1]['body_open'] = True
            out_lines.append('<hr class="md-divider">')
            continue

        # 4a. Single-line <details><summary>...</summary>
        m_both = re.match(r'^<details(?:\s+([^>]*))?>\s*<summary(?:\s+[^>]*)?>(.*?)</summary>(.*)', stripped, re.IGNORECASE)
        if m_both:
            if in_list:
                out_lines.append(f'</{list_type}>')
                in_list = False
                list_type = None
            attrs = m_both.group(1) or ""
            is_open = 'open' in attrs.lower()
            open_attr = ' open' if is_open else ''
            raw_title = m_both.group(2).strip()
            rest = m_both.group(3).strip()
            formatted_title = inline_formatting(raw_title)
            out_lines.append(f'<details class="md-details"{open_attr}>')
            out_lines.append(f'<summary class="md-summary"><span class="md-summary-title">{formatted_title}</span><span class="md-summary-chevron">▶</span></summary>')
            out_lines.append('<div class="md-details-body">')
            details_stack.append({'body_open': True})
            if rest:
                if rest.lower() == '</details>':
                    out_lines.append('</div>')
                    out_lines.append('</details>')
                    details_stack.pop()
                else:
                    out_lines.append(f'<p class="md-p">{inline_formatting(rest)}</p>')
            continue

        # 4b. Opening <details> container
        m_details = re.match(r'^<details(?:\s+([^>]*))?>', stripped, re.IGNORECASE)
        if m_details:
            if in_list:
                out_lines.append(f'</{list_type}>')
                in_list = False
                list_type = None
            attrs = m_details.group(1) or ""
            is_open = 'open' in attrs.lower()
            open_attr = ' open' if is_open else ''
            out_lines.append(f'<details class="md-details"{open_attr}>')
            details_stack.append({'body_open': False})
            continue

        # 4c. <summary>...</summary> tag
        m_summary = re.match(r'^<summary(?:\s+[^>]*)?>(.*?)</summary>', stripped, re.IGNORECASE)
        if m_summary:
            if in_list:
                out_lines.append(f'</{list_type}>')
                in_list = False
                list_type = None
            raw_title = m_summary.group(1).strip()
            formatted_title = inline_formatting(raw_title)
            out_lines.append(f'<summary class="md-summary"><span class="md-summary-title">{formatted_title}</span><span class="md-summary-chevron">▶</span></summary>')
            out_lines.append('<div class="md-details-body">')
            if details_stack:
                details_stack[-1]['body_open'] = True
            continue

        # 4d. Closing </details> tag
        if stripped.lower() == '</details>' or stripped.lower().endswith('</details>'):
            if in_list:
                out_lines.append(f'</{list_type}>')
                in_list = False
                list_type = None
            if stripped.lower() != '</details>':
                before = stripped[:-10].strip()
                if before:
                    out_lines.append(f'<p class="md-p">{inline_formatting(before)}</p>')
            if details_stack:
                info = details_stack.pop()
                if info['body_open']:
                    out_lines.append('</div>')
            else:
                out_lines.append('</div>')
            out_lines.append('</details>')
            continue

        # Ensure body is open if content is encountered inside a details block without summary
        if details_stack and not details_stack[-1]['body_open']:
            out_lines.append('<div class="md-details-body">')
            details_stack[-1]['body_open'] = True

        # Headings
        if stripped.startswith('#### '):
            out_lines.append(f'<h5 class="md-h5">{inline_formatting(stripped[5:])}</h5>')
            continue
        if stripped.startswith('### '):
            out_lines.append(f'<h4 class="md-h4">{inline_formatting(stripped[4:])}</h4>')
            continue
        if stripped.startswith('## '):
            out_lines.append(f'<h3 class="md-h3">{inline_formatting(stripped[3:])}</h3>')
            continue
        if stripped.startswith('# '):
            out_lines.append(f'<h2 class="md-h2">{inline_formatting(stripped[2:])}</h2>')
            continue

        # Unordered list
        if stripped.startswith('- ') or stripped.startswith('* '):
            if not in_list:
                out_lines.append('<ul class="md-list">')
                in_list = True
                list_type = 'ul'
            out_lines.append(f'<li>{inline_formatting(stripped[2:])}</li>')
            continue

        # Ordered list
        m_ol = re.match(r'^\d+\.\s+(.*)', stripped)
        if m_ol:
            if not in_list:
                out_lines.append('<ol class="md-list-ol">')
                in_list = True
                list_type = 'ol'
            out_lines.append(f'<li>{inline_formatting(m_ol.group(1))}</li>')
            continue

        # Table wrapper markup pass through
        if stripped.startswith('<div class="table-wrapper">') or stripped.startswith('<table>') or stripped.startswith('</div>'):
            out_lines.append(line)
            continue

        # Regular paragraph
        out_lines.append(f'<p class="md-p">{inline_formatting(stripped)}</p>')

    flush_blockquote()

    if in_list:
        out_lines.append(f'</{list_type}>')

    while details_stack:
        info = details_stack.pop()
        if info['body_open']:
            out_lines.append('</div>')
        out_lines.append('</details>')

    result = '\n'.join(out_lines)

    # 5. Restore placeholders
    for idx, b_html in enumerate(blocks):
        result = result.replace(f'__BLOCK_PLACEHOLDER_{idx}__', b_html)
    for idx, m_html in enumerate(math_blocks):
        result = result.replace(f'__MATH_PLACEHOLDER_{idx}__', m_html)

    return result

def inline_formatting(text: str) -> str:
    """Parses inline bold, italic, code, links, and escapes raw < and > while preserving valid HTML."""
    if not text:
        return ""
    # Protect inline code: `code`
    code_inlines = []
    def save_inline_code(m):
        idx = len(code_inlines)
        code_inlines.append(f'<code>{html.escape(m.group(1))}</code>')
        return f"__INLINE_CODE_{idx}__"
    
    text = re.sub(r'`([^`]+)`', save_inline_code, text)
    
    # Protect valid HTML tags from angle bracket escaping
    saved_html_tags = []
    def save_html_tag(m):
        idx = len(saved_html_tags)
        saved_html_tags.append(m.group(0))
        return f"__HTML_TAG_{idx}__"
        
    text = HTML_TAG_PATTERN.sub(save_html_tag, text)

    # Math symbols & raw comparison angle brackets
    text = text.replace('<=', '≤').replace('>=', '≥')
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    
    # Bold italic: ***bold italic***
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold: **bold**
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    # Italic: *italic* or _italic_
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    text = re.sub(r'(?<!\w)_([^_]+)_(?!\w)', r'<em>\1</em>', text)
    # Links: [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    
    # Restore valid HTML tags
    for idx, tag in enumerate(saved_html_tags):
        text = text.replace(f"__HTML_TAG_{idx}__", tag)

    # Restore inline code
    for idx, c_html in enumerate(code_inlines):
        text = text.replace(f"__INLINE_CODE_{idx}__", c_html)
        
    return text

def parse_docstring(py_code: str) -> dict:
    meta = {
        "title": "",
        "pattern": "",
        "difficulty": "Medium",
        "link": "",
        "eli5": "",
        "approach": "",
        "time": "",
        "space": "",
        "edge_cases": ""
    }
    match = re.search(r'"""(.*?)"""', py_code, re.DOTALL)
    if not match:
        return meta
    doc = match.group(1)
    title_m = re.search(r'Problem:\s*(.+)', doc)
    if title_m: meta["title"] = title_m.group(1).strip()
    diff_m = re.search(r'Difficulty:\s*(.+)', doc)
    if diff_m: meta["difficulty"] = diff_m.group(1).strip()
    link_m = re.search(r'Link:\s*(.+)', doc)
    if link_m: meta["link"] = link_m.group(1).strip()
    eli5_m = re.search(r'UNDERSTANDING THE PROBLEM.*?:\s*\n-*\s*\n(.*?)(?=\n[A-Z\s]{4,}|\Z)', doc, re.DOTALL)
    if eli5_m: meta["eli5"] = eli5_m.group(1).strip()
    appr_m = re.search(r'APPROACH:\s*\n-*\s*\n(.*?)(?=\n[A-Z\s]{4,}|\Z)', doc, re.DOTALL)
    if appr_m: meta["approach"] = appr_m.group(1).strip()
    time_m = re.search(r'Time:\s*(.+)', doc)
    if time_m: meta["time"] = time_m.group(1).strip()
    space_m = re.search(r'Space:\s*(.+)', doc)
    if space_m: meta["space"] = space_m.group(1).strip()
    edge_m = re.search(r'EDGE CASES:\s*\n-*\s*\n(.*?)(?=\n[=]{4,}|\Z)', doc, re.DOTALL)
    if edge_m: meta["edge_cases"] = edge_m.group(1).strip()
    return meta

def extract_code_body(py_code: str) -> str:
    return re.sub(r'"""(.*?)"""\s*', '', py_code, count=1, flags=re.DOTALL).strip()

def build_fundamentals():
    """Compiles all sections under 00 - Fundamentals into structured modules."""
    print("📖 Compiling 00 - Fundamentals (Theoretical Foundations, 14 Engines, Trees, Graphs, Pattern Cracker)...")
    fund_dir = ROOT_DIR / "00 - Fundamentals"
    modules = []

    # 1. 000 - Theoretical Foundations (13 Chapters)
    theo_dir = fund_dir / "000 - Theoretical Foundations (The Complete Guide)"
    if theo_dir.exists():
        chapters = []
        for md_file in sorted(theo_dir.glob("*.md")):
            if md_file.name == "README.md":
                continue
            raw = md_file.read_text(encoding="utf-8")
            title_m = re.search(r'^#\s*(.+)', raw, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else md_file.stem.replace('_', ' ').title()
            parsed_html = render_markdown(raw)
            chapters.append({
                "id": f"fund-theo-{md_file.stem}",
                "file": md_file.name,
                "title": title,
                "html": parsed_html
            })
        modules.append({
            "id": "sec-fundamentals-theory",
            "name": "000. Theoretical Foundations (13 Deep Chapters)",
            "icon": "🏛️",
            "badge": "Theory",
            "chapters": chapters,
            "type": "theory"
        })

    # 2. 001 - 014: The 14 Primitive Data Structure Engine Rooms
    engines = []
    for num in range(1, 15):
        pattern_str = f"{num:03d} - "
        engine_dirs = [d for d in fund_dir.iterdir() if d.is_dir() and d.name.startswith(pattern_str)]
        if engine_dirs:
            edir = engine_dirs[0]
            py_files = list(edir.glob("*.py"))
            wt_files = list(edir.glob("*walkthrough.md"))
            py_code = py_files[0].read_text(encoding="utf-8") if py_files else ""
            wt_raw = wt_files[0].read_text(encoding="utf-8") if wt_files else ""
            wt_html = render_markdown(wt_raw)
            clean_code = extract_code_body(py_code) if py_code else ""
            engines.append({
                "id": f"fund-engine-{edir.name.split(' - ')[0]}",
                "name": edir.name,
                "walkthrough_html": wt_html,
                "code": clean_code,
                "file": py_files[0].name if py_files else ""
            })
    modules.append({
        "id": "sec-fundamentals-engines",
        "name": "001–014. The 14 Data Structure Engine Rooms",
        "icon": "⚙️",
        "badge": "14 Engines",
        "engines": engines,
        "type": "engines"
    })

    # 3. 015 - Trees Guide
    trees_dir = fund_dir / "015 - Trees (The Complete Guide)"
    if trees_dir.exists():
        trees_chapters = []
        for md_file in sorted(trees_dir.glob("*.md")):
            if md_file.name == "README.md":
                continue
            raw = md_file.read_text(encoding="utf-8")
            title_m = re.search(r'^#\s*(.+)', raw, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else md_file.stem.replace('_', ' ').title()
            trees_chapters.append({
                "id": f"fund-trees-{md_file.stem}",
                "file": md_file.name,
                "title": title,
                "html": render_markdown(raw)
            })
        modules.append({
            "id": "sec-fundamentals-trees",
            "name": "015. Trees (The Complete Guide)",
            "icon": "🌲",
            "badge": "7 Chapters",
            "chapters": trees_chapters,
            "type": "theory"
        })

    # 4. 016 - Graphs Guide
    graphs_dir = fund_dir / "016 - Graphs (The Complete Guide)"
    if graphs_dir.exists():
        graphs_chapters = []
        for md_file in sorted(graphs_dir.glob("*.md")):
            if md_file.name == "README.md":
                continue
            raw = md_file.read_text(encoding="utf-8")
            title_m = re.search(r'^#\s*(.+)', raw, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else md_file.stem.replace('_', ' ').title()
            graphs_chapters.append({
                "id": f"fund-graphs-{md_file.stem}",
                "file": md_file.name,
                "title": title,
                "html": render_markdown(raw)
            })
        modules.append({
            "id": "sec-fundamentals-graphs",
            "name": "016. Graphs (The Complete Guide)",
            "icon": "🕸️",
            "badge": "8 Chapters",
            "chapters": graphs_chapters,
            "type": "theory"
        })

    # 5. 017 - The Pattern Cracker
    cracker_dir = fund_dir / "017 - The Pattern Cracker"
    if cracker_dir.exists():
        cracker_chapters = []
        for md_file in sorted(cracker_dir.glob("*.md")):
            if md_file.name == "README.md":
                continue
            raw = md_file.read_text(encoding="utf-8")
            title_m = re.search(r'^#\s*(.+)', raw, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else md_file.stem.replace('_', ' ').title()
            cracker_chapters.append({
                "id": f"fund-cracker-{md_file.stem}",
                "file": md_file.name,
                "title": title,
                "html": render_markdown(raw)
            })
        modules.append({
            "id": "sec-fundamentals-cracker",
            "name": "017. The Pattern Cracker (Mental Model)",
            "icon": "🧠",
            "badge": "Framework",
            "chapters": cracker_chapters,
            "type": "theory"
        })

    return modules

def build_catalog():
    print("🚀 Scanning 43 algorithmic pattern directories...")
    pattern_dirs = sorted([d for d in ROOT_DIR.iterdir() if d.is_dir() and d.name[0].isdigit() and d.name != ".git" and d.name != "_site" and not d.name.startswith("00")])
    
    catalog = []
    all_problems_index = []
    
    for pdir in pattern_dirs:
        pattern_slug = pdir.name
        theory_file = pdir / "theory.md"
        theory_html = ""
        theory_title = pattern_slug
        
        if theory_file.exists():
            raw_theory = theory_file.read_text(encoding="utf-8")
            title_m = re.search(r'^#\s*(.+)', raw_theory, re.MULTILINE)
            if title_m: theory_title = title_m.group(1).strip()
            theory_html = render_markdown(raw_theory)

        pattern_entry = {
            "slug": pattern_slug,
            "id": f"pattern-{pattern_slug.split(' - ')[0]}",
            "name": pattern_slug,
            "title": theory_title,
            "family": get_family_for_pattern(pattern_slug),
            "theory_html": theory_html,
            "problems": []
        }
        
        # Scan problems
        py_files = sorted(pdir.glob("problem_*.py"))
        for py_path in py_files:
            py_code = py_path.read_text(encoding="utf-8")
            meta = parse_docstring(py_code)
            clean_code = extract_code_body(py_code)
            
            walkthrough_path = py_path.with_name(f"{py_path.stem}_walkthrough.md")
            walkthrough_html = ""
            if walkthrough_path.exists():
                wt_raw = walkthrough_path.read_text(encoding="utf-8")
                walkthrough_html = render_markdown(wt_raw)
            
            title = meta["title"] or py_path.stem.replace("problem_", "").replace("_", " ").title()
            prob_id = f"prob-{pattern_slug.split(' - ')[0]}-{py_path.stem}"
            
            prob_entry = {
                "id": prob_id,
                "file": py_path.name,
                "title": title,
                "difficulty": meta["difficulty"],
                "link": meta["link"],
                "eli5": meta["eli5"],
                "approach": meta["approach"],
                "time": meta["time"],
                "space": meta["space"],
                "edge_cases": meta["edge_cases"],
                "code": clean_code,
                "walkthrough_html": walkthrough_html
            }
            pattern_entry["problems"].append(prob_entry)
            
            all_problems_index.append({
                "id": prob_id,
                "title": title,
                "pattern": pattern_slug,
                "difficulty": meta["difficulty"],
                "time": meta["time"]
            })
            
        catalog.append(pattern_entry)
    
    return catalog, all_problems_index

def generate_html(fundamentals_modules, catalog, all_problems_index):
    # Family filter chips with dynamic count badge
    family_chips_html = []
    for fam, fdata in FAMILIES.items():
        fam_icon = fdata["icon"]
        fam_count = len(fdata["patterns"])
        family_chips_html.append(f'''
        <button class="family-chip" data-family-target="{fam}">
          <span class="family-chip-name">{fam_icon} {fam}</span>
          <span class="family-count-badge">{fam_count}</span>
        </button>
        ''')
    family_chips_sidebar_html = ''.join(family_chips_html)

    # 7 Pattern Families Radar Cards in Main Content
    family_radar_cards = []
    for fam, fdata in FAMILIES.items():
        fam_icon = fdata["icon"]
        fam_desc = fdata["desc"]
        fam_count = len(fdata["patterns"])
        patterns_links = [f'<span class="nav-pill" style="margin:2px;">{p.split(" - ")[1]}</span>' for p in fdata["patterns"]]
        family_radar_cards.append(f'''
        <div class="family-radar-card" data-family-card="{fam}">
          <div class="family-card-top">
            <span class="family-name">{fam_icon} {fam}</span>
            <span class="family-count-badge" style="font-size:0.75rem;padding:3px 8px;">{fam_count} Patterns</span>
          </div>
          <div class="family-gut-say">{fdata["desc"]}</div>
          <div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:6px;">
            {''.join(patterns_links)}
          </div>
        </div>
        ''')
    family_radar_grid_html = ''.join(family_radar_cards)
    
    # Sidebar Navigation Tree HTML
    sidebar_parts = []
    sidebar_parts.append('<div class="nav-tree-section-title">🏛️ Pillar 0 & 1 · Fundamentals</div>')
    for mod in fundamentals_modules:
        mod_id = mod["id"]
        mod_name = mod["name"]
        icon = mod["icon"]
        badge = mod["badge"]
        
        items_html = []
        if mod["type"] == "theory":
            for ch in mod["chapters"]:
                items_html.append(f'<a href="#{ch["id"]}" class="nav-tree-link">{html.escape(ch["title"])}</a>')
        elif mod["type"] == "engines":
            for eng in mod["engines"]:
                items_html.append(f'<a href="#{eng["id"]}" class="nav-tree-link">{html.escape(eng["name"])}</a>')

        sidebar_parts.append(f'''
        <div class="nav-tree-group" id="nav-group-{mod_id}">
          <div class="nav-tree-header" data-target="#{mod_id}">
            <div class="tree-title-group">
              <span class="tree-chevron">▶</span>
              <span class="tree-icon">{icon}</span>
              <span class="tree-title-text">{html.escape(mod_name)}</span>
            </div>
            <span class="nav-pill">{badge}</span>
          </div>
          <div class="nav-tree-children">
            {''.join(items_html)}
          </div>
        </div>
        ''')

    # 2. 43 Algorithmic Patterns in sidebar
    sidebar_parts.append('<div class="nav-tree-section-title">⚔️ Pillar 2 · Algorithmic Patterns (43)</div>')
    for cat in catalog:
        cat_id = cat["id"]
        cat_name = cat["name"]
        fam = cat["family"]
        fam_icon = FAMILIES.get(fam, {}).get("icon", "⚡")
        prob_count = len(cat["problems"])
        
        prob_links = []
        for p in cat["problems"]:
            prob_links.append(f'<a href="#{p["id"]}" class="nav-tree-link">{html.escape(p["title"])}</a>')

        theory_link = f'<a href="#{cat_id}" class="nav-tree-link" style="color:var(--accent-cyan);font-weight:600;">📖 Pattern Theory &amp; Mental Models</a>' if cat["theory_html"] else ''

        sidebar_parts.append(f'''
        <div class="nav-tree-group" data-family="{fam}" id="nav-group-{cat_id}">
          <div class="nav-tree-header" data-target="#{cat_id}">
            <div class="tree-title-group">
              <span class="tree-chevron">▶</span>
              <span class="tree-icon">{fam_icon}</span>
              <span class="tree-title-text">{html.escape(cat_name)}</span>
            </div>
            <span class="nav-pill">{prob_count}</span>
          </div>
          <div class="nav-tree-children">
            {theory_link}
            {''.join(prob_links)}
          </div>
        </div>
        ''')

    sidebar_tree_html = '\n'.join(sidebar_parts)

    # Main Content Stage Chapters
    content_parts = []

    # 1. Fundamentals Sections in main content
    for mod in fundamentals_modules:
        mod_id = mod["id"]
        mod_name = mod["name"]
        icon = mod["icon"]
        badge = mod["badge"]

        inner_items = []
        if mod["type"] == "theory":
            for ch in mod["chapters"]:
                inner_items.append(f'''
                <details class="problem-card" id="{ch["id"]}">
                  <summary class="problem-summary">
                    <div class="problem-left-cluster">
                      <span class="difficulty-pill diff-easy">Theory</span>
                      <span class="problem-title">{html.escape(ch["title"])}</span>
                    </div>
                    <span class="problem-chevron">▶</span>
                  </summary>
                  <div class="problem-details-body">
                    {ch["html"]}
                  </div>
                </details>
                ''')
        elif mod["type"] == "engines":
            for eng in mod["engines"]:
                inner_items.append(f'''
                <details class="problem-card" id="{eng["id"]}">
                  <summary class="problem-summary">
                    <div class="problem-left-cluster">
                      <span class="difficulty-pill diff-medium">Engine</span>
                      <span class="problem-title">{html.escape(eng["name"])}</span>
                    </div>
                    <span class="problem-chevron">▶</span>
                  </summary>
                  <div class="problem-details-body">
                    {eng["walkthrough_html"]}
                    {f'<div class="dna-skeleton-box"><div class="dna-skeleton-header"><span class="dna-label">⚙️ {html.escape(eng["file"])}</span><button class="copy-btn" onclick="navigator.clipboard.writeText(this.closest(\x27.dna-skeleton-box\x27).querySelector(\x27pre code\x27).innerText);this.innerText=\x27Copied!\x27;setTimeout(()=>this.innerText=\x27Copy\x27,1600);">Copy</button></div><div class="code-container"><pre><code class="language-python">{html.escape(eng["code"])}</code></pre></div></div>' if eng["code"] else ''}
                  </div>
                </details>
                ''')

        content_parts.append(f'''
        <section class="pattern-chapter is-collapsed" id="{mod_id}">
          <div class="chapter-header-bar" data-target="#{mod_id}">
            <div class="chapter-header-left">
              <span class="chapter-chevron">▶</span>
              <span class="tree-icon" style="font-size:1.3rem;">{icon}</span>
              <h2 class="chapter-title">{html.escape(mod_name)}</h2>
            </div>
            <div class="chapter-header-right">
              <span class="hero-tag">{badge}</span>
              <button class="chapter-toggle-btn">Expand</button>
            </div>
          </div>
          <div class="chapter-content-body">
            {''.join(inner_items)}
          </div>
        </section>
        ''')

    # 2. 43 Algorithmic Pattern Sections in main content
    for cat in catalog:
        cat_id = cat["id"]
        cat_name = cat["name"]
        fam = cat["family"]
        fam_icon = FAMILIES.get(fam, {}).get("icon", "⚡")
        prob_count = len(cat["problems"])

        problems_html = []
        for p in cat["problems"]:
            p_id = p["id"]
            p_title = p["title"]
            p_diff = p["difficulty"]
            diff_cls = f"diff-{p_diff.lower()}" if p_diff.lower() in ['easy', 'medium', 'hard'] else 'diff-medium'
            lc_link_html = f'<a href="{p["link"]}" target="_blank" rel="noopener" class="nav-pill" style="color:var(--accent-cyan);text-decoration:none;">LeetCode ↗</a>' if p["link"] else ''

            body_content = []
            if p["walkthrough_html"]:
                body_content.append(f'<div class="walkthrough-pane">{p["walkthrough_html"]}</div>')
            elif p["eli5"] or p["approach"]:
                if p["eli5"]:
                    body_content.append(f'<div class="eli5-frosted-card"><div class="eli5-label">Intuition</div><div class="eli5-body">{html.escape(p["eli5"])}</div></div>')
                if p["approach"]:
                    body_content.append(f'<div style="font-size:0.92rem;color:var(--text-muted);"><strong style="color:var(--text-main);">Strategy:</strong> {html.escape(p["approach"])}</div>')

            body_content.append(f'''
            <div class="dna-skeleton-box">
              <div class="dna-skeleton-header">
                <span class="dna-label">⚡ Python 3.12+ Implementation</span>
                <button class="copy-btn" onclick="navigator.clipboard.writeText(this.closest('.dna-skeleton-box').querySelector('pre code').innerText);this.innerText='Copied!';setTimeout(()=>this.innerText='Copy',1600);">Copy</button>
              </div>
              <div class="code-container">
                <pre><code class="language-python">{html.escape(p["code"])}</code></pre>
              </div>
            </div>
            <div style="display:flex;gap:12px;font-family:var(--font-mono);font-size:0.78rem;color:var(--text-muted);flex-wrap:wrap;margin-top:12px;">
              {f'<span>⏱ Time: <strong style="color:var(--text-main);">{html.escape(p["time"])}</strong></span>' if p["time"] else ''}
              {f'<span>💾 Space: <strong style="color:var(--text-main);">{html.escape(p["space"])}</strong></span>' if p["space"] else ''}
            </div>
            ''')

            problems_html.append(f'''
            <details class="problem-card" id="{p_id}">
              <summary class="problem-summary">
                <div class="problem-left-cluster">
                  <span class="difficulty-pill {diff_cls}">{html.escape(p_diff)}</span>
                  <span class="problem-title">{html.escape(p_title)}</span>
                </div>
                <div style="display:flex;align-items:center;gap:12px;">
                  {lc_link_html}
                  <span class="problem-chevron">▶</span>
                </div>
              </summary>
              <div class="problem-details-body">
                {''.join(body_content)}
              </div>
            </details>
            ''')

        content_parts.append(f'''
        <section class="pattern-chapter is-collapsed" id="{cat_id}" data-family="{fam}">
          <div class="chapter-header-bar" data-target="#{cat_id}">
            <div class="chapter-header-left">
              <span class="chapter-chevron">▶</span>
              <span class="tree-icon" style="font-size:1.3rem;">{fam_icon}</span>
              <h2 class="chapter-title">{html.escape(cat_name)}</h2>
            </div>
            <div class="chapter-header-right">
              <span class="hero-tag">{fam}</span>
              <span class="nav-pill">{prob_count} Problems</span>
              <button class="chapter-toggle-btn">Expand</button>
            </div>
          </div>
          <div class="chapter-content-body">
            {f'<details class="theory-details" open><summary class="theory-summary"><span style="font-family:var(--font-mono);font-size:0.8rem;color:var(--accent-cyan);font-weight:700;">📖 COMPREHENSIVE THEORY &amp; MENTAL MODELS</span><span class="problem-chevron">▶</span></summary><div class="theory-body-wrapper">{cat["theory_html"]}</div></details>' if cat["theory_html"] else ''}
            <div class="problems-catalog">
              {''.join(problems_html)}
            </div>
          </div>
        </section>
        ''')

    all_chapters_html = '\n'.join(content_parts)

    html_template = f'''<!DOCTYPE html>
<html lang="en" data-theme="liquid">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DSA Pattern Bible — Complete Algorithmic &amp; Theoretical Compendium</title>
  <meta name="description" content="Master 44 Algorithmic Patterns, Theoretical Foundations, and 305 typed Python implementations with interactive mental models.">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E%3Cstop offset='0' stop-color='%2300f2fe'/%3E%3Cstop offset='1' stop-color='%23a855f7'/%3E%3Cstop offset='1' stop-color='%23ff4de1'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='64' height='64' rx='16' fill='url(%23g)'/%3E%3Ctext x='50%25' y='58%25' font-family='sans-serif' font-size='26' font-weight='900' fill='white' text-anchor='middle' dominant-baseline='middle'%3EDSA%3C/text%3E%3C/svg%3E">
  
  <!-- Modern CDN Fonts & Styles -->
  <link rel="stylesheet" href="./style.css">
  
  <!-- KaTeX Mathematical Typesetting -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
  
  <!-- Mermaid Diagrams -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({{
      startOnLoad: false,
      theme: 'dark',
      themeVariables: {{
        darkMode: true,
        background: 'transparent',
        primaryColor: '#00f2fe',
        primaryBorderColor: '#00f2fe',
        primaryTextColor: '#f1f5f9',
        lineColor: '#a855f7',
        fontFamily: 'Inter, system-ui, sans-serif'
      }}
    }});
  </script>
</head>
<body>
  <!-- Ambient Halo Lighting Engine -->
  <div class="canvas-ambient-halo" aria-hidden="true">
    <div class="halo-orb-pointer" id="halo-orb"></div>
    <div class="halo-orb-aurora"></div>
  </div>

  <!-- Header Navigation -->
  <header class="header-glass">
    <div class="header-left-cluster">
      <button class="mobile-nav-toggle" id="mobile-nav-toggle" aria-label="Open Navigation">☰</button>
      <button class="sidebar-dock-toggle" id="sidebar-dock-toggle" aria-label="Toggle Navigation Sidebar" title="Toggle Sidebar (⌘B / [)">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
          <line x1="9" y1="3" x2="9" y2="21"></line>
        </svg>
      </button>
      <a href="#" class="brand-badge">
        <div class="brand-logo-icon">Ω</div>
        <div class="brand-text-group">
          <span class="brand-title">DSA PATTERN BIBLE</span>
          <span class="brand-subtitle">Algorithmic Patterns &amp; Foundations</span>
        </div>
      </a>
    </div>

    <div class="header-telemetry-cluster">
      <div class="telemetry-chip">
        <span class="pulse-dot"></span>
        <span>PATTERNS: <strong>44</strong></span>
      </div>
      <div class="telemetry-chip">
        <span>PROBLEMS: <strong>305</strong></span>
      </div>
      <div class="telemetry-chip">
        <span>WALKTHROUGHS: <strong>328</strong></span>
      </div>
    </div>

    <div class="header-controls-cluster">
      <button class="hud-search-btn" id="hud-search-trigger" title="Global Fuzzy Search (⌘K)">
        <span>Search library...</span>
        <span class="kbd-shortcut">⌘K</span>
      </button>

      <div class="theme-picker-group">
        <button class="theme-pill-btn active" data-theme-set="liquid" title="Deep Space Liquid Glass">Liquid</button>
        <button class="theme-pill-btn" data-theme-set="mica" title="Fluent Aero Mica">Mica</button>
        <button class="theme-pill-btn" data-theme-set="holo" title="Holo 2050 Cyberpunk">Holo</button>
        <button class="theme-pill-btn" data-theme-set="matrix" title="Matrix Obsidian">Matrix</button>
      </div>

      <button class="hud-tool-btn" id="audio-toggle-btn" title="Toggle Audio Feedback">🔊</button>
      <a href="https://github.com/vadde/DSA" target="_blank" rel="noopener" class="hud-tool-btn" title="View Source on GitHub">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
      </a>
    </div>
  </header>

  <!-- Layout Container -->
  <div class="layout-container">
    <div class="mobile-drawer-backdrop" id="mobile-drawer-backdrop" aria-hidden="true"></div>
    <button class="floating-sidebar-toggle" id="floating-sidebar-toggle" aria-label="Open Navigation Sidebar" title="Open Sidebar (⌘B / [)">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
        <line x1="9" y1="3" x2="9" y2="21"></line>
        <path d="m13 15 3-3-3-3"></path>
      </svg>
      <span>Navigation</span>
    </button>

    <!-- Navigation Sidebar -->
    <aside class="sidebar" id="main-sidebar">
      <div class="sidebar-search-row">
        <div class="sidebar-search-box">
          <span class="sidebar-search-icon">🔍</span>
          <input type="text" class="sidebar-search-input" id="sidebar-filter-input" placeholder="Filter 44 patterns &amp; engines...">
        </div>
        <button class="sidebar-collapse-pill sidebar-close-btn" id="sidebar-close-btn" aria-label="Close navigation sidebar" title="Collapse sidebar (⌘B / [)">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="9" y1="3" x2="9" y2="21"></line>
            <path d="m14 9-3 3 3 3"></path>
          </svg>
        </button>
      </div>

      <div class="tree-controls-bar">
        <button class="mini-tool-btn" id="sidebar-expand-all">⊞ Expand All</button>
        <button class="mini-tool-btn" id="sidebar-collapse-all">⊟ Collapse All</button>
      </div>

      <div class="family-filter-container">
        <div class="family-filter-header">
          <span>7 Pattern Families</span>
          <button id="clear-family-filter" style="background:none;border:none;color:var(--accent-cyan);cursor:pointer;font-size:0.7rem;">Reset</button>
        </div>
        <div class="family-filter-chips">
{family_chips_sidebar_html}
        </div>
      </div>

      <nav id="sidebar-tree">
{sidebar_tree_html}
      </nav>
    </aside>

    <!-- Draggable Sidebar Resizer Splitter -->
    <div class="sidebar-resizer" id="sidebar-resizer" role="separator" aria-orientation="vertical" aria-label="Resize navigation sidebar" title="Drag to adjust sidebar width (Double-click to reset)"></div>

    <!-- Content Reading Stage -->
    <main class="content-area">
      <div class="stage-wrapper">
        <!-- Hero Section -->
        <section class="command-deck-hero" id="sec-hero">
          <div class="hero-eyebrow-cluster">
            <span class="hero-tag">THE DEFINITIVE PATTERN COMPENDIUM</span>
            <span class="nav-pill">Production Grade</span>
          </div>
          <h1 class="hero-headline">The Complete DSA Pattern Bible</h1>
          <p class="hero-subdeck">
            <em>"You don't need to memorize 43 patterns. You need to memorize <strong>5 questions</strong>, <strong>7 families</strong>, and <strong>1 mantra</strong>."</em>
          </p>

          <div class="three-pillars-grid">
            <div class="pillar-card">
              <span class="pillar-badge">Pillar 0 · Theory</span>
              <h3 class="pillar-title">Physics of Computation</h3>
              <p class="pillar-desc">Computability, Rice's theorem, Turing reductions, Complexity Zoo (P, NP, PSPACE), Lower Bounds &amp; Amortization.</p>
            </div>
            <div class="pillar-card">
              <span class="pillar-badge">Pillar 1 · Mechanics</span>
              <h3 class="pillar-title">14 Engine Rooms</h3>
              <p class="pillar-desc">Array &amp; String, Heaps, BSTs, Tries, Disjoint Sets, Circular Lists, and Bitwise Engines with typed Python implementations.</p>
            </div>
            <div class="pillar-card">
              <span class="pillar-badge">Pillar 2 · Arsenal</span>
              <h3 class="pillar-title">43 Algorithmic Patterns</h3>
              <p class="pillar-desc">The SIFT Method, Muscle Memory skeletons, Step-by-Step execution dry runs, and 305 typed Python solutions.</p>
            </div>
          </div>
        </section>

        <!-- Reading Mode Toolbar (Expand / Collapse & Focus Mode) -->
        <div class="reading-controls-bar">
          <div class="mode-toggles-cluster">
            <button class="mode-btn" id="btn-expand-all" title="Expand all pattern chapters">⊞ Expand All</button>
            <button class="mode-btn active" id="btn-focus-mode" title="Focus mode: Only expand one pattern at a time">🎯 Focus Mode</button>
            <button class="mode-btn" id="btn-collapse-all" title="Collapse all pattern chapters">⊟ Collapse All</button>
          </div>
          <div style="font-family:var(--font-mono);font-size:0.75rem;color:var(--text-dim);">
            Click chapter headers to toggle accordion
          </div>
        </div>

        <!-- SIFT Method Interactive Simulator -->
        <section class="sift-interactive-panel" id="sec-sift">
          <div class="section-hud-header">
            <div class="section-hud-title">
              <span>⚡</span>
              <span>The SIFT Method — 10-Second Pattern Finder</span>
            </div>
            <span class="hero-tag">Mental Radar</span>
          </div>
          <p style="font-size:0.92rem;color:var(--text-muted);">
            Before writing a single line of code, execute the SIFT protocol: <strong>State</strong> the problem, <strong>Identify</strong> inputs/constraints, <strong>Find</strong> the trigger, <strong>Template</strong> the skeleton.
          </p>

          <div class="sift-simulator-box">
            <div class="sift-input-group">
              <label class="sift-input-label">1. Input Structure</label>
              <select class="sift-select" id="sift-input-type">
                <option value="sorted_arr">Sorted Array</option>
                <option value="unsorted_arr">Unsorted Array / String</option>
                <option value="linked_list">Linked List</option>
                <option value="tree">Tree / Binary Tree</option>
                <option value="graph">Graph / Matrix Grid</option>
                <option value="intervals">Intervals / Timestamps</option>
              </select>
            </div>

            <div class="sift-input-group">
              <label class="sift-input-label">2. Target Goal</label>
              <select class="sift-select" id="sift-target-goal">
                <option value="pair_sum">Find Pair / Triplet with Target</option>
                <option value="contiguous">Contiguous Subarray / Window</option>
                <option value="cycle">Detect Cycle / Loop</option>
                <option value="top_k">Find Kth Largest / Top K</option>
                <option value="connected">Connected Components / Islands</option>
                <option value="optimize">Count Ways / Maximize Value (DP)</option>
              </select>
            </div>

            <div class="sift-input-group">
              <label class="sift-input-label">3. Constraint Scale (N)</label>
              <select class="sift-select" id="sift-constraint-n">
                <option value="linear">N ≤ 10^6 (O(N) Required)</option>
                <option value="nlogn">N ≤ 10^5 (O(N log N) Heap/Sort)</option>
                <option value="quadratic">N ≤ 5,000 (O(N^2) 2D DP)</option>
                <option value="exponential">N ≤ 20 (O(2^N) Backtracking)</option>
              </select>
            </div>
          </div>

          <div class="sift-output-deck" id="sift-recommendation-card">
            <div class="sift-output-header">
              <span style="font-family:var(--font-mono);font-size:0.75rem;color:var(--accent-cyan);text-transform:uppercase;">Identified Pattern</span>
              <span class="nav-pill" id="sift-family-pill">🏃 Runner</span>
            </div>
            <div class="sift-matched-pattern" id="sift-matched-name">Two Pointers (Opposite Ends)</div>
            <div class="sift-mantra-box" id="sift-mantra-text">
              "My input is a sorted array. I need to find a pair. The constraint is O(N). Therefore, shrink from both ends inwards."
            </div>
          </div>
        </section>

        <!-- 7 Pattern Families Radar Grid -->
        <section class="sift-interactive-panel" id="sec-families">
          <div class="section-hud-header">
            <div class="section-hud-title">
              <span>👨‍👩‍👧‍👦</span>
              <span>The 7 Pattern Families</span>
            </div>
            <span class="hero-tag">Categorical Mastery</span>
          </div>
          <p style="font-size:0.92rem;color:var(--text-muted);">
            <em>"Don't memorize 43 patterns. Memorize 7 families. Each family shares the same intuitive feeling."</em>
          </p>
          <div class="families-radar-grid">
{family_radar_grid_html}
          </div>
        </section>

        <!-- Master Decision Flowchart -->
        <section class="canvas-container" id="sec-flowchart">
          <div class="canvas-header-bar">
            <span class="canvas-type-tag">🗺️ Master Algorithmic Decision Flowchart</span>
            <div class="canvas-controls-group">
              <button class="canvas-tool-btn zoom-out-btn" title="Zoom Out">−</button>
              <span class="zoom-level-badge">100%</span>
              <button class="canvas-tool-btn zoom-in-btn" title="Zoom In">+</button>
              <button class="canvas-tool-btn zoom-reset-btn" title="Reset Zoom">⟲</button>
              <button class="canvas-tool-btn fullscreen-btn" title="View Fullscreen Theater">⛶</button>
            </div>
          </div>
          <div class="canvas-viewport">
            <div class="canvas-content-surface">
              <pre class="mermaid" id="mermaid-diagram-master-flowchart">
flowchart TD
    START["📖 Read the Problem"] --> Q1["❓ What is the INPUT?"]
    
    Q1 -->|"Sorted Array"| SA["🔍 Binary Search&lt;br/&gt;👉 Two Pointers"]
    Q1 -->|"Unsorted Array / String"| UA["❓ What do you need?"]
    Q1 -->|"Linked List"| LL["🐢 Fast & Slow&lt;br/&gt;🔄 In-place Reversal&lt;br/&gt;📋 Clone"]
    Q1 -->|"Tree"| TR["❓ Level-by-level&lt;br/&gt;or Path-by-path?"]
    Q1 -->|"Graph / Matrix"| GR["❓ What to find?"]
    Q1 -->|"Intervals"| IV["📐 Merge Intervals&lt;br/&gt;🤑 Greedy"]
    Q1 -->|"Numbers / Bits"| BT["⊕ Bitwise XOR"]
    
    UA -->|"Subarray contiguous"| SUB["🪟 Sliding Window&lt;br/&gt;➕ Prefix Sum"]
    UA -->|"Pair / Triplet"| TP["👉 Two Pointers (sort first!)"]
    UA -->|"Missing in 1 to N"| CS["🔢 Cyclic Sort"]
    UA -->|"Next Greater / Smaller"| MS["📊 Monotonic Stack"]
    UA -->|"All combos"| BK["🔙 Backtracking&lt;br/&gt;📦 Subsets"]
    UA -->|"Kth largest / smallest"| TK["🏆 Top K / Heap"]
    UA -->|"Count ways / Optimize"| DP["🧮 Dynamic Programming"]
    UA -->|"Lookup / Frequency"| HM["#️⃣ Hash Map"]
    
    TR -->|"Level-by-level"| BFS["🌊 Tree BFS (Queue)"]
    TR -->|"Path / Depth"| DFS["🌲 Tree DFS (Recursion)"]
    
    GR -->|"Connected groups"| UF["🔗 Union Find"]
    GR -->|"Task ordering"| TS["📋 Topological Sort"]
    GR -->|"Islands / Flood fill"| IS["🏝️ Island Traversal"]
    GR -->|"Critical edges"| AP["🌉 Articulation Points"]
              </pre>
            </div>
          </div>
          <div class="canvas-caption">Figure 1.0: Algorithmic Routing Matrix (Double-click or drag to explore topology)</div>
        </section>

        <!-- Complexity Triage Table -->
        <section class="sift-interactive-panel" id="sec-triage">
          <div class="section-hud-header">
            <div class="section-hud-title">
              <span>⚡</span>
              <span>Engineering Complexity Triage: Kill Mode vs Pull the Plug</span>
            </div>
            <span class="hero-tag">Asymptotic Rules</span>
          </div>

          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Constraint (N)</th>
                  <th>Allowed Complexity</th>
                  <th>Tactical Mindset</th>
                  <th>Strategic Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>N ≤ 10</code></td>
                  <td><code>O(N!) or O(N^6)</code></td>
                  <td>🔙 Permutations / Backtracking</td>
                  <td>Brute-force DFS, state permutations (itertools)</td>
                </tr>
                <tr>
                  <td><code>N ≤ 20</code></td>
                  <td><code>O(2^N · N)</code></td>
                  <td>🧩 Bitmask DP / Subsets</td>
                  <td>Meet-in-the-Middle, State compression DP</td>
                </tr>
                <tr>
                  <td><code>N ≤ 100</code></td>
                  <td><code>O(N^4)</code></td>
                  <td>🧮 2D/3D DP / Floyd-Warshall</td>
                  <td>High-dimensional Dynamic Programming</td>
                </tr>
                <tr>
                  <td><code>N ≤ 5,000</code></td>
                  <td><code>O(N^2)</code></td>
                  <td>🪟 Nested Loops / 2D DP</td>
                  <td>Quadratic DP, Kadane variants, nested sweeps</td>
                </tr>
                <tr>
                  <td><code>N ≤ 10^5</code></td>
                  <td><code>O(N log N)</code></td>
                  <td><span class="badge-kill-mode">🚀 KILL MODE: Sort / Heap</span></td>
                  <td>Sorting, Divide &amp; Conquer, Segment Trees, Heaps</td>
                </tr>
                <tr>
                  <td><code>N ≤ 10^6</code></td>
                  <td><code>O(N)</code></td>
                  <td><span class="badge-kill-mode">⚡ KILL MODE: Linear Scan</span></td>
                  <td>Sliding Window, Two Pointers, Monotonic Stack</td>
                </tr>
                <tr>
                  <td><code>N ≥ 10^9</code></td>
                  <td><code>O(log N) or O(1)</code></td>
                  <td>🎯 Math / Binary Search</td>
                  <td>Binary Search over answer space, closed-form math</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- All Pattern & Fundamentals Chapters -->
        <div id="all-pattern-chapters">
{all_chapters_html}
        </div>
      </div>
    </main>
  </div>

  <!-- Global Cmd+K Fuzzy Search Modal -->
  <div class="search-modal-backdrop" id="search-modal-backdrop" aria-hidden="true">
    <div class="search-dialog-panel" role="dialog" aria-modal="true" aria-label="Search DSA Bible">
      <div class="search-dialog-header">
        <span style="color:var(--accent-cyan);font-size:1.1rem;">🔍</span>
        <input type="text" class="search-dialog-input" id="search-dialog-input" placeholder="Search 44 patterns, 14 engines, 305 problems, algorithms..." autofocus>
      </div>
      <div class="search-dialog-results" id="search-dialog-results"></div>
      <div class="search-dialog-footer">
        <span>Use <kbd>↑</kbd> <kbd>↓</kbd> to navigate</span>
        <span><kbd>Enter</kbd> to select</span>
        <span><kbd>ESC</kbd> to close</span>
      </div>
    </div>
  </div>

  <!-- Interactive Visual Canvas Fullscreen Theater Modal (Native Top Layer) -->
  <dialog id="theater-modal" class="theater-dialog" aria-labelledby="theater-title" aria-modal="true">
    <div class="theater-header-bar">
      <div class="theater-title-cluster">
        <span class="theater-icon">🗺️</span>
        <h3 id="theater-title" class="theater-title">Architecture Canvas</h3>
        <span class="nav-pill" id="theater-tag">Theater Mode</span>
      </div>
      <div class="theater-controls-cluster">
        <button class="theater-tool-btn" id="theater-zoom-out" title="Zoom Out (−)">−</button>
        <span class="zoom-level-badge" id="theater-zoom-badge">100%</span>
        <button class="theater-tool-btn" id="theater-zoom-in" title="Zoom In (+)">+</button>
        <button class="theater-tool-btn" id="theater-zoom-reset" title="Reset Zoom (⟲)">100%</button>
        <button class="theater-tool-btn" id="theater-zoom-fit" title="Fit to Viewport">Fit</button>
        <button class="theater-close-btn" id="theater-close-btn" title="Close Theater (Esc)">✕ Close</button>
      </div>
    </div>
    <div class="theater-viewport" id="theater-viewport">
      <div class="theater-content-surface" id="theater-surface"></div>
    </div>
  </dialog>

  <script src="./app.js"></script>
</body>
</html>
'''
    return html_template

def main():
    global _MERMAID_DIAGRAM_COUNTER
    _MERMAID_DIAGRAM_COUNTER = 0
    fund_modules = build_fundamentals()
    catalog, all_problems_index = build_catalog()
    html_page = generate_html(fund_modules, catalog, all_problems_index)
    
    DOCS_SITE_DIR.mkdir(parents=True, exist_ok=True)
    index_path = DOCS_SITE_DIR / "index.html"
    index_path.write_text(html_page, encoding="utf-8")
    print(f"✅ Generated {index_path} ({index_path.stat().st_size / 1024:.1f} KB)")
    
    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = CATALOG_DIR / "manifest.json"
    manifest_data = {
        "version": "2.0.0",
        "total_patterns": len(catalog) + 1,
        "total_problems": len(all_problems_index),
        "fundamentals_modules": [{"id": m["id"], "name": m["name"], "badge": m["badge"]} for m in fund_modules],
        "patterns": [{"slug": "00 - Fundamentals", "id": "sec-fundamentals-theory", "name": "00 - Fundamentals", "family": "Theory", "problem_count": len(fund_modules)}] + [{"slug": c["slug"], "id": c["id"], "name": c["name"], "family": c["family"], "problem_count": len(c["problems"])} for c in catalog],
        "problems": all_problems_index
    }
    manifest_path.write_text(json.dumps(manifest_data, indent=2), encoding="utf-8")
    print(f"✅ Generated {manifest_path} ({manifest_path.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    main()
