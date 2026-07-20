"""
============================================================
Problem: Order-Agnostic Binary Search
Pattern: Modified Binary Search
Difficulty: Easy
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1c7bfbbfa0fb48c898c1
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are given a dictionary and asked to find a word.
But there's a trick! The dictionary might be sorted normally (A to Z), OR it 
might be printed backwards (Z to A)!
Before you start doing your Binary Search (ripping the book in half), you need 
to know which way the book is sorted.
How do you do that? You just look at the very first page and the very last page!
If the first page is "Apple" and the last is "Zebra", it's sorted A to Z.
If the first page is "Zebra" and the last is "Apple", it's sorted Z to A.
Once you know the direction, you do a normal Binary Search, but you just flip 
the rules for which half of the book to throw away!

APPROACH:
---------
1. Initialize `left = 0` and `right = len(arr) - 1`.
2. Check if the array is ascending: `is_ascending = arr[left] < arr[right]`.
   - (Note: if `arr[left] == arr[right]`, all elements are the same, so it 
     doesn't matter which way we assume it's sorted).
3. Loop while `left <= right`:
   - Calculate `mid = left + (right - left) // 2`.
   - If `arr[mid] == target`, return `mid`.
   - If `is_ascending`:
     - If `target < arr[mid]`, target is on the left (`right = mid - 1`).
     - Else, target is on the right (`left = mid + 1`).
   - If NOT `is_ascending` (descending):
     - If `target < arr[mid]`, target is on the RIGHT (`left = mid + 1`)!
     - Else, target is on the LEFT (`right = mid - 1`)!
4. Return `-1` if not found.

COMPLEXITY:
-----------
Time:  O(log N) — Standard binary search time.
Space: O(1) — Only using a few pointers.

EDGE CASES:
-----------
- Edge case 1: Array has only 1 element. `arr[left] == arr[right]`, loop runs once.
============================================================
"""

from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """
    Returns the index of target in the array. 
    Handles both ascending and descending sorted arrays.
    """
    if not arr:
        return -1
        
    left = 0
    right = len(arr) - 1
    
    # Determine the sorting order
    is_ascending = arr[left] <= arr[right]
    
    while left <= right:
        # Avoid potential integer overflow
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
            
        if is_ascending:
            if target < arr[mid]:
                right = mid - 1 # Throw away right half
            else:
                left = mid + 1  # Throw away left half
        else:
            if target < arr[mid]:
                left = mid + 1  # Throw away left half (because small numbers are on the right!)
            else:
                right = mid - 1 # Throw away right half
                
    return -1

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert binary_search([4, 6, 10], 10) == 2, "Test 1: Ascending"
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 5) == 4, "Test 2: Ascending"
    assert binary_search([10, 6, 4], 10) == 0, "Test 3: Descending"
    assert binary_search([10, 6, 4], 4) == 2, "Test 4: Descending"

    # 🔲 Edge cases
    assert binary_search([5], 5) == 0, "Edge 1: Single element found"
    assert binary_search([5], 10) == -1, "Edge 2: Single element not found"
    assert binary_search([], 10) == -1, "Edge 3: Empty array"

    print("All tests passed!")
