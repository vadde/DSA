"""
============================================================
Problem: Maximum Population Year
Pattern: Counting Pattern (Sweep Line / Difference Array)
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-population-year/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a list of people with birth years and death years. A person is
alive from birth year UP TO BUT NOT INCLUDING death year. Find the year
with the most people alive. If there's a tie, return the earliest year.

APPROACH (Difference Array):
---------
1. Years range from 1950 to 2050 (only 101 years).
2. For each person [birth, death]: increment count at `birth`, decrement at `death`.
3. Sweep through years computing running sum (prefix sum of the difference array).
4. Track the year with the maximum running sum.

COMPLEXITY:
-----------
Time:  O(N + Y) where Y = 101 (constant range).
Space: O(Y) = O(1).

EDGE CASES:
-----------
- Everyone born and dies in the same year interval.
- Single person.
============================================================
"""

from typing import List


def maximum_population(logs: List[List[int]]) -> int:
    # Difference array for years 1950 to 2050
    delta = [0] * 101  # index 0 = year 1950, index 100 = year 2050

    for birth, death in logs:
        delta[birth - 1950] += 1
        delta[death - 1950] -= 1

    max_pop = 0
    max_year = 1950
    running = 0

    for i in range(101):
        running += delta[i]
        if running > max_pop:
            max_pop = running
            max_year = 1950 + i

    return max_year


if __name__ == "__main__":
    assert maximum_population([[1993,1999],[2000,2010]]) == 1993, "Test 1"
    assert maximum_population([[1950,1961],[1960,1971],[1970,1981]]) == 1960, "Test 2"
    assert maximum_population([[2000,2005]]) == 2000, "Test 3: single"
    assert maximum_population([[1950,1951],[1950,1951]]) == 1950, "Test 4"
    print("All tests passed!")
