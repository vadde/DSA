"""
============================================================
Problem: Staircase (Climbing Stairs)
Pattern: Fibonacci Numbers (DP)
Difficulty: Easy
LeetCode: #70
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Climbing n stairs, taking 1 or 2 steps at a time. How many distinct ways?
ways[n] = ways[n-1] + ways[n-2] — exactly the Fibonacci recurrence.

COMPLEXITY:
-----------
Time: O(N), Space: O(1)
============================================================
"""


def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89
    print("All tests passed!")
