"""
============================================================
Problem: Kth Smallest Number in M Sorted Lists
Pattern: K-way Merge
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1ce2a00cc465d6c827c1
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have `M` separate arrays, and each one is sorted.
You want to find the 5th smallest number among ALL of them combined.
Instead of actually combining them into one giant list (like we did in the 
last problem) and then picking the 5th one, we can just do the exact same 
thing, but count!
1. Pop the smallest number from the heap. (Count = 1).
2. Pop the next smallest. (Count = 2).
3. Pop again. (Count = 3).
...
Once `Count == K`, the number you just popped is your answer!
You don't need to build a new list. You just throw away the first `K-1` numbers, 
and keep the `K`th one!

APPROACH:
---------
1. Put the first element of each of the `M` arrays into a Min-Heap.
   - We must push a tuple: `(value, array_index, element_index)`.
2. Initialize `count = 0`.
3. Loop while `min_heap` is not empty:
   - Pop the smallest number: `value, arr_idx, el_idx = heappop(min_heap)`.
   - `count += 1`.
   - If `count == k`: return `value`!
   - If that array has more elements (`el_idx + 1 < len(arrays[arr_idx])`):
     - Push the next element from that array into the heap!
4. If we exit the loop, there weren't enough elements, return `-1`.

COMPLEXITY:
-----------
Time:  O(K * log M) — Where M is the number of input arrays. We push M items 
       initially. Then we pop and push at most K times.
Space: O(M) — For the heap.

EDGE CASES:
-----------
- Edge case 1: K is larger than the total number of elements in all arrays.
============================================================
"""

import heapq
from typing import List

def find_kth_smallest(lists: List[List[int]], k: int) -> int:
    """
    Finds the Kth smallest number across M sorted arrays.
    """
    min_heap = []
    
    # 1. Put the first element of each array into the Min-Heap
    for i in range(len(lists)):
        if len(lists[i]) > 0:
            # (value, array_index, element_index)
            heapq.heappush(min_heap, (lists[i][0], i, 0))
            
    count = 0
    
    # 2. Keep popping the smallest number until we hit 'K'
    while min_heap:
        value, arr_idx, el_idx = heapq.heappop(min_heap)
        
        count += 1
        
        # Did we find the Kth smallest?
        if count == k:
            return value
            
        # 3. If there are more elements in the current array, push the next one
        if el_idx + 1 < len(lists[arr_idx]):
            next_value = lists[arr_idx][el_idx + 1]
            heapq.heappush(min_heap, (next_value, arr_idx, el_idx + 1))
            
    # If K is larger than the total number of elements
    return -1

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    l1 = [2, 6, 8]
    l2 = [3, 6, 7]
    l3 = [1, 3, 4]
    
    # Combined sorted: 1, 2, 3, 3, 4, 6, 6, 7, 8
    assert find_kth_smallest([l1, l2, l3], 5) == 4, "Test 1"
    
    l1 = [5, 8, 9]
    l2 = [1, 7]
    # Combined sorted: 1, 5, 7, 8, 9
    assert find_kth_smallest([l1, l2], 3) == 7, "Test 2"

    # 🔲 Edge cases
    assert find_kth_smallest([[1, 2], [3]], 5) == -1, "Edge 1: K is too large"

    print("All tests passed!")
