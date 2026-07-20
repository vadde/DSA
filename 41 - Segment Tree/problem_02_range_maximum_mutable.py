"""
============================================================
Problem: Range Maximum Query (Mutable)
Pattern: Segment Tree
Difficulty: Medium
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Similar to the sum problem, but instead of finding the sum of a range,
we need to find the MAXIMUM number in a range.
We also need to be able to update numbers!

APPROACH: Array-based Segment Tree
---------
Exactly the same as the sum Segment Tree, but instead of:
`parent = left_child + right_child`
we use:
`parent = max(left_child, right_child)`
And for queries with NO OVERLAP, instead of returning `0`, we return `-infinity`!

COMPLEXITY:
-----------
Time:  O(N) to build. O(log N) per update/query.
Space: O(N) for the tree array.
============================================================
"""

from typing import List


class MaxSegmentTree:
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
        
        # Max instead of Sum
        self.tree[node] = max(self.tree[left_node], self.tree[right_node])

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
            
        # Max instead of Sum
        self.tree[node] = max(self.tree[left_node], self.tree[right_node])

    def update(self, index: int, val: int) -> None:
        if self.n > 0:
            self._update(0, 0, self.n - 1, index, val)

    def _query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        # Complete overlap
        if l <= start and end <= r:
            return self.tree[node]
        # No overlap - return negative infinity so it doesn't affect the max!
        if r < start or end < l:
            return float('-inf')
            
        # Partial overlap
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        left_max = self._query(left_node, start, mid, l, r)
        right_max = self._query(right_node, mid + 1, end, l, r)
        
        # Max instead of Sum
        return max(left_max, right_max)

    def maxRange(self, left: int, right: int) -> int:
        if self.n == 0:
            return float('-inf')
        return int(self._query(0, 0, self.n - 1, left, right))


if __name__ == "__main__":
    st = MaxSegmentTree([1, 8, 5, 9, 6, 3])
    assert st.maxRange(0, 2) == 8, "Test 1"
    assert st.maxRange(1, 4) == 9, "Test 2"
    st.update(2, 15)  # Change 5 to 15
    assert st.maxRange(1, 4) == 15,"Test 3"
    print("All tests passed!")
