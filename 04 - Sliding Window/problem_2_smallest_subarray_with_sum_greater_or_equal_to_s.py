"""
============================================================
Problem: Smallest Subarray with Sum ≥ S
Pattern: Sliding Window
Difficulty: Easy
Link: https://leetcode.com/problems/minimum-size-subarray-sum/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a row of treasure chests, each with some gold coins. You need to collect at
least S coins. You want to carry as few chests as possible to hit that target, but
you can only pick up chests that are sitting right next to each other in a line.
You stretch a rope around chests until you have enough coins, and then see if you
can tighten the rope from the left side and still have enough.

APPROACH (Dynamic-Size Window):
-------------------------------
1. INITIALIZE variables: `window_start = 0`, `window_sum = 0`, `min_length = inf`.
2. EXPAND the window: iterate `window_end` from 0 to N-1, adding elements to `window_sum`.
3. SHRINK LOOP: while `window_sum >= S`:
   a. RECORD the minimum length: `min_length = min(min_length, window_end - window_start + 1)`.
   b. SHRINK from the left: subtract `arr[window_start]` from `window_sum` and increment `window_start`.
4. RETURN `min_length` (or 0 if no valid window was found).

COMPLEXITY:
-----------
Time:  O(N) — Each element is added to the window_sum once and removed at most once. The while loop only processes each element once overall.
Space: O(1) — We only use a few tracking variables.

EDGE CASES:
-----------
- Edge case 1: No subarray sums to S. Return 0.
- Edge case 2: The very first element is ≥ S. Should return 1.
============================================================
"""

import math

def smallest_subarray_with_given_sum(target: int, arr: list[int]) -> int:
    """
    Find the length of the smallest contiguous subarray whose sum is greater than or equal to `target`.
    """
    window_sum: int = 0
    min_length: int | float = math.inf
    window_start: int = 0

    for window_end in range(len(arr)):
        # EXPAND: Add the new element entering from the right
        window_sum += arr[window_end]

        # SHRINK: Keep shrinking from the left as long as the condition holds
        while window_sum >= target:
            # RECORD: Update the min_length since the condition is met inside this loop
            min_length = min(min_length, window_end - window_start + 1)

            # Shrink the window
            window_sum -= arr[window_start]
            window_start += 1

    return min_length if min_length != math.inf else 0


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]) == 2, "Test 1 failed: [5, 2] length is 2"
    assert smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]) == 1, "Test 2 failed: [8] length is 1"
    assert smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]) == 3, "Test 3 failed: [3, 4, 1] or [1, 1, 6]"

    # 🔲 Edge cases
    assert smallest_subarray_with_given_sum(100, [1, 2, 3]) == 0, "Edge 1: No subarray sum is >= 100, should return 0"
    assert smallest_subarray_with_given_sum(4, [1, 4, 4]) == 1, "Edge 2: Single element >= target"
    assert smallest_subarray_with_given_sum(7, []) == 0, "Edge 3: Empty array"

    print("All tests passed!")
