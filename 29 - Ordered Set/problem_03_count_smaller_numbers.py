"""
============================================================
Problem: Count of Smaller Numbers After Self
Pattern: Ordered Set (using bisect in Python)
Difficulty: Hard
LeetCode: #315
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
For each number in an array, count how many numbers to its right are smaller.
E.g., [5, 2, 6, 1] →
- 5: 2 and 1 are smaller (2)
- 2: 1 is smaller (1)
- 6: 1 is smaller (1)
- 1: nothing is smaller (0)
Output: [2, 1, 1, 0]

APPROACH: Ordered Set (Sorted List)
---------
Iterate from right to left.
Maintain a sorted list of numbers seen so far.
For the current number, use Binary Search (`bisect_left`) on the sorted list
to find how many numbers are strictly smaller than it.
Then insert the current number into the sorted list to keep it sorted.

COMPLEXITY:
-----------
Time:  O(N log N) with a true Balanced BST or Fenwick Tree.
       O(N^2) in Python using `bisect.insort` (due to list shifting), but often passes.
Space: O(N)
============================================================
"""

import bisect
from typing import List


def count_smaller(nums: List[int]) -> List[int]:
    sorted_list: List[int] = []
    result = []
    
    # Traverse from right to left
    for num in reversed(nums):
        # Find index of first element >= num. This index is exactly
        # the count of elements strictly smaller than num.
        idx = bisect.bisect_left(sorted_list, num)
        result.append(idx)
        # Insert num to keep the list sorted
        bisect.insort(sorted_list, num)
        
    return result[::-1]


if __name__ == "__main__":
    assert count_smaller([5, 2, 6, 1]) == [2, 1, 1, 0], "Test 1"
    assert count_smaller([-1]) == [0],                  "Test 2"
    assert count_smaller([-1, -1]) == [0, 0],           "Test 3"
    print("All tests passed!")
