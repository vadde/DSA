"""
============================================================
Problem: Partition Array Into Two Arrays to Minimize Sum Difference
Pattern: Meet in the Middle
Difficulty: Hard
LeetCode: #2035
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an array of `2N` integers. You must split them into exactly two arrays
of size `N`. Minimize the absolute difference of their sums.
N <= 15, so 2N <= 30. Total combinations = C(30, 15) = 155 million (A bit too slow!).

APPROACH: Meet in the Middle (Grouping by Size)
---------
1. Target sum for one array is `total_sum // 2`.
2. Split array into `left` and `right` halves (size N each).
3. We must pick `k` elements from `left` and `N - k` elements from `right` to form size N.
4. For both halves, generate all subset sums, GROUPED BY HOW MANY elements are in the subset!
5. Sort the `right` subset sums.
6. For each size `k` in `left`, and for each sum `s` in `left_sums[k]`, we need 
   an element in `right_sums[N - k]` that brings the total close to `target`.
   Use Binary Search!

COMPLEXITY:
-----------
Time:  O(2^N * N)
Space: O(2^N)
============================================================
"""

from typing import List
import bisect
from collections import defaultdict
from itertools import combinations


def minimumDifference(nums: List[int]) -> int:
    n = len(nums) // 2
    left, right = nums[:n], nums[n:]
    total_sum = sum(nums)
    target = total_sum / 2
    
    # Generate all subset sums for a half, grouped by size of subset
    def get_sums_by_length(arr: List[int]) -> dict:
        res = defaultdict(list)
        for k in range(len(arr) + 1):
            for combo in combinations(arr, k):
                res[k].append(sum(combo))
        return res

    left_sums = get_sums_by_length(left)
    right_sums = get_sums_by_length(right)
    
    # Sort the right side for binary searching
    for k in right_sums:
        right_sums[k].sort()
        
    min_diff = float('inf')
    
    # We pick k elements from the left, meaning we must pick n-k from the right
    for k in range(n + 1):
        for s in left_sums[k]:
            needed = target - s
            right_list = right_sums[n - k]
            idx = bisect.bisect_left(right_list, needed)
            
            # Check closest smaller or equal
            if idx < len(right_list):
                current_sum = s + right_list[idx]
                min_diff = min(min_diff, abs(total_sum - 2 * current_sum))
            
            # Check closest strictly smaller
            if idx > 0:
                current_sum = s + right_list[idx - 1]
                min_diff = min(min_diff, abs(total_sum - 2 * current_sum))
                
    return int(min_diff)


if __name__ == "__main__":
    assert minimumDifference([3,9,7,3]) == 2,       "Test 1: [3,9] and [7,3]"
    assert minimumDifference([-36,36]) == 72,       "Test 2: [-36] and [36]"
    assert minimumDifference([2,-1,0,4,-2,-9]) == 0,"Test 3"
    print("All tests passed!")
