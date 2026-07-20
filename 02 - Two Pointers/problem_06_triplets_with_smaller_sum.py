"""
============================================================
Problem: Triplets with Smaller Sum
Pattern: Two Pointers (Opposite Ends)
Difficulty: Medium
Link: https://leetcode.com/problems/3sum-smaller/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you want to buy 3 toys, and you only have $20 total. You want to know 
HOW MANY different combinations of 3 toys you can afford.
You line up all the toys from cheapest to most expensive. You pick one toy first.
Now you just need to find two more toys that cost less than the money you have left.
Because they are sorted, if the cheapest toy (left) and the most expensive toy (right) 
combined are affordable, then that cheapest toy paired with ANY toy in between will 
ALSO be affordable! So instead of counting them one by one, you can just count 
the whole chunk at once!

APPROACH:
---------
1. Sort the array.
2. Initialize `count = 0`.
3. Loop through the array, using `i` as the pinned element.
   a. Set `target = target_sum - arr[i]`.
   b. Set `left = i + 1` and `right = len(arr) - 1`.
4. While `left < right`:
   a. If `arr[left] + arr[right] < target`:
      - MAGIC MATH: Since the array is sorted, if `arr[right]` is valid with `arr[left]`, 
        then `arr[right-1]`, `arr[right-2]`, ... down to `arr[left+1]` are ALSO valid 
        with `arr[left]`.
      - We can instantly add `right - left` to our count.
      - Increment `left` to find combinations for the next number.
   b. If `arr[left] + arr[right] >= target`:
      - The sum is too big. We need a smaller number, so decrement `right`.
5. Return the `count`.

COMPLEXITY:
-----------
Time:  O(N log N + N^2) = O(N^2) — Sorting takes O(N log N), and we iterate with Two Pointers taking O(N^2).
Space: O(1) or O(N) — Depending on the sorting algorithm.

EDGE CASES:
-----------
- Edge case 1: No triplets sum to less than the target. Returns 0.
- Edge case 2: Duplicates exist. (We don't need to skip them uniquely unless the problem asks for UNIQUE triplets. This problem just asks for count of combinations, so indices matter, not distinct values).
============================================================
"""

def triplet_with_smaller_sum(arr: list[int], target_sum: int) -> int:
    """
    Returns the count of triplets whose sum is less than the target_sum.
    """
    arr.sort()
    count: int = 0
    n: int = len(arr)

    for i in range(n - 2):
        target: int = target_sum - arr[i]
        left: int = i + 1
        right: int = n - 1

        while left < right:
            if arr[left] + arr[right] < target:
                # If arr[left] + arr[right] < target, then everything between 
                # left and right is also < target when paired with arr[left].
                # E.g. [1, 2, 3, 4, 5], target = 7. If 1+5 = 6 < 7, then 1+4, 1+3, 1+2 are also < 7.
                # The number of such pairs is exactly (right - left)
                count += (right - left)
                # Move left to find more valid combinations using the next smallest number
                left += 1
            else:
                # Sum is too large, try a smaller right pointer
                right -= 1

    return count

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert triplet_with_smaller_sum([-1, 0, 2, 3], 3) == 2, "Test 1 failed: [-1, 0, 3], [-1, 0, 2]"
    assert triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5) == 4, "Test 2 failed: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]"
    
    # 🔲 Edge cases
    assert triplet_with_smaller_sum([1, 2, 3, 4], 0) == 0, "Edge 1: Impossible target"
    assert triplet_with_smaller_sum([1, 1, 1, 1], 4) == 4, "Edge 2: Duplicates counting"

    print("All tests passed!")
