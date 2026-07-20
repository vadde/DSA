"""
============================================================
Problem: Search Bitonic Array
Pattern: Modified Binary Search
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1c9aa00cc465d6c8273d
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are walking on a mountain again: `[1, 3, 8, 4, 3]`.
I ask you to find the number `3`.
You can't just do a normal Binary Search, because the mountain goes UP and then DOWN.
What if you first find the peak of the mountain? (Which is `8` at index 2).
Now, the mountain is split into two perfectly sorted halves!
- The left half `[1, 3, 8]` is sorted going UP.
- The right half `[4, 3]` is sorted going DOWN.
So, you just do an Order-Agnostic Binary Search on the left half. If you find `3`, great!
If not, you do an Order-Agnostic Binary Search on the right half.

APPROACH:
---------
1. Find the maximum element in the bitonic array (from the previous problem).
2. Write a helper function `binary_search(key, left, right, is_ascending)`.
3. Try searching the left half: `binary_search(key, 0, max_index, True)`.
4. If it returns an index, return it.
5. If not, try searching the right half: `binary_search(key, max_index + 1, len(arr) - 1, False)`.
6. Return the result.

COMPLEXITY:
-----------
Time:  O(log N) — Finding the max is O(log N). Searching left is O(log N). 
       Searching right is O(log N). Total is O(log N).
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: The key isn't in the array. Returns -1.
============================================================
"""

from typing import List

def search_bitonic_array(arr: List[int], key: int) -> int:
    """
    Finds a key in a bitonic array and returns its index.
    """
    def find_max(arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
        
    def binary_search(arr, key, left, right, is_ascending):
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == key:
                return mid
                
            if is_ascending:
                if key < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if key < arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1

    # 1. Find the peak of the mountain
    max_index = find_max(arr)
    
    # 2. Search the ascending left half
    key_index = binary_search(arr, key, 0, max_index, True)
    
    # 3. If not found, search the descending right half
    if key_index == -1:
        key_index = binary_search(arr, key, max_index + 1, len(arr) - 1, False)
        
    return key_index

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert search_bitonic_array([1, 3, 8, 4, 3], 4) == 3, "Test 1"
    assert search_bitonic_array([3, 8, 3, 1], 8) == 1, "Test 2: Peak is the key"
    assert search_bitonic_array([1, 3, 8, 12], 12) == 3, "Test 3: Entirely ascending"
    assert search_bitonic_array([10, 9, 8], 10) == 0, "Test 4: Entirely descending"

    # 🔲 Edge cases
    assert search_bitonic_array([1, 3, 8, 4, 3], 9) == -1, "Edge 1: Not found"

    print("All tests passed!")
