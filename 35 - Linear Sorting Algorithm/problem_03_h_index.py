"""
============================================================
Problem: H-Index
Pattern: Counting Sort (Linear Sorting)
Difficulty: Medium
LeetCode: #274
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A researcher has an h-index of `h` if they have published at least `h` papers
that have each been cited at least `h` times.
We want to find the MAXIMUM possible `h`.

APPROACH: Counting Sort / Bucket Sort
---------
1. An h-index cannot be larger than the total number of papers `N`.
2. We create an array `counts` of size `N + 1`.
3. If a paper has > N citations, we just add it to `counts[N]` (because any
   citations beyond N don't help increase the max possible h-index past N).
4. Otherwise, we add it to `counts[citations]`.
5. We iterate backward from N to 0, keeping a running total of papers we've seen.
   Once our running total >= the current index `h`, that index is our h-index!

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)
============================================================
"""

from typing import List


def hIndex(citations: List[int]) -> int:
    n = len(citations)
    counts = [0] * (n + 1)
    
    for c in citations:
        if c >= n:
            counts[n] += 1
        else:
            counts[c] += 1
            
    papers_with_at_least_h_citations = 0
    for h in range(n, -1, -1):
        papers_with_at_least_h_citations += counts[h]
        if papers_with_at_least_h_citations >= h:
            return h
            
    return 0


if __name__ == "__main__":
    assert hIndex([3,0,6,1,5]) == 3, "Test 1"
    assert hIndex([1,3,1]) == 1,     "Test 2"
    assert hIndex([100, 100]) == 2,  "Test 3"
    print("All tests passed!")
