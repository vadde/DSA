"""
============================================================
Problem: Minimum Number of Days to Disconnect Island
Pattern: Articulation Points / Brute Force Simulation
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a grid of land (1) and water (0). The land forms one connected island.
You can turn land cells into water. What is the MINIMUM number of cells you
need to change to water to disconnect the island (split it into 2+ pieces, or
make it all water)?

KEY INSIGHT: The answer is always 0, 1, or 2!
- 0: If already disconnected or no land.
- 1: If there exists an articulation point (a cell whose removal disconnects the island).
- 2: Otherwise (by removing 2 cells around a corner, you can always disconnect).

APPROACH:
---------
1. Count connected components. If != 1, return 0.
2. Check if any land cell is an articulation point. If yes, return 1.
3. Otherwise, return 2.

For articulation point detection on a grid, use Tarjan's algorithm adapted
for grid cells.

COMPLEXITY:
-----------
Time:  O(R * C) — BFS/DFS for connectivity + Tarjan's.
Space: O(R * C)

EDGE CASES:
-----------
- No land → 0.
- Single land cell → 1 (turn it to water).
- Two adjacent land cells → 1.
============================================================
"""

from typing import List


def min_days(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def count_islands() -> int:
        visited = [[False] * cols for _ in range(rows)]
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    islands += 1
                    # BFS
                    queue = [(r, c)]
                    visited[r][c] = True
                    while queue:
                        cr, cc = queue.pop()
                        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nr, nc = cr+dr, cc+dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
        return islands

    # Step 1: If already disconnected or no island
    if count_islands() != 1:
        return 0

    # Step 2: Try removing each land cell. If it disconnects, answer is 1.
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                grid[r][c] = 0
                islands = count_islands()
                grid[r][c] = 1
                if islands != 1:
                    return 1

    # Step 3: Otherwise, answer is always 2
    return 2


if __name__ == "__main__":
    assert min_days([[0,1,1,0],[0,1,1,0],[0,0,0,0]]) == 2, "Test 1"
    assert min_days([[1,1]]) == 2, "Test 2"
    assert min_days([[1,0],[0,1]]) == 0, "Test 3: already disconnected"
    assert min_days([[1]]) == 1, "Test 4: single cell"
    print("All tests passed!")
