"""
============================================================
Problem: 0/1 Knapsack
Pattern: 0/1 Knapsack (DP)
Difficulty: Medium
Classic Problem
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Backpack holds W pounds max. You have N items each with weight[i] and value[i].
Pick items (each at most ONCE) to maximize total value without exceeding W.

APPROACH: 1D DP (Space-Optimized)
---------
dp[w] = max value achievable with capacity exactly w.
Iterate items outer, capacity REVERSED inner (prevents double-counting).

COMPLEXITY:
-----------
Time:  O(N * W)
Space: O(W) — 1D array
============================================================
"""

from typing import List


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        # Reverse to avoid using item i more than once
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # weights=[2,3,1,4], values=[4,5,3,7], capacity=5 → take items 0,2 or 2,3 → max 10
    assert knapsack_01([2, 3, 1, 4], [4, 5, 3, 7], 5) == 10, "Test 1"
    assert knapsack_01([1, 2, 3], [1, 6, 10], 5) == 16,       "Test 2: items 1+2 → 16"
    assert knapsack_01([], [], 10) == 0,                       "Edge: no items"
    assert knapsack_01([5], [10], 4) == 0,                     "Edge: item too heavy"
    assert knapsack_01([1], [100], 1) == 100,                  "Edge: exact fit"
    print("All tests passed!")
