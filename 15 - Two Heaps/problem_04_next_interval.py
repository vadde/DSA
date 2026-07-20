"""
============================================================
Problem: Next Interval
Pattern: Two Heaps
Difficulty: Hard (Advanced)
Link: https://leetcode.com/problems/find-right-interval/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bunch of meetings (intervals) with a Start time and an End time.
For EVERY meeting, you want to find the "Next Meeting". 
The "Next Meeting" is the meeting that starts right after your current meeting 
ends. If there are multiple meetings that start after yours ends, you want the 
one that starts the SOONEST!
If we just compare every meeting to every other meeting, it takes way too long (O(N^2)).

So we use Two Sorting Hats (Heaps)!
1. A Max Heap that sorts all meetings by their END time.
2. A Max Heap that sorts all meetings by their START time.

We pull out the meeting that Ends the ABSOLUTE LATEST. 
Then we look at the Start Hat. We pull out ALL meetings that start after this 
latest end time.
The very last one we pull out before the start time becomes too early is our 
"Next Meeting"! We record its index.
But wait! What about the meeting that Ends the SECOND latest?
Since its end time is earlier, the "Next Meeting" we just found for the latest 
meeting might also be the "Next Meeting" for this one too! So we just throw 
that ONE meeting back into the Start Hat so it can be reused.

APPROACH:
---------
1. Initialize `max_end_heap` and `max_start_heap`.
2. Push all intervals into the heaps. 
   - `max_end_heap`: push `(-end_time, index)`
   - `max_start_heap`: push `(-start_time, index)`
3. Create a `result` array initialized to `-1` for all intervals.
4. Loop `N` times (for every interval):
   - Pop `(end_time, end_idx)` from `max_end_heap`.
   - Initialize `best_start_idx = -1` and `best_start_time = 0`.
   - While `max_start_heap` is not empty AND its top `start_time` is `>= end_time`:
     - Pop `(start_time, start_idx)` from `max_start_heap`.
     - Update `best_start_idx = start_idx` and `best_start_time = start_time`.
   - If we found a valid `best_start_idx`:
     - Set `result[end_idx] = best_start_idx`.
     - PUSH the `best_start_time` back into the `max_start_heap`! Why? Because 
       the next `end_time` we pop will be smaller or equal to the current one. 
       This means our `best_start_time` is absolutely guaranteed to still be 
       `>=` the next `end_time`, and could be its closest answer too! We don't 
       need to push the other popped start times back, because they are larger 
       and thus less optimal.
5. Return `result`.

COMPLEXITY:
-----------
Time:  O(N log N) — Every element is pushed/popped from the heap at most twice.
Space: O(N) — Heaps store N elements.

EDGE CASES:
-----------
- Edge case 1: Single interval. Loop will just leave the result as `[-1]`.
============================================================
"""

import heapq
from typing import List

def find_right_interval(intervals: List[List[int]]) -> List[int]:
    """
    Returns an array of the next interval indices for each interval.
    """
    n = len(intervals)
    max_end_heap = []
    max_start_heap = []
    
    # 1. Populate the heaps
    for i in range(n):
        # Python uses Min Heaps, so we push negative values to simulate Max Heaps
        start, end = intervals[i]
        heapq.heappush(max_start_heap, (-start, i))
        heapq.heappush(max_end_heap, (-end, i))
        
    result = [-1] * n
    
    # 2. Process from the latest ending interval to the earliest
    for _ in range(n):
        top_end, end_idx = heapq.heappop(max_end_heap)
        
        # Un-negate the end time
        top_end = -top_end
        
        best_start_idx = -1
        best_start_time = 0
        
        # 3. Find the smallest start time that is >= top_end
        # Because it's a Max Heap, we just keep popping all start times >= top_end.
        # The very last one we pop will be the smallest one!
        while max_start_heap and -max_start_heap[0][0] >= top_end:
            start_time, start_idx = heapq.heappop(max_start_heap)
            best_start_idx = start_idx
            best_start_time = start_time
            
        # 4. If we found a match, record it
        if best_start_idx != -1:
            result[end_idx] = best_start_idx
            # Push it back! The next end time will be smaller, so this start time
            # might be the perfect match for it as well!
            heapq.heappush(max_start_heap, (best_start_time, best_start_idx))
            
    return result

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    intervals1 = [[3,4], [2,3], [1,2]]
    # Next for [3,4] is None (-1)
    # Next for [2,3] is [3,4] (index 0)
    # Next for [1,2] is [2,3] (index 1)
    assert find_right_interval(intervals1) == [-1, 0, 1], "Test 1 failed"

    intervals2 = [[1,4], [2,3], [3,4]]
    # Next for [1,4] is None (-1)
    # Next for [2,3] is [3,4] (index 2)
    # Next for [3,4] is None (-1)
    assert find_right_interval(intervals2) == [-1, 2, -1], "Test 2 failed"

    # 🔲 Edge cases
    assert find_right_interval([[1,2]]) == [-1], "Edge 1: Single interval"

    print("All tests passed!")
