"""
============================================================
Problem: Minimum Number of Coins for Fruits
Pattern: Monotonic Queue (DP + Sliding Window Minimum)
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-number-of-coins-for-fruits/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You're at a fruit shop with fruits numbered 1 to N. If you BUY fruit i
(paying prices[i-1] coins), you get the next `i` fruits FOR FREE!
You must acquire all N fruits. Minimize total coins spent.

KEY INSIGHT: This is a DP problem. Let dp[i] = minimum cost to acquire
fruits 1..i where fruit i is the last fruit you BOUGHT.
If you buy fruit i, you get fruits i+1 to i+i for free.
So dp[j] (for j in range i+1 to min(i+i, n)) can be directly achieved.
We want the minimum dp[j] over a sliding range → Monotonic Queue!

APPROACH:
---------
1. dp[i] = prices[i-1] + min(dp[j]) for j in the "free range" after buying i.
2. Process from right to left.
3. Use a monotonic deque to efficiently get the minimum dp in the window.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)

EDGE CASES:
-----------
- Single fruit → must buy it.
- Two fruits → buy fruit 1, get fruit 2 free.
============================================================
"""

from typing import List
from collections import deque


def minimum_coins(prices: List[int]) -> int:
    n = len(prices)
    # dp[i] = min cost to acquire ALL fruits from index i..n (1-indexed).
    # If we buy fruit i (cost = prices[i-1]), we get fruits i+1..2*i for free.
    # Then we must handle fruit 2*i+1 onward, BUT we can also choose to buy
    # any free fruit j in [i+1, 2*i] to extend coverage further.
    # So dp[i] = prices[i-1] + min(dp[j]) for j in [i+1, 2*i+1].
    # dp[j] = 0 for j > n (nothing left to acquire).

    dp = [0] * (n + 2)  # dp[n+1] = 0

    # Monotonic increasing deque (front = index with min dp value)
    dq = deque()
    # Seed with dp[n+1] = 0
    dq.append(n + 1)

    for i in range(n, 0, -1):
        # Window for dp[i] is [i+1, 2*i+1], clamped to n+1
        window_right = min(2 * i + 1, n + 1)

        # Remove elements from front that are out of window (< i+1 shouldn't happen
        # since we go right to left, but > window_right can)
        while dq and dq[0] > window_right:
            dq.popleft()

        # dp[i] = prices[i-1] + min dp in window
        if dq:
            dp[i] = prices[i - 1] + dp[dq[0]]
        else:
            dp[i] = prices[i - 1]

        # Add dp[i] to deque for future windows (maintaining increasing order)
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
        dq.append(i)

    return dp[1]


if __name__ == "__main__":
    assert minimum_coins([3,1,2]) == 4, "Test 1"
    assert minimum_coins([1,10,1,1]) == 2, "Test 2"
    assert minimum_coins([5]) == 5, "Test 3: single"
    assert minimum_coins([1,1]) == 1, "Test 4: buy 1, get 2 free"
    print("All tests passed!")
