"""
============================================================
Problem: Range Sum Query - Mutable
Pattern: Segment Tree
Difficulty: Medium
LeetCode: #307
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an array. You need to do two things very fast:
1. Find the sum of numbers between index L and R.
2. Change the number at index `i` to a new value.
Prefix sums can do #1 fast, but #2 is slow. 
Segment Tree does BOTH in O(log N) time!

APPROACH: Array-based Segment Tree
---------
We can build a Segment Tree using an array of size 4*N.
Node `node` represents a segment. Its left child is `2*node + 1`,
and right child is `2*node + 2`.
1. **build**: Recursively divide the segment in half. When left == right, 
   set the leaf. Then parent = left_child + right_child.
2. **update**: Find the leaf, update it, and update all parents on the way up.
3. **query**: If segment is fully inside query, return node value.
   If outside, return 0. If partial overlap, return sum of left and right children queries.

COMPLEXITY:
-----------
Time:  O(N) to build. O(log N) per update/query.
Space: O(N) for the tree array.
============================================================
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums: List[int], node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = nums[start]
            return
            
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        self._build(nums, left_node, start, mid)
        self._build(nums, right_node, mid + 1, end)
        
        self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def _update(self, node: int, start: int, end: int, index: int, val: int) -> None:
        if start == end:
            self.tree[node] = val
            return
            
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        if start <= index <= mid:
            self._update(left_node, start, mid, index, val)
        else:
            self._update(right_node, mid + 1, end, index, val)
            
        self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def update(self, index: int, val: int) -> None:
        if self.n > 0:
            self._update(0, 0, self.n - 1, index, val)

    def _query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        # Complete overlap
        if l <= start and end <= r:
            return self.tree[node]
        # No overlap
        if r < start or end < l:
            return 0
            
        # Partial overlap
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        left_sum = self._query(left_node, start, mid, l, r)
        right_sum = self._query(right_node, mid + 1, end, l, r)
        
        return left_sum + right_sum

    def sumRange(self, left: int, right: int) -> int:
        if self.n == 0:
            return 0
        return self._query(0, 0, self.n - 1, left, right)


if __name__ == "__main__":
    numArray = NumArray([1, 3, 5])
    assert numArray.sumRange(0, 2) == 9, "Test 1"
    numArray.update(1, 2)
    assert numArray.sumRange(0, 2) == 8, "Test 2"
    print("All tests passed!")
