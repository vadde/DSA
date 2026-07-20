"""
============================================================
Problem: Find if Path Exists in Graph
Pattern: Graphs (BFS/DFS)
Difficulty: Easy
Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a map of roads connecting cities. Given a start city and a destination
city, can you actually drive from start to destination using the roads? You
just need a yes or no answer — any path works!

APPROACH:
---------
1. Build an adjacency list from the edges.
2. BFS (or DFS) from `source`.
3. If we ever reach `destination`, return True.
4. If the queue empties without reaching it, return False.

COMPLEXITY:
-----------
Time:  O(V + E) — visit each node and edge once.
Space: O(V + E) — adjacency list + visited set.

EDGE CASES:
-----------
- source == destination → True.
- No edges at all → only True if source == destination.
- Disconnected graph components.
============================================================
"""

from typing import List
from collections import deque, defaultdict


def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = {source}
    queue = deque([source])

    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


if __name__ == "__main__":
    assert valid_path(3, [[0,1],[1,2],[2,0]], 0, 2) == True, "Test 1"
    assert valid_path(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5) == False, "Test 2"
    assert valid_path(1, [], 0, 0) == True, "Test 3: same node"
    assert valid_path(2, [], 0, 1) == False, "Test 4: no edges"
    print("All tests passed!")
