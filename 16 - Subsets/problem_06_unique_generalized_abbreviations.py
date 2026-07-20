"""
============================================================
Problem: Unique Generalized Abbreviations
Pattern: Subsets (BFS)
Difficulty: Hard (Advanced)
Link: https://leetcode.com/problems/generalized-abbreviation/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are given a word, like `"BAT"`.
An abbreviation replaces letters with numbers representing how many letters 
were skipped.
For example, `"B1T"` skips the 'A'. `"3"` skips all three letters.
You want to generate EVERY possible abbreviation!
For every single letter in the word, you have exactly two choices:
Choice 1: Keep the letter!
Choice 2: Abbreviate the letter! (Instead of writing the letter, we start 
counting how many letters we've abbreviated in a row).

We can use a Queue to explore all branches.
We put a bundle in our queue: `(current_string, current_index, abbreviation_count)`.
Start: `("", 0, 0)`

Pop it. The first letter is `'B'`.
- Branch 1 (Keep 'B'): We must first write down any existing abbreviations we 
  counted up! Since `abbreviation_count` is 0, we just write `'B'`. 
  Push `("B", index 1, count 0)`.
- Branch 2 (Abbreviate 'B'): We don't write anything, we just increment our count! 
  Push `("", index 1, count 1)`.

Pop `("", 1, 1)`. The next letter is `'A'`.
- Branch 1 (Keep 'A'): We MUST write down our abbreviation count `1` before 
  writing `'A'`. So the string becomes `"1A"`. Push `("1A", index 2, count 0)`.
- Branch 2 (Abbreviate 'A'): We just increment the count! 
  Push `("", index 2, count 2)`.

When we reach the end of the word, if we still have a `count > 0`, we just 
slap it onto the end of the string!

APPROACH:
---------
1. Initialize `result = []`.
2. Initialize `queue = deque([("", 0, 0)])` storing `(string, index, count)`.
3. Loop while `queue` is not empty:
   - Pop the bundle: `s, i, count = queue.popleft()`.
   - Base Case: If `i == len(word)`, we reached the end!
     - If `count > 0`, we have to append it to the end of our string: `s += str(count)`.
     - Append `s` to `result`.
   - Branch 1: Abbreviate the current letter! 
     We just increment `count` by 1 and move to the next index.
     `queue.append((s, i + 1, count + 1))`
   - Branch 2: Keep the current letter!
     If we had a `count > 0`, we MUST append that number to our string FIRST.
     Then, we append the actual letter `word[i]`.
     Because we broke the chain of abbreviations, we reset `count` to 0!
     `queue.append((s + (str(count) if count > 0 else "") + word[i], i + 1, 0))`
4. Return `result`.

COMPLEXITY:
-----------
Time:  O(N * 2^N) — There are exactly 2^N combinations. For each one, we manipulate strings of length N.
Space: O(N * 2^N) — To store all combinations in the result and queue.

EDGE CASES:
-----------
- Edge case 1: Empty word `""`. Returns `[""]`.
============================================================
"""

from typing import List
from collections import deque

def generate_generalized_abbreviation(word: str) -> List[str]:
    """
    Generates all unique generalized abbreviations of a word.
    """
    result = []
    
    # Store tuples of (current_string, current_index, current_abbreviation_count)
    queue = deque([("", 0, 0)])
    
    word_len = len(word)
    
    while queue:
        s, i, count = queue.popleft()
        
        # Base case: we reached the end of the word
        if i == word_len:
            # If we had a running count of abbreviated letters, append it at the very end
            if count > 0:
                s += str(count)
            result.append(s)
        else:
            # Branch 1: Abbreviate the current character
            # We don't add anything to the string yet, we just increment our count!
            queue.append((s, i + 1, count + 1))
            
            # Branch 2: Keep the current character
            # If we had a running count, we MUST write it down BEFORE writing the character
            new_s = s
            if count > 0:
                new_s += str(count)
            new_s += word[i]
            
            # We kept a character, so the abbreviation chain is broken. Reset count to 0!
            queue.append((new_s, i + 1, 0))
            
    return result

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # Word: "BAT"
    # Size: 2^3 = 8
    result1 = generate_generalized_abbreviation("BAT")
    expected1 = ["3", "2T", "1A1", "1AT", "B2", "B1T", "BA1", "BAT"]
    assert sorted(result1) == sorted(expected1), "Test 1 failed"

    # Word: "code"
    # Size: 2^4 = 16
    result2 = generate_generalized_abbreviation("code")
    expected2 = ["4","3e","2d1","2de","1o2","1o1e","1od1","1ode",
                 "c3","c2e","c1d1","c1de","co2","co1e","cod1","code"]
    assert sorted(result2) == sorted(expected2), "Test 2 failed"

    # 🔲 Edge cases
    assert generate_generalized_abbreviation("") == [""], "Edge 1: Empty string"
    assert sorted(generate_generalized_abbreviation("A")) == ["1", "A"], "Edge 2: Single char"

    print("All tests passed!")
