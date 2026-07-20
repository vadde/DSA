"""
============================================================
Problem: Subsets Having Sum Between A and B
Pattern: Meet in the Middle
Difficulty: Hard
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Count the number of subsets whose sum falls within the range [A, B]
(inclusive). N can be up to 40, so we need Meet in the Middle.

APPROACH:
---------
1. Split the array into left and right halves.
2. Generate all subset sums for both halves.
3. Sort the right sums.
4. For each left sum `s`, we need to count right sums `r` such that
   A <= s + r <= B, i.e., A - s <= r <= B - s.
5. Use binary search (bisect) to count values in that range!

COMPLEXITY:
-----------
Time:  O(2^(N/2) * log(2^(N/2)))
Space: O(2^(N/2))

EDGE CASES:
-----------
- A = B → count subsets with exact sum A.
- A = 0, B = total_sum → count = 2^N (all subsets).
- No subsets in range → 0.
============================================================
"""

from typing import List
import bisect


def count_subsets_in_range(nums: List[int], A: int, B: int) -> int:
    def get_all_sums(arr):
        sums = [0]
        for num in arr:
            sums += [s + num for s in sums]
        return sums

    n = len(nums)
    left_sums = get_all_sums(nums[:n // 2])
    right_sums = sorted(get_all_sums(nums[n // 2:]))

    count = 0
    for s in left_sums:
        lo = bisect.bisect_left(right_sums, A - s)
        hi = bisect.bisect_right(right_sums, B - s)
        count += hi - lo

    return count


if __name__ == "__main__":
    assert count_subsets_in_range([1, 2, 3], 3, 5) == 3, "Test 1: {3}, {1,2}, {1,3} have sums 3,3,4"
    assert count_subsets_in_range([1, 1, 1], 2, 3) == 4, "Test 2"
    assert count_subsets_in_range([5], 1, 4) == 0, "Test 3: nothing in range"
    assert count_subsets_in_range([5], 5, 5) == 1, "Test 4: exact match"
    assert count_subsets_in_range([], 0, 0) == 1, "Test 5: empty subset has sum 0"
    print("All tests passed!")
