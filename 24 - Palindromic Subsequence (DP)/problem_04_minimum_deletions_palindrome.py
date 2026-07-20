"""
============================================================
Problem: Minimum Deletions to Make a String Palindrome
Pattern: Palindromic Subsequence (DP)
Difficulty: Medium
LeetCode: #1312 (min insertions) / classic deletion variant
============================================================
Key insight: minimum deletions = N - LPS(s).
Because the characters NOT in the LPS must be deleted to make the string a palindrome.
============================================================
"""


def min_deletions_palindrome(s: str) -> int:
    n = len(s)
    # LPS = Longest Palindromic Subsequence
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (dp[i + 1][j - 1] if length > 2 else 0) + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return n - dp[0][n - 1]


if __name__ == "__main__":
    assert min_deletions_palindrome("abdbca") == 1,  "Test 1: delete 'c'"
    assert min_deletions_palindrome("cddpd") == 2,   "Test 2"
    assert min_deletions_palindrome("pqr") == 2,     "Test 3: all diff"
    assert min_deletions_palindrome("a") == 0,       "Edge: single"
    assert min_deletions_palindrome("aa") == 0,      "Edge: already palindrome"
    print("All tests passed!")
