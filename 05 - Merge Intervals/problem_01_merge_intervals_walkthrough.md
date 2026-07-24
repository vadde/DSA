# 🚶‍♂️ Walkthrough: Merge Intervals

## 👶 Explain Like I'm 5
Imagine you have a calendar with a bunch of meetings scheduled. Some of these meetings happen at the exact same time, or they overlap. 
For example, if you have a meeting from 1:00 to 3:00, and another meeting from 2:00 to 4:00, you are basically busy from 1:00 to 4:00 continuously!

The goal is to take a messy list of meetings and combine the overlapping ones so you just have a clean list of "blocks of time you are busy".
The easiest way to do this? **Sort the meetings by their start time.** Once they are sorted, you just look at them one by one. If the next meeting starts *before* the current one ends, they overlap, so you merge them into one big meeting!

## 🎯 Core Strategy
1. **Sort** the list of intervals based on their **START time**. This guarantees that any overlapping intervals will be right next to each other in the list.
2. Create an empty `merged` list.
3. Add the very first interval into the `merged` list.
4. Loop through the remaining intervals. For each interval:
   - Look at the LAST interval you added to the `merged` list.
   - **Check Overlap**: If the current interval's start time is $\le$ the last merged interval's end time, they overlap!
   - **Merge**: Update the last merged interval's end time to be the MAXIMUM of both end times. (e.g., merging `[1, 5]` and `[2, 3]` gives `[1, 5]`, not `[1, 3]`).
   - **No Overlap**: If they don't overlap, it's a completely separate block of time. Just add the current interval to the `merged` list.
5. Return the `merged` list.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `intervals = [[6, 7], [2, 4], [5, 9]]`
1. **Sort**: `[[2, 4], [5, 9], [6, 7]]`
2. `merged = [[2, 4]]`

| Step | Current Interval | Last Merged | Overlap? (start $\le$ end) | Action | `merged` List State |
|------|------------------|-------------|----------------------------|--------|---------------------|
| 1 | `[5, 9]` | `[2, 4]` | `5 <= 4`? **No.** | No overlap. Append it. | `[[2, 4], [5, 9]]` |
| 2 | `[6, 7]` | `[5, 9]` | `6 <= 9`? **YES!** | Merge! New end = max(9, 7) = 9. | `[[2, 4], [5, 9]]` |

Result: `[[2, 4], [5, 9]]`

## 📊 Visual Diagram
Here is a visual representation of how sorting makes merging simple:

```mermaid
flowchart TD
    subgraph Step 1 [Sort Intervals]
        W1["Unsorted: [6, 7], [2, 4], [5, 9]\nSorted: [2, 4], [5, 9], [6, 7]"]
    end
    
    subgraph Step 2 [Add First]
        W2["Merged: [2, 4]"]
    end
    
    subgraph Step 3 [Compare next: 5, 9]
        W3["Does 5 <= 4?\nNo! Add to list."]
        N3["Merged: [2, 4], [5, 9]"]
    end
    
    subgraph Step 4 [Compare next: 6, 7]
        W4["Does 6 <= 9?\nYES! Overlap!"]
        N4["Update end: max(9, 7) = 9.\nMerged: [2, 4], [5, 9]"]
    end
    
    Step 1 --> Step 2
    Step 2 --> Step 3
    Step 3 --> Step 4
    
    style W4 fill:#ffcdd2,color:#000
    style N4 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log N)$. Sorting the intervals dominates the time complexity, taking $O(N \log N)$ time. The subsequent `for` loop iterates through the array exactly once, taking $O(N)$ time.
- **Space Complexity:** $O(N)$. In the worst-case scenario where there are no overlapping intervals at all, the `merged` list will store all $N$ intervals. (Also, Python's built-in sort algorithm, Timsort, requires $O(N)$ auxiliary space).

### Edge Cases Handled Safely
- **Touching Boundaries:** If one meeting ends at 4:00 and another starts at 4:00 (e.g., `[1, 4]` and `[4, 5]`), the condition `4 <= 4` evaluates to True, successfully merging them into `[1, 5]`.
- **Swallowed Intervals:** If one large meeting completely encompasses a smaller one (e.g., `[1, 10]` and `[2, 5]`), the code updates the end time to `max(10, 5)`. It stays `10`, perfectly ignoring the smaller interval's end time.
