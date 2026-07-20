"""
============================================================
Problem: Number of Provinces
Pattern: Union Find
Difficulty: Medium
LeetCode: #547
============================================================
isConnected[i][j]=1 means city i and j are directly connected.
Find the number of connected components (provinces).
Approach: Union-Find on N cities. Count distinct roots.
============================================================
"""

from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # number of components

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.count -= 1


def find_circle_num(is_connected: List[List[int]]) -> int:
    n = len(is_connected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                uf.union(i, j)
    return uf.count


if __name__ == "__main__":
    assert find_circle_num([[1,1,0],[1,1,0],[0,0,1]]) == 2, "Test 1"
    assert find_circle_num([[1,0,0],[0,1,0],[0,0,1]]) == 3, "Test 2"
    assert find_circle_num([[1]]) == 1,                     "Edge: single city"
    print("All tests passed!")
