"""
============================================================
Problem: Subarrays with K Different Integers
Pattern: Sliding Window (Advanced: Exact K = AtMost K - AtMost K-1)
Difficulty: Hard
Link: https://leetcode.com/problems/subarrays-with-k-different-integers/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you want to cut a piece of a ribbon that has different colored stripes, but you 
want a piece that has *exactly* 3 different colors. Finding "exactly 3" is mathematically 
hard to do in one smooth motion, because when you have 3 colors, you don't know whether 
to stop, keep going, or shrink. 
Instead, we use a clever math trick: 
(Total pieces with AT MOST 3 colors) - (Total pieces with AT MOST 2 colors) 
= (Total pieces with EXACTLY 3 colors).
We just run a simple "at most" sliding window twice!

APPROACH (The "At Most K" Trick):
---------------------------------
1. Define a helper function `at_most_k(nums, k)` that counts the number of valid subarrays
   with `k` or fewer distinct elements.
2. Inside `at_most_k`:
   a. INITIALIZE: `window_start = 0`, `total_subarrays = 0`, `freq_map = {}`.
   b. EXPAND: iterate `window_end`. Add `nums[window_end]` to `freq_map`.
   c. SHRINK LOOP: while the number of distinct elements (`len(freq_map)`) > `k`,
      remove `nums[window_start]` from the map and increment `window_start`.
   d. RECORD (The Counting Trick): If a window from `start` to `end` is valid, then
      all subarrays ending at `end` and starting anywhere between `start` and `end` 
      are ALSO valid. There are exactly `window_end - window_start + 1` such subarrays.
      Add this number to `total_subarrays`.
3. In the main function, return `at_most_k(nums, k) - at_most_k(nums, k - 1)`.

COMPLEXITY:
-----------
Time:  O(N) — The helper function processes the array in O(N). We call it twice, so O(2N) = O(N).
Space: O(N) — The frequency map stores at most N distinct integers in the worst case.

EDGE CASES:
-----------
- Edge case 1: K is larger than the total number of distinct elements. Handled gracefully.
- Edge case 2: Empty array. Return 0.
============================================================
"""

from collections import Counter

def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    """
    Return the number of subarrays with exactly K distinct integers.
    """
    def at_most_k(nums: list[int], limit: int) -> int:
        if limit == 0:
            return 0
            
        window_start: int = 0
        total_subarrays: int = 0
        freq_map: Counter[int] = Counter()

        for window_end in range(len(nums)):
            # EXPAND
            freq_map[nums[window_end]] += 1

            # SHRINK
            while len(freq_map) > limit:
                left_num = nums[window_start]
                freq_map[left_num] -= 1
                if freq_map[left_num] == 0:
                    del freq_map[left_num]
                window_start += 1
            
            # RECORD: Count all valid subarrays ending at window_end
            # If the window is [A, B, C], the valid subarrays ending at C are:
            # [C], [B, C], [A, B, C]. The count is exactly the window length.
            total_subarrays += (window_end - window_start + 1)

        return total_subarrays

    # Exact(K) = AtMost(K) - AtMost(K-1)
    return at_most_k(nums, k) - at_most_k(nums, k - 1)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert subarrays_with_k_distinct([1,2,1,2,3], 2) == 7, "Test 1 failed"
    assert subarrays_with_k_distinct([1,2,1,3,4], 3) == 3, "Test 2 failed"
    
    # 🔲 Edge cases
    assert subarrays_with_k_distinct([1,1,1,1], 1) == 10, "Edge 1: all same elements"
    assert subarrays_with_k_distinct([1,2,3], 4) == 0, "Edge 2: K greater than distinct"
    assert subarrays_with_k_distinct([], 2) == 0, "Edge 3: empty array"

    print("All tests passed!")
