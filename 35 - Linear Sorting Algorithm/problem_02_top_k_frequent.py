"""
============================================================
Problem: Top K Frequent Elements
Pattern: Bucket Sort (Linear Sorting)
Difficulty: Medium
LeetCode: #347
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array of numbers, return the K most frequent numbers.
You must do better than O(N log N). Can we do it in O(N)? Yes!

APPROACH: Bucket Sort
---------
1. Count the frequency of each number using a Hash Map.
2. The maximum possible frequency is N (if all numbers are the same).
3. Create N+1 "buckets" (an array of lists). The index of the bucket represents
   the frequency.
4. Put each number into the bucket corresponding to its frequency.
5. Traverse the buckets from right to left (highest frequency to lowest) and
   collect K elements!

COMPLEXITY:
-----------
Time:  O(N) — Counting takes O(N), bucket placement takes O(N), gathering takes O(N).
Space: O(N) — Buckets and hash map.
============================================================
"""

from typing import List
from collections import Counter


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    
    # Create buckets. max_freq is at most len(nums).
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    
    # Place numbers in buckets based on their frequency
    for num, freq in count.items():
        buckets[freq].append(num)
        
    result = []
    # Traverse backwards from highest frequency
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
                
    return result


if __name__ == "__main__":
    assert sorted(top_k_frequent([1,1,1,2,2,3], 2)) == [1, 2], "Test 1"
    assert top_k_frequent([1], 1) == [1],                      "Test 2"
    assert sorted(top_k_frequent([4,4,4,4,5,5,6], 2)) == [4, 5],"Test 3"
    print("All tests passed!")
