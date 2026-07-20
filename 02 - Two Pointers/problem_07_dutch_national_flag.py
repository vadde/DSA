"""
============================================================
Problem: Dutch National Flag Problem
Pattern: Two Pointers (Advanced: Three Pointers / Partitioning)
Difficulty: Medium
Link: https://leetcode.com/problems/sort-colors/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a messy pile of red, white, and blue balls. You want to sort 
them so all red are on the left, all white are in the middle, and all blue are on 
the right.
Instead of counting them and buying new balls, you can just swap them around in place!
You use three fingers to keep track of things:
- Left finger: where the next red ball should go.
- Right finger: where the next blue ball should go.
- Middle finger: points to the ball you are currently holding and looking at.
If it's red, you swap it with the left finger's spot. If it's blue, you swap it with 
the right finger's spot. If it's white, you just leave it and move on!

APPROACH:
---------
1. Initialize three pointers: `low = 0`, `high = len(arr) - 1`, and `mid = 0`.
2. Loop `while mid <= high`:
   a. If `arr[mid] == 0` (Red):
      - Swap `arr[low]` and `arr[mid]`.
      - Increment BOTH `low` and `mid`. (We know the element swapped from `low` 
        to `mid` is either a 1 or 0, so it's safe to advance `mid`).
   b. If `arr[mid] == 1` (White):
      - It's already in the correct middle section, just increment `mid`.
   c. If `arr[mid] == 2` (Blue):
      - Swap `arr[mid]` and `arr[high]`.
      - Decrement `high`.
      - DO NOT increment `mid` yet! The new element swapped from `high` to `mid` 
        is completely unexamined (it could be a 0, 1, or 2), so we must evaluate 
        it on the next loop iteration.
3. The array is sorted in-place.

COMPLEXITY:
-----------
Time:  O(N) — We iterate through the array once. Each element is evaluated at most twice.
Space: O(1) — We sort the array in-place.

EDGE CASES:
-----------
- Edge case 1: Array is entirely one color (e.g., all 0s). Works flawlessly.
- Edge case 2: Array has length 1. Loop finishes immediately.
============================================================
"""

def sort_colors(arr: list[int]) -> None:
    """
    Sorts an array of 0s, 1s, and 2s in-place.
    """
    low: int = 0
    high: int = len(arr) - 1
    mid: int = 0

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # We don't increment mid here because the newly swapped arr[mid] 
            # hasn't been evaluated yet!

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [1, 0, 2, 1, 0]
    sort_colors(arr1)
    assert arr1 == [0, 0, 1, 1, 2], "Test 1 failed"

    arr2 = [2, 2, 0, 1, 2, 0]
    sort_colors(arr2)
    assert arr2 == [0, 0, 1, 2, 2, 2], "Test 2 failed"
    
    # 🔲 Edge cases
    arr3 = [0, 0, 0]
    sort_colors(arr3)
    assert arr3 == [0, 0, 0], "Edge 1: All zeros"

    arr4 = [1]
    sort_colors(arr4)
    assert arr4 == [1], "Edge 2: Single element"

    print("All tests passed!")
