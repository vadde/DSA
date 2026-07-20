"""
============================================================
Problem: Pangram
Pattern: Warmup
Difficulty: Easy
LeetCode: #1832
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A pangram is a sentence that uses EVERY letter of the alphabet at least once.
"The quick brown fox jumps over the lazy dog" is a famous one.
To check: just collect every unique letter you see, and confirm you have all 26.

APPROACH: Set
---------
Lowercase the sentence, then add each alphabetic character to a set.
If `len(set) == 26` at the end, every letter appeared at least once.

COMPLEXITY:
-----------
Time:  O(N) — one pass through the sentence
Space: O(1) — set holds at most 26 lowercase letters

EDGE CASES:
-----------
- Empty string → False
- String with only punctuation → False
============================================================
"""


def check_if_pangram(sentence: str) -> bool:
    return len(set(sentence.lower()) & set("abcdefghijklmnopqrstuvwxyz")) == 26


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert check_if_pangram("thequickbrownfoxjumpsoverthelazydog") is True,  "Test 1"
    assert check_if_pangram("leetcode") is False,                             "Test 2"
    assert check_if_pangram("") is False,                                     "Edge: empty"
    assert check_if_pangram("abcdefghijklmnopqrstuvwxyz") is True,           "Edge: exact alphabet"
    print("All tests passed!")
