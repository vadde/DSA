"""
============================================================
Problem: Smallest Window containing Substring
Pattern: Sliding Window
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-window-substring/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a shopping list of ingredients (your pattern) and you are walking
down a long grocery aisle (the string). You want to find the shortest possible section
of the aisle that contains every single ingredient on your list. You keep walking
until you have everything (expanding the window). Then, to make sure you're looking
at the shortest possible section, you try to leave items behind from where you started
(shrinking the window) as long as you still have all the required ingredients.

APPROACH (Dynamic Window + Hash Map):
-------------------------------------
1. INITIALIZE variables: `window_start = 0`, `matched = 0`, `min_length = inf`,
   `substr_start = 0`, and `char_freq` tallying the pattern's characters.
2. EXPAND the window: iterate `window_end` from 0 to len(s)-1. 
3. If `s[window_end]` is in our `char_freq`, decrement its count. 
   If `char_freq[s[window_end]] >= 0` AFTER decrementing, it means this character
   was actually needed (not just an extra copy), so we increment `matched`.
4. SHRINK LOOP: while `matched == len(pattern)` (we have all required characters):
   a. RECORD: If the current window length is smaller than `min_length`, update
      `min_length` and remember `substr_start = window_start`.
   b. Look at the character going out: `s[window_start]`.
   c. Increment `window_start`.
   d. If the outgoing character is in `char_freq`, we must put it back in our tally.
      If `char_freq[left_char] == 0` BEFORE incrementing, it means we are losing
      a character we strictly needed, so we decrement `matched`.
      Then increment `char_freq[left_char]`.
5. RETURN the substring using string slicing, or `""` if no valid window was found.

COMPLEXITY:
-----------
Time:  O(N + M) — We process the string (N) and the pattern (M). Both pointers only move right.
Space: O(M) — We store the frequencies of the pattern characters, bounded by O(26) = O(1).

EDGE CASES:
-----------
- Edge case 1: Pattern is longer than the string. Return `""`.
- Edge case 2: No such window exists. Return `""`.
============================================================
"""

from collections import Counter
import math

def find_substring(s: str, pattern: str) -> str:
    """
    Find the smallest substring in `s` containing all characters of `pattern`.
    """
    if len(pattern) > len(s) or not pattern:
        return ""

    window_start: int = 0
    matched: int = 0
    char_freq: Counter[str] = Counter(pattern)
    
    min_length: int | float = math.inf
    substr_start: int = 0

    for window_end in range(len(s)):
        right_char: str = s[window_end]

        # EXPAND: If the character is part of the pattern, we process it
        if right_char in char_freq:
            char_freq[right_char] -= 1
            # If it's >= 0, it means we needed this character to fulfill the pattern
            if char_freq[right_char] >= 0:
                matched += 1

        # SHRINK LOOP: We have all characters, try to minimize the window
        while matched == len(pattern):
            # RECORD: Found a smaller window?
            current_length = window_end - window_start + 1
            if current_length < min_length:
                min_length = current_length
                substr_start = window_start

            # Shrink from the left
            left_char: str = s[window_start]
            window_start += 1

            if left_char in char_freq:
                # If its frequency is exactly 0, losing it means we no longer
                # have all the required characters for the pattern
                if char_freq[left_char] == 0:
                    matched -= 1
                
                # Put it back in the requirement tally
                char_freq[left_char] += 1

    if min_length == math.inf:
        return ""
    
    # Python slicing requires integer indices, so we use int() just in case,
    # though it's guaranteed to be an int if min_length changed.
    return s[substr_start:substr_start + int(min_length)]


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert find_substring("aabdec", "abc") == "abdec", "Test 1 failed: 'abdec' contains a, b, c"
    assert find_substring("aabdec", "abac") == "aabdec", "Test 2 failed: need two a's"
    assert find_substring("abdbca", "abc") == "bca", "Test 3 failed: 'bca' is length 3"
    assert find_substring("adcad", "abc") == "", "Test 4 failed: no 'b' exists"

    # 🔲 Edge cases
    assert find_substring("a", "aa") == "", "Edge 1: pattern longer than string"
    assert find_substring("a", "a") == "a", "Edge 2: exact match"
    assert find_substring("ADOBECODEBANC", "ABC") == "BANC", "Edge 3: classic LC 76 test case"

    print("All tests passed!")
