"""
============================================================
Problem: My Calendar II
Pattern: Ordered Set (Sweep Line variation)
Difficulty: Medium
LeetCode: #731
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You can double-book a room (2 people at the same time), but you CANNOT
triple-book it (3 people at the same time).

APPROACH: Overlaps List
---------
Maintain two lists:
1. `calendar`: all bookings.
2. `overlaps`: all regions where double bookings happen.
When a new booking comes:
1. First, check if it overlaps with anything in `overlaps`. If yes, it's a TRIPLE booking! Return False.
2. If safe, find overlaps with `calendar` and add them to `overlaps`.
3. Add the booking to `calendar`.

COMPLEXITY:
-----------
Time:  O(N) per booking.
Space: O(N)
============================================================
"""


class MyCalendarTwo:
    def __init__(self) -> None:
        self.calendar: list[tuple[int, int]] = []
        self.overlaps: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        # 1. Check if it overlaps with any existing double bookings (making it a triple)
        for o_start, o_end in self.overlaps:
            if max(start, o_start) < min(end, o_end):
                return False

        # 2. Find overlaps with single bookings and add to overlaps list
        for c_start, c_end in self.calendar:
            overlap_start = max(start, c_start)
            overlap_end = min(end, c_end)
            if overlap_start < overlap_end:
                self.overlaps.append((overlap_start, overlap_end))

        # 3. Add to single bookings
        self.calendar.append((start, end))
        return True


if __name__ == "__main__":
    cal = MyCalendarTwo()
    assert cal.book(10, 20) is True,   "Test 1: 1st booking"
    assert cal.book(50, 60) is True,   "Test 2: 2nd booking (no overlap)"
    assert cal.book(10, 40) is True,   "Test 3: Double booking [10, 20)"
    assert cal.book(5, 15) is False,   "Test 4: Triple booking [10, 15)!"
    assert cal.book(5, 10) is True,    "Test 5: Valid, touches [10, 20)"
    assert cal.book(25, 55) is True,   "Test 6: Valid"
    print("All tests passed!")
