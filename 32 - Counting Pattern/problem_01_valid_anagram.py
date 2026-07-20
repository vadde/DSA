"""
============================================================
Problem: Valid Anagram
Pattern: Counting Pattern
Difficulty: Easy
LeetCode: #242
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Two strings are anagrams if they use the exact same letters in the exact
same amounts. "listen" and "silent" are anagrams.

APPROACH: Array Frequency Count
---------
We can just use a frequency array of size 26 (for lowercase English letters).
Increment for letters in string `s`, decrement for letters in string `t`.
If the array is all zeroes at the end, they are anagrams!

COMPLEXITY:
-----------
Time:  O(N) — One pass over strings.
Space: O(1) — Fixed array size of 26.
============================================================
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
        
    for c in count:
        if c != 0:
            return False
            
    return True


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True, "Test 1"
    assert is_anagram("rat", "car") is False,        "Test 2"
    assert is_anagram("a", "a") is True,             "Test 3"
    print("All tests passed!")
