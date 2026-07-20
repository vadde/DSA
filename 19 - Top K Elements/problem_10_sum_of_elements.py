"""
============================================================
Problem: Sum of Elements
Pattern: Top K Elements
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1ccba00cc465d6c82790
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an array: `[1, 3, 12, 5, 15, 11]`.
I want you to find the sum of all numbers that are BIGGER than the 3rd smallest 
number (which is `5`) but SMALLER than the 6th smallest number (which is `15`).
Basically, the numbers between `K1` (3) and `K2` (6).
The numbers between `5` and `15` in our list are `12` and `11`. Their sum is `23`.
To find these numbers easily, we can use a **Min-Heap**.
If we dump all the numbers into a Min-Heap, they are magically organized so 
that the smallest numbers come out first.
So:
1. Pop `K1` numbers out of the heap. (We throw them in the trash, we don't need them).
   - Pops 1, 3, 5.
2. Now, the heap is perfectly queued up with the numbers we DO want!
3. Pop the heap exactly `(K2 - K1 - 1)` times, and add those numbers together!
   - Pops 11, 12. Sum = 23.
   - We stop before hitting K2.

APPROACH:
---------
1. Put all numbers in a `min_heap`. (Use `heapq.heapify` for O(N) time).
2. Loop `K1` times and `heappop` the heap (discarding the elements).
3. Initialize `element_sum = 0`.
4. Loop `K2 - K1 - 1` times:
   - `element_sum += heappop(min_heap)`
5. Return `element_sum`.

COMPLEXITY:
-----------
Time:  O(N + K2 * log N) — O(N) to build the heap. We pop at most K2 times, each 
       taking O(log N).
Space: O(N) — To store the numbers in the heap.

EDGE CASES:
-----------
- Edge case 1: There are no numbers between K1 and K2. (e.g., K1 = 2, K2 = 3).
  The loop for accumulating sum will run `3 - 2 - 1 = 0` times. Returns 0.
============================================================
"""

import heapq
from typing import List

def find_sum_of_elements(nums: List[int], k1: int, k2: int) -> int:
    """
    Returns the sum of all numbers between the k1'th and k2'th smallest elements.
    """
    # 1. Build the Min-Heap
    min_heap = nums[:] # Make a copy to avoid mutating the input
    heapq.heapify(min_heap)
    
    # 2. Throw away the first K1 smallest numbers
    for _ in range(k1):
        heapq.heappop(min_heap)
        
    element_sum = 0
    
    # 3. Add up the numbers between K1 and K2
    # The number of elements between K1 and K2 is (K2 - K1 - 1)
    for _ in range(k2 - k1 - 1):
        element_sum += heapq.heappop(min_heap)
        
    return element_sum

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # Sorted: 1, 3, 5, 11, 12, 15
    # K1 = 3 (5). K2 = 6 (15). Between them: 11, 12. Sum = 23.
    assert find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6) == 23, "Test 1"
    
    # Sorted: 1, 3, 5, 12
    # K1 = 1 (1). K2 = 4 (12). Between them: 3, 5. Sum = 8.
    assert find_sum_of_elements([3, 5, 8, 7], 1, 4) == 12, "Test 2" 
    # Wait, 3,5,8,7 sorted is 3,5,7,8. K1=1 (3). K2=4 (8). Between them: 5, 7. Sum = 12.
    # Ah, I wrote [3,5,8,7], but my explanation was 1,3,5,12. 
    # 3,5,8,7 sorted is 3,5,7,8. Between 1st and 4th is 5,7. 5+7=12. Correct.

    # 🔲 Edge cases
    assert find_sum_of_elements([1, 2, 3, 4], 2, 3) == 0, "Edge 1: Adjacent K1 and K2"

    print("All tests passed!")
