"""
============================================================
Problem: Maximum Distinct Elements
Pattern: Top K Elements / Greedy
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cc9a00cc465d6c8278c
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bag of fruit: `[apple, apple, orange, banana, banana, banana]`.
You have a magic wand that can delete EXACTLY `K = 2` fruits.
You want to have as many DIFFERENT types of fruits as possible at the end!
Currently, you have 3 distinct fruits (apple, orange, banana). But you HAVE to 
delete 2 fruits.
Which ones do you delete?
- If you delete the `orange`, you lose a distinct fruit! Bad idea!
- If you delete an `apple`, you still have one `apple` left. Distinct count is safe!
- If you delete two `banana`s, you still have one `banana` left. Distinct count is safe!
So, you want to delete the DUPLICATES. 
But to save the most fruits, you should target the fruits that only have a FEW 
duplicates first!
For example, it only takes 1 swipe of the wand to fix the `apples`. It takes 
2 swipes to fix the `bananas`.
So, we put all the fruits that have duplicates into a **Min-Heap**, sorted by 
how many duplicates they have!
Then we pop them out and delete them until our wand runs out of power (`K=0`).
If our wand STILL has power after fixing all duplicates, we are forced to delete 
unique fruits, reducing our distinct count.

APPROACH:
---------
1. Count the frequencies of all numbers using a Hash Map.
2. Initialize `distinct_count = 0` and a `min_heap = []`.
3. Loop through the Hash Map:
   - If `freq == 1`, `distinct_count += 1`.
   - If `freq > 1`, push `(freq, num)` to `min_heap`.
4. While `K > 0` and `min_heap` is not empty:
   - `freq, num = heappop(min_heap)`
   - We need to delete `freq - 1` elements to make this number unique.
   - `K -= (freq - 1)`
   - If `K >= 0`, we successfully made it unique! `distinct_count += 1`.
   - If `K < 0`, we didn't have enough power. It's completely gone.
5. If `K > 0` after the heap is empty, we must delete unique elements.
   - `distinct_count -= K`
6. Return `distinct_count`.

COMPLEXITY:
-----------
Time:  O(N * log N) — Counting takes O(N). Pushing to heap takes O(N log N) worst case.
Space: O(N) — For Hash Map and Heap.

EDGE CASES:
-----------
- Edge case 1: K is larger than the array length. We delete everything, returning 0.
============================================================
"""

import heapq
from typing import List
from collections import Counter

def find_maximum_distinct_elements(nums: List[int], k: int) -> int:
    """
    Returns the maximum number of distinct elements after removing exactly K elements.
    """
    if len(nums) <= k:
        return 0
        
    freq_map = Counter(nums)
    distinct_count = 0
    min_heap = []
    
    # 1. Separate the already distinct numbers from the ones with duplicates
    for num, freq in freq_map.items():
        if freq == 1:
            distinct_count += 1
        else:
            heapq.heappush(min_heap, (freq, num))
            
    # 2. Try to reduce duplicates to exactly 1 using our 'k' deletions greedily
    while k > 0 and min_heap:
        freq, num = heapq.heappop(min_heap)
        
        # To make a number unique, we need to delete (freq - 1) of it
        deletions_needed = freq - 1
        
        # Do we have enough deletions left?
        if k >= deletions_needed:
            k -= deletions_needed
            distinct_count += 1 # We successfully salvaged this number!
        else:
            # We don't have enough deletions to save this number. We just use 
            # whatever k we have left, but it won't become unique.
            k = 0
            
    # 3. If we STILL have deletions left, we are forced to delete unique numbers
    if k > 0:
        distinct_count -= k
        
    return distinct_count

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # 1,2,3 are unique (3). 7 is duplicate (freq 3). K=2.
    # Delete two 7s. 7 becomes unique. Total distinct = 4.
    assert find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2) == 3, "Test 1"
    # Freq: 3:3, 5:2, 7:1, 8:1. Distinct=2. Heap: (2,5), (3,3). K=2.
    # Pop 5. Deletions needed=1. K becomes 1. Distinct becomes 3.
    # Pop 3. Deletions needed=2. K=1. Not enough! K becomes 0. Distinct stays 3.
    
    assert find_maximum_distinct_elements([3, 5, 12, 11, 12], 3) == 2, "Test 2"

    # 🔲 Edge cases
    assert find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2) == 3, "Edge 1"

    print("All tests passed!")
