"""
============================================================
Problem: Minimum Window Sort
Pattern: Two Pointers (Opposite Ends)
Difficulty: Medium
Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a bookshelf where the books are mostly sorted by height, but some mischievous 
cat knocked over a chunk in the middle and scrambled them. 
You want to find the exact chunk of books you need to pull out and re-sort so the 
ENTIRE shelf is perfectly sorted.
First, you walk from the left until you find a book that is taller than the one after it. 
That's the start of the mess. Then, you walk from the right until you find a book shorter 
than the one before it. That's the end of the mess.
BUT WAIT! What if the smallest book IN the mess is actually smaller than the books 
to the left of the mess? You have to include those left books in your sorting chunk! 
Similarly, if the tallest book in the mess is taller than the books to the right, 
you must include those right books too.

APPROACH:
---------
1. Initialize `low = 0` and `high = len(arr) - 1`.
2. Find the first out-of-order element from the left:
   - `while low < len(arr) - 1 and arr[low] <= arr[low + 1]: low += 1`
   - If `low == len(arr) - 1`, the array is already sorted! Return 0.
3. Find the first out-of-order element from the right:
   - `while high > 0 and arr[high] >= arr[high - 1]: high -= 1`
4. Find the MAXIMUM and MINIMUM values within the subarray `arr[low : high+1]`.
5. Expand the subarray bounds:
   - While `low > 0` and `arr[low - 1] > subarray_min`, we decrement `low`.
   - While `high < len(arr) - 1` and `arr[high + 1] < subarray_max`, we increment `high`.
6. The required minimum window length is `high - low + 1`.

COMPLEXITY:
-----------
Time:  O(N) — We scan the array a few times, but it's purely linear.
Space: O(1) — We just store pointer indices and min/max values.

EDGE CASES:
-----------
- Edge case 1: Array is perfectly sorted. Returns 0.
- Edge case 2: Array is completely sorted in reverse. Returns `len(arr)`.
- Edge case 3: Duplicates exist. (Handled correctly by using `>=` and `<=`).
============================================================
"""

import math

def shortest_window_sort(arr: list[int]) -> int:
    """
    Finds the length of the shortest subarray that, if sorted, 
    leaves the entire array sorted.
    """
    n: int = len(arr)
    if n < 2:
        return 0

    low: int = 0
    high: int = n - 1

    # Find the first element out of sorting order from the beginning
    while low < n - 1 and arr[low] <= arr[low + 1]:
        low += 1

    # If the array is perfectly sorted
    if low == n - 1:
        return 0

    # Find the first element out of sorting order from the end
    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1

    # Find the maximum and minimum of the subarray
    subarray_min: int | float = math.inf
    subarray_max: int | float = -math.inf
    for k in range(low, high + 1):
        subarray_min = min(subarray_min, arr[k])
        subarray_max = max(subarray_max, arr[k])

    # Extend the subarray to include any number which is bigger than the minimum of the subarray
    while low > 0 and arr[low - 1] > subarray_min:
        low -= 1

    # Extend the subarray to include any number which is smaller than the maximum of the subarray
    while high < n - 1 and arr[high + 1] < subarray_max:
        high += 1

    return high - low + 1

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]) == 5, "Test 1 failed: [5, 3, 7, 10, 9]"
    assert shortest_window_sort([1, 3, 2, 0, -1, 7, 10]) == 5, "Test 2 failed: [1, 3, 2, 0, -1]"
    assert shortest_window_sort([1, 2, 3]) == 0, "Test 3 failed: Already sorted"
    
    # 🔲 Edge cases
    assert shortest_window_sort([3, 2, 1]) == 3, "Edge 1: Reverse sorted"
    assert shortest_window_sort([1, 1, 1]) == 0, "Edge 2: All identical"
    assert shortest_window_sort([2, 1]) == 2, "Edge 3: Two elements reversed"

    print("All tests passed!")
