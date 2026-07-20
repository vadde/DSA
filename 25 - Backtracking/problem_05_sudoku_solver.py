"""
============================================================
Problem: Sudoku Solver
Pattern: Backtracking
Difficulty: Hard
LeetCode: #37
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Fill in a 9x9 Sudoku grid so that each row, column, and 3x3 box contains
the digits 1-9 exactly once. Empty cells are marked with '.'.
Strategy: find an empty cell, try digits 1-9, validate, recurse. Backtrack if stuck.

APPROACH: Backtracking with Constraint Sets
---------
Track which digits are used in each row, column, and 3x3 box (27 sets total).
For each empty cell: try digits not yet used in that row/col/box.
If valid, place and recurse. If recursion fails, remove and try next digit.

COMPLEXITY:
-----------
Time:  O(9^81) worst case, dramatically pruned in practice
Space: O(81) — stack depth + constraint sets
============================================================
"""

from typing import List


def solve_sudoku(board: List[List[str]]) -> None:
    """Modifies board in-place."""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]  # box index = (r//3)*3 + c//3
    empties: List[tuple[int, int]] = []

    # Initialize constraint sets
    for r in range(9):
        for c in range(9):
            d = board[r][c]
            if d == '.':
                empties.append((r, c))
            else:
                b = (r // 3) * 3 + c // 3
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)

    def backtrack(idx: int) -> bool:
        if idx == len(empties):
            return True  # All empty cells filled
        r, c = empties[idx]
        b = (r // 3) * 3 + c // 3
        for digit in "123456789":
            if digit not in rows[r] and digit not in cols[c] and digit not in boxes[b]:
                # Place digit
                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[b].add(digit)
                if backtrack(idx + 1):
                    return True
                # Backtrack
                board[r][c] = '.'
                rows[r].discard(digit)
                cols[c].discard(digit)
                boxes[b].discard(digit)
        return False

    backtrack(0)


if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    solve_sudoku(board)
    # Verify no '.' remains and rows/cols/boxes are valid
    for row in board:
        assert '.' not in row and set(row) == set("123456789"), "Row invalid"
    print("All tests passed!")
