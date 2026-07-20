"""
============================================================
Problem: 3Sum With Multiplicity
Pattern: Two Pointers (Advanced: Combinatorics + Duplicates)
Difficulty: Hard
Link: https://leetcode.com/problems/3sum-with-multiplicity/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Remember the standard 3Sum problem where we skipped duplicate numbers because we 
only wanted unique triplets?
Now, the rules have changed! We WANT to count the duplicates! If we have a target 
of 5, and our array is [1, 2, 2, 2], the combination (1, 2, 2) can actually be made 
in 3 different ways because there are three different "2"s we can choose from!
So instead of blindly skipping duplicates, we use math. We count how many times a 
duplicate appears. If the left side has 2 copies and the right side has 3 copies, 
that gives us 2 * 3 = 6 valid combinations instantly.

APPROACH:
---------
1. Sort the array.
2. Initialize `total_ways = 0`. Modulo `10^9 + 7` as required by large answer constraints.
3. Loop through the array with `i` from `0` to `n - 3`. Let `target = target_sum - arr[i]`.
4. Initialize `left = i + 1`, `right = n - 1`.
5. While `left < right`:
   a. If `arr[left] + arr[right] < target`, `left += 1`.
   b. If `arr[left] + arr[right] > target`, `right -= 1`.
   c. If they match the target, we found a valid pair! Now we do combinatorics:
      - Case 1: `arr[left] != arr[right]`
        Count how many duplicates of `arr[left]` exist (`count_left`).
        Count how many duplicates of `arr[right]` exist (`count_right`).
        Add `count_left * count_right` to `total_ways`.
        Move `left` forward by `count_left` and `right` backward by `count_right`.
      - Case 2: `arr[left] == arr[right]`
        This means ALL numbers between `left` and `right` are exactly the same!
        If we have `M` identical numbers, the number of ways to pick 2 of them 
        is `M * (M - 1) / 2`.
        Add this to `total_ways` and BREAK out of the `while` loop (since all pairs 
        for this `i` are exhausted).
6. Return `total_ways % (10**9 + 7)`.

COMPLEXITY:
-----------
Time:  O(N^2) — Sorting takes O(N log N). The outer loop runs N times, and the inner loop processes the remaining elements using O(N).
Space: O(1) or O(N) — Depending on sorting overhead.

EDGE CASES:
-----------
- Edge case 1: The entire array is identical numbers. Combinatorics formula handles it perfectly.
- Edge case 2: Very large number of combinations. Handled by modulo arithmetic.
============================================================
"""

def three_sum_multi(arr: list[int], target_sum: int) -> int:
    """
    Returns the number of tuples i, j, k such that i < j < k 
    and arr[i] + arr[j] + arr[k] == target.
    """
    MOD: int = 10**9 + 7
    arr.sort()
    total_ways: int = 0
    n: int = len(arr)

    for i in range(n - 2):
        target: int = target_sum - arr[i]
        left: int = i + 1
        right: int = n - 1

        while left < right:
            current_sum: int = arr[left] + arr[right]

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # MATCH FOUND! Time for combinatorics.
                
                if arr[left] != arr[right]:
                    # Count duplicates on the left
                    count_left: int = 1
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        count_left += 1
                        left += 1
                    
                    # Count duplicates on the right
                    count_right: int = 1
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        count_right += 1
                        right -= 1
                    
                    # Number of ways to combine them
                    total_ways += (count_left * count_right)
                    total_ways %= MOD
                    
                    # Move to the next distinct elements
                    left += 1
                    right -= 1
                
                else:
                    # All elements between left and right are IDENTICAL!
                    # Example: [2, 2, 2, 2], we need to pick 2 of them.
                    # Formula: M Choose 2 = M * (M - 1) // 2
                    m: int = right - left + 1
                    total_ways += (m * (m - 1)) // 2
                    total_ways %= MOD
                    
                    # Since all elements are the same, no other combinations exist for this 'i'
                    break

    return total_ways

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert three_sum_multi([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8) == 20, "Test 1 failed"
    assert three_sum_multi([1, 1, 2, 2, 2, 2], 5) == 12, "Test 2 failed: [1, 2, 2] combinations"
    
    # 🔲 Edge cases
    assert three_sum_multi([2, 2, 2, 2, 2], 6) == 10, "Edge 1: All identical elements (5 choose 3)"
    assert three_sum_multi([0, 0, 0], 0) == 1, "Edge 2: Minimum possible valid array"
    assert three_sum_multi([1, 2, 3, 4], 100) == 0, "Edge 3: Impossible target"

    print("All tests passed!")
