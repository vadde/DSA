"""
============================================================
Problem: Topological Sort
Pattern: Topological Sort (Graph)
Difficulty: Medium
Classic (Kahn's Algorithm — BFS)
============================================================
"""

from typing import List
from collections import deque


def topological_sort(vertices: int, edges: List[List[int]]) -> List[int]:
    """Returns a topological ordering of vertices, or [] if cycle detected."""
    adj: List[List[int]] = [[] for _ in range(vertices)]
    in_degree = [0] * vertices

    for src, dst in edges:
        adj[src].append(dst)
        in_degree[dst] += 1

    queue: deque[int] = deque(v for v in range(vertices) if in_degree[v] == 0)
    result: List[int] = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == vertices else []  # [] = cycle detected


if __name__ == "__main__":
    order = topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    # Valid order: 3 must come before 2, 2 before 0, 2 before 1
    assert order.index(3) < order.index(2), "3 before 2"
    assert order.index(2) < order.index(0), "2 before 0"
    assert order.index(2) < order.index(1), "2 before 1"
    # Cycle detection
    assert topological_sort(2, [[0, 1], [1, 0]]) == [], "Cycle → empty"
    print("All tests passed!")
