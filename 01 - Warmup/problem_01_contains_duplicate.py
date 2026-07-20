"""
============================================================
Problem: Contains Duplicate
Pattern: Warmup
Difficulty: Easy
LeetCode: #217
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bag of colored balls. Is there ANY color that appears more than once?
Just dump them all out, and as you pick each one up, check if you've seen that
color before. If yes — DUPLICATE FOUND! If you empty the bag without a match,
there are no duplicates.

APPROACH: Hash Set
---------
Use a set to track seen numbers. On each element:
  - If it's already in the set → return True (duplicate found).
  - Otherwise, add it to the set.
Return False if we exhaust the array.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N) — set stores up to N elements

EDGE CASES:
-----------
- Empty array → False (no elements means no duplicates)
- Single element → False
============================================================
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    seen: set[int] = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True,   "Test 1"
    assert contains_duplicate([1, 2, 3, 4]) is False,  "Test 2"
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True, "Test 3"
    assert contains_duplicate([]) is False,             "Edge: empty"
    assert contains_duplicate([99]) is False,           "Edge: single"
    print("All tests passed!")
