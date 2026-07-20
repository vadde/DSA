"""
============================================================
Problem: Longest Consecutive Sequence
Pattern: Hash Maps (Sets)
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bucket of completely random numbers: [100, 4, 200, 1, 3, 2].
You want to find the longest sequence of numbers that count up by 1.
In this bucket, the longest sequence is `1, 2, 3, 4` (length 4).
How do we do this without sorting the bucket? (Sorting takes too long, O(N log N)).
First, we pour the bucket into a magical Hash Set. A Set is just a Hash Map that 
only stores Keys (no Values). It lets us ask "Do you have this number?" in O(1) time.
Then, we pick up a number, like `4`. We ask: "Is `3` in the Set?"
If `3` IS in the set, that means `4` is NOT the beginning of a sequence! It's just 
the middle or end. So we ignore `4` for now.
But if we pick up `1` and ask "Is `0` in the set?" The answer is NO!
That means `1` is the glorious START of a new sequence!
Since we found a starting line, we just start counting up: "Do you have 2? 3? 4? 5?" 
until the set says NO.
We keep track of the longest streak we find.

APPROACH:
---------
1. Convert the input array into a `nums_set` (a Hash Set).
2. Initialize `longest_streak = 0`.
3. Loop through every `num` in the `nums_set`:
   - Check if `num` is the START of a sequence. It is the start ONLY if `num - 1` 
     is NOT in the set.
   - If it is the start:
     - Initialize `current_num = num` and `current_streak = 1`.
     - While `current_num + 1` IS in the set:
       - `current_num += 1`
       - `current_streak += 1`
     - Update `longest_streak = max(longest_streak, current_streak)`.
4. Return `longest_streak`.

COMPLEXITY:
-----------
Time:  O(N) — We only start counting if we are at the beginning of a sequence. The inner `while` loop only runs for the exact length of that sequence. Every number is visited at most twice.
Space: O(N) — The Hash Set stores all N numbers.

EDGE CASES:
-----------
- Edge case 1: Empty array. Returns 0.
- Edge case 2: Array with duplicate numbers `[1, 2, 0, 1]`. The Set automatically removes duplicates! So it perfectly processes `0, 1, 2` (length 3).
============================================================
"""

def longest_consecutive(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence in O(N) time.
    """
    if not nums:
        return 0

    # 1. Pour everything into a Hash Set for O(1) lookups and to remove duplicates
    nums_set = set(nums)
    longest_streak = 0

    # 2. Iterate through the set
    for num in nums_set:
        # 3. Only start counting if this number is the START of a sequence
        if num - 1 not in nums_set:
            current_num = num
            current_streak = 1
            
            # 4. Count upwards as long as the next number exists in the set
            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1
                
            # 5. Update our record
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4, "Test 1 failed"  # 1, 2, 3, 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9, "Test 2 failed"  # 0 to 8
    
    # 🔲 Edge cases
    assert longest_consecutive([]) == 0, "Edge 1: Empty array"
    assert longest_consecutive([5, 5, 5, 5]) == 1, "Edge 2: All duplicates"
    assert longest_consecutive([1]) == 1, "Edge 3: Single element"

    print("All tests passed!")
