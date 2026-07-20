"""
============================================================
Problem: Fruits into Baskets
Pattern: Sliding Window
Difficulty: Medium
Link: https://leetcode.com/problems/fruit-into-baskets/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you are walking past a row of fruit trees. You have exactly 2 baskets,
and each basket can only hold one type of fruit (like only apples or only oranges).
You want to pick as many fruits as possible by walking continuously down the row.
If you encounter a 3rd type of fruit, you have to stop and rethink your starting
point so you only ever have 2 types of fruit at any time.

APPROACH (Dynamic Window + Hash Map):
-------------------------------------
This is a disguised version of "Longest Substring with K Distinct Characters" where K=2.

1. INITIALIZE variables: `window_start = 0`, `max_fruits = 0`, and `fruit_freq = Counter()`.
2. EXPAND the window: iterate `window_end` from 0 to len(fruits)-1. Add `fruits[window_end]` to the `fruit_freq` tally.
3. SHRINK LOOP: while `len(fruit_freq) > 2` (we have more than 2 types of fruit):
   a. Decrement the frequency of the fruit at `window_start`.
   b. If the frequency drops to 0, completely `del` the fruit type from the map.
   c. Increment `window_start`.
4. RECORD: Once the while loop ends, our window only has at most 2 types of fruit. Update `max_fruits`.
5. RETURN `max_fruits`.

COMPLEXITY:
-----------
Time:  O(N) — We iterate through the array of fruits. Each fruit is added once and removed at most once.
Space: O(1) — The hash map stores at most 3 elements at any time, which is constant space.

EDGE CASES:
-----------
- Edge case 1: The array is empty. Return 0.
- Edge case 2: The array has fewer than 3 fruits. We can pick all of them.
============================================================
"""

from collections import Counter

def fruits_into_baskets(fruits: list[int]) -> int:
    """
    Find the maximum number of fruits you can collect in 2 baskets.
    (Equivalent to finding the longest subarray with at most 2 distinct elements).
    """
    if not fruits:
        return 0

    window_start: int = 0
    max_fruits: int = 0
    fruit_freq: Counter[int] = Counter()

    for window_end in range(len(fruits)):
        # EXPAND: Pick the fruit from the right
        right_fruit: int = fruits[window_end]
        fruit_freq[right_fruit] += 1

        # SHRINK: If we exceed 2 types of fruits
        while len(fruit_freq) > 2:
            left_fruit: int = fruits[window_start]
            fruit_freq[left_fruit] -= 1
            
            # Critical: remove the fruit type completely if frequency is 0
            if fruit_freq[left_fruit] == 0:
                del fruit_freq[left_fruit]
                
            window_start += 1

        # RECORD: Update the maximum fruits collected
        max_fruits = max(max_fruits, window_end - window_start + 1)

    return max_fruits


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert fruits_into_baskets([1, 2, 1]) == 3, "Test 1 failed: can pick all [1, 2, 1]"
    assert fruits_into_baskets([0, 1, 2, 2]) == 3, "Test 2 failed: can pick [1, 2, 2]"
    assert fruits_into_baskets([1, 2, 3, 2, 2]) == 4, "Test 3 failed: can pick [2, 3, 2, 2]"
    assert fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5, "Test 4 failed: can pick [1, 2, 1, 1, 2]"

    # 🔲 Edge cases
    assert fruits_into_baskets([]) == 0, "Edge 1: empty array should return 0"
    assert fruits_into_baskets([1]) == 1, "Edge 2: single fruit should return 1"
    assert fruits_into_baskets([1, 1, 1, 1, 1]) == 5, "Edge 3: all same fruit type"

    print("All tests passed!")
