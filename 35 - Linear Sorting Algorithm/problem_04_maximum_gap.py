"""
============================================================
Problem: Maximum Gap
Pattern: Bucket Sort / Pigeonhole Principle
Difficulty: Hard
LeetCode: #164
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an unsorted array, find the maximum difference between two successive
elements in its SORTED form. You must solve it in O(N) time!
Since we can't sort it normally (which takes O(N log N)), we use Buckets.

APPROACH: Bucket Sort
---------
1. Find the min and max of the array.
2. If we evenly distribute the values, the average gap between numbers is
   `gap = ceil((max - min) / (N - 1))`.
3. The MAXIMUM gap MUST be at least this average `gap`.
4. Therefore, the maximum gap will NEVER happen between two numbers in the SAME bucket.
   It will only happen between the MAX of one bucket and the MIN of the next non-empty bucket!
5. So, create buckets of size `gap`. For each bucket, just keep track of the local
   min and max.
6. Iterate through the buckets and find the max difference between adjacent non-empty buckets.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)
============================================================
"""

from typing import List
import math


def maximum_gap(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
        
    min_val, max_val = min(nums), max(nums)
    if min_val == max_val:
        return 0
        
    n = len(nums)
    # The minimum possible max-gap (Pigeonhole principle)
    gap = math.ceil((max_val - min_val) / (n - 1))
    
    # Store [min, max] for each bucket. None means empty bucket.
    buckets = [[float('inf'), float('-inf')] for _ in range(n)]
    
    # Put numbers into buckets
    for num in nums:
        idx = (num - min_val) // gap
        buckets[idx][0] = min(buckets[idx][0], num)
        buckets[idx][1] = max(buckets[idx][1], num)
        
    max_gap = 0
    prev_max = min_val
    
    # Check gap between adjacent non-empty buckets
    for i in range(n):
        # Skip empty buckets
        if buckets[i][0] == float('inf'):
            continue
            
        # The gap is current bucket's min - previous bucket's max
        max_gap = max(max_gap, buckets[i][0] - prev_max)
        prev_max = buckets[i][1]
        
    return max_gap


if __name__ == "__main__":
    assert maximum_gap([3,6,9,1]) == 3, "Test 1: Sorted is 1,3,6,9"
    assert maximum_gap([10]) == 0,      "Test 2"
    assert maximum_gap([1, 10000000]) == 9999999, "Test 3"
    print("All tests passed!")
