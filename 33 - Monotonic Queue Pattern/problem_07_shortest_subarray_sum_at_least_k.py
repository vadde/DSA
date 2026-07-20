"""
============================================================
Problem: Shortest Subarray with Sum at Least K
Pattern: Monotonic Queue + Prefix Sum
Difficulty: Hard
Link: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Find the shortest contiguous block of numbers that adds up to at least K.
Because numbers can be NEGATIVE, a simple Sliding Window doesn't work (adding
a number might decrease the sum). We need a Monotonic Queue with Prefix Sums!

APPROACH:
---------
1. Compute prefix sums. A subarray from i to j has sum `P[j] - P[i]`.
2. We want `P[j] - P[i] >= K` with the smallest `j - i`.
3. Use a monotonic increasing deque of indices for the prefix sums.
4. For each `j`:
   - While `P[j] - P[deque[0]] >= K`, we found a valid subarray! Record its length, 
     then pop it from the front (we don't need it again because any future `j` would
     result in a LONGER subarray).
   - While `P[j] <= P[deque[-1]]`, pop from the back. (A larger prefix sum that 
     comes earlier is strictly worse: it makes it harder to reach K, and even if it 
     does, the subarray would be longer).
   - Push `j` to the deque.

COMPLEXITY:
-----------
Time:  O(N) - each index is pushed and popped at most once.
Space: O(N) - for prefix sums and deque.

EDGE CASES:
-----------
- No such subarray exists -> return -1.
- K is negative (though problem usually bounds K >= 1).
- Array contains large negative numbers.
============================================================
"""

from typing import List
from collections import deque

def shortestSubarray(nums: List[int], k: int) -> int:
    n = len(nums)
    P = [0] * (n + 1)
    for i in range(n):
        P[i + 1] = P[i] + nums[i]
        
    dq = deque()
    shortest = float('inf')
    
    for y in range(n + 1):
        # Found a valid window
        while dq and P[y] - P[dq[0]] >= k:
            shortest = min(shortest, y - dq.popleft())
            
        # Maintain monotonic increasing deque
        while dq and P[y] <= P[dq[-1]]:
            dq.pop()
            
        dq.append(y)
        
    return shortest if shortest != float('inf') else -1

if __name__ == "__main__":
    assert shortestSubarray([1], 1) == 1, "Test 1"
    assert shortestSubarray([1, 2], 4) == -1, "Test 2"
    assert shortestSubarray([2, -1, 2], 3) == 3, "Test 3"
    assert shortestSubarray([84, -37, 32, 40, 95], 167) == 3, "Test 4"
    print("All tests passed!")
