"""
============================================================
Problem: Sort Colors
Pattern: Linear Sorting (Counting Sort / Dutch National Flag)
Difficulty: Medium
LeetCode: #75
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an array with 0s (Red), 1s (White), and 2s (Blue).
Sort them in-place so all 0s are first, then 1s, then 2s.
You must do this in O(N) time without using the built-in sort function.

APPROACH: Counting Sort (Two-Pass)
---------
(Note: Dutch National Flag one-pass uses pointers. Since this is the
Linear Sorting pattern, we'll demonstrate Counting Sort).
1. Pass 1: Count how many 0s, 1s, and 2s we have.
2. Pass 2: Overwrite the original array with the right number of 0s, 1s, and 2s!

COMPLEXITY:
-----------
Time:  O(N) (Two passes)
Space: O(1) (Only 3 variables for counting)
============================================================
"""

from typing import List


def sort_colors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Step 1: Count frequencies
    count = [0, 0, 0]
    for num in nums:
        count[num] += 1
        
    # Step 2: Overwrite array
    idx = 0
    for color in range(3):
        for _ in range(count[color]):
            nums[idx] = color
            idx += 1


if __name__ == "__main__":
    arr1 = [2,0,2,1,1,0]
    sort_colors(arr1)
    assert arr1 == [0,0,1,1,2,2], "Test 1"
    
    arr2 = [2,0,1]
    sort_colors(arr2)
    assert arr2 == [0,1,2], "Test 2"
    print("All tests passed!")
