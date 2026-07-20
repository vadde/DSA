"""
============================================================
Problem: 'K' Closest Numbers
Pattern: Top K Elements / Two Pointers / Binary Search
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cc59bc5746ebec8ee14
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a sorted list of numbers: `[5, 6, 7, 8, 9]`.
You are looking for the `3` numbers that are CLOSEST to the target `7`.
Since the array is already sorted, the numbers closest to `7` will be right 
next to it!
So, step 1 is to FIND where `7` (or the number closest to it) is in the array. 
Because the array is sorted, we can find it super fast using **Binary Search**!
Once we find the closest number, we put two pointers right next to it:
- `left` pointing at the closest number (or the one before it).
- `right` pointing at the one after it.
Then, we just compare the two pointers!
"Is the number at `left` closer to `7` than the number at `right`?"
- If `left` is closer, we add `left` to our list and move `left` backwards.
- If `right` is closer, we add `right` to our list and move `right` forwards.
We repeat this until we have exactly `K` numbers!
(Note: You could also solve this with a Max-Heap by dumping the closest numbers 
into it, but Two Pointers is faster because the array is already sorted!).

APPROACH:
---------
1. Create a Binary Search helper to find the index of the number closest to `X`.
   - If `X` is found, return its index.
   - If `X` is not found, return the index of the number closest to it.
2. Initialize two pointers, `left = closest_idx` and `right = closest_idx + 1`.
3. Create a `result` deque (or list).
4. Loop `K` times:
   - Calculate the distance from `arr[left]` to `X`.
   - Calculate the distance from `arr[right]` to `X`.
   - If `left` is valid and its distance is <= `right`'s distance, we pick `left`. 
     (We decrement `left`).
   - Otherwise, we pick `right` and increment `right`.
5. Return the collected numbers in sorted order.

COMPLEXITY:
-----------
Time:  O(log N + K) — Binary search takes O(log N). Expanding the window takes O(K).
       (If you used a heap, it would be O(log N + K log K)).
Space: O(K) — To store the result.

EDGE CASES:
-----------
- Edge case 1: Target `X` is smaller than all elements.
- Edge case 2: Target `X` is larger than all elements.
============================================================
"""

from typing import List
from collections import deque

def find_closest_elements(arr: List[int], K: int, X: int) -> List[int]:
    """
    Finds the K closest numbers to X in a sorted array.
    """
    # 1. Binary Search to find the closest element
    def binary_search_closest(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        # left is now pointing to the ceiling, right to the floor
        if left < len(arr) and right >= 0:
            # Return whichever is closer
            if abs(arr[left] - target) < abs(arr[right] - target):
                return left
            return right
            
        if left < len(arr):
            return left
        return right

    closest_idx = binary_search_closest(arr, X)
    
    # 2. Two pointers to expand outwards
    left = closest_idx
    right = closest_idx + 1
    
    result = deque()
    
    # 3. Collect K elements
    for _ in range(K):
        # If left is out of bounds, pick right
        if left < 0:
            result.append(arr[right])
            right += 1
        # If right is out of bounds, pick left
        elif right >= len(arr):
            result.appendleft(arr[left])
            left -= 1
        # Otherwise, compare distances
        else:
            dist_left = abs(arr[left] - X)
            dist_right = abs(arr[right] - X)
            
            if dist_left <= dist_right:
                # We use appendleft to keep the result sorted!
                result.appendleft(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
                
    return list(result)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert find_closest_elements([5, 6, 7, 8, 9], 3, 7) == [6, 7, 8], "Test 1"
    assert find_closest_elements([2, 4, 5, 6, 9], 3, 6) == [4, 5, 6], "Test 2"

    # 🔲 Edge cases
    assert find_closest_elements([2, 4, 5, 6, 9], 3, 10) == [5, 6, 9], "Edge 1: Target bigger than all"
    assert find_closest_elements([2, 4, 5, 6, 9], 3, 1) == [2, 4, 5], "Edge 2: Target smaller than all"

    print("All tests passed!")
