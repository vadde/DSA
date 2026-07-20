"""
============================================================
Problem: Kth Smallest Number
Pattern: Top K Elements
Difficulty: Easy
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1caea00cc465d6c82765
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bag of numbers: `[1, 5, 12, 2, 11, 5]`.
I want to find the 3rd SMALLEST number.
This time, we don't want the VIP club for the strongest people. We want the 
VIP club for the WEAKEST people! (Smallest numbers).
If we want the weakest people, who do we want the bouncer to kick out? 
The STRONGEST person!
So, we use a **Max Heap**! A Max Heap puts the largest number right at the front door.
1. We put the first 3 numbers in the club: `[1, 5, 12]`.
   - The Max Heap puts `12` at the door.
2. We look at the next number: `2`.
   - Is `2` WEAKER (smaller) than the strongest guy in the club (`12`)?
   - YES! Kick out `12`, let `2` in.
   - Club: `[1, 2, 5]`. The strongest is now `5`.
3. We look at `11`.
   - Is `11` weaker than `5`? NO! Go away.
4. We look at `5`.
   - Is `5` weaker than `5`? NO. (We usually only swap if strictly smaller).
When we run out of numbers, our club has exactly the 3 smallest numbers: `[1, 2, 5]`.
Since the Max Heap puts the LARGEST of these 3 numbers at the front door, the 
number standing at the door is exactly the 3rd smallest number in the whole bag!
Which is `5`!

APPROACH:
---------
1. Since Python's `heapq` is a Min-Heap, we simulate a Max-Heap by pushing the 
   negative value of the numbers (`-num`).
2. Initialize `max_heap = []`.
3. Push the first `K` elements (negated) into `max_heap`.
4. Loop through the rest of the array.
5. If the current number is SMALLER than the top of the heap (which is `-max_heap[0]`), 
   we pop the top element and push the current number (negated).
6. Return the top of the heap (negated back to positive).

COMPLEXITY:
-----------
Time:  O(N * log K)
Space: O(K)

EDGE CASES:
-----------
- Edge case 1: Array length is exactly K. We just put everything in the heap 
  and return the top.
============================================================
"""

import heapq
from typing import List

def find_Kth_smallest_number(nums: List[int], k: int) -> int:
    """
    Returns the Kth smallest number in an array using a Max-Heap.
    """
    max_heap = []
    
    # 1. Put the first 'K' numbers in the max heap
    # In Python, we push -num to simulate a Max-Heap
    for i in range(k):
        heapq.heappush(max_heap, -nums[i])
        
    # 2. Go through the remaining numbers
    for i in range(k, len(nums)):
        # 3. If the current number is smaller than the largest number in our 
        #    "weak VIP club", swap them!
        # The largest number is at max_heap[0], but it's negative.
        # So -max_heap[0] is the actual positive value.
        if nums[i] < -max_heap[0]:
            heapq.heappushpop(max_heap, -nums[i])
            
    # The top of the max heap is the largest of the K smallest numbers.
    # Which is exactly the Kth smallest number!
    return -max_heap[0]

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3) == 5, "Test 1"
    assert find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4) == 5, "Test 2"
    assert find_Kth_smallest_number([5, 12, 11, -1, 12], 3) == 11, "Test 3"

    # 🔲 Edge cases
    assert find_Kth_smallest_number([1, 2], 2) == 2, "Edge 1: K == N"

    print("All tests passed!")
