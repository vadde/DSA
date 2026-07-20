"""
============================================================
Problem: Path With Minimum Effort
Pattern: Union Find / Binary Search + BFS
Difficulty: Medium
LeetCode: #1631
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Grid of heights. Find a path from top-left to bottom-right where the MAXIMUM
absolute difference between consecutive cells is MINIMIZED.
This is the "min bottleneck path" problem.

APPROACH: Dijkstra (Optimal for this problem)
---------
Use a min-heap (priority queue). For each cell, track the minimum effort to
reach it. effort[r][c] = min over all paths of the max step difference.
Start with effort[0][0] = 0. For each cell, try all 4 neighbors and update
their effort = max(current_effort, abs_height_diff).

COMPLEXITY: O(N*M*log(N*M)) — Dijkstra with priority queue.
============================================================
"""

from typing import List
import heapq
import math


def minimum_effort_path(heights: List[List[int]]) -> int:
    rows, cols = len(heights), len(heights[0])
    effort = [[math.inf] * cols for _ in range(rows)]
    effort[0][0] = 0
    min_heap = [(0, 0, 0)]  # (effort, row, col)

    while min_heap:
        eff, r, c = heapq.heappop(min_heap)
        if r == rows - 1 and c == cols - 1:
            return eff
        if eff > effort[r][c]:
            continue
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_eff = max(eff, abs(heights[nr][nc] - heights[r][c]))
                if new_eff < effort[nr][nc]:
                    effort[nr][nc] = new_eff
                    heapq.heappush(min_heap, (new_eff, nr, nc))

    return int(effort[rows - 1][cols - 1])


if __name__ == "__main__":
    assert minimum_effort_path([[1,2,2],[3,8,2],[5,3,5]]) == 2,             "Test 1"
    assert minimum_effort_path([[1,2,3],[3,8,4],[5,3,5]]) == 1,             "Test 2"
    assert minimum_effort_path([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0, "Test 3"
    assert minimum_effort_path([[1]]) == 0,                                 "Edge: 1x1"
    print("All tests passed!")
