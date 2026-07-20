"""
============================================================
Problem: Valid Anagram
Pattern: Warmup
Difficulty: Easy
LeetCode: #242
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Two words are anagrams if they use EXACTLY the same letters, just in a
different order. "listen" and "silent" are anagrams.
Trick: Count each letter in both words. If every letter has the same count
in both → anagram! If any count differs → not an anagram.

APPROACH: Counter
---------
1. If len(s) != len(t) → return False immediately.
2. Use Counter(s) and Counter(t).
3. If they're equal → True, else False.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(K) — K is the size of the alphabet (26 for lowercase English)

EDGE CASES:
-----------
- Different lengths → always False
- Empty strings → True (both are "empty anagrams")
- Same string → True
============================================================
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True,  "Test 1"
    assert is_anagram("rat", "car") is False,         "Test 2"
    assert is_anagram("", "") is True,                "Edge: both empty"
    assert is_anagram("a", "b") is False,             "Edge: single different"
    assert is_anagram("ab", "a") is False,            "Edge: different lengths"
    assert is_anagram("listen", "silent") is True,    "Test 3: classic anagram"
    print("All tests passed!")
