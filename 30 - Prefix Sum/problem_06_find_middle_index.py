"""
============================================================
Problem: Find the Middle Index in Array
Pattern: Prefix Sum
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-middle-index-in-array/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a row of numbered blocks. Find a block (the "middle index") where
the sum of ALL blocks to its LEFT equals the sum of ALL blocks to its RIGHT.
The middle block itself is NOT counted in either sum.

APPROACH:
---------
1. Compute `total_sum` of the array.
2. Iterate with a running `left_sum`.
3. At each index `i`, `right_sum = total_sum - left_sum - nums[i]`.
4. If `left_sum == right_sum`, return `i`!
5. Otherwise, add `nums[i]` to `left_sum` and continue.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(1)

EDGE CASES:
-----------
- Middle index at position 0 (left_sum = 0 == right_sum).
- Middle index at last position.
- No valid middle index → return -1.
============================================================
"""

from typing import List


def find_middle_index(nums: List[int]) -> int:
    total = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        right_sum = total - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num

    return -1


if __name__ == "__main__":
    assert find_middle_index([2,3,-1,8,4]) == 3, "Test 1"
    assert find_middle_index([1,-1,4]) == 2, "Test 2"
    assert find_middle_index([2,5]) == -1, "Test 3"
    assert find_middle_index([1]) == 0, "Test 4: single element"
    print("All tests passed!")
