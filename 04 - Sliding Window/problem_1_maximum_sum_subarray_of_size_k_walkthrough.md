# 🚶‍♂️ Walkthrough: Maximum Sum Subarray of Size K

## 👶 Explain Like I'm 5
Imagine a train of numbered blocks. You hold up a picture frame that is exactly wide enough to fit exactly $K$ blocks at a time.
You want to find out which section of $K$ blocks adds up to the biggest total number!

You *could* pick up the frame, put it on the first $K$ blocks, add them up, then pick up the frame and put it on the next $K$ blocks and add them up again... but that's a lot of repeating yourself!

Instead, what if you just **slide** the frame 1 block to the right? 
When you slide it, one block falls out of the left side of the frame, and one new block enters the right side. So, to find the new total, you just take your old total, **subtract** the block you lost, and **add** the new block you gained. 
This makes finding the biggest sum super fast!

## 🎯 Core Strategy
This is the most fundamental introduction to the **Sliding Window (Fixed Size)** pattern.
1. Initialize variables for `window_start = 0`, the current `window_sum = 0`, and the `max_sum` (starting at $-\infty$).
2. Expand the window by iterating `window_end` from 0 to the end of the array, continuously adding elements to `window_sum`.
3. Check the size of the window. Once `window_end >= k - 1`, the window has reached the required size $K$.
4. At this point, record the `window_sum` by taking the `max()` against `max_sum`.
5. Now, shrink the window from the left: subtract the element at `window_start` from `window_sum`, and increment `window_start`.
6. As the loop continues, the window perfectly slides across the array.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `arr = [2, 1, 5, 1, 3, 2]`, `k = 3`
Initialization: `window_start = 0`, `window_sum = 0`, `max_sum = -inf`

| Step | `window_end` | `arr[window_end]` | `window_sum` | `end >= k-1` (2)? | Actions (Update max, subtract start, move start) |
|------|--------------|-------------------|--------------|-------------------|--------------------------------------------------|
| 1 | `0` | `2` | `2` | No | Window is growing. `[2]` |
| 2 | `1` | `1` | `3` | No | Window is growing. `[2, 1]` |
| 3 | `2` | `5` | `8` | **Yes!** | `max_sum` = max(-inf, 8) = **8**. <br> Subtract `arr[0]` (2). Sum = 6. `start = 1`. |
| 4 | `3` | `1` | `7` | **Yes!** | `max_sum` = max(8, 7) = **8**. <br> Subtract `arr[1]` (1). Sum = 6. `start = 2`. |
| 5 | `4` | `3` | `9` | **Yes!** | `max_sum` = max(8, 9) = **9**. <br> Subtract `arr[2]` (5). Sum = 4. `start = 3`. |
| 6 | `5` | `2` | `6` | **Yes!** | `max_sum` = max(9, 6) = **9**. <br> Subtract `arr[3]` (1). Sum = 5. `start = 4`. |

Result: The maximum sum is `9` (from the subarray `[5, 1, 3]`).

## 📊 Visual Diagram
Here is a visualization of the Sliding Window mechanism:

```mermaid
flowchart TD
    subgraph Iteration3 [Iteration 3: window_end = 2]
        W1["[ 2, 1, 5 ], 1, 3, 2"]
        M1["max_sum = 8"]
    end
    
    subgraph Iteration4 [Iteration 4: window_end = 3]
        Slide1["Subtract 2, Add 1"]
        W2["2, [ 1, 5, 1 ], 3, 2"]
        M2["max_sum = 8"]
    end
    
    subgraph Iteration5 [Iteration 5: window_end = 4]
        Slide2["Subtract 1, Add 3"]
        W3["2, 1, [ 5, 1, 3 ], 2"]
        M3["max_sum = 9"]
    end

Iteration3 --> Slide1 --> Iteration 4
    Iteration4 --> Slide2 --> Iteration 5
    
    style W1 fill:#32CD32,color:#000
    style W2 fill:#32CD32,color:#000
    style W3 fill:#FFD700,color:#000,stroke:#f00,stroke-width:2px
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. Every element is added to the window sum exactly once and subtracted exactly once. The time it takes is strictly proportional to the number of elements in the array.
- **Space Complexity:** $O(1)$. The sliding window only requires three scalar variables (`window_sum`, `window_start`, `max_sum`).

### Edge Cases Handled Safely
- **Array size is smaller than K:** If `len(arr) < k`, no window of size K can ever be formed. The algorithm handles this by returning `-math.inf` immediately.
- **All elements are negative:** `[-2, -1, -5, -1]`. Because `max_sum` is initialized to `-math.inf` instead of `0`, it correctly records and returns the *least negative* sum (`-6` from `[-1, -5]`).
