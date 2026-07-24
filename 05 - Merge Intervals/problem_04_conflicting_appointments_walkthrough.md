# 🚶‍♂️ Walkthrough: Conflicting Appointments

## 👶 Explain Like I'm 5
Imagine you have a list of meetings you want to attend today. Since you haven't invented a cloning machine yet, you can only be in one place at a time. 
If Meeting A is from 1:00 to 3:00, and Meeting B is from 2:00 to 4:00, you have a problem! You can't attend both.
However, if Meeting A ends at *exactly* 3:00 and Meeting B starts at *exactly* 3:00, that's completely fine! You can just run out of the first room and straight into the second room.

To figure out if you can attend ALL the meetings, you just need to sort them by their start time. Then, you look at them one by one. If any meeting starts *before* the previous meeting finishes, you have a conflict!

## 🎯 Core Strategy
This is the simplest variation of the **Merge Intervals** pattern. Instead of merging overlapping intervals, we simply return `False` as soon as we detect an overlap.

1. **Sort** the list of intervals based on their start time. This ensures that we only need to compare adjacent intervals.
2. Iterate through the sorted intervals starting from the second one (index `1`).
3. **Check for Overlap:** Compare the current interval's `start` time with the previous interval's `end` time.
   - If `current.start < previous.end`, an overlap exists! Return `False` immediately.
   - Note that we use strictly less than (`<`). If `current.start == previous.end`, they just touch boundaries, which is allowed.
4. If the loop finishes without finding any overlaps, return `True`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `intervals = [[1, 4], [2, 5], [7, 9]]`
1. **Sort**: They are already sorted by start time.

| Step `i` | Current Interval `[i]` | Previous Interval `[i-1]` | Conflict? (current `start` < previous `end`) | Action |
|----------|------------------------|---------------------------|----------------------------------------------|--------|
| `1` | `[2, 5]` | `[1, 4]` | `2 < 4`? **YES!** | Conflict found! Return `False`. |

Result: `False`.

**Example 2 Input**: `intervals = [[6, 7], [2, 4], [8, 12]]`
1. **Sort**: `[[2, 4], [6, 7], [8, 12]]`

| Step `i` | Current Interval `[i]` | Previous Interval `[i-1]` | Conflict? (current `start` < previous `end`) | Action |
|----------|------------------------|---------------------------|----------------------------------------------|--------|
| `1` | `[6, 7]` | `[2, 4]` | `6 < 4`? No. | Continue. |
| `2` | `[8, 12]` | `[6, 7]` | `8 < 7`? No. | Loop finishes. |

Result: `True`.

## 📊 Visual Diagram
Here is how sorting makes identifying conflicts effortless:

```mermaid
flowchart TD
    subgraph Step 1 [Sort by Start Time]
        W1["[4, 5], [2, 3], [3, 6]\nbecomes\n[2, 3], [3, 6], [4, 5]"]
    end
    
    subgraph Step 2 [Compare Adjacent Pairs]
        W2["Pair 1: [2, 3] and [3, 6]"]
        N2["3 < 3? No. Boundary touch is allowed!"]
        
        W3["Pair 2: [3, 6] and [4, 5]"]
        N3["4 < 6? YES! Overlap detected!"]
    end
    
    subgraph Step 3 [Result]
        W4["Return False instantly!"]
    end
    
    Step 1 --> W2
    W2 --> N2
    N2 --> W3
    W3 --> N3
    N3 --> W4
    
    style N2 fill:#c8e6c9,color:#000
    style N3 fill:#ffcdd2,color:#000
    style W4 fill:#ffcdd2,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log N)$. Sorting the array of intervals is the most computationally expensive operation. The `for` loop that follows only iterates through the array once, taking $O(N)$ time.
- **Space Complexity:** $O(N)$ or $O(\log N)$ depending on the underlying sorting algorithm used by the language (Python's Timsort uses $O(N)$ space).

### Edge Cases Handled Safely
- **List with 0 or 1 appointment:** The function immediately returns `True` since it's impossible to have a conflict.
- **Appointments touch exactly:** e.g., `[1, 2]` and `[2, 3]`. Because the condition checks if `2 < 2`, which is False, the code correctly allows back-to-back appointments.
