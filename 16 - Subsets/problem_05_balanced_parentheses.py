"""
============================================================
Problem: Balanced Parentheses
Pattern: Subsets (BFS)
Difficulty: Hard
Link: https://leetcode.com/problems/generate-parentheses/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are given a number `n`. You need to create all possible strings that use 
exactly `n` open parentheses `(` and `n` close parentheses `)`.
BUT, they must be "balanced"! 
Balanced means you can never have more close parentheses than open parentheses 
at any point while reading from left to right.
For example, `)(` is illegal because you closed it before you opened it!

We start with an empty string: `""`.
We can only add a `(` if we haven't used all `n` of them yet.
We can only add a `)` if we currently have MORE open ones than close ones!

Let's use a Queue (BFS).
We start the queue with a bundle: `(current_string, open_count, close_count)`.
Start: `("", 0, 0)`
Pop it. Can we add `(`? Yes (0 < 3). Push `("(", 1, 0)`.
Pop `("(", 1, 0)`. 
  - Can we add `(`? Yes (1 < 3). Push `("((", 2, 0)`.
  - Can we add `)`? Yes (0 < 1). Push `("()", 1, 1)`.
Keep doing this until `open_count == n` AND `close_count == n`. Then we have 
a finished, balanced string!

APPROACH:
---------
1. Initialize `result = []`.
2. Initialize `queue = deque([("", 0, 0)])` storing `(string, open_count, close_count)`.
3. Loop while `queue` is not empty:
   - Pop the bundle: `s, open_count, close_count = queue.popleft()`.
   - Base Case: If `open_count == n` and `close_count == n`, we finished a valid 
     string! Append `s` to `result`.
   - Branch 1: If `open_count < n`, we are allowed to add an open parenthesis. 
     Append `(s + "(", open_count + 1, close_count)` to the queue.
   - Branch 2: If `close_count < open_count`, we are allowed to add a close parenthesis.
     Append `(s + ")", open_count, close_count + 1)` to the queue.
4. Return `result`.

COMPLEXITY:
-----------
Time:  O(4^N / sqrt(N)) — This is the Nth Catalan number. It's the exact number 
       of valid combinations.
Space: O(4^N / sqrt(N)) — To store the results and the queue.

EDGE CASES:
-----------
- Edge case 1: n = 0. Returns `[""]`. (Though usually n >= 1 in constraints).
============================================================
"""

from typing import List
from collections import deque

def generate_parentheses(n: int) -> List[str]:
    """
    Generates all combinations of n pairs of balanced parentheses.
    """
    result = []
    
    # Store tuples of (current_string, open_count, close_count)
    queue = deque([("", 0, 0)])
    
    while queue:
        s, open_count, close_count = queue.popleft()
        
        # If we have reached the required number of pairs, add to result
        if open_count == n and close_count == n:
            result.append(s)
        else:
            # We can always add an open parenthesis if we haven't reached n
            if open_count < n:
                queue.append((s + "(", open_count + 1, close_count))
                
            # We can ONLY add a close parenthesis if we have unmatched open ones
            if close_count < open_count:
                queue.append((s + ")", open_count, close_count + 1))
                
    return result

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # Input: 2
    # Output: ["(())", "()()"]
    result1 = generate_parentheses(2)
    expected1 = ["(())", "()()"]
    # We sort both to ensure order doesn't fail the test
    assert sorted(result1) == sorted(expected1), "Test 1 failed"

    # Input: 3
    result2 = generate_parentheses(3)
    expected2 = ["((()))","(()())","(())()","()(())","()()()"]
    assert sorted(result2) == sorted(expected2), "Test 2 failed"

    # 🔲 Edge cases
    assert generate_parentheses(1) == ["()"], "Edge 1: n = 1"

    print("All tests passed!")
