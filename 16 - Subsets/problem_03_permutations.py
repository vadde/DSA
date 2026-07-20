"""
============================================================
Problem: Permutations
Pattern: Subsets (BFS)
Difficulty: Medium
Link: https://leetcode.com/problems/permutations/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
This time, you aren't just deciding whether to put toys IN or OUT of a box.
You MUST put ALL the toys in the box, but you care about what ORDER they are in!
Let's say you have toys `[1, 2, 3]`.
You start with an empty lineup: `[]`.
You pick up Toy 1. The only place it can go is at the start: `[1]`.
You pick up Toy 2. Where can it go? It can go BEFORE Toy 1, or AFTER Toy 1!
So you take your `[1]` lineup, and make TWO copies:
- Put Toy 2 at the front: `[2, 1]`
- Put Toy 2 at the back: `[1, 2]`
Now you pick up Toy 3. You take BOTH of those lineups, and for each one, Toy 3 
can go at the front, in the middle, or at the back!
- From `[2, 1]`, you make: `[3, 2, 1]`, `[2, 3, 1]`, `[2, 1, 3]`
- From `[1, 2]`, you make: `[3, 1, 2]`, `[1, 3, 2]`, `[1, 2, 3]`
You just found all 6 permutations!

APPROACH:
---------
1. Initialize a `result` array.
2. Initialize a queue (using `collections.deque`) with an empty list: `deque([[]])`.
3. Loop through every number in `nums`:
   - Take a snapshot of the queue size: `n = len(permutations)`.
   - Loop `n` times:
     - Pop an `old_permutation` from the front of the queue.
     - We want to insert the current number into EVERY possible slot of the `old_permutation`.
     - The number of slots is exactly `len(old_permutation) + 1` (e.g. if length is 2, we have index 0, index 1, and index 2).
     - Loop `j` from `0` to `len(old_permutation)`:
       - Create a deep copy: `new_permutation = list(old_permutation)`.
       - Insert the number at index `j`: `new_permutation.insert(j, current_number)`.
       - If the `new_permutation` is full size (`== len(nums)`), append it to `result`.
       - Otherwise, append it to the back of the `permutations` queue so it's ready for the next number!
4. Return `result`.

COMPLEXITY:
-----------
Time:  O(N * N!) — There are N! permutations. For each, we copy an array of size up to N.
Space: O(N * N!) — To store the results and the queue.

EDGE CASES:
-----------
- Edge case 1: Empty input array. Returns `[[]]`.
============================================================
"""

from typing import List
from collections import deque

def find_permutations(nums: List[int]) -> List[List[int]]:
    """
    Returns all possible permutations of an array of distinct integers.
    """
    if not nums:
        return [[]]
        
    result = []
    permutations = deque([[]])
    
    for current_number in nums:
        # Take a snapshot of how many partial permutations are in the queue
        n = len(permutations)
        
        for _ in range(n):
            # Take the oldest partial permutation out
            old_permutation = permutations.popleft()
            
            # Create a new permutation by inserting current_number into EVERY possible slot
            # If length is 2, possible indices are 0, 1, 2. (So range length + 1)
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, current_number)
                
                # If it's a complete permutation, add to result
                if len(new_permutation) == len(nums):
                    result.append(new_permutation)
                else:
                    # Otherwise, put it back in the queue for the next number
                    permutations.append(new_permutation)
                    
    return result

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # Input: [1, 2, 3]
    # Expected length: 3! = 6
    result1 = find_permutations([1, 2, 3])
    # The order of generation using this BFS approach usually puts the newest number
    # at index 0, then 1, then 2.
    expected1_length = 6
    assert len(result1) == expected1_length, "Test 1 failed"
    # We can also verify that [1,2,3] and [3,2,1] are inside
    assert [1, 2, 3] in result1 and [3, 2, 1] in result1, "Test 1 content check failed"

    # 🔲 Edge cases
    assert find_permutations([1]) == [[1]], "Edge 1: Single element"
    assert find_permutations([]) == [[]], "Edge 2: Empty array"

    print("All tests passed!")
