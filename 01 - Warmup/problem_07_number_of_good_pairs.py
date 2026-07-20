"""
============================================================
Problem: Number of Good Pairs
Pattern: Warmup
Difficulty: Easy
LeetCode: #1512
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A "good pair" is two indices (i, j) where i < j AND nums[i] == nums[j].
So we need to count how many pairs of matching numbers exist in the array.
Key insight: if a number appears k times, it forms k*(k-1)//2 good pairs.
  (Like choosing 2 from k: combinations formula C(k, 2))

APPROACH: Counter Math
---------
1. Count the frequency of each number using Counter.
2. For each number with frequency k, add k*(k-1)//2 to the result.
3. Return total.

Alternative approach (if you don't remember the formula):
  - For each number, track how many times we've seen it so far.
  - Every time we see a number again, it forms (count_so_far) new pairs.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N) — Counter dictionary

EDGE CASES:
-----------
- All unique elements → 0 pairs
- All same elements → n*(n-1)//2 pairs
- Single element → 0 pairs
============================================================
"""

from typing import List
from collections import Counter


def num_identical_pairs(nums: List[int]) -> int:
    count = 0
    freq = Counter(nums)
    for k in freq.values():
        count += k * (k - 1) // 2
    return count


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert num_identical_pairs([1, 2, 3, 1, 1, 3]) == 4,  "Test 1: (0,3),(0,4),(3,4),(2,5)"
    assert num_identical_pairs([1, 1, 1, 1]) == 6,         "Test 2: C(4,2)=6"
    assert num_identical_pairs([1, 2, 3]) == 0,            "Test 3: no duplicates"
    assert num_identical_pairs([1]) == 0,                  "Edge: single"
    assert num_identical_pairs([]) == 0,                   "Edge: empty"
    print("All tests passed!")
