"""
============================================================
Problem: Sliding Window Maximum
Pattern: Sliding Window (Advanced: Monotonic Deque)
Difficulty: Hard
Link: https://leetcode.com/problems/sliding-window-maximum/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you are looking at a line of kids of different heights through a small window
that only shows K kids at a time. As you slide the window from left to right, you want
to write down the height of the tallest kid you can see in the window at each step.
The tricky part is: when the tallest kid steps out of the left side of your window,
how do you quickly know who the *second* tallest kid was?

APPROACH (Monotonic Deque):
---------------------------
We use a double-ended queue (deque) to store the *indices* of the array elements.
We maintain a strict rule (a monotonic invariant): the elements in our deque must
always be in DECREASING order of their values.

1. INITIALIZE: `result = []`, `window_start = 0`, and `dq = deque()`.
2. EXPAND: iterate `window_end` from 0 to len(nums)-1.
3. Before adding the current element (`nums[window_end]`) to the deque:
   a. POP from the BACK of the deque as long as the current element is GREATER than or 
      EQUAL to the element at the back. (Why? Because those smaller elements can NEVER 
      be the maximum in any future window since our current element is both bigger and 
      arrived later).
   b. APPEND `window_end` to the back of the deque.
4. SHRINK: If the index at the FRONT of the deque is out of bounds (i.e., `< window_start`),
   POP it from the FRONT.
5. RECORD: Once our window has hit size K (i.e., `window_end >= k - 1`), the maximum
   for this window is guaranteed to be at the FRONT of the deque.
   a. Append `nums[dq[0]]` to `result`.
   b. Increment `window_start`.
6. RETURN `result`.

COMPLEXITY:
-----------
Time:  O(N) — Every element is pushed to the deque exactly once and popped at most once.
Space: O(K) — The deque stores at most K elements (the size of the window).

EDGE CASES:
-----------
- Edge case 1: K is 1. The result is just the original array.
- Edge case 2: Array is smaller than K. Though normally constrained, handle gracefully.
============================================================
"""

from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """
    Return the maximum sliding window of size K.
    """
    if not nums or k == 0:
        return []
    
    if k == 1:
        return nums

    result: list[int] = []
    dq: deque[int] = deque()
    window_start: int = 0

    for window_end in range(len(nums)):
        # Remove elements from the back that are smaller than the current element.
        # They are useless because the current element is larger and will stay in the window longer.
        while dq and nums[dq[-1]] <= nums[window_end]:
            dq.pop()
        
        # Add the current element's index to the deque
        dq.append(window_end)

        # If the window has reached size K, we need to record the max and slide
        if window_end >= k - 1:
            # The largest element in the current window is always at the front of the deque
            result.append(nums[dq[0]])
            
            # Remove the front element if it's falling out of the window as we slide left boundary
            if dq[0] == window_start:
                dq.popleft()
            
            # Slide the window forward
            window_start += 1

    return result


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7], "Test 1 failed"
    assert max_sliding_window([7,2,4], 2) == [7,4], "Test 2 failed"
    
    # 🔲 Edge cases
    assert max_sliding_window([1], 1) == [1], "Edge 1: single element"
    assert max_sliding_window([8, 7, 6, 5, 4, 3], 2) == [8, 7, 6, 5, 4], "Edge 2: strictly decreasing"
    assert max_sliding_window([1, 2, 3, 4, 5, 6], 2) == [2, 3, 4, 5, 6], "Edge 3: strictly increasing"
    assert max_sliding_window([1,-1], 1) == [1,-1], "Edge 4: K=1"

    print("All tests passed!")
