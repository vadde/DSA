"""
============================================================
Problem: Minimum Subset Sum Difference
Pattern: 0/1 Knapsack (DP)
Difficulty: Hard
Classic / LeetCode #2035 variant
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Split an array into two groups (any split), and minimize the ABSOLUTE DIFFERENCE
of their sums. E.g. [1,2,3,9] → groups {1,2,3}=6 and {9}=9 → diff = 3.
Best possible split gives smallest |sum1 - sum2|.

APPROACH: 0/1 Knapsack + Find Closest to S/2
---------
1. Total sum = S. We want subset1 summing to as close to S//2 as possible.
2. Build DP: dp[w] = True if any subset sums to w (w from 0 to S).
3. After DP, find the LARGEST w <= S//2 where dp[w] is True.
4. Answer = S - 2*w (since subset2 sum = S - w, diff = (S-w) - w = S - 2w).

COMPLEXITY:
-----------
Time:  O(N * S)
Space: O(S)
============================================================
"""

from typing import List


def minimum_subset_sum_difference(nums: List[int]) -> int:
    total = sum(nums)
    dp = [False] * (total + 1)
    dp[0] = True

    for num in nums:
        for w in range(total, num - 1, -1):
            dp[w] = dp[w] or dp[w - num]

    # Find the largest sum <= total//2 that is achievable
    for w in range(total // 2, -1, -1):
        if dp[w]:
            return total - 2 * w

    return total  # edge case: shouldn't happen for non-empty nums


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert minimum_subset_sum_difference([1, 2, 3, 9]) == 3,       "Test 1"
    assert minimum_subset_sum_difference([1, 2, 7, 1, 5]) == 0,    "Test 2: perfect split"
    assert minimum_subset_sum_difference([1, 3, 100, 4]) == 92,     "Test 3"
    assert minimum_subset_sum_difference([1]) == 1,                 "Edge: single"
    assert minimum_subset_sum_difference([1, 1]) == 0,              "Edge: equal pair"
    print("All tests passed!")
