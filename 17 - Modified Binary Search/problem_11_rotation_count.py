"""
============================================================
Problem: Rotation Count
Pattern: Modified Binary Search
Difficulty: Medium (Advanced)
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1ca29bc5746ebec8eddf
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a perfectly sorted list: `[1, 2, 3, 4, 5]`.
Someone rotated it twice! `[4, 5, 1, 2, 3]`.
Notice that the smallest number (`1`) is now at index `2`.
The number of times the array was rotated is exactly equal to the INDEX of the 
smallest element!
So this problem is just asking: "Find the index of the minimum element!"
How do we find the minimum element with Binary Search?
Look at `mid`. Compare it with `right`.
If `arr[mid] > arr[right]`, it means the right side is wrapping around! 
Like `[4, 5, 1, 2]`. Mid is `5`, Right is `2`. The only way a number on the left 
is bigger than a number on the right is if the rotation happened between them!
So the minimum MUST be to the right of `mid`.
If `arr[mid] <= arr[right]`, it means the right side is perfectly sorted!
Like `[1, 2, 3]`. Mid is `2`, Right is `3`.
If the right side is perfectly sorted and increasing, the minimum CANNOT be there. 
It must be `mid` or somewhere to the left of `mid`.

APPROACH:
---------
1. Initialize `left = 0`, `right = len(arr) - 1`.
2. Loop while `left < right`: (We want them to converge on the minimum).
3. `mid = left + (right - left) // 2`.
4. If `arr[mid] > arr[right]`:
   - The array wraps around between `mid` and `right`.
   - The minimum is to the right!
   - `left = mid + 1`.
5. Else (`arr[mid] <= arr[right]`):
   - The right side is perfectly sorted.
   - The minimum is at `mid` or to the left!
   - `right = mid`.
6. When the loop finishes, `left == right`, pointing to the minimum element.
7. Return `left` (which is the rotation count).

COMPLEXITY:
-----------
Time:  O(log N) — Standard binary search.
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: Array is not rotated (`[1, 2, 3]`). `arr[mid] <= arr[right]` will 
  always trigger, shrinking `right` down to `0`. It returns `0` rotations!
============================================================
"""

from typing import List

def count_rotations(arr: List[int]) -> int:
    """
    Finds the number of times a sorted array has been rotated.
    This is equivalent to finding the index of the minimum element.
    """
    left = 0
    right = len(arr) - 1
    
    # We want left and right to converge on the minimum element
    while left < right:
        mid = left + (right - left) // 2
        
        # If mid is greater than the rightmost element, the wrap-around 
        # MUST happen to the right of mid.
        if arr[mid] > arr[right]:
            left = mid + 1
        # Otherwise, the right side is sorted, so the minimum is at mid 
        # or to the left of mid.
        else:
            right = mid
            
    # The index of the minimum element is the number of rotations!
    return left

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert count_rotations([10, 15, 1, 3, 8]) == 2, "Test 1"
    assert count_rotations([4, 5, 7, 9, 10, -1, 2]) == 5, "Test 2"

    # 🔲 Edge cases
    assert count_rotations([1, 3, 8, 10]) == 0, "Edge 1: Not rotated"
    assert count_rotations([5, 1]) == 1, "Edge 2: Two elements"

    print("All tests passed!")
