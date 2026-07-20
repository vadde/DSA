"""
============================================================
Problem: Longest Substring with K Distinct Characters
Pattern: Sliding Window
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you are making a necklace out of beads with letters on them. You want the
longest piece of the necklace you can make, but you're only allowed to use up to K
different types of beads. You keep adding beads from right to left. If you accidentally
add a (K+1)th type of bead, you must take off beads from the left side until you're
back down to K types.

APPROACH (Dynamic Window + Hash Map):
-------------------------------------
1. INITIALIZE variables: `window_start = 0`, `max_length = 0`, and `char_freq = Counter()`.
2. EXPAND the window: iterate `window_end` from 0 to len(s)-1. Add `s[window_end]` to the `char_freq` tally.
3. SHRINK LOOP: while `len(char_freq) > K` (we have too many distinct characters):
   a. Decrement the frequency of `s[window_start]`.
   b. If the frequency drops to 0, completely `del` the character from the map to keep `len()` accurate.
   c. Increment `window_start`.
4. RECORD: Once the while loop ends, the window is valid. Update `max_length = max(max_length, window_end - window_start + 1)`.
5. RETURN `max_length`.

COMPLEXITY:
-----------
Time:  O(N) — We iterate through the string once with `window_end`. `window_start` also traverses the string at most once. Hash map operations are O(1).
Space: O(K) — The hash map stores at most K + 1 characters at any time, so the space complexity is proportional to K.

EDGE CASES:
-----------
- Edge case 1: The string is empty, or K is 0. Return 0.
- Edge case 2: K is greater than or equal to the total number of distinct characters in the string. The entire string is the answer.
============================================================
"""

from collections import Counter

def longest_substring_with_k_distinct(s: str, k: int) -> int:
    """
    Find the length of the longest substring in `s` with no more than `k` distinct characters.
    """
    if k == 0 or not s:
        return 0

    window_start: int = 0
    max_length: int = 0
    char_freq: Counter[str] = Counter()

    for window_end in range(len(s)):
        # EXPAND: Add the new character to the frequency map
        right_char: str = s[window_end]
        char_freq[right_char] += 1

        # SHRINK: If we exceed the allowed number of distinct characters
        while len(char_freq) > k:
            left_char: str = s[window_start]
            char_freq[left_char] -= 1
            
            # Critical: remove the character completely if frequency is 0
            if char_freq[left_char] == 0:
                del char_freq[left_char]
                
            window_start += 1

        # RECORD: Update the max_length now that the window is valid
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert longest_substring_with_k_distinct("araaci", 2) == 4, "Test 1 failed: 'araa' is length 4"
    assert longest_substring_with_k_distinct("araaci", 1) == 2, "Test 2 failed: 'aa' is length 2"
    assert longest_substring_with_k_distinct("cbbebi", 3) == 5, "Test 3 failed: 'cbbeb' or 'bbebi' is length 5"

    # 🔲 Edge cases
    assert longest_substring_with_k_distinct("", 2) == 0, "Edge 1: empty string"
    assert longest_substring_with_k_distinct("abc", 0) == 0, "Edge 2: k=0 should return 0"
    assert longest_substring_with_k_distinct("aabacbebebe", 10) == 11, "Edge 3: K is larger than unique characters"

    print("All tests passed!")
