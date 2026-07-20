"""
============================================================
Problem: Sliding Window Maximum
Pattern: Monotonic Queue
Difficulty: Hard
LeetCode: #239
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a window of size K sliding across an array.
You need to report the MAXIMUM number in that window at each step.
You can't just scan the window every time (that takes O(N*K), too slow).

APPROACH: Monotonic Decreasing Queue
---------
Use a double-ended queue (deque) to store indices.
The queue will ALWAYS be strictly decreasing in values.
Why? If a new giant number walks into the window, all the smaller numbers currently
in the window are useless (they will NEVER be the maximum). So we kick them out!
Also, if the index at the front of the queue is outside our window, we kick it out.
The MAXIMUM for the current window is always at the front of the queue.

COMPLEXITY:
-----------
Time:  O(N) — Each element is pushed and popped at most once.
Space: O(K) — The queue stores at most K elements.
============================================================
"""

from typing import List
from collections import deque


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    result = []
    q: deque[int] = deque()  # stores *indices*
    
    for i, num in enumerate(nums):
        # 1. Remove indices that are out of the current window bounds
        if q and q[0] < i - k + 1:
            q.popleft()
            
        # 2. Remove elements from the BACK that are smaller than the new number.
        # They are useless because the new number is bigger and will stay in the
        # window longer!
        while q and nums[q[-1]] < num:
            q.pop()
            
        # 3. Add the new number's index
        q.append(i)
        
        # 4. If our window has reached size K, add the max (at the front) to result
        if i >= k - 1:
            result.append(nums[q[0]])
            
    return result


if __name__ == "__main__":
    assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7], "Test 1"
    assert max_sliding_window([1], 1) == [1],                          "Test 2"
    assert max_sliding_window([1,-1], 1) == [1, -1],                   "Test 3"
    print("All tests passed!")
