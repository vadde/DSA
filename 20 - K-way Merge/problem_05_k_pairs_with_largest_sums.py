"""
============================================================
Problem: K Pairs with Largest Sums
Pattern: K-way Merge
Difficulty: Hard
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1ce9a00cc465d6c827e5
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have two sorted (in descending order) lists of numbers.
You want to pick **k** pairs, each pair consisting of one number from the first list and one from the second list, such that the sums of those pairs are the **largest possible**.
Think of it like having two piles of gold coins. You need to pick k ways to take one coin from each pile, and you want the total gold in each chosen pair to be as big as possible.

APPROACH:
---------
Because both arrays are sorted (largest to smallest), the **biggest** sum is simply `nums1[0] + nums2[0]`.
After we take a pair, the next best candidates are either:
- Move one step forward in the first array while keeping the second index the same, or
- Move one step forward in the second array while keeping the first index the same.
We can treat each candidate as a node in a virtual grid and use a **Max‑Heap** to always pop the currently best sum.
We also keep a `visited` set of index pairs to avoid pushing the same cell twice.
The algorithm stops after we have extracted `k` pairs (or the heap empties).

COMPLEXITY:
-----------
Time: O(k log k) – each pop/push costs log k and we do at most k iterations.
Space: O(k) – the heap and visited set store at most k entries.

EDGE CASES:
-----------
- One of the arrays could be empty → return an empty list.
- k could be larger than total possible pairs → we simply return all possible pairs.
============================================================
"""

import heapq
from typing import List, Tuple, Set

def k_largest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[Tuple[int, int]]:
    """Return the k pairs (a, b) with the largest sums where a comes from nums1 and b from nums2.
    The result is a list of tuples ``(a, b)`` sorted in descending order of their sums.
    """
    if not nums1 or not nums2 or k <= 0:
        return []

    # Ensure both arrays are sorted in descending order for the logic to hold.
    nums1_sorted = sorted(nums1, reverse=True)
    nums2_sorted = sorted(nums2, reverse=True)

    max_heap: List[Tuple[int, int, int]] = []  # Store (-sum, i, j) for max-heap behavior using min-heap.
    visited: Set[Tuple[int, int]] = set()

    # Seed the heap with the best possible pair (0,0).
    initial_sum = nums1_sorted[0] + nums2_sorted[0]
    heapq.heappush(max_heap, (-initial_sum, 0, 0))
    visited.add((0, 0))

    result: List[Tuple[int, int]] = []
    while max_heap and len(result) < k:
        neg_sum, i, j = heapq.heappop(max_heap)
        result.append((nums1_sorted[i], nums2_sorted[j]))
        # Next candidate from moving forward in nums1.
        if i + 1 < len(nums1_sorted) and (i + 1, j) not in visited:
            next_sum = nums1_sorted[i + 1] + nums2_sorted[j]
            heapq.heappush(max_heap, (-next_sum, i + 1, j))
            visited.add((i + 1, j))
        # Next candidate from moving forward in nums2.
        if j + 1 < len(nums2_sorted) and (i, j + 1) not in visited:
            next_sum = nums1_sorted[i] + nums2_sorted[j + 1]
            heapq.heappush(max_heap, (-next_sum, i, j + 1))
            visited.add((i, j + 1))

    return result

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal case
    a = [9, 8, 2]
    b = [6, 3, 1]
    # Expected top 3 sums: (9,6)=15, (9,3)=12, (8,6)=14 => order by sum descending -> [(9,6), (8,6), (9,3)]
    res = k_largest_pairs(a, b, 3)
    expected = [(9, 6), (8, 6), (9, 3)]
    assert res == expected, f"Test 1 failed: got {res}"

    # 🔲 Edge cases
    assert k_largest_pairs([], [1, 2], 2) == []
    assert k_largest_pairs([1, 2], [], 2) == []
    # k larger than total pairs
    assert k_largest_pairs([1], [2], 5) == [(1, 2)]

    print("All tests passed!")
