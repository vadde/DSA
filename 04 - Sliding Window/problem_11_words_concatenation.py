"""
============================================================
Problem: Words Concatenation
Pattern: Sliding Window
Difficulty: Hard
Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a few specific Lego blocks of the exact same size, each with a word on it.
You are looking at a very long track built out of identical-sized Lego blocks. You want to
find every place on the track where your specific blocks are laid out right next to each
other in ANY order, with no extra blocks in between. Because the blocks are all the same
size, instead of moving forward one tiny bump at a time, you can move forward block by block!

APPROACH (Fixed Window with Word-Sized Steps):
----------------------------------------------
Since all words have the exact same length, this is just "String Anagrams" where instead
of matching characters, we match words.

1. Create a `word_freq` map from the list of `words`.
2. Let `word_length = len(words[0])` and `total_words = len(words)`.
3. To cover all possible starting positions, we must run a sliding window `word_length` times,
   starting at index 0, then 1, ..., up to `word_length - 1`.
4. For each starting offset `i`:
   a. INITIALIZE: `window_start = i`, `matched = 0`, and `words_seen = Counter()`.
   b. EXPAND: move `window_end` in steps of `word_length`.
      - Extract the `current_word = s[window_end : window_end + word_length]`.
      - If `current_word` is in `word_freq`, add it to `words_seen`.
      - If it matches the required frequency exactly, increment `matched`.
      - SHRINK: If we've seen this word TOO MANY times (`words_seen[current_word] > word_freq[current_word]`),
        we must shrink from the left by `word_length` steps until the count is valid again.
      - RECORD: If `matched == len(word_freq)` (all distinct words matched perfectly),
        append `window_start` to our results.
   c. If `current_word` is NOT in `word_freq`, this completely breaks our consecutive chain.
      Reset `window_start` to the next word, clear `words_seen`, and reset `matched = 0`.
5. RETURN the list of result indices.

COMPLEXITY:
-----------
Time:  O(N) — We run `word_length` loops, and in each loop, we jump by `word_length`. This means every character in the string is processed essentially twice (once added, once removed). Extracting the substring takes O(word_length), making it overall O(N).
Space: O(M) — We store the frequency of M words in hash maps.

EDGE CASES:
-----------
- Edge case 1: String is shorter than the required total length. Return [].
- Edge case 2: Empty words list or empty string. Return [].
============================================================
"""

from collections import Counter

def find_word_concatenation(s: str, words: list[str]) -> list[int]:
    """
    Find all starting indices of substrings in `s` that are a concatenation of all `words` in any order.
    """
    if not s or not words:
        return []

    word_freq: Counter[str] = Counter(words)
    word_length: int = len(words[0])
    total_words: int = len(words)
    distinct_words: int = len(word_freq)
    
    result_indices: list[int] = []

    # We only need to run the sliding window `word_length` times to cover all alignments
    for i in range(word_length):
        window_start = i
        matched = 0
        words_seen: Counter[str] = Counter()

        # Move by word_length steps
        for window_end in range(i, len(s) - word_length + 1, word_length):
            current_word = s[window_end : window_end + word_length]

            if current_word in word_freq:
                # EXPAND
                words_seen[current_word] += 1
                if words_seen[current_word] == word_freq[current_word]:
                    matched += 1

                # SHRINK if we have too many of the current word
                while words_seen[current_word] > word_freq[current_word]:
                    left_word = s[window_start : window_start + word_length]
                    if words_seen[left_word] == word_freq[left_word]:
                        matched -= 1
                    words_seen[left_word] -= 1
                    window_start += word_length

                # RECORD
                if matched == distinct_words:
                    result_indices.append(window_start)
            else:
                # BREAK: The chain is broken, reset everything
                window_start = window_end + word_length
                words_seen.clear()
                matched = 0

    return result_indices


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert sorted(find_word_concatenation("catfoxcat", ["cat", "fox"])) == [0, 3], "Test 1 failed: 'catfox' at 0, 'foxcat' at 3"
    assert sorted(find_word_concatenation("catcatfoxfox", ["cat", "fox"])) == [3], "Test 2 failed: 'catfox' at 3"
    assert sorted(find_word_concatenation("barfoothefoobarman", ["foo", "bar"])) == [0, 9], "Test 3 failed: 'barfoo' at 0, 'foobar' at 9"
    assert sorted(find_word_concatenation("wordgoodgoodgoodbestword", ["word","good","best","word"])) == [], "Test 4 failed: no valid concatenation"
    assert sorted(find_word_concatenation("barfoofoobarthefoobarman", ["bar","foo","the"])) == [6, 9, 12], "Test 5 failed: 'foobarthe' at 6, 'barthefoo' at 9, 'thefoobar' at 12"

    # 🔲 Edge cases
    assert find_word_concatenation("a", ["a"]) == [0], "Edge 1: single char match"
    assert find_word_concatenation("abc", ["abcd"]) == [], "Edge 2: word longer than string"
    assert find_word_concatenation("", ["a"]) == [], "Edge 3: empty string"
    assert find_word_concatenation("foobar", []) == [], "Edge 4: empty words array"

    print("All tests passed!")
