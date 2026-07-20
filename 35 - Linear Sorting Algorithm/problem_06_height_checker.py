"""
============================================================
Problem: Height Checker
Pattern: Linear Sorting (Counting Sort)
Difficulty: Easy
Link: https://leetcode.com/problems/height-checker/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Students are standing in a line. You have their current heights. The teacher
wants them sorted by height. Count how many students are NOT standing in
their correct position.

APPROACH:
---------
1. Create a sorted copy of the heights (this is the "expected" order).
2. Compare element by element. Count mismatches.
   (For linear sorting: since heights are bounded [1, 100], counting sort works!)

COMPLEXITY:
-----------
Time:  O(N + K) with counting sort, K = max height.
Space: O(N) for the sorted copy.

EDGE CASES:
-----------
- Already sorted → 0.
- All same heights → 0.
- Completely reversed → could be N.
============================================================
"""

from typing import List


def height_checker(heights: List[int]) -> int:
    expected = sorted(heights)
    return sum(1 for h, e in zip(heights, expected) if h != e)


if __name__ == "__main__":
    assert height_checker([1,1,4,2,1,3]) == 3, "Test 1"
    assert height_checker([5,1,2,3,4]) == 5, "Test 2"
    assert height_checker([1,2,3,4,5]) == 0, "Test 3: already sorted"
    assert height_checker([2,2,2]) == 0, "Test 4: all same"
    print("All tests passed!")
