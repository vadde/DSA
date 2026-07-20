"""
============================================================
Problem: Word Search
Pattern: Backtracking
Difficulty: Medium
LeetCode: #79
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a grid of letters. Can you find a given word by moving to adjacent
cells (up, down, left, right) without revisiting the same cell?

APPROACH: DFS Backtracking
---------
For each cell, try to start the word from it.
At each step: if current cell matches current letter → continue DFS in 4 directions.
Mark visited by temporarily replacing cell with '#', restore on backtrack.

COMPLEXITY:
-----------
Time:  O(N * M * 4^L) where L = word length
Space: O(L) recursion depth
============================================================
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, idx: int) -> bool:
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
        # Mark as visited
        temp = board[r][c]
        board[r][c] = '#'
        found = (
            dfs(r + 1, c, idx + 1) or
            dfs(r - 1, c, idx + 1) or
            dfs(r, c + 1, idx + 1) or
            dfs(r, c - 1, idx + 1)
        )
        # Restore (backtrack)
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


if __name__ == "__main__":
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board1, "ABCCED") is True,  "Test 1"
    assert exist(board1, "SEE") is True,     "Test 2"
    assert exist(board1, "ABCB") is False,   "Test 3: can't revisit"
    assert exist([["a"]], "a") is True,      "Edge: single cell"
    assert exist([["a"]], "b") is False,     "Edge: not found"
    print("All tests passed!")
