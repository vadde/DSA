"""
============================================================
Problem: Longest Continuous Subarray With Absolute Diff <= Limit
Pattern: Ordered Set / Sliding Window + SortedList
Difficulty: Medium
Link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Find the longest contiguous chunk of numbers where the difference between the
BIGGEST and SMALLEST number in the chunk is at most `limit`. This is a sliding
window problem, but you need an efficient way to know the current window's
min and max.

APPROACH (Ordered Set / SortedList):
---------
1. Use a sliding window with `left` and `right` pointers.
2. Maintain a SortedList (or two monotonic deques) for efficient min/max.
3. Expand the window by adding `nums[right]`.
4. While `max - min > limit`, shrink from the left.
5. Track the maximum window length.

NOTE: Since sortedcontainers may not be available in all environments,
we use the Two-Deque approach (monotonic deques for max and min), which
is more interview-friendly anyway.

COMPLEXITY:
-----------
Time:  O(N) — each element added/removed from deques at most once.
Space: O(N) for the deques.

EDGE CASES:
-----------
- All elements equal → entire array.
- limit = 0 → longest run of same value.
- Single element → 1.
============================================================
"""

from typing import List
from collections import deque


def longest_subarray(nums: List[int], limit: int) -> int:
    max_deque = deque()  # Decreasing: front is max of window
    min_deque = deque()  # Increasing: front is min of window
    left = 0
    result = 0

    for right in range(len(nums)):
        # Maintain max_deque (decreasing)
        while max_deque and nums[max_deque[-1]] <= nums[right]:
            max_deque.pop()
        max_deque.append(right)

        # Maintain min_deque (increasing)
        while min_deque and nums[min_deque[-1]] >= nums[right]:
            min_deque.pop()
        min_deque.append(right)

        # Shrink window if constraint violated
        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            left += 1
            if max_deque[0] < left:
                max_deque.popleft()
            if min_deque[0] < left:
                min_deque.popleft()

        result = max(result, right - left + 1)

    return result


if __name__ == "__main__":
    assert longest_subarray([8,2,4,7], 4) == 2, "Test 1"
    assert longest_subarray([10,1,2,4,7,2], 5) == 4, "Test 2"
    assert longest_subarray([4,2,2,2,4,4,2,2], 0) == 3, "Test 3: limit=0"
    assert longest_subarray([1], 10) == 1, "Test 4: single"
    print("All tests passed!")
