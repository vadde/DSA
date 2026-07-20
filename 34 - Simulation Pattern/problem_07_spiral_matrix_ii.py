"""
============================================================
Problem: Spiral Matrix II
Pattern: Simulation
Difficulty: Medium
Link: https://leetcode.com/problems/spiral-matrix-ii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are given a number `n`. You need to create an `n x n` grid and fill it
with numbers from 1 to `n^2` in a spiral order (starting from top-left, going
right, down, left, up, right...).

APPROACH:
---------
1. Create an `n x n` matrix filled with 0s.
2. Define 4 boundaries: top, bottom, left, right.
3. Keep track of the current number to insert (1 to n^2).
4. Simulate walking the spiral, adjusting boundaries inward after completing
   each row or column.

COMPLEXITY:
-----------
Time:  O(N^2)
Space: O(1) (excluding the output matrix)

EDGE CASES:
-----------
- n = 1 -> single element [[1]].
============================================================
"""

from typing import List

def generateMatrix(n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # Traverse from right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            
        # Traverse from bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
    return matrix

if __name__ == "__main__":
    assert generateMatrix(1) == [[1]], "Test 1"
    assert generateMatrix(3) == [[1,2,3],[8,9,4],[7,6,5]], "Test 2"
    print("All tests passed!")
