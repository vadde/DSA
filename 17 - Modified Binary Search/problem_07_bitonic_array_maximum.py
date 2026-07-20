"""
============================================================
Problem: Bitonic Array Maximum
Pattern: Modified Binary Search
Difficulty: Easy
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1c9aa00cc465d6c8273d
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are walking up a mountain. `[1, 3, 8, 12, 4, 2]`
At first, the numbers keep getting bigger (`1 -> 3 -> 8 -> 12`).
Then, they start getting smaller (`12 -> 4 -> 2`).
We want to find the very top of the mountain (the peak)!
Because the mountain only goes up once, and then goes down once, we can use 
Binary Search to find the peak!
We look at a number (like `8`), and we compare it to the next number (`12`).
Because `8 < 12`, we know we are still walking UPHILL. The peak must be to the right!
If we look at `4`, and compare it to the next number `2`, we see `4 > 2`.
We are walking DOWNHILL. The peak must be to the left (or it could be `4` itself)!
We keep shrinking our search space until `left` and `right` point to the exact 
same number. That number is the peak!

APPROACH:
---------
1. Initialize `left = 0`, `right = len(arr) - 1`.
2. Loop while `left < right`: (Notice we use `<` instead of `<=`. We want them to meet at the peak).
3. `mid = left + (right - left) // 2`.
4. If `arr[mid] > arr[mid + 1]`:
   - We are on the descending part of the mountain.
   - The maximum could be `arr[mid]`, or it could be somewhere to the left.
   - So we set `right = mid`. (Not `mid - 1`, because `mid` might be the peak!)
5. If `arr[mid] <= arr[mid + 1]`:
   - We are on the ascending part of the mountain.
   - The maximum MUST be to the right of `mid`. It cannot be `mid` itself.
   - So we set `left = mid + 1`.
6. When the loop ends, `left == right`, and they are pointing to the maximum!
7. Return `arr[left]`.

COMPLEXITY:
-----------
Time:  O(log N) — Standard binary search.
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: Array is entirely increasing. `left` will move all the way to `right`.
- Edge case 2: Array is entirely decreasing. `right` will move all the way to `left`.
============================================================
"""

from typing import List

def find_max_in_bitonic_array(arr: List[int]) -> int:
    """
    Returns the maximum value in a given Bitonic array.
    """
    left = 0
    right = len(arr) - 1
    
    # Notice the loop condition is strictly less than.
    # We want left and right to converge on the single max element.
    while left < right:
        mid = left + (right - left) // 2
        
        # Compare mid with the next element
        if arr[mid] > arr[mid + 1]:
            # We are going downhill. The peak is at mid or to the left.
            right = mid
        else:
            # We are going uphill. The peak is to the right of mid.
            left = mid + 1
            
    # At the end of the loop, left == right, pointing to the peak!
    return arr[left]

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]) == 12, "Test 1"
    assert find_max_in_bitonic_array([3, 8, 3, 1]) == 8, "Test 2"
    assert find_max_in_bitonic_array([1, 3, 8, 12]) == 12, "Test 3: Entirely ascending"
    assert find_max_in_bitonic_array([10, 9, 8]) == 10, "Test 4: Entirely descending"

    print("All tests passed!")
