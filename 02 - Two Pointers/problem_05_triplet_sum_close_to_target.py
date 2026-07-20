"""
============================================================
Problem: Triplet Sum Close to Target
Pattern: Two Pointers (Opposite Ends)
Difficulty: Medium
Link: https://leetcode.com/problems/3sum-closest/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you are trying to guess the number of jellybeans in a jar (the target).
You get to pick exactly three smaller jars of jellybeans to pour together. 
If you can't hit the exact number, you want to get as close as possible.
And if two different sets of jars get you equally close (e.g., 98 and 102 for a 
target of 100), you always prefer the smaller number (98).
By sorting our jars and using the Two Pointers trick, we can keep track of our 
"best guess so far" and adjust our pointers based on whether we need more or fewer 
jellybeans.

APPROACH:
---------
1. Sort the input array.
2. Initialize `smallest_difference = infinity`. This will store `target - current_sum`.
3. Loop through the array, using `i` as the pinned element.
   a. If `i > 0` and `arr[i] == arr[i-1]`, skip to avoid duplicate work.
   b. Set `left = i + 1` and `right = len(arr) - 1`.
4. While `left < right`:
   a. Calculate `target_diff = target_sum - arr[i] - arr[left] - arr[right]`.
   b. If `target_diff == 0`, we found an exact match! Return `target_sum`.
   c. We need to update `smallest_difference` if:
      - The absolute difference is smaller (`abs(target_diff) < abs(smallest_difference)`).
      - OR the absolute difference is the same, but the current sum is smaller. A smaller 
        sum means a LARGER `target_diff` (since `target_diff = target - sum`). 
        So if `abs(target_diff) == abs(smallest_difference)` and `target_diff > smallest_difference`, we update.
   d. If `target_diff > 0`, our sum is too small. We need a larger sum to get closer: `left += 1`.
   e. If `target_diff < 0`, our sum is too large. We need a smaller sum: `right -= 1`.
5. Return `target_sum - smallest_difference`.

COMPLEXITY:
-----------
Time:  O(N log N + N^2) = O(N^2) — Sorting takes O(N log N), and we iterate with Two Pointers taking O(N^2).
Space: O(1) or O(N) — Depending on the sorting algorithm.

EDGE CASES:
-----------
- Edge case 1: Multiple triplets have the same difference, must return the one with the smaller sum.
- Edge case 2: Exact match is found early, algorithm short-circuits.
============================================================
"""

import math

def triplet_sum_close_to_target(arr: list[int], target_sum: int) -> int:
    """
    Finds a triplet whose sum is as close to the target as possible.
    If multiple have the same distance, returns the smaller sum.
    """
    arr.sort()
    smallest_difference: int | float = math.inf
    n: int = len(arr)

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left: int = i + 1
        right: int = n - 1

        while left < right:
            # We track the DIFFERENCE rather than just the absolute distance.
            # target_diff = target - sum. 
            target_diff: int = target_sum - arr[i] - arr[left] - arr[right]

            if target_diff == 0:
                return target_sum

            # Update condition:
            # 1. We found a closer difference.
            # 2. Or, we found a tie in absolute difference, but the new sum is SMALLER.
            # A smaller sum means a LARGER target_diff.
            if abs(target_diff) < abs(smallest_difference) or \
               (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                smallest_difference = target_diff

            if target_diff > 0:
                left += 1 # We need a larger sum
            else:
                right -= 1 # We need a smaller sum

    # The sum is target_sum - target_diff
    return target_sum - int(smallest_difference)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert triplet_sum_close_to_target([-2, 0, 1, 2], 2) == 1, "Test 1 failed: [-2, 1, 2] = 1"
    assert triplet_sum_close_to_target([-3, -1, 1, 2], 1) == 0, "Test 2 failed: [-3, 1, 2] = 0"
    assert triplet_sum_close_to_target([1, 0, 1, 1], 100) == 3, "Test 3 failed: [1, 1, 1] = 3"
    
    # 🔲 Edge cases
    # Distance of 10 from target 100: sum = 90 (target_diff = 10) vs sum = 110 (target_diff = -10).
    # Expected is the smaller sum: 90.
    assert triplet_sum_close_to_target([90, 110, 0, 0], 100) == 90, "Edge 1: Tie breaker test"
    assert triplet_sum_close_to_target([0, 0, 0], 1) == 0, "Edge 2: All zeros"

    print("All tests passed!")
