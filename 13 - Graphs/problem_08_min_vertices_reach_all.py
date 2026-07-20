"""
============================================================
Problem: Minimum Number of Vertices to Reach All Nodes
Pattern: Graphs (In-Degree Analysis)
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a bunch of rooms connected by one-way doors. You want to find the
SMALLEST set of rooms to start from so that you can eventually reach EVERY
room in the building. Answer: start from any room that has NO doors leading
INTO it (in-degree = 0). If nobody can reach that room, you MUST start there!

APPROACH:
---------
1. For a DAG (directed acyclic graph), a node that has no incoming edges
   CANNOT be reached from any other node.
2. Therefore, ALL nodes with in-degree 0 MUST be starting points.
3. Conversely, any node with in-degree > 0 CAN be reached from some other node.
4. So the answer is simply: all nodes with in-degree 0!

COMPLEXITY:
-----------
Time:  O(V + E) — scan edges to compute in-degrees, then scan nodes.
Space: O(V) — in-degree array.

EDGE CASES:
-----------
- Single node with no edges → return [0].
- Star graph (all edges from one center) → center is the only answer.
============================================================
"""

from typing import List


def find_smallest_set_of_vertices(n: int, edges: List[List[int]]) -> List[int]:
    has_incoming = set()
    for _, to_node in edges:
        has_incoming.add(to_node)

    # Nodes with no incoming edges must be starting points
    return [i for i in range(n) if i not in has_incoming]


if __name__ == "__main__":
    assert sorted(find_smallest_set_of_vertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]])) == [0, 3], "Test 1"
    assert sorted(find_smallest_set_of_vertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]])) == [0, 2, 3], "Test 2"
    assert find_smallest_set_of_vertices(1, []) == [0], "Test 3: single node"
    print("All tests passed!")
