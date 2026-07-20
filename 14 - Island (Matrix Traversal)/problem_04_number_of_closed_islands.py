"""
============================================================
Problem: Number of Closed Islands
Pattern: Island (Matrix Traversal)
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-closed-islands/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
WARNING: In this specific problem, `0` is Land, and `1` is Water!
A "Closed Island" is a piece of land that is COMPLETELY surrounded by water.
If an island touches the very edge of the map, it is NOT closed, because we don't 
know what's beyond the edge of the map! It might be connected to a huge continent.
So how do we only count the closed ones?
We do this in Two Passes (two steps).
Step 1: The "Border Patrol".
We walk entirely around the outer edge of the map. If we see ANY land (0) touching 
the edge, we drop our paint bucket and sink that entire island (turn it to 1).
By the time we finish the border patrol, every single island that touched the 
edge is gone.
Step 2: The "Safe Zone".
Now we just scan the whole map normally, exactly like we did in Problem 1. 
Any land we find NOW is guaranteed to be a completely Closed Island! We count it, 
sink it, and keep scanning.

APPROACH:
---------
1. Initialize `ROWS, COLS = len(grid), len(grid[0])`.
2. Define `dfs(r, c)` that sinks land (`grid[r][c] = 1`).
3. SINK THE BORDERS (Pass 1):
   - Loop through every column in the FIRST row (`r=0`) and LAST row (`r=ROWS-1`). 
     If `grid[r][c] == 0`, call `dfs(r, c)`.
   - Loop through every row in the FIRST col (`c=0`) and LAST col (`c=COLS-1`). 
     If `grid[r][c] == 0`, call `dfs(r, c)`.
4. COUNT CLOSED ISLANDS (Pass 2):
   - Initialize `closed_islands = 0`.
   - Loop through all rows and cols.
   - If `grid[r][c] == 0`, increment `closed_islands` and call `dfs(r, c)`.
5. Return `closed_islands`.

COMPLEXITY:
-----------
Time:  O(M * N) — We still only visit every cell a constant number of times.
Space: O(M * N) — Recursion stack depth.

EDGE CASES:
-----------
- Edge case 1: The entire grid is one big island. The Border Patrol will sink the whole thing, and the safe zone scan will find 0 islands. Correct!
============================================================
"""

from typing import List

def closed_island(grid: List[List[int]]) -> int:
    """
    Returns the number of closed islands (completely surrounded by water).
    Note: 0 is land, 1 is water.
    """
    if not grid:
        return 0

    ROWS = len(grid)
    COLS = len(grid[0])
    
    def sink(r: int, c: int):
        # Base cases: out of bounds, or already water (1)
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 1:
            return
        
        # Sink the land
        grid[r][c] = 1
        
        sink(r - 1, c)
        sink(r + 1, c)
        sink(r, c - 1)
        sink(r, c + 1)

    # 1. BORDER PATROL: Sink all islands connected to the edge of the map
    for r in range(ROWS):
        for c in range(COLS):
            # Only trigger DFS if we are on the border AND we see land (0)
            if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and grid[r][c] == 0:
                sink(r, c)
                
    # 2. SAFE ZONE: Count whatever is left!
    closed_islands = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                closed_islands += 1
                sink(r, c)
                
    return closed_islands

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    grid1 = [
        [1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]
    ]
    # The '0's on the right edge are not closed. 
    # The '0' at (3,6) touches the bottom edge if we trace it. Wait, (3,6) is 0, (4,6) is 1... it doesn't touch the edge!
    # Ah, let's just test it and make sure it handles things correctly.
    # The island in the top left/middle:
    # 0,0,0,0
    # 0,1,0,1
    # 0,0,0,0
    # That big circle of 0s is totally enclosed by 1s. That's 1 closed island.
    # The 0 at (3,6) is also enclosed by 1s. That's 2 closed islands.
    assert closed_island(grid1) == 2, f"Test 1 failed: {closed_island(grid1)}"

    grid2 = [
        [0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]
    ]
    # The island in the middle (1,2) is surrounded by 1s. The rest touch the borders.
    assert closed_island(grid2) == 1, "Test 2 failed"

    # 🔲 Edge cases
    assert closed_island([[0,0],[0,0]]) == 0, "Edge 1: All land (all touches borders)"
    assert closed_island([[1,1],[1,1]]) == 0, "Edge 2: All water"

    print("All tests passed!")
