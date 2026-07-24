# 🚶‍♂️ Walkthrough: Employee Free Time

## 👶 Explain Like I'm 5
Imagine you have a team of 3 people. Each person gives you a list of the times they are busy working today. 
You want to schedule a team-building pizza party, which means you need to find all the times when **EVERYONE is free!**

Since everyone is free when *no one* is working, this is the exact opposite of finding when people are busy. 
If we take EVERY single working shift from ALL employees, dump them into a big pile, and sort them from morning to night, we just need to look for the "GAPS" between the shifts!
If the latest time anyone has worked so far is 3:00, and the next person doesn't start working until 4:00, then from 3:00 to 4:00, the whole team is free!

## 🎯 Core Strategy
This is a clever inversion of the standard **Merge Intervals** pattern. Instead of merging overlapping intervals, we are looking for the *empty space* between merged intervals.

1. **Flatten the Schedule**: Take the lists of intervals from all employees and combine them into one massive, flat list of intervals.
2. **Sort** all the intervals in this massive list by their start time.
3. Keep track of the `max_end` time we've seen so far. Initialize it to the first interval's end time.
4. Iterate through the sorted intervals starting from the second one (index `1`):
   - **Find the Gap**: If the current interval's start time is STRICTLY GREATER than `max_end`, we found a gap where no one is working! Add the interval `[max_end, current.start]` to our `free_time` list.
   - **Update `max_end`**: Regardless of whether we found a gap or not, we might have overlapping or extending shifts. Update `max_end = max(max_end, current.end)`.
5. Return the `free_time` list.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `schedule = [[[1, 3], [9, 12]], [[2, 4]], [[6, 8]]]`
1. **Flatten**: `[[1, 3], [9, 12], [2, 4], [6, 8]]`
2. **Sort**: `[[1, 3], [2, 4], [6, 8], [9, 12]]`
3. Initialize: `max_end = 3`, `free_time = []`

| Step | Current Shift | `max_end` (Before) | Gap Found? (`start > max_end`) | Action | `max_end` (After) | `free_time` State |
|------|---------------|--------------------|--------------------------------|--------|-------------------|-------------------|
| 1 | `[2, 4]` | `3` | `2 > 3`? No. | Just update max_end. | `max(3, 4) = 4` | `[]` |
| 2 | `[6, 8]` | `4` | `6 > 4`? **YES!** | Found gap! Add `[4, 6]`. | `max(4, 8) = 8` | `[[4, 6]]` |
| 3 | `[9, 12]`| `8` | `9 > 8`? **YES!** | Found gap! Add `[8, 9]`. | `max(8, 12) = 12` | `[[4, 6], [8, 9]]`|

Result: `[[4, 6], [8, 9]]`

## 📊 Visual Diagram
Here is how tracking `max_end` perfectly identifies gaps across multiple people:

```mermaid
flowchart TD
    subgraph Step 1 [Shift: 1 to 3]
        W1["Max End is 3."]
    end
    
    subgraph Step 2 [Shift: 2 to 4]
        W2["Starts at 2. Ends at 4."]
        N2["2 is not past 3. No gap.\nMax End extends to 4!"]
    end
    
    subgraph Step 3 [Shift: 6 to 8]
        W3["Starts at 6."]
        N3["6 IS past 4!\nGAP FOUND: [4, 6]!"]
        H3["Max End extends to 8."]
    end
    
    Step 1 --> Step 2
    Step 2 --> Step 3
    
    style N3 fill:#32CD32,color:#000
    style W2 fill:#e1f5fe,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log N)$. $N$ is the total number of intervals across all employees. Flattening takes $O(N)$, sorting takes $O(N \log N)$, and the final iteration takes $O(N)$. The bottleneck is the sorting step.
- **Space Complexity:** $O(N)$. We create a new flat list containing all $N$ intervals, and the result array can also contain up to $N$ free time gaps.

### Edge Cases Handled Safely
- **Overlapping Chain:** e.g., `[[1, 3], [2, 4], [3, 5]]`. `max_end` will smoothly update from `3` to `4` to `5` without ever triggering the gap condition, correctly recognizing that the team is continuously busy from `1` to `5`.
- **Identical Hours:** If everyone works `[9, 5]`, sorting puts them together, and `max_end` stays `5` while no gaps are detected. Works perfectly.
