"""
============================================================
Problem: Spiral Matrix
Pattern: Simulation
Difficulty:
Link: https://leetcode.com/problem-placeholder/ Medium
LeetCode: #54
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a grid of numbers. Start at the top-left and walk around the outside
edge in a clockwise circle. When you finish the outer layer, step inward and do
it again! Collect all the numbers in the order you walk over them.

APPROACH: Boundary Shrinking Simulation
---------
Maintain 4 boundaries: `top`, `bottom`, `left`, `right`.
1. Walk from left to right along the `top` row. Then `top += 1` (peel it off).
2. Walk from top to bottom along the `right` col. Then `right -= 1`.
3. Walk from right to left along the `bottom` row. Then `bottom -= 1`.
4. Walk from bottom to top along the `left` col. Then `left += 1`.
Repeat until boundaries cross!

COMPLEXITY:
-----------
Time:  O(R * C) — Visit each cell once.
Space: O(1) — (excluding output array).

EDGE CASES:
-----------
- Basic empty/null edge cases.
- Boundary constraints.
============================================================
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
        
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse Top Row (left to right)
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        
        # Traverse Right Col (top to bottom)
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        
        if top <= bottom:
            # Traverse Bottom Row (right to left)
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1
            
        if left <= right:
            # Traverse Left Col (bottom to top)
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
            
    return result


if __name__ == "__main__":
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert spiral_order(matrix1) == [1,2,3,6,9,8,7,4,5], "Test 1"
    
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    assert spiral_order(matrix2) == [1,2,3,4,8,12,11,10,9,5,6,7], "Test 2"
    
    assert spiral_order([[1]]) == [1], "Test 3"
    print("All tests passed!")
