# Chapter 8: Graphs Cheat Sheet ⚡

*Everything in one quick reference — algorithms, complexities, when to use what, and the key patterns.*

---

## ⚡ Algorithm Complexity at a Glance

| Algorithm | Use Case | Time | Space | Key Condition |
|-----------|---------|------|-------|---------------|
| **BFS** | Shortest path (unweighted) | O(V+E) | O(V) | Unweighted edges |
| **DFS** | Traversal, cycle detection, topo sort | O(V+E) | O(V) | Any graph |
| **Dijkstra's** | Shortest path (positive weights) | O((V+E) log V) | O(V) | No negative weights |
| **Bellman-Ford** | Shortest path (any weights) | O(VE) | O(V) | Detects neg cycles |
| **Floyd-Warshall** | All-pairs shortest path | O(V³) | O(V²) | Any weights |
| **0-1 BFS** | Shortest path (weights 0 or 1) | O(V+E) | O(V) | Only 0 or 1 weights |
| **Kruskal's MST** | Minimum Spanning Tree | O(E log E) | O(V) | Undirected connected |
| **Prim's MST** | Minimum Spanning Tree | O((V+E) log V) | O(V) | Undirected connected |
| **Topo Sort (DFS)** | Ordering in DAG | O(V+E) | O(V) | DAG only |
| **Topo Sort (Kahn's)** | Ordering in DAG | O(V+E) | O(V) | DAG only |
| **Union-Find** | Components, cycle detection | O(α(N)) ≈ O(1) | O(V) | Any graph |
| **Cycle detect (undirected)** | Has cycle? | O(V+E) | O(V) | — |
| **Cycle detect (directed)** | Has cycle? | O(V+E) | O(V) | 3-color DFS |

---

## 🗄️ Representation Trade-Off

| Operation | Adjacency List | Adjacency Matrix | Edge List |
|-----------|---------------|-----------------|-----------|
| Space | O(V+E) ✅ | O(V²) | O(E) |
| Add edge | O(1) | O(1) | O(1) |
| Edge exists? | O(degree) | O(1) ✅ | O(E) |
| Iterate neighbors | O(degree) ✅ | O(V) | O(E) |
| **Best for** | Most problems | Dense/Floyd-W | Kruskal's |

---

## 🤔 "Which Algorithm?" — Decision Flowchart

```mermaid
flowchart TD
    PROB{Problem type?} --> TRAV{Just traversal\nor components?}
    TRAV -->|Yes| BFSDFS["BFS (levels) or DFS (paths)\nO(V+E)"]
    TRAV -->|No| SHORT{Shortest path?}
    SHORT -->|Yes| UNWEIGHTED{Unweighted?}
    UNWEIGHTED -->|Yes| BFSSP["BFS\nO(V+E)"]
    UNWEIGHTED -->|No| NEGWEIGHT{Negative weights?}
    NEGWEIGHT -->|Yes| BELLF["Bellman-Ford\nO(VE)"]
    NEGWEIGHT -->|No| ALLPAIRS{All pairs?}
    ALLPAIRS -->|Yes| FLOYD["Floyd-Warshall\nO(V³)"]
    ALLPAIRS -->|No| DIJKSTRA["Dijkstra's\nO((V+E)logV)"]
    SHORT -->|No| ORDER{Need ordering\n(dependencies)?}
    ORDER -->|Yes| TOPO2["Topological Sort\n(Kahn's or DFS)\nO(V+E)"]
    ORDER -->|No| SPAN{Min spanning\ntree?}
    SPAN -->|Yes| SPARSE2{Sparse graph?}
    SPARSE2 -->|Yes| KRUSKAL["Kruskal's\nO(E log E)"]
    SPARSE2 -->|No| PRIM["Prim's\nO((V+E)logV)"]
    SPAN -->|No| UNION{Component\nor cycle check?}
    UNION -->|Yes| UF2["Union-Find\nO(α(N)) ≈ O(1)"]

    style BFSSP fill:#74B9FF,color:#333
    style DIJKSTRA fill:#6C5CE7,color:#fff
    style BELLF fill:#FF7675,color:#fff
    style FLOYD fill:#A29BFE,color:#fff
    style TOPO2 fill:#55EFC4,color:#333
    style KRUSKAL fill:#FDCB6E,color:#333
    style PRIM fill:#FDCB6E,color:#333
    style UF2 fill:#00B894,color:#fff
```

---

## 🔗 Pattern Connection Map

| DSA Pattern | Graph Concept | Key Chapter |
|------------|--------------|-------------|
| **Pattern 13** — Graphs | BFS/DFS traversal, connected components | Ch 4 |
| **Pattern 14** — Island Matrix | Grid as implicit graph, BFS/DFS | Ch 3, Ch 4 |
| **Pattern 27** — Topological Sort | DAG, topological ordering | Ch 7 |
| **Pattern 28** — Union Find | DSU, components, cycle detection | Ch 7 |
| **Shortest Path problems** | Dijkstra, Bellman-Ford, BFS | Ch 5 |
| **MST problems** | Kruskal, Prim | Ch 6 |
| **Bipartite check** | 2-coloring BFS | Ch 2 |
| **Cycle detection** | DFS 3-color / Union-Find | Ch 7 |
| **Clone Graph** | Graph BFS/DFS + hash map | Ch 4 |

---

## 🧠 Key Insights to Never Forget

| Insight | What it means |
|---------|--------------|
| **Tree ⊂ Graph** | Every tree IS a graph. Every tree algorithm also works on trees-as-graphs. |
| **Visited set is mandatory for graphs** | Without it, cycles cause infinite loops. Never skip it. |
| **BFS = shortest unweighted path** | BFS finds the shortest path in terms of EDGE COUNT (not weight). |
| **Dijkstra fails with negative weights** | Use Bellman-Ford when any weight can be negative. |
| **Topological sort = valid only for DAGs** | A cycle makes topological sort impossible (Kahn's returns fewer than N nodes). |
| **Union-Find ≈ O(1) per operation** | With path compression + union by rank, α(N) ≈ 1 for all practical N. |
| **Mark visited on enqueue, not dequeue** | Marking on dequeue allows the same node to be enqueued multiple times. |
| **Grid problems = graph problems** | Any 2D grid can be treated as an implicit adjacency list. |

---

## ⚠️ Top 10 Graph Interview Traps

| # | Trap | Correct Approach |
|---|------|----------------|
| 1 | **Forgetting visited set** | Always initialize before BFS/DFS |
| 2 | **Marking visited when dequeued (not enqueued)** | Mark when you ADD to queue, not when you process |
| 3 | **Assuming the graph is connected** | Always loop over all vertices and start new BFS/DFS for each unvisited |
| 4 | **Using Dijkstra's with negative weights** | Use Bellman-Ford instead |
| 5 | **DFS cycle detection: parent vs back-edge** | In undirected graphs, only flag a cycle if visited neighbor ≠ your parent |
| 6 | **Topological sort on a graph with cycles** | Check for cycles first; Kahn's signals it via `len(result) < n` |
| 7 | **Union-Find without path compression** | O(N) per operation instead of O(α(N)) — TLE on large inputs |
| 8 | **BFS for "all paths" problems** | BFS prunes paths once it finds a node. DFS + backtracking finds all paths. |
| 9 | **Not considering disconnected graphs** | "Number of components" = how many separate BFS/DFS runs you need |
| 10 | **Multi-source BFS: forgetting to mark all sources visited upfront** | Add ALL sources to visited AND queue at the start |

---

## 🏃 Interview Warm-Up Checklist

Before any graph problem, ask:
- [ ] Is the graph **directed** or **undirected**?
- [ ] Is it **weighted** or **unweighted**?
- [ ] Can there be **cycles**? (If not → DAG → topological sort)
- [ ] Is it **connected** or could there be multiple components?
- [ ] What **representation** is given? (adjacency list, matrix, edge list, grid?)
- [ ] Do I need **shortest path** (BFS/Dijkstra) or **all paths** (DFS)?
- [ ] Do I need to **detect cycles** (Union-Find or DFS coloring)?
- [ ] Will my DFS recursion hit a **stack overflow** on large inputs? (Switch to iterative)
- [ ] Have I initialized my **visited set** and am I marking on **enqueue**?

---

*← [Chapter 7: Advanced Concepts](07_advanced_graph_concepts.md)*

---

## 📚 Full Guide Navigation

### Trees (010 - Trees The Complete Guide)
1. [What Is a Tree?](../010%20-%20Trees%20%28The%20Complete%20Guide%29/01_what_is_a_tree.md)
2. [Binary Trees](../010%20-%20Trees%20%28The%20Complete%20Guide%29/02_binary_trees.md)
3. [Tree Traversals](../010%20-%20Trees%20%28The%20Complete%20Guide%29/03_tree_traversals.md)
4. [Binary Search Trees](../010%20-%20Trees%20%28The%20Complete%20Guide%29/04_binary_search_trees.md)
5. [Balanced Trees](../010%20-%20Trees%20%28The%20Complete%20Guide%29/05_balanced_trees.md)
6. [Special Trees](../010%20-%20Trees%20%28The%20Complete%20Guide%29/06_special_trees.md)
7. [Trees Cheat Sheet](../010%20-%20Trees%20%28The%20Complete%20Guide%29/07_trees_cheat_sheet.md)

### Graphs (011 - Graphs The Complete Guide)
1. [What Is a Graph?](01_what_is_a_graph.md)
2. [Graph Types](02_graph_types.md)
3. [Graph Representations](03_graph_representations.md)
4. [Graph Traversals](04_graph_traversals.md)
5. [Shortest Paths](05_shortest_paths.md)
6. [Minimum Spanning Trees](06_minimum_spanning_trees.md)
7. [Advanced Graph Concepts](07_advanced_graph_concepts.md)
8. **[Graphs Cheat Sheet](08_graphs_cheat_sheet.md)** ← You are here
