"""
============================================================
Problem: Factor Combinations
Pattern: Backtracking
Difficulty: Medium
LeetCode: #254
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given N, return all possible ways to express N as a product of integers >= 2.
E.g. N=12 → [[2,2,3],[2,6],[3,4]]
N itself (as a product of 1 and N) is NOT included.

APPROACH: Backtracking
---------
Try each factor f from 2 to sqrt(n).
If n % f == 0: include f, recurse on n//f.
Also include [n] at each recursive call (using the remaining n as the last factor).

COMPLEXITY: O(N log N) — pruning keeps it manageable.
============================================================
"""

from typing import List


def get_factors(n: int) -> List[List[int]]:
    result: List[List[int]] = []

    def backtrack(remaining: int, start: int, current: List[int]) -> None:
        # If we have at least one factor chosen, record current + remaining
        if current:
            result.append(current + [remaining])
        # Try more factors
        f = start
        while f * f <= remaining:
            if remaining % f == 0:
                current.append(f)
                backtrack(remaining // f, f, current)
                current.pop()
            f += 1

    backtrack(n, 2, [])
    return result


if __name__ == "__main__":
    res1 = get_factors(12)
    expected1 = [[2, 2, 3], [2, 6], [3, 4]]
    assert sorted(map(sorted, res1)) == sorted(map(sorted, expected1)), "Test 1"

    res2 = get_factors(1)
    assert res2 == [], "Edge: 1 has no factor combinations"

    res3 = get_factors(37)
    assert res3 == [], "Edge: prime → no combinations"

    print("All tests passed!")
