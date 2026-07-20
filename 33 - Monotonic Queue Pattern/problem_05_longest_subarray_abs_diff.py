"""
============================================================
Problem: Longest Continuous Subarray With Absolute Diff <= Limit
Pattern: Monotonic Queue (Sliding Window + Two Deques)
Difficulty: Medium
Link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Same problem as Ordered Set #7, but here we emphasize that the MONOTONIC
QUEUE approach (two deques tracking running min and max) is the canonical
technique for this pattern. The Monotonic Queue is the hero data structure.

APPROACH:
---------
1. Max-Deque (Decreasing): Front always holds the index of the max in the window.
2. Min-Deque (Increasing): Front always holds the index of the min in the window.
3. Sliding window: expand right, shrink left when max - min > limit.
4. Track maximum window size.

COMPLEXITY:
-----------
Time:  O(N) — amortized O(1) per element for deque operations.
Space: O(N) for the two deques.

EDGE CASES:
-----------
- limit = 0 → longest run of identical values.
- All elements the same → whole array.
============================================================
"""

from typing import List
from collections import deque


def longest_subarray(nums: List[int], limit: int) -> int:
    max_dq = deque()  # Indices, decreasing values
    min_dq = deque()  # Indices, increasing values
    left = 0
    result = 0

    for right in range(len(nums)):
        while max_dq and nums[max_dq[-1]] <= nums[right]:
            max_dq.pop()
        max_dq.append(right)

        while min_dq and nums[min_dq[-1]] >= nums[right]:
            min_dq.pop()
        min_dq.append(right)

        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()

        result = max(result, right - left + 1)

    return result


if __name__ == "__main__":
    assert longest_subarray([8,2,4,7], 4) == 2, "Test 1"
    assert longest_subarray([10,1,2,4,7,2], 5) == 4, "Test 2"
    assert longest_subarray([4,2,2,2,4,4,2,2], 0) == 3, "Test 3"
    print("All tests passed!")
