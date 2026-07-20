"""
============================================================
Problem: Count Elements With Maximum Frequency
Pattern: Counting Pattern
Difficulty: Easy
Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Count how many elements appear the same number of times as the element that
appears the MOST. Then return the TOTAL count of all such elements.

APPROACH:
---------
1. Count the frequency of every element.
2. Find the maximum frequency.
3. Sum all frequencies that equal the maximum.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N) for the counter.

EDGE CASES:
-----------
- All elements unique → max_freq = 1, answer = N.
- All elements the same → answer = N.
============================================================
"""

from typing import List
from collections import Counter


def max_frequency_elements(nums: List[int]) -> int:
    freq = Counter(nums)
    max_freq = max(freq.values())
    return sum(f for f in freq.values() if f == max_freq)


if __name__ == "__main__":
    assert max_frequency_elements([1,2,2,3,1,4]) == 4, "Test 1: 1 and 2 both appear 2x"
    assert max_frequency_elements([1,2,3,4,5]) == 5, "Test 2: all unique"
    assert max_frequency_elements([7,7,7]) == 3, "Test 3: all same"
    assert max_frequency_elements([1,1,2,2,3]) == 4, "Test 4"
    print("All tests passed!")
