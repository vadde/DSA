"""
============================================================
Problem: Scheduling Tasks
Pattern: Top K Elements
Difficulty: Hard
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cd7a00cc465d6c827a3
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are a boss, and you have tasks for your workers: `["A", "A", "B", "C"]`.
But there's a union rule: If a worker does task `"A"`, they MUST take `K=2` 
coffee breaks (intervals) before they are allowed to do task `"A"` again!
During those coffee breaks, they CAN do other tasks, or they can just sit idle.
You want to finish all the tasks in the minimum amount of time.
What should you do?
Always assign the MOST common task first! If `"A"` has to be done 10 times, 
you want to start chipping away at `"A"` immediately, because every time you 
do it, you trigger a long coffee break for `"A"`.
So, we put our tasks in a **Max-Heap** based on how many times we need to do them.
We pull out tasks and assign them. 
Since the coffee break is `K`, a "block" of time where `"A"` cannot repeat is 
actually `K + 1` intervals long! (The time `"A"` takes, plus `K` breaks).
So we try to pull `K + 1` different tasks from the Max-Heap.
If we run out of different tasks in the heap before the block is full, the workers 
must sit IDLE. We still count those idle hours towards the total time!
Then, we put the tasks we just did (with their counts reduced by 1) back into 
the Max-Heap for the next block.

APPROACH:
---------
1. Count the frequencies of all tasks.
2. Push `(-frequency, task)` into a `max_heap`.
3. Initialize `total_intervals = 0`.
4. Loop while `max_heap` is not empty:
   - Create a `wait_list` for the tasks we process in this block.
   - We need to process `K + 1` tasks to complete a block (so a task can repeat 
     safely in the next block).
   - Loop `n` from `0` to `K` (which is `K + 1` times):
     - If `max_heap` is not empty:
       - `freq, task = heappop(max_heap)`
       - `total_intervals += 1`
       - If `freq + 1 < 0`, the task still needs to be done more times! 
         Append it to the `wait_list`.
     - Else if `wait_list` is not empty, we MUST add an idle interval!
       - `total_intervals += 1`
       - (If both `max_heap` and `wait_list` are empty, we are completely done, 
         so we break out early!)
   - Put all tasks from the `wait_list` back into the `max_heap`.
5. Return `total_intervals`.

COMPLEXITY:
-----------
Time:  O(N * log D) — Where N is total tasks, D is distinct tasks.
Space: O(D) — For the Hash Map, Heap, and Wait List.

EDGE CASES:
-----------
- Edge case 1: K is 0. Tasks can be done back-to-back. Time is just N.
============================================================
"""

import heapq
from typing import List
from collections import Counter

def schedule_tasks(tasks: List[str], k: int) -> int:
    """
    Returns the minimum number of intervals required to schedule all tasks.
    """
    freq_map = Counter(tasks)
    max_heap = []
    
    # 1. Put all tasks into a Max-Heap based on frequency
    for char, freq in freq_map.items():
        heapq.heappush(max_heap, (-freq, char))
        
    total_intervals = 0
    
    while max_heap:
        wait_list = []
        # We need a block of size K+1 to satisfy the cooldown period K
        n = k + 1
        
        while n > 0 and max_heap:
            total_intervals += 1
            freq, char = heapq.heappop(max_heap)
            
            # If we still have more of this task to do, put it in the wait list!
            if freq + 1 < 0:
                wait_list.append((freq + 1, char))
                
            n -= 1
            
        # Put the tasks from the wait list back into the heap for the next block
        for item in wait_list:
            heapq.heappush(max_heap, item)
            
        # If the heap is NOT empty, we MUST sit idle for the remaining 'n' intervals
        # to satisfy the K cooldown period for the most frequent tasks!
        if max_heap:
            total_intervals += n
            
    return total_intervals

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # A takes 3, B takes 2. K=2.
    # Block 1: A, B, idle
    # Block 2: A, B, idle
    # Block 3: A
    # Total = 3 + 3 + 1 = 7
    assert schedule_tasks(["A", "A", "A", "B", "B"], 2) == 7, "Test 1"
    
    # A=3, B=2, C=1, K=1
    # Block 1: A, B
    # Block 2: A, B
    # Block 3: A, C
    # Total = 2 + 2 + 2 = 6
    assert schedule_tasks(["A", "A", "A", "B", "B", "C"], 1) == 6, "Test 2"

    # 🔲 Edge cases
    assert schedule_tasks(["A", "A"], 0) == 2, "Edge 1: K=0"

    print("All tests passed!")
