"""
============================================================
Problem: Longest Substring with Same Letters after Replacement
Pattern: Sliding Window
Difficulty: Hard
Link: https://leetcode.com/problems/longest-repeating-character-replacement/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a string of colored beads. You want a long segment where all beads
are the exact same color. You are allowed to magically repaint up to K beads to any
color you want. To get the longest segment, you should find a window where most of the
beads are already the same color, and use your K magic repaints on the odd ones out.
So, the rule is: (Total beads in window) - (Count of most frequent bead) <= K.

APPROACH (Dynamic Window + Hash Map):
-------------------------------------
1. INITIALIZE variables: `window_start = 0`, `max_length = 0`, `max_repeat_letter_count = 0`,
   and `char_freq = Counter()`.
2. EXPAND the window: iterate `window_end` from 0 to len(s)-1. 
3. Update `char_freq` with `s[window_end]` and update `max_repeat_letter_count` if this
   character's frequency is the highest we've seen in the current window.
4. SHRINK LOOP: The number of letters we need to replace is `(window_end - window_start + 1) - max_repeat_letter_count`.
   If this number is `> k`, our window is invalid.
   a. Decrement `char_freq[s[window_start]]`.
   b. Increment `window_start`.
   (Note: We don't strictly need to decrement `max_repeat_letter_count` because we only
   care about finding a LARGER maximum to get a longer valid window).
5. RECORD: `max_length = max(max_length, window_end - window_start + 1)`.
6. RETURN `max_length`.

COMPLEXITY:
-----------
Time:  O(N) — We iterate through the string. `window_start` only moves forward. The math and map updates are O(1).
Space: O(26) = O(1) — We store the frequencies of English letters, bounded by 26.

EDGE CASES:
-----------
- Edge case 1: String length is less than or equal to K. We can replace all of them, so return len(s).
- Edge case 2: Empty string. Return 0.
============================================================
"""

from collections import Counter

def character_replacement(s: str, k: int) -> int:
    """
    Find the length of the longest substring containing the same letter after at most K replacements.
    """
    window_start: int = 0
    max_length: int = 0
    max_repeat_letter_count: int = 0
    char_freq: Counter[str] = Counter()

    for window_end in range(len(s)):
        right_char: str = s[window_end]
        char_freq[right_char] += 1

        # We keep track of the count of the most frequent letter in the CURRENT window.
        # It tells us how many letters we DON'T need to replace.
        max_repeat_letter_count = max(max_repeat_letter_count, char_freq[right_char])

        # Current window size is (window_end - window_start + 1).
        # Letters to replace = Current window size - max_repeat_letter_count.
        # If letters to replace > k, the window is invalid, so shrink it.
        if (window_end - window_start + 1) - max_repeat_letter_count > k:
            left_char: str = s[window_start]
            char_freq[left_char] -= 1
            window_start += 1
            
            # Note: We do NOT need to update max_repeat_letter_count when we shrink.
            # Why? Because we only care about finding a LONGER valid window. A longer
            # valid window requires a strictly larger max_repeat_letter_count. 
            # Keeping the old max is safe and mathematically guarantees O(1) time here.

        # The window is guaranteed to be valid at this point (or same size as the previous valid one)
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert character_replacement("aabccbb", 2) == 5, "Test 1 failed: 'bbbbb' (replace a,c)"
    assert character_replacement("abbcb", 1) == 4, "Test 2 failed: 'bbbb' (replace c)"
    assert character_replacement("abccde", 1) == 3, "Test 3 failed: 'ccc' (replace b or d)"

    # 🔲 Edge cases
    assert character_replacement("", 2) == 0, "Edge 1: empty string"
    assert character_replacement("abcd", 4) == 4, "Edge 2: K >= length"
    assert character_replacement("aaaaa", 0) == 5, "Edge 3: K=0, all same"

    print("All tests passed!")
