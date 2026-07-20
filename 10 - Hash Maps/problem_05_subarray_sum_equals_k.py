"""
============================================================
Problem: Subarray Sum Equals K
Pattern: Hash Maps (Prefix Sums)
Difficulty: Medium
Link: https://leetcode.com/problems/subarray-sum-equals-k/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a line of numbers, some positive and some negative: [1, -1, 1, 1, 1, 1].
You want to find how many contiguous blocks (subarrays) add up exactly to K (e.g. K=3).
Normally, we could use the "Sliding Window" pattern for subarrays. 
BUT WAIT! Sliding Window ONLY works if all numbers are positive (because adding 
makes the sum bigger, and shrinking makes the sum smaller). 
Here, we have negative numbers! Adding a '-1' actually makes the sum smaller, 
so the Sliding Window breaks.
Instead, we keep a "Running Total" (Prefix Sum) from the very beginning.
If our Running Total right now is 10, and we are looking for K = 3...
We just need to look in our magical notebook to see: "Did my Running Total ever 
equal 7 in the past?"
If it was 7 in the past, and it's 10 now, that means the numbers in between 
must add up exactly to 3!
We use a Hash Map to keep track of how many times we've seen every Running Total.

APPROACH:
---------
1. Initialize `count = 0` (our answer).
2. Initialize `current_sum = 0`.
3. Initialize a dictionary `prefix_sums = {0: 1}`. 
   - WHY `{0: 1}`? Because before we look at any numbers, our running total is 0. 
     If we find a number that exactly equals K on its own, `current_sum - K` will 
     be 0. If 0 isn't in the map, we'd miss it!
4. Loop through every `num` in the array:
   - Add `num` to `current_sum`.
   - Calculate `needed = current_sum - k`.
   - If `needed` is in our `prefix_sums` map, add that frequency to `count`.
   - Finally, add the new `current_sum` to our `prefix_sums` map (or increment its count).
5. Return `count`.

COMPLEXITY:
-----------
Time:  O(N) — One pass through the array. Map lookups are O(1).
Space: O(N) — The Hash Map can store up to N distinct prefix sums.

EDGE CASES:
-----------
- Edge case 1: Array with negatives and zeros (e.g., `[1, -1, 0]`, k=0). 
  The Hash Map handles multiple occurrences perfectly!
- Edge case 2: Empty array. Returns 0.
============================================================
"""

def subarray_sum(nums: list[int], k: int) -> int:
    """
    Finds the total number of continuous subarrays whose sum equals to k.
    """
    count = 0
    current_sum = 0
    
    # Base case: A prefix sum of 0 has been seen exactly 1 time (before we start)
    prefix_sums: dict[int, int] = {0: 1}

    for num in nums:
        # 1. Update our running total
        current_sum += num
        
        # 2. Check if we can chop off a previous prefix to leave exactly 'k'
        needed = current_sum - k
        if needed in prefix_sums:
            count += prefix_sums[needed]
            
        # 3. Add the current running total to our magical notebook
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

    return count

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert subarray_sum([1, 1, 1], 2) == 2, "Test 1 failed"  # [1, 1] at start, and [1, 1] at end
    assert subarray_sum([1, 2, 3], 3) == 2, "Test 2 failed"  # [1, 2] and [3]
    
    # 🔲 Edge cases
    # Array with negative numbers and zeros
    assert subarray_sum([1, -1, 0], 0) == 3, "Edge 1 failed" 
    # The 3 subarrays are: [1, -1], [-1, 0] wait, no. 
    # [1, -1] = 0
    # [1, -1, 0] = 0
    # [0] = 0. Yes, 3 subarrays!
    
    assert subarray_sum([], 0) == 0, "Edge 2 failed"

    print("All tests passed!")
