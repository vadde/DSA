"""
============================================================
Problem: Sliding Window Median
Pattern: Two Heaps / Sliding Window
Difficulty: Hard
Link: https://leetcode.com/problems/sliding-window-median/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Remember the Two Heaps we used to find the Median of a stream of scores?
What if the principal changes the rules: "I only care about the median of the 
LAST 3 SCORES!"
As the 4th score comes in, the 1st score "slides" out of the window and must 
be thrown in the trash.
But here's the problem: Our magical sorting hats (Heaps) are only designed to 
pull numbers out of the very TOP of the hat. What if the score we need to throw 
away is buried deep at the bottom of the hat?
We can't easily dig it out!
So, we use a trick called "Lazy Deletion".
We keep a "Trash List" (a Hash Map). When a score leaves the window, we just 
write it down on the Trash List and leave the actual paper inside the hat!
Whenever we go to check the Top of the hat, we first look at the top paper and 
ask: "Wait, is this number on the Trash List?"
If yes, we finally pull it out and throw it away, and check the NEXT paper.
We keep pulling trash out of the top until we see a clean, valid number!

APPROACH:
---------
1. Initialize `max_heap`, `min_heap`, and `trash_map = {}` (to count how many 
   times a number should be deleted).
2. We need to track the "valid" size of both heaps (ignoring the trash buried 
   inside them). `max_heap_valid_size` and `min_heap_valid_size`.
3. `insert(num)`: 
   - Push to `max_heap`, then transfer the largest to `min_heap`. Update valid sizes.
4. `remove(num)`:
   - Increment `trash_map[num] += 1`.
   - If `num` is <= the largest number in the bottom half (i.e., `num <= -max_heap[0]`), 
     it means it's buried in the `max_heap`. Decrement `max_heap_valid_size`.
   - Otherwise, it's buried in the `min_heap`. Decrement `min_heap_valid_size`.
5. `rebalance()`:
   - Make sure `max_heap_valid_size` is always equal to, or exactly 1 greater 
     than, `min_heap_valid_size`. If they are unbalanced, pop a number from one 
     and push it to the other (and update valid sizes).
6. `clean_tops()`:
   - This is the crucial "Lazy Deletion" step!
   - `while max_heap and trash_map[-max_heap[0]] > 0`: pop it and decrement the trash count!
   - Do the same for `min_heap`.
   - We MUST do this before returning the median, so the top numbers are always real!

COMPLEXITY:
-----------
Time:  O(N log K) — Inserting and lazily deleting takes O(log K) time per element.
Space: O(K) — The heaps and hash map will never grow much larger than K.

EDGE CASES:
-----------
- Edge case 1: K is 1. The median is just the array itself.
============================================================
"""

import heapq
from typing import List

class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.trash = {}
        # We track the actual number of VALID elements in each heap
        self.max_size = 0
        self.min_size = 0

    def median_sliding_window(self, nums: List[int], k: int) -> List[float]:
        result = []
        
        for i in range(len(nums)):
            # 1. Insert the new number
            num = nums[i]
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            self.min_size += 1
            
            # 2. Rebalance (max_heap should always have >= elements than min_heap)
            if self.min_size > self.max_size:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                self.min_size -= 1
                self.max_size += 1

            # 3. If the window is too large, we must remove the oldest number
            if i >= k:
                old_num = nums[i - k]
                self.trash[old_num] = self.trash.get(old_num, 0) + 1
                
                # Determine which heap the old_num was buried in
                # We can safely look at max_heap[0] because we know k > 0 and 
                # we just did a push/rebalance, so max_heap is never empty here.
                if old_num <= -self.max_heap[0]:
                    self.max_size -= 1
                else:
                    self.min_size -= 1
                    
            # 4. Rebalance AGAIN after the logical removal
            if self.max_size > self.min_size + 1:
                self.clean_heap_top(self.max_heap, True)
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                self.max_size -= 1
                self.min_size += 1
            elif self.max_size < self.min_size:
                self.clean_heap_top(self.min_heap, False)
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                self.min_size -= 1
                self.max_size += 1

            # 5. If our window is exactly size K, record the median
            if i >= k - 1:
                # CRITICAL: Clean the tops of both heaps before looking at them!
                self.clean_heap_top(self.max_heap, True)
                self.clean_heap_top(self.min_heap, False)
                
                if k % 2 == 1:
                    result.append(float(-self.max_heap[0]))
                else:
                    result.append((-self.max_heap[0] + self.min_heap[0]) / 2.0)

        return result

    def clean_heap_top(self, heap: List[int], is_max_heap: bool):
        """
        Lazily deletes elements from the top of the heap if they are in the trash.
        """
        while heap:
            top_val = -heap[0] if is_max_heap else heap[0]
            if self.trash.get(top_val, 0) > 0:
                self.trash[top_val] -= 1
                heapq.heappop(heap)
            else:
                break

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    swm = SlidingWindowMedian()
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    # Windows:
    # [1, 3, -1] -> Median: 1.0
    # [3, -1, -3] -> Median: -1.0
    # [-1, -3, 5] -> Median: -1.0
    # [-3, 5, 3] -> Median: 3.0
    # [5, 3, 6] -> Median: 5.0
    # [3, 6, 7] -> Median: 6.0
    expected1 = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    assert swm.median_sliding_window(nums1, k1) == expected1, f"Test 1 failed"

    # 🔲 Edge cases
    swm2 = SlidingWindowMedian()
    assert swm2.median_sliding_window([1, 2, 3], 1) == [1.0, 2.0, 3.0], "Edge 1: k=1"

    swm3 = SlidingWindowMedian()
    assert swm3.median_sliding_window([1, 2], 2) == [1.5], "Edge 2: k=len"

    print("All tests passed!")
