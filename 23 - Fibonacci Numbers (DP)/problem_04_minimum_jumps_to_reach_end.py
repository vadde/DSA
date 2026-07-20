"""
============================================================
Problem: Minimum Jumps to Reach the End
Pattern: Fibonacci Numbers (DP)
Difficulty: Medium
LeetCode: #45 (Jump Game II)
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Array of non-negative integers. Each element = max jump length from that index.
Find the MINIMUM number of jumps to reach the last index.

APPROACH: Greedy BFS (O(N) optimal)
---------
Think of it like BFS levels:
- curr_end = how far we can reach with current # of jumps
- farthest = the farthest we've seen so far
When we reach curr_end, we must take one more jump → increment jumps, update curr_end.

COMPLEXITY: O(N) time, O(1) space.
============================================================
"""

from typing import List


def jump(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0
    jumps = 0
    curr_end = 0
    farthest = 0
    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = farthest
            if curr_end >= n - 1:
                break
    return jumps


if __name__ == "__main__":
    assert jump([2, 3, 1, 1, 4]) == 2, "Test 1"
    assert jump([2, 3, 0, 1, 4]) == 2, "Test 2"
    assert jump([1]) == 0,             "Edge: single element"
    assert jump([1, 2]) == 1,          "Edge: two elements"
    assert jump([1, 1, 1, 1]) == 3,    "Test 3"
    print("All tests passed!")
