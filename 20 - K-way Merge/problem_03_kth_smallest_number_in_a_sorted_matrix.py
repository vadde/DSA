"""
============================================================
Problem: Kth Smallest Number in a Sorted Matrix
Pattern: K-way Merge
Difficulty: Hard
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1ce5a00cc465d6c827cd
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a square grid of numbers where **every row** is sorted from left to right **and** **every column** is sorted from top to bottom.
Think of it like a bookshelf where each shelf (row) is organized, and each column of the shelves is also organized.
You want to find the *k*th smallest number in the whole grid **without** flattening the whole bookshelf into one big list.

APPROACH:
---------
1. Put the **top‑left** element (row 0, col 0) into a **Min‑Heap**.
2. Repeatedly pop the smallest element from the heap – that gives us the next smallest number in the matrix.
3. After popping a cell `(r, c)`, push its **right neighbour** `(r, c+1)` **and** its **bottom neighbour** `(r+1, c)` **if they exist**.
   - To avoid pushing the same cell twice we keep a `visited` set of `(r, c)` pairs.
4. Do this `k` times; the value we pop on the `k`‑th iteration is the answer.

Why this works:
- Because rows and columns are sorted, any neighbour we push is guaranteed to be **greater or equal** to the cell we just popped, so the heap always contains the next candidate smallest numbers.

COMPLEXITY:
-----------
Time:  O(k · log k) – we perform at most `k` heap pushes/pops.
Space: O(k) – the heap and visited set never grow larger than `k` elements.

EDGE CASES:
-----------
- The matrix could be empty → return `-1`.
- `k` could be larger than the total number of elements → return `-1`.
============================================================
"""

import heapq
from typing import List, Tuple, Set

def kth_smallest_in_matrix(matrix: List[List[int]], k: int) -> int:
    """Finds the k‑th smallest element in a row‑ and column‑sorted matrix.
    Returns -1 if the matrix is empty or k is out of bounds.
    """
    if not matrix or not matrix[0]:
        return -1
    rows, cols = len(matrix), len(matrix[0])
    total = rows * cols
    if k < 1 or k > total:
        return -1
    
    min_heap: List[Tuple[int, int, int]] = []  # (value, row, col)
    visited: Set[Tuple[int, int]] = set()
    
    # Start with the smallest element at (0,0)
    heapq.heappush(min_heap, (matrix[0][0], 0, 0))
    visited.add((0, 0))
    
    count = 0
    while min_heap:
        value, r, c = heapq.heappop(min_heap)
        count += 1
        if count == k:
            return value
        # Push right neighbour
        if c + 1 < cols and (r, c + 1) not in visited:
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
            visited.add((r, c + 1))
        # Push bottom neighbour
        if r + 1 < rows and (r + 1, c) not in visited:
            heapq.heappush(min_heap, (matrix[r + 1][c], r + 1, c))
            visited.add((r + 1, c))
    
    return -1  # Should never reach here if k is valid

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    mat = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    # Sorted order: 1,5,9,10,11,12,13,13,15
    assert kth_smallest_in_matrix(mat, 1) == 1, "Test 1"
    assert kth_smallest_in_matrix(mat, 5) == 11, "Test 2"
    assert kth_smallest_in_matrix(mat, 9) == 15, "Test 3"
    
    # Edge cases
    assert kth_smallest_in_matrix([], 1) == -1, "Edge empty matrix"
    assert kth_smallest_in_matrix([[2]], 2) == -1, "Edge k too large"
    
    print("All tests passed!")
