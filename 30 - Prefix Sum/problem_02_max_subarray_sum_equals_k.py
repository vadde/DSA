"""
============================================================
Problem: Maximum Size Subarray Sum Equals K
Pattern: Prefix Sum + Hash Map
Difficulty: Medium
LeetCode: #325
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Similar to "Subarray Sum Equals K", but instead of COUNTING how many,
we want the LENGTH of the longest subarray that sums to K.

APPROACH: Prefix Sum + Hash Map (storing INDICES)
---------
Keep a running total (`current_sum`).
If `current_sum - K` exists in the Hash Map, we found a valid subarray.
To get the MAXIMUM length, we want the EARLIEST time we saw `current_sum - K`.
So we store `{prefix_sum: first_seen_index}` in the Hash Map.
Initialize with `{0: -1}` so a prefix starting at index 0 works correctly.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)
============================================================
"""

from typing import List


def max_sub_array_len(nums: List[int], k: int) -> int:
    prefix_indices: dict[int, int] = {0: -1}
    current_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        current_sum += num
        needed_prefix = current_sum - k

        if needed_prefix in prefix_indices:
            length = i - prefix_indices[needed_prefix]
            max_len = max(max_len, length)

        # Only store the FIRST time we see a prefix sum to maximize length later
        if current_sum not in prefix_indices:
            prefix_indices[current_sum] = i

    return max_len


if __name__ == "__main__":
    assert max_sub_array_len([1, -1, 5, -2, 3], 3) == 4, "Test 1: [1, -1, 5, -2]"
    assert max_sub_array_len([-2, -1, 2, 1], 1) == 2,    "Test 2: [-1, 2]"
    assert max_sub_array_len([1, 1, 1], 5) == 0,         "Test 3: not possible"
    print("All tests passed!")
