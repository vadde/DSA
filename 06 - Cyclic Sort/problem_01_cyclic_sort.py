"""
============================================================
Problem: Cyclic Sort
Pattern: Cyclic Sort
Difficulty: Easy
Link: https://www.educative.io/courses/grokking-the-coding-interview/B8qXVqVwDKY
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bunch of numbered boxes mixed up in a row. The numbers on the boxes 
are exactly 1, 2, 3, up to N. 
You want to put Box 1 in the 1st spot, Box 2 in the 2nd spot, and so on.
Instead of looking at all the boxes at once, you just look at the box in the 1st spot.
If it's Box 4, you say, "Hey! You belong in the 4th spot!" So you take Box 4 and 
swap it with whatever box is currently sitting in the 4th spot.
Now you look at the 1st spot again. Is it Box 1 yet? If not, keep swapping it 
with the spot where it belongs! 
Once Box 1 is in the 1st spot, you move on to the 2nd spot and repeat. 
Eventually, every box gets swapped exactly once into its perfect home.

APPROACH:
---------
1. Initialize a pointer `i = 0`.
2. Loop through the array using a `while` loop (so we control when `i` increments).
3. The correct index for the number `nums[i]` is `nums[i] - 1` (because the numbers start at 1, but indices start at 0).
4. If `nums[i]` is NOT currently at its correct index:
   - Swap `nums[i]` and `nums[nums[i] - 1]`.
   - Do NOT increment `i` yet, because the new number we just swapped into index `i` might still be wrong!
5. If `nums[i]` IS at its correct index:
   - Increment `i += 1`.
6. Return the sorted array.

COMPLEXITY:
-----------
Time:  O(N) — Even though there's a while loop, every swap places at least one number in its correct position. The maximum number of swaps is N-1. Total time is O(N) + O(N-1) = O(N).
Space: O(1) — Sorting is done completely in-place.

EDGE CASES:
-----------
- Edge case 1: The array is already sorted. O(N) traversal with 0 swaps.
- Edge case 2: Array is in reverse order.
============================================================
"""

def cyclic_sort(nums: list[int]) -> list[int]:
    """
    Sorts an array containing numbers from 1 to N in O(N) time and O(1) space.
    """
    i: int = 0
    n: int = len(nums)

    while i < n:
        # The correct index for the number at nums[i]
        j: int = nums[i] - 1
        
        # If the number is not at its correct index, swap them
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            # Only increment if the current number is happy
            i += 1

    return nums

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [3, 1, 5, 4, 2]
    assert cyclic_sort(arr1) == [1, 2, 3, 4, 5], f"Test 1 failed: {arr1}"

    arr2 = [2, 6, 4, 3, 1, 5]
    assert cyclic_sort(arr2) == [1, 2, 3, 4, 5, 6], f"Test 2 failed: {arr2}"
    
    # 🔲 Edge cases
    arr3 = [1, 2, 3, 4, 5]
    assert cyclic_sort(arr3) == [1, 2, 3, 4, 5], "Edge 1: Already sorted"
    
    arr4 = [5, 4, 3, 2, 1]
    assert cyclic_sort(arr4) == [1, 2, 3, 4, 5], "Edge 2: Reverse order"

    print("All tests passed!")
