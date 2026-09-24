# ⚔️ Pillar 2: The Pattern Cracker

> *"Don't memorize solutions. Memorize the shape of solutions."*  
> *"If you can classify a problem in under 10 seconds, you have already solved 80% of it."*

Welcome to **The Pattern Cracker** — the tactical command center for technical interviews. This module connects the deep theoretical limits of [Pillar 0](../000%20-%20Theoretical%20Foundations%20%28The%20Complete%20Guide%29/) and data structure engine rooms of [Pillar 1](../README.md#%EF%B8%8F-pillar-1-data-structure-engine-rooms-the-concrete-mechanics) with the 43 tactical problem-solving patterns.

---

## 📖 Primary Guide

👉 **[Read the Full Mental Model: `pattern_cracker_mental_model.md`](pattern_cracker_mental_model.md)**

---

## 🔑 The 5-Layer Elimination Funnel

When faced with any technical assessment question, run through this 5-question funnel in order:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. INPUT TYPE        ──► Array (Sorted? Unsorted?), String, Tree, Graph?    │
│ 2. OUTPUT ASKED      ──► Optimization (Min/Max), Decision (T/F), Counting?  │
│ 3. CONSTRAINTS       ──► N ≤ 10^3 (O(N^2) OK) vs N ≥ 10^5 (Need O(N log N))?│
│ 4. MEMORY / STATE    ──► Need past history? (Hash/Stack), O(1) in-place?    │
│ 5. PROBLEM SHRINKAGE ──► Divide into independent subproblems? (DP/D&C)      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 👨‍👩‍👧‍👦 The 7 Master Pattern Families

Rather than memorizing 43 disconnected patterns, recognize which family the problem belongs to:

| Family | Members | Core Tactical Idea |
|---|---|---|
| 🏃 **Runners** | Two Pointers, Fast & Slow, Sliding Window | Coordinated traversal through linear buffers |
| 📦 **Sorters** | Merge Intervals, Cyclic Sort, In-Place Reversals | Establishing invariant spatial or temporal order |
| 🌲 **Explorers** | BFS, DFS, Island Traversal, Backtracking | State-space search over trees, graphs, or permutations |
| 📊 **Rankers** | Top K, Two Heaps, K-Way Merge | Maintaining dynamic priority over streaming subsets |
| 🔍 **Searchers** | Binary Search, Trie, Hash Map | Logarithmic or constant-time element lookup |
| 🧮 **Counters** | Prefix Sum, Dynamic Programming, BIT, Segment Tree | Accumulating or decomposing aggregate values |
| 🔗 **Connectors** | Union Find, Topological Sort, Clone Graph | Managing dynamic partitions and dependency orders |

---

## 🌉 Cross-Pillar Bridges

### 🏛️ Upstream: The Physical Laws (Pillar 0)
- **Constraint Limits**: Before writing code, check the input size against the [Complexity Sizing Table](../000%20-%20Theoretical%20Foundations%20%28The%20Complete%20Guide%29/12_kill_mode_vs_pull_plug.md#1-the-input-constraint-sizing-table).
- **Kill Mode vs Pull the Plug**: If $N \le 20$ for an NP-Hard problem, go Kill Mode with Bitmask DP. If $N \ge 100$, Pull the Plug and switch to heuristics or greedy approximations ([Ch 12](../000%20-%20Theoretical%20Foundations%20%28The%20Complete%20Guide%29/12_kill_mode_vs_pull_plug.md)).

### ⚙️ Midstream: Concrete Engines (Pillar 1)
- **Hierarchical problems**: Review [009 - Trees (The Complete Guide)](../009%20-%20Trees%20%28The%20Complete%20Guide%29/).
- **Mesh / Dependency problems**: Review [010 - Graphs (The Complete Guide)](../010%20-%20Graphs%20%28The%20Complete%20Guide%29/).

### ⚔️ Downstream: Tactical Patterns (Pillar 2)
- Jump directly into the patterns catalog:
  - [02 - Two Pointers](../../02%20-%20Two%20Pointers/)
  - [04 - Sliding Window](../../04%20-%20Sliding%20Window/)
  - [11 - Tree Breadth First Search](../../11%20-%20Tree%20Breadth%20First%20Search/)
  - [13 - Graphs](../../13%20-%20Graphs/)
  - [16 - Subsets](../../16%20-%20Subsets/)
  - [27 - Topological Sort (Graph)](../../27%20-%20Topological%20Sort%20%28Graph%29/)

---

## 🧭 Navigation

| ← Previous (Pillar 1: Graphs) | ↑ Fundamentals Hub | Next (Pillar 2: Patterns) → |
|:---|:---:|---:|
| [🕸️ 010 - Graphs (The Complete Guide)](../010%20-%20Graphs%20%28The%20Complete%20Guide%29/) | [📚 Fundamentals Index](../README.md) | [01 - Warmup Patterns →](../../01%20-%20Warmup/) |
