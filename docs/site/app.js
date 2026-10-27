/**
 * ==============================================================================
 * DSA LIVING DOCUMENTATION PORTAL — CLIENT-SIDE RUNTIME ENGINE (app.js)
 * Modern Day UI/UX: Liquid Glass, Draggable Resizer, Mobile Drawer, Cmd+K Search,
 * Bi-Directional Synchrony, Focus Mode, Collapsible Chapters, Dynamic Chevrons,
 * SIFT Simulator, Lazy Mermaid/KaTeX Engine, and Web Audio Telemetry.
 * ==============================================================================
 */

(function () {
  'use strict';

  // Global UI State
  const STATE = {
    theme: localStorage.getItem('dsa_theme') || 'liquid',
    sidebarWidth: parseInt(localStorage.getItem('dsa_sidebar_width'), 10) || 330,
    audioEnabled: localStorage.getItem('dsa_audio_enabled') === 'true',
    isFocusMode: true, // Default to Focus Mode (one expanded chapter at a time)
    isBatchExpanding: false, // Prevents synchronous batch render freeze
    manifest: null,
    searchActiveIndex: -1,
    searchResults: [],
    isProgrammaticScroll: false,
    programmaticScrollTimer: null
  };

  // ---------------------------------------------------------------------------
  // 1. WEB AUDIO TELEMETRY ENGINE (Zero external dependencies)
  // ---------------------------------------------------------------------------
  let audioCtx = null;
  function playCyberBeep(frequency = 880, type = 'sine', duration = 0.05) {
    if (!STATE.audioEnabled) return;
    try {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(frequency, audioCtx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(frequency * 0.5, audioCtx.currentTime + duration);
      gain.gain.setValueAtTime(0.06, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + duration);
    } catch (e) {
      // Audio context restricted or disabled
    }
  }

  // ---------------------------------------------------------------------------
  // 2. THEME ENGINE (Liquid Glass, Fluent Mica, Holo 2050, Matrix Obsidian)
  // ---------------------------------------------------------------------------
  function initThemeEngine() {
    applyTheme(STATE.theme);

    document.querySelectorAll('.theme-pill-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        applyTheme(btn.dataset.themeSet);
        playCyberBeep(960, 'triangle', 0.06);
      });
    });

    // Keyboard shortcut 'T' to cycle themes
    document.addEventListener('keydown', e => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 't' || e.key === 'T') {
        const themes = ['liquid', 'mica', 'holo', 'matrix'];
        const nextIdx = (themes.indexOf(STATE.theme) + 1) % themes.length;
        applyTheme(themes[nextIdx]);
        playCyberBeep(1100, 'sine', 0.05);
      }
    });

    const audioBtn = document.getElementById('audio-toggle-btn');
    if (audioBtn) {
      updateAudioBtn(audioBtn);
      audioBtn.addEventListener('click', () => {
        STATE.audioEnabled = !STATE.audioEnabled;
        localStorage.setItem('dsa_audio_enabled', STATE.audioEnabled);
        updateAudioBtn(audioBtn);
        if (STATE.audioEnabled) playCyberBeep(1200, 'square', 0.08);
      });
    }
  }

  function updateAudioBtn(btn) {
    btn.innerText = STATE.audioEnabled ? '🔊' : '🔇';
    btn.title = STATE.audioEnabled ? 'Audio Feedback: ON' : 'Audio Feedback: OFF';
  }

  function applyTheme(themeName) {
    STATE.theme = themeName;
    document.documentElement.setAttribute('data-theme', themeName);
    localStorage.setItem('dsa_theme', themeName);

    document.querySelectorAll('.theme-pill-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.themeSet === themeName);
    });
  }

  // ---------------------------------------------------------------------------
  // 3. AERO MICA DYNAMIC HALO ENGINE
  // ---------------------------------------------------------------------------
  function initHaloEngine() {
    const orb = document.getElementById('halo-orb');
    if (!orb) return;

    window.addEventListener('pointermove', e => {
      document.documentElement.style.setProperty('--mx', `${e.clientX}px`);
      document.documentElement.style.setProperty('--my', `${e.clientY}px`);
    }, { passive: true });
  }

  // ---------------------------------------------------------------------------
  // 4. INTERACTIVE DRAGGABLE SIDEBAR RESIZER STANDARD
  // ---------------------------------------------------------------------------
  function initSidebarResizer() {
    const resizer = document.getElementById('sidebar-resizer');
    const sidebar = document.getElementById('main-sidebar');
    if (!resizer || !sidebar) return;

    const MIN_WIDTH = 240;
    const MAX_WIDTH = 560;
    const DEFAULT_WIDTH = 330;

    const clampedWidth = Math.max(MIN_WIDTH, Math.min(MAX_WIDTH, STATE.sidebarWidth));
    document.documentElement.style.setProperty('--sidebar-width', `${clampedWidth}px`);

    let isResizing = false;

    resizer.addEventListener('pointerdown', e => {
      isResizing = true;
      resizer.classList.add('is-resizing');
      document.body.classList.add('resizing-sidebar');
      resizer.setPointerCapture(e.pointerId);
      e.preventDefault();
    });

    resizer.addEventListener('pointermove', e => {
      if (!isResizing) return;
      const newWidth = Math.max(MIN_WIDTH, Math.min(MAX_WIDTH, e.clientX));
      document.documentElement.style.setProperty('--sidebar-width', `${newWidth}px`);
      STATE.sidebarWidth = newWidth;
    });

    function stopResizing() {
      if (!isResizing) return;
      isResizing = false;
      resizer.classList.remove('is-resizing');
      document.body.classList.remove('resizing-sidebar');
      localStorage.setItem('dsa_sidebar_width', STATE.sidebarWidth);
    }

    resizer.addEventListener('pointerup', stopResizing);
    resizer.addEventListener('pointercancel', stopResizing);

    resizer.addEventListener('dblclick', () => {
      document.documentElement.style.setProperty('--sidebar-width', `${DEFAULT_WIDTH}px`);
      STATE.sidebarWidth = DEFAULT_WIDTH;
      localStorage.setItem('dsa_sidebar_width', DEFAULT_WIDTH);
      playCyberBeep(750, 'sine', 0.06);
    });
  }

  // ---------------------------------------------------------------------------
  // 5. YEAR 2500 MOBILE NAVIGATION DRAWER
  // ---------------------------------------------------------------------------
  function initMobileDrawer() {
    const toggleBtn = document.getElementById('mobile-nav-toggle');
    const sidebar = document.getElementById('main-sidebar');
    const backdrop = document.getElementById('mobile-drawer-backdrop');
    if (!toggleBtn || !sidebar || !backdrop) return;

    function openDrawer() {
      sidebar.classList.add('mobile-open');
      backdrop.classList.add('show');
      document.body.style.overflow = 'hidden';
      playCyberBeep(820, 'triangle', 0.05);
    }

    function closeDrawer() {
      sidebar.classList.remove('mobile-open');
      backdrop.classList.remove('show');
      document.body.style.overflow = '';
    }

    toggleBtn.addEventListener('click', openDrawer);
    backdrop.addEventListener('click', closeDrawer);

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && sidebar.classList.contains('mobile-open')) {
        closeDrawer();
      }
    });

    sidebar.addEventListener('click', e => {
      if (e.target.closest('.nav-tree-link') && window.innerWidth <= 1024) {
        closeDrawer();
      }
    });
  }

  // ---------------------------------------------------------------------------
  // 6. PRECISION NAVIGATION & COLLAPSIBLE CHAPTERS
  // ---------------------------------------------------------------------------
  function navigateToTarget(targetEl) {
    if (!targetEl) return;

    STATE.isProgrammaticScroll = true;
    clearTimeout(STATE.programmaticScrollTimer);

    // 1. Uncollapse the containing chapter
    const chapter = targetEl.closest('.pattern-chapter') || (targetEl.classList.contains('pattern-chapter') ? targetEl : null);
    if (chapter) {
      if (STATE.isFocusMode) {
        document.querySelectorAll('.pattern-chapter').forEach(c => {
          if (c !== chapter) {
            c.classList.add('is-collapsed');
            const btn = c.querySelector('.chapter-toggle-btn');
            if (btn) btn.innerText = 'Expand';
          }
        });
      }
      chapter.classList.remove('is-collapsed');
      const toggleBtn = chapter.querySelector('.chapter-toggle-btn');
      if (toggleBtn) toggleBtn.innerText = 'Collapse';

      // Synchronize Left Navigation tree
      const targetId = chapter.id;
      const sidebarGroup = document.getElementById(`nav-group-${targetId}`);
      if (sidebarGroup) {
        document.querySelectorAll('.nav-tree-group').forEach(g => {
          if (g === sidebarGroup) {
            g.classList.add('expanded');
          } else {
            g.classList.remove('expanded');
          }
        });
        document.querySelectorAll('.nav-tree-header').forEach(h => {
          const g = h.closest('.nav-tree-group');
          if (g === sidebarGroup) {
            h.classList.add('active-branch');
          } else {
            h.classList.remove('active-branch');
          }
        });
        sidebarGroup.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      }

      triggerDiagramRenders(chapter);
    }

    // 2. If target is inside a <details>, open it!
    if (targetEl.tagName === 'DETAILS') {
      targetEl.open = true;
      triggerDiagramRenders(targetEl);
    } else {
      const parentDetails = targetEl.closest('details');
      if (parentDetails) {
        parentDetails.open = true;
        triggerDiagramRenders(parentDetails);
      }
    }

    // Highlight active link in sidebar
    document.querySelectorAll('.nav-tree-link').forEach(link => {
      const href = link.getAttribute('href');
      if (href === `#${targetEl.id}` || (chapter && href === `#${chapter.id}`)) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });

    // 3. Force synchronous layout reflow so the browser finalizes all coordinates
    void document.body.offsetHeight;

    // 4. Calculate exact absolute pixel position
    const headerHeight = 72; // 64px header + 8px padding
    const rect = targetEl.getBoundingClientRect();
    const absoluteY = window.pageYOffset + rect.top - headerHeight;

    window.scrollTo({
      top: Math.max(0, absoluteY),
      behavior: 'smooth'
    });

    // 5. Visual flash glow on the target element
    targetEl.classList.remove('flash-focus');
    void targetEl.offsetWidth; // reflow
    targetEl.classList.add('flash-focus');
    setTimeout(() => targetEl.classList.remove('flash-focus'), 1800);

    STATE.programmaticScrollTimer = setTimeout(() => {
      STATE.isProgrammaticScroll = false;
    }, 950);
  }

  function ensureChapterExpanded(targetEl, shouldScroll = false) {
    if (!targetEl) return;
    if (shouldScroll) {
      navigateToTarget(targetEl);
      return;
    }
    const chapter = targetEl.closest('.pattern-chapter');
    if (chapter) {
      chapter.classList.remove('is-collapsed');
      const toggleBtn = chapter.querySelector('.chapter-toggle-btn');
      if (toggleBtn) toggleBtn.innerText = 'Collapse';
      triggerDiagramRenders(chapter);
    }
    if (targetEl.tagName === 'DETAILS') {
      targetEl.open = true;
      triggerDiagramRenders(targetEl);
    } else {
      const parentDetails = targetEl.closest('details');
      if (parentDetails) {
        parentDetails.open = true;
        triggerDiagramRenders(parentDetails);
      }
    }
  }

  function initCollapsibleChapters() {
    const expandAllBtn = document.getElementById('btn-expand-all');
    const collapseAllBtn = document.getElementById('btn-collapse-all');
    const focusModeBtn = document.getElementById('btn-focus-mode');
    const sidebarExpandBtn = document.getElementById('sidebar-expand-all');
    const sidebarCollapseBtn = document.getElementById('sidebar-collapse-all');

    function setActiveReadingBtn(btn) {
      [expandAllBtn, focusModeBtn, collapseAllBtn].forEach(b => {
        if (b) b.classList.remove('active');
      });
      if (btn) btn.classList.add('active');
    }

    // Click handler for Chapter Header Bar
    document.querySelectorAll('.chapter-header-bar').forEach(header => {
      header.addEventListener('click', () => {
        const chapter = header.closest('.pattern-chapter');
        if (!chapter) return;

        const isCollapsed = chapter.classList.contains('is-collapsed');
        if (isCollapsed) {
          // Expanding
          if (STATE.isFocusMode) {
            document.querySelectorAll('.pattern-chapter').forEach(c => {
              if (c !== chapter) {
                c.classList.add('is-collapsed');
                const btn = c.querySelector('.chapter-toggle-btn');
                if (btn) btn.innerText = 'Expand';
              }
            });
          }
          chapter.classList.remove('is-collapsed');
          const toggleBtn = chapter.querySelector('.chapter-toggle-btn');
          if (toggleBtn) toggleBtn.innerText = 'Collapse';

          // Sync with sidebar tree
          const targetId = chapter.id;
          const sidebarGroup = document.getElementById(`nav-group-${targetId}`);
          if (sidebarGroup) {
            if (STATE.isFocusMode) {
              document.querySelectorAll('.nav-tree-group').forEach(g => {
                if (g !== sidebarGroup) g.classList.remove('expanded');
              });
            }
            sidebarGroup.classList.add('expanded');
          }

          triggerDiagramRenders(chapter);
          playCyberBeep(700, 'sine', 0.04);
        } else {
          // Collapsing
          chapter.classList.add('is-collapsed');
          const toggleBtn = chapter.querySelector('.chapter-toggle-btn');
          if (toggleBtn) toggleBtn.innerText = 'Expand';
          playCyberBeep(550, 'sine', 0.04);
        }
      });
    });

    // Expand All Chapters & Details (High performance: zero synchronous diagram render freeze)
    if (expandAllBtn) {
      expandAllBtn.addEventListener('click', () => {
        STATE.isFocusMode = false;
        STATE.isBatchExpanding = true;
        setActiveReadingBtn(expandAllBtn);
        document.querySelectorAll('.pattern-chapter').forEach(c => {
          c.classList.remove('is-collapsed');
          const btn = c.querySelector('.chapter-toggle-btn');
          if (btn) btn.innerText = 'Collapse';
        });
        document.querySelectorAll('.problem-card, .theory-details').forEach(d => {
          d.open = true;
        });
        setTimeout(() => {
          STATE.isBatchExpanding = false;
          renderVisibleDiagrams();
        }, 50);
        playCyberBeep(900, 'triangle', 0.06);
      });
    }

    // Collapse All Chapters & Details
    if (collapseAllBtn) {
      collapseAllBtn.addEventListener('click', () => {
        STATE.isFocusMode = false;
        setActiveReadingBtn(collapseAllBtn);
        document.querySelectorAll('.pattern-chapter').forEach(c => {
          c.classList.add('is-collapsed');
          const btn = c.querySelector('.chapter-toggle-btn');
          if (btn) btn.innerText = 'Expand';
        });
        document.querySelectorAll('.problem-card').forEach(d => {
          d.open = false;
        });
        document.querySelectorAll('.nav-tree-group').forEach(g => g.classList.remove('expanded'));
        document.querySelectorAll('.nav-tree-header').forEach(h => h.classList.remove('active-branch'));
        document.querySelectorAll('.nav-tree-link').forEach(l => l.classList.remove('active'));
        playCyberBeep(500, 'sine', 0.05);
      });
    }

    // Focus Mode Toggle / Activate
    if (focusModeBtn) {
      focusModeBtn.addEventListener('click', () => {
        STATE.isFocusMode = true;
        setActiveReadingBtn(focusModeBtn);
        // Collapse all except first open chapter
        const chapters = Array.from(document.querySelectorAll('.pattern-chapter'));
        let foundOpen = false;
        chapters.forEach(c => {
          if (!foundOpen && !c.classList.contains('is-collapsed')) {
            foundOpen = true;
          } else {
            c.classList.add('is-collapsed');
            const btn = c.querySelector('.chapter-toggle-btn');
            if (btn) btn.innerText = 'Expand';
          }
        });
        if (!foundOpen && chapters.length > 0) {
          chapters[0].classList.remove('is-collapsed');
          const btn = chapters[0].querySelector('.chapter-toggle-btn');
          if (btn) btn.innerText = 'Collapse';
          triggerDiagramRenders(chapters[0]);
        }
        playCyberBeep(850, 'sine', 0.05);
      });
    }

    // Sidebar Expand / Collapse All
    if (sidebarExpandBtn) {
      sidebarExpandBtn.addEventListener('click', () => {
        document.querySelectorAll('.nav-tree-group').forEach(g => g.classList.add('expanded'));
        playCyberBeep(800, 'sine', 0.04);
      });
    }

    if (sidebarCollapseBtn) {
      sidebarCollapseBtn.addEventListener('click', () => {
        document.querySelectorAll('.nav-tree-group').forEach(g => g.classList.remove('expanded'));
        playCyberBeep(600, 'sine', 0.04);
      });
    }

    // Handle deep links or initial open
    handleInitialDeepLink();
  }

  function handleInitialDeepLink() {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      try {
        const targetEl = document.querySelector(hash);
        if (targetEl) {
          ensureChapterExpanded(targetEl, true);
          return;
        }
      } catch (e) {}
    }
    // If no deep link, keep all chapters and sidebar groups collapsed by default!
    // The user initiates interaction or scrolls to dynamically expand.
  }

  // ---------------------------------------------------------------------------
  // 7. SIDEBAR REAL-TIME FILTER & 7 FAMILY CHIPS
  // ---------------------------------------------------------------------------
  function initSidebarFilters() {
    const filterInput = document.getElementById('sidebar-filter-input');
    const treeGroups = document.querySelectorAll('.nav-tree-group');
    const familyChips = document.querySelectorAll('.family-chip');
    const resetFamilyBtn = document.getElementById('clear-family-filter');

    let activeFamily = null;

    function applyFilters() {
      const query = filterInput ? filterInput.value.trim().toLowerCase() : '';
      treeGroups.forEach(group => {
        const titleText = group.querySelector('.tree-title-text').innerText.toLowerCase();
        const family = group.dataset.family;

        const matchesQuery = !query || titleText.includes(query);
        const matchesFamily = !activeFamily || family === activeFamily;

        if (matchesQuery && matchesFamily) {
          group.style.display = '';
        } else {
          group.style.display = 'none';
        }
      });
    }

    if (filterInput) {
      filterInput.addEventListener('input', applyFilters);
    }

    familyChips.forEach(chip => {
      chip.addEventListener('click', () => {
        const fam = chip.dataset.familyTarget;
        if (activeFamily === fam) {
          activeFamily = null;
          chip.classList.remove('active');
        } else {
          familyChips.forEach(c => c.classList.remove('active'));
          activeFamily = fam;
          chip.classList.add('active');
        }
        applyFilters();
        playCyberBeep(780, 'sine', 0.04);
      });
    });

    if (resetFamilyBtn) {
      resetFamilyBtn.addEventListener('click', () => {
        familyChips.forEach(c => c.classList.remove('active'));
        activeFamily = null;
        if (filterInput) filterInput.value = '';
        applyFilters();
        playCyberBeep(650, 'sine', 0.04);
      });
    }

    // Clicking group headers in sidebar
    document.querySelectorAll('.nav-tree-header').forEach(header => {
      header.addEventListener('click', () => {
        const group = header.closest('.nav-tree-group');
        if (!group) return;
        const willExpand = !group.classList.contains('expanded');

        if (STATE.isFocusMode && willExpand) {
          document.querySelectorAll('.nav-tree-group').forEach(g => {
            if (g !== group) g.classList.remove('expanded');
          });
        }
        group.classList.toggle('expanded', willExpand);

        // Bi-directional synchrony: expand corresponding chapter in content!
        const targetId = header.getAttribute('data-target');
        if (targetId) {
          const targetSection = document.querySelector(targetId);
          if (targetSection && willExpand) {
            ensureChapterExpanded(targetSection, true);
          }
        }
        playCyberBeep(600, 'sine', 0.03);
      });
    });

    // Universal precision navigation for in-page anchors across the entire portal
    document.addEventListener('click', e => {
      const link = e.target.closest('a[href^="#"]');
      if (!link) return;
      const href = link.getAttribute('href');
      if (href && href !== '#' && href.length > 1) {
        const targetEl = document.querySelector(href);
        if (targetEl) {
          e.preventDefault();
          navigateToTarget(targetEl);
          if (history.pushState) {
            history.pushState(null, null, href);
          }
          playCyberBeep(900, 'sine', 0.04);
        }
      }
    });
  }

  // ---------------------------------------------------------------------------
  // 8. GLOBAL CMD+K FUZZY SEARCH MODAL
  // ---------------------------------------------------------------------------
  async function loadManifest() {
    if (STATE.manifest) return STATE.manifest;
    try {
      const res = await fetch('./catalog/manifest.json');
      if (res.ok) {
        STATE.manifest = await res.json();
      }
    } catch (e) {
      console.warn('Unable to load manifest.json:', e);
    }
    return STATE.manifest;
  }

  function initSearchModal() {
    const triggerBtn = document.getElementById('hud-search-trigger');
    const backdrop = document.getElementById('search-modal-backdrop');
    const input = document.getElementById('search-dialog-input');
    const resultsContainer = document.getElementById('search-dialog-results');
    if (!triggerBtn || !backdrop || !input || !resultsContainer) return;

    loadManifest();

    function openSearch() {
      backdrop.classList.add('show');
      input.value = '';
      resultsContainer.innerHTML = '<div style="padding:16px;color:var(--text-dim);font-size:0.85rem;text-align:center;">Type to search 44 patterns, 14 engines, and 305 problems...</div>';
      input.focus();
      STATE.searchActiveIndex = -1;
      playCyberBeep(1050, 'sine', 0.05);
    }

    function closeSearch() {
      backdrop.classList.remove('show');
    }

    triggerBtn.addEventListener('click', openSearch);
    backdrop.addEventListener('click', e => {
      if (e.target === backdrop) closeSearch();
    });

    document.addEventListener('keydown', e => {
      if ((e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K')) {
        e.preventDefault();
        if (backdrop.classList.contains('show')) closeSearch();
        else openSearch();
      } else if (e.key === 'Escape' && backdrop.classList.contains('show')) {
        closeSearch();
      }
    });

    input.addEventListener('input', async () => {
      const q = input.value.trim().toLowerCase();
      if (!q) {
        resultsContainer.innerHTML = '<div style="padding:16px;color:var(--text-dim);font-size:0.85rem;text-align:center;">Type to search patterns, engines &amp; problems...</div>';
        STATE.searchResults = [];
        return;
      }

      const manifest = await loadManifest();
      if (!manifest) return;

      const matchedPatterns = manifest.patterns.filter(p =>
        p.name.toLowerCase().includes(q) || p.slug.toLowerCase().includes(q) || p.family.toLowerCase().includes(q)
      ).slice(0, 4);

      const matchedProblems = manifest.problems.filter(prob =>
        prob.title.toLowerCase().includes(q) || prob.pattern.toLowerCase().includes(q) || (prob.time && prob.time.toLowerCase().includes(q))
      ).slice(0, 10);

      STATE.searchResults = [];
      let html = '';

      if (matchedPatterns.length > 0) {
        html += '<div style="font-family:var(--font-mono);font-size:0.72rem;color:var(--accent-cyan);padding:4px 8px;text-transform:uppercase;">Patterns</div>';
        matchedPatterns.forEach(p => {
          STATE.searchResults.push({ type: 'pattern', target: `#${p.id}` });
          html += `
            <a href="#${p.id}" class="search-result-item" data-index="${STATE.searchResults.length - 1}">
              <span class="item-title">📂 ${escapeHtml(p.name)}</span>
              <span class="item-meta">${p.family} · ${p.problem_count} Problems</span>
            </a>
          `;
        });
      }

      if (matchedProblems.length > 0) {
        html += '<div style="font-family:var(--font-mono);font-size:0.72rem;color:var(--accent-violet);padding:8px 8px 4px;text-transform:uppercase;">Problems</div>';
        matchedProblems.forEach(prob => {
          STATE.searchResults.push({ type: 'problem', target: `#${prob.id}` });
          html += `
            <a href="#${prob.id}" class="search-result-item" data-index="${STATE.searchResults.length - 1}">
              <span class="item-title">⚡ ${escapeHtml(prob.title)}</span>
              <span class="item-meta">${prob.pattern.split(' - ')[1] || prob.pattern} · ${prob.difficulty}</span>
            </a>
          `;
        });
      }

      if (!html) {
        html = '<div style="padding:20px;color:var(--text-dim);font-size:0.88rem;text-align:center;">No matching patterns or problems found.</div>';
      }

      resultsContainer.innerHTML = html;
      STATE.searchActiveIndex = -1;
    });

    input.addEventListener('keydown', e => {
      const items = resultsContainer.querySelectorAll('.search-result-item');
      if (!items.length) return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        STATE.searchActiveIndex = (STATE.searchActiveIndex + 1) % items.length;
        updateActiveSearchResult(items);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        STATE.searchActiveIndex = (STATE.searchActiveIndex - 1 + items.length) % items.length;
        updateActiveSearchResult(items);
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (STATE.searchActiveIndex >= 0 && items[STATE.searchActiveIndex]) {
          items[STATE.searchActiveIndex].click();
        }
      }
    });

    resultsContainer.addEventListener('click', e => {
      const item = e.target.closest('.search-result-item');
      if (item) {
        closeSearch();
        const href = item.getAttribute('href');
        const targetEl = document.querySelector(href);
        if (targetEl) {
          navigateToTarget(targetEl);
          playCyberBeep(1200, 'sine', 0.08);
        }
      }
    });
  }

  function updateActiveSearchResult(items) {
    items.forEach((item, idx) => {
      item.classList.toggle('selected', idx === STATE.searchActiveIndex);
      if (idx === STATE.searchActiveIndex) {
        item.scrollIntoView({ block: 'nearest' });
      }
    });
  }

  function escapeHtml(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  // ---------------------------------------------------------------------------
  // 9. SIFT METHOD INTERACTIVE SIMULATOR
  // ---------------------------------------------------------------------------
  function initSiftSimulator() {
    const inputType = document.getElementById('sift-input-type');
    const targetGoal = document.getElementById('sift-target-goal');
    const constraintN = document.getElementById('sift-constraint-n');
    const patternName = document.getElementById('sift-matched-name');
    const familyPill = document.getElementById('sift-family-pill');
    const mantraText = document.getElementById('sift-mantra-text');

    if (!inputType || !targetGoal || !constraintN || !patternName) return;

    function evaluateSift() {
      const inp = inputType.value;
      const goal = targetGoal.value;

      let name = "Two Pointers (Opposite Ends)";
      let fam = "🏃 Runner";
      let mantra = "My input is a sorted array. I need to find a pair. The constraint is O(N). Therefore, shrink from both ends inwards.";

      if (inp === 'sorted_arr') {
        if (goal === 'pair_sum') {
          name = "Two Pointers (Opposite Ends)";
          fam = "🏃 Runner";
          mantra = "My input is a sorted array. I need a pair/triplet sum. Therefore, shrink inwards with two pointers.";
        } else {
          name = "Binary Search (Modified)";
          fam = "🔍 Searcher";
          mantra = "My input is sorted. I need to find an element or boundary. Therefore, cut the search space in half with lo and hi.";
        }
      } else if (inp === 'unsorted_arr') {
        if (goal === 'contiguous') {
          name = "Sliding Window Pattern";
          fam = "🏃 Runner";
          mantra = "My input is an array/string. I need a contiguous subarray/substring. Therefore, expand right, shrink left.";
        } else if (goal === 'pair_sum') {
          name = "Hash Map (Complement Lookup)";
          fam = "🔍 Searcher";
          mantra = "My input is unsorted. I need pairs. Therefore, store seen elements in an O(1) hash map.";
        } else if (goal === 'top_k') {
          name = "Top K Elements (Min-Heap)";
          fam = "📊 Ranker";
          mantra = "I need the K largest elements. Therefore, maintain a min-heap of size K.";
        } else if (goal === 'optimize') {
          name = "Dynamic Programming (Knapsack/Fibonacci)";
          fam = "🧮 Counter";
          mantra = "I need to count ways or maximize total value. Therefore, build state transition recurrence with memoization.";
        }
      } else if (inp === 'linked_list') {
        if (goal === 'cycle') {
          name = "Fast & Slow Pointers (Tortoise & Hare)";
          fam = "🏃 Runner";
          mantra = "My input is a linked list. I need to detect a cycle or find middle. Therefore, step slow by 1 and fast by 2.";
        } else {
          name = "In-place Reversal of LinkedList";
          fam = "🔗 Connector";
          mantra = "I need to reverse links between positions. Therefore, dance prev, curr, and next in place.";
        }
      } else if (inp === 'tree') {
        if (goal === 'contiguous' || goal === 'cycle') {
          name = "Tree Breadth First Search (BFS)";
          fam = "🌲 Explorer";
          mantra = "I need level-by-level traversal. Therefore, use a queue with level_size loop.";
        } else {
          name = "Tree Depth First Search (DFS)";
          fam = "🌲 Explorer";
          mantra = "I need path sums or tree depth. Therefore, recurse left and right with base cases.";
        }
      } else if (inp === 'graph') {
        if (goal === 'connected') {
          name = "Island Traversal / Union Find";
          fam = "🌲 Explorer / 🔗 Connector";
          mantra = "I need connected components or islands. Therefore, mark visited with BFS grid flood-fill or Disjoint Set.";
        } else {
          name = "Topological Sort (Kahn's Algorithm)";
          fam = "🔗 Connector";
          mantra = "I have task dependencies. Therefore, compute in-degrees and process in-degree 0 nodes with a queue.";
        }
      } else if (inp === 'intervals') {
        name = "Merge Intervals Pattern";
        fam = "📦 Sorter";
        mantra = "My input has start/end intervals. Therefore, sort by start time and merge overlapping pairs greedily.";
      }

      patternName.innerText = name;
      familyPill.innerText = fam;
      mantraText.innerText = mantra;
      playCyberBeep(700, 'sine', 0.04);
    }

    inputType.addEventListener('change', evaluateSift);
    targetGoal.addEventListener('change', evaluateSift);
    constraintN.addEventListener('change', evaluateSift);
  }

  // ---------------------------------------------------------------------------
  // 10. ZOOMABLE MERMAID CANVAS ENGINE & TOP-LAYER THEATER MODAL
  // ---------------------------------------------------------------------------
  function initZoomableCanvases() {
    const theaterModal = document.getElementById('theater-modal');
    const theaterTitle = document.getElementById('theater-title');
    const theaterSurface = document.getElementById('theater-surface');
    const theaterViewport = document.getElementById('theater-viewport');
    const closeTheaterBtn = document.getElementById('theater-close-btn');
    const theaterZoomIn = document.getElementById('theater-zoom-in');
    const theaterZoomOut = document.getElementById('theater-zoom-out');
    const theaterZoomReset = document.getElementById('theater-zoom-reset');
    const theaterZoomFit = document.getElementById('theater-zoom-fit');
    const theaterZoomBadge = document.getElementById('theater-zoom-badge');

    let activeTheaterZoom = 1.0;
    let activeTheaterPanX = 0;
    let activeTheaterPanY = 0;
    let isTheaterPanning = false;
    let theaterStartX = 0;
    let theaterStartY = 0;
    let savedScrollY = 0;
    let activeSourceContainer = null;
    let cachedVbW = 800;
    let cachedVbH = 500;

    function applyTheaterTransform() {
      if (!theaterSurface) return;
      theaterSurface.style.transform = `translate(${activeTheaterPanX}px, ${activeTheaterPanY}px) scale(${activeTheaterZoom})`;
      if (theaterZoomBadge) theaterZoomBadge.innerText = `${Math.round(activeTheaterZoom * 100)}%`;
    }

    function calculateFitScale(svgEl) {
      if (!theaterViewport) return 1.0;
      let vbW = cachedVbW;
      let vbH = cachedVbH;
      if (!vbW || !vbH) {
        if (svgEl) {
          const vb = svgEl.getAttribute('viewBox');
          if (vb) {
            const parts = vb.trim().split(/[\s,]+/).map(Number);
            if (parts.length >= 4 && parts[2] > 0 && parts[3] > 0) {
              vbW = parts[2];
              vbH = parts[3];
            }
          }
        }
      }
      vbW = vbW || 800;
      vbH = vbH || 500;
      const availW = Math.max(300, (theaterViewport.clientWidth || window.innerWidth) - 64);
      const availH = Math.max(200, (theaterViewport.clientHeight || window.innerHeight) - 64);
      const fitW = availW / vbW;
      const fitH = availH / vbH;
      const scale = Math.min(fitW, fitH);
      return Math.max(0.15, Math.min(scale, 3.5));
    }

    async function openTheater(title, sourceContainer) {
      if (!theaterModal || !theaterSurface || !sourceContainer) return;

      // 1. Save scroll position precisely BEFORE opening
      savedScrollY = window.scrollY || window.pageYOffset;
      activeSourceContainer = sourceContainer;

      // Clean emoji duplication in header
      const emojiMatch = title.match(/^(\p{Extended_Pictographic}+|\S+)\s*(.*)$/u);
      if (emojiMatch && emojiMatch[2]) {
        const iconEl = theaterModal.querySelector('.theater-icon');
        if (iconEl) iconEl.innerText = emojiMatch[1];
        theaterTitle.innerText = emojiMatch[2];
      } else {
        theaterTitle.innerText = title;
      }
      theaterSurface.innerHTML = '';

      // 2. Clone ONLY the SVG element directly (no <pre> or wrapper clutter!)
      let originalSvg = sourceContainer.querySelector('.mermaid svg');
      if (!originalSvg) {
        const pre = sourceContainer.querySelector('.mermaid');
        if (pre && window.mermaid) {
          try {
            await renderMermaidElement(pre);
            originalSvg = pre.querySelector('svg') || sourceContainer.querySelector('.mermaid svg');
          } catch (e) {
            console.warn('Theater mode on-demand render failed:', e);
          }
        }
      }

      if (originalSvg) {
        const cleanSvg = originalSvg.cloneNode(true);
        cleanSvg.removeAttribute('style');

        let vbW = 0, vbH = 0;
        const vb = cleanSvg.getAttribute('viewBox');
        if (vb) {
          const parts = vb.trim().split(/[\s,]+/).map(Number);
          if (parts.length >= 4 && parts[2] > 0 && parts[3] > 0) {
            vbW = parts[2];
            vbH = parts[3];
          }
        }
        if (vbW && vbH) {
          cachedVbW = vbW;
          cachedVbH = vbH;
          cleanSvg.style.width = vbW + 'px';
          cleanSvg.style.height = vbH + 'px';
        } else {
          cachedVbW = 800;
          cachedVbH = 500;
          cleanSvg.style.width = '100%';
          cleanSvg.style.height = 'auto';
        }
        cleanSvg.style.maxWidth = 'none';
        cleanSvg.style.maxHeight = 'none';
        theaterSurface.appendChild(cleanSvg);
      } else {
        const surf = sourceContainer.querySelector('.canvas-content-surface');
        if (surf) theaterSurface.innerHTML = surf.innerHTML;
      }

      // 3. Open modal and freeze background
      theaterModal.showModal();
      document.body.classList.add('theater-open');

      // 4. Fit to Viewport by default: make use of screen boundaries
      const renderedSvg = theaterSurface.querySelector('svg');
      activeTheaterZoom = calculateFitScale(renderedSvg);
      activeTheaterPanX = 0;
      activeTheaterPanY = 0;
      applyTheaterTransform();

      playCyberBeep(1100, 'triangle', 0.06);
    }

    function closeTheater() {
      if (!theaterModal || !theaterModal.open) return;
      theaterModal.close();
      document.body.classList.remove('theater-open');
      if (theaterSurface) theaterSurface.innerHTML = '';

      // 5. RESTORE USER'S EXACT SCROLL POSITION INSTANTLY (ZERO TREASURE HUNT!)
      window.scrollTo({ top: savedScrollY, behavior: 'instant' });

      // 6. Highlight original container so user is grounded - zero forced reflow
      if (activeSourceContainer) {
        const container = activeSourceContainer;
        requestAnimationFrame(() => {
          container.classList.add('flash-focus');
          setTimeout(() => container?.classList.remove('flash-focus'), 1800);
        });
      }

      playCyberBeep(650, 'sine', 0.04);
    }

    // Explicit dismiss ONLY: clicking close button (✕) or pressing Esc key
    // Diagram area & viewport clicks remain interactive for panning, exploring, and copying text
    if (closeTheaterBtn) closeTheaterBtn.addEventListener('click', closeTheater);
    if (theaterModal) {
      theaterModal.addEventListener('cancel', e => {
        e.preventDefault();
        closeTheater();
      });
      theaterModal.addEventListener('close', closeTheater);
    }

    if (theaterZoomIn) {
      theaterZoomIn.addEventListener('click', () => {
        activeTheaterZoom = Math.min(5.0, Number((activeTheaterZoom + 0.25).toFixed(2)));
        applyTheaterTransform();
        playCyberBeep(920, 'sine', 0.03);
      });
    }

    if (theaterZoomOut) {
      theaterZoomOut.addEventListener('click', () => {
        activeTheaterZoom = Math.max(0.15, Number((activeTheaterZoom - 0.25).toFixed(2)));
        applyTheaterTransform();
        playCyberBeep(760, 'sine', 0.03);
      });
    }

    if (theaterZoomReset) {
      theaterZoomReset.addEventListener('click', () => {
        activeTheaterZoom = 1.0; // 100% 1:1 true native size
        activeTheaterPanX = 0;
        activeTheaterPanY = 0;
        applyTheaterTransform();
        playCyberBeep(840, 'sine', 0.03);
      });
    }

    if (theaterZoomFit) {
      theaterZoomFit.addEventListener('click', () => {
        const svg = theaterSurface.querySelector('svg');
        if (svg) {
          activeTheaterZoom = calculateFitScale(svg);
          activeTheaterPanX = 0;
          activeTheaterPanY = 0;
          applyTheaterTransform();
          playCyberBeep(880, 'sine', 0.04);
        }
      });
    }

    // Theater draggable panning
    if (theaterViewport) {
      theaterViewport.addEventListener('pointerdown', e => {
        if (e.target.closest('button') || e.target.closest('text') || e.target.closest('foreignObject') || e.target.closest('span')) return;
        isTheaterPanning = true;
        theaterStartX = e.clientX - activeTheaterPanX;
        theaterStartY = e.clientY - activeTheaterPanY;
        theaterViewport.setPointerCapture(e.pointerId);
      });

      theaterViewport.addEventListener('pointermove', e => {
        if (!isTheaterPanning) return;
        activeTheaterPanX = e.clientX - theaterStartX;
        activeTheaterPanY = e.clientY - theaterStartY;
        applyTheaterTransform();
      });

      function stopTheaterPan(e) {
        if (!isTheaterPanning) return;
        isTheaterPanning = false;
        try { theaterViewport.releasePointerCapture(e.pointerId); } catch (_) {}
      }

      theaterViewport.addEventListener('pointerup', stopTheaterPan);
      theaterViewport.addEventListener('pointercancel', stopTheaterPan);

      // Mouse wheel zoom in theater
      theaterViewport.addEventListener('wheel', e => {
        e.preventDefault();
        const delta = e.deltaY < 0 ? 0.12 : -0.12;
        activeTheaterZoom = Math.min(4.0, Math.max(0.4, activeTheaterZoom + delta));
        applyTheaterTransform();
      }, { passive: false });
    }

    // In-card zoomable canvases
    document.querySelectorAll('.canvas-container').forEach(container => {
      const viewport = container.querySelector('.canvas-viewport');
      const surface = container.querySelector('.canvas-content-surface');
      const badge = container.querySelector('.zoom-level-badge');
      const zoomInBtn = container.querySelector('.zoom-in-btn');
      const zoomOutBtn = container.querySelector('.zoom-out-btn');
      const resetBtn = container.querySelector('.zoom-reset-btn');
      const fullscreenBtn = container.querySelector('.fullscreen-btn');
      const typeTag = container.querySelector('.canvas-type-tag')?.innerText || 'Architecture View';

      if (!viewport || !surface) return;

      let zoom = 1.0;
      let panX = 0;
      let panY = 0;
      let isPanning = false;
      let startX = 0;
      let startY = 0;

      function updateCardTransform() {
        surface.style.transform = `scale(${zoom}) translate(${panX}px, ${panY}px)`;
        if (badge) badge.innerText = `${Math.round(zoom * 100)}%`;
      }

      if (zoomInBtn) {
        zoomInBtn.addEventListener('click', () => {
          zoom = Math.min(3.0, zoom + 0.15);
          updateCardTransform();
          playCyberBeep(900, 'sine', 0.03);
        });
      }

      if (zoomOutBtn) {
        zoomOutBtn.addEventListener('click', () => {
          zoom = Math.max(0.5, zoom - 0.15);
          updateCardTransform();
          playCyberBeep(750, 'sine', 0.03);
        });
      }

      if (resetBtn) {
        resetBtn.addEventListener('click', () => {
          zoom = 1.0;
          panX = 0;
          panY = 0;
          updateCardTransform();
          playCyberBeep(820, 'sine', 0.04);
        });
      }

      if (fullscreenBtn) {
        fullscreenBtn.addEventListener('click', async () => {
          let svgEl = container.querySelector('.mermaid svg');
          if (!svgEl) {
            const pre = container.querySelector('.mermaid:not([data-processed="true"])');
            if (pre && window.mermaid) {
              await renderMermaidElement(pre);
            }
          }
          openTheater(typeTag, container);
        });
      }

      viewport.addEventListener('pointerdown', e => {
        if (e.target.closest('button')) return;
        isPanning = true;
        startX = e.clientX - panX;
        startY = e.clientY - panY;
        viewport.setPointerCapture(e.pointerId);
      });

      viewport.addEventListener('pointermove', e => {
        if (!isPanning) return;
        panX = e.clientX - startX;
        panY = e.clientY - startY;
        updateCardTransform();
      });

      function stopPan(e) {
        if (!isPanning) return;
        isPanning = false;
        try { viewport.releasePointerCapture(e.pointerId); } catch (_) {}
      }

      viewport.addEventListener('pointerup', stopPan);
      viewport.addEventListener('pointercancel', stopPan);
    });
  }

  // ---------------------------------------------------------------------------
  // 11. LAZY MERMAID & KATEX ENGINE (Isolated Non-Blocking Renderers)
  // ---------------------------------------------------------------------------
  let mermaidCounter = 0;
  let mermaidObserver = null;

  async function renderMermaidElement(el) {
    if (!window.mermaid || !el) return;
    if (el.dataset.processed === "true" || el.dataset.processed === "rendering") return;

    if (!el.id) {
      el.id = 'mermaid-dyn-' + (++mermaidCounter);
    }

    const code = el.textContent.trim();
    if (!code) return;

    el.dataset.processed = "rendering";
    try {
      const renderId = 'svg-' + el.id.replace(/[^a-zA-Z0-9_-]/g, '_') + '-' + Math.random().toString(36).substr(2, 6);
      const { svg, bindFunctions } = await window.mermaid.render(renderId, code);
      el.innerHTML = svg;
      if (bindFunctions) bindFunctions(el);

      // Safari & Cross-Browser Sizing Normalization:
      // Inject explicit intrinsic width, height, and aspect-ratio from viewBox so WebKit doesn't collapse to 0x0
      const svgEl = el.querySelector('svg');
      if (svgEl) {
        const vb = svgEl.getAttribute('viewBox');
        if (vb) {
          const parts = vb.trim().split(/[\s,]+/).map(Number);
          if (parts.length >= 4 && parts[2] > 0 && parts[3] > 0) {
            svgEl.setAttribute('width', parts[2]);
            svgEl.setAttribute('height', parts[3]);
            svgEl.style.aspectRatio = `${parts[2]} / ${parts[3]}`;
          }
        }
      }

      el.dataset.processed = "true";
    } catch (e) {
      console.warn('Mermaid render failure on element:', el.id, e);
      el.dataset.processed = "error";
      document.querySelectorAll('[id^="dmermaid"]').forEach(n => n.remove());
    }
  }

  function renderVisibleDiagrams(container = document) {
    if (!window.mermaid || !container) return;
    const targets = container.querySelectorAll('.mermaid:not([data-processed="true"]):not([data-processed="rendering"])');
    if (!targets.length) return;
    const vh = window.innerHeight;
    targets.forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.top < vh + 600 && r.bottom > -600 && (r.width > 0 || r.height > 0 || el.offsetParent !== null)) {
        if (mermaidObserver) mermaidObserver.unobserve(el);
        renderMermaidElement(el);
      }
    });
  }

  function triggerDiagramRenders(container) {
    renderVisibleDiagrams(container);
  }

  function initLazyRenderers() {
    // Eagerly render the Master Decision Flowchart hero diagram on load
    const heroMermaid = document.getElementById('mermaid-diagram-master-flowchart');
    if (heroMermaid) {
      renderMermaidElement(heroMermaid);
    }

    // 1. Mermaid lazy rendering
    const mermaidElements = document.querySelectorAll('.mermaid:not([data-processed="true"])');
    if ('IntersectionObserver' in window && mermaidElements.length > 0) {
      mermaidObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const el = entry.target;
            const r = el.getBoundingClientRect();
            if (r.width > 0 || r.height > 0 || el.offsetParent !== null) {
              observer.unobserve(el);
              renderMermaidElement(el);
            }
          }
        });
      }, { rootMargin: '500px 0px' });

      mermaidElements.forEach(el => mermaidObserver.observe(el));
    }

    // Passive scroll watcher (Safari fallback & high-velocity scroll tracking)
    let scrollRenderTimer = null;
    window.addEventListener('scroll', () => {
      if (scrollRenderTimer) return;
      scrollRenderTimer = requestAnimationFrame(() => {
        scrollRenderTimer = null;
        renderVisibleDiagrams();
      });
    }, { passive: true });

    // Initial render pass for diagrams within viewport
    renderVisibleDiagrams();

    // Trigger render when details accordions open (guarded against batch expansion freeze)
    document.querySelectorAll('.problem-card, .theory-details').forEach(details => {
      details.addEventListener('toggle', () => {
        if (details.open && !STATE.isBatchExpanding) {
          renderVisibleDiagrams(details);
        }
      });
    });

    // 2. KaTeX Mathematical Typesetting
    if (window.renderMathInElement) {
      renderMathInElement(document.body, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    }
  }

  // ---------------------------------------------------------------------------
  // 12. DYNAMIC ACCORDION SCROLLSPY (Bi-Directional Synchrony)
  // ---------------------------------------------------------------------------
  function initScrollSpy() {
    const chapters = Array.from(document.querySelectorAll('.pattern-chapter'));
    const navLinks = Array.from(document.querySelectorAll('.nav-tree-link'));
    const navGroups = Array.from(document.querySelectorAll('.nav-tree-group'));
    const navHeaders = Array.from(document.querySelectorAll('.nav-tree-header'));
    if (!chapters.length) return;

    let currentActiveChapterId = null;
    let ticking = false;

    function onScrollUpdate() {
      ticking = false;
      if (STATE.isProgrammaticScroll) return;

      const scrollY = window.scrollY || window.pageYOffset;
      const headerHeight = 72; // 64px header + 8px cushion

      // If at the very top of the page (Hero HUD / SIFT area), keep all sidebar groups collapsed
      if (scrollY < 220) {
        if (currentActiveChapterId !== null) {
          currentActiveChapterId = null;
          navGroups.forEach(g => g.classList.remove('expanded'));
          navHeaders.forEach(h => h.classList.remove('active-branch'));
          navLinks.forEach(l => l.classList.remove('active'));
        }
        return;
      }

      // Find the chapter currently active on screen
      let activeChapter = null;
      for (let i = chapters.length - 1; i >= 0; i--) {
        const ch = chapters[i];
        const rect = ch.getBoundingClientRect();
        if (rect.top <= headerHeight + 60) {
          activeChapter = ch;
          break;
        }
      }
      if (!activeChapter && chapters.length > 0) {
        activeChapter = chapters[0];
      }

      if (!activeChapter) return;

      const activeChapterId = activeChapter.id;

      // 1. If active chapter changed, dynamically accordion the sidebar groups
      if (activeChapterId !== currentActiveChapterId) {
        currentActiveChapterId = activeChapterId;
        const targetGroup = document.getElementById(`nav-group-${activeChapterId}`);

        navGroups.forEach(group => {
          if (group === targetGroup) {
            group.classList.add('expanded');
          } else {
            group.classList.remove('expanded');
          }
        });

        navHeaders.forEach(header => {
          const group = header.closest('.nav-tree-group');
          if (group === targetGroup) {
            header.classList.add('active-branch');
          } else {
            header.classList.remove('active-branch');
          }
        });

        // Gently keep the active group visible in sidebar
        if (targetGroup) {
          targetGroup.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        }
      }

      // 2. Identify active sub-item inside activeChapter (if expanded)
      let activeSubId = null;
      if (!activeChapter.classList.contains('is-collapsed')) {
        const subItems = Array.from(activeChapter.querySelectorAll('[id]'));
        for (let i = subItems.length - 1; i >= 0; i--) {
          const item = subItems[i];
          if (item.classList.contains('problem-card') || item.id.startsWith('fund-')) {
            const r = item.getBoundingClientRect();
            if (r.top <= headerHeight + 50 && r.bottom > headerHeight) {
              activeSubId = item.id;
              break;
            }
          }
        }
      }

      // 3. Highlight matching link in sidebar
      navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (activeSubId && href === `#${activeSubId}`) {
          link.classList.add('active');
        } else if (!activeSubId && href === `#${activeChapterId}`) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
    }

    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(onScrollUpdate);
        ticking = true;
      }
    }, { passive: true });

    // Initial check after DOM setup
    onScrollUpdate();
  }

  // ---------------------------------------------------------------------------
  // INITIALIZATION ON DOMContentLoaded
  // ---------------------------------------------------------------------------
  document.addEventListener('DOMContentLoaded', () => {
    initThemeEngine();
    initHaloEngine();
    initSidebarResizer();
    initMobileDrawer();
    initCollapsibleChapters();
    initSearchModal();
    initSidebarFilters();
    initSiftSimulator();
    initZoomableCanvases();
    initLazyRenderers();
    initScrollSpy();

    console.log('%c Ω DSA PATTERN BIBLE — Activated ', 'background:#00f2fe;color:#03020a;font-weight:bold;padding:4px 8px;border-radius:4px;');
  });
})();
