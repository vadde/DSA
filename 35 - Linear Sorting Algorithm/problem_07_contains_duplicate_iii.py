"""
============================================================
Problem: Contains Duplicate III
Pattern: Linear Sorting (Bucket Sort variant)
Difficulty: Hard
Link: https://leetcode.com/problems/contains-duplicate-iii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Find if there are two numbers in the array that are very close to each other
in VALUE (difference at most `valueDiff`) AND very close to each other in 
POSITION (index difference at most `indexDiff`).
Instead of checking all pairs, we can use buckets of size `valueDiff + 1`.

APPROACH:
---------
1. Use buckets of size `t + 1` (where t = valueDiff).
2. If two elements belong to the same bucket, their difference is at most `t`.
3. An element in bucket `i` could also be close to elements in bucket `i-1` or `i+1`.
4. Maintain a sliding window of buckets of size `k` (where k = indexDiff).
5. If the window exceeds size `k`, remove the oldest element's bucket.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(min(N, K))

EDGE CASES:
-----------
- valueDiff < 0 -> Impossible, return False.
- indexDiff <= 0 -> Impossible, return False.
============================================================
"""

from typing import List

def containsNearbyAlmostDuplicate(nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    if valueDiff < 0 or indexDiff <= 0:
        return False
        
    buckets = {}
    w = valueDiff + 1 # Bucket size
    
    for i, num in enumerate(nums):
        bucket_id = num // w
        
        # Check current bucket
        if bucket_id in buckets:
            return True
            
        # Check adjacent buckets
        if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
            return True
        if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
            return True
            
        # Add to bucket
        buckets[bucket_id] = num
        
        # Maintain window size
        if i >= indexDiff:
            del buckets[nums[i - indexDiff] // w]
            
    return False

if __name__ == "__main__":
    assert containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) == True, "Test 1"
    assert containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) == False, "Test 2"
    print("All tests passed!")
