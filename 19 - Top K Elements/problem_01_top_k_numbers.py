"""
============================================================
Problem: Top 'K' Numbers
Pattern: Top K Elements
Difficulty: Easy
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1caca00cc465d6c8275e
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bag of numbers: `[3, 1, 5, 12, 2, 11]`.
I want you to give me the 3 LARGEST numbers.
You could sort the whole bag and give me the last 3, but sorting is slow!
Instead, you make a special VIP club that only fits 3 people.
You use a "Min Heap" as the bouncer for this club.
A Min Heap always puts the WEAKEST (smallest) person right at the front door.
1. You put the first 3 numbers in the club: `[3, 1, 5]`.
   - The Min Heap arranges them so the weakest (`1`) is at the door.
2. You look at the next number: `12`.
   - You ask: "Is 12 stronger than the weakest guy in the club (`1`)?"
   - YES! So you kick out `1` and let `12` in.
   - Now the club has `[3, 5, 12]`. The weakest is now `3`.
3. You look at `2`.
   - "Is 2 stronger than 3?" NO! Go away.
4. You look at `11`.
   - "Is 11 stronger than 3?" YES! Kick out `3`, let `11` in.
   - Club: `[5, 11, 12]`.
When you run out of numbers, the club only contains the Top 3 Largest numbers!

APPROACH:
---------
1. Initialize a `min_heap = []`.
2. Push the first `K` elements from the array into `min_heap`.
3. Loop through the rest of the array (from index `K` to the end).
4. If the current number is LARGER than the top of the heap (`min_heap[0]`), 
   we pop the top element and push the current number.
5. Return the heap (converted to a list if necessary).

COMPLEXITY:
-----------
Time:  O(N * log K) — We iterate through N numbers, and pushing/popping from 
       a heap of size K takes O(log K).
Space: O(K) — To store the K elements in the heap.

EDGE CASES:
-----------
- Edge case 1: K is larger than or equal to the size of the array. Just put 
  everything in the heap and return it!
============================================================
"""

import heapq
from typing import List

def find_k_largest_numbers(nums: List[int], k: int) -> List[int]:
    """
    Returns the top K largest numbers in the given array using a Min-Heap.
    """
    min_heap = []
    
    # 1. Put the first 'K' numbers in the min heap
    # (Handling the edge case where K > len(nums))
    for i in range(min(k, len(nums))):
        heapq.heappush(min_heap, nums[i])
        
    # 2. Go through the remaining numbers of the array
    for i in range(k, len(nums)):
        # 3. If the current number is bigger than the smallest number in the 
        #    "VIP club", it deserves to be in the club!
        if nums[i] > min_heap[0]:
            # heappushpop is more efficient than doing a heappop then heappush!
            heapq.heappushpop(min_heap, nums[i])
            
    # The heap now contains the top 'K' numbers
    return list(min_heap)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    result1 = find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)
    # The order inside the heap might not be perfectly sorted, so we sort for the assert
    assert sorted(result1) == [5, 11, 12], f"Test 1 failed. Got {result1}"
    
    result2 = find_k_largest_numbers([5, 12, 11, -1, 12], 3)
    assert sorted(result2) == [11, 12, 12], f"Test 2 failed. Got {result2}"

    # 🔲 Edge cases
    assert sorted(find_k_largest_numbers([1, 2], 3)) == [1, 2], "Edge 1: K > N"

    print("All tests passed!")
