"""
============================================================
Problem: Find the Corrupt Pair
Pattern: Cyclic Sort
Difficulty: Easy
Link: https://leetcode.com/problems/set-mismatch/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a box of N puzzle pieces that should be numbered 1 to N.
But the factory made a mistake (a corruption!). They accidentally put two 
copies of one piece into the box, and entirely forgot to put another piece in!
Since the box still has exactly N pieces, this means exactly ONE number is 
duplicated, and exactly ONE number is missing.
We use our Cyclic Sort to put every piece into its correct spot.
After we finish swapping, exactly ONE spot will have the wrong piece in it.
If the 4th spot has a Piece 2 sitting in it, what does that tell us?
1. Piece 2 is the DUPLICATE (because the real Piece 2 is already sitting happily in the 2nd spot).
2. Piece 4 is MISSING (because its spot was stolen by the duplicate, and it's nowhere to be found!)

APPROACH:
---------
1. Initialize `i = 0`.
2. Loop through the array using a `while` loop to Cyclic Sort.
3. If `nums[i] != nums[nums[i] - 1]`: swap them.
4. Else: increment `i += 1`.
5. After the array is sorted, do a second pass (`for` loop).
6. Find the index `i` where `nums[i] != i + 1`.
7. `nums[i]` is the duplicate number.
8. `i + 1` is the missing number.
9. Return `[nums[i], i + 1]`.

COMPLEXITY:
-----------
Time:  O(N) — One pass to sort (with at most N swaps), one pass to find the corrupt pair.
Space: O(1) — Sorting is done completely in-place.

EDGE CASES:
-----------
- Edge case 1: Missing number is at the beginning or end of the array. Handled perfectly.
============================================================
"""

def find_corrupt_pair(nums: list[int]) -> list[int]:
    """
    Finds the duplicate and missing numbers in a corrupted array.
    Returns: [duplicate, missing]
    """
    i: int = 0
    n: int = len(nums)

    # 1. Sort the array using Cyclic Sort
    while i < n:
        j = nums[i] - 1
        
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # 2. Second pass to find the corrupt pair
    for i in range(n):
        if nums[i] != i + 1:
            # nums[i] is the duplicate, i + 1 is the missing number
            return [nums[i], i + 1]

    return [-1, -1]

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [3, 1, 2, 5, 2]
    assert find_corrupt_pair(arr1) == [2, 4], "Test 1 failed: Duplicate 2, Missing 4"

    arr2 = [3, 1, 2, 3, 6, 4]
    assert find_corrupt_pair(arr2) == [3, 5], "Test 2 failed: Duplicate 3, Missing 5"
    
    # 🔲 Edge cases
    arr3 = [2, 2]
    assert find_corrupt_pair(arr3) == [2, 1], "Edge 1: Minimum possible array"
    
    arr4 = [1, 2, 2, 4]
    assert find_corrupt_pair(arr4) == [2, 3], "Edge 2: Already sorted except for corruption"

    print("All tests passed!")
