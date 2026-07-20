"""
============================================================
Problem: Sum of Absolute Differences in a Sorted Array
Pattern: Prefix Sum
Difficulty: Medium
Link: https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a sorted row of numbers. For each number, compute the sum of
absolute differences between it and EVERY other number. Return this as an
array. Brute force is O(N^2). We need O(N) using prefix sums!

KEY INSIGHT: Because the array is SORTED, for any index `i`:
- All elements to the LEFT are <= nums[i]. Their total difference is:
  `i * nums[i] - left_sum` (since nums[i] - x is positive for all x <= nums[i]).
- All elements to the RIGHT are >= nums[i]. Their total difference is:
  `right_sum - (n - i - 1) * nums[i]`.
- Total = left_contribution + right_contribution.

APPROACH:
---------
1. Compute `total_sum`.
2. Maintain `left_sum` as we iterate left to right.
3. For each index `i`:
   - `right_sum = total_sum - left_sum - nums[i]`
   - `left_diff = i * nums[i] - left_sum`
   - `right_diff = right_sum - (n - i - 1) * nums[i]`
   - `result[i] = left_diff + right_diff`
   - `left_sum += nums[i]`

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N) for the result.

EDGE CASES:
-----------
- Single element → [0].
- All elements equal → all zeros.
============================================================
"""

from typing import List


def get_sum_absolute_differences(nums: List[int]) -> List[int]:
    n = len(nums)
    total_sum = sum(nums)
    left_sum = 0
    result = []

    for i in range(n):
        right_sum = total_sum - left_sum - nums[i]
        left_diff = i * nums[i] - left_sum
        right_diff = right_sum - (n - i - 1) * nums[i]
        result.append(left_diff + right_diff)
        left_sum += nums[i]

    return result


if __name__ == "__main__":
    assert get_sum_absolute_differences([2,3,5]) == [4,3,5], "Test 1"
    assert get_sum_absolute_differences([1,4,6,8,10]) == [24,15,13,15,21], "Test 2"
    assert get_sum_absolute_differences([5]) == [0], "Test 3: single"
    assert get_sum_absolute_differences([3,3,3]) == [0,0,0], "Test 4: all equal"
    print("All tests passed!")
