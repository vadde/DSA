"""
============================================================
Problem: Longest Palindromic Subsequence (LPS)
Pattern: Palindromic Subsequence (DP)
Difficulty: Medium
LeetCode: #516
============================================================
dp[i][j] = LPS length in s[i..j].
Base: dp[i][i] = 1 (single char).
Recurrence:
  s[i]==s[j]: dp[i][j] = dp[i+1][j-1] + 2
  else:       dp[i][j] = max(dp[i+1][j], dp[i][j-1])
Fill by increasing substring length.
============================================================
"""


def longest_palindromic_subsequence(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    # Fill by length of substring
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (dp[i + 1][j - 1] if length > 2 else 0) + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


if __name__ == "__main__":
    assert longest_palindromic_subsequence("bbbab") == 4, "Test 1"
    assert longest_palindromic_subsequence("cbbd") == 2,  "Test 2"
    assert longest_palindromic_subsequence("a") == 1,     "Edge: single"
    assert longest_palindromic_subsequence("aa") == 2,    "Edge: two same"
    assert longest_palindromic_subsequence("ab") == 1,    "Edge: two diff"
    print("All tests passed!")
