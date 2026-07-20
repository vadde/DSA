"""
============================================================
Problem: Range Sum Query 2D - Immutable
Pattern: 2D Prefix Sum
Difficulty: Medium
LeetCode: #304
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a 2D grid of numbers. You need to quickly answer:
"What is the sum of the numbers in a specific rectangle from (r1, c1) to (r2, c2)?"
You can't loop through the rectangle every time—it's too slow.

APPROACH: 2D Prefix Sum (Inclusion-Exclusion Principle)
---------
1. Build a 2D `prefix[r][c]` which stores the sum of all elements in the
   rectangle from (0,0) to (r-1,c-1).
2. `prefix[r][c] = matrix[r-1][c-1] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]`
3. To query sum from (r1,c1) to (r2,c2):
   `Sum = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]`
   (We add back the top-left area because it was subtracted twice).

COMPLEXITY:
-----------
Time:  O(R*C) to build, O(1) per query
Space: O(R*C)
============================================================
"""

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            self.prefix = []
            return
            
        rows, cols = len(matrix), len(matrix[0])
        # Pad with 1 row and 1 column of zeros to handle edges cleanly
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c] 
                    + self.prefix[r][c + 1] 
                    + self.prefix[r + 1][c] 
                    - self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1] 
            - self.prefix[row1][col2 + 1] 
            - self.prefix[row2 + 1][col1] 
            + self.prefix[row1][col1]
        )


if __name__ == "__main__":
    matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    nm = NumMatrix(matrix)
    assert nm.sumRegion(2, 1, 4, 3) == 8,  "Test 1"
    assert nm.sumRegion(1, 1, 2, 2) == 11, "Test 2"
    assert nm.sumRegion(1, 2, 2, 4) == 12, "Test 3"
    print("All tests passed!")
