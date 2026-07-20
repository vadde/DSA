"""
============================================================
Problem: Merge Intervals
Pattern: Merge Intervals
Difficulty: Medium
Link: https://leetcode.com/problems/merge-intervals/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a calendar with a bunch of meetings scheduled. Some of these 
meetings happen at the exact same time, or they overlap.
If a meeting runs from 1:00 to 3:00, and another runs from 2:00 to 4:00, you are 
busy from 1:00 to 4:00 continuously!
The goal is to take a messy list of meetings and combine the overlapping ones so 
you just have a clean list of "blocks of time you are busy".
The easiest way to do this is to sort all the meetings by their start time. Then, 
you just look at them one by one. If the next meeting starts BEFORE the current 
one ends, you merge them!

APPROACH:
---------
1. Sort the list of intervals based on their START time.
2. Create an empty list called `merged`.
3. Add the very first interval into the `merged` list.
4. For each subsequent interval in the sorted list:
   - Look at the LAST interval you added to the `merged` list (let's call it `last_merged`).
   - If the current interval's start time is <= `last_merged`'s end time, they overlap!
   - Update `last_merged`'s end time to be the MAXIMUM of both end times. (e.g., [1, 5] and [2, 3] merges to [1, 5], not [1, 3]).
   - If they DON'T overlap, just add the current interval to the `merged` list.
5. Return the `merged` list.

COMPLEXITY:
-----------
Time:  O(N log N) — Sorting the intervals takes O(N log N). The merging pass takes O(N).
Space: O(N) — In the worst case (no overlaps), we store all N intervals in the result list.

EDGE CASES:
-----------
- Edge case 1: Empty list of intervals. Returns empty list.
- Edge case 2: Intervals completely swallow other intervals (e.g., `[1, 10]` and `[2, 5]`).
- Edge case 3: Exact touching boundaries (e.g., `[1, 4]` and `[4, 5]`). The problem considers this an overlap.
============================================================
"""

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
        
    def __repr__(self):
        return f"[{self.start}, {self.end}]"

def merge(intervals: list[Interval]) -> list[Interval]:
    """
    Merges all overlapping intervals.
    """
    if len(intervals) < 2:
        return intervals

    # 1. Sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)

    merged: list[Interval] = []
    
    # 2. Add the first interval to our merged list
    merged.append(intervals[0])

    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        last_merged = merged[-1]

        # 3. If they overlap, merge them by updating the end time
        if current_interval.start <= last_merged.end:
            last_merged.end = max(last_merged.end, current_interval.end)
        else:
            # 4. If they don't overlap, just add it to the list
            merged.append(current_interval)

    return merged

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    intervals1 = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    res1 = merge(intervals1)
    assert res1 == [Interval(1, 5), Interval(7, 9)], f"Test 1 failed: {res1}"

    intervals2 = [Interval(6, 7), Interval(2, 4), Interval(5, 9)]
    res2 = merge(intervals2)
    assert res2 == [Interval(2, 4), Interval(5, 9)], f"Test 2 failed: {res2}"
    
    # 🔲 Edge cases
    intervals3 = [Interval(1, 4), Interval(4, 5)]
    res3 = merge(intervals3)
    assert res3 == [Interval(1, 5)], "Edge 1: Touching boundaries"
    
    intervals4 = [Interval(1, 10), Interval(2, 5)]
    res4 = merge(intervals4)
    assert res4 == [Interval(1, 10)], "Edge 2: Swallowed interval"

    print("All tests passed!")
