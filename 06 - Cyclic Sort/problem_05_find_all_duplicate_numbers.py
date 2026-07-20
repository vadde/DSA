"""
============================================================
Problem: Find all Duplicate Numbers
Pattern: Cyclic Sort
Difficulty: Easy
Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
This is just like "Find all Missing Numbers".
You have a box of N puzzle pieces. You try to sort them into their N spots.
If you pick up a Piece 3, and you look at the 3rd spot and see a Piece 3 is 
already there, you just say, "You're a duplicate!" and leave the extra Piece 3 
sitting right where it is.
After you've done this for the whole box, every "correct" piece is in its home.
Any piece that is sitting in the WRONG spot MUST be a duplicate!
For example, if you look at the 5th spot, and instead of a Piece 5, you see 
another Piece 3, you just write down "3" on your list of duplicates.

APPROACH:
---------
1. Initialize `i = 0`.
2. Loop through the array using a `while` loop.
3. The correct index for the number `nums[i]` is `nums[i] - 1`.
4. If `nums[i] != nums[nums[i] - 1]`:
   - Swap `nums[i]` and `nums[nums[i] - 1]`.
5. Else:
   - Increment `i += 1`.
6. After the array is "sorted", do a second pass (`for` loop).
7. If `nums[i] != i + 1`, then the number `nums[i]` is a duplicate! Add it to our list.
8. Return the list of duplicates.

COMPLEXITY:
-----------
Time:  O(N) — One pass to sort (with at most N swaps), one pass to find duplicates.
Space: O(1) — Sorting is done completely in-place. (Excluding the output list).

EDGE CASES:
-----------
- Edge case 1: Multiple duplicates. Handled naturally.
- Edge case 2: No duplicates (array is just a permutation). Returns empty list.
============================================================
"""

def find_all_duplicates(nums: list[int]) -> list[int]:
    """
    Finds all duplicate numbers in an array containing numbers from 1 to N.
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

    duplicates: list[int] = []

    # 2. Second pass to find all numbers sitting in the wrong spots
    for i in range(n):
        if nums[i] != i + 1:
            # The number AT this wrong spot is the duplicate
            duplicates.append(nums[i])

    return duplicates

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [3, 4, 4, 5, 5]
    assert find_all_duplicates(arr1) == [5, 4], "Test 1 failed"

    arr2 = [5, 4, 7, 2, 3, 5, 3]
    assert find_all_duplicates(arr2) == [3, 5], "Test 2 failed"
    
    # 🔲 Edge cases
    arr3 = [1, 2, 3]
    assert find_all_duplicates(arr3) == [], "Edge 1: No duplicates"
    
    arr4 = [2, 2]
    assert find_all_duplicates(arr4) == [2], "Edge 2: Only duplicates"

    print("All tests passed!")
