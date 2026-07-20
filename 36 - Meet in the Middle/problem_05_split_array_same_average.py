"""
============================================================
Problem: Split Array With Same Average
Pattern: Meet in the Middle
Difficulty: Hard
Link: https://leetcode.com/problems/split-array-with-same-average/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Can you split an array of numbers into two groups (A and B) so that the 
AVERAGE value of both groups is exactly the same?
If Average(A) == Average(B), then it must also equal Average(Total).

APPROACH:
---------
1. If Average(A) == Average(Total), then Sum(A) = Average(Total) * len(A).
2. For this to be possible, Average(Total) * len(A) must be an integer.
3. This is a Subset Sum problem where we need a specific sum for a specific subset size.
4. With N up to 30, we can use Meet in the Middle or DP. Meet in the middle is 
   perfect: split into two halves, find all (sum, size) pairs, and see if they match.

COMPLEXITY:
-----------
Time:  O(2^(N/2))
Space: O(2^(N/2))

EDGE CASES:
-----------
- It's impossible to split if no valid integer sum exists for any valid length.
============================================================
"""

from typing import List

def splitArraySameAverage(nums: List[int]) -> bool:
    total_sum = sum(nums)
    n = len(nums)
    
    # Quick filter: is there any length i where total_sum * i is divisible by n?
    possible = False
    for i in range(1, n // 2 + 1):
        if (total_sum * i) % n == 0:
            possible = True
            break
    if not possible:
        return False
        
    # We want to find if there is a subset of size k with sum = total_sum * k / n.
    # To avoid floating point, we can shift every number: nums[i] = nums[i] * n - total_sum.
    # Then we just need to find a subset (size > 0 and size < n) that sums to 0!
    
    A = [num * n - total_sum for num in nums]
    
    # Meet in the middle
    left = A[:n//2]
    right = A[n//2:]
    
    left_sums = set()
    # bitmask to generate all subsets
    for i in range(1, 1 << len(left)):
        current_sum = sum(left[j] for j in range(len(left)) if (i & (1 << j)))
        if current_sum == 0:
            return True
        left_sums.add(current_sum)
        
    for i in range(1, 1 << len(right)):
        current_sum = sum(right[j] for j in range(len(right)) if (i & (1 << j)))
        if current_sum == 0:
            return True
        # Check if we can form 0 with the left side, but ensure we don't take ALL elements
        if -current_sum in left_sums and i != (1 << len(right)) - 1:
            return True
            
        # The edge case where we take all of right and all of left is excluded by the above
        # condition because taking all elements inherently sums to 0 (since sum(A) = 0),
        # but the problem requires two NON-EMPTY parts.
    
    # We also have to check the case where a combination of some right and all left is 0?
    # Actually `i != (1 << len(right)) - 1` prevents taking ALL of right when combined with 
    # some left? Wait, if we take ALL left and ALL right, sum is 0. So we just need to make 
    # sure we don't take both ALL left AND ALL right. 
    # We can just check if `-current_sum in left_sums`. If it is, and we aren't using all N elements.
    for i in range(1, (1 << len(right)) - 1): # exclude the full right subset from direct check if it pairs with full left
        current_sum = sum(right[j] for j in range(len(right)) if (i & (1 << j)))
        if -current_sum in left_sums:
            return True
            
    return False

if __name__ == "__main__":
    assert splitArraySameAverage([1,2,3,4,5,6,7,8]) == True, "Test 1"
    assert splitArraySameAverage([3,1]) == False, "Test 2"
    print("All tests passed!")
