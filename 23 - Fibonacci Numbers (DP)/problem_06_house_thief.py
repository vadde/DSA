"""
============================================================
Problem: House Thief (House Robber)
Pattern: Fibonacci Numbers (DP)
Difficulty: Medium
LeetCode: #198
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You're a burglar planning to rob houses on a street. Each house has some money.
RULE: You cannot rob two ADJACENT houses (the alarm will go off).
What is the maximum amount of money you can rob?

E.g. [2,7,9,3,1] → rob houses 0,2,4 → 2+9+1=12.

APPROACH: Fibonacci DP
---------
dp[i] = max money robbing from houses 0..i.
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
  → Either skip house i (take dp[i-1]) or rob it (take dp[i-2] + nums[i]).

COMPLEXITY: O(N) time, O(1) space.
============================================================
"""

from typing import List


def house_robber(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr
    return prev1


if __name__ == "__main__":
    assert house_robber([2, 7, 9, 3, 1]) == 12, "Test 1"
    assert house_robber([1, 2, 3, 1]) == 4,     "Test 2"
    assert house_robber([]) == 0,               "Edge: empty"
    assert house_robber([5]) == 5,              "Edge: single"
    assert house_robber([2, 1]) == 2,           "Edge: two houses"
    print("All tests passed!")
