"""
============================================================
Problem: Next Greater Element I
Pattern: Monotonic Stack
Difficulty: Easy
LeetCode: #496
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an array. For each number, find the FIRST number to its right that is
LARGER than it. If there isn't one, output -1.

APPROACH: Monotonic Decreasing Stack
---------
We want to keep a stack of numbers that are waiting for their "next greater element".
We iterate through the array. If the current number is LARGER than the top of the stack,
it means the current number is the "next greater element" for the top of the stack!
We pop it, record the answer in a Hash Map, and keep checking.
If the current number is smaller, we push it onto the stack to wait for its turn.

COMPLEXITY:
-----------
Time:  O(N) — Each element is pushed and popped at most once.
Space: O(N) — For the stack and hash map.
============================================================
"""

from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    next_greater: dict[int, int] = {}
    stack: List[int] = []  # Monotonic decreasing stack
    
    for num in nums2:
        # While the current number is greater than the top of the stack,
        # it is the "next greater" for that top element!
        while stack and num > stack[-1]:
            smaller_num = stack.pop()
            next_greater[smaller_num] = num
        
        # Push current number onto stack to wait for its next greater
        stack.append(num)
        
    # Any elements left in the stack do not have a next greater element.
    # We don't strictly need to do anything since our map lookup will handle it.
    
    return [next_greater.get(num, -1) for num in nums1]


if __name__ == "__main__":
    assert next_greater_element([4,1,2], [1,3,4,2]) == [-1, 3, -1], "Test 1"
    assert next_greater_element([2,4], [1,2,3,4]) == [3, -1],       "Test 2"
    assert next_greater_element([1], [2, 1, 3]) == [3],             "Test 3"
    print("All tests passed!")
