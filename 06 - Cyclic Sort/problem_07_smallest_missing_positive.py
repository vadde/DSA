"""
============================================================
Problem: Find the Smallest Missing Positive Number
Pattern: Cyclic Sort
Difficulty: Medium
Link: https://leetcode.com/problems/first-missing-positive/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a really messy room full of toys. Some toys have negative numbers (like -5), 
some have zero (0), and some have huge numbers (like 1,000,000). 
Your parents tell you to find the SMALLEST positive toy number that is missing 
from your room. Positive numbers start at 1, 2, 3...
Because your room can only hold N toys total, the smallest missing positive number 
MUST be between 1 and N+1.
Why? If your room holds 5 toys, the best you could possibly do is have toys 1, 2, 3, 4, 5. 
In that perfect case, the missing one is 6. In any other case, it's 1, 2, 3, 4, or 5.
So, we use Cyclic Sort to try and put Toy 1 in Spot 1, Toy 2 in Spot 2...
If we find a toy like -5 or 1,000,000, we just IGNORE IT! It doesn't belong in 
Spots 1 to N, so we just let it sit wherever it lands.
After sorting, we walk through the spots. The first spot that doesn't have the 
right toy is our answer!

APPROACH:
---------
1. Initialize `i = 0`.
2. Loop through the array using a `while` loop.
3. The correct index for a number `nums[i]` is `j = nums[i] - 1`.
4. We ONLY care about `nums[i]` if it's a valid positive number that fits in our array:
   - `0 < nums[i] <= len(nums)`
5. If it is valid AND not already at its correct spot (`nums[i] != nums[j]`):
   - Swap them!
6. Else:
   - Increment `i += 1`. (This naturally skips negative numbers and numbers > N).
7. Second pass: find the first index `i` where `nums[i] != i + 1`.
8. Return `i + 1`.
9. If all spots are perfectly filled with 1 to N, then the answer is `len(nums) + 1`.

COMPLEXITY:
-----------
Time:  O(N) — One pass to sort (ignoring out-of-bounds numbers), one pass to check.
Space: O(1) — Sorting is done completely in-place.

EDGE CASES:
-----------
- Edge case 1: All negative numbers. First pass does nothing, second pass immediately returns 1.
- Edge case 2: Perfectly sorted `1` to `N`. Returns `N + 1`.
============================================================
"""

def find_first_smallest_missing_positive(nums: list[int]) -> int:
    """
    Finds the smallest missing positive integer in O(N) time and O(1) space.
    """
    i: int = 0
    n: int = len(nums)

    # 1. Sort the array using Cyclic Sort, ignoring out-of-bounds numbers
    while i < n:
        j = nums[i] - 1
        
        # Only swap if the number is a valid positive integer that fits in our array
        # AND it is not already in the correct position
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # 2. Second pass to find the first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # 3. If the array has all numbers from 1 to N, the missing one is N + 1
    return n + 1

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [-3, 1, 5, 4, 2]
    assert find_first_smallest_missing_positive(arr1) == 3, "Test 1 failed"

    arr2 = [3, -2, 0, 1, 2]
    assert find_first_smallest_missing_positive(arr2) == 4, "Test 2 failed"
    
    # 🔲 Edge cases
    arr3 = [3, 2, 5, 1]
    assert find_first_smallest_missing_positive(arr3) == 4, "Edge 1: Missing number in the middle"
    
    arr4 = [1, 2, 3]
    assert find_first_smallest_missing_positive(arr4) == 4, "Edge 2: Perfect array, missing is N+1"

    arr5 = [-1, -2, -3]
    assert find_first_smallest_missing_positive(arr5) == 1, "Edge 3: All negatives"

    print("All tests passed!")
