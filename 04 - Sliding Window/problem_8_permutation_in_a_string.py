"""
============================================================
Problem: Permutation in a String
Pattern: Sliding Window
Difficulty: Hard
Link: https://leetcode.com/problems/permutation-in-string/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a specific set of Scrabble tiles, say 'A', 'B', and 'C'. You are looking
at a long row of other Scrabble tiles. You want to see if you can find your exact set of
tiles all clumped together in the long row. The order of the tiles doesn't matter, as long
as you have all of them right next to each other. So 'ABC', 'CBA', and 'BCA' are all a match.
We use a fixed-size frame exactly as wide as our set of tiles and slide it along to check.

APPROACH (Fixed Window + Hash Map):
-----------------------------------
1. INITIALIZE variables: `window_start = 0`, `matched = 0`, and `char_freq` tracking the pattern's characters.
2. EXPAND the window: iterate `window_end` from 0 to len(s)-1. 
3. If `s[window_end]` is in our `char_freq`, decrement its count. If the count hits 0, we have
   completely matched one unique character from the pattern. Increment `matched`.
4. RECORD: If `matched == len(char_freq)`, we found a valid permutation. Return `True`.
5. SHRINK: The window size must be exactly `len(pattern)`. So, if `window_end >= len(pattern) - 1`,
   we must shrink the window from the left before the next expansion.
   a. Look at the character going out: `s[window_start]`.
   b. If it's part of the pattern, and its frequency is exactly 0, we are losing a complete match,
      so decrement `matched`.
   c. Put the character back into the `char_freq` tally (increment its frequency).
   d. Increment `window_start`.
6. RETURN `False` if the loop finishes without returning `True`.

COMPLEXITY:
-----------
Time:  O(N + M) — Where N is the length of the string and M is the length of the pattern. We build the frequency map in O(M) and traverse the string in O(N).
Space: O(M) — Or strictly O(26) = O(1) for English letters. We store the frequency of the pattern's characters.

EDGE CASES:
-----------
- Edge case 1: Pattern is longer than the string. Impossible to match, return False.
- Edge case 2: Pattern is empty. Technically True, but typically constraints say pattern length >= 1.
============================================================
"""

from collections import Counter

def check_inclusion(pattern: str, s: str) -> bool:
    """
    Return True if the string `s` contains a permutation of `pattern`, otherwise False.
    """
    if len(pattern) > len(s):
        return False

    window_start: int = 0
    matched: int = 0
    char_freq: Counter[str] = Counter(pattern)
    
    # We need to match this many DISTINCT characters
    distinct_chars: int = len(char_freq)

    for window_end in range(len(s)):
        right_char: str = s[window_end]

        # EXPAND: If the character is part of the pattern, decrement its required count
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1

        # RECORD: Have we matched all distinct characters perfectly?
        if matched == distinct_chars:
            return True

        # SHRINK: Our window size is strictly fixed to len(pattern)
        if window_end >= len(pattern) - 1:
            left_char: str = s[window_start]
            window_start += 1

            if left_char in char_freq:
                # If it was fully matched, losing this character breaks the match
                if char_freq[left_char] == 0:
                    matched -= 1
                # Put it back into our "needed" tally
                char_freq[left_char] += 1

    return False


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert check_inclusion("abc", "oidbcaf") == True, "Test 1 failed: 'bca' is a permutation"
    assert check_inclusion("dc", "odicf") == False, "Test 2 failed: no permutation exists"
    assert check_inclusion("bcdyabcdx", "bcdxabcdy") == True, "Test 3 failed: exact match"
    assert check_inclusion("abc", "aaacb") == True, "Test 4 failed: 'acb' is a permutation"

    # 🔲 Edge cases
    assert check_inclusion("hello", "ooolleoooleh") == False, "Edge 1: 'ooolle' has 3 o's instead of 1, 'oooleh' has 'leh' but only 1 'l'. Actually 'ooolle' - no, 'ooleh' - no. Wait, 'ooleh' is 5 chars. e:1, h:1, l:1, o:2. Pattern 'hello' has e:1, h:1, l:2, o:1. So it should be False."
    assert check_inclusion("ab", "a") == False, "Edge 2: pattern longer than string"
    assert check_inclusion("a", "ab") == True, "Edge 3: single character pattern"

    print("All tests passed!")
