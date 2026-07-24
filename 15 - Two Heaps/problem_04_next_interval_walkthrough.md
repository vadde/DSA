# 🚶‍♂️ Walkthrough: Next Interval

## 👶 Explain Like I'm 5
You have a bunch of meetings (intervals) with a Start time and an End time.
For EVERY meeting, you want to find the **"Next Meeting"**. 
The "Next Meeting" is the meeting that starts right after your current meeting ends. If there are multiple meetings that start after yours ends, you want the one that starts the SOONEST!

If we just compare every meeting to every other meeting, it takes way too long. So we use Two Sorting Hats (Heaps)!
1. A **Max Heap** that sorts all meetings by their END time.
2. A **Max Heap** that sorts all meetings by their START time.

We pull out the meeting that Ends the ABSOLUTE LATEST. 
Then we look at the Start Hat. We pull out ALL meetings that start after this latest end time.
The very last one we pull out before the start time becomes too early is our "Next Meeting"! We record its index.

But wait! What about the meeting that Ends the SECOND latest?
Since its end time is earlier, the "Next Meeting" we just found for the latest meeting might also be the "Next Meeting" for this one too! So we just throw that ONE meeting back into the Start Hat so it can be reused.

## 🎯 Core Strategy
This uses the **Two Heaps** pattern to efficiently query intervals without comparing every pair.

1. **State Tracking**:
   - `max_end_heap`: Stores `(-end_time, index)`.
   - `max_start_heap`: Stores `(-start_time, index)`.
2. **Initialization**:
   - Push all intervals into both heaps. Initialize a `result` array to `-1`.
3. **Execution Loop**:
   - Loop $N$ times. Each iteration pops the `top_end` time from `max_end_heap`.
   - Pop from `max_start_heap` as long as `start_time >= top_end`. 
   - Since it's a Max Heap, we are popping the *latest* starting meetings first. The very last one we pop (before the condition fails) will be the *earliest* valid starting meeting! We record its index.
   - **Crucial Re-push**: If we found a valid "Next Meeting", we push its `(start_time, index)` BACK into the `max_start_heap`. Why? Because the next `end_time` we evaluate will be $\le$ the current one. Therefore, this start time will *still* be valid for the next end time, and it could be its best match too! The ones we popped before it were larger, so they are guaranteed to be less optimal, and we leave them in the trash.
4. Return `result`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `intervals = [[3,4], [2,3], [1,2]]`
(Indices: 0, 1, 2)

### Initialization
- `max_end_heap`: `[(-4, 0), (-3, 1), (-2, 2)]`
- `max_start_heap`: `[(-3, 0), (-2, 1), (-1, 2)]`

### Loop 1
- Pop `max_end_heap`: `top_end = 4` (Index 0).
- Check `max_start_heap`: Top `start_time` is `3`.
- Is `3 >= 4`? NO. Loop never runs.
- `result[0] = -1`.

### Loop 2
- Pop `max_end_heap`: `top_end = 3` (Index 1).
- Check `max_start_heap`: Top is `3`.
- Is `3 >= 3`? YES!
  - Pop it! `best_start_idx = 0` (The `[3,4]` interval).
- Check next `max_start_heap`: Top is `2`.
- Is `2 >= 3`? NO. Loop stops.
- We found a match! `result[1] = 0`.
- **Re-push**: Push the matched start time back: `(-3, 0)` goes back into `max_start_heap`.

### Loop 3
- Pop `max_end_heap`: `top_end = 2` (Index 2).
- Check `max_start_heap`: Top is `3` (The one we just pushed back!).
- Is `3 >= 2`? YES!
  - Pop it! `best_start_idx = 0`.
- Check next `max_start_heap`: Top is `2`.
- Is `2 >= 2`? YES!
  - Pop it! `best_start_idx = 1` (The `[2,3]` interval).
- Check next `max_start_heap`: Top is `1`.
- Is `1 >= 2`? NO. Loop stops.
- Match found! `result[2] = 1`.

Return `result`: `[-1, 0, 1]`. Correct!

## 📊 Visual Diagram
Here is a visualization of the Heap state during Loop 3, showing why pushing the best match back is so important:

```mermaid
flowchart TD
    subgraph Iteration 2 End State
        END["max_end_heap\nNext: End=2"]
        START["max_start_heap\nTop: Start=3"]
        note1["Start=3 was pushed back.\nWe need it for End=2!"]
    end
    
    subgraph Iteration 3 Pop Loop
        POP1["Pop Start=3\n(3 >= 2)"] --> POP2["Pop Start=2\n(2 >= 2)"]
        POP2 --> CHECK["Check Start=1\n(1 < 2) STOP"]
    end
    
    subgraph Iteration 3 Result
        RES["best_start_idx = 1"]
        note2["The last popped value (Start=2)\nis the tightest fit!"]
    end
    
    Iteration 2 End State --> Iteration 3 Pop Loop
    Iteration 3 Pop Loop --> Iteration 3 Result
    
    style END fill:#bbdefb,color:#000
    style START fill:#c8e6c9,color:#000
    style POP1 fill:#ffcc80,color:#000
    style POP2 fill:#ffcc80,color:#000
    style RES fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log N)$. Populating the heaps takes $O(N \log N)$. In the evaluation loop, every interval is popped from `max_start_heap` at most once, and re-pushed at most once. Therefore, heap operations remain bounded by $O(N \log N)$.
- **Space Complexity:** $O(N)$ to store the two heaps and the `result` array.

### Edge Cases Handled Safely
- **Single Interval:** Loop runs once, `max_start_heap` condition fails, returns `[-1]`.
- **Interval is its own Next:** The problem allows an interval to be its own "Next Meeting" if its End Time equals its Start Time (e.g., `[2, 2]`). This logic naturally supports it because both start and end times will be exactly the same, allowing the `>=` condition to hit!
