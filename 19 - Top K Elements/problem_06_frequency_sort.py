"""
============================================================
Problem: Frequency Sort
Pattern: Top K Elements
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cbea00cc465d6c8277d
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a word: `"Programming"`.
You want to rebuild the word so that the most popular letters come FIRST.
First, we count the letters!
P: 1
r: 2
o: 1
g: 2
a: 1
m: 2
i: 1
n: 1
Now, we want to grab the MOST popular letters. Who gives us the largest things 
first? A **Max-Heap**!
We throw all these counts into a Max-Heap.
Then, we just pop them out one by one. The Max-Heap guarantees that the letters 
with the biggest counts will come out first.
When 'r' comes out (count 2), we add `"rr"` to our new string.
When 'g' comes out (count 2), we add `"gg"`.
When 'm' comes out (count 2), we add `"mm"`.
When 'P' comes out (count 1), we add `"P"`.
...and so on!
Result: `"rrggmmPioan"` (or some variation depending on tie-breakers).

APPROACH:
---------
1. Count the frequencies of all characters in the string using a Hash Map.
2. Initialize a `max_heap = []`.
3. Loop through the Hash Map and push `(-frequency, char)` to simulate a Max-Heap.
   - Note: If frequencies are the same, Python will try to compare the characters 
     themselves. This is fine because characters are comparable (alphabetical order)!
4. Pop elements from the heap one by one.
5. Append `char * frequency` to a result list.
6. Join the result list into a string and return it.

COMPLEXITY:
-----------
Time:  O(D * log D) — Where D is the number of DISTINCT characters. In the worst 
       case, D = N. (Or D is a constant like 26 for lowercase English, making 
       the heap part O(1), and the total time O(N) for counting).
Space: O(D) — For the Hash Map and Heap.

EDGE CASES:
-----------
- Edge case 1: String is empty. Returns empty string.
============================================================
"""

import heapq
from typing import List
from collections import Counter

def sort_character_by_frequency(s: str) -> str:
    """
    Sorts a string based on the decreasing frequency of its characters.
    """
    # 1. Count frequencies
    freq_map = Counter(s)
    
    max_heap = []
    
    # 2. Push to Max-Heap (using negative frequencies)
    for char, freq in freq_map.items():
        heapq.heappush(max_heap, (-freq, char))
        
    # 3. Build the result string
    result = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        
        # freq is negative, so we make it positive
        count = -freq
        
        # Append the character 'count' times
        result.append(char * count)
        
    return "".join(result)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # For "Programming", r=2, g=2, m=2. P,o,a,i,n = 1
    # Note: Characters with the same frequency will be sorted alphabetically 
    # because of the tuple comparison `(-freq, char)`.
    # -2, 'g' -> -2, 'm' -> -2, 'r'
    # Wait, actually, since they are negative, 'g' comes before 'm' because 
    # (-2, 'g') < (-2, 'm'). So 'g' is popped first.
    # Let's just verify the length and that the characters are grouped.
    res1 = sort_character_by_frequency("Programming")
    assert len(res1) == len("Programming"), "Test 1 length"
    assert "gg" in res1 and "mm" in res1 and "rr" in res1, "Test 1 groupings"
    
    res2 = sort_character_by_frequency("abcbab")
    # b: 3, a: 2, c: 1 => bbb aac
    assert res2 == "bbbaac", f"Test 2 failed. Got {res2}"

    # 🔲 Edge cases
    assert sort_character_by_frequency("") == "", "Edge 1: Empty string"
    assert sort_character_by_frequency("A") == "A", "Edge 2: Single char"

    print("All tests passed!")
