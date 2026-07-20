"""
============================================================
Problem: Minimum Meeting Rooms
Pattern: Merge Intervals (Min-Heap)
Difficulty: Hard
Link: https://leetcode.com/problems/meeting-rooms-ii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are the manager of a very busy conference center. You have a list of meetings 
happening today, and you want to know the MAXIMUM number of rooms you will need 
open at any single time.
If you sort the meetings by start time, you can process them chronologically.
Every time a meeting starts, you need to check: "Did any previous meeting just finish?"
If a meeting just finished, you can re-use that exact same room!
To quickly know when the "soonest" meeting is finishing, you can use a magic list 
that always keeps the smallest number at the top. This is called a Min-Heap.
You put the END times of active meetings in the Min-Heap. Whenever a new meeting 
starts, if its start time is greater than or equal to the top of the Min-Heap, 
a room is free! Pop it off, and add the new meeting's end time.

APPROACH:
---------
1. Sort the intervals by start time.
2. Create an empty Min-Heap to keep track of the end times of active meetings.
3. Initialize `min_rooms = 0`.
4. Loop through the sorted intervals:
   - While the heap is not empty AND the current meeting starts AFTER (or EXACTLY WHEN) 
     the meeting at the top of the heap ends (`interval.start >= heap[0]`):
     - Pop from the heap. (The room is now free).
   - Push the current meeting's end time onto the heap. (Occupy a room).
   - Update `min_rooms = max(min_rooms, len(heap))`.
5. Return `min_rooms`.

COMPLEXITY:
-----------
Time:  O(N log N) — Sorting takes O(N log N). Pushing/popping from a heap takes O(log N), 
       which happens N times, so the heap operations are also O(N log N).
Space: O(N) — In the worst case (all meetings overlap), the heap stores N end times.

EDGE CASES:
-----------
- Edge case 1: Touching boundaries (e.g., [1, 2] and [2, 3]). `2 >= 2`, so the room is reused.
- Edge case 2: Empty list. Returns 0.
============================================================
"""

import heapq

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def min_meeting_rooms(intervals: list[Interval]) -> int:
    """
    Finds the minimum number of meeting rooms required.
    """
    if not intervals:
        return 0

    # 1. Sort the intervals by start time
    intervals.sort(key=lambda x: x.start)

    min_rooms: int = 0
    min_heap: list[int] = []

    for interval in intervals:
        # Remove all meetings that have ended by the time the current meeting starts
        while min_heap and interval.start >= min_heap[0]:
            heapq.heappop(min_heap)

        # Add the current meeting's end time to the heap
        heapq.heappush(min_heap, interval.end)

        # The size of the heap is the number of active meetings right now!
        min_rooms = max(min_rooms, len(min_heap))

    return min_rooms

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    assert min_meeting_rooms(arr1) == 2, "Test 1 failed: Needs 2 rooms for [1,4] and [2,5]"

    arr2 = [Interval(6, 7), Interval(2, 4), Interval(8, 12)]
    assert min_meeting_rooms(arr2) == 1, "Test 2 failed: No overlaps, needs 1 room"

    arr3 = [Interval(1, 4), Interval(2, 3), Interval(3, 6)]
    assert min_meeting_rooms(arr3) == 2, "Test 3 failed: [1,4] overlaps with [2,3], then [3,6] reuses [2,3]'s room"
    
    arr4 = [Interval(4, 5), Interval(2, 3), Interval(2, 4), Interval(3, 5)]
    assert min_meeting_rooms(arr4) == 2, "Test 4 failed"

    # 🔲 Edge cases
    assert min_meeting_rooms([]) == 0, "Edge 1: Empty list"
    assert min_meeting_rooms([Interval(1, 2), Interval(2, 3)]) == 1, "Edge 2: Exact boundary touching"

    print("All tests passed!")
