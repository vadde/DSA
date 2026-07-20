"""
============================================================
Problem: Closest Subsequence Sum
Pattern: Meet in the Middle
Difficulty: Hard
LeetCode: #1755
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an array of up to 40 numbers.
You want to pick some numbers (a subsequence) so their sum is as close
to a `goal` as possible. Return the minimum absolute difference.
Since 2^40 is 1 trillion (Too Slow!), we split the array in half.

APPROACH: Meet in the Middle
---------
1. Split `nums` into `left` (first 20) and `right` (last 20).
2. Generate all 2^20 subset sums for `left` -> `left_sums`.
3. Generate all 2^20 subset sums for `right` -> `right_sums`.
4. Sort `right_sums`.
5. For each `s` in `left_sums`, we need a value in `right_sums` close to `goal - s`.
   Use Binary Search (`bisect`) to find the closest element!

COMPLEXITY:
-----------
Time:  O(2^(N/2) * log(2^(N/2))) ≈ 20 Million operations (Very fast!)
Space: O(2^(N/2)) to store the sums.
============================================================
"""

from typing import List
import bisect


def minAbsDifference(nums: List[int], goal: int) -> int:
    def get_subset_sums(arr: List[int]) -> List[int]:
        sums = {0}
        for num in arr:
            sums |= {s + num for s in sums}
        return list(sums)

    n = len(nums)
    left_sums = get_subset_sums(nums[:n // 2])
    right_sums = sorted(get_subset_sums(nums[n // 2:]))

    min_diff = float('inf')

    for s in left_sums:
        target = goal - s
        # Binary search for closest value to target in right_sums
        idx = bisect.bisect_left(right_sums, target)

        # Check the element exactly at idx (if within bounds)
        if idx < len(right_sums):
            min_diff = min(min_diff, abs(goal - (s + right_sums[idx])))
            
        # Check the element right before idx (if it exists)
        if idx > 0:
            min_diff = min(min_diff, abs(goal - (s + right_sums[idx - 1])))

        if min_diff == 0:
            return 0

    return min_diff


if __name__ == "__main__":
    assert minAbsDifference([5,-7,3,5], 6) == 0, "Test 1: 5 + 3 - 7 + 5 is 6"
    assert minAbsDifference([7,-9,15,-2], -5) == 1,"Test 2: -9 - 2 + 7 = -4. abs(-5 - -4) = 1"
    assert minAbsDifference([1,2,3], -7) == 7,   "Test 3: Pick empty subset sum=0, diff=7"
    print("All tests passed!")
