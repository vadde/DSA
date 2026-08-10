# 📚 Trees & Graphs: The Complete Guide

> A comprehensive, from-first-principles deep-dive into Trees and Graphs — the two most important data structures in computer science interviews. Written for everyone from curious beginners to PhD candidates.

---

## 🌲 Part 1: Trees — Complete Guide

[📂 `010 - Trees (The Complete Guide)/`](010%20-%20Trees%20(The%20Complete%20Guide)/)

| Chapter | File | Topics Covered |
|---------|------|---------------|
| **Ch 1** | [What Is a Tree?](010%20-%20Trees%20(The%20Complete%20Guide)/01_what_is_a_tree.md) | Formal definition, complete terminology bible (root/leaf/height/depth/level/ancestor/subtree), N−1 edges property, recursive definition, Handshaking Lemma, tree taxonomy |
| **Ch 2** | [Binary Trees](010%20-%20Trees%20(The%20Complete%20Guide)/02_binary_trees.md) | 5 types (full/complete/perfect/balanced/degenerate), all math formulas, array representation, heap connection, Python TreeNode |
| **Ch 3** | [Tree Traversals](010%20-%20Trees%20(The%20Complete%20Guide)/03_tree_traversals.md) | All 4 traversals (BFS/pre/in/post-order), recursive + iterative Python, call stack visualization, generator pattern, DFS vs BFS space |
| **Ch 4** | [Binary Search Trees](010%20-%20Trees%20(The%20Complete%20Guide)/04_binary_search_trees.md) | BST property, all 3 delete cases, in-order successor/predecessor, complexity (balanced vs skewed), BST↔sorted array duality, interview patterns |
| **Ch 5** | [Balanced Trees](010%20-%20Trees%20(The%20Complete%20Guide)/05_balanced_trees.md) | Why BSTs fail, AVL balance factor + 4 rotations, Red-Black 5 properties + O(log N) proof, B-Trees, Python SortedList/heapq |
| **Ch 6** | [Special Trees](010%20-%20Trees%20(The%20Complete%20Guide)/06_special_trees.md) | N-ary trees, Trie, Segment Tree, Fenwick Tree, Heap, Expression Trees — structure + code + pattern links |
| **⚡ Ch 7** | [Trees Cheat Sheet](010%20-%20Trees%20(The%20Complete%20Guide)/07_trees_cheat_sheet.md) | All formulas, traversal mnemonics, complexity table, which-tree decision flowchart, pattern map, top 10 traps |

---

## 🕸️ Part 2: Graphs — Complete Guide

[📂 `011 - Graphs (The Complete Guide)/`](011%20-%20Graphs%20(The%20Complete%20Guide)/)

| Chapter | File | Topics Covered |
|---------|------|---------------|
| **Ch 1** | [What Is a Graph?](011%20-%20Graphs%20(The%20Complete%20Guide)/01_what_is_a_graph.md) | Formal G=(V,E), complete terminology bible, Handshaking Lemma with proof, Euler's Formula, Tree as special graph, graph density |
| **Ch 2** | [Graph Types](011%20-%20Graphs%20(The%20Complete%20Guide)/02_graph_types.md) | Directed/undirected, weighted, DAG, bipartite, complete, connected/strongly connected, sparse/dense, planar — all with diagrams |
| **Ch 3** | [Graph Representations](011%20-%20Graphs%20(The%20Complete%20Guide)/03_graph_representations.md) | Adjacency list/matrix/edge list — code, full trade-off table, grid as implicit graph, Python tips |
| **Ch 4** | [Graph Traversals](011%20-%20Graphs%20(The%20Complete%20Guide)/04_graph_traversals.md) | BFS/DFS with visited set, step-by-step traces, when-to-use flowchart, connected components, multi-source BFS, 0-1 BFS |
| **Ch 5** | [Shortest Paths](011%20-%20Graphs%20(The%20Complete%20Guide)/05_shortest_paths.md) | BFS (unweighted), Dijkstra's (positive weights), Bellman-Ford (negative weights), Floyd-Warshall (all-pairs) — traces + code + comparison |
| **Ch 6** | [Minimum Spanning Trees](011%20-%20Graphs%20(The%20Complete%20Guide)/06_minimum_spanning_trees.md) | Cut property, Kruskal's (Union-Find), Prim's (min-heap) — step-by-step traces + code + real-world apps |
| **Ch 7** | [Advanced Graph Concepts](011%20-%20Graphs%20(The%20Complete%20Guide)/07_advanced_graph_concepts.md) | Cycle detection (undirected+directed), topological sort (DFS+Kahn's), Union-Find, SCCs, bridges, graph coloring, relationship map |
| **⚡ Ch 8** | [Graphs Cheat Sheet](011%20-%20Graphs%20(The%20Complete%20Guide)/08_graphs_cheat_sheet.md) | All algorithms + complexity, representation table, master decision flowchart, pattern map, top 10 traps, interview checklist |

---

## 🔗 The Big Picture: How Everything Connects

```
Tree ⊂ Graph             (a tree IS a connected acyclic graph)
Heap = Complete BT +     Heap-order property
Trie = N-ary Tree +      Character-edge semantics
BST  = Binary Tree +     BST ordering property (left < root < right)
AVL  = BST +             Balance factor ±1 invariant
RB   = BST +             5 Red-Black coloring properties
DAG  = Directed Graph +  No directed cycles → enables Topological Sort
MST  = Spanning tree +   Minimum total edge weight (Kruskal / Prim)
Union-Find = Forest of   inverted trees (children point to parents)
BFS Pattern = Level-order traversal generalized to graphs
```

---

## 🔗 Links to Coding Patterns

| Concept | DSA Pattern Folder |
|---------|--------------------|
| Tree BFS (level-order) | `11 - Tree Breadth First Search/` |
| Tree DFS (root-to-leaf) | `12 - Tree Depth First Search/` |
| Graph traversal + components | `13 - Graphs/` |
| Grid/matrix traversal | `14 - Island (Matrix Traversal)/` |
| Heaps | `06 - Min and Max Heap/`, `15 - Two Heaps/`, `19 - Top K Elements/` |
| Trie | `07 - Trie/`, `26 - Trie/` |
| Topological sort (DAG) | `27 - Topological Sort (Graph)/` |
| Union-Find (DSU) | `28 - Union Find/` |
| Segment Tree | `41 - Segment Tree/` |
| Binary Indexed Tree | `42 - Binary Indexed Tree/` |
