"""
============================================================
Problem: Maximum Sum Subarray of Size K
Pattern: Sliding Window
Difficulty: Easy
Link: https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a train of numbered blocks. You hold up a frame that fits exactly K blocks.
You slide this frame block by block to the right. Every time you slide, you drop the
number that falls out of the left side of the frame and add the new number that
enters from the right. Your goal is to find the frame position that gives the highest total.

APPROACH:
---------
1. INITIALIZE variables: `window_start = 0`, `window_sum = 0`, `max_sum = -inf`.
2. EXPAND the window: iterate `window_end` from 0 to N-1, adding elements to `window_sum`.
3. CHECK SIZE: when `window_end >= K - 1`, the window is full (size K).
4. RECORD: update `max_sum` with the maximum of `max_sum` and `window_sum`.
5. SHRINK: subtract the element at `window_start` from `window_sum` and increment `window_start`.
6. RETURN the `max_sum`.

COMPLEXITY:
-----------
Time:  O(N) — Every element in the array is added to the window_sum exactly once (when `window_end` passes it) and subtracted at most once (when `window_start` passes it).
Space: O(1) — We only store a few variables (window boundaries and sum), regardless of the input size.

EDGE CASES:
-----------
- Edge case 1: The array length is less than K. Return -inf.
- Edge case 2: All elements are negative. The sliding window naturally handles this by taking the least negative sum because we initialized max_sum to -inf.
============================================================
"""

import math

def maximum_sum_subarray(arr: list[int], k: int) -> int | float:
    """
    Find the maximum sum of any contiguous subarray of size K.
    """
    # Edge case: if K is larger than the array length, no valid window can be formed
    if len(arr) < k:
        return -math.inf

    window_sum: int = 0
    max_sum: int | float = -math.inf
    window_start: int = 0

    for window_end in range(len(arr)):
        # EXPAND: Add the new element entering from the right
        window_sum += arr[window_end]

        # CHECK SIZE: Have we hit the required window size K?
        if window_end >= k - 1:
            # RECORD: The window is full, so see if we have a new max
            max_sum = max(max_sum, window_sum)

            # SHRINK: Remove the left element as we slide the window forward
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert maximum_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9, "Test 1 failed: [5, 1, 3] sum is 9"
    assert maximum_sum_subarray([2, 3, 4, 1, 5], 2) == 7, "Test 2 failed: [3, 4] sum is 7"

    # 🔲 Edge cases
    assert maximum_sum_subarray([], 3) == -math.inf, "Edge 1: empty array should return -inf"
    assert maximum_sum_subarray([1, 2], 3) == -math.inf, "Edge 2: array smaller than K should return -inf"
    assert maximum_sum_subarray([5], 1) == 5, "Edge 3: single element, K=1"
    
    # 🔲 All negative elements
    assert maximum_sum_subarray([-2, -1, -5, -1, -3, -2], 3) == -6, "Edge 4: All negatives. Max is [-1, -3, -2] = -6"
    
    print("All tests passed!")
