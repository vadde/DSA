"""
============================================================
Problem: Longest Palindrome
Pattern: Counting Pattern
Difficulty: Easy
LeetCode: #409
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given a string of letters, what is the LONGEST palindrome you could build
using those letters? (You can rearrange them).
E.g. "abccccdd" -> "dccaccd" (length 7).

APPROACH: Hash Map Frequency Count
---------
Count all character frequencies.
A palindrome can have ANY character with an EVEN count.
It can have EXACTLY ONE character with an ODD count (placed in the middle).
So, sum all even counts. For odd counts, add (count - 1) to make them even.
If there was at least one odd count, add 1 to the final length for the middle character.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(1)
============================================================
"""

from collections import Counter


def longest_palindrome(s: str) -> int:
    counts = Counter(s)
    length = 0
    has_odd = False
    
    for count in counts.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            has_odd = True
            
    if has_odd:
        length += 1
        
    return length


if __name__ == "__main__":
    assert longest_palindrome("abccccdd") == 7, "Test 1"
    assert longest_palindrome("a") == 1,        "Test 2"
    assert longest_palindrome("bb") == 2,       "Test 3"
    print("All tests passed!")
