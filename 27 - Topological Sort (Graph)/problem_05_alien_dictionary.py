"""
============================================================
Problem: Alien Dictionary
Pattern: Topological Sort (Graph)
Difficulty: Hard
LeetCode: #269
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You receive a sorted list of words from an alien language. From the sort order,
figure out the ORDERING of characters in the alien alphabet.
E.g. words=["wrt","wrf","er","ett","rftt"] → "wertf"

APPROACH: Build graph from adjacent word comparisons + Topological Sort
---------
1. For each consecutive pair of words, find the FIRST differing character.
   Add an edge: word1_char → word2_char (word1_char comes before word2_char).
2. If word1 is a prefix of word2 AND longer → invalid input (return "").
3. Run Kahn's topological sort on the character graph.
4. If result has all characters → valid. If cycle → return "".

COMPLEXITY: O(C) where C = total characters across all words.
============================================================
"""

from typing import List
from collections import deque, defaultdict


def alien_order(words: List[str]) -> str:
    # Gather all unique chars
    char_set = set(c for word in words for c in word)
    adj: dict[str, List[str]] = {c: [] for c in char_set}
    in_degree: dict[str, int] = {c: 0 for c in char_set}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""  # invalid: longer word is prefix of shorter
        for j in range(min_len):
            if w1[j] != w2[j]:
                adj[w1[j]].append(w2[j])
                in_degree[w2[j]] += 1
                break

    queue: deque[str] = deque(c for c in in_degree if in_degree[c] == 0)
    result = []
    while queue:
        c = queue.popleft()
        result.append(c)
        for neighbor in adj[c]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(char_set):
        return ""  # cycle detected
    return "".join(result)


if __name__ == "__main__":
    res = alien_order(["wrt", "wrf", "er", "ett", "rftt"])
    # Must have: t<f, w<e, r<t, e<r → w<e<r<t<f
    assert res.index('w') < res.index('e'), "w before e"
    assert res.index('e') < res.index('r'), "e before r"
    assert res.index('r') < res.index('t'), "r before t"
    assert res.index('t') < res.index('f'), "t before f"

    assert alien_order(["z", "x"]) == "zx", "Test 2"
    assert alien_order(["z", "x", "z"]) == "", "Test 3: cycle"
    assert alien_order(["abc", "ab"]) == "", "Test 4: invalid prefix"
    print("All tests passed!")
