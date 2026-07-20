"""
============================================================
Problem: Binary Subarrays With Sum
Pattern: Prefix Sum + Hash Map
Difficulty: Medium
Link: https://leetcode.com/problems/binary-subarrays-with-sum/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a row of 0s and 1s. Count how many contiguous chunks (subarrays)
add up to exactly a `goal`. Since it's binary, the sum of a subarray equals
the number of 1s in it.

APPROACH:
---------
1. Classic prefix sum + hash map pattern (same as Subarray Sum Equals K).
2. Maintain a running `prefix_sum`.
3. At each position, check if `prefix_sum - goal` has been seen before in
   our hash map. If so, all those previous positions form valid subarrays
   ending here!
4. Increment `count` by that many.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N) for the hash map.

EDGE CASES:
-----------
- goal = 0 → consecutive 0s form valid subarrays.
- All 1s, goal = length → only 1 subarray (the whole array).
- Empty subarrays don't count.
============================================================
"""

from typing import List
from collections import defaultdict


def num_subarrays_with_sum(nums: List[int], goal: int) -> int:
    prefix_count = defaultdict(int)
    prefix_count[0] = 1  # Empty prefix has sum 0
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num
        count += prefix_count[prefix_sum - goal]
        prefix_count[prefix_sum] += 1

    return count


if __name__ == "__main__":
    assert num_subarrays_with_sum([1,0,1,0,1], 2) == 4, "Test 1"
    assert num_subarrays_with_sum([0,0,0,0,0], 0) == 15, "Test 2: all zeros"
    assert num_subarrays_with_sum([1,1,1], 3) == 1, "Test 3: whole array"
    assert num_subarrays_with_sum([1,0,0,1], 1) == 6, "Test 4"
    print("All tests passed!")
