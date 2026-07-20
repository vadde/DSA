"""
============================================================
Problem: Ceiling of a Number
Pattern: Modified Binary Search
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1c84b11f375001ff97cc
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You want to buy a pair of shoes that cost $45.
You are looking at a sorted list of price tags: `[$10, $20, $30, $40, $50, $60]`.
You don't have exactly $45, but you want to find the CHEAPEST shoe that is at 
least $45 (so you can afford it with a $50 bill). 
This is called the "Ceiling". It's the smallest number that is >= your target.
If you do a normal Binary Search for $45, you won't find it. 
Usually, Binary Search just returns `-1` if the exact number isn't there.
BUT, when the Binary Search finishes and `left` crosses over `right` (so `left > right`), 
an amazing thing happens: the `left` pointer will magically be pointing exactly 
at the Ceiling! (In this case, the $50 shoe).
Why? Because `left` only moves to the right when it sees numbers that are too 
small. It stops moving the moment it passes all the small numbers.
So, you just return `left`!

APPROACH:
---------
1. If the target is larger than the very last element in the array, there is NO 
   ceiling. Return `-1` immediately.
2. Initialize `left = 0` and `right = len(arr) - 1`.
3. Loop while `left <= right`:
   - Calculate `mid = left + (right - left) // 2`.
   - If `arr[mid] == target`, we found an exact match! Return `mid`.
   - If `target < arr[mid]`, target is on the left (`right = mid - 1`).
   - If `target > arr[mid]`, target is on the right (`left = mid + 1`).
4. We didn't find an exact match. But `left` is now pointing to the smallest 
   number greater than the target. Return `left`.

COMPLEXITY:
-----------
Time:  O(log N) — Standard binary search.
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: Target is smaller than the first element. The loop will push 
  `right` past `left`, and `left` will stay at `0`. This correctly returns index `0`.
- Edge case 2: Target is larger than the last element. Handled by step 1.
============================================================
"""

from typing import List

def search_ceiling_of_a_number(arr: List[int], key: int) -> int:
    """
    Returns the index of the smallest element in the given array greater than or equal to the key.
    """
    if not arr:
        return -1
        
    # If the key is bigger than the biggest element, there is no ceiling
    if key > arr[-1]:
        return -1
        
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == key:
            return mid
            
        if key < arr[mid]:
            right = mid - 1 # Look in the left half
        else:
            left = mid + 1  # Look in the right half
            
    # Since the loop is running until 'left <= right', at the end of the loop,
    # 'left' will be pointing to the smallest element greater than 'key'
    return left

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert search_ceiling_of_a_number([4, 6, 10], 6) == 1, "Test 1: Exact match"
    assert search_ceiling_of_a_number([1, 3, 8, 10, 15], 12) == 4, "Test 2: Ceiling is 15"
    assert search_ceiling_of_a_number([4, 6, 10], 17) == -1, "Test 3: No ceiling exists"
    
    # 🔲 Edge cases
    assert search_ceiling_of_a_number([4, 6, 10], -1) == 0, "Edge 1: Key is smaller than all elements"

    print("All tests passed!")
