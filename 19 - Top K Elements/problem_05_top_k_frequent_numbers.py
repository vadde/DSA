"""
============================================================
Problem: Top 'K' Frequent Numbers
Pattern: Top K Elements
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cbaa00cc465d6c82779
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bag of numbers: `[1, 3, 5, 12, 11, 12, 11, 12, 5]`.
I want to know the 2 numbers that appear the MOST often!
Before we can know who appears the most, we have to actually count them!
So, step 1 is always: Go through the bag and make a tally sheet (a Hash Map).
`1` appears 1 time.
`3` appears 1 time.
`5` appears 2 times.
`11` appears 2 times.
`12` appears 3 times.
Now, we have a list of frequencies. We want the Top 2 LARGEST frequencies!
Just like Problem 1, when we want the LARGEST of something, we use a **Min-Heap**.
We put the frequencies into a Min-Heap of size K (2).
The heap will kick out the numbers with the smallest frequencies, leaving only 
the K numbers with the largest frequencies!

APPROACH:
---------
1. Count the frequencies of all numbers and store them in a Hash Map.
2. Initialize a `min_heap = []`.
3. Loop through the Hash Map. For each `(number, frequency)`:
   - Push `(frequency, number)` into the `min_heap`.
     (We put frequency FIRST because the heap sorts based on the first item!)
   - If the size of the `min_heap` grows larger than `K`, pop the top!
     (This kicks out the number with the lowest frequency).
4. Return a list of just the numbers from the `min_heap`.

COMPLEXITY:
-----------
Time:  O(N + U * log K) — Where N is the total numbers (for counting) and U is 
       the number of UNIQUE numbers (for pushing into the heap).
Space: O(U) — For the Hash Map. The heap takes O(K) space.

EDGE CASES:
-----------
- Edge case 1: K is equal to the number of unique elements. It just returns 
  all the unique elements.
============================================================
"""

import heapq
from typing import List
from collections import Counter

def find_k_frequent_numbers(nums: List[int], k: int) -> List[int]:
    """
    Returns the K most frequent numbers in an array.
    """
    # 1. Count the frequencies of each number
    freq_map = Counter(nums)
    
    min_heap = []
    
    # 2. Iterate through the unique numbers and their frequencies
    for num, freq in freq_map.items():
        # Push a tuple of (frequency, number) so the heap sorts by frequency
        heapq.heappush(min_heap, (freq, num))
        
        # 3. If the heap gets too big, kick out the one with the smallest frequency
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    # 4. Extract just the numbers to return
    result = []
    for item in min_heap:
        result.append(item[1])
        
    return result

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    result1 = find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)
    # 11 and 12 both appear twice
    assert sorted(result1) == [11, 12], f"Test 1 failed. Got {result1}"
    
    result2 = find_k_frequent_numbers([5, 12, 11, 3, 11], 2)
    # 11 appears twice, others appear once. So 11 and (one of 5, 12, 3).
    # Since K=2, the second item could be any of the ones that appear once.
    # We'll just verify 11 is in there and the length is 2.
    assert 11 in result2 and len(result2) == 2, f"Test 2 failed. Got {result2}"

    # 🔲 Edge cases
    assert sorted(find_k_frequent_numbers([1, 1, 1, 1], 1)) == [1], "Edge 1: All same"

    print("All tests passed!")
