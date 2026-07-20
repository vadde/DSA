"""
============================================================
Problem: Extra Characters in a String
Pattern: Trie
Difficulty: Medium
LeetCode: #2707
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given a string s and a dictionary of words, break s into substrings found in
the dictionary. Any characters left over (not part of any word) count as "extra".
Find the MINIMUM number of extra characters.

APPROACH: Trie + DP
---------
Build a Trie from the dictionary.
dp[i] = min extra chars for s[0..i-1].
dp[0] = 0.
For each position i, default is dp[i-1] + 1 (treat s[i-1] as extra).
Then walk Trie from position i backwards: whenever we hit a word end at j,
update dp[i] = min(dp[i], dp[j]).

COMPLEXITY:
-----------
Time:  O(N^2 + M*L) — DP + Trie build
Space: O(M*L + N) — Trie + DP array
============================================================
"""

from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False


def min_extra_char(s: str, dictionary: List[str]) -> int:
    # Build Trie
    root = TrieNode()
    for word in dictionary:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    n = len(s)
    # dp[i] = min extra chars for s[0..i-1]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(n):
        if dp[i] == float('inf'):
            continue
        # Option 1: treat s[i] as extra character
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        # Option 2: match a word starting at i, walking Trie forward
        node = root
        for j in range(i, n):
            if s[j] not in node.children:
                break
            node = node.children[s[j]]
            if node.is_end:
                dp[j + 1] = min(dp[j + 1], dp[i])
    return int(dp[n])


if __name__ == "__main__":
    assert min_extra_char("leetscode", ["leet", "code", "leetcode"]) == 1, "Test 1"
    assert min_extra_char("sayhelloworld", ["hello", "world"]) == 3,        "Test 2: say=3 extra"
    assert min_extra_char("abc", ["a", "b", "c"]) == 0,                     "Test 3: all covered"
    assert min_extra_char("abc", []) == 3,                                   "Edge: empty dict"
    print("All tests passed!")
