"""
============================================================
Problem: Search Suggestions System
Pattern: Trie
Difficulty: Medium
LeetCode: #1268
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given a list of products and a search word, for each prefix of the search word,
return at most 3 products with that prefix that come first lexicographically.
This is exactly how phone/browser autocomplete works!

APPROACH: Trie with sorted products
---------
1. Sort products lexicographically.
2. Build Trie. Each node stores a list of up to 3 product names that pass through it.
   Since products are sorted, the first 3 are always lexicographically smallest.
3. For each prefix of search_word, retrieve the suggestion list from the Trie node.

COMPLEXITY:
-----------
Time:  O(M log M + M*L + N*L) — sort + Trie build + queries
Space: O(M*L) — Trie storage
Where M=number of products, L=avg length, N=search word length.
============================================================
"""

from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.suggestions: List[str] = []


def suggested_products(products: List[str], search_word: str) -> List[List[str]]:
    products.sort()
    root = TrieNode()

    # Build Trie, storing up to 3 suggestions per node
    for product in products:
        node = root
        for ch in product:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if len(node.suggestions) < 3:
                node.suggestions.append(product)

    # Query for each prefix of search_word
    result: List[List[str]] = []
    node = root
    for ch in search_word:
        if node and ch in node.children:
            node = node.children[ch]
            result.append(node.suggestions[:])
        else:
            node = None  # type: ignore
            result.append([])
    return result


if __name__ == "__main__":
    res = suggested_products(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
    expected = [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]
    assert res == expected, f"Test 1 failed: {res}"

    res2 = suggested_products(["havana"], "havana")
    assert all(r == ["havana"] for r in res2), "Test 2"

    print("All tests passed!")
