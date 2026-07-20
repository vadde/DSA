"""
============================================================
Problem: Relative Sort Array
Pattern: Linear Sorting (Counting Sort)
Difficulty: Easy
Link: https://leetcode.com/problems/relative-sort-array/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Sort arr1 so that elements appear in the same order as arr2. Elements NOT in
arr2 go at the end, sorted in ascending order.

APPROACH:
---------
1. Count frequencies of each element in arr1 using a Counter.
2. First, iterate through arr2. For each element, append it `count` times.
3. Then, for any remaining elements (not in arr2), sort them and append.

COMPLEXITY:
-----------
Time:  O(N log N) for sorting the remainder (or O(N + K) if using counting sort).
Space: O(N) for the counter.

EDGE CASES:
-----------
- All elements of arr1 in arr2.
- No elements of arr1 in arr2.
============================================================
"""

from typing import List
from collections import Counter


def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    count = Counter(arr1)
    result = []

    # First: elements in arr2 order
    for num in arr2:
        result.extend([num] * count.pop(num, 0))

    # Then: remaining elements sorted
    remaining = sorted(count.elements())
    result.extend(remaining)

    return result


if __name__ == "__main__":
    assert relative_sort_array([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19], "Test 1"
    assert relative_sort_array([28,6,22,8,44,17], [22,28,8,6]) == [22,28,8,6,17,44], "Test 2"
    assert relative_sort_array([1,2,3], []) == [1,2,3], "Test 3: empty arr2"
    print("All tests passed!")
