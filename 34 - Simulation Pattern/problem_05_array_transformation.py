"""
============================================================
Problem: Array Transformation
Pattern: Simulation
Difficulty: Easy
Link: https://leetcode.com/problems/array-transformation/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a row of numbers. Each day, every number looks at its left and right
neighbors. If a number is SMALLER than both neighbors, it goes UP by 1.
If it's BIGGER than both neighbors, it goes DOWN by 1. Otherwise it stays.
Keep repeating until nothing changes anymore.

APPROACH:
---------
1. Simulate day by day.
2. Each day, create a new array based on the rules.
3. Stop when the new array equals the old one (no changes).

COMPLEXITY:
-----------
Time:  O(N * max_val) — in the worst case, values converge slowly.
Space: O(N) for the copy.

EDGE CASES:
-----------
- Already stable → return immediately.
- Length 1 or 2 → always stable (no element has two neighbors).
============================================================
"""

from typing import List


def transform_array(arr: List[int]) -> List[int]:
    changed = True
    while changed:
        changed = False
        new_arr = arr[:]
        for i in range(1, len(arr) - 1):
            if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                new_arr[i] += 1
                changed = True
            elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                new_arr[i] -= 1
                changed = True
        arr = new_arr
    return arr


if __name__ == "__main__":
    assert transform_array([6,2,3,4]) == [6,3,3,4], "Test 1"
    assert transform_array([1,6,3,4,3,5]) == [1,4,4,4,4,5], "Test 2"
    assert transform_array([5]) == [5], "Test 3: single"
    assert transform_array([1,2]) == [1,2], "Test 4: two elements"
    print("All tests passed!")
