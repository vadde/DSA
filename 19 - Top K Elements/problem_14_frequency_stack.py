"""
============================================================
Problem: Frequency Stack
Pattern: Top K Elements
Difficulty: Hard
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cdda00cc465d6c827aa
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are designing a magic box. You can put numbers into it (`push`), and you 
can ask it to give you a number back (`pop`).
Normally, a box gives you the LAST thing you put in.
But this magic box gives you the MOST POPULAR thing inside it! (The most frequent).
If there is a tie (e.g., both `5` and `7` are inside the box twice), it gives 
you the one that was put in MOST RECENTLY.
How do we build this? We need three things to decide who wins:
1. Frequency (Higher wins)
2. Sequence / Age (Newer wins)
So, we use a **Max-Heap**! But what do we put in the Max-Heap?
We put a tuple: `(-frequency, -sequence_number, number)`.
- The first thing it looks at is `frequency`. The highest (most negative) wins.
- If they tie, it looks at `sequence_number`. The newest (most negative) wins!
"But wait!" you say. "If I push `5` twice, do I have to search the heap to 
update its frequency?!"
NO! This is the most beautiful part of this algorithm.
When you push `5` the first time, you put `(freq=1, seq=1, num=5)` in the heap.
When you push `5` the second time, you just put a NEW entry in the heap: 
`(freq=2, seq=2, num=5)`.
The heap now has TWO entries for `5`. But the `freq=2` one is guaranteed to 
be popped first! 
When you pop it, you just decrease the count of `5` in your Hash Map back to `1`.
The old `freq=1` entry is still sitting in the heap, waiting perfectly for the 
next time you need a `5` with frequency 1!

APPROACH:
---------
1. In `__init__`, create `sequence_number = 0`, an empty `max_heap`, and a 
   `frequency_map` (using `collections.defaultdict(int)`).
2. In `push(num)`:
   - `frequency_map[num] += 1`
   - `sequence_number += 1`
   - Push `(-frequency_map[num], -sequence_number, num)` to `max_heap`.
3. In `pop()`:
   - Pop from `max_heap`. The elements are `(-freq, -seq, num)`.
   - The number to return is `num`.
   - Decrease `frequency_map[num]` by 1.
   - Return `num`.

COMPLEXITY:
-----------
Time:  O(log N) for both `push()` and `pop()`. (N is number of elements).
Space: O(N) — To store all elements in the Heap and Hash Map.

EDGE CASES:
-----------
- Edge case 1: Popping from an empty stack (we assume this won't happen or we 
  could handle it by returning `None` or raising an Exception).
============================================================
"""

import heapq
from collections import defaultdict

class FrequencyStack:
    def __init__(self):
        # Keeps track of the exact order elements were pushed
        self.sequence_number = 0
        # The Max-Heap to sort by (Frequency -> Sequence)
        self.max_heap = []
        # Hash Map to track current frequencies
        self.frequency_map = defaultdict(int)

    def push(self, num: int) -> None:
        """
        Pushes a number onto the stack.
        """
        # Increment frequency and sequence
        self.frequency_map[num] += 1
        self.sequence_number += 1
        
        # Push to Max-Heap (we negate so the largest values rise to the top)
        heapq.heappush(
            self.max_heap, 
            (-self.frequency_map[num], -self.sequence_number, num)
        )

    def pop(self) -> int:
        """
        Removes and returns the most frequent element in the stack.
        """
        # Pop the most frequent (and most recent, if tied)
        freq, seq, num = heapq.heappop(self.max_heap)
        
        # Decrease its frequency in the map
        self.frequency_map[num] -= 1
        
        return num

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    freq_stack = FrequencyStack()
    freq_stack.push(1)
    freq_stack.push(2)
    freq_stack.push(1)
    freq_stack.push(3)
    freq_stack.push(2)
    freq_stack.push(1)
    
    # Heap has 1 (freq 3), 2 (freq 2), 3 (freq 1)
    assert freq_stack.pop() == 1, "Test 1: 1 is most frequent"
    # Now 1 (freq 2), 2 (freq 2). 2 was pushed later!
    assert freq_stack.pop() == 2, "Test 2: 2 and 1 tie, but 2 is newer"
    # Now 1 (freq 2), 2 (freq 1).
    assert freq_stack.pop() == 1, "Test 3: 1 is most frequent again"

    print("All tests passed!")
