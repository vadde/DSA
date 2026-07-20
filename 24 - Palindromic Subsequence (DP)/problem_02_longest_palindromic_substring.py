"""
============================================================
Problem: Longest Palindromic Substring
Pattern: Palindromic Subsequence (DP)
Difficulty: Medium
LeetCode: #5
============================================================
Expand Around Center approach: O(N^2) time, O(1) space.
For each position, expand for odd-length and even-length palindromes.
============================================================
"""


def longest_palindromic_substring(s: str) -> str:
    def expand(lo: int, hi: int) -> tuple[int, int]:
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return lo + 1, hi - 1  # last valid positions

    best_l, best_r = 0, 0
    for i in range(len(s)):
        # Odd-length
        l, r = expand(i, i)
        if r - l > best_r - best_l:
            best_l, best_r = l, r
        # Even-length
        l, r = expand(i, i + 1)
        if r - l > best_r - best_l:
            best_l, best_r = l, r
    return s[best_l: best_r + 1]


if __name__ == "__main__":
    assert longest_palindromic_substring("babad") in ("bab", "aba"), "Test 1"
    assert longest_palindromic_substring("cbbd") == "bb",            "Test 2"
    assert longest_palindromic_substring("a") == "a",                "Edge: single"
    assert longest_palindromic_substring("racecar") == "racecar",    "Test 3"
    print("All tests passed!")
