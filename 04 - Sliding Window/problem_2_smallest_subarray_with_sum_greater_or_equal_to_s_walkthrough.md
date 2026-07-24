# 🚶‍♂️ Walkthrough: Smallest Subarray with Sum ≥ S

## 👶 Explain Like I'm 5
Imagine a row of treasure chests, each with some gold coins. You need to collect at least $S$ coins to buy a spaceship. You want to carry as *few chests as possible*, but you can only pick up chests that are sitting right next to each other in a line.

You start stretching a rope around chests from left to right until you have enough coins. Once you hit the goal, you try to **tighten** the rope from the left side (dropping the first chest) to see if you STILL have enough coins. You keep dropping chests from the left until you don't have enough anymore, recording your "tightest" rope length along the way! 
Then you stretch the rope to the right again to get more chests.

## 🎯 Core Strategy
This introduces the **Dynamic-Size Sliding Window**.
1. Initialize variables: `window_start = 0`, `window_sum = 0`, `min_length = inf`.
2. Iterate `window_end` through the array, expanding the window to the right by adding the new element to `window_sum`.
3. Whenever `window_sum >= S`, we have a valid window! We enter a `while` loop to **shrink** it.
4. While the condition `window_sum >= S` is true:
   - Record the current length (`window_end - window_start + 1`) if it's smaller than `min_length`.
   - Shrink the window from the left by subtracting `arr[window_start]` from `window_sum` and incrementing `window_start`.
5. Repeat until the end of the array is reached.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `arr = [2, 1, 5, 2, 8]`, `S = 7`
Initialization: `window_start = 0`, `window_sum = 0`, `min_length = inf`

| Step | `window_end` | `arr[window_end]` | `window_sum` | `sum >= 7`? | Actions (Update min_length, Shrink) |
|------|--------------|-------------------|--------------|-------------|-------------------------------------|
| 1 | `0` | `2` | `2` | No | Expand. |
| 2 | `1` | `1` | `3` | No | Expand. |
| 3 | `2` | `5` | `8` | **Yes!** | `min_len` = min(inf, 3) = **3**. <br> Subtract 2 (start 0). Sum=6. `start = 1`. |
| 4 | - | - | `6` | No | Break shrink loop. Expand again. |
| 5 | `3` | `2` | `8` | **Yes!** | `min_len` = min(3, 3) = **3**. <br> Subtract 1 (start 1). Sum=7. `start = 2`. |
| 6 | - | - | `7` | **Yes!** | `min_len` = min(3, 2) = **2** `[5, 2]`. <br> Subtract 5 (start 2). Sum=2. `start = 3`. |
| 7 | - | - | `2` | No | Break shrink loop. Expand again. |
| 8 | `4` | `8` | `10` | **Yes!** | `min_len` = min(2, 2) = **2**. <br> Subtract 2 (start 3). Sum=8. `start = 4`. |
| 9 | - | - | `8` | **Yes!** | `min_len` = min(2, 1) = **1** `[8]`. <br> Subtract 8 (start 4). Sum=0. `start = 5`. |

Result: The minimum length is `1` (from the subarray `[8]`).

## 📊 Visual Diagram
Here is a visualization of the window expanding and shrinking:

```mermaid
flowchart TD
    subgraph Expand to 8 [end = 2]
        W1["[ 2, 1, 5 ], 2, 8"]
        note1["Sum: 8. Valid! Len: 3"]
    end
    
    subgraph Shrink 1 [start = 1]
        W2["2, [ 1, 5 ], 2, 8"]
        note2["Sum: 6. Invalid."]
    end
    
    subgraph Expand to 8 again [end = 3]
        W3["2, [ 1, 5, 2 ], 8"]
        note3["Sum: 8. Valid! Len: 3"]
    end
    
    subgraph Shrink 2 [start = 2]
        W4["2, 1, [ 5, 2 ], 8"]
        note4["Sum: 7. Valid! Len: 2"]
    end
    
    Expand to 8 --> Shrink 1
    Shrink 1 --> Expand to 8 again
    Expand to 8 again --> Shrink 2
    
    style W1 fill:#32CD32,color:#000
    style W2 fill:#ff6b6b,color:#000
    style W3 fill:#32CD32,color:#000
    style W4 fill:#FFD700,color:#000,stroke:#f00,stroke-width:2px
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. Even though there is a `while` loop inside the `for` loop, the time complexity is strictly linear. Why? Because the `window_start` pointer only ever moves *forward*. Each element is added to the window at most once and subtracted at most once. So, the inner loop executes at most $N$ times across the *entire program*, making the overall operations proportional to $2N$, which is $O(N)$.
- **Space Complexity:** $O(1)$. The sliding window strictly uses scalar variables, ignoring the size of the input array.

### Edge Cases Handled Safely
- **No subarray sum reaches S:** If the sum of the entire array is less than `S`, `min_length` will remain `math.inf`. At the end, we check this and safely return `0`.
- **A single element is >= S:** If an element is naturally larger than `S` (like `8 > 7`), the window will shrink all the way down to a length of 1 around that element, perfectly returning 1.
