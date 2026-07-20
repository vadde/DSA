"""
============================================================
Problem: First Non-repeating Character
Pattern: Hash Maps
Difficulty: Easy
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a word like "apple".
You want to find the first letter that appears exactly ONE time in the whole word.
If you look at 'a', it appears 1 time. It's the first letter! So the answer is 'a'.
What about "aabbc"?
'a' appears 2 times. 'b' appears 2 times. 'c' appears 1 time. So the answer is 'c'.
To solve this quickly, we just read the word twice:
First time: We write down in our magical notebook how many times we see every letter.
Second time: We look at the letters in order, check the notebook, and as soon as 
we find a letter with a count of exactly 1, we stop and return its index!

APPROACH:
---------
1. Initialize an empty dictionary `freq_map = {}` to store character counts.
2. First Pass: Loop through the string.
   - For every character, add 1 to its count in `freq_map`.
   - `freq_map[char] = freq_map.get(char, 0) + 1`
3. Second Pass: Loop through the string again using `enumerate` to get the index.
   - If `freq_map[char] == 1`, return the index `i`.
4. If the loop finishes and we didn't return anything, it means every character 
   was repeated! Return `-1`.

COMPLEXITY:
-----------
Time:  O(N) — We loop through the string twice. 2N is still O(N).
Space: O(1) — The Hash Map will at most store 26 characters (if only lowercase English letters).

EDGE CASES:
-----------
- Edge case 1: String where all characters repeat (e.g., "aabb"). Returns `-1`.
- Edge case 2: Empty string. Returns `-1`.
============================================================
"""

def first_uniq_char(s: str) -> int:
    """
    Finds the index of the first non-repeating character in a string.
    Returns -1 if it doesn't exist.
    """
    freq_map: dict[str, int] = {}

    # 1. First Pass: Build the frequency map
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1

    # 2. Second Pass: Find the first character with a frequency of 1
    for i, char in enumerate(s):
        if freq_map[char] == 1:
            return i

    # No unique character found
    return -1

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert first_uniq_char("leetcode") == 0, "Test 1 failed"       # 'l' is at 0
    assert first_uniq_char("loveleetcode") == 2, "Test 2 failed"   # 'v' is at 2
    assert first_uniq_char("aabbc") == 4, "Test 3 failed"          # 'c' is at 4
    
    # 🔲 Edge cases
    assert first_uniq_char("aabb") == -1, "Edge 1: All repeat"
    assert first_uniq_char("") == -1, "Edge 2: Empty string"
    assert first_uniq_char("z") == 0, "Edge 3: Single character"

    print("All tests passed!")
