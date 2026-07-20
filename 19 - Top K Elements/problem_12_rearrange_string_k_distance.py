"""
============================================================
Problem: Rearrange String K Distance Apart
Pattern: Top K Elements
Difficulty: Hard
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cd2a00cc465d6c8279d
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
This is EXACTLY the same as the last problem! 
In the last problem, you wanted NO two identical characters to be next to each 
other. That means they had to be at least `2` distance apart!
(Example: "pap". The 'p's are at index 0 and 2. Distance = 2-0 = 2).
Now, someone gives you a specific number `K`. They want the same characters 
to be at least `K` distance apart!
In the last problem, our "Waiting Room" was just a single variable (`previous_char`), 
which meant the character had to wait exactly ONE turn before being allowed 
back in the heap.
Now, the character needs to wait `K - 1` turns!
So, instead of a single variable, we make our Waiting Room a **Queue**.
1. We pop the most frequent character.
2. We add it to our string.
3. We put it in the Queue (the Waiting Room).
4. As soon as the Queue gets to size `K`, it means the person at the front of 
   the line has been waiting exactly long enough!
5. We let the person at the front out of the Queue and put them back in the 
   Max-Heap so they can be picked again!

APPROACH:
---------
1. Count the frequencies of all characters.
2. Push `(-frequency, char)` into a `max_heap`.
3. Initialize a `queue` using `collections.deque`.
4. Initialize a `result` list.
5. Loop while `max_heap` is not empty:
   - Pop `freq, char` from the heap.
   - Append `char` to `result`.
   - Push `(freq + 1, char)` into the `queue`. (Adding 1 to negative freq).
   - If `len(queue) == k`:
     - Pop from the front of the queue: `past_freq, past_char = queue.popleft()`.
     - If `past_freq < 0`, push it back into the `max_heap`!
6. If the length of the result string == original string length, return it.
   Else, return `""`.

COMPLEXITY:
-----------
Time:  O(N * log D) — N is string length, D is distinct characters.
Space: O(D) — For the Hash Map, Heap, and Queue.

EDGE CASES:
-----------
- Edge case 1: K is 0 or 1. If K <= 1, they don't even need to be separated. 
  We could just return the original string or the sorted string. (But our queue 
  logic will actually handle K=1 gracefully by immediately popping).
============================================================
"""

import heapq
from typing import List
from collections import Counter, deque

def rearrange_string_k_distance(s: str, k: int) -> str:
    """
    Rearranges a string so that identical characters are at least K distance apart.
    """
    if k <= 1:
        return s
        
    freq_map = Counter(s)
    max_heap = []
    
    # 1. Put all characters into a Max-Heap
    for char, freq in freq_map.items():
        heapq.heappush(max_heap, (-freq, char))
        
    queue = deque()
    result = []
    
    # 2. Greedily pick the most frequent character
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        
        # Append to result
        result.append(char)
        
        # 3. Put the character in the waiting room!
        queue.append((freq + 1, char))
        
        # 4. If the waiting room is exactly K in size, the person at the front 
        #    has waited long enough! Let them back into the Heap!
        if len(queue) == k:
            past_freq, past_char = queue.popleft()
            if past_freq < 0:
                heapq.heappush(max_heap, (past_freq, past_char))
                
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
    res1 = rearrange_string_k_distance("mmpp", 2)
    # Valid arrangements: "mpmp" or "pmpm". Both are length 4.
    assert len(res1) == 4, "Test 1"
    
    res2 = rearrange_string_k_distance("Programming", 3)
    assert len(res2) == len("Programming"), "Test 2"

    # 🔲 Edge cases
    assert rearrange_string_k_distance("aab", 2) == "aba", "Edge 1"
    assert rearrange_string_k_distance("aab", 3) == "", "Edge 2: Impossible"

    print("All tests passed!")
