"""
============================================================
Problem: All Tasks Scheduling Orders
Pattern: Topological Sort (Graph)
Difficulty: Hard
Classic (Enumerate all valid topological orderings)
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Same setup as Course Schedule II, but now find ALL possible valid orderings.
This is an NP problem in the general case — we use backtracking + Kahn's.

APPROACH: Kahn's + Backtracking
---------
At each step, all nodes with in-degree 0 are "available" choices.
Pick one (branch), recurse on the remaining graph, backtrack.

COMPLEXITY: O(V! * (V+E)) worst case — exponential.
============================================================
"""

from typing import List
from collections import defaultdict


def all_topological_orders(vertices: int, edges: List[List[int]]) -> List[List[int]]:
    adj: dict[int, List[int]] = defaultdict(list)
    in_degree = [0] * vertices

    for src, dst in edges:
        adj[src].append(dst)
        in_degree[dst] += 1

    results: List[List[int]] = []

    def backtrack(current: List[int]) -> None:
        # Find all nodes with in-degree 0
        available = [v for v in range(vertices) if in_degree[v] == 0]
        if not available:
            if len(current) == vertices:
                results.append(current[:])
            return
        for node in available:
            # Choose
            current.append(node)
            in_degree[node] = -1  # mark chosen
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
            # Explore
            backtrack(current)
            # Unchoose (backtrack)
            current.pop()
            in_degree[node] = 0
            for neighbor in adj[node]:
                in_degree[neighbor] += 1

    backtrack([])
    return results


if __name__ == "__main__":
    orders = all_topological_orders(3, [[0, 2], [1, 2]])
    # 0 and 1 can be in either order; 2 must come last
    assert all(o.index(2) == 2 for o in orders), "2 always last"
    assert len(orders) == 2, "2 valid orderings: [0,1,2] and [1,0,2]"
    print("All tests passed!")
