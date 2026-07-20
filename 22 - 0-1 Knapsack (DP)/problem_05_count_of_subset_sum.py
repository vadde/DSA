"""
============================================================
Problem: Count of Subset Sum
Pattern: 0/1 Knapsack (DP)
Difficulty: Hard
Classic / LeetCode #494 variant
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array and a target, count how many DISTINCT subsets sum to exactly target.
E.g. [1,1,2,3], target=4 → subsets: {1,3},{1,3},{2,1,1} → 3 ways.

APPROACH: 0/1 Knapsack Counting DP
---------
dp[w] = number of subsets that sum to w.
dp[0] = 1 (one way to sum to 0: empty subset)
For each num, iterate w REVERSED:
  dp[w] += dp[w - num]

COMPLEXITY:
-----------
Time:  O(N * T)
Space: O(T)
============================================================
"""

from typing import List


def count_subset_sum(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for w in range(target, num - 1, -1):
            dp[w] += dp[w - num]

    return dp[target]


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert count_subset_sum([1, 1, 2, 3], 4) == 3, "Test 1"
    assert count_subset_sum([1, 2, 7, 1, 5], 9) == 3, "Test 2"
    assert count_subset_sum([1], 1) == 1,           "Edge: single match"
    assert count_subset_sum([1], 2) == 0,           "Edge: no match"
    assert count_subset_sum([], 0) == 1,            "Edge: empty → 1 way (empty subset)"
    print("All tests passed!")
