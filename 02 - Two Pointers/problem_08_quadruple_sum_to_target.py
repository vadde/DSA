"""
============================================================
Problem: Quadruple Sum to Target (4Sum)
Pattern: Two Pointers (Opposite Ends + Nested Loops)
Difficulty: Medium / Hard
Link: https://leetcode.com/problems/4sum/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Remember when we looked for THREE numbers that add up to a target? We picked one 
number to "pin" down, and then used two pointers to find the other two.
Now we need FOUR numbers. The logic is exactly the same, but we just need to "pin" 
down TWO numbers first! 
So, we use two outer loops to pick the first and second numbers. Then, we use our 
trusted two pointers to find the third and fourth numbers. We just have to be extra 
careful to skip duplicates at EVERY step so we don't return the same set of four 
numbers twice.

APPROACH:
---------
1. Sort the input array.
2. Iterate `i` from 0 to `n - 3`. This is our first pinned number.
   - Skip duplicates for `i`: `if i > 0 and arr[i] == arr[i-1]`.
3. Iterate `j` from `i + 1` to `n - 2`. This is our second pinned number.
   - Skip duplicates for `j`: `if j > i + 1 and arr[j] == arr[j-1]`.
4. Now we need to find two numbers that sum up to `target - arr[i] - arr[j]`.
   - Set `left = j + 1` and `right = n - 1`.
   - Run the standard Two Pointers (Opposite Ends) loop.
5. When a valid quadruplet is found, add it to results, increment `left`, decrement `right`, 
   and immediately skip any duplicate `left` and `right` elements.

COMPLEXITY:
-----------
Time:  O(N log N + N^3) = O(N^3) — Sorting takes O(N log N). We have two nested loops O(N^2) and inside, the two pointers take O(N). Total is O(N^3).
Space: O(1) or O(N) — Depending on the sorting algorithm. Output space is ignored.

EDGE CASES:
-----------
- Edge case 1: Array has fewer than 4 elements. Returns empty list.
- Edge case 2: Array contains duplicates, effectively handled by our `skip` conditions.
============================================================
"""

def search_quadruplets(arr: list[int], target: int) -> list[list[int]]:
    """
    Finds all unique quadruplets in the array that add up to the target.
    """
    arr.sort()
    quadruplets: list[list[int]] = []
    n: int = len(arr)

    for i in range(n - 3):
        # Skip duplicate elements for the first part
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            # Skip duplicate elements for the second part
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            
            sub_target: int = target - arr[i] - arr[j]
            left: int = j + 1
            right: int = n - 1

            while left < right:
                current_sum = arr[left] + arr[right]

                if current_sum == sub_target:
                    quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate elements for the third part
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    # Skip duplicate elements for the fourth part
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                
                elif current_sum < sub_target:
                    left += 1
                else:
                    right -= 1

    return quadruplets

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert search_quadruplets([4, 1, 2, -1, 1, -3], 1) == [[-3, -1, 1, 4], [-3, 1, 1, 2]], "Test 1 failed"
    assert search_quadruplets([2, 0, -1, 1, -2, 2], 2) == [[-2, 0, 2, 2], [-1, 0, 1, 2]], "Test 2 failed"
    
    # 🔲 Edge cases
    assert search_quadruplets([0, 0, 0, 0], 0) == [[0, 0, 0, 0]], "Edge 1: All zeros"
    assert search_quadruplets([1, 2, 3], 6) == [], "Edge 2: Not enough elements"
    assert search_quadruplets([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]], "Edge 3: Duplicates handling"

    print("All tests passed!")
