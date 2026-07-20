"""
============================================================
Problem: Search in a Sorted Infinite Array
Pattern: Modified Binary Search
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1c8a14b308e2f89f24db
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are standing on a road that stretches on forever. You are looking for house #50.
You can't do a normal Binary Search because you don't know where the road ends! 
(You can't set `right = infinity`).
Instead of starting from the edges and shrinking, we start from the beginning 
and GROW our search space exponentially!
You look at house 0 and 1. Not there.
You jump to house 3. (Range size 2). Not there.
You jump to house 7. (Range size 4). Not there.
You jump to house 15. (Range size 8). Not there.
You keep doubling the size of your range until you finally see a house number 
that is LARGER than 50. Let's say you see house 60 at index 31.
Aha! Now you have a start (index 15) and an end (index 31). 
Now you can do a perfectly normal Binary Search between those two indices!

APPROACH:
---------
1. We are given an `ArrayReader` object with a `.get(index)` method. (If index 
   is out of bounds, it usually returns Infinity).
2. Find the bounds:
   - Initialize `left = 0`, `right = 1`.
   - While `reader.get(right) < key`:
     - Calculate the new size of the window: `(right - left + 1) * 2`.
     - Update `left = right + 1`.
     - Update `right = right + new_size`.
3. Do a normal Binary Search between `left` and `right`.
   - Loop while `left <= right`:
     - `mid = left + (right - left) // 2`.
     - `if key < reader.get(mid): right = mid - 1`.
     - `elif key > reader.get(mid): left = mid + 1`.
     - `else: return mid`.
4. Return `-1` if not found.

COMPLEXITY:
-----------
Time:  O(log N) — Finding the bounds takes O(log N) steps because we double the 
       index. The binary search also takes O(log N).
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: Key is found immediately at index 0 or 1.
============================================================
"""

import math

class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader: ArrayReader, key: int) -> int:
    """
    Searches for a key in an infinite sorted array by exponentially growing the bounds.
    """
    # 1. Find the proper bounds
    left = 0
    right = 1
    
    # We keep growing the bounds as long as the key is BIGGER than the rightmost element
    while reader.get(right) < key:
        new_left = right + 1
        # Double the bound size: new_size = (right - left + 1) * 2
        # So new_right = current_right + new_size
        right += (right - left + 1) * 2
        left = new_left
        
    # 2. Perform normal Binary Search within those bounds
    while left <= right:
        mid = left + (right - left) // 2
        
        mid_val = reader.get(mid)
        
        if key == mid_val:
            return mid
        elif key < mid_val:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    
    assert search_in_infinite_array(reader, 16) == 6, "Test 1"
    assert search_in_infinite_array(reader, 11) == -1, "Test 2: Not found"
    
    # 🔲 Edge cases
    reader2 = ArrayReader([1, 3, 8, 10, 15])
    assert search_in_infinite_array(reader2, 15) == 4, "Edge 1: Last element in small array"
    assert search_in_infinite_array(reader2, 200) == -1, "Edge 2: Beyond end of array"

    print("All tests passed!")
