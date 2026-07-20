"""
============================================================
Problem: Count of Smaller Numbers After Self
Pattern: Segment Tree
Difficulty: Hard
Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
For each number in an array, find out how many numbers to its RIGHT are
strictly smaller than it.

APPROACH (Segment Tree):
---------
1. To use a Segment Tree, we need to map values to indices. Since values can
   be negative and large (-10^4 to 10^4), we can apply an offset (e.g., +10000) 
   so all values are >= 0.
2. The Segment Tree will store the FREQUENCY of each value seen so far.
3. We iterate from RIGHT to LEFT.
4. For each number, we QUERY the Segment Tree for the sum of frequencies in
   the range [0, number - 1]. This tells us how many smaller numbers we've seen.
5. Then, we UPDATE the Segment Tree by incrementing the frequency of `number`.

COMPLEXITY:
-----------
Time:  O(N log M) where M is the range of values (20001 here).
Space: O(M) for the Segment Tree array.

EDGE CASES:
-----------
- All elements same -> 0 for all.
- Strictly increasing -> 0 for all.
- Strictly decreasing -> N-1, N-2, ..., 0.
============================================================
"""

from typing import List

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * self.n)
        
    def update(self, node, start, end, index, val):
        if start == end:
            self.tree[node] += val
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update(2 * node + 1, start, mid, index, val)
        else:
            self.update(2 * node + 2, mid + 1, end, index, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        
    def query(self, node, start, end, l, r):
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(2 * node + 1, start, mid, l, r) + self.query(2 * node + 2, mid + 1, end, l, r)

def countSmaller(nums: List[int]) -> List[int]:
    offset = 10000
    size = 20002
    st = SegmentTree(size)
    
    result = []
    for num in reversed(nums):
        val = num + offset
        # query sum of frequencies of values strictly less than val
        result.append(st.query(0, 0, size - 1, 0, val - 1))
        # add this val to the tree
        st.update(0, 0, size - 1, val, 1)
        
    return result[::-1]

if __name__ == "__main__":
    assert countSmaller([5,2,6,1]) == [2,1,1,0], "Test 1"
    assert countSmaller([-1]) == [0], "Test 2"
    assert countSmaller([-1,-1]) == [0,0], "Test 3"
    print("All tests passed!")
