"""
============================================================
Problem: Number Factors (Count Ways to Reach N)
Pattern: Fibonacci Numbers (DP)
Difficulty: Medium
Classic DP
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given N, find the number of ways to express N as a sum of 1, 3, or 4.
E.g. N=4: {1+1+1+1}, {1+3}, {3+1}, {4} → 4 ways.

APPROACH: DP
---------
dp[i] = number of ways to express i.
dp[0] = 1 (empty sum), dp[1] = 1, dp[2] = 1, dp[3] = 2.
For i >= 4: dp[i] = dp[i-1] + dp[i-3] + dp[i-4]

COMPLEXITY: O(N) time, O(N) space (or O(4) with rolling).
============================================================
"""


def count_ways(n: int) -> int:
    if n < 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] += dp[i - 1]
        if i >= 3:
            dp[i] += dp[i - 3]
        if i >= 4:
            dp[i] += dp[i - 4]
    return dp[n]


if __name__ == "__main__":
    assert count_ways(4) == 4,  "Test 1"
    assert count_ways(5) == 6,  "Test 2"
    assert count_ways(6) == 9,  "Test 3"
    assert count_ways(0) == 1,  "Edge: base case"
    assert count_ways(1) == 1,  "Edge: N=1"
    print("All tests passed!")
