"""
============================================================
Problem: Merge Similar Items
Pattern: Ordered Set / Sorting
Difficulty: Easy
Link: https://leetcode.com/problems/merge-similar-items/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have two lists of items. Each item has a value and a weight. If the same
value appears in both lists, combine their weights. Return all unique values
sorted by value, each with the total weight.

APPROACH:
---------
1. Use a dictionary (or SortedDict) to merge weights by value.
2. Sort the result by value.
   (In an interview, mentioning SortedDict from sortedcontainers is a plus,
    but a regular dict + sorting works fine for this easy problem.)

COMPLEXITY:
-----------
Time:  O((N + M) log(N + M)) for sorting.
Space: O(N + M) for the dictionary.

EDGE CASES:
-----------
- No overlapping values.
- All values overlap.
- Empty input list.
============================================================
"""

from typing import List
from collections import defaultdict


def merge_similar_items(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    weight_map = defaultdict(int)

    for val, weight in items1:
        weight_map[val] += weight
    for val, weight in items2:
        weight_map[val] += weight

    return sorted([val, weight] for val, weight in weight_map.items())


if __name__ == "__main__":
    assert merge_similar_items([[1,1],[4,5],[3,8]], [[3,1],[1,5]]) == [[1,6],[3,9],[4,5]], "Test 1"
    assert merge_similar_items([[1,1],[3,2],[2,3]], [[2,1],[3,2],[1,3]]) == [[1,4],[2,4],[3,4]], "Test 2"
    assert merge_similar_items([[1,3],[2,2]], [[7,1],[2,2],[1,4]]) == [[1,7],[2,4],[7,1]], "Test 3"
    print("All tests passed!")
