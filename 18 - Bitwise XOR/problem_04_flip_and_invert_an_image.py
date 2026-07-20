"""
============================================================
Problem: Flip and Invert an Image
Pattern: Bitwise XOR
Difficulty: Hard (More like Easy/Medium)
Link: https://leetcode.com/problems/flipping-an-image/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a grid of numbers that are either `0` or `1`. (Like a black-and-white image).
For example, one row is `[1, 1, 0]`.
You need to do two things to it:
1. FLIP IT: Reverse the row. `[1, 1, 0]` becomes `[0, 1, 1]`.
2. INVERT IT: Change all 0s to 1s, and 1s to 0s. `[0, 1, 1]` becomes `[1, 0, 0]`.
We can do both of these steps at the EXACT SAME TIME using two pointers and XOR!
We put a pointer `left` at the start, and `right` at the end.
We want to swap the numbers they point to, but AS we swap them, we flip them!
To flip a bit, we just XOR it with `1`.
`0 ^ 1 = 1`
`1 ^ 1 = 0`
So we just do: `row[left], row[right] = row[right] ^ 1, row[left] ^ 1`.
Then we move `left` inward and `right` inward until they cross!
Notice: If the row has an odd number of elements (like 3), `left` and `right` 
will eventually point to the EXACT SAME middle element. That's fine! 
The math still works perfectly. It swaps it with itself, and inverts it!

APPROACH:
---------
1. Loop through every `row` in the matrix.
2. Initialize `left = 0` and `right = len(row) - 1`.
3. Loop while `left <= right`:
   - `row[left], row[right] = row[right] ^ 1, row[left] ^ 1`
   - `left += 1`
   - `right -= 1`
4. Return the matrix!

COMPLEXITY:
-----------
Time:  O(N) — Where N is the total number of elements in the matrix. We touch 
       every element exactly once.
Space: O(1) — We mutate the matrix in-place!

EDGE CASES:
-----------
- Edge case 1: The row only has 1 element. `left` and `right` are both 0. It 
  inverts it and we're done.
============================================================
"""

from typing import List

def flip_and_invert_image(matrix: List[List[int]]) -> List[List[int]]:
    """
    Flips a binary matrix horizontally, then inverts it.
    """
    for row in matrix:
        left = 0
        right = len(row) - 1
        
        # We must use <= so that the middle element gets inverted
        # when the length of the row is odd.
        while left <= right:
            # We simultaneously swap the elements AND invert them using XOR 1!
            row[left], row[right] = row[right] ^ 1, row[left] ^ 1
            left += 1
            right -= 1
            
    return matrix

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    matrix1 = [[1,1,0], [1,0,1], [0,0,0]]
    expected1 = [[1,0,0], [0,1,0], [1,1,1]]
    assert flip_and_invert_image(matrix1) == expected1, "Test 1"

    matrix2 = [[1,1,0,0], [1,0,0,1], [0,1,1,1], [1,0,1,0]]
    expected2 = [[1,1,0,0], [0,1,1,0], [0,0,0,1], [1,0,1,0]]
    assert flip_and_invert_image(matrix2) == expected2, "Test 2"

    # 🔲 Edge cases
    assert flip_and_invert_image([[1]]) == [[0]], "Edge 1: Single element"
    assert flip_and_invert_image([[0, 0]]) == [[1, 1]], "Edge 2: Row of 2 elements"

    print("All tests passed!")
