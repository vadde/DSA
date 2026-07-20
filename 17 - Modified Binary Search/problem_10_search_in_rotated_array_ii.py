"""
============================================================
Problem: Search in Rotated Array II
Pattern: Modified Binary Search
Difficulty: Medium (Advanced)
Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
This is EXACTLY the same as searching in a rotated array, but now there can 
be duplicate numbers.
Normally, we check if the left half is perfectly sorted by asking: 
"Is the left number smaller than or equal to the middle number?"
But what if the array is `[3, 1, 2, 3, 3, 3, 3]`?
Left is 3. Middle is 3. Right is 3.
Is the left half sorted? NO. (It contains `[3, 1, 2, 3]`).
Is the right half sorted? YES. (It contains `[3, 3, 3]`).
Because `left`, `mid`, and `right` are all the same number, we are BLIND. 
We can't tell which half is the clean, sorted half!
So, what do we do? We just take a tiny step inward!
We throw away the `left` number (`left += 1`) and we throw away the `right` 
number (`right -= 1`).
We can safely do this because we already know that `mid` is not our target (we 
check `arr[mid] == target` before anything else). Since `left` and `right` are 
equal to `mid`, they aren't our target either!

APPROACH:
---------
1. Initialize `left = 0`, `right = len(arr) - 1`.
2. Loop while `left <= right`:
   - `mid = left + (right - left) // 2`.
   - If `arr[mid] == key`, return `True` (or the index).
   - If `arr[left] == arr[mid] == arr[right]`:
     - We are blind! Just shrink the window: `left += 1`, `right -= 1`.
     - `continue` to the next loop iteration.
   - Else if `arr[left] <= arr[mid]`: (Left side is sorted)
     - Check if key is inside: `arr[left] <= key < arr[mid]`
       - If yes: `right = mid - 1`
       - If no: `left = mid + 1`
   - Else: (Right side is sorted)
     - Check if key is inside: `arr[mid] < key <= arr[right]`
       - If yes: `left = mid + 1`
       - If no: `right = mid - 1`
3. Return `False` (or `-1` if returning index).

COMPLEXITY:
-----------
Time:  O(log N) average. O(N) worst case! If the array is `[1, 1, 1, 1, 1, 1]` 
       and we are looking for `2`, we have to shrink the array one step at a 
       time, which takes N steps.
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: Array is entirely duplicates except for the key.
============================================================
"""

from typing import List

def search_rotated_array_with_duplicates(arr: List[int], key: int) -> bool:
    """
    Returns True if key is in the rotated sorted array (which may contain duplicates).
    (LeetCode expects a boolean for this problem, but we could also return an index).
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == key:
            return True
            
        # The ONLY difference from standard Rotated Array Search:
        # If we have duplicates at the ends and the middle, we can't tell which half is sorted.
        if arr[left] == arr[mid] and arr[mid] == arr[right]:
            left += 1
            right -= 1
            continue
            
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        # Right half is sorted
        else:
            if arr[mid] < key <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return False

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert search_rotated_array_with_duplicates([3, 7, 3, 3, 3], 7) == True, "Test 1"
    assert search_rotated_array_with_duplicates([3, 1, 2, 3, 3, 3, 3], 2) == True, "Test 2"

    # 🔲 Edge cases
    assert search_rotated_array_with_duplicates([1, 1, 1, 1, 1], 2) == False, "Edge 1: All duplicates"
    assert search_rotated_array_with_duplicates([1], 1) == True, "Edge 2: Single element"

    print("All tests passed!")
