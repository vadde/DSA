"""
============================================================
Problem: Left and Right Sum Differences
Pattern: Prefix Sum
Difficulty: Easy
Link: https://leetcode.com/problems/left-and-right-sum-differences/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
For each block in a row, compute how different the sum of blocks on its LEFT
is from the sum of blocks on its RIGHT. Return the absolute difference for
each position as an array.

APPROACH:
---------
1. Compute `total_sum`.
2. Walk left to right, maintaining `left_sum`.
3. At each position `i`:
   - `right_sum = total_sum - left_sum - nums[i]`
   - `result[i] = abs(left_sum - right_sum)`
   - `left_sum += nums[i]`

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N) for the result array (O(1) auxiliary).

EDGE CASES:
-----------
- Single element → left and right are both 0, answer is [0].
- All same elements.
============================================================
"""

from typing import List


def left_right_difference(nums: List[int]) -> List[int]:
    total = sum(nums)
    left_sum = 0
    result = []

    for num in nums:
        right_sum = total - left_sum - num
        result.append(abs(left_sum - right_sum))
        left_sum += num

    return result


if __name__ == "__main__":
    assert left_right_difference([10,4,8,3]) == [15,1,11,22], "Test 1"
    assert left_right_difference([1]) == [0], "Test 2: single"
    assert left_right_difference([1,1,1]) == [2,0,2], "Test 3: uniform"
    print("All tests passed!")
