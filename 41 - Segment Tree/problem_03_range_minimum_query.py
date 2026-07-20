"""
============================================================
Problem: Range Minimum Query (Segment Tree)
Pattern: Segment Tree
Difficulty:
Link: https://leetcode.com/problem-placeholder/ Easy
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array, answer queries: "What is the MINIMUM value between index L
and R?" This is the classic Segment Tree use case alongside range sum and
range max.

APPROACH:
---------
Same as Range Sum/Max Segment Tree, but:
- Build: parent = min(left_child, right_child)
- Query: No-overlap returns float('inf') (identity for min)
- Update: Same traversal, parent = min(left_child, right_child)

COMPLEXITY:
-----------
Time:  O(N) build, O(log N) query/update.
Space: O(N)

EDGE CASES:
-----------
- Single element.
- Query entire array.
- Update to a value smaller/larger than all others.
============================================================
"""

from typing import List


class MinSegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
            return
        mid = (start + end) // 2
        self._build(nums, 2*node+1, start, mid)
        self._build(nums, 2*node+2, mid+1, end)
        self.tree[node] = min(self.tree[2*node+1], self.tree[2*node+2])

    def _update(self, node, start, end, index, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if index <= mid:
            self._update(2*node+1, start, mid, index, val)
        else:
            self._update(2*node+2, mid+1, end, index, val)
        self.tree[node] = min(self.tree[2*node+1], self.tree[2*node+2])

    def update(self, index, val):
        if self.n > 0:
            self._update(0, 0, self.n-1, index, val)

    def _query(self, node, start, end, l, r):
        if l <= start and end <= r:
            return self.tree[node]
        if r < start or end < l:
            return float('inf')
        mid = (start + end) // 2
        return min(
            self._query(2*node+1, start, mid, l, r),
            self._query(2*node+2, mid+1, end, l, r)
        )

    def min_range(self, left, right):
        if self.n == 0:
            return float('inf')
        return self._query(0, 0, self.n-1, left, right)


if __name__ == "__main__":
    st = MinSegmentTree([5, 2, 8, 1, 9, 3])
    assert st.min_range(0, 2) == 2, "Test 1"
    assert st.min_range(1, 4) == 1, "Test 2"
    assert st.min_range(0, 5) == 1, "Test 3: full range"
    st.update(3, 10)  # Change 1 to 10
    assert st.min_range(1, 4) == 2, "Test 4: after update"
    assert st.min_range(3, 3) == 10, "Test 5: single element"
    print("All tests passed!")
