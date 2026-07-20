"""
============================================================
Problem: Number of Islands
Pattern: Island (Matrix Traversal)
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-islands/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are flying a helicopter over an ocean looking at a giant grid.
Some squares are Water ('0'), some are Land ('1').
If you see Land touching other Land (Up, Down, Left, or Right), they form 
a single Island.
Your job is to count exactly how many Islands there are.
How do you make sure you don't count the same big island 5 times?
When you spot a piece of Land, you say "I found an Island! +1". 
Then, you drop a massive Paint Bucket of Water on that square. 
The water magically spreads to all the connected Land squares, turning the 
ENTIRE island into Water ('0').
Now you can keep flying and scanning the grid. If you see a '1' again, you 
know for a fact it's a BRAND NEW island!

APPROACH:
---------
1. Initialize `islands = 0`. Get the `ROWS` and `COLS` of the grid.
2. Define a recursive `dfs(r, c)` function:
   - Base Case 1: Are we out of bounds? (`r < 0` or `r >= ROWS` etc.)
     If yes, just return. We fell off the map!
   - Base Case 2: Is this square Water? (`grid[r][c] == '0'`)
     If yes, just return. Nothing to do here.
   - SINK THE ISLAND: Change `grid[r][c] = '0'`.
   - Recursively call DFS in all 4 directions (Up, Down, Left, Right).
3. Scan the grid with nested loops (`for r in range(ROWS): for c in range(COLS):`)
4. If `grid[r][c] == '1'`, we found a new island!
   - `islands += 1`
   - Call `dfs(r, c)` to sink this entire island so we don't double count it.
5. Return `islands`.

COMPLEXITY:
-----------
Time:  O(M * N) — Where M is rows and N is columns. We visit every cell at most a constant number of times.
Space: O(M * N) — In the worst case (the entire grid is one giant island), the recursion stack goes M*N deep.

EDGE CASES:
-----------
- Edge case 1: Empty grid. Returns 0.
- Edge case 2: Grid with only '0's. Returns 0.
- Edge case 3: Grid with only '1's. Returns 1.
============================================================
"""

from typing import List

def num_islands(grid: List[List[str]]) -> int:
    """
    Returns the number of islands in a 2D binary grid.
    """
    if not grid:
        return 0

    ROWS = len(grid)
    COLS = len(grid[0])
    islands = 0

    def sink_island(r: int, c: int):
        # 1. Base cases: Out of bounds OR it's water
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0':
            return
        
        # 2. Sink it! (Mark as visited by mutating the grid)
        grid[r][c] = '0'

        # 3. Spread the water to all 4 neighbors
        sink_island(r - 1, c) # Up
        sink_island(r + 1, c) # Down
        sink_island(r, c - 1) # Left
        sink_island(r, c + 1) # Right

    # 4. Scan the grid from top-left to bottom-right
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1':
                # We found a piece of unvisited land! It's a new island.
                islands += 1
                # Sink it and all connected land
                sink_island(r, c)

    return islands

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    # We must pass a copy or recreate it if we run multiple tests, since it mutates.
    assert num_islands(grid1) == 1, "Test 1 failed"

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert num_islands(grid2) == 3, "Test 2 failed"

    # 🔲 Edge cases
    assert num_islands([]) == 0, "Edge 1: Empty grid"
    assert num_islands([["0", "0"], ["0", "0"]]) == 0, "Edge 2: All water"
    assert num_islands([["1", "1"], ["1", "1"]]) == 1, "Edge 3: All land"

    print("All tests passed!")
