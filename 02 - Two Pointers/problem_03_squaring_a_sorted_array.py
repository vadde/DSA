"""
============================================================
Problem: Squaring a Sorted Array
Pattern: Two Pointers (Opposite Ends)
Difficulty: Easy
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a list of numbers sorted from smallest to largest, but some of 
them are negative. When you square a negative number, it becomes positive (e.g., -5 
becomes 25). So, the biggest squares will come from either the largest positive numbers 
at the very right, OR the most negative numbers at the very left!
The smallest squares will be somewhere in the middle (near zero).
Since we want a sorted array of squares, we can start by looking at both ends (left 
and right). Whichever end gives a BIGGER square gets placed at the end of our new array, 
and we slowly work our way to the middle!

APPROACH:
---------
1. Initialize `left = 0` and `right = len(arr) - 1`.
2. Create a new array `squares` of the same length as `arr`, filled with zeros.
3. Initialize an index `highest_square_idx = len(arr) - 1` to place numbers from 
   the back to the front.
4. Loop while `left <= right`:
   a. Calculate `left_square = arr[left] * arr[left]` and `right_square = arr[right] * arr[right]`.
   b. If `left_square > right_square`:
      - Place `left_square` at `squares[highest_square_idx]`.
      - Increment `left`.
   c. Else:
      - Place `right_square` at `squares[highest_square_idx]`.
      - Decrement `right`.
   d. Decrement `highest_square_idx`.
5. Return the `squares` array.

COMPLEXITY:
-----------
Time:  O(N) — We only pass through the array once.
Space: O(N) — We create a new array to hold the squares.

EDGE CASES:
-----------
- Edge case 1: Array is entirely positive. (Right pointer moves inward).
- Edge case 2: Array is entirely negative. (Left pointer moves inward).
- Edge case 3: Array has a mix of negative and positive numbers.
============================================================
"""

def make_squares(arr: list[int]) -> list[int]:
    """
    Given a sorted array, returns a new array containing squares of all the 
    numbers of the input array in sorted order.
    """
    n: int = len(arr)
    squares: list[int] = [0] * n
    
    left: int = 0
    right: int = n - 1
    highest_square_idx: int = n - 1

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square > right_square:
            squares[highest_square_idx] = left_square
            left += 1
        else:
            squares[highest_square_idx] = right_square
            right -= 1
            
        highest_square_idx -= 1

    return squares

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert make_squares([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9], "Test 1 failed: mixed numbers"
    assert make_squares([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9], "Test 2 failed: mixed numbers"
    
    # 🔲 Edge cases
    assert make_squares([1, 2, 3]) == [1, 4, 9], "Edge 1: All positive"
    assert make_squares([-5, -4, -1]) == [1, 16, 25], "Edge 2: All negative"
    assert make_squares([0]) == [0], "Edge 3: Single element zero"

    print("All tests passed!")
