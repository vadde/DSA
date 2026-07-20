"""
============================================================
Problem: Reverse Pairs
Pattern: Binary Indexed Tree (Fenwick Tree)
Difficulty: Hard
Link: https://leetcode.com/problems/reverse-pairs/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Find how many pairs of numbers (i, j) exist such that i < j (i comes before j)
AND nums[i] > 2 * nums[j].

APPROACH (Binary Indexed Tree / Fenwick Tree):
---------
1. This is similar to "Count Smaller Numbers After Self", but the condition is 
   `nums[i] > 2 * nums[j]`.
2. Since numbers can be very large (up to 2^31 - 1), we can't use their exact
   values as indices in the BIT. We MUST use Coordinate Compression.
3. Collect all `nums[i]` and `2 * nums[i]` into a sorted set to create a rank map.
4. Iterate from RIGHT to LEFT.
5. For each `nums[i]`, query the BIT for the sum of frequencies of values strictly
   less than `nums[i]`. (We are looking for previously seen `2 * nums[j]` that are 
   strictly smaller than `nums[i]`).
6. Then, update the BIT by incrementing the frequency of `2 * nums[i]`.

Wait, actually, it's easier to iterate RIGHT to LEFT, query for `< nums[i]`, and 
insert `2 * nums[i]`.

COMPLEXITY:
-----------
Time:  O(N log N)
Space: O(N)

EDGE CASES:
-----------
- No reverse pairs -> 0.
- Negative numbers (e.g., -5 > 2 * -3 -> -5 > -6, true).
============================================================
"""

from typing import List

class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        
    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def reversePairs(nums: List[int]) -> int:
    # Coordinate compression
    values = set()
    for num in nums:
        values.add(num)
        values.add(2 * num)
        
    sorted_values = sorted(list(values))
    ranks = {val: i + 1 for i, val in enumerate(sorted_values)}
    
    bit = BIT(len(ranks))
    count = 0
    
    # Iterate from right to left
    for num in reversed(nums):
        # We want to find how many numbers we've seen to the right
        # that are strictly less than nums[i]
        # Since we inserted `2 * nums[j]` into the BIT, querying `< nums[i]`
        # means querying `< ranks[nums[i]]`
        rank_query = ranks[num] - 1
        count += bit.query(rank_query)
        
        # Insert 2 * nums[i] into the BIT
        bit.update(ranks[2 * num], 1)
        
    return count

if __name__ == "__main__":
    assert reversePairs([1,3,2,3,1]) == 2, "Test 1"
    assert reversePairs([2,4,3,5,1]) == 3, "Test 2"
    assert reversePairs([5,4,3,2,1]) == 4, "Test 3"
    print("All tests passed!")
