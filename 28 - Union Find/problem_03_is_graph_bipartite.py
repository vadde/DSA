"""
============================================================
Problem: Is Graph Bipartite?
Pattern: Union Find (or BFS/DFS 2-coloring)
Difficulty: Medium
LeetCode: #785
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A graph is bipartite if its nodes can be split into two groups (A and B)
such that every edge goes BETWEEN the groups (not within).
Like teams in a game: no edge connects two players on the same team.
BFS 2-coloring: color each node with color 0 or 1. If a neighbor has the
same color → NOT bipartite.

APPROACH: BFS 2-coloring
---------
Use BFS. Assign color 0 to start node. Neighbors get color 1.
If any neighbor already has the same color as the current node → False.

COMPLEXITY: O(V + E).
============================================================
"""

from typing import List
from collections import deque


def is_bipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue
        queue: deque[int] = deque([start])
        color[start] = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False  # same color → not bipartite
    return True


if __name__ == "__main__":
    assert is_bipartite([[1,2,3],[0,2],[0,1,3],[0,2]]) is False, "Test 1: odd cycle"
    assert is_bipartite([[1,3],[0,2],[1,3],[0,2]]) is True,      "Test 2: bipartite"
    assert is_bipartite([[],[],[],[]]) is True,                   "Edge: no edges"
    print("All tests passed!")
