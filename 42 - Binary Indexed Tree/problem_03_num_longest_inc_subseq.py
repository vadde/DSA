"""
============================================================
Problem: Number of Longest Increasing Subsequence
Pattern: Binary Indexed Tree / DP
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Find the LENGTH of the longest increasing subsequence (LIS) AND count HOW
MANY subsequences achieve that length. A subsequence doesn't need to be
contiguous — just in order.

APPROACH (DP):
---------
1. length[i] = length of LIS ending at index i.
2. count[i] = number of LIS of that length ending at index i.
3. For each i, check all j < i where nums[j] < nums[i]:
   - If length[j] + 1 > length[i]: found a longer LIS → update.
   - If length[j] + 1 == length[i]: found another path → add count.
4. Answer = sum of count[i] for all i where length[i] == max length.

NOTE: This can be optimized to O(N log N) with BIT, but O(N^2) DP is clean
and sufficient for interview-level N <= 2000.

COMPLEXITY:
-----------
Time:  O(N^2)
Space: O(N)

EDGE CASES:
-----------
- All elements equal → LIS length is 1, count = N.
- Strictly increasing → 1 LIS.
- All decreasing → N LIS of length 1.
============================================================
"""

from typing import List


def find_number_of_lis(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n

    length = [1] * n  # Length of LIS ending at i
    count = [1] * n   # Count of LIS of that length ending at i

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]

    max_len = max(length)
    return sum(count[i] for i in range(n) if length[i] == max_len)


if __name__ == "__main__":
    assert find_number_of_lis([1,3,5,4,7]) == 2, "Test 1: [1,3,5,7] and [1,3,4,7]"
    assert find_number_of_lis([2,2,2,2,2]) == 5, "Test 2: all same"
    assert find_number_of_lis([1,2,3]) == 1, "Test 3: strictly increasing"
    assert find_number_of_lis([3,2,1]) == 3, "Test 4: strictly decreasing"
    assert find_number_of_lis([1]) == 1, "Test 5: single"
    print("All tests passed!")
