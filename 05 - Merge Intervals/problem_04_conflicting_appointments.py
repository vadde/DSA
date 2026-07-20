"""
============================================================
Problem: Conflicting Appointments
Pattern: Merge Intervals
Difficulty: Medium
Link: https://leetcode.com/problems/meeting-rooms/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a list of meetings you want to attend today. 
You can only be in one place at a time. If Meeting A is from 1:00 to 3:00, and 
Meeting B is from 2:00 to 4:00, you have a problem! You can't attend both.
If Meeting A ends at exactly 3:00 and Meeting B starts at exactly 3:00, that's fine! 
You can just run out of the first room and into the second room.
To figure out if you can attend ALL the meetings, you just need to sort them 
by start time. Then, look at them one by one. If any meeting starts BEFORE the 
previous meeting finishes, you have a conflict!

APPROACH:
---------
1. Sort the list of intervals based on their start time.
2. Iterate through the intervals starting from the second one (`i = 1`).
3. Check if the current interval starts BEFORE the previous interval ends.
   - `if intervals[i].start < intervals[i - 1].end:`
   - Notice we use `<` and not `<=`. If a meeting ends at 4 and another starts at 4, 
     they do NOT conflict.
4. If a conflict is found, return `False`.
5. If the loop completes without finding any conflicts, return `True`.

COMPLEXITY:
-----------
Time:  O(N log N) — Sorting the intervals is the bottleneck. The loop itself is O(N).
Space: O(N) or O(log N) — Depending on the sorting algorithm's overhead in Python.

EDGE CASES:
-----------
- Edge case 1: Empty list or list with 1 appointment. Returns `True` instantly.
- Edge case 2: Appointments touch boundaries (e.g. `[1, 2], [2, 3]`). Returns `True`.
============================================================
"""

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def can_attend_all_appointments(intervals: list[Interval]) -> bool:
    """
    Determines if a person can attend all given appointments without conflicts.
    """
    if len(intervals) < 2:
        return True

    # 1. Sort the intervals by start time
    intervals.sort(key=lambda x: x.start)

    # 2. Check for any overlap
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            # Overlap found!
            return False

    return True

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    assert can_attend_all_appointments(arr1) == False, "Test 1 failed: Conflict [1,4] and [2,5]"

    arr2 = [Interval(6, 7), Interval(2, 4), Interval(8, 12)]
    assert can_attend_all_appointments(arr2) == True, "Test 2 failed: No conflicts"
    
    # 🔲 Edge cases
    arr3 = [Interval(4, 5), Interval(2, 3), Interval(3, 6)]
    assert can_attend_all_appointments(arr3) == False, "Edge 1: Unsorted conflict"
    
    arr4 = [Interval(1, 2), Interval(2, 3)]
    assert can_attend_all_appointments(arr4) == True, "Edge 2: Touching boundaries are allowed"

    print("All tests passed!")
