"""
============================================================
Problem: Subset Sum
Pattern: 0/1 Knapsack (DP)
Difficulty: Medium
Classic Problem
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array of positive integers and a target S, does ANY subset sum to S?
This is exactly the "Equal Subset" problem generalized to an arbitrary target.

APPROACH: 0/1 Knapsack Boolean DP
---------
Same as Equal Subset: dp[w] = can we reach sum w?

COMPLEXITY:
-----------
Time:  O(N * S)
Space: O(S)
============================================================
"""

from typing import List


def subset_sum(nums: List[int], target: int) -> bool:
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for w in range(target, num - 1, -1):
            dp[w] = dp[w] or dp[w - num]

    return dp[target]


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert subset_sum([1, 2, 3, 7], 6) is True,  "Test 1: 1+2+3=6"
    assert subset_sum([1, 2, 7, 1, 5], 10) is True, "Test 2: 1+2+7=10"
    assert subset_sum([1, 3, 4, 8], 6) is False, "Test 3"
    assert subset_sum([], 0) is True,             "Edge: empty, target 0"
    assert subset_sum([], 1) is False,            "Edge: empty, target 1"
    assert subset_sum([5], 5) is True,            "Edge: exact single"
    print("All tests passed!")
