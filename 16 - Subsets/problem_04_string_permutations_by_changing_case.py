"""
============================================================
Problem: Letter Case Permutation
Pattern: Subsets (BFS)
Difficulty: Medium
Link: https://leetcode.com/problems/letter-case-permutation/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are given a password like `"a1b"`.
Some characters are letters, some are numbers.
For every letter, it can be either lowercase or uppercase. You want to find EVERY 
possible combination of passwords!
You start with your original password in a box: `["a1b"]`.
You scan the password from left to right.
First character is `'a'`. It's a letter!
So, you make a copy of everything in your box. In the copies, you change the `'a'` 
to an `'A'`.
Now your box has: `["a1b", "A1b"]`.
Second character is `'1'`. It's a number! We ignore it and do nothing.
Third character is `'b'`. It's a letter!
You make copies of EVERYTHING in your box, and change the `'b'` to a `'B'` in 
the copies.
Now your box has: `["a1b", "A1b", "a1B", "A1B"]`.
You are done!

APPROACH:
---------
1. Initialize `permutations = [s]`. (We start with the original string).
2. Loop through every character index `i` from `0` to `len(s) - 1`.
3. If `s[i]` is a letter (use `.isalpha()`):
   - Take a snapshot of the current size of the list: `n = len(permutations)`.
   - Loop `j` from `0` to `n - 1`:
     - Since strings are immutable in Python, we convert the string `permutations[j]` 
       into a list of characters: `chs = list(permutations[j])`.
     - Swap the case of the character at index `i`: `chs[i] = chs[i].swapcase()`.
     - Convert the list back to a string and append it: `permutations.append("".join(chs))`.
4. Return `permutations`.

COMPLEXITY:
-----------
Time:  O(N * 2^N) — In the worst case, every character is a letter, so there are 2^N permutations. 
       We do string/list conversions which take O(N) time for each permutation.
Space: O(N * 2^N) — To store all the resulting strings.

EDGE CASES:
-----------
- Edge case 1: String has no letters (e.g., `"123"`). Returns `["123"]`.
============================================================
"""

from typing import List

def letter_case_permutation(s: str) -> List[str]:
    """
    Returns all possible strings we could create by swapping the case of letters.
    """
    permutations = [s]
    
    for i in range(len(s)):
        # We only care about letters. Ignore numbers!
        if s[i].isalpha():
            # Take snapshot of current size
            n = len(permutations)
            
            for j in range(n):
                # 1. Convert string to a list of characters so we can mutate it
                chs = list(permutations[j])
                
                # 2. Swap the case (lower becomes upper, upper becomes lower)
                chs[i] = chs[i].swapcase()
                
                # 3. Join back into a string and add to our list
                permutations.append("".join(chs))
                
    return permutations

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # "a1b2" -> "a1b2", "A1b2", "a1B2", "A1B2"
    result1 = letter_case_permutation("a1b2")
    expected1 = ["a1b2", "A1b2", "a1B2", "A1B2"]
    # Order doesn't strictly matter for the problem, but our algorithm generates this exact order
    assert result1 == expected1, f"Test 1 failed. Got {result1}"

    # 🔲 Edge cases
    assert letter_case_permutation("12345") == ["12345"], "Edge 1: No letters"
    assert letter_case_permutation("C") == ["C", "c"], "Edge 2: Single uppercase letter"

    print("All tests passed!")
