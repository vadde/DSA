"""
============================================================
Problem: Equal Subset Sum Partition
Pattern: 0/1 Knapsack (DP)
Difficulty: Medium
LeetCode: #416
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Can you split an array into TWO groups that have EQUAL sums?
E.g. [1,5,11,5] → [1,5,5] (sum 11) and [11] (sum 11). Yes!
Key insight: if total sum is S, we need a subset summing to exactly S//2.
If S is odd → impossible.

APPROACH: 0/1 Knapsack Boolean DP
---------
dp[w] = True if any subset sums to exactly w.
- dp[0] = True (empty subset sums to 0)
- For each number n, iterate w from target down to n:
  dp[w] = dp[w] OR dp[w - n]

COMPLEXITY:
-----------
Time:  O(N * S/2)
Space: O(S/2)
============================================================
"""

from typing import List


def can_partition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
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
    assert can_partition([1, 5, 11, 5]) is True,  "Test 1"
    assert can_partition([1, 2, 3, 5]) is False,  "Test 2"
    assert can_partition([1, 1]) is True,          "Test 3"
    assert can_partition([2]) is False,            "Edge: single element"
    assert can_partition([1, 3, 4, 2, 2]) is True, "Test 4"
    print("All tests passed!")
