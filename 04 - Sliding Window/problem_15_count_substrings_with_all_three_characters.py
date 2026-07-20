"""
============================================================
Problem: Count Substrings with All Three Chars
Pattern: Sliding Window (Advanced: Counting Combinations)
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you need to buy an Apple, a Banana, and a Carrot. You are walking down a row
of fruit stands. As soon as you have bought at least one of each, you are happy.
But here's the trick: if you are happy right now, you would STILL be happy if you kept 
walking and bought even MORE fruits from the stands further down the road!
So, instead of just saying "Yes, I found a happy stretch", we can instantly count ALL 
the longer stretches down the road that start from the same place. We add them to our 
total score, and then we step away from our first stand to see if we can still be happy.

APPROACH (Mathematical Counting):
---------------------------------
1. INITIALIZE variables: `window_start = 0`, `total_substrings = 0`, and a simple
   dictionary to count 'a', 'b', and 'c'.
2. EXPAND the window: iterate `window_end` from 0 to len(s)-1. 
3. Increment the count of `s[window_end]`.
4. SHRINK LOOP: While our window contains at least one 'a', one 'b', and one 'c':
   a. RECORD (The Math Trick): If the current window `s[window_start : window_end]` 
      is valid, then any string that extends further to the right is ALSO valid. 
      How many such extensions exist? Exactly `len(s) - window_end`.
      Add this directly to `total_substrings`.
   b. Shrink the window from the left by decrementing the count of `s[window_start]`.
   c. Increment `window_start`.
5. RETURN `total_substrings`.

COMPLEXITY:
-----------
Time:  O(N) — Both `window_start` and `window_end` traverse the string at most once.
Space: O(1) — The dictionary always has exactly 3 keys ('a', 'b', 'c').

EDGE CASES:
-----------
- Edge case 1: String is shorter than 3 characters. Impossible, returns 0.
- Edge case 2: String is missing one of the characters entirely (e.g., "ababab"). Returns 0.
============================================================
"""

def number_of_substrings(s: str) -> int:
    """
    Return the number of substrings containing at least one 'a', one 'b', and one 'c'.
    """
    window_start: int = 0
    total_substrings: int = 0
    
    # We only care about 'a', 'b', and 'c'
    counts = {'a': 0, 'b': 0, 'c': 0}
    n: int = len(s)

    for window_end in range(n):
        # EXPAND
        char = s[window_end]
        if char in counts:
            counts[char] += 1

        # SHRINK LOOP: We have a valid window
        while counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0:
            # RECORD: All substrings starting at `window_start` and ending at 
            # `window_end` OR ANY INDEX AFTER `window_end` are valid!
            total_substrings += (n - window_end)

            # Shrink from the left to find the next valid window
            left_char = s[window_start]
            if left_char in counts:
                counts[left_char] -= 1
            window_start += 1

    return total_substrings


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert number_of_substrings("abcabc") == 10, "Test 1 failed: 'abcabc' has 10 valid substrings"
    assert number_of_substrings("aaacb") == 3, "Test 2 failed: 'aaacb', 'aacb', 'acb'"
    assert number_of_substrings("abc") == 1, "Test 3 failed: 'abc' is exactly 1"

    # 🔲 Edge cases
    assert number_of_substrings("ab") == 0, "Edge 1: less than 3 chars"
    assert number_of_substrings("abababab") == 0, "Edge 2: missing 'c'"
    assert number_of_substrings("aabcc") == 4, "Edge 3: 'aabc', 'aabcc', 'abc', 'abcc'"

    print("All tests passed!")
