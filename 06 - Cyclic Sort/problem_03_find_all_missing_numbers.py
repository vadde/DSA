"""
============================================================
Problem: Find all Missing Numbers
Pattern: Cyclic Sort
Difficulty: Easy
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a box of 8 puzzle pieces, but someone mixed them up, and even worse, 
they accidentally put duplicates in the box and lost some of the original pieces!
The pieces are supposed to be numbered 1 through 8.
We use our Cyclic Sort magic trick to put every piece in its correct spot.
If we pick up a Piece 3, we put it in the 3rd spot.
But what if we pick up another Piece 3 later? We look at the 3rd spot, see that 
a Piece 3 is already sitting there perfectly happy, and we say, "Oh well, you're 
a duplicate." We just leave it exactly where we found it and move on.
After we try to sort the whole box, we just walk down the line. If the 5th spot 
doesn't have a Piece 5 in it (maybe it has a duplicate Piece 3 stuck there instead), 
we know Piece 5 is missing! We write down '5' and keep checking.

APPROACH:
---------
1. Initialize `i = 0`.
2. Loop through the array using a `while` loop.
3. The correct index for the number `nums[i]` is `nums[i] - 1` (1-indexed numbers).
4. If `nums[i] != nums[nums[i] - 1]`:
   - This checks if the number is NOT at its correct index, AND the number currently 
     sitting at the target index is not an identical duplicate!
   - Swap them!
5. Else:
   - Increment `i += 1`.
6. After the array is "sorted", do a second pass (`for` loop).
7. If `nums[i] != i + 1`, then the number `i + 1` is missing. Add it to our list.
8. Return the list of missing numbers.

COMPLEXITY:
-----------
Time:  O(N) — One pass to sort (with at most N swaps), one pass to find missing numbers.
Space: O(1) — Sorting is done completely in-place. (Excluding the space for the output list).

EDGE CASES:
-----------
- Edge case 1: Multiple missing numbers. Handled correctly.
- Edge case 2: No missing numbers (array is just a permutation). Returns empty list.
============================================================
"""

def find_all_missing_numbers(nums: list[int]) -> list[int]:
    """
    Finds all missing numbers in an array containing numbers from 1 to N with duplicates.
    """
    i: int = 0
    n: int = len(nums)

    # 1. Sort the array using Cyclic Sort
    while i < n:
        j = nums[i] - 1
        
        # Only swap if the number is not already at the correct index
        # This implicitly handles duplicates (it won't swap identical numbers infinitely)
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers: list[int] = []

    # 2. Second pass to find all missing numbers
    for i in range(n):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)

    return missing_numbers

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [2, 3, 1, 8, 2, 3, 5, 1]
    assert find_all_missing_numbers(arr1) == [4, 6, 7], "Test 1 failed"

    arr2 = [2, 4, 1, 2]
    assert find_all_missing_numbers(arr2) == [3], "Test 2 failed"
    
    # 🔲 Edge cases
    arr3 = [2, 3, 2, 1]
    assert find_all_missing_numbers(arr3) == [4], "Edge 1: Missing N"
    
    arr4 = [1, 2, 3]
    assert find_all_missing_numbers(arr4) == [], "Edge 2: No missing numbers"

    print("All tests passed!")
