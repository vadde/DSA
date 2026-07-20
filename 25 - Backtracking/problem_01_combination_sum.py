"""
============================================================
Problem: Combination Sum
Pattern: Backtracking
Difficulty: Medium
LeetCode: #39
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given a list of candidate numbers and a target, find all UNIQUE combinations
where chosen numbers sum to target. You can use the SAME number multiple times.
E.g. candidates=[2,3,6,7], target=7 → [[2,2,3],[7]]

APPROACH: Backtracking
---------
At each step: try each candidate starting from current index (to avoid duplicates).
If adding candidate exceeds target → prune (stop trying larger candidates).
If sum == target → record the combination.
Backtrack by removing the last chosen element.

COMPLEXITY:
-----------
Time:  O(N^(T/M)) where T=target, M=min candidate
Space: O(T/M) recursion depth
============================================================
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result: List[List[int]] = []
    candidates.sort()  # Sorting enables early pruning

    def backtrack(start: int, current: List[int], remaining: int) -> None:
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                break  # Sorted → all further candidates also too large
            current.append(c)
            backtrack(i, current, remaining - c)  # i, not i+1: can reuse
            current.pop()

    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    res1 = combination_sum([2, 3, 6, 7], 7)
    assert sorted(res1) == sorted([[2, 2, 3], [7]]), "Test 1"

    res2 = combination_sum([2, 3, 5], 8)
    assert sorted(res2) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]]), "Test 2"

    assert combination_sum([2], 1) == [],  "Edge: no combination"
    assert combination_sum([1], 1) == [[1]], "Edge: single exact"
    print("All tests passed!")
