"""
============================================================
Problem: Kth Largest Number in a Stream
Pattern: Top K Elements
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cc19bc5746ebec8ee0b
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you are the scorekeeper for a video game that never ends.
Players are constantly submitting new scores (a "stream" of numbers).
At any given moment, someone might ask you: "What is the 3rd highest score so far?"
You can't pause the game, sort all 1,000,000 scores, and pick the 3rd one. That 
takes too long!
Instead, you keep a tiny notebook that only holds EXACTLY 3 scores.
You use a **Min-Heap** to manage this notebook.
The Min-Heap keeps the SMALLEST of your Top 3 scores at the top of the page.
When a new score comes in, you check the top of the page.
- "Is this new score BIGGER than the smallest score in my Top 3?"
- If yes, you erase the smallest score, and write down the new one!
- If no, you just ignore the new score.
When someone asks for the 3rd highest score, you just read them the score at 
the top of your page! It takes 0 extra seconds!

APPROACH:
---------
1. In the `__init__` method, store `k` and an empty `min_heap`.
2. Loop through the initial `nums` array and call `self.add(num)` for each.
3. In the `add(num)` method:
   - Push `num` onto the `min_heap`.
   - If the heap has more than `k` elements, kick out the smallest one 
     (`heapq.heappop`).
   - The Kth largest element is now sitting at `min_heap[0]`.
   - Return it!

COMPLEXITY:
-----------
Time:  O(log K) for each `add()` call. Initializing takes O(N * log K).
Space: O(K) — To store the K elements in the heap.

EDGE CASES:
-----------
- Edge case 1: Asking for the Kth largest before we even have K elements!
  (The problem usually guarantees we will have at least K elements before 
   expecting a valid Kth largest, or we just return the minimum of what we have).
============================================================
"""

import heapq
from typing import List

class KthLargestNumberInStream:
    def __init__(self, nums: List[int], k: int):
        self.k = k
        self.min_heap = []
        
        # Add all initial numbers to our heap
        for num in nums:
            self.add(num)
            
    def add(self, num: int) -> int:
        """
        Adds a new number to the stream and returns the Kth largest number so far.
        """
        # Add the new number
        heapq.heappush(self.min_heap, num)
        
        # If we have more than K numbers, kick out the smallest one!
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The smallest number in our Top K VIP club is the Kth largest overall!
        return self.min_heap[0]

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    kth_largest = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    # Stream is [3, 1, 5, 12, 2, 11]. Top 4 are [12, 11, 5, 3]. 4th largest is 3.
    assert kth_largest.add(6) == 5, "Test 1: Added 6. Top 4 are [12, 11, 6, 5]."
    assert kth_largest.add(13) == 6, "Test 2: Added 13. Top 4 are [13, 12, 11, 6]."
    assert kth_largest.add(4) == 6, "Test 3: Added 4. Top 4 are [13, 12, 11, 6]."

    print("All tests passed!")
