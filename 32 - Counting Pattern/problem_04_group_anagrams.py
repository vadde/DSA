"""
============================================================
Problem: Group Anagrams
Pattern: Counting Pattern
Difficulty: Medium
LeetCode: #49
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array of strings, group the anagrams together.
"eat", "tea", "tan", "ate", "nat", "bat" ->
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

APPROACH: Tuple of Frequency Counts as Hash Key
---------
Instead of sorting each string (which takes O(K log K) per string),
we build a frequency array of size 26 for each string.
We convert this array to a tuple (since tuples are hashable in Python)
and use it as the key in our Hash Map.

COMPLEXITY:
-----------
Time:  O(N * K) where N is number of words, K is max length of word.
Space: O(N * K)
============================================================
"""

from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Tuple is hashable!
        groups[tuple(count)].append(s)
        
    return list(groups.values())


if __name__ == "__main__":
    res = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Convert lists to sorted lists of sorted lists to compare safely
    res_sorted = sorted([sorted(group) for group in res])
    expected = sorted([sorted(["eat", "tea", "ate"]), sorted(["tan", "nat"]), sorted(["bat"])])
    assert res_sorted == expected, "Test 1"
    
    assert group_anagrams([""]) == [[""]], "Test 2"
    assert group_anagrams(["a"]) == [["a"]], "Test 3"
    print("All tests passed!")
