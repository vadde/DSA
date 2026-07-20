"""
============================================================
Problem: Find the Duplicate Number
Pattern: Cyclic Sort
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-duplicate-number/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have N+1 boxes, and exactly N unique toys to put in them. 
This means ONE of the toys is a duplicate, and there are two of them!
We can use our Cyclic Sort trick to put every toy into its correct box.
Toy 3 goes into Box 3. Toy 5 goes into Box 5.
If we pick up a Toy 4, we walk over to Box 4 to put it away. But wait! There is 
ALREADY a Toy 4 sitting in Box 4! 
Since we found two of the exact same toy trying to claim the exact same spot, 
we caught the duplicate red-handed! We don't even need to finish sorting; we can 
just shout out the answer immediately.

NOTE: We solved this same problem in the "Fast & Slow Pointers" chapter using 
a magical trick that didn't modify the array at all. Cyclic Sort WILL modify 
the array by swapping elements around, but it is much easier to understand!

APPROACH:
---------
1. Initialize `i = 0`.
2. Loop through the array using a `while` loop.
3. If the current number `nums[i]` is not at its correct index (i.e. `nums[i] != i + 1`):
   - Check where it belongs: `j = nums[i] - 1`.
   - Look at the number sitting at index `j`. Is it the EXACT SAME number?
   - If `nums[i] != nums[j]`, they are different. Swap them!
   - If `nums[i] == nums[j]`, they are identical! We found the duplicate. Return `nums[i]`.
4. If it IS at the correct index, just increment `i += 1`.
5. Return -1 if no duplicate is found (though the problem guarantees one).

COMPLEXITY:
-----------
Time:  O(N) — Every swap puts at least one number in its correct spot.
Space: O(1) — Sorting is done completely in-place.

EDGE CASES:
-----------
- Edge case 1: Multiple copies of the duplicate (e.g., `[2, 2, 2, 2]`). Caught on the first clash.
============================================================
"""

def find_duplicate(nums: list[int]) -> int:
    """
    Finds the duplicate number in an array using Cyclic Sort.
    """
    i: int = 0
    n: int = len(nums)

    while i < n:
        # If the number is not at its correct index
        if nums[i] != i + 1:
            j = nums[i] - 1
            
            # If the spot it wants to go to is occupied by a DIFFERENT number, swap
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                # The spot is occupied by the EXACT SAME number! It's a duplicate.
                return nums[i]
        else:
            # The number is perfectly happy where it is
            i += 1

    return -1

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [1, 4, 4, 3, 2]
    assert find_duplicate(arr1) == 4, "Test 1 failed"

    arr2 = [2, 1, 3, 3, 5, 4]
    assert find_duplicate(arr2) == 3, "Test 2 failed"
    
    # 🔲 Edge cases
    arr3 = [2, 4, 1, 4, 4]
    assert find_duplicate(arr3) == 4, "Edge 1: Multiple duplicates"
    
    arr4 = [1, 1]
    assert find_duplicate(arr4) == 1, "Edge 2: Minimum possible array"

    print("All tests passed!")
