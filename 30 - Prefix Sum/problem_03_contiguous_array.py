"""
============================================================
Problem: Contiguous Array (Equal 0s and 1s)
Pattern: Prefix Sum + Hash Map (Transformation)
Difficulty: Medium
LeetCode: #525
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array of 0s and 1s, find the maximum length of a contiguous subarray
with an EQUAL number of 0s and 1s.

APPROACH: Transform and Prefix Sum
---------
Transform all `0`s into `-1`s.
Now, the problem becomes exactly: "Find the maximum size subarray that sums to 0".
We can use the exact same Prefix Sum + Hash Map logic from the previous problem,
with target K = 0.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)
============================================================
"""

from typing import List


def find_max_length(nums: List[int]) -> int:
    prefix_indices: dict[int, int] = {0: -1}
    current_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        # Treat 0 as -1
        current_sum += 1 if num == 1 else -1
        
        # Target sum is 0, so needed_prefix = current_sum - 0 = current_sum
        if current_sum in prefix_indices:
            length = i - prefix_indices[current_sum]
            max_len = max(max_len, length)
        else:
            # Only store first occurrence
            prefix_indices[current_sum] = i

    return max_len


if __name__ == "__main__":
    assert find_max_length([0, 1]) == 2,          "Test 1: [0, 1]"
    assert find_max_length([0, 1, 0]) == 2,       "Test 2: [0, 1] or [1, 0]"
    assert find_max_length([0, 0, 0, 1, 1]) == 4, "Test 3: [0, 0, 1, 1]"
    assert find_max_length([1, 1, 1]) == 0,       "Test 4: impossible"
    print("All tests passed!")
