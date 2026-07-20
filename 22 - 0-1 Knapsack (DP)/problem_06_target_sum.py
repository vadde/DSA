"""
============================================================
Problem: Target Sum
Pattern: 0/1 Knapsack (DP)
Difficulty: Hard
LeetCode: #494
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array, assign a '+' or '-' sign to each number. How many ways can
you make the total equal to `target`?
E.g. [1,1,1,1,1], target=3 → 5 ways (choose which two to negate).

APPROACH: 0/1 Knapsack Reduction
---------
Let P = set of numbers with '+', N = set with '-'.
P + N = total  (sum of all absolute values)
P - N = target
Adding: 2P = total + target  →  P = (total + target) / 2

So the problem reduces to: count subsets summing to (total + target) / 2.
If (total + target) is odd or total < |target| → 0 ways.

COMPLEXITY:
-----------
Time:  O(N * P) where P = (total + target) / 2
Space: O(P)
============================================================
"""

from typing import List


def find_target_sum_ways(nums: List[int], target: int) -> int:
    total = sum(nums)
    # Edge cases
    if (total + target) % 2 != 0 or abs(target) > total:
        return 0

    subset_target = (total + target) // 2
    dp = [0] * (subset_target + 1)
    dp[0] = 1

    for num in nums:
        for w in range(subset_target, num - 1, -1):
            dp[w] += dp[w - num]

    return dp[subset_target]


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert find_target_sum_ways([1, 1, 1, 1, 1], 3) == 5,  "Test 1"
    assert find_target_sum_ways([1], 1) == 1,               "Test 2"
    assert find_target_sum_ways([1], 2) == 0,               "Test 3: impossible"
    assert find_target_sum_ways([1, 0], 1) == 2,            "Test 4: zero element"
    assert find_target_sum_ways([1, 2, 3, 1], 3) == 2,      "Test 5"
    print("All tests passed!")
