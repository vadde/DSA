"""
============================================================
Problem: Max Area of Island
Pattern: Island (Matrix Traversal)
Difficulty: Medium
Link: https://leetcode.com/problems/max-area-of-island/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
We are back in our helicopter, but this time we don't just care about HOW MANY 
islands there are, we want to find the BIGGEST island.
When we drop our Paint Bucket of Water on an island, we want to measure exactly 
how much Land we painted over before it sank.
To do this, every time the paint touches a square of Land, that square shouts "1!"
Then, it asks its neighbors (Up, Down, Left, Right) to shout their numbers, 
and it adds them all together.
So if I touch a piece of Land, and its left neighbor is size 2, and its right 
neighbor is size 1, my total size is `1 (me) + 2 (left) + 1 (right) = 4`.
We keep track of the biggest size we've seen so far as we scan the grid.

APPROACH:
---------
1. Initialize `max_area = 0`.
2. Define a recursive helper `dfs(r, c)` that RETURNS an integer (the area).
   - Base Case: Out of bounds, OR the cell is Water (`0`). Return `0` (Area is 0).
   - Sink it: Mark `grid[r][c] = 0` so we don't double count it!
   - Recursively calculate the area of the 4 neighbors.
   - `return 1 + dfs(Up) + dfs(Down) + dfs(Left) + dfs(Right)`
3. Scan the grid from top-left to bottom-right.
4. If `grid[r][c] == 1`, we found a new island!
   - `current_area = dfs(r, c)`
   - `max_area = max(max_area, current_area)`
5. Return `max_area`.

COMPLEXITY:
-----------
Time:  O(M * N) — Every cell is visited at most a constant number of times.
Space: O(M * N) — The recursion stack could reach M*N if the whole grid is one giant snake-shaped island.

EDGE CASES:
-----------
- Edge case 1: Entire grid is Water. Returns `0`.
- Edge case 2: Grid has negative numbers or non-binary? The problem specifies binary `1` and `0` integers.
============================================================
"""

from typing import List

def max_area_of_island(grid: List[List[int]]) -> int:
    """
    Returns the maximum area of an island in a binary grid.
    """
    if not grid:
        return 0

    ROWS = len(grid)
    COLS = len(grid[0])
    max_area = 0

    def get_island_area(r: int, c: int) -> int:
        # Base case: Out of bounds OR it is Water
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
            return 0
        
        # SINK IT! Mark as visited to avoid infinite loops
        grid[r][c] = 0

        # Ask my neighbors how big they are, and add 1 for myself
        return (1 + 
                get_island_area(r - 1, c) + # Up
                get_island_area(r + 1, c) + # Down
                get_island_area(r, c - 1) + # Left
                get_island_area(r, c + 1))  # Right

    # Scan the entire grid
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                # Calculate this island's area and see if it's the new record!
                current_area = get_island_area(r, c)
                max_area = max(max_area, current_area)

    return max_area

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    grid1 = [
        [0,0,1,0,0],
        [0,0,1,1,1],
        [0,1,0,0,0],
        [0,1,1,0,0]
    ]
    # Island 1 (top right) = 4
    # Island 2 (bottom left) = 3
    # Max = 4
    assert max_area_of_island(grid1) == 4, "Test 1 failed"

    grid2 = [
        [1,1,1],
        [1,0,0],
        [1,1,1]
    ]
    # Snake shaped island of size 7
    assert max_area_of_island(grid2) == 7, "Test 2 failed"

    # 🔲 Edge cases
    assert max_area_of_island([[0,0],[0,0]]) == 0, "Edge 1: All water"
    assert max_area_of_island([]) == 0, "Edge 2: Empty grid"

    print("All tests passed!")
