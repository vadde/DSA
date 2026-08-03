# 🚶‍♂️ Walkthrough: Daily Temperatures

## 👶 Explain Like I'm 5
You have a list of temperatures for the next few days.
For every single day, you want to know: "How many days do I have to wait until it is WARMER than today?"
If it never gets warmer, you just say "0 days".

This is exactly the "Next Greater Element" problem, but instead of writing down the *temperature* of the warmer day, you want to write down the *distance* (number of days) between today and the warmer day.

Because we store the **index** of the day in our Monotonic Stack, calculating the distance is super easy! It's just `warmer_day_index - today_index`.

## 🎯 Core Strategy
We use a **monotonically decreasing stack**. The stack will store the *indices* of days that are waiting for a warmer day. Because it's monotonically decreasing, the temperatures corresponding to the indices in the stack will strictly decrease from bottom to top.

1. Initialize a `result` array of the same length as `temperatures`, filled with `0` (default if no warmer day is found).
2. Initialize an empty `stack` to store indices.
3. Loop `for i, temp in enumerate(temperatures)`:
   - **Pop & Resolve**: While the stack is not empty AND `temp` is GREATER than the temperature of the day currently at the top of the stack (`temperatures[stack[-1]]`):
     - A warmer day has arrived! 
     - Pop the index from the stack: `popped_day = stack.pop()`.
     - Calculate how long that day waited: `wait_time = i - popped_day`.
     - Update the result for that day: `result[popped_day] = wait_time`.
   - **Push**: Push the current day's index into the waiting room: `stack.append(i)`.
4. Return `result`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`
Initialization: `result = [0, 0, 0, 0, 0, 0, 0, 0]`, `stack = []`.

| `i` | `temp` | Action | `stack` (Indices) | `result` |
|-----|--------|--------|-------------------|----------|
| 0 | 73 | Push 0. | `[0]` | `[0,0,0,0,0,0,0,0]` |
| 1 | 74 | 74 > temps[0] (73). Pop 0. result[0] = 1-0 = 1. Push 1. | `[1]` | `[1,0,0,0,0,0,0,0]` |
| 2 | 75 | 75 > temps[1] (74). Pop 1. result[1] = 2-1 = 1. Push 2. | `[2]` | `[1,1,0,0,0,0,0,0]` |
| 3 | 71 | 71 < temps[2] (75). Push 3. | `[2, 3]` | `[1,1,0,0,0,0,0,0]` |
| 4 | 69 | 69 < temps[3] (71). Push 4. | `[2, 3, 4]` | `[1,1,0,0,0,0,0,0]` |
| 5 | 72 | 72 > temps[4] (69). Pop 4. result[4] = 5-4 = 1.<br>72 > temps[3] (71). Pop 3. result[3] = 5-3 = 2.<br>Push 5. | `[2, 5]` | `[1,1,0,2,1,0,0,0]` |
| 6 | 76 | 76 > temps[5] (72). Pop 5. result[5] = 6-5 = 1.<br>76 > temps[2] (75). Pop 2. result[2] = 6-2 = 4.<br>Push 6. | `[6]` | `[1,1,4,2,1,1,0,0]` |
| 7 | 73 | 73 < temps[6] (76). Push 7. | `[6, 7]` | `[1,1,4,2,1,1,0,0]` |

Loop ends.
Final `result`: `[1, 1, 4, 2, 1, 1, 0, 0]`.

## 📊 Visual Diagram
Here is how Day 5 (temp 72) resolves the colder days that were waiting in the stack:

```mermaid
flowchart TD
    subgraph WaitRoom [Wait Room]
        W1["Stack before Day 5 (72) arrives:\n["Index 2 (Temp 75)"]\n["Index 3 (Temp 71)"]\n["Index 4 (Temp 69)"]"]
    end
    
    subgraph AWarmDayArrives [A Warm Day Arrives]
        A1["Day 5 (Temp 72) arrives"]
    end
    
    subgraph Resolutions
        R1["72 > 69. Pop Day 4. result[4] = 5-4 = 1"]
        R2["72 > 71. Pop Day 3. result[3] = 5-3 = 2"]
        N1["72 < 75. Stop popping. Push Day 5."]
    end

WaitRoom --> AWarmDayArrives
AWarmDayArrives --> Resolutions
    
    style A1 fill:#c8e6c9,color:#000
    style R1 fill:#fff9c4,color:#000
    style R2 fill:#fff9c4,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We loop through the array of length $N$ exactly once. Every index is pushed and popped at most once.
- **Space Complexity:** $O(N)$. In the worst-case scenario (an array sorted in descending order), nobody ever finds a warmer day, and the stack grows to hold all $N$ indices.

### Edge Cases Handled Safely
- **Decreasing Temperatures:** `[90, 80, 70, 60]`. The `while stack and temp > temperatures[stack[-1]]` loop literally never executes. The stack just fills up completely. Result remains identically `[0, 0, 0, 0]`. Perfect!
- **Single temperature:** `[30]`. Loop runs once, pushes index 0. Returns `[0]`. Perfect!
