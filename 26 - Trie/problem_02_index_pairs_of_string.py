"""
============================================================
Problem: Index Pairs of a String
Pattern: Trie
Difficulty: Easy
LeetCode: #1065
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given a text string and a list of words, find all [i, j] index pairs such that
text[i..j] matches one of the words.
E.g. text="thestoryofleetcodeandme", words=["story","fleet","leetcode"] →
     [[3,7],[10,18],[19,21]] (but we return sorted pairs)

APPROACH: Trie for Efficient Prefix Matching
---------
Build a Trie from all words.
For each starting index i in text, walk the Trie character by character.
Whenever we hit a terminal node → record [i, j].

COMPLEXITY:
-----------
Time:  O(N * L) where N = text length, L = max word length
Space: O(M * L) where M = number of words
============================================================
"""

from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False


def index_pairs(text: str, words: List[str]) -> List[List[int]]:
    # Build Trie
    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    result = []
    n = len(text)
    for i in range(n):
        node = root
        for j in range(i, n):
            if text[j] not in node.children:
                break
            node = node.children[text[j]]
            if node.is_end:
                result.append([i, j])
    return result


if __name__ == "__main__":
    assert index_pairs("thestoryofleetcodeandme", ["story", "leetcode"]) == [
        [3, 7], [10, 17]
    ], "Test 1"
    assert index_pairs("ababa", ["aba", "ab"]) == [[0, 1], [0, 2], [2, 3], [2, 4]], "Test 2"
    assert index_pairs("foo", ["bar"]) == [], "Edge: no match"
    print("All tests passed!")
