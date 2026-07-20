"""
============================================================
Problem: Palindromic Partitioning (Minimum Cuts)
Pattern: Palindromic Subsequence (DP)
Difficulty: Hard
LeetCode: #132
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Cut a string into pieces so each piece is a palindrome.
Find the MINIMUM number of cuts to do this.
E.g. "aab" → "aa"|"b" → 1 cut.
     "abcbc" → "a"|"b"|"cbc" → 2 cuts.

APPROACH: DP
---------
1. Precompute is_pal[i][j]: True if s[i..j] is a palindrome.
   Use bottom-up: for each center pair, mark palindromes.
2. cuts[i] = minimum cuts for s[0..i-1].
   - If s[0..i-1] is a palindrome, cuts[i] = 0.
   - Otherwise: min over all j where s[j..i-1] is palindrome of cuts[j] + 1.

COMPLEXITY:
-----------
Time:  O(N²) — palindrome precomputation + DP
Space: O(N²) — palindrome table

EDGE CASES:
-----------
- Single character → 0 cuts (already a palindrome)
- Already a palindrome → 0 cuts
============================================================
"""


def min_cut(s: str) -> int:
    n = len(s)

    # Step 1: precompute palindrome table
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                is_pal[i][j] = True

    # Step 2: cuts[i] = min cuts for s[0..i-1]
    cuts = list(range(-1, n))   # cuts[0]=-1, cuts[1..n] initialized to i-1 (max possible)
    for i in range(1, n + 1):
        if is_pal[0][i - 1]:
            cuts[i] = 0
        else:
            cuts[i] = min(
                cuts[j] + 1
                for j in range(1, i)
                if is_pal[j][i - 1]
            )
    return cuts[n]


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert min_cut("aab") == 1,    "Test 1: aa|b"
    assert min_cut("a") == 0,      "Edge: single char"
    assert min_cut("ab") == 1,     "Test 2: a|b"
    assert min_cut("aba") == 0,    "Test 3: already palindrome"
    assert min_cut("abcbc") == 2,  "Test 4: a|b|cbc"
    assert min_cut("abba") == 0,   "Test 5: abba is palindrome"
    print("All tests passed!")
