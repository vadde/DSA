"""
============================================================
Problem: Search in Rotated Array
Pattern: Modified Binary Search
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1c9fa00cc465d6c82743
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a sorted array: `[1, 2, 3, 4, 5, 6, 7]`.
Someone comes along, chops it into two pieces, and swaps the pieces!
Now it looks like this: `[5, 6, 7, 1, 2, 3, 4]`.
We call this a "Rotated Array".
Can we still use Binary Search? YES!
If you cut a rotated array in half, AT LEAST ONE of those halves will be 
perfectly sorted. Always. Guaranteed.
Let's look at `mid` (which is `1`).
Left half is `[5, 6, 7, 1]`. (Not sorted perfectly).
Right half is `[1, 2, 3, 4]`. (Perfectly sorted!).
So, to find our number:
1. Find which half is perfectly sorted.
2. Check if our number fits inside the perfectly sorted half.
3. If it fits, we throw away the messy half and search the perfect half!
4. If it doesn't fit, we throw away the perfect half and search the messy half!

APPROACH:
---------
1. Initialize `left = 0`, `right = len(arr) - 1`.
2. Loop while `left <= right`:
   - `mid = left + (right - left) // 2`.
   - If `arr[mid] == key`, return `mid`.
   - Check if the LEFT side is sorted: `if arr[left] <= arr[mid]:`
     - If yes, is the key inside it? `if arr[left] <= key < arr[mid]:`
       - If yes, search left (`right = mid - 1`).
       - If no, search right (`left = mid + 1`).
   - If the LEFT side isn't sorted, the RIGHT side MUST be sorted! `else:`
     - Is the key inside it? `if arr[mid] < key <= arr[right]:`
       - If yes, search right (`left = mid + 1`).
       - If no, search left (`right = mid - 1`).
3. Return `-1`.

COMPLEXITY:
-----------
Time:  O(log N) — Still discarding half the array every time!
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: Array is not rotated at all (`[1, 2, 3]`). The left side will 
  evaluate to sorted, and it will just do a standard Binary Search.
============================================================
"""

from typing import List

def search_rotated_array(arr: List[int], key: int) -> int:
    """
    Finds a key in a rotated sorted array and returns its index.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == key:
            return mid
            
        # 1. Determine which half is perfectly sorted
        # If the left number is smaller than or equal to the middle number, 
        # the left half is sorted!
        if arr[left] <= arr[mid]:
            
            # 2. Check if the key lies strictly within this sorted left half
            if arr[left] <= key < arr[mid]:
                right = mid - 1 # Yes! Throw away the right half.
            else:
                left = mid + 1  # No! It must be in the right half.
                
        # If the left half ISN'T sorted, then the right half MUST be sorted!
        else:
            
            # 2. Check if the key lies strictly within this sorted right half
            if arr[mid] < key <= arr[right]:
                left = mid + 1  # Yes! Throw away the left half.
            else:
                right = mid - 1 # No! It must be in the left half.
                
    return -1

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert search_rotated_array([10, 15, 1, 3, 8], 15) == 1, "Test 1"
    assert search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10) == 4, "Test 2"

    # 🔲 Edge cases
    assert search_rotated_array([1, 2, 3, 4, 5], 4) == 3, "Edge 1: Not actually rotated"
    assert search_rotated_array([4, 5, 7, 9, 10, -1, 2], 11) == -1, "Edge 2: Not found"
    assert search_rotated_array([5, 1], 1) == 1, "Edge 3: Two elements"

    print("All tests passed!")
