"""
============================================================
Problem: Shortest Word Distance
Pattern: Warmup
Difficulty: Easy
LeetCode: #243
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a list of words. Find two specific words and compute the shortest
distance (number of index positions) between any occurrence of word1 and word2.
Like a treasure hunt on a number line — find the closest pair of two X marks.

APPROACH: Linear Scan with Index Tracking
---------
1. Track the last seen index for word1 (i1) and word2 (i2).
   Initialize both to -1.
2. Scan the array. Whenever we see word1, update i1 = current index.
   Whenever we see word2, update i2 = current index.
3. If BOTH i1 and i2 are valid (not -1), update min_dist = min(min_dist, |i1 - i2|).
4. Return min_dist.

COMPLEXITY:
-----------
Time:  O(N) — single pass
Space: O(1) — only two index variables

EDGE CASES:
-----------
- word1 == word2: The problem guarantees they are different, but if equal, we
  track two occurrences of the same word.
- Words appear only once each: Still works, one valid pair at the end.
============================================================
"""

from typing import List
import math


def shortest_word_distance(words: List[str], word1: str, word2: str) -> int:
    i1, i2 = -1, -1
    min_dist = math.inf

    for i, word in enumerate(words):
        if word == word1:
            i1 = i
        elif word == word2:
            i2 = i
        if i1 != -1 and i2 != -1:
            min_dist = min(min_dist, abs(i1 - i2))

    return int(min_dist)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    words1 = ["practice", "makes", "perfect", "coding", "makes"]
    assert shortest_word_distance(words1, "coding", "practice") == 3, "Test 1"
    assert shortest_word_distance(words1, "makes", "coding") == 1,    "Test 2"

    words2 = ["a", "c", "b", "b", "a"]
    assert shortest_word_distance(words2, "a", "b") == 1,             "Test 3"
    print("All tests passed!")
