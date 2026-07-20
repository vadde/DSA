"""
============================================================
Problem: Find Eventual Safe States
Pattern: Graphs (Cycle Detection / Topological Sort)
Difficulty: Medium
Link: https://leetcode.com/problems/find-eventual-safe-states/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a game board where each square has arrows pointing to other squares.
A "safe" square is one where NO MATTER which arrows you follow, you ALWAYS
eventually reach a square with no outgoing arrows (a "terminal" node).
A square is "unsafe" if there's ANY path from it that leads to a cycle
(an infinite loop where you go around in circles forever).

APPROACH:
---------
1. A node is safe if ALL its outgoing paths lead to terminal (safe) nodes.
2. A node is unsafe if it's part of a cycle or can reach a cycle.
3. Use DFS with 3-color marking:
   - WHITE (0): unvisited.
   - GRAY (1): currently in the DFS stack (being explored).
   - BLACK (2): fully explored and determined to be safe.
4. If we encounter a GRAY node during DFS, we found a cycle → not safe.
5. If all neighbors of a node are BLACK, the node is BLACK (safe).

COMPLEXITY:
-----------
Time:  O(V + E)
Space: O(V)

EDGE CASES:
-----------
- Terminal nodes (no outgoing edges) are always safe.
- Self-loops make a node unsafe.
============================================================
"""

from typing import List


def eventual_safe_nodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    # 0 = white, 1 = gray, 2 = black
    color = [0] * n

    def dfs(node: int) -> bool:
        """Returns True if node is safe (eventually terminal)."""
        if color[node] != 0:
            return color[node] == 2

        color[node] = 1  # Mark gray (in progress)

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False  # Found cycle or reaches a cycle

        color[node] = 2  # Mark black (safe)
        return True

    return [i for i in range(n) if dfs(i)]


if __name__ == "__main__":
    assert eventual_safe_nodes([[1,2],[2,3],[5],[0],[5],[],[]]) == [2,4,5,6], "Test 1"
    assert eventual_safe_nodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]) == [4], "Test 2"
    assert eventual_safe_nodes([[]]) == [0], "Test 3: single terminal"
    assert eventual_safe_nodes([[0]]) == [], "Test 4: self-loop"
    print("All tests passed!")
