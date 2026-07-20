"""
============================================================
Problem: Maximize Capital
Pattern: Two Heaps
Difficulty: Hard (Advanced)
Link: https://leetcode.com/problems/ipo/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are an investor with some starting money (Capital `w`).
There are many projects you can invest in. Every project costs a certain amount 
of Capital to start, and gives you a certain amount of Profit.
You only have time to do `k` projects.
You want to make the absolute most money possible!
If you just pick the project with the highest profit, you might not have enough 
money to afford it yet.
So, you use Two Sorting Hats (Heaps):
1. The "Too Expensive" Hat (Min Heap): You put ALL projects in here, sorted by 
   how much they COST.
2. The "Affordable" Hat (Max Heap): You put projects you can afford in here, 
   sorted by how much PROFIT they make.

Step 1: You look at the "Too Expensive" hat. For any project that you can now 
afford (because Cost <= your Capital `w`), you take it out and throw it into 
the "Affordable" hat!
Step 2: You reach into the "Affordable" hat and pull out the SINGLE project that 
gives the most Profit. You do it, and you add the Profit to your Capital `w`!
Now that you have more money, maybe you can afford new projects! So you repeat 
Step 1 and Step 2 until you've done `k` projects.

APPROACH:
---------
1. Initialize `min_capital_heap = []` and `max_profit_heap = []`.
2. Push all projects into `min_capital_heap` as tuples: `(capital_cost, profit)`. 
   (Since it's a Min Heap, it will sort by `capital_cost` automatically).
3. Loop `k` times:
   - While the `min_capital_heap` is not empty AND the cheapest project's cost 
     is `<= w`:
     - Pop it from `min_capital_heap`.
     - Push it into `max_profit_heap` as `(-profit, capital_cost)` so it sorts 
       by the highest profit!
   - If `max_profit_heap` is empty, it means we can't afford ANY projects! Break.
   - Pop the most profitable project from `max_profit_heap`.
   - Add its profit to `w`.
4. Return `w`.

COMPLEXITY:
-----------
Time:  O(N log N + K log N) — O(N log N) to insert all projects into the min heap. 
       We then pop and push to the max heap at most N times overall, and we do K 
       pops from the max heap.
Space: O(N) — For the two heaps.

EDGE CASES:
-----------
- Edge case 1: We can't afford the cheapest project. Loop breaks immediately.
- Edge case 2: `k` is larger than the total number of projects. We just do all 
  affordable projects and stop when the heaps are empty.
============================================================
"""

import heapq
from typing import List

def find_maximized_capital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    """
    Returns the maximum capital possible after finishing at most k distinct projects.
    """
    # 1. Min heap to store projects sorted by their capital requirement
    min_capital_heap = []
    for i in range(len(profits)):
        heapq.heappush(min_capital_heap, (capital[i], profits[i]))
        
    # 2. Max heap to store affordable projects sorted by profit
    max_profit_heap = []
    
    # 3. Do at most k projects
    for _ in range(k):
        # Transfer all projects we can currently afford into the max_profit_heap
        while min_capital_heap and min_capital_heap[0][0] <= w:
            cost, profit = heapq.heappop(min_capital_heap)
            # Push -profit to simulate a Max Heap
            heapq.heappush(max_profit_heap, (-profit, cost))
            
        # If we can't afford any projects, we have to stop early
        if not max_profit_heap:
            break
            
        # Do the project that gives the maximum profit!
        # Remember to negate the profit back to a positive number
        best_profit = -heapq.heappop(max_profit_heap)[0]
        w += best_profit
        
    return w

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # Profits: [1, 2, 3], Capital: [0, 1, 1], Initial Capital: 0, K = 2
    # Can afford project 0 (profit 1, cost 0). Capital becomes 0 + 1 = 1.
    # Can now afford projects 1 and 2. We pick project 2 (profit 3, cost 1). Capital becomes 1 + 3 = 4.
    assert find_maximized_capital(2, 0, [1, 2, 3], [0, 1, 1]) == 4, "Test 1 failed"

    # Profits: [1, 2, 3], Capital: [0, 1, 2], Initial Capital: 0, K = 3
    # Step 1: cost 0 -> profit 1. Cap = 1
    # Step 2: cost 1 -> profit 2. Cap = 3
    # Step 3: cost 2 -> profit 3. Cap = 6
    assert find_maximized_capital(3, 0, [1, 2, 3], [0, 1, 2]) == 6, "Test 2 failed"

    # 🔲 Edge cases
    # Initial capital is too low to afford anything
    assert find_maximized_capital(2, 0, [1, 2, 3], [1, 1, 1]) == 0, "Edge 1: Can't afford anything"

    print("All tests passed!")
