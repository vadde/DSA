"""
============================================================
Problem: Design Tic-Tac-Toe
Pattern: Simulation (State Optimization)
Difficulty: Medium
LeetCode: #348
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Design a Tic-Tac-Toe game on an N x N board.
When a player makes a move, you need to check if they won.
Checking the entire row, column, and diagonals takes O(N).
Can we do it in O(1) time?

APPROACH: Row/Col Accumulation
---------
Instead of a grid, keep track of the "score" for every row, column, and the two diagonals.
Player 1 adds +1. Player 2 adds -1.
If any row, column, or diagonal reaches exactly +N, Player 1 wins!
If any reaches exactly -N, Player 2 wins!

COMPLEXITY:
-----------
Time:  O(1) per move.
Space: O(N) to store row and col arrays.
============================================================
"""


class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        val = 1 if player == 1 else -1
        
        # Update row and col
        self.rows[row] += val
        self.cols[col] += val
        
        # Update diagonals
        if row == col:
            self.diag += val
        # Anti-diagonal condition: row + col == n - 1
        if row + col == self.n - 1:
            self.anti_diag += val
            
        # Check if this move won the game
        target = self.n if player == 1 else -self.n
        if (self.rows[row] == target or
            self.cols[col] == target or
            self.diag == target or
            self.anti_diag == target):
            return player
            
        return 0


if __name__ == "__main__":
    game = TicTacToe(3)
    assert game.move(0, 0, 1) == 0
    assert game.move(0, 2, 2) == 0
    assert game.move(2, 2, 1) == 0
    assert game.move(1, 1, 2) == 0
    assert game.move(2, 0, 1) == 0
    assert game.move(1, 0, 2) == 0
    assert game.move(2, 1, 1) == 1, "Test 1: Player 1 wins on bottom row!"
    print("All tests passed!")
