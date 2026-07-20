"""
============================================================
Problem: Find the Missing Number
Pattern: Cyclic Sort
Difficulty: Easy
Link: https://leetcode.com/problems/missing-number/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a set of puzzle pieces numbered from 0 to N. But there is one problem:
your box only holds N pieces, so exactly ONE piece is missing!
Because the pieces are numbered starting at 0, their numbers match their indices 
perfectly! (Piece 0 belongs at index 0, Piece 3 belongs at index 3).
Wait, what if we find Piece N? There is no index N! (Since the array is size N).
That's totally fine! If we find Piece N, we just ignore it and leave it where it is.
We just keep swapping all the OTHER pieces into their correct spots.
Once we are done, we just walk down the line. If we look at index 2 and don't see 
Piece 2, we know that Piece 2 is the missing one!

APPROACH:
---------
1. Initialize pointer `i = 0`.
2. Loop through the array using a `while` loop.
3. The correct index for the number `nums[i]` is exactly `nums[i]`.
4. If `nums[i]` is a valid index (`< len(nums)`) AND `nums[i]` is not already at its correct index:
   - Swap `nums[i]` and `nums[nums[i]]`.
   - Do not increment `i`.
5. Else:
   - Increment `i += 1`.
6. After the array is sorted, do a second pass (`for` loop).
7. If `nums[i] != i`, return `i`.
8. If all indices match their numbers, the missing number must be the only one left: `len(nums)`.

COMPLEXITY:
-----------
Time:  O(N) — One pass to sort (with at most N swaps), one pass to find the missing number.
Space: O(1) — Sorting is done completely in-place.

EDGE CASES:
-----------
- Edge case 1: The missing number is `N`. The second pass finishes and we return `N`.
- Edge case 2: The missing number is `0`. Found immediately on index 0 during second pass.
============================================================
"""

def find_missing_number(nums: list[int]) -> int:
    """
    Finds the missing number from an array containing numbers in the range 0 to N.
    """
    i: int = 0
    n: int = len(nums)

    # 1. Sort the array using Cyclic Sort
    while i < n:
        j = nums[i]
        
        # If the number is within bounds and not at its correct index, swap
        if j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            # We either found the correct number, OR we found 'n' which is out of bounds
            i += 1

    # 2. Second pass to find the missing number
    for i in range(n):
        if nums[i] != i:
            return i

    # 3. If all numbers are correct, then 'n' itself is the missing number
    return n

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [4, 0, 3, 1]
    assert find_missing_number(arr1) == 2, "Test 1 failed: Missing 2"

    arr2 = [8, 3, 5, 2, 4, 6, 0, 1]
    assert find_missing_number(arr2) == 7, "Test 2 failed: Missing 7"
    
    # 🔲 Edge cases
    arr3 = [0, 1, 2, 3]
    assert find_missing_number(arr3) == 4, "Edge 1: Missing N"
    
    arr4 = [1, 2, 3]
    assert find_missing_number(arr4) == 0, "Edge 2: Missing 0"

    print("All tests passed!")
