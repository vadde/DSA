"""
============================================================
Problem: Minimum Jumps with Fee
Pattern: Fibonacci Numbers (DP)
Difficulty: Medium
Classic DP
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a staircase of N steps. Each step has a fee[i] cost.
You can take 1, 2, or 3 steps at a time.
Find the minimum fee to reach the TOP (step N, beyond the last step).

APPROACH: 1D DP
---------
dp[i] = minimum cost to reach step i.
dp[0] = 0 (ground floor, free).
For each step i from 1 to N:
  dp[i] = fee[i-1] + min(dp[i-1], dp[i-2] if i>=2 else inf, dp[i-3] if i>=3 else inf)
Answer = dp[N] (step N = beyond all steps).

COMPLEXITY: O(N) time, O(1) rolling space.
============================================================
"""

from typing import List
import math


def min_cost_climbing_stairs(fee: List[int]) -> int:
    n = len(fee)
    # dp[i] = min cost to reach step i (step 0 = ground floor, free start)
    # step n = destination (beyond all fee steps)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        take1 = dp[i - 1] + fee[i - 1]
        take2 = dp[i - 2] + fee[i - 2] if i >= 2 else float('inf')
        take3 = dp[i - 3] + fee[i - 3] if i >= 3 else float('inf')
        dp[i] = min(take1, take2, take3)
    return dp[n]


if __name__ == "__main__":
    assert min_cost_climbing_stairs([1, 2, 5, 2, 1, 2]) == 3, "Test 1"
    assert min_cost_climbing_stairs([2, 3, 4, 5]) == 5,        "Test 2"
    assert min_cost_climbing_stairs([0]) == 0,                  "Edge: single free"
    print("All tests passed!")
