"""
============================================================
Problem: Subset Sum Equal to Target (Meet in the Middle)
Pattern: Meet in the Middle
Difficulty: Medium
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array of numbers, determine if there exists a subset that sums to
exactly `target`. This is the classic Subset Sum problem, but here N can be
up to 40 — too large for O(2^N) brute force but perfect for Meet in the Middle.

APPROACH:
---------
1. Split the array into left and right halves.
2. Generate all subset sums for both halves.
3. Put the right sums in a set.
4. For each left sum `s`, check if `target - s` exists in the right set.

COMPLEXITY:
-----------
Time:  O(2^(N/2))
Space: O(2^(N/2))

EDGE CASES:
-----------
- target = 0 → empty subset always works (True).
- All negative numbers.
- Single element equals target.
============================================================
"""

from typing import List


def subset_sum(nums: List[int], target: int) -> bool:
    def get_all_sums(arr):
        sums = {0}
        for num in arr:
            sums |= {s + num for s in sums}
        return sums

    n = len(nums)
    left_sums = get_all_sums(nums[:n // 2])
    right_sums = get_all_sums(nums[n // 2:])

    for s in left_sums:
        if target - s in right_sums:
            return True

    return False


if __name__ == "__main__":
    assert subset_sum([2, 3, 7, 8, 10], 11) == True, "Test 1: 3+8"
    assert subset_sum([1, 2, 3, 4, 5], 100) == False, "Test 2"
    assert subset_sum([1, 5, 11, 5], 11) == True, "Test 3"
    assert subset_sum([], 0) == True, "Test 4: empty subset"
    assert subset_sum([10], 10) == True, "Test 5: single element"
    assert subset_sum([-1, -2, 3], 0) == True, "Test 6: negatives"
    print("All tests passed!")
