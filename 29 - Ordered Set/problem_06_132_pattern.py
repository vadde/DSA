"""
============================================================
Problem: 132 Pattern
Pattern: Ordered Set / Monotonic Stack
Difficulty: Medium
Link: https://leetcode.com/problems/132-pattern/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Find three numbers nums[i] < nums[k] < nums[j] where i < j < k.
In other words: a small number, then a BIG number, then a MEDIUM number
(smaller than the big, but bigger than the small). The pattern looks like
the shape "1-3-2" reading left to right.

KEY INSIGHT: Iterate from RIGHT to LEFT. Use a stack to track candidates
for the "3" (the largest element). When we pop from the stack, the popped
element becomes our candidate for "2" (the medium element). Then we just
need to find a "1" (a smaller element) to the left.

APPROACH:
---------
1. Iterate from right to left.
2. Maintain `candidate_2` (the largest value popped from the stack so far).
3. Maintain a monotonically decreasing stack.
4. At each position:
   - If `nums[i] < candidate_2`, we found the "1"! Return True.
   - While stack top <= nums[i], pop and update candidate_2.
   - Push nums[i] onto stack.
5. If we finish without finding, return False.

COMPLEXITY:
-----------
Time:  O(N) — each element pushed and popped at most once.
Space: O(N) — stack.

EDGE CASES:
-----------
- Array length < 3 → False.
- All equal elements → False.
- Strictly increasing or decreasing → check carefully.
============================================================
"""

from typing import List


def find132pattern(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    stack = []
    candidate_2 = float('-inf')  # The "2" in the 1-3-2 pattern

    # Iterate right to left
    for i in range(len(nums) - 1, -1, -1):
        # If current < candidate_2, we found the "1" (smallest)
        if nums[i] < candidate_2:
            return True

        # Pop elements smaller than current — they become candidate_2
        while stack and stack[-1] < nums[i]:
            candidate_2 = stack.pop()

        stack.append(nums[i])

    return False


if __name__ == "__main__":
    assert find132pattern([1,2,3,4]) == False, "Test 1: strictly increasing"
    assert find132pattern([3,1,4,2]) == True, "Test 2: 1,4,2"
    assert find132pattern([-1,3,2,0]) == True, "Test 3: -1,3,2"
    assert find132pattern([1,0,1,-4,-3]) == False, "Test 4"
    assert find132pattern([3,5,0,3,4]) == True, "Test 5"
    print("All tests passed!")
