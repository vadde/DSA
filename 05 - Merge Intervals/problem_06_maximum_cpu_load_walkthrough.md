# 🚶‍♂️ Walkthrough: Maximum CPU Load

## 👶 Explain Like I'm 5
Imagine your computer is a worker who can carry multiple backpacks at once. 
Throughout the day, people hand the worker a backpack (Start Time), and later take it back (End Time). Each backpack has a different weight (CPU Load). 
You want to know the **MAXIMUM total weight** the worker was carrying at any single moment in the day.

Just like figuring out how many meeting rooms we need, we can keep track of which backpacks the worker is currently holding using a magic list (a Min-Heap).
When a new backpack is handed to the worker, we first check if any old backpacks were taken away (their End Time has passed). If so, we subtract their weight. 
Then we add the new backpack's weight and keep track of the maximum total weight!

## 🎯 Core Strategy
This is almost identical to the **Minimum Meeting Rooms** problem, but instead of counting the *number* of rooms (size of the heap), we track the *sum* of a specific value (CPU load).

1. **Sort** the jobs by their start time to process them chronologically.
2. Initialize `max_load = 0` and `current_load = 0`.
3. Create an empty Min-Heap. The heap will store tuples of `(end_time, cpu_load)`. By putting `end_time` first in the tuple, Python's heap automatically keeps the job that ends *soonest* at the very top!
4. Loop through the sorted jobs. For each `job`:
   - **Remove Finished Jobs**: While the heap is not empty AND the new job starts AFTER (or exactly when) the job at the top of the heap ends:
     - Pop the job from the heap.
     - Subtract its `cpu_load` from `current_load`. (The backpack was returned!)
   - **Add New Job**: Push the new job's `(end_time, cpu_load)` onto the heap.
   - Add the new job's `cpu_load` to `current_load`. (Handed a new backpack!)
   - **Record Peak**: Update `max_load = max(max_load, current_load)`.
5. Return `max_load`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `jobs = [{start:1, end:4, load:3}, {start:2, end:5, load:4}, {start:7, end:9, load:6}]`
1. **Sort**: Already sorted by start time.
2. Initialize: `min_heap = []`, `current_load = 0`, `max_load = 0`.

| Step | Current Job | Top of Heap (Earliest End) | Job Ended? (Start $\ge$ Top End) | Action | `current_load` | `max_load` | Heap State (End, Load) |
|------|-------------|----------------------------|----------------------------------|--------|----------------|------------|------------------------|
| 1 | `[1, 4, 3]` | `None` (Empty) | No | Push `(4, 3)`. | `0 + 3 = 3` | `max(0, 3) = 3` | `[(4, 3)]` |
| 2 | `[2, 5, 4]` | `(4, 3)` | `2 >= 4`? No. | Push `(5, 4)`. | `3 + 4 = 7` | `max(3, 7) = 7` | `[(4, 3), (5, 4)]` |
| 3 | `[7, 9, 6]` | `(4, 3)` | `7 >= 4`? **YES!** | Pop `(4, 3)`. Subtract `3`. <br> *Check again*: `7 >= 5`? **YES!** <br> Pop `(5, 4)`. Subtract `4`. <br> Push `(9, 6)`. | `7 - 3 - 4 + 6 = 6`| `max(7, 6) = 7` | `[(9, 6)]` |

Result: `max_load = 7`.

## 📊 Visual Diagram
Here is how the Min-Heap tracks active jobs and their loads:

```mermaid
flowchart TD
    subgraph Step 2 [Time: 2. Heap has (4,3)]
        W1["Current Job: [2, 5, load 4]"]
        N1["Does 2 >= 4? No.\nKeep the old job!"]
        H1["Current Load: 3 + 4 = 7\nMax Load = 7"]
    end
    
    subgraph Step 3 [Time: 7. Heap has (4,3), (5,4)]
        W2["Current Job: [7, 9, load 6]"]
        N2["7 >= 4? YES! Pop it. Load - 3 = 4.\n7 >= 5? YES! Pop it. Load - 4 = 0."]
        H2["Push new job.\nCurrent Load = 0 + 6 = 6\nMax Load remains 7!"]
    end
    
    Step 2 --> Step 3
    
    style H1 fill:#ffcdd2,color:#000
    style N2 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log N)$. Sorting the jobs takes $O(N \log N)$. Iterating through the $N$ jobs and performing heap pushes/pops takes $O(\log N)$ per operation.
- **Space Complexity:** $O(N)$. In the worst-case scenario where all jobs overlap simultaneously, the min-heap will store $N$ tuples.

### Edge Cases Handled Safely
- **Exact boundary touching:** e.g., `[1, 2, load: 5]` and `[2, 3, load: 5]`. The condition `job.start >= min_heap[0][0]` translates to `2 >= 2`, which is True. The first job is popped, its load is subtracted, and *then* the new job is added. The `current_load` briefly drops to `0` and goes back up to `5`. It never incorrectly spikes to `10`.
