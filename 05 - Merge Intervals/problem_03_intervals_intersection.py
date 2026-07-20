"""
============================================================
Problem: Intervals Intersection
Pattern: Merge Intervals (Two Pointers)
Difficulty: Medium
Link: https://leetcode.com/problems/interval-list-intersections/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you and your friend both have very busy schedules. You both have a list 
of the times you are working. 
You want to find the EXACT times when BOTH of you are working at the same time.
Since both of your schedules are already sorted in order from morning to night, 
you can just hold them side-by-side!
You look at your first meeting, and your friend's first meeting. 
Is there any overlap? If yes, write down the overlapping time.
Then, whoever's meeting ends FIRST moves on to their next meeting (because their 
current meeting is definitely over and can't overlap with anything else).
You repeat this until one of you runs out of meetings!

APPROACH:
---------
1. Initialize two pointers, `i = 0` (for first list) and `j = 0` (for second list).
2. Loop while `i < len(intervals_a)` and `j < len(intervals_b)`:
   - Check if they overlap. The magical overlap formula is: 
     `start = max(a.start, b.start)`
     `end = min(a.end, b.end)`
     If `start <= end`, they overlap!
   - If they overlap, add `[start, end]` to the result list.
   - Now, we need to advance a pointer. The interval that ENDS FIRST is the one 
     we are completely done with. It cannot possibly intersect with the next 
     interval from the other list. 
   - So, if `a.end < b.end`, `i += 1`. Else, `j += 1`.
3. Return the result list.

COMPLEXITY:
-----------
Time:  O(N + M) — Where N and M are the lengths of the two lists. We scan them simultaneously.
Space: O(N + M) — The maximum possible intersections is proportional to the number of intervals.

EDGE CASES:
-----------
- Edge case 1: One or both lists are empty. Returns empty.
- Edge case 2: Exact boundary touching (e.g., [1, 2] and [2, 3] intersects at [2, 2]). Handled perfectly by the `<=`.
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

def merge(intervals_a: list[Interval], intervals_b: list[Interval]) -> list[Interval]:
    """
    Finds the intersection of two sorted lists of disjoint intervals.
    """
    result: list[Interval] = []
    i: int = 0
    j: int = 0
    
    len_a: int = len(intervals_a)
    len_b: int = len(intervals_b)

    while i < len_a and j < len_b:
        # Find the potential intersection boundary
        start = max(intervals_a[i].start, intervals_b[j].start)
        end = min(intervals_a[i].end, intervals_b[j].end)

        # If they overlap, add to the result
        if start <= end:
            result.append(Interval(start, end))

        # Move the pointer of the interval that ends first
        if intervals_a[i].end < intervals_b[j].end:
            i += 1
        else:
            j += 1

    return result

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [Interval(1, 3), Interval(5, 6), Interval(7, 9)]
    arr2 = [Interval(2, 3), Interval(5, 7)]
    res1 = merge(arr1, arr2)
    assert res1 == [Interval(2, 3), Interval(5, 6), Interval(7, 7)], f"Test 1 failed: {res1}"

    arr3 = [Interval(1, 3), Interval(5, 7), Interval(9, 12)]
    arr4 = [Interval(5, 10)]
    res2 = merge(arr3, arr4)
    assert res2 == [Interval(5, 7), Interval(9, 10)], f"Test 2 failed: {res2}"
    
    # 🔲 Edge cases
    res3 = merge([], [Interval(1, 2)])
    assert res3 == [], "Edge 1: One empty list"
    
    res4 = merge([Interval(1, 2)], [Interval(3, 4)])
    assert res4 == [], "Edge 2: No overlaps"

    print("All tests passed!")
