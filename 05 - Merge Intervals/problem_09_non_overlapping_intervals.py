"""
============================================================
Problem: Non-overlapping Intervals
Pattern: Merge Intervals (Greedy End-Time Sort)
Difficulty: Medium
Link: https://leetcode.com/problems/non-overlapping-intervals/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bunch of meetings scheduled, but you realize that a lot of them overlap!
You want to cancel the FEWEST number of meetings possible so that none of the 
remaining meetings overlap.
To cancel the fewest meetings, we want to KEEP the most meetings.
How do we fit the most meetings into a day? We always choose the meeting that 
FINISHES the earliest! By finishing early, it leaves the rest of the day wide 
open for more meetings.
So, we sort the meetings by their END time. 
We attend the first meeting. If the next meeting overlaps with the one we are 
attending, we just skip it (cancel it). If it doesn't overlap, we attend it!

APPROACH:
---------
1. Sort the intervals by their END time.
2. Initialize `removed_count = 0`.
3. Set `current_end = intervals[0].end`. This is the end time of the meeting we are attending.
4. Loop through the remaining intervals:
   - If the next interval starts BEFORE our current meeting ends 
     (`interval.start < current_end`):
     - This is a conflict! Since we sorted by end time, the current meeting we 
       chose finishes earlier or at the same time as this conflicting one. 
       So we keep the current one and CANCEL the conflicting one.
     - `removed_count += 1`
   - Else (the next interval starts exactly when or after our current meeting ends):
     - No conflict! We attend this new meeting.
     - Update `current_end = interval.end`
5. Return `removed_count`.

COMPLEXITY:
-----------
Time:  O(N log N) — Sorting by end time takes O(N log N). The loop takes O(N).
Space: O(N) or O(log N) — Depending on Python's sort overhead.

EDGE CASES:
-----------
- Edge case 1: Empty list. Returns 0.
- Edge case 2: Exactly touching boundaries (e.g. `[1, 2]` and `[2, 3]`). These do NOT overlap.
============================================================
"""

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def erase_overlap_intervals(intervals: list[Interval]) -> int:
    """
    Finds the minimum number of intervals to remove to make the rest non-overlapping.
    """
    if not intervals:
        return 0

    # 1. Sort the intervals by END time (Greedy strategy)
    intervals.sort(key=lambda x: x.end)

    removed_count: int = 0
    current_end: int = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]

        # 2. Check for overlap
        if interval.start < current_end:
            # Overlap! We remove this interval.
            removed_count += 1
        else:
            # No overlap! We keep it and update our current end time.
            current_end = interval.end

    return removed_count

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [Interval(1, 2), Interval(2, 3), Interval(3, 4), Interval(1, 3)]
    assert erase_overlap_intervals(arr1) == 1, "Test 1 failed: Remove [1,3]"

    arr2 = [Interval(1, 2), Interval(1, 2), Interval(1, 2)]
    assert erase_overlap_intervals(arr2) == 2, "Test 2 failed: Keep one [1,2], remove others"
    
    # 🔲 Edge cases
    arr3 = [Interval(1, 2), Interval(2, 3)]
    assert erase_overlap_intervals(arr3) == 0, "Edge 1: Touching boundaries don't overlap"
    
    assert erase_overlap_intervals([]) == 0, "Edge 2: Empty list"

    print("All tests passed!")
