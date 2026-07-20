"""
============================================================
Problem: Shortest Subarray with Sum at Least K
Pattern: Sliding Window (Advanced: Prefix Sum + Monotonic Deque)
Difficulty: Hard
Link: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a game board where moving forward usually gets you points, but some spaces 
actually LOSE you points (negative numbers). You want to find the shortest path that 
scores at least K points.
The standard sliding window breaks here because adding a new space might lower your 
score, and removing a space might raise it! It's completely unpredictable.
To fix this, we write down our "total score from the start" at every step (Prefix Sum).
Then we use a smart queue to remember the lowest scores we've seen recently, so we 
always know the best place to measure from.

APPROACH (Prefix Sum + Monotonic Deque):
----------------------------------------
1. Calculate a `prefix_sum` array. `prefix_sum[i]` is the sum of all elements before `i`.
   This turns the subarray sum problem into a simple subtraction: 
   `Sum(i to j) = prefix_sum[j] - prefix_sum[i]`.
2. Initialize a deque `dq` to store INDICES of the prefix sum array.
3. Iterate `i` through the `prefix_sum` array:
   a. SHRINK (Check Valid Window): While the deque is not empty and the current prefix 
      sum minus the prefix sum at the front of the deque is `>= k`:
      - We found a valid subarray! `min_length = min(min_length, i - dq[0])`.
      - We can `popleft()` because we want the SHORTEST subarray. Any future `i` 
        will only make the subarray longer, so this starting point `dq[0]` is now useless.
   b. MAINTAIN DEQUE (Optimize Starting Points): While the deque is not empty and the 
      current prefix sum is `<=` the prefix sum at the back of the deque:
      - We `pop()` from the back. Why? Because the current `i` provides a LOWER (or equal) 
        prefix sum AND it is a CLOSER starting point for any future `j`. The older, higher 
        prefix sum is completely outclassed.
   c. Add the current index `i` to the deque.
4. Return `min_length`.

COMPLEXITY:
-----------
Time:  O(N) — We iterate through the array to build prefix sums. Every index is pushed to and popped from the deque at most once.
Space: O(N) — For the prefix sum array and the deque.

EDGE CASES:
-----------
- Edge case 1: No subarray reaches sum K. Return -1.
- Edge case 2: The very first element is >= K. Returns 1.
============================================================
"""

from collections import deque
import math

def shortest_subarray(nums: list[int], k: int) -> int:
    """
    Find the length of the shortest non-empty subarray with a sum of at least K.
    """
    # Create prefix sum array of size N+1
    # prefix_sum[i] stores the sum of nums[0...i-1]
    n: int = len(nums)
    prefix_sum: list[int] = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    dq: deque[int] = deque()
    min_length: int | float = math.inf

    for i in range(n + 1):
        # 1. Check if we found a valid subarray from a previous starting point
        while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
            min_length = min(min_length, i - dq[0])
            # Pop left because we want the shortest. Any future `i` paired with dq[0] will be longer.
            dq.popleft()

        # 2. Maintain monotonic increasing property of the deque
        # If the current prefix sum is smaller than previous ones, it's a better starting point!
        # It's both closer (larger index) and smaller (easier to reach target K).
        while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
            dq.pop()

        # 3. Add current index to deque
        dq.append(i)

    return min_length if min_length != math.inf else -1


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert shortest_subarray([1], 1) == 1, "Test 1 failed: single element"
    assert shortest_subarray([1, 2], 4) == -1, "Test 2 failed: impossible"
    assert shortest_subarray([2, -1, 2], 3) == 3, "Test 3 failed: with negative numbers"
    
    # 🔲 Edge cases
    assert shortest_subarray([84, -37, 32, 40, 95], 167) == 3, "Edge 1: [32, 40, 95] = 167"
    assert shortest_subarray([-28, 81, -20, 28, -29], 89) == 3, "Edge 2: [81, -20, 28] = 89"
    assert shortest_subarray([], 1) == -1, "Edge 3: empty array"

    print("All tests passed!")
