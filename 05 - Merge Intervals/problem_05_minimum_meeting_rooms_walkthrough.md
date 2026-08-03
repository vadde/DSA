# 🚶‍♂️ Walkthrough: Minimum Meeting Rooms

## 👶 Explain Like I'm 5
You are the manager of a very busy conference center. You have a messy list of meetings happening today, and you want to know the MAXIMUM number of rooms you will need to open at any single time.

If you sort the meetings by their start time, you can process them chronologically—just like a real day. 
Every time a new meeting is about to start, you ask: "Hey, did any previous meeting just finish?" 
If a meeting just finished, great! You can clean it and re-use that exact same room!

To quickly know when the "soonest" meeting is finishing, you can use a magic priority list (a Min-Heap). This list magically always keeps the smallest number (the earliest end time) at the very top.
Whenever a new meeting starts, you just look at the top of the magic list. If the new meeting starts *after* the time on top of the list, a room just freed up! You pop that old meeting off the list, and put your new meeting's end time in. 

The most rooms you *ever* need is simply the maximum size your magic list reaches during the day.

## 🎯 Core Strategy
This is an advanced Merge Intervals problem that requires a **Min-Heap**.
1. **Sort** the intervals by start time so we can process them in chronological order.
2. Create an empty Min-Heap. The heap will store the **end times** of all currently active meetings.
3. Initialize `min_rooms = 0`.
4. Loop through the sorted intervals. For each `interval`:
   - **Free up rooms**: While the heap is not empty AND the current meeting starts on or after the meeting at the top of the heap ends (`interval.start >= heap[0]`), it means a room just became available! `heappop()` from the heap.
   - **Occupy a room**: `heappush()` the current meeting's `end` time onto the heap. This meeting is now active.
   - **Record Peak Usage**: The size of the heap `len(heap)` represents the exact number of meetings happening simultaneously *right now*. Update `min_rooms = max(min_rooms, len(heap))`.
5. Return `min_rooms`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `intervals = [[1, 4], [2, 3], [3, 6]]`
1. **Sort**: They are already sorted by start time.
2. Initialize: `min_heap = []`, `max_rooms = 0`.

| Step | Current Meeting | Top of Heap (Earliest End) | Free Room? (Start $\ge$ Top) | Action | Heap State | Peak Rooms |
|------|-----------------|----------------------------|------------------------------|--------|------------|------------|
| 1 | `[1, 4]` | `None` (Empty) | No | Push `4`. | `[4]` | `max(0, 1) = 1` |
| 2 | `[2, 3]` | `4` | `2 >= 4`? No. | Push `3`. | `[3, 4]` | `max(1, 2) = 2` |
| 3 | `[3, 6]` | `3` | `3 >= 3`? **YES!** | Pop `3`! Room is free! <br> Push `6`. | `[4, 6]` | `max(2, 2) = 2` |

Result: `2` rooms required.

## 📊 Visual Diagram
Here is how the Min-Heap tracks active rooms:

```mermaid
flowchart TD
    subgraph Step2 [Step 2: Time: 2. Heap has [4]]
        W1["Current Meeting: [2, 3]"]
        N1["Does 2 >= 4? No.\nMust open a NEW room!"]
        H1["Heap becomes [3, 4]\nPeak = 2"]
    end
    
    subgraph Step3 [Step 3: Time: 3. Heap has [3, 4]]
        W2["Current Meeting: [3, 6]"]
        N2["Does 3 >= 3? YES!"]
        H2["Meeting ending at 3 is over.\nPop 3!\nRe-use the room.\nPush 6!"]
    end
    
    subgraph State [End State]
        W3["Heap becomes [4, 6]\nPeak remains 2"]
    end

Step2 --> Step3
Step3 --> State
    
    style N1 fill:#ffcdd2,color:#000
    style N2 fill:#32CD32,color:#000
    style H2 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log N)$. Sorting the intervals takes $O(N \log N)$. Iterating through the $N$ intervals and performing heap operations (push and pop) takes $O(\log N)$ per operation. The total heap operations take $O(N \log N)$. Therefore, the overall time complexity is strictly $O(N \log N)$.
- **Space Complexity:** $O(N)$. In the worst-case scenario where all meetings overlap simultaneously, the min-heap will store $N$ end times.

### Edge Cases Handled Safely
- **Exact boundary touching:** e.g., `[1, 2]` and `[2, 3]`. The condition `interval.start >= min_heap[0]` translates to `2 >= 2`, which is True. The room is correctly marked as free and immediately re-used, keeping the required room count at `1`.
- **Many meetings ending at the same time:** The `while min_heap and interval.start >= min_heap[0]:` loop ensures that if a new meeting starts at 5, and three previous meetings ended at 3, 4, and 5, *all three* rooms are popped off the heap and made available before the new meeting occupies one.
