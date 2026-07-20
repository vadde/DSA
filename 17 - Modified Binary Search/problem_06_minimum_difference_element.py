"""
============================================================
Problem: Minimum Difference Element
Pattern: Modified Binary Search
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1c93a00cc465d6c82737
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are looking for the number `7` in a list: `[1, 3, 8, 10, 15]`.
But `7` isn't in the list!
So, you want to find the number that is CLOSEST to `7`.
If we do a normal Binary Search, what happens when we don't find the number?
The pointers `left` and `right` cross each other.
Specifically, `left` ends up pointing to the smallest number GREATER than `7` (the ceiling).
And `right` ends up pointing to the largest number SMALLER than `7` (the floor).
In our list, `left` will point to `8`, and `right` will point to `3`.
The closest number to `7` MUST be one of those two!
So we just check the math: `8 - 7 = 1`. `7 - 3 = 4`.
`8` is closer, so we return `8`!

APPROACH:
---------
1. Edge cases: If the key is smaller than the first element, the first element is closest. 
   If the key is larger than the last element, the last element is closest.
2. Initialize `left = 0`, `right = len(arr) - 1`.
3. Loop while `left <= right`:
   - `mid = left + (right - left) // 2`
   - If `key == arr[mid]`, we found an exact match. Return `arr[mid]`.
   - If `key < arr[mid]`, target is on the left (`right = mid - 1`).
   - If `key > arr[mid]`, target is on the right (`left = mid + 1`).
4. At the end of the loop, `arr[left]` is the ceiling and `arr[right]` is the floor.
5. Check which one has a smaller absolute difference to `key` and return it.

COMPLEXITY:
-----------
Time:  O(log N) — Standard binary search.
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: Array has 1 element.
============================================================
"""

from typing import List

def search_min_diff_element(arr: List[int], key: int) -> int:
    """
    Returns the element in the array that has the minimum difference with the key.
    """
    if not arr:
        raise ValueError("Array cannot be empty")
        
    # If the key is out of bounds, the closest is an endpoint!
    if key < arr[0]:
        return arr[0]
    if key > arr[-1]:
        return arr[-1]
        
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if key == arr[mid]:
            return arr[mid]
            
        if key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    # At this point, left > right.
    # arr[left] is the ceiling, arr[right] is the floor.
    # Let's find which one is closer.
    
    # We know arr[left] > key, and key > arr[right]
    if (arr[left] - key) < (key - arr[right]):
        return arr[left]
    else:
        return arr[right]

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert search_min_diff_element([4, 6, 10], 7) == 6, "Test 1: Floor is closer"
    assert search_min_diff_element([4, 6, 10], 4) == 4, "Test 2: Exact match"
    assert search_min_diff_element([1, 3, 8, 10, 15], 12) == 10, "Test 3: Floor is closer"
    assert search_min_diff_element([4, 6, 10], 17) == 10, "Test 4: Out of bounds (right)"
    
    # 🔲 Edge cases
    assert search_min_diff_element([4, 6, 10], -1) == 4, "Edge 1: Out of bounds (left)"
    assert search_min_diff_element([5], 10) == 5, "Edge 2: Single element"

    print("All tests passed!")
