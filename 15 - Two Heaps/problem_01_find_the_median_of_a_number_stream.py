"""
============================================================
Problem: Find the Median of a Number Stream
Pattern: Two Heaps
Difficulty: Medium
Link: https://leetcode.com/problems/find-median-from-data-stream/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are a teacher receiving a constant stream of test scores from your students.
Every time a new score comes in, the principal bursts into the room and yells: 
"WHAT IS THE MEDIAN SCORE RIGHT NOW?!"
If you have to sort the entire stack of papers every single time he asks, you 
will never get any work done.
Instead, you put two baskets on your desk:
1. The "Bottom Half" basket. (It only shows you the LARGEST score inside it).
2. The "Top Half" basket. (It only shows you the SMALLEST score inside it).
When a new score comes in, you drop it into the Bottom Half basket.
But what if that score was a 100%? It belongs in the Top Half!
So, you immediately grab the largest score from the Bottom Half basket and 
throw it into the Top Half basket. This perfectly filters the scores!
Finally, if the Top Half basket ever gets fuller than the Bottom Half basket, 
you grab its smallest score and throw it back into the Bottom Half basket. 
This guarantees the Bottom Half is always exactly equal to, or exactly 1 paper 
larger than, the Top Half.
When the principal yells, you just look at the top paper in both baskets!

APPROACH:
---------
1. Initialize two heaps:
   - `max_heap` (Bottom half of numbers). Python only has Min Heaps, so we push `-num`.
   - `min_heap` (Top half of numbers).
2. Define `insert_num(num)`:
   - Push `-num` onto the `max_heap`.
   - Pop from `max_heap` (remember to negate it back!) and push it onto `min_heap`. 
     This ensures the absolute largest number in the bottom half correctly moves to the top half.
   - If `len(min_heap) > len(max_heap)`, pop from `min_heap` and push it (negated) 
     back to `max_heap`. This ensures `max_heap` always has the middle element if 
     the total count is odd!
3. Define `find_median()`:
   - If both heaps are the same size (even total), the median is the average of 
     the top elements of both heaps: `(-max_heap[0] + min_heap[0]) / 2.0`.
   - If `max_heap` is larger (odd total), the median is just the top element of 
     `max_heap`: `-max_heap[0] / 1.0`.

COMPLEXITY:
-----------
Time:  O(log N) for `insert_num` due to heap operations. O(1) for `find_median`.
Space: O(N) to store the numbers in the heaps.

EDGE CASES:
-----------
- Edge case 1: Getting the median after only 1 insertion. Handled correctly because `max_heap` will have size 1 and `min_heap` will have size 0.
============================================================
"""

import heapq

class MedianFinder:
    def __init__(self):
        # max_heap stores the smaller half of the numbers
        self.max_heap = []
        # min_heap stores the larger half of the numbers
        self.min_heap = []

    def insert_num(self, num: int) -> None:
        # 1. Always push to the max_heap first (negate the number for Python)
        heapq.heappush(self.max_heap, -num)
        
        # 2. Transfer the largest number from the bottom half to the top half
        largest_bottom = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, largest_bottom)
        
        # 3. Balance the heaps. We want max_heap to be >= min_heap in size.
        if len(self.min_heap) > len(self.max_heap):
            smallest_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smallest_top)

    def find_median(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            # Even number of elements, take average of the two middle elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        
        # Odd number of elements, the middle element is at the top of max_heap
        return -self.max_heap[0] / 1.0

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    median_finder = MedianFinder()
    
    # Insert 3 -> [3]
    median_finder.insert_num(3)
    assert median_finder.find_median() == 3.0, "Test 1 failed"
    
    # Insert 1 -> [1, 3]
    median_finder.insert_num(1)
    assert median_finder.find_median() == 2.0, "Test 2 failed"
    
    # Insert 5 -> [1, 3, 5]
    median_finder.insert_num(5)
    assert median_finder.find_median() == 3.0, "Test 3 failed"
    
    # Insert 4 -> [1, 3, 4, 5]
    median_finder.insert_num(4)
    assert median_finder.find_median() == 3.5, "Test 4 failed"

    print("All tests passed!")
