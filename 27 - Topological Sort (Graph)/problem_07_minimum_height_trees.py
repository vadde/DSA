"""
============================================================
Problem: Minimum Height Trees
Pattern: Topological Sort (Graph)
Difficulty: Hard
LeetCode: #310
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A tree with N nodes. Any node can be the root. Some roots give taller trees,
some give shorter. Find ALL roots that give the MINIMUM height tree.
Key insight: The minimum height roots are always the center(s) of the tree.
There can be at most 2 such centers.

APPROACH: Leaf-Peeling (Like Topological Sort from outside in)
---------
Repeatedly remove all current leaf nodes (degree 1) until 1 or 2 nodes remain.
Those remaining nodes are the minimum height tree roots.
(Think of it as Kahn's algorithm from the leaves inward.)

COMPLEXITY: O(N) time, O(N) space.
============================================================
"""

from typing import List
from collections import deque


def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    adj: List[set[int]] = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    leaves: deque[int] = deque(i for i in range(n) if len(adj[i]) == 1)
    remaining = n

    while remaining > 2:
        leaf_count = len(leaves)
        remaining -= leaf_count
        new_leaves: deque[int] = deque()
        for _ in range(leaf_count):
            leaf = leaves.popleft()
            for neighbor in adj[leaf]:
                adj[neighbor].discard(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
        leaves = new_leaves

    return list(leaves)


if __name__ == "__main__":
    assert sorted(find_min_height_trees(4, [[1,0],[1,2],[1,3]])) == [1],        "Test 1"
    assert sorted(find_min_height_trees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) == [3,4], "Test 2"
    assert find_min_height_trees(1, []) == [0],                                 "Edge: single"
    assert sorted(find_min_height_trees(2, [[0,1]])) == [0, 1],                 "Edge: two nodes"
    print("All tests passed!")
