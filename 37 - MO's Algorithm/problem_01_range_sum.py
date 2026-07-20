"""
============================================================
Problem: Range Sum Query (MO's Algorithm Intro)
Pattern: MO's Algorithm
Difficulty: Medium
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an array and a bunch of queries `[L, R]`.
For each query, you need to find the sum of elements from index L to R.
(Yes, Prefix Sum does this in O(1), but we are doing this to illustrate
how the MO's sliding window pointers work before we do harder problems!)

APPROACH: MO's Algorithm
---------
1. Break the array into blocks of size `sqrt(N)`.
2. Sort the queries. Primary key: `L // block_size`. Secondary key: `R`.
3. Keep a `current_sum`, and `curr_L`, `curr_R` pointers.
4. For each query, `add()` elements by expanding the window, and `remove()`
   elements by shrinking the window until it matches the query's `L` and `R`.

COMPLEXITY:
-----------
Time:  O(Q log Q + Q * sqrt(N))
Space: O(Q)
============================================================
"""

from typing import List
import math


class Query:
    def __init__(self, L: int, R: int, index: int):
        self.L = L
        self.R = R
        self.index = index


def range_sum_queries(nums: List[int], queries_input: List[List[int]]) -> List[int]:
    n = len(nums)
    if n == 0:
        return []
        
    block_size = int(math.sqrt(n))
    
    queries = [Query(q[0], q[1], i) for i, q in enumerate(queries_input)]
    
    # Sort queries according to MO's logic
    queries.sort(key=lambda q: (q.L // block_size, q.R))
    
    result = [0] * len(queries)
    
    curr_L = 0
    curr_R = -1
    current_sum = 0
    
    for q in queries:
        L, R = q.L, q.R
        
        # Add elements if current window is too small on the right
        while curr_R < R:
            curr_R += 1
            current_sum += nums[curr_R]
            
        # Remove elements if current window is too large on the right
        while curr_R > R:
            current_sum -= nums[curr_R]
            curr_R -= 1
            
        # Add elements if current window is too small on the left
        while curr_L > L:
            curr_L -= 1
            current_sum += nums[curr_L]
            
        # Remove elements if current window is too large on the left
        while curr_L < L:
            current_sum -= nums[curr_L]
            curr_L += 1
            
        result[q.index] = current_sum
        
    return result


if __name__ == "__main__":
    nums = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    queries = [[0, 4], [1, 3], [2, 4]]
    # Sums:
    # 0 to 4: 1+1+2+1+3 = 8
    # 1 to 3: 1+2+1 = 4
    # 2 to 4: 2+1+3 = 6
    assert range_sum_queries(nums, queries) == [8, 4, 6], "Test 1"
    print("All tests passed!")
