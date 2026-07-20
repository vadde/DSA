"""
============================================================
Problem: Valid Palindrome
Pattern: Warmup
Difficulty: Easy
LeetCode: #125
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A palindrome reads the same forwards and backwards. "racecar" is a palindrome.
But what about "A man, a plan, a canal: Panama"?
Rules: Ignore spaces, punctuation, and uppercase/lowercase differences.
Use two hands — one at each end of the word. Walk them inward.
At each step, the characters under both hands must match (case-insensitive).
If they ever don't match, it's not a palindrome.

APPROACH: Two Pointers
---------
1. left = 0, right = len(s) - 1
2. Move left right while char is NOT alphanumeric.
3. Move right left while char is NOT alphanumeric.
4. Compare s[left].lower() == s[right].lower(). If not → False.
5. Move both inward, repeat until left >= right.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(1) — no extra data structures

EDGE CASES:
-----------
- Empty string → True (vacuously a palindrome)
- Single character → True
- Only punctuation → True (".,") after filtering becomes ""
============================================================
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True,  "Test 1"
    assert is_palindrome("race a car") is False,                       "Test 2"
    assert is_palindrome(" ") is True,                                 "Test 3: whitespace only"
    assert is_palindrome("") is True,                                  "Edge: empty"
    assert is_palindrome("a") is True,                                 "Edge: single char"
    assert is_palindrome("0P") is False,                               "Edge: digit vs letter"
    print("All tests passed!")
