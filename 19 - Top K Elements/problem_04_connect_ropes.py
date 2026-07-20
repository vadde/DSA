"""
============================================================
Problem: Connect Ropes
Pattern: Top K Elements
Difficulty: Easy
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cb7a00cc465d6c82775
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bunch of short ropes: `[1, 3, 11, 5]`.
You need to tie them all together to make one giant rope.
But tying ropes takes energy! The energy it takes to tie two ropes together 
is equal to the length of the ropes you are holding.
For example, if you tie the `11` and the `5`, it costs you `16` energy.
And now you have a new combined rope of length `16`!
To save as much energy as possible, you always want to tie the TWO SHORTEST 
ropes together first.
So:
1. Find the two shortest: `1` and `3`. Tie them. Cost = `4`.
   New ropes: `[4, 11, 5]`.
2. Find the two shortest: `4` and `5`. Tie them. Cost = `9`.
   New ropes: `[9, 11]`.
3. Find the two shortest: `9` and `11`. Tie them. Cost = `20`.
   New ropes: `[20]`.
Total energy spent = `4 + 9 + 20 = 33`.
Because we ALWAYS need the two smallest items from a changing list, this is the 
perfect job for a **Min-Heap**!

APPROACH:
---------
1. Put all the ropes into a `min_heap`. (In Python, `heapq.heapify(ropes)` does 
   this in O(N) time).
2. Initialize `total_cost = 0`.
3. Loop while the heap has more than 1 rope:
   - Pop the smallest rope: `rope1 = heappop(min_heap)`.
   - Pop the second smallest rope: `rope2 = heappop(min_heap)`.
   - Calculate the cost to tie them: `temp_cost = rope1 + rope2`.
   - Add it to the total: `total_cost += temp_cost`.
   - Put the newly tied, longer rope back into the pile! 
     `heappush(min_heap, temp_cost)`.
4. Return `total_cost`.

COMPLEXITY:
-----------
Time:  O(N * log N) — We insert N items. Then we do 2 pops and 1 push (each takes 
       O(log N)) until 1 item remains.
Space: O(N) — To store the N ropes in the heap.

EDGE CASES:
-----------
- Edge case 1: There is only 1 rope. No tying needed! Cost is 0.
============================================================
"""

import heapq
from typing import List

def connect_ropes(rope_lengths: List[int]) -> int:
    """
    Returns the minimum cost to connect all ropes into one.
    """
    if len(rope_lengths) <= 1:
        return 0
        
    # 1. Turn the list into a Min-Heap in O(N) time!
    min_heap = rope_lengths[:]
    heapq.heapify(min_heap)
    
    total_cost = 0
    
    # 2. Keep tying ropes until only 1 giant rope is left
    while len(min_heap) > 1:
        # Get the two shortest ropes
        rope1 = heapq.heappop(min_heap)
        rope2 = heapq.heappop(min_heap)
        
        # Tie them together
        current_cost = rope1 + rope2
        total_cost += current_cost
        
        # Throw the newly tied rope back into the pile
        heapq.heappush(min_heap, current_cost)
        
    return total_cost

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert connect_ropes([1, 3, 11, 5]) == 33, "Test 1"
    assert connect_ropes([3, 4, 5, 6]) == 36, "Test 2"
    assert connect_ropes([1, 3, 11, 5, 2]) == 42, "Test 3"

    # 🔲 Edge cases
    assert connect_ropes([10]) == 0, "Edge 1: Only one rope"

    print("All tests passed!")
