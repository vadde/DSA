"""
============================================================
Problem: First Unique Character in a String
Pattern: Counting Pattern
Difficulty: Easy
LeetCode: #387
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Find the first character in a string that does not repeat anywhere else
in the string. Return its index.

APPROACH: Hash Map Frequency Count
---------
1. Count the frequency of all characters (first pass).
2. Iterate through the string again, returning the index of the first character
   whose frequency is exactly 1 (second pass).

COMPLEXITY:
-----------
Time:  O(N)
Space: O(1) (Since there are at most 26 English letters).
============================================================
"""

from collections import Counter


def first_uniq_char(s: str) -> int:
    counts = Counter(s)
    
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
            
    return -1


if __name__ == "__main__":
    assert first_uniq_char("leetcode") == 0,         "Test 1: 'l'"
    assert first_uniq_char("loveleetcode") == 2,     "Test 2: 'v'"
    assert first_uniq_char("aabb") == -1,            "Test 3: no unique"
    print("All tests passed!")
