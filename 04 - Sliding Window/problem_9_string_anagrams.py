"""
============================================================
Problem: String Anagrams
Pattern: Sliding Window
Difficulty: Hard
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Remember the Scrabble tiles from the "Permutation in a String" problem? This time,
instead of stopping when you find the FIRST match, you want to walk down the entire
row of tiles and write down the starting position of EVERY place where your tiles
match. An anagram is just another word for permutation (same letters, different order).

APPROACH (Fixed Window + Hash Map):
-----------------------------------
This is exactly the same algorithm as "Permutation in a String", except we collect all
valid starting indices instead of returning True immediately.

1. INITIALIZE variables: `window_start = 0`, `matched = 0`, `result_indices = []`, 
   and `char_freq` tracking the pattern's characters.
2. EXPAND the window: iterate `window_end` from 0 to len(s)-1. 
3. If `s[window_end]` is in our `char_freq`, decrement its count. If the count hits 0,
   we have completely matched one unique character from the pattern. Increment `matched`.
4. RECORD: If `matched == len(char_freq)`, append `window_start` to `result_indices`.
5. SHRINK: If `window_end >= len(pattern) - 1`, we must shrink the window from the left
   before the next expansion.
   a. Look at the character going out: `s[window_start]`.
   b. If it's part of the pattern, and its frequency is exactly 0, we lose a complete match,
      so decrement `matched`.
   c. Put the character back into the `char_freq` tally.
   d. Increment `window_start`.
6. RETURN `result_indices`.

COMPLEXITY:
-----------
Time:  O(N + M) — Where N is the length of the string and M is the length of the pattern.
Space: O(M) — Or strictly O(26) = O(1) for English letters to store the frequency map. The result array takes O(N) space in the worst case (e.g., string="aaaaa", pattern="a"), but this is typically not counted against auxiliary space.

EDGE CASES:
-----------
- Edge case 1: Pattern is longer than the string. Return empty list [].
- Edge case 2: No anagrams exist. Return empty list [].
============================================================
"""

from collections import Counter

def find_string_anagrams(s: str, pattern: str) -> list[int]:
    """
    Return a list of starting indices of all anagrams of `pattern` in the string `s`.
    """
    result_indices: list[int] = []
    
    if len(pattern) > len(s) or not pattern:
        return result_indices

    window_start: int = 0
    matched: int = 0
    char_freq: Counter[str] = Counter(pattern)
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
            result_indices.append(window_start)

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

    return result_indices


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert find_string_anagrams("ppqp", "pq") == [1, 2], "Test 1 failed: 'pq' at 1, 'qp' at 2"
    assert find_string_anagrams("abbcabc", "abc") == [2, 3, 4], "Test 2 failed: 'bca' at 2, 'cab' at 3, 'abc' at 4"
    assert find_string_anagrams("cbaebabacd", "abc") == [0, 6], "Test 3 failed: 'cba' at 0, 'bac' at 6"

    # 🔲 Edge cases
    assert find_string_anagrams("abab", "ab") == [0, 1, 2], "Edge 1: overlapping anagrams"
    assert find_string_anagrams("aaaa", "a") == [0, 1, 2, 3], "Edge 2: single char pattern matches all"
    assert find_string_anagrams("abc", "abcd") == [], "Edge 3: pattern longer than string"

    print("All tests passed!")
