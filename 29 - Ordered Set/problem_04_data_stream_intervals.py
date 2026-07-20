"""
============================================================
Problem: Data Stream as Disjoint Intervals
Pattern: Ordered Set
Difficulty: Hard
LeetCode: #352
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You get numbers one by one: 1, 3, 7, 2, 6...
You need to group them into continuous ranges (intervals).
- After 1: [[1, 1]]
- After 3: [[1, 1], [3, 3]]
- After 7: [[1, 1], [3, 3], [7, 7]]
- After 2: [[1, 3], [7, 7]]  (2 connects 1 and 3!)
- After 6: [[1, 3], [6, 7]]  (6 connects with 7)

APPROACH: Ordered Set (Sorted List of Intervals)
---------
Maintain a sorted list of disjoint intervals.
When a new value comes, binary search (`bisect`) its position.
Merge with the left interval if `val == left.end + 1`.
Merge with the right interval if `val == right.start - 1`.
If it merges with BOTH, combine them into one!

COMPLEXITY:
-----------
Time:  O(N) per add in Python (shifting array), O(log N) in C++ std::set.
Space: O(N)
============================================================
"""

import bisect


class SummaryRanges:
    def __init__(self) -> None:
        self.intervals: list[list[int]] = []

    def addNum(self, value: int) -> None:
        # Create a dummy interval to find insertion point
        idx = bisect.bisect_right(self.intervals, [value, float('inf')])

        # Check if it falls inside the PREVIOUS interval
        if idx > 0 and self.intervals[idx - 1][0] <= value <= self.intervals[idx - 1][1]:
            return

        merge_left = (idx > 0 and self.intervals[idx - 1][1] + 1 == value)
        merge_right = (idx < len(self.intervals) and self.intervals[idx][0] - 1 == value)

        if merge_left and merge_right:
            # Connects left and right intervals
            self.intervals[idx - 1][1] = self.intervals[idx][1]
            self.intervals.pop(idx)
        elif merge_left:
            # Extends left interval
            self.intervals[idx - 1][1] = value
        elif merge_right:
            # Extends right interval backward
            self.intervals[idx][0] = value
        else:
            # Standalone interval
            self.intervals.insert(idx, [value, value])

    def getIntervals(self) -> list[list[int]]:
        return self.intervals


if __name__ == "__main__":
    sr = SummaryRanges()
    sr.addNum(1)
    assert sr.getIntervals() == [[1, 1]]
    sr.addNum(3)
    assert sr.getIntervals() == [[1, 1], [3, 3]]
    sr.addNum(7)
    assert sr.getIntervals() == [[1, 1], [3, 3], [7, 7]]
    sr.addNum(2)
    assert sr.getIntervals() == [[1, 3], [7, 7]]
    sr.addNum(6)
    assert sr.getIntervals() == [[1, 3], [6, 7]]
    print("All tests passed!")
