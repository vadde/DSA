# 🚶‍♂️ Walkthrough: Non-overlapping Intervals

## 👶 Explain Like I'm 5
Imagine you have a bunch of meetings scheduled, but you realize that a lot of them overlap! You are exhausted, so you want to cancel the FEWEST number of meetings possible so that none of the remaining meetings overlap.

Here is the trick: to cancel the fewest meetings, we want to KEEP the *most* meetings.
How do we fit the most meetings into a day? We always choose the meeting that **FINISHES the earliest!** By finishing early, it leaves the rest of the day wide open for more meetings.

So, we sort the meetings by their **END** time. 
We attend the first meeting. If the next meeting overlaps with the one we are attending, we just skip it (cancel it). If it doesn't overlap, we attend it!

## 🎯 Core Strategy
This uses a **Greedy Strategy** by sorting intervals by their **END time**, exactly like the "Minimum Arrows to Burst Balloons" problem.

1. **Sort** the intervals by their `end` time. This is the crucial greedy step: always favor the interval that ends first to leave room for future intervals.
2. Initialize `removed_count = 0`.
3. Set `current_end = intervals[0].end`. This tracks the end time of the meeting we have chosen to attend.
4. Loop through the remaining intervals. For each `interval`:
   - **Conflict**: If the next interval starts BEFORE our current meeting ends (`interval.start < current_end`):
     - We have an overlap! Because we sorted by end time, the `current_end` meeting we already chose finishes earlier (or at the same time) as this conflicting one. Keeping the earlier-ending one is mathematically always the better choice.
     - So, we KEEP the current one and CANCEL the new conflicting one: `removed_count += 1`.
   - **No Conflict**: If the next interval starts exactly when or after our current meeting ends:
     - We can safely attend this new meeting!
     - Update `current_end = interval.end`.
5. Return `removed_count`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]`
1. **Sort by End Time**: `[[1, 2], [2, 3], [1, 3], [3, 4]]`
2. Initialize: `removed_count = 0`, `current_end = 2` (from the first meeting `[1, 2]`).

| Step | Current Meeting | `current_end` | Conflict? (`start < current_end`) | Action | `removed_count` |
|------|-----------------|---------------|-----------------------------------|--------|-----------------|
| 1 | `[2, 3]` | `2` | `2 < 2`? No. | Attend! Update `current_end` to `3`. | `0` |
| 2 | `[1, 3]` | `3` | `1 < 3`? **YES!** | Conflict! Cancel this meeting. | `1` |
| 3 | `[3, 4]` | `3` | `3 < 3`? No. | Attend! Update `current_end` to `4`. | `1` |

Result: `1` meeting removed.

## 📊 Visual Diagram
Here is why sorting by **End Time** guarantees the optimal choice:

```mermaid
flowchart TD
    subgraph Bad Choice [Sorted by Start Time]
        W1["Meetings: [1, 10], [2, 3], [4, 5]"]
        N1["If you attend [1, 10], you miss TWO meetings!\nRemoved count = 2."]
    end
    
    subgraph Good Choice [Sorted by End Time]
        W2["Meetings: [2, 3], [4, 5], [1, 10]"]
        N2["You attend [2, 3], then [4, 5].\nYou only miss [1, 10].\nRemoved count = 1!"]
    end
    
    Bad Choice -.->|Suboptimal| W1
    Good Choice -.->|Optimal| W2
    
    style Bad Choice fill:#ffcdd2,color:#000
    style Good Choice fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log N)$. Sorting the intervals by their end times takes $O(N \log N)$. The subsequent greedy pass loops through the array exactly once, taking $O(N)$ time. The total complexity is dominated by the sorting step.
- **Space Complexity:** $O(N)$ or $O(\log N)$ depending on the underlying sorting algorithm used by the language (Python's Timsort uses $O(N)$ space).

### Edge Cases Handled Safely
- **Touching boundaries:** e.g., `[1, 2]` and `[2, 3]`. The condition checks if `2 < 2`. This evaluates to False. The algorithm correctly recognizes that these do NOT overlap and attends both.
- **Empty List:** Fast-path `if not intervals: return 0` handles an empty schedule instantly.
