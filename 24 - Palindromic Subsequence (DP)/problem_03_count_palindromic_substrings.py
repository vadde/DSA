"""
============================================================
Problem: Count of Palindromic Substrings
Pattern: Palindromic Subsequence (DP)
Difficulty: Medium
LeetCode: #647
============================================================
Expand Around Center — count every valid palindrome found.
============================================================
"""


def count_substrings(s: str) -> int:
    count = 0

    def expand(lo: int, hi: int) -> None:
        nonlocal count
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            count += 1
            lo -= 1
            hi += 1

    for i in range(len(s)):
        expand(i, i)      # odd-length
        expand(i, i + 1)  # even-length

    return count


if __name__ == "__main__":
    assert count_substrings("abc") == 3,   "Test 1: a,b,c"
    assert count_substrings("aaa") == 6,   "Test 2: a,a,a,aa,aa,aaa"
    assert count_substrings("a") == 1,     "Edge: single"
    assert count_substrings("aba") == 4,   "Test 3: a,b,a,aba"
    print("All tests passed!")
