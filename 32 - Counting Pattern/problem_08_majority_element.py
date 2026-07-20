"""
============================================================
Problem: Majority Element
Pattern: Counting (Boyer-Moore Voting Algorithm)
Difficulty: Easy
Link: https://leetcode.com/problems/majority-element/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a list of votes for different candidates. One candidate has MORE THAN
HALF of the votes (the majority). Find out who it is.
You could count everyone's votes, but can you do it by just keeping track of 
one candidate and a single tally counter?

APPROACH (Boyer-Moore Voting):
---------
1. Maintain a `candidate` and a `count`.
2. For each vote:
   - If `count == 0`, pick the current vote as the new `candidate`.
   - If the vote matches the `candidate`, `count += 1`.
   - If the vote doesn't match, `count -= 1`.
3. Because the majority element appears more than N/2 times, its count will
   always outlast all other elements combined.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(1)

EDGE CASES:
-----------
- Only one element -> it is the majority.
- Array with exact N/2 + 1 majority elements.
============================================================
"""

from typing import List

def majorityElement(nums: List[int]) -> int:
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
            
    return candidate

if __name__ == "__main__":
    assert majorityElement([3,2,3]) == 3, "Test 1"
    assert majorityElement([2,2,1,1,1,2,2]) == 2, "Test 2"
    assert majorityElement([5]) == 5, "Test 3: Single element"
    print("All tests passed!")
