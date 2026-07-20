"""
============================================================
Problem: Find the First K Missing Positive Numbers
Pattern: Cyclic Sort
Difficulty: Hard
Link: https://www.educative.io/courses/grokking-the-coding-interview/q2LA7G0ANX2
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have your messy room full of toys, just like the last problem. 
But this time, your parents want you to find the first 'K' missing positive 
toy numbers. (Like, find the first 3 missing toys starting from 1).
First, we do the exact same trick: Cyclic Sort. We try to put Toy 1 in Spot 1, 
Toy 2 in Spot 2... ignoring negatives and toys with huge numbers.
When we are done sorting, we walk through the spots. 
If Spot 1 doesn't have Toy 1, then Toy 1 is missing! We write down "1".
But wait! What if the toy sitting in Spot 1 is Toy 100?
Toy 100 is an "extra" toy that we don't care about right now, but we need to 
remember we have it. Why? Because if we still need to find more missing numbers 
after checking all N spots, we have to start counting up: N+1, N+2, N+3...
If we accidentally say "Oh, Toy 100 is missing," we'd be wrong, because it was 
sitting right there in Spot 1!
So we keep a little notepad (`extra_numbers` set) to write down any out-of-bounds 
toys we see sitting in wrong spots. Then we can safely count up past N without 
making a mistake.

APPROACH:
---------
1. Initialize `i = 0`.
2. Loop through the array using a `while` loop to Cyclic Sort, ignoring out-of-bounds numbers.
3. Initialize `missing_numbers = []` and `extra_numbers = set()`.
4. Loop `i` from `0` to `N - 1`:
   - If we have found `k` missing numbers, break.
   - If `nums[i] != i + 1`:
     - The number `i + 1` is missing. Add it to `missing_numbers`.
     - The number currently sitting here (`nums[i]`) is an extra out-of-bounds number. 
       Add it to `extra_numbers`.
5. If we STILL need more numbers (`len(missing_numbers) < k`), we start checking numbers 
   greater than N (`candidate = N + 1`).
6. While `len(missing_numbers) < k`:
   - If `candidate` is NOT in `extra_numbers`, it's truly missing! Add it.
   - `candidate += 1`
7. Return `missing_numbers`.

COMPLEXITY:
-----------
Time:  O(N + K) — O(N) to sort and scan, O(K) to find the remaining numbers if they are beyond N.
Space: O(K) — To store the `extra_numbers` set and the `missing_numbers` list.

EDGE CASES:
-----------
- Edge case 1: K is larger than the number of missing numbers inside the array. The `while` loop takes over.
- Edge case 2: The array is perfectly sorted from 1 to N. Returns `N+1` to `N+K`.
============================================================
"""

def find_first_k_missing_positive(nums: list[int], k: int) -> list[int]:
    """
    Finds the first K missing positive numbers in an unsorted array.
    """
    i: int = 0
    n: int = len(nums)

    # 1. Sort the array using Cyclic Sort
    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers: list[int] = []
    extra_numbers: set[int] = set()

    # 2. Find missing numbers within the bounds of the array
    for i in range(n):
        if len(missing_numbers) < k:
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
                # Keep track of the out-of-bounds number that stole this spot
                extra_numbers.add(nums[i])
        else:
            break

    # 3. If we still need more missing numbers, look beyond N
    candidate: int = n + 1
    while len(missing_numbers) < k:
        if candidate not in extra_numbers:
            missing_numbers.append(candidate)
        candidate += 1

    return missing_numbers

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [3, -1, 4, 5, 5]
    assert find_first_k_missing_positive(arr1, 3) == [1, 2, 6], "Test 1 failed"

    arr2 = [2, 3, 4]
    assert find_first_k_missing_positive(arr2, 3) == [1, 5, 6], "Test 2 failed"
    
    # 🔲 Edge cases
    arr3 = [-2, -3, 4]
    assert find_first_k_missing_positive(arr3, 2) == [1, 2], "Edge 1: Missing before and inside"

    print("All tests passed!")
