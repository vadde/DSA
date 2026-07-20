"""
============================================================
Problem: Sort Characters By Frequency
Pattern: Counting Pattern
Difficulty: Medium
LeetCode: #451
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given a string, sort it in DECREASING order based on the frequency of the characters.
"tree" -> "e" appears twice, "t" and "r" appear once.
Result: "eert" or "eetr".

APPROACH: Hash Map Frequency Count -> Bucket Sort
---------
1. Count the frequencies of all characters.
2. We could just sort the characters by frequency (O(K log K) where K is unique chars).
3. OR use Bucket Sort! Create an array of strings where the index represents
   the frequency. Max frequency is the length of the string N.
4. Iterate backward over the buckets to build the result.

COMPLEXITY:
-----------
Time:  O(N) — Bucket sort avoids the O(N log N) step!
Space: O(N)
============================================================
"""

from collections import Counter


def frequency_sort(s: str) -> str:
    counts = Counter(s)
    
    # Bucket sort: index is frequency, value is list of chars with that frequency
    max_freq = max(counts.values()) if counts else 0
    buckets: list[list[str]] = [[] for _ in range(max_freq + 1)]
    
    for char, freq in counts.items():
        buckets[freq].append(char)
        
    result = []
    # Build result from highest frequency bucket down to 1
    for freq in range(max_freq, 0, -1):
        for char in buckets[freq]:
            result.append(char * freq)
            
    return "".join(result)


if __name__ == "__main__":
    res = frequency_sort("tree")
    assert res in ("eert", "eetr"), "Test 1"
    
    res2 = frequency_sort("cccaaa")
    assert res2 in ("cccaaa", "aaaccc"), "Test 2"
    
    assert frequency_sort("Aabb") == "bbAa" or frequency_sort("Aabb") == "bbaA", "Test 3: case sensitive"
    print("All tests passed!")
