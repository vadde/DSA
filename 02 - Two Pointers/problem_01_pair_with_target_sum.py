"""
============================================================
Problem: Pair with Target Sum
Pattern: Two Pointers (Opposite Ends)
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a sorted list of numbered blocks, and you need to find exactly two 
blocks that add up to a specific target number. Because the blocks are sorted from 
smallest to largest, you don't need to try every single combination. You can start 
by pointing at the smallest block (left) and the largest block (right). If they add up 
to too much, you need a smaller block, so you move the right pointer left. If they don't 
add up to enough, you need a bigger block, so you move the left pointer right.

APPROACH:
---------
1. Initialize two pointers: `left` at the beginning (index 0) and `right` at the end (len - 1).
2. Loop while `left < right` (Opposite Ends collision condition):
   a. Calculate the `current_sum` of `arr[left]` + `arr[right]`.
   b. If `current_sum == target`, return the values (or indices).
   c. If `current_sum < target`, we need a larger sum, so we increment `left`.
   d. If `current_sum > target`, we need a smaller sum, so we decrement `right`.
3. If the loop finishes and no pair is found, return `[-1, -1]`.

COMPLEXITY:
-----------
Time:  O(N) — Each element is visited at most once as pointers move inwards.
Space: O(1) — We only store two integer pointers.

EDGE CASES:
-----------
- Edge case 1: No valid pair exists in the array. Return `[-1, -1]`.
- Edge case 2: Array contains negative numbers. The logic perfectly holds because the array is sorted.
============================================================
"""

def search_pair(arr: list[int], target_sum: int) -> list[int]:
    """
    Returns the indices of the two numbers that add up to the target_sum.
    (Assuming 0-indexed for generic DSA, LC Two Sum II is 1-indexed)
    """
    left: int = 0
    right: int = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            return [left, right]
        elif current_sum < target_sum:
            left += 1  # Need a larger sum
        else:
            right -= 1 # Need a smaller sum

    return [-1, -1]

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert search_pair([1, 2, 3, 4, 6], 6) == [1, 3], "Test 1 failed"
    assert search_pair([2, 5, 9, 11], 11) == [0, 2], "Test 2 failed"
    
    # 🔲 Edge cases
    assert search_pair([-3, -1, 0, 2, 5], -1) == [0, 3], "Edge 1: Contains negative numbers"
    assert search_pair([1, 2, 3], 100) == [-1, -1], "Edge 2: No valid pair"
    assert search_pair([5, 5], 10) == [0, 1], "Edge 3: Pair composed of identical numbers"

    print("All tests passed!")
