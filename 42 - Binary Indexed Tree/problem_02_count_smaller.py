"""
============================================================
Problem: Count of Smaller Numbers After Self
Pattern: Binary Indexed Tree
Difficulty:
Link: https://leetcode.com/problem-placeholder/ Hard
LeetCode: #315
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array, for each element, count how many numbers to its RIGHT are smaller
than it.
e.g., `[5, 2, 6, 1]` -> `[2, 1, 1, 0]`.
To the right of 5, there are two smaller numbers (2 and 1).

APPROACH: Binary Indexed Tree + Coordinate Compression
---------
1. If we iterate from Right to Left, the problem becomes: "How many numbers
   smaller than `x` have I seen so far?"
2. We can use a BIT! The "index" in the BIT represents the VALUE of the number,
   and the "value" in the BIT is the count of how many times we've seen it.
3. But the values can be negative or very large! We don't want a BIT of size 1 million.
4. **Coordinate Compression**: We sort the unique values and map them to ranks 
   (1, 2, 3, ...). Now our BIT size is just `N`!
5. Iterate Right to Left:
   - Rank of current number `r = rank(num)`.
   - Query BIT for sum of all ranks from 1 to `r - 1` (this is the count of smaller numbers!).
   - Update BIT by adding 1 to rank `r`.

COMPLEXITY:
-----------
Time:  O(N log N)
Space: O(N)

EDGE CASES:
-----------
- Basic empty/null edge cases.
- Boundary constraints.
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


def countSmaller(nums: List[int]) -> List[int]:
    # Coordinate Compression
    sorted_unique_nums = sorted(list(set(nums)))
    ranks = {val: i + 1 for i, val in enumerate(sorted_unique_nums)}
    
    bit = BIT(len(ranks))
    result = []
    
    # Iterate from Right to Left
    for num in reversed(nums):
        rank = ranks[num]
        
        # Query how many numbers we've seen that are smaller (rank - 1)
        smaller_count = bit.query(rank - 1)
        result.append(smaller_count)
        
        # Add the current number to the BIT
        bit.update(rank, 1)
        
    # We built the result backwards, so reverse it
    return result[::-1]


if __name__ == "__main__":
    assert countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0], "Test 1"
    assert countSmaller([-1]) == [0],                  "Test 2"
    assert countSmaller([-1, -1]) == [0, 0],           "Test 3"
    print("All tests passed!")
