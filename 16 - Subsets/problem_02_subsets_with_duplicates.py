"""
============================================================
Problem: Subsets With Duplicates
Pattern: Subsets (BFS)
Difficulty: Easy
Link: https://leetcode.com/problems/subsets-ii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an empty box `[]`.
This time, your toys are an Apple, a Bear, and ANOTHER Bear! `[A, B, B]`.
If you do the exact same thing as before, you will eventually create two boxes 
that both just have `[A, B]` inside them, because you added the first Bear to 
an `[A]` box, and later you added the second Bear to an `[A]` box.
We don't want duplicate boxes!
To fix this, we sort the toys so the two Bears are right next to each other.
When we pick up the FIRST Bear, we add it to ALL of our existing boxes.
But when we pick up the SECOND Bear, we say: "Wait! I just saw a Bear. If I add 
this new Bear to ALL my old boxes, I'll make duplicates. I should ONLY add this 
new Bear to the brand new boxes I JUST created in the previous step!"

APPROACH:
---------
1. Sort the input array `nums.sort()`. This ensures duplicates are adjacent.
2. Initialize `subsets = [[]]`.
3. Initialize `start_idx = 0` and `end_idx = 0`. These will track which subsets 
   we are allowed to add the current number to.
4. Loop through every number `nums[i]`:
   - Reset `start_idx = 0`. (By default, we add the number to ALL subsets).
   - Check for duplicate: If `i > 0` and `nums[i] == nums[i - 1]`, we found a duplicate!
     Change `start_idx = end_idx`. (We will only add this number to the subsets 
     created in the previous step).
   - Set `end_idx = len(subsets)`. (This is the total number of subsets before 
     we start adding new ones in this step).
   - Loop `j` from `start_idx` to `end_idx - 1`:
     - Create a copy of `subsets[j]`.
     - Append `nums[i]`.
     - Append the copy to `subsets`.
5. Return `subsets`.

COMPLEXITY:
-----------
Time:  O(N * 2^N) — Sorting is O(N log N), but the subset generation dominates.
Space: O(N * 2^N) — To store the subsets.

EDGE CASES:
-----------
- Edge case 1: Empty input. Returns `[[]]`.
- Edge case 2: All identical elements `[1, 1, 1]`. Correctly avoids generating 
  duplicate subsets of the same size.
============================================================
"""

from typing import List

def find_subsets_with_duplicates(nums: List[int]) -> List[List[int]]:
    """
    Returns all possible distinct subsets of an array that may contain duplicates.
    """
    # 1. Sort the array so duplicates are adjacent
    nums.sort()
    
    subsets = [[]]
    start_idx = 0
    end_idx = 0
    
    for i in range(len(nums)):
        start_idx = 0
        
        # If this is a duplicate, we only add it to the subsets created in the LAST step
        if i > 0 and nums[i] == nums[i - 1]:
            start_idx = end_idx
            
        # Record the current size before we add new elements
        end_idx = len(subsets)
        
        # Loop from start_idx to end_idx
        for j in range(start_idx, end_idx):
            set_copy = list(subsets[j])
            set_copy.append(nums[i])
            subsets.append(set_copy)
            
    return subsets

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # Input: [1, 3, 3]
    # Expected output: [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]
    result1 = find_subsets_with_duplicates([1, 3, 3])
    expected1 = [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]
    assert result1 == expected1, f"Test 1 failed. Got {result1}"

    # 🔲 Edge cases
    assert find_subsets_with_duplicates([2, 2]) == [[], [2], [2, 2]], "Edge 1: All duplicates"
    assert find_subsets_with_duplicates([]) == [[]], "Edge 2: Empty array"

    print("All tests passed!")
