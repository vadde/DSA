"""
============================================================
Problem: No-repeat Substring
Pattern: Sliding Window
Difficulty: Hard
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you are collecting different types of stickers in a row. You want the longest
strip of stickers possible, but you are not allowed to have any duplicates! As you slide
your frame to the right, if you see a sticker you already have in your frame, you must
cut off the left side of your strip until that duplicate sticker is thrown away, so your
current strip only has unique stickers again.

APPROACH (Dynamic Window + Hash Map for Index Tracking):
--------------------------------------------------------
1. INITIALIZE variables: `window_start = 0`, `max_length = 0`, and `char_index = {}`.
2. EXPAND the window: iterate `window_end` from 0 to len(s)-1. 
3. SHRINK (Optimized Jump): Instead of a `while` loop that slowly moves `window_start` right,
   we check if `s[window_end]` is already in `char_index`. If it is, and its previous
   position is inside our current window (`>= window_start`), we jump `window_start`
   directly to `char_index[s[window_end]] + 1`.
4. Update the dictionary: `char_index[s[window_end]] = window_end`.
5. RECORD: The window is now guaranteed to have no repeats. `max_length = max(max_length, window_end - window_start + 1)`.
6. RETURN `max_length`.

COMPLEXITY:
-----------
Time:  O(N) — We iterate through the string exactly once. The dictionary lookups and updates are O(1).
Space: O(K) — The hash map stores at most K distinct characters, where K is the number of distinct characters in the alphabet (e.g., O(26) for English letters, making it O(1) conceptually, but bounded by string length if using arbitrary characters).

EDGE CASES:
-----------
- Edge case 1: Empty string. Return 0.
- Edge case 2: All identical characters (e.g., "aaaa"). Return 1.
============================================================
"""

def no_repeat_substring(s: str) -> int:
    """
    Find the length of the longest substring with no repeating characters.
    """
    window_start: int = 0
    max_length: int = 0
    
    # Store the most recent index of each character
    char_index: dict[str, int] = {}

    for window_end in range(len(s)):
        right_char: str = s[window_end]

        # SHRINK (Optimized): If we've seen this character before AND it's inside our current window
        if right_char in char_index and char_index[right_char] >= window_start:
            # Jump window_start past the previous occurrence of this character
            window_start = char_index[right_char] + 1

        # EXPAND: Record/update the index of the current character
        char_index[right_char] = window_end

        # RECORD: Update the maximum length found so far
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert no_repeat_substring("aabccbb") == 3, "Test 1 failed: 'abc' or 'cab'"
    assert no_repeat_substring("abbbb") == 2, "Test 2 failed: 'ab'"
    assert no_repeat_substring("abccde") == 3, "Test 3 failed: 'cde' or 'abc'"

    # 🔲 Edge cases
    assert no_repeat_substring("") == 0, "Edge 1: empty string"
    assert no_repeat_substring("aaaaa") == 1, "Edge 2: all identical"
    assert no_repeat_substring("abcdef") == 6, "Edge 3: no repeats at all"
    
    # 🔲 Jumping logic test
    assert no_repeat_substring("tmmzuxt") == 5, "Edge 4: 'mzuxt'"

    print("All tests passed!")
