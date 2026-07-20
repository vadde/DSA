"""
============================================================
Problem: Redundant Connection
Pattern: Union Find
Difficulty: Medium
LeetCode: #684
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given a tree (N nodes, N-1 edges) with ONE extra edge added (making exactly one cycle),
find the redundant edge that, if removed, makes the graph a valid tree again.
Return the last such edge in the input list (if multiple, return the later one).

APPROACH: Union Find — detect the edge that creates a cycle
---------
Process edges one by one. For each edge (u, v):
- If find(u) == find(v) → this edge creates a cycle → it's the REDUNDANT edge.
- Otherwise: union(u, v) and continue.

COMPLEXITY: O(N * α(N)) ≈ O(N).
============================================================
"""

from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    uf = UnionFind(len(edges))
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]
    return []


if __name__ == "__main__":
    assert find_redundant_connection([[1,2],[1,3],[2,3]]) == [2, 3], "Test 1"
    assert find_redundant_connection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1, 4], "Test 2"
    print("All tests passed!")
