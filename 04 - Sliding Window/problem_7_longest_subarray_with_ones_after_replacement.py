"""
============================================================
Problem: Longest Subarray with Ones after Replacement
Pattern: Sliding Window
Difficulty: Hard
Link: https://leetcode.com/problems/max-consecutive-ones-iii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a row of light switches. Some are turned ON (1) and some are OFF (0).
You want to find the longest stretch of lights that are all ON. You have a magic wand
that can flip at most K switches from OFF to ON. To find the longest stretch, you slide
a frame over the switches. As long as your frame contains K or fewer OFF switches,
it's a valid stretch (because you could use your magic wand on all of them). If you get
too many OFF switches, you must slide the left side of your frame to drop some OFF switches.

APPROACH (Dynamic Window):
--------------------------
1. INITIALIZE variables: `window_start = 0`, `max_length = 0`, and `zeros_count = 0`.
2. EXPAND the window: iterate `window_end` from 0 to len(arr)-1.
3. If `arr[window_end]` is 0, increment `zeros_count`.
4. SHRINK LOOP: while `zeros_count > k` (we have more than K zeros in our window):
   a. If `arr[window_start]` is 0, decrement `zeros_count`.
   b. Increment `window_start`.
5. RECORD: The window is now valid (zeros_count <= k). `max_length = max(max_length, window_end - window_start + 1)`.
6. RETURN `max_length`.

COMPLEXITY:
-----------
Time:  O(N) — We iterate through the array once. Both pointers move from left to right.
Space: O(1) — We only store a few variables for counting and boundaries.

EDGE CASES:
-----------
- Edge case 1: K is 0. We can't replace any zeros, so we just find the longest stretch of existing 1s.
- Edge case 2: K is greater than or equal to the total number of 0s in the array. The answer is the entire array length.
============================================================
"""

def longest_ones(arr: list[int], k: int) -> int:
    """
    Find the length of the longest contiguous subarray of 1s after replacing at most K 0s.
    """
    window_start: int = 0
    max_length: int = 0
    zeros_count: int = 0

    for window_end in range(len(arr)):
        # EXPAND: Process the new element
        if arr[window_end] == 0:
            zeros_count += 1

        # SHRINK: If we have more zeros than allowed replacements, we must shrink
        while zeros_count > k:
            if arr[window_start] == 0:
                zeros_count -= 1
            window_start += 1

        # RECORD: We now have a valid window
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert longest_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) == 6, "Test 1 failed: [0, 1, 1, 0, 1, 1] at the end"
    assert longest_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) == 9, "Test 2 failed: [1, 1, 0, 1, 1, 0, 0, 1, 1]"

    # 🔲 Edge cases
    assert longest_ones([1, 1, 1], 0) == 3, "Edge 1: k=0, all ones"
    assert longest_ones([0, 0, 0], 0) == 0, "Edge 2: k=0, all zeros"
    assert longest_ones([0, 0, 0], 5) == 3, "Edge 3: K is larger than total zeros"
    assert longest_ones([], 2) == 0, "Edge 4: empty array"

    print("All tests passed!")
