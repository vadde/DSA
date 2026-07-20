"""
============================================================
Problem: My Calendar I
Pattern: Ordered Set
Difficulty: Medium
LeetCode: #729
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You want to book a meeting room. A booking is [start, end).
You cannot book if there is ANY overlap with an existing booking.

APPROACH: Ordered Set (using `bisect` in Python)
---------
Keep the list of bookings sorted by start time.
When a new booking [start, end) comes in:
1. Use Binary Search to find where it should be inserted.
2. Check the booking directly BEFORE it: does it end after our new start? (Overlap!)
3. Check the booking directly AFTER it: does it start before our new end? (Overlap!)
4. If no overlaps, insert it and keep the list sorted.

COMPLEXITY:
-----------
Time:  O(log N) to find, O(N) to insert in Python list (O(log N) in C++/Java TreeSet)
Space: O(N) to store bookings
============================================================
"""

import bisect


class MyCalendar:
    def __init__(self) -> None:
        self.calendar: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        # Find the index where (start, end) would be inserted based on start time
        idx = bisect.bisect_right(self.calendar, (start, end))

        # Check overlap with previous event
        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False

        # Check overlap with next event
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False

        self.calendar.insert(idx, (start, end))
        return True


if __name__ == "__main__":
    cal = MyCalendar()
    assert cal.book(10, 20) is True,   "Test 1: Normal booking"
    assert cal.book(15, 25) is False,  "Test 2: Overlaps [10, 20)"
    assert cal.book(20, 30) is True,   "Test 3: Exactly touches previous end (allowed)"
    print("All tests passed!")
