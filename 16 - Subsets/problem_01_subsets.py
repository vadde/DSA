"""
============================================================
Problem: Subsets
Pattern: Subsets (BFS)
Difficulty: Easy
Link: https://leetcode.com/problems/subsets/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an empty box `[]`.
You are given a list of toys: `[1, 2, 3]`.
You walk up to Toy 1. You make a copy of your empty box, and put Toy 1 inside.
Now you have two boxes: `[]` and `[1]`.
You walk up to Toy 2. You make copies of BOTH of your boxes, and put Toy 2 inside 
the copies.
Now you have four boxes: `[]`, `[1]`, `[2]`, `[1, 2]`.
You walk up to Toy 3. You make copies of ALL FOUR boxes, and put Toy 3 inside.
Now you have eight boxes! You have found every possible combination of toys.
This is exactly how we write the code! We loop through the toys, and for every toy, 
we double our list of boxes.

APPROACH:
---------
1. Initialize `subsets = [[]]`. (Our starting empty box).
2. Loop through every number `num` in the input array `nums`.
3. Take a snapshot of how many subsets we currently have: `n = len(subsets)`.
   - WARNING: Do not just iterate `for subset in subsets:` while appending to it, 
     or you will create an infinite loop! You must take the length FIRST.
4. Loop `i` from `0` to `n - 1`:
   - Create a copy of the subset at index `i`: `set_copy = list(subsets[i])`.
   - Add the current `num` to the copy: `set_copy.append(num)`.
   - Add the new copy back to our main list: `subsets.append(set_copy)`.
5. Return the final list of `subsets`.

COMPLEXITY:
-----------
Time:  O(N * 2^N) — For N numbers, there are 2^N subsets. In each step, we copy 
       arrays that can be up to length N.
Space: O(N * 2^N) — To store all 2^N subsets in the result array.

EDGE CASES:
-----------
- Edge case 1: Empty input `nums = []`. Returns `[[]]`.
============================================================
"""

from typing import List

def find_subsets(nums: List[int]) -> List[List[int]]:
    """
    Returns all possible subsets of an array of distinct integers.
    """
    subsets = [[]]

    for num in nums:
        # Take a snapshot of the current number of subsets
        # We MUST do this, otherwise appending inside the loop causes an infinite loop!
        n = len(subsets)
        
        for i in range(n):
            # 1. Create a deep copy of the existing subset
            set_copy = list(subsets[i])
            
            # 2. Add the current number to the copy
            set_copy.append(num)
            
            # 3. Add the brand new subset back to our main list
            subsets.append(set_copy)

    return subsets

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # Input: [1, 2, 3]
    # Expected output (order doesn't matter, but our algorithm produces this exact order):
    # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    result1 = find_subsets([1, 2, 3])
    expected1 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert result1 == expected1, f"Test 1 failed. Got {result1}"

    # 🔲 Edge cases
    assert find_subsets([]) == [[]], "Edge 1: Empty input"
    assert find_subsets([0]) == [[], [0]], "Edge 2: Single element"

    print("All tests passed!")
