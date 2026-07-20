"""
============================================================
Problem: Removing Minimum and Maximum From Array
Pattern: Greedy Algorithms
Difficulty: Medium
LeetCode: #2091
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an array. Find the minimum and maximum values. Remove both of them.
BUT: you can only remove elements from the FRONT or BACK of the array (not the
middle). Find the minimum number of moves to eliminate BOTH the min and max.

Think of it like a conveyor belt — you can only remove items from either end.
You need to grab two specific items (min and max). What's the fastest way?

APPROACH: Greedy — 3 Strategies
---------
Let min_idx and max_idx be the positions of the minimum and maximum.
(Swap them if min_idx > max_idx so min_idx <= max_idx always).

Three ways to remove both:
1. Take both from the LEFT: moves = max_idx + 1
2. Take both from the RIGHT: moves = n - min_idx
3. Take min from LEFT and max from RIGHT: moves = (min_idx + 1) + (n - max_idx)

Return the minimum of these three strategies.

COMPLEXITY:
-----------
Time:  O(N) — to find min and max indices
Space: O(1)

EDGE CASES:
-----------
- Array of size 1: min and max are same → 1 move
- Array of size 2: always 2 moves
- min and max at same position: impossible (all elements identical, 1 move)
============================================================
"""

from typing import List


def minimum_deletions(nums: List[int]) -> int:
    n = len(nums)
    min_idx = nums.index(min(nums))
    max_idx = nums.index(max(nums))

    # Normalize so min_idx <= max_idx
    lo, hi = min(min_idx, max_idx), max(min_idx, max_idx)

    # Strategy 1: take both from left  → need hi+1 moves
    from_left = hi + 1
    # Strategy 2: take both from right → need n - lo moves
    from_right = n - lo
    # Strategy 3: take lo from left, hi from right
    split = (lo + 1) + (n - hi)

    return min(from_left, from_right, split)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert minimum_deletions([2, 10, 7, 5, 4, 1, 8, 6]) == 5, "Test 1"
    assert minimum_deletions([0, -4, 19, 1, 8, -2, -3, 5]) == 3, "Test 2"
    assert minimum_deletions([101]) == 1,                        "Edge: single"
    assert minimum_deletions([1, 2]) == 2,                       "Edge: two elements"
    assert minimum_deletions([3, 1]) == 2,                       "Edge: two reversed"
    print("All tests passed!")
