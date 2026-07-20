"""
============================================================
Problem: Triplet Sum to Zero
Pattern: Two Pointers (Opposite Ends)
Difficulty: Medium
Link: https://leetcode.com/problems/3sum/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you want to find three blocks that add up exactly to zero.
Finding three things at once is hard! But what if we pick ONE block first (let's say 
a block with a value of -5)? Now the problem gets much simpler: we just need to find 
TWO other blocks that add up to +5 so that they all cancel out to zero!
So, we can sort all our blocks, pick one block at a time (from left to right), and 
then use our "Two Pointers" trick on the remaining blocks to find the matching pair.
We just have to be careful to skip identical blocks so we don't accidentally write 
down the exact same winning trio twice.

APPROACH:
---------
1. Sort the input array. This is crucial for Two Pointers to work and to easily skip duplicates.
2. Loop through the array, using `i` as the index of our "pinned" first element.
   a. To avoid duplicate triplets, if `i > 0` and `arr[i] == arr[i-1]`, we `continue` 
      to skip it.
   b. The target for our two pointers will be `-arr[i]`.
   c. Set `left = i + 1` and `right = len(arr) - 1`.
3. While `left < right`:
   a. Calculate `current_sum = arr[left] + arr[right]`.
   b. If `current_sum == target`:
      - We found a valid triplet! Add `[arr[i], arr[left], arr[right]]` to results.
      - Move BOTH pointers inward: `left += 1` and `right -= 1`.
      - Skip duplicates for the inner pointers: 
        `while left < right and arr[left] == arr[left - 1]: left += 1`
        `while left < right and arr[right] == arr[right + 1]: right -= 1`
   c. If `current_sum < target`, we need a larger sum: `left += 1`.
   d. If `current_sum > target`, we need a smaller sum: `right -= 1`.
4. Return the list of triplets.

COMPLEXITY:
-----------
Time:  O(N log N + N^2) = O(N^2) — Sorting takes O(N log N). We then iterate N times, and for each iteration, the two pointers take O(N).
Space: O(1) or O(N) — Ignoring the space required for the output array, the space complexity is dependent on the sorting algorithm which typically takes O(N) memory in Python (Timsort).

EDGE CASES:
-----------
- Edge case 1: Array has fewer than 3 elements. Returns empty list.
- Edge case 2: Array contains all zeros (`[0, 0, 0, 0]`). Should correctly return `[[0, 0, 0]]` just once.
============================================================
"""

def search_triplets(arr: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets in the array that add up to zero.
    """
    arr.sort()
    triplets: list[list[int]] = []
    n: int = len(arr)

    for i in range(n - 2):
        # Skip duplicate elements for the first part of the triplet
        if i > 0 and arr[i] == arr[i - 1]:
            continue
            
        target: int = -arr[i]
        left: int = i + 1
        right: int = n - 1

        while left < right:
            current_sum: int = arr[left] + arr[right]

            if current_sum == target:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                
                # Skip duplicate elements for the second part of the triplet
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                # Skip duplicate elements for the third part of the triplet
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return triplets

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert search_triplets([-3, 0, 1, 2, -1, 1, -2]) == [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]], "Test 1 failed"
    assert search_triplets([-5, 2, -1, -2, 3]) == [[-5, 2, 3], [-2, -1, 3]], "Test 2 failed"
    
    # 🔲 Edge cases
    assert search_triplets([0, 0, 0, 0]) == [[0, 0, 0]], "Edge 1: All zeros"
    assert search_triplets([1, 2, 3]) == [], "Edge 2: No valid triplets"
    assert search_triplets([]) == [], "Edge 3: Empty array"

    print("All tests passed!")
