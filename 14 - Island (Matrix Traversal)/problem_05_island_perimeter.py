"""
============================================================
Problem: Island Perimeter
Pattern: Island (Matrix Traversal)
Difficulty: Easy
Link: https://leetcode.com/problems/island-perimeter/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are building a fence around an island.
If a piece of land touches another piece of land, you don't need a fence there.
You ONLY need a fence if the land touches the Water, OR if it touches the edge 
of the map!
So, you walk around the island. Every time you are standing on Land, you look in 
all 4 directions.
If you look Left and see Water: "+1 to the fence!"
If you look Right and see the edge of the map: "+1 to the fence!"
If you look Up and see Land, you say: "Oh, no fence needed here," but you still 
step onto that new land to keep exploring.

APPROACH:
---------
1. Initialize `ROWS, COLS`.
2. Define a recursive helper `dfs(r, c)` that RETURNS the length of the fence.
   - Base Case 1: Are we looking at Water (`0`) or the edge of the map (`r < 0`...)?
     If yes, this is a boundary! Return `1` (we need 1 piece of fence here).
   - Base Case 2: Have we ALREADY visited this Land? (`grid[r][c] == -1`)
     If yes, we already built the fence around it or explored it. Return `0`.
   - Mark this land as visited: `grid[r][c] = -1`. (Don't use `0` because that 
     would look like Water and confuse our fence counting!)
   - Check all 4 directions, and add up all the fence pieces they return.
   - `return dfs(Up) + dfs(Down) + dfs(Left) + dfs(Right)`
3. Scan the grid. Because there is exactly ONE island, the moment you find a `1`, 
   you just `return dfs(r, c)` and you are completely done!

COMPLEXITY:
-----------
Time:  O(M * N) — We scan the grid and visit each island cell a constant number of times.
Space: O(M * N) — The recursion stack depth.

EDGE CASES:
-----------
- Edge case 1: The island is just 1 square. Returns `4`.
- Edge case 2: The island fills the entire grid. Returns the perimeter of the grid rectangle: `2 * ROWS + 2 * COLS`.
============================================================
"""

from typing import List

def island_perimeter(grid: List[List[int]]) -> int:
    """
    Returns the perimeter of the single island in the grid.
    """
    if not grid:
        return 0

    ROWS = len(grid)
    COLS = len(grid[0])

    def dfs(r: int, c: int) -> int:
        # Base Case 1: Edge of the map OR Water. This is a perimeter boundary!
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
            return 1
        
        # Base Case 2: Already visited land. No perimeter here, and don't re-explore.
        if grid[r][c] == -1:
            return 0
        
        # Mark as visited (use -1 so we don't confuse it with Water)
        grid[r][c] = -1

        # Add up the perimeter boundaries from all 4 sides
        return (dfs(r - 1, c) + # Up
                dfs(r + 1, c) + # Down
                dfs(r, c - 1) + # Left
                dfs(r, c + 1))  # Right

    # Find the one and only island
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                return dfs(r, c)
                
    return 0

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    grid1 = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    # Perimeter should be 16
    assert island_perimeter(grid1) == 16, f"Test 1 failed: {island_perimeter(grid1)}"

    # 🔲 Edge cases
    grid2 = [[1]]
    assert island_perimeter(grid2) == 4, "Edge 1: Single cell"
    
    grid3 = [[1,0]]
    assert island_perimeter(grid3) == 4, "Edge 2: Two cells, one island"

    print("All tests passed!")
