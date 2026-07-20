"""
============================================================
Problem: Range Distinct Elements
Pattern: MO's Algorithm
Difficulty: Hard
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array, you get many queries `[L, R]`.
For each query, answer: "How many DISTINCT numbers are there from index L to R?"
Prefix sums CANNOT solve this because distinct elements don't just "add up".

APPROACH: MO's Algorithm
---------
1. Same as before, sort queries by `block(L)` and then `R`.
2. Maintain a `frequency` hash map and a `distinct_count` variable.
3. When `add(num)` is called:
   - If `frequency[num] == 0`, `distinct_count += 1`
   - `frequency[num] += 1`
4. When `remove(num)` is called:
   - `frequency[num] -= 1`
   - If `frequency[num] == 0`, `distinct_count -= 1`
5. Slide the window to match each query, recording `distinct_count`!

COMPLEXITY:
-----------
Time:  O(Q log Q + Q * sqrt(N))
Space: O(N + Q)
============================================================
"""

from typing import List
import math


class Query:
    def __init__(self, L: int, R: int, index: int):
        self.L = L
        self.R = R
        self.index = index


def range_distinct_queries(nums: List[int], queries_input: List[List[int]]) -> List[int]:
    n = len(nums)
    if n == 0:
        return []
        
    block_size = int(math.sqrt(n))
    queries = [Query(q[0], q[1], i) for i, q in enumerate(queries_input)]
    
    # Sort queries according to MO's logic
    queries.sort(key=lambda q: (q.L // block_size, q.R))
    
    result = [0] * len(queries)
    freq = {}
    distinct_count = 0
    
    def add(num: int):
        nonlocal distinct_count
        count = freq.get(num, 0)
        if count == 0:
            distinct_count += 1
        freq[num] = count + 1
        
    def remove(num: int):
        nonlocal distinct_count
        count = freq.get(num, 0)
        if count == 1:
            distinct_count -= 1
        if count > 0:
            freq[num] = count - 1

    curr_L = 0
    curr_R = -1
    
    for q in queries:
        L, R = q.L, q.R
        
        while curr_R < R:
            curr_R += 1
            add(nums[curr_R])
            
        while curr_R > R:
            remove(nums[curr_R])
            curr_R -= 1
            
        while curr_L > L:
            curr_L -= 1
            add(nums[curr_L])
            
        while curr_L < L:
            remove(nums[curr_L])
            curr_L += 1
            
        result[q.index] = distinct_count
        
    return result


if __name__ == "__main__":
    nums = [1, 1, 2, 1, 3]
    queries = [[0, 4], [0, 1], [1, 4]]
    # Distinct in 0 to 4: {1, 2, 3} -> 3
    # Distinct in 0 to 1: {1} -> 1
    # Distinct in 1 to 4: {1, 2, 3} -> 3
    assert range_distinct_queries(nums, queries) == [3, 1, 3], "Test 1"
    print("All tests passed!")
