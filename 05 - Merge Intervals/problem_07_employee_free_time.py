"""
============================================================
Problem: Employee Free Time
Pattern: Merge Intervals
Difficulty: Hard
Link: https://leetcode.com/problems/employee-free-time/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a team of 3 people. Each person gives you a list of the times 
they are busy working today. 
You want to schedule a team-building pizza party, which means you need to find 
all the times when EVERYONE is free!
Since everyone is free when NO ONE is working, this is the exact opposite of the 
"Merge Intervals" problem. 
If we take EVERY single working shift from ALL employees, dump them into a big pile, 
and sort them from morning to night, we just need to look for the "GAPS" between shifts!
If the latest time anyone has worked so far is 3:00, and the next person doesn't 
start working until 4:00, then from 3:00 to 4:00, the whole team is free!

APPROACH:
---------
1. Flatten the list of lists into a single list of all intervals from all employees.
2. Sort all intervals by their start time.
3. Keep track of the `max_end` time we've seen so far. (Initialize it to the first interval's end time).
4. Iterate through the sorted intervals (starting from the second one):
   - If the current interval's start time is GREATER than `max_end`, we found a gap!
     Add `[max_end, current_interval.start]` to the result list.
   - Update `max_end = max(max_end, current_interval.end)` because we might have overlapping shifts.
5. Return the result list.

COMPLEXITY:
-----------
Time:  O(N log N) — Where N is the total number of intervals across all employees. Sorting takes O(N log N).
Space: O(N) — To store the flattened list and the resulting gaps.

EDGE CASES:
-----------
- Edge case 1: Only one employee. Their free time is before and after their shifts, but usually problems only want finite intervals between working hours.
- Edge case 2: Everyone works exactly the same hours. No free time between shifts.
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

def find_employee_free_time(schedule: list[list[Interval]]) -> list[Interval]:
    """
    Finds the finite intervals of free time common to all employees.
    """
    # 1. Flatten the schedule
    all_intervals: list[Interval] = []
    for employee in schedule:
        all_intervals.extend(employee)

    if not all_intervals:
        return []

    # 2. Sort by start time
    all_intervals.sort(key=lambda x: x.start)

    free_time: list[Interval] = []
    
    # 3. Track the maximum end time seen so far
    max_end: int = all_intervals[0].end

    # 4. Find the gaps
    for i in range(1, len(all_intervals)):
        current = all_intervals[i]

        if current.start > max_end:
            # We found a gap where no one is working!
            free_time.append(Interval(max_end, current.start))
        
        # Always update the max_end
        max_end = max(max_end, current.end)

    return free_time

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    sched1 = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    res1 = find_employee_free_time(sched1)
    assert res1 == [Interval(3, 5)], f"Test 1 failed: {res1}"

    sched2 = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    res2 = find_employee_free_time(sched2)
    assert res2 == [Interval(4, 6), Interval(8, 9)], f"Test 2 failed: {res2}"
    
    # 🔲 Edge cases
    sched3 = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    res3 = find_employee_free_time(sched3)
    assert res3 == [Interval(5, 7)], "Edge 1: Overlapping chain"

    print("All tests passed!")
