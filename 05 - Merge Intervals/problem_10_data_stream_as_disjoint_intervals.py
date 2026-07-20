"""
============================================================
Problem: Data Stream as Disjoint Intervals
Pattern: Merge Intervals (Dynamic Insertion)
Difficulty: Hard
Link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you are building a jigsaw puzzle, but someone is handing you pieces one 
by one. Each piece has a number. If someone hands you piece 1, you put it down.
If someone hands you piece 3, you put it down. Right now you have `[1, 1]` and `[3, 3]`.
If someone then hands you piece 2, suddenly all three pieces connect! You can merge 
them all together to say you have a solid block from `[1, 3]`.
Because pieces are handed to you one by one, you need a fast way to slot a piece 
into the correct place in your sorted list, and then just check if it connects to 
its immediate left or right neighbors.

APPROACH:
---------
Since the integers arrive as a stream, we can't afford to re-sort the entire list 
every single time.
1. Maintain a sorted list of disjoint intervals.
2. When a new `value` arrives, use Binary Search to find its exact insertion position.
   - If the value is already inside one of the existing intervals, ignore it!
3. Insert `[value, value]` at the found index. (This takes O(N) in a Python list).
4. After insertion, check the newly inserted interval against its immediate LEFT neighbor.
   - If `left_neighbor.end + 1 == new_interval.start`, they connect! Merge them.
5. Check the newly merged interval against its immediate RIGHT neighbor.
   - If `merged_interval.end + 1 == right_neighbor.start`, they connect! Merge them.
   
By doing this, we keep the list perfectly compressed and sorted at all times.

COMPLEXITY:
-----------
Time:  O(N) per `addNum` — Binary search is O(log N), but list insertion is O(N).
       O(1) per `getIntervals` — Just return the list.
Space: O(N) — To store the disjoint intervals.

EDGE CASES:
-----------
- Edge case 1: Duplicate numbers in the stream. Handled by the binary search check.
- Edge case 2: Numbers connecting multiple separate blocks simultaneously. Handled by merging left, then right.
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

class SummaryRanges:
    def __init__(self):
        self.intervals: list[Interval] = []

    def addNum(self, value: int) -> None:
        # Binary search to find the correct insertion index
        left, right = 0, len(self.intervals) - 1
        
        while left <= right:
            mid = (left + right) // 2
            interval = self.intervals[mid]
            
            # If the value is already completely inside an existing interval, do nothing
            if interval.start <= value <= interval.end:
                return
            elif interval.start > value:
                right = mid - 1
            else:
                left = mid + 1
                
        # Insert the new interval at the found position
        idx = left
        self.intervals.insert(idx, Interval(value, value))
        
        # Merge with the left neighbor if they connect
        if idx > 0 and self.intervals[idx - 1].end + 1 == self.intervals[idx].start:
            self.intervals[idx - 1].end = self.intervals[idx].end
            self.intervals.pop(idx)
            idx -= 1  # The active interval shifted one spot left
            
        # Merge with the right neighbor if they connect
        if idx < len(self.intervals) - 1 and self.intervals[idx].end + 1 == self.intervals[idx + 1].start:
            self.intervals[idx].end = self.intervals[idx + 1].end
            self.intervals.pop(idx + 1)

    def getIntervals(self) -> list[Interval]:
        return self.intervals

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    sr = SummaryRanges()
    
    sr.addNum(1)
    assert sr.getIntervals() == [Interval(1, 1)]
    
    sr.addNum(3)
    assert sr.getIntervals() == [Interval(1, 1), Interval(3, 3)]
    
    sr.addNum(7)
    assert sr.getIntervals() == [Interval(1, 1), Interval(3, 3), Interval(7, 7)]
    
    sr.addNum(2) # Connects 1 and 3!
    assert sr.getIntervals() == [Interval(1, 3), Interval(7, 7)]
    
    sr.addNum(6) # Connects to 7
    assert sr.getIntervals() == [Interval(1, 3), Interval(6, 7)]
    
    sr.addNum(6) # Duplicate, should do nothing
    assert sr.getIntervals() == [Interval(1, 3), Interval(6, 7)]

    print("All tests passed!")
