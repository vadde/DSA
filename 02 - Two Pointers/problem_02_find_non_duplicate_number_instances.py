"""
============================================================
Problem: Find Non-Duplicate Number Instances (Remove Duplicates)
Pattern: Two Pointers (Same Direction / Partitioning)
Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a line of people holding numbered tickets, sorted in order.
Some people have the exact same number. You are asked to send all the people 
with duplicate numbers to the back, keeping only one person per unique number 
at the front of the line.
You can't create a new line (no extra memory), you must just swap people around 
in the current line.
Since the line is sorted, all identical numbers are standing right next to each other!

APPROACH (Two Pointers - Same Direction):
-----------------------------------------
1. If the array is empty, return 0.
2. We use two pointers:
   - `next_non_duplicate` (slow pointer): Points to the index where the NEXT unique 
     element should be placed. It starts at 1, because the element at index 0 is 
     always unique (it's the first one).
   - `i` (fast pointer): Iterates through the array starting from 1.
3. Compare the current element `arr[i]` with the last unique element we saved, 
   which is at `arr[next_non_duplicate - 1]`.
4. If they are different (we found a new unique number):
   a. Overwrite `arr[next_non_duplicate]` with `arr[i]`.
   b. Increment `next_non_duplicate`.
5. Return `next_non_duplicate`, which represents the length of the subarray 
   with no duplicates.

COMPLEXITY:
-----------
Time:  O(N) — We iterate through the array exactly once with the fast pointer.
Space: O(1) — We modify the array in-place without allocating any extra structures.

EDGE CASES:
-----------
- Edge case 1: Array is empty. Return 0.
- Edge case 2: Array has all identical elements. Returns 1.
============================================================
"""

def remove_duplicates(arr: list[int]) -> int:
    """
    Modifies the array in-place to remove duplicates and returns the 
    length of the new valid subarray.
    """
    if not arr:
        return 0

    next_non_duplicate: int = 1

    for i in range(1, len(arr)):
        # If the current element is different from the last unique element we placed
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1

    return next_non_duplicate

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [2, 3, 3, 3, 6, 9, 9]
    length1 = remove_duplicates(arr1)
    assert length1 == 4, "Test 1 length failed"
    assert arr1[:length1] == [2, 3, 6, 9], "Test 1 array failed"

    arr2 = [2, 2, 2, 11]
    length2 = remove_duplicates(arr2)
    assert length2 == 2, "Test 2 length failed"
    assert arr2[:length2] == [2, 11], "Test 2 array failed"
    
    # 🔲 Edge cases
    assert remove_duplicates([]) == 0, "Edge 1: Empty array"
    assert remove_duplicates([5]) == 1, "Edge 2: Single element"
    assert remove_duplicates([1, 1, 1, 1, 1]) == 1, "Edge 3: All duplicates"

    print("All tests passed!")
