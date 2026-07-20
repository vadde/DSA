"""
============================================================
Problem: Rearrange String
Pattern: Top K Elements
Difficulty: Hard
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1ccfa00cc465d6c82798
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a word: `"aappp"`.
You want to scramble the letters so that NO TWO IDENTICAL LETTERS are next 
to each other!
If you just randomly pick letters, you might get `"papap"`, which is good!
But how do we do it reliably?
We should ALWAYS try to place the letter we have the MOST of first! Because 
if we save all our `'p'`s for the end, we'll be forced to put them next to 
each other.
So, we use a **Max-Heap** to keep track of letter counts.
1. Pop the most frequent letter. (Let's say `'p'`).
2. Add `'p'` to our new string.
3. We have fewer `'p'`s now. Should we put it back in the Max-Heap?
   WAIT! If we put it back right away, it might STILL be the most frequent letter!
   And the Max-Heap will give it to us again on the very next turn, causing 
   two `'p'`s to be next to each other!
4. So, we hold the `'p'` in a "Waiting Room" (a `prev` variable).
5. On the NEXT turn, we pop a different letter (say, `'a'`). We add `'a'` to 
   the string.
6. NOW it is safe to take `'p'` out of the waiting room and put it back in 
   the heap! Because we just placed an `'a'`, so placing another `'p'` next 
   time is perfectly fine!

APPROACH:
---------
1. Count the frequencies of all characters in the string.
2. Push all `(-frequency, char)` pairs into a `max_heap`.
3. Keep track of a `previous_char` (initially `None`) and `previous_freq` (initially `0`).
4. Initialize a `result` list.
5. Loop while the `max_heap` is not empty:
   - Pop `freq, char` from the heap.
   - Append `char` to `result`.
   - If `previous_char` is not `None` and its frequency is still > 0, push it 
     back into the heap!
   - Set `previous_char = char`, and `previous_freq = freq + 1` (since freq is 
     negative, adding 1 brings it closer to 0).
6. If the length of `result` matches the original string length, return it!
   - If it doesn't match, it means we couldn't place all letters without 
     having them touch. Return `""`.

COMPLEXITY:
-----------
Time:  O(N * log D) — Where N is string length, D is distinct characters.
Space: O(D) — For the Hash Map and Heap.

EDGE CASES:
-----------
- Edge case 1: A single character takes up more than half the string (e.g., 
  `"aaab"`). It's mathematically impossible to separate them. The loop will 
  finish early and we return `""`.
============================================================
"""

import heapq
from typing import List
from collections import Counter

def rearrange_string(s: str) -> str:
    """
    Rearranges a string so that no two identical characters are adjacent.
    """
    freq_map = Counter(s)
    max_heap = []
    
    # 1. Put all characters and their counts into a Max-Heap
    for char, freq in freq_map.items():
        heapq.heappush(max_heap, (-freq, char))
        
    previous_char = None
    previous_freq = 0
    result = []
    
    # 2. Greedily pick the most frequent character
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        
        # Append it to the result
        result.append(char)
        
        # 3. If we had a character waiting from the LAST turn, it is now safe 
        #    to put it back in the heap!
        if previous_char is not None and previous_freq < 0:
            heapq.heappush(max_heap, (previous_freq, previous_char))
            
        # 4. Put the CURRENT character in the waiting room!
        # freq + 1 because the frequency is negative, so this effectively 
        # decreases the positive count by 1.
        previous_char = char
        previous_freq = freq + 1
        
    # If we couldn't place all characters, it's impossible!
    result_str = "".join(result)
    if len(result_str) == len(s):
        return result_str
    return ""

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # a: 2, p: 3 -> p, a, p, a, p
    assert rearrange_string("aappp") == "papap", "Test 1"
    
    # P: 1, r: 2, o: 1, g: 2, r, m: 2 -> valid arrangement
    res2 = rearrange_string("Programming")
    assert len(res2) == len("Programming"), "Test 2"
    # Verify no adjacent duplicates
    for i in range(1, len(res2)):
        assert res2[i] != res2[i-1], f"Test 2 failed. Adjacent duplicates in {res2}"

    # 🔲 Edge cases
    assert rearrange_string("aapa") == "", "Edge 1: Impossible"

    print("All tests passed!")
