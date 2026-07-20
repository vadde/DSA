"""
============================================================
Problem: Maximum CPU Load
Pattern: Merge Intervals (Min-Heap)
Difficulty: Hard
Link: https://www.educative.io/courses/grokking-the-coding-interview/xVlyyv3rR93
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine your computer is a worker who can carry multiple backpacks at once.
Throughout the day, people hand the worker a backpack (Start Time), and later take 
it back (End Time). Each backpack has a different weight (CPU Load).
You want to know the MAXIMUM total weight the worker was carrying at any single 
moment in the day.
Just like figuring out how many meeting rooms we need, we can keep track of which 
backpacks the worker is currently holding using a Min-Heap.
When a new backpack is handed to the worker, we first check if any old backpacks 
were taken away (their End Time has passed). We subtract their weight. 
Then we add the new backpack's weight and keep track of the maximum total weight!

APPROACH:
---------
1. Sort the jobs by their start time.
2. Initialize `max_load = 0` and `current_load = 0`.
3. Create an empty Min-Heap. The heap will store tuples of `(end_time, cpu_load)`. 
   By putting `end_time` first, the heap naturally keeps the job that ends soonest at the top!
4. Loop through the sorted jobs:
   - While the heap is not empty AND the new job starts AFTER (or exactly when) 
     the job at the top of the heap ends:
     - Pop the job from the heap.
     - Subtract its `cpu_load` from `current_load`.
   - Push the new job's `(end, cpu_load)` onto the heap.
   - Add the new job's `cpu_load` to `current_load`.
   - Update `max_load = max(max_load, current_load)`.
5. Return `max_load`.

COMPLEXITY:
-----------
Time:  O(N log N) — Sorting takes O(N log N). Heap operations take O(log N) for N jobs.
Space: O(N) — In the worst case (all jobs overlap), the heap stores N jobs.

EDGE CASES:
-----------
- Edge case 1: Jobs touch exactly at boundaries. Properly handled by `>=`.
- Edge case 2: Empty list of jobs. Returns 0.
============================================================
"""

import heapq

class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

def find_max_cpu_load(jobs: list[Job]) -> int:
    """
    Finds the maximum CPU load at any time if all jobs run on the same machine.
    """
    if not jobs:
        return 0

    # 1. Sort the jobs by start time
    jobs.sort(key=lambda x: x.start)

    max_load: int = 0
    current_load: int = 0
    min_heap: list[tuple[int, int]] = [] # Stores (end_time, cpu_load)

    for job in jobs:
        # Remove all jobs that have ended
        while min_heap and job.start >= min_heap[0][0]:
            ended_job_end_time, ended_job_load = heapq.heappop(min_heap)
            current_load -= ended_job_load

        # Add the current job to the heap and to the current load
        heapq.heappush(min_heap, (job.end, job.cpu_load))
        current_load += job.cpu_load

        # Record the maximum load we've seen so far
        max_load = max(max_load, current_load)

    return max_load

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    jobs1 = [Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]
    assert find_max_cpu_load(jobs1) == 7, "Test 1 failed: Overlap [1,4] and [2,5] -> 3+4=7"

    jobs2 = [Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)]
    assert find_max_cpu_load(jobs2) == 15, "Test 2 failed: No overlap, max is 15"
    
    # 🔲 Edge cases
    jobs3 = [Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]
    assert find_max_cpu_load(jobs3) == 8, "Edge 1: Multiple overlapping (2+1+5=8)"
    
    jobs4 = [Job(1, 2, 5), Job(2, 3, 5)]
    assert find_max_cpu_load(jobs4) == 5, "Edge 2: Exact boundary touching (does not sum)"
    
    assert find_max_cpu_load([]) == 0, "Edge 3: Empty list"

    print("All tests passed!")
