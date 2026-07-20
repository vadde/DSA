"""
============================================================
Problem: Range Sum Query - Mutable (BIT Version)
Pattern: Binary Indexed Tree (Fenwick Tree)
Difficulty: Medium
LeetCode: #307
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
We want to do the exact same thing as the Segment Tree problem:
Query a range sum, and update a point.
But this time, we will use a Binary Indexed Tree, which is MUCH shorter
to write and uses less memory!

APPROACH: Binary Indexed Tree
---------
1. A BIT uses a 1-indexed array of size `N + 1`.
2. `update(i, delta)`: Adds `delta` to index `i`. Then moves to the next
   affected index by adding the Lowest Significant Bit (LSB): `i += i & (-i)`.
3. `query(i)`: Gets the prefix sum from 1 to `i`. Then moves to the previous
   chunk by subtracting the LSB: `i -= i & (-i)`.
4. To get a range sum `[L, R]`, we just do `query(R) - query(L - 1)`!

COMPLEXITY:
-----------
Time:  O(N log N) to build. O(log N) for query/update.
Space: O(N)
============================================================
"""

from typing import List


class BIT:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)
        
    def update(self, i: int, delta: int) -> None:
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BIT(len(nums))
        for i, val in enumerate(nums):
            self.bit.update(i + 1, val)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self.bit.update(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right + 1) - self.bit.query(left)


if __name__ == "__main__":
    numArray = NumArray([1, 3, 5])
    assert numArray.sumRange(0, 2) == 9, "Test 1"
    numArray.update(1, 2)
    assert numArray.sumRange(0, 2) == 8, "Test 2"
    print("All tests passed!")
