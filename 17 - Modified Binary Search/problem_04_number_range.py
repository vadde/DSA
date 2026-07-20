"""
============================================================
Problem: Number Range
Pattern: Modified Binary Search
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1c8a14b308e2f89f24db
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are looking at a sorted list of numbers: `[1, 3, 8, 8, 8, 8, 10, 15]`.
I ask you: "Where are all the 8s?"
Because they are sorted, all the 8s are clumped together in a single group.
If you just do a normal Binary Search for `8`, it might land directly on the 
middle `8` (at index 4) and return it. But that doesn't tell us where the 
group *starts* and *ends*!
To find the exact range, we do Binary Search TWICE.
1. The Left Border Search: We do a normal search, but when we find an `8`, we 
   say "Cool, but are there more 8s to the left?" and we FORCE the search to 
   keep looking in the left half!
2. The Right Border Search: We do a normal search, but when we find an `8`, we 
   say "Cool, but are there more 8s to the right?" and we FORCE the search to 
   keep looking in the right half!

APPROACH:
---------
1. Define a helper function `find_index(find_max_index: bool)`.
2. Initialize `key_index = -1`, `left = 0`, `right = len(arr) - 1`.
3. Loop while `left <= right`:
   - Calculate `mid`.
   - If `key < arr[mid]`, search left (`right = mid - 1`).
   - If `key > arr[mid]`, search right (`left = mid + 1`).
   - If `key == arr[mid]`:
     - We found a match! Save it: `key_index = mid`.
     - Now, which way do we keep exploring?
     - If `find_max_index` is True, we want the rightmost boundary. So we throw 
       away the left half and search the right (`left = mid + 1`).
     - If `find_max_index` is False, we want the leftmost boundary. So we throw 
       away the right half and search the left (`right = mid - 1`).
4. In the main function, call `find_index(False)` to get the start index.
5. If the start index isn't `-1`, call `find_index(True)` to get the end index!
6. Return `[start_index, end_index]`.

COMPLEXITY:
-----------
Time:  O(log N) — We do two binary searches. O(log N) + O(log N) = O(log N).
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: Array doesn't contain the key. Returns `[-1, -1]`.
- Edge case 2: Array contains exactly ONE instance of the key. Start and End 
  will be the same index.
============================================================
"""

from typing import List

def find_range(arr: List[int], key: int) -> List[int]:
    """
    Returns the [start, end] range of indices where 'key' appears in the array.
    """
    def search(find_max_index: bool) -> int:
        key_index = -1
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if key < arr[mid]:
                right = mid - 1
            elif key > arr[mid]:
                left = mid + 1
            else:
                # We found the key! Record it.
                key_index = mid
                
                # But don't stop! Keep searching for the boundary.
                if find_max_index:
                    left = mid + 1 # Force search to the right for the maximum index
                else:
                    right = mid - 1 # Force search to the left for the minimum index
                    
        return key_index

    # 1. Find the left boundary
    start_idx = search(False)
    
    # 2. Find the right boundary (only if the key actually exists!)
    end_idx = -1
    if start_idx != -1:
        end_idx = search(True)
        
    return [start_idx, end_idx]

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert find_range([4, 6, 6, 6, 9], 6) == [1, 3], "Test 1"
    assert find_range([1, 3, 8, 10, 15], 10) == [3, 3], "Test 2: Single instance"
    assert find_range([1, 3, 8, 10, 15], 12) == [-1, -1], "Test 3: Not found"

    # 🔲 Edge cases
    assert find_range([6, 6, 6, 6, 6], 6) == [0, 4], "Edge 1: All identical"
    assert find_range([], 6) == [-1, -1], "Edge 2: Empty array"

    print("All tests passed!")
