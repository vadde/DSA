# Pattern 28: Union Find (Disjoint Set Union)

## 👶 Explain Like I'm 5

Imagine a school with students. Some students are friends with each other,
and friends-of-friends are in the same "friend group".
Union Find answers: **"Are two students in the same friend group?"** in near-O(1) time.
Every student has a "representative" (like a group leader).
- **Find**: "Who is my group leader?"
- **Union**: "Merge two groups by making one leader point to the other."

---

## 🧩 Core Idea & Pattern Detection

**Union Find = Efficient group membership with path compression + union by rank.**

```python
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))  # each node is its own parent
        self.rank = [0] * n           # tree height approximation

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # already in same group
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True
```

### When to use it:
- Connected components in a graph.
- Detecting cycles in undirected graphs.
- Kruskal's Minimum Spanning Tree.
- Keywords: "connected", "same group", "merge", "redundant connection".

---

## ⏱️ Complexity Analysis

| Operation | Complexity |
|-----------|-----------|
| Find | O(α(N)) ≈ O(1) amortized |
| Union | O(α(N)) ≈ O(1) amortized |
| Space | O(N) |

(α = inverse Ackermann function, effectively constant for all practical N)

---

## ✅ Problems in This Pattern

| # | Problem | Difficulty | LeetCode |
|---|---------|------------|----------|
| 1 | Redundant Connection | Medium | #684 |
| 2 | Number of Provinces | Medium | #547 |
| 3 | Is Graph Bipartite? | Medium | #785 |
| 4 | Path With Minimum Effort | Medium | #1631 |
