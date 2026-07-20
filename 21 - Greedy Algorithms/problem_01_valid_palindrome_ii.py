"""
============================================================
Problem: Valid Palindrome II
Pattern: Greedy Algorithms
Difficulty: Easy
LeetCode: #680
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a string. Can you delete AT MOST ONE character and make it a palindrome?
Greedy approach: Use two pointers. Walk from both ends inward.
If they match → great, keep walking.
If they DON'T match → we must delete one of them. Try deleting the LEFT char
(check if the rest is a palindrome), OR try deleting the RIGHT char.
If EITHER works → return True. Otherwise → False.

APPROACH:
---------
1. Helper: is_palindrome(s, left, right) — two-pointer palindrome check.
2. Use two pointers on the original string.
3. On first mismatch at (left, right):
   - Try is_palindrome(s, left+1, right)
   - Try is_palindrome(s, left, right-1)
   - Return True if either works.
4. If we reach the center without any mismatch → already a palindrome → True.

COMPLEXITY:
-----------
Time:  O(N) — each helper call is O(N), called at most once.
Space: O(1)

EDGE CASES:
-----------
- Already a palindrome → True (0 deletions needed)
- Length 1 → True
- Need to delete more than 1 char → False
============================================================
"""


def valid_palindrome(s: str) -> bool:
    def is_pal(lo: int, hi: int) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_pal(left + 1, right) or is_pal(left, right - 1)
        left += 1
        right -= 1
    return True


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert valid_palindrome("aba") is True,    "Test 1: already palindrome"
    assert valid_palindrome("abca") is True,   "Test 2: delete 'c'"
    assert valid_palindrome("abc") is False,   "Test 3: needs 2+ deletions"
    assert valid_palindrome("a") is True,      "Edge: single char"
    assert valid_palindrome("") is True,       "Edge: empty"
    assert valid_palindrome("deeee") is True,  "Test 4: delete 'd'"
    print("All tests passed!")
