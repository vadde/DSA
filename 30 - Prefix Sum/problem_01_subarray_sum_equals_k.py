"""
============================================================
Problem: Subarray Sum Equals K
Pattern: Prefix Sum + Hash Map
Difficulty: Medium
LeetCode: #560
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array (with positive AND negative numbers) and a target K.
Find how many continuous subarrays add up exactly to K.
Because of negative numbers, we CANNOT use Sliding Window.

APPROACH: Prefix Sum + Hash Map
---------
Keep a running total (`current_sum`).
If a subarray ending here sums to K, then the prefix sum BEFORE this subarray
must be `current_sum - K`.
We use a Hash Map to store how many times we've seen each prefix sum.
Initialize map with {0: 1} to handle the case where a prefix itself exactly equals K.

COMPLEXITY:
-----------
Time:  O(N) — One pass.
Space: O(N) — Hash map storage.
============================================================
"""

from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    prefix_counts: dict[int, int] = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        needed_prefix = current_sum - k
        
        if needed_prefix in prefix_counts:
            count += prefix_counts[needed_prefix]
            
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count


if __name__ == "__main__":
    assert subarray_sum([1, 1, 1], 2) == 2,      "Test 1"
    assert subarray_sum([1, 2, 3], 3) == 2,      "Test 2: [1,2] and [3]"
    assert subarray_sum([-1, -1, 1], 0) == 1,    "Test 3: [-1, 1]"
    assert subarray_sum([1, -1, 0], 0) == 3,     "Test 4: [1,-1], [1,-1,0], [0]"
    print("All tests passed!")
