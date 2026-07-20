"""
============================================================
Problem: Game of Life
Pattern: Simulation (In-Place State Machine)
Difficulty:
Link: https://leetcode.com/problem-placeholder/ Medium
LeetCode: #289
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Conway's Game of Life. A grid of cells. 1 is alive, 0 is dead.
Rules for next generation:
1. Live cell with < 2 neighbors dies (underpopulation)
2. Live cell with 2 or 3 neighbors lives
3. Live cell with > 3 neighbors dies (overpopulation)
4. Dead cell with exactly 3 neighbors becomes alive (reproduction)
You must update ALL cells SIMULTANEOUSLY without using extra space!

APPROACH: State Machine with Bit Manipulation / Arbitrary Values
---------
Since we can't use an extra grid, we need a way to store BOTH the "old" state
and the "new" state in the same cell.
- 0: Was Dead, stays Dead
- 1: Was Alive, stays Alive
- 2: Was Dead, becomes Alive
- 3: Was Alive, becomes Dead

To check the OLD state of a cell, we just check if it was 1 or 3!
At the very end, we make a second pass to update 2s to 1s, and 3s to 0s.

COMPLEXITY:
-----------
Time:  O(R * C)
Space: O(1)

EDGE CASES:
-----------
- Basic empty/null edge cases.
- Boundary constraints.
============================================================
"""

from typing import List


def game_of_life(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    rows, cols = len(board), len(board[0])
    
    # All 8 neighbors
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    # Pass 1: Apply rules and encode new states
    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Old state was alive if it's 1 or 3
                    if board[nr][nc] == 1 or board[nr][nc] == 3:
                        live_neighbors += 1
                        
            if board[r][c] == 1:
                # Rule 1 or 3
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = 3 # Alive -> Dead
            else:
                # Rule 4
                if live_neighbors == 3:
                    board[r][c] = 2 # Dead -> Alive
                    
    # Pass 2: Finalize states
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 2:
                board[r][c] = 1
            elif board[r][c] == 3:
                board[r][c] = 0


if __name__ == "__main__":
    board = [
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ]
    game_of_life(board)
    expected = [
      [0,0,0],
      [1,0,1],
      [0,1,1],
      [0,1,0]
    ]
    assert board == expected, "Test 1"
    print("All tests passed!")
