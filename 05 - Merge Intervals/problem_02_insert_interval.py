"""
============================================================
Problem: Insert Interval
Pattern: Merge Intervals
Difficulty: Medium
Link: https://leetcode.com/problems/insert-interval/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you already have a perfectly sorted, clean list of meeting times where 
none of them overlap. 
Suddenly, your boss tells you to schedule a brand new meeting right in the middle 
of the day. This new meeting might overlap with one existing meeting, or maybe 
five of them! 
Since the list is already sorted, we don't need to sort it again from scratch.
We can just walk through the list and do three things:
1. Walk past all the meetings that end BEFORE the new meeting starts. (Leave them alone).
2. For all the meetings that OVERLAP with the new meeting, swallow them up into 
   one giant meeting! (Merge them into the new meeting).
3. Walk past all the remaining meetings that start AFTER the giant new meeting 
   ends. (Leave them alone).

APPROACH:
---------
1. Initialize a `merged` list and a counter `i = 0`.
2. Skip and add all intervals that come completely BEFORE the `new_interval`:
   `while i < len(intervals) and intervals[i].end < new_interval.start`
3. Merge all intervals that OVERLAP with the `new_interval`:
   `while i < len(intervals) and intervals[i].start <= new_interval.end`
   - Update `new_interval.start = min(intervals[i].start, new_interval.start)`
   - Update `new_interval.end = max(intervals[i].end, new_interval.end)`
   - Increment `i`.
   - After this loop, add the newly bloated `new_interval` to `merged`.
4. Add all the remaining intervals that come completely AFTER:
   `while i < len(intervals)`
5. Return the `merged` list.

COMPLEXITY:
-----------
Time:  O(N) — We only pass through the list exactly once. No sorting needed!
Space: O(N) — We return a new list containing up to N+1 intervals.

EDGE CASES:
-----------
- Edge case 1: The original list is empty. Just return `[new_interval]`.
- Edge case 2: The new interval swallows EVERY interval in the list.
- Edge case 3: The new interval is at the very beginning or very end without overlapping.
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

def insert(intervals: list[Interval], new_interval: Interval) -> list[Interval]:
    """
    Inserts a new interval into a sorted list of non-overlapping intervals,
    merging any overlapping intervals.
    """
    merged: list[Interval] = []
    i: int = 0
    n: int = len(intervals)

    # 1. Skip (and add to output) all intervals that end BEFORE the new_interval starts
    while i < n and intervals[i].end < new_interval.start:
        merged.append(intervals[i])
        i += 1

    # 2. Merge all intervals that OVERLAP with the new_interval
    while i < n and intervals[i].start <= new_interval.end:
        new_interval.start = min(intervals[i].start, new_interval.start)
        new_interval.end = max(intervals[i].end, new_interval.end)
        i += 1
    
    # Insert the newly merged interval
    merged.append(new_interval)

    # 3. Add all the remaining intervals to the output
    while i < n:
        merged.append(intervals[i])
        i += 1

    return merged

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    intervals1 = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    res1 = insert(intervals1, Interval(4, 6))
    assert res1 == [Interval(1, 3), Interval(4, 7), Interval(8, 12)], "Test 1 failed"

    intervals2 = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    res2 = insert(intervals2, Interval(4, 10))
    assert res2 == [Interval(1, 3), Interval(4, 12)], "Test 2 failed"
    
    # 🔲 Edge cases
    res3 = insert([], Interval(1, 2))
    assert res3 == [Interval(1, 2)], "Edge 1: Empty list"
    
    intervals4 = [Interval(2, 3), Interval(5, 7)]
    res4 = insert(intervals4, Interval(1, 10))
    assert res4 == [Interval(1, 10)], "Edge 2: New interval swallows all"

    print("All tests passed!")
