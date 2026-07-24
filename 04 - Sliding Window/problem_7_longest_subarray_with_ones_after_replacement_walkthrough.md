# 🚶‍♂️ Walkthrough: Longest Subarray with Ones after Replacement

## 👶 Explain Like I'm 5
Imagine a long row of light switches. Some are turned **ON (1)** and some are **OFF (0)**.
You want to find the longest stretch of lights that are all ON. 
You have a magic wand that can flip at most $K$ switches from OFF to ON. 

To find the absolute longest stretch, you hold up a sliding frame over the switches. As long as your frame contains $K$ or fewer OFF switches, it's a valid stretch (because you could use your magic wand on all the OFF switches inside the frame). 
If you accidentally pull too many OFF switches into your frame, you must slide the left side of your frame forward to drop some of those OFF switches until you're back down to a number you can handle.

## 🎯 Core Strategy
This is a straightforward application of the **Dynamic-Size Sliding Window**.
1. Initialize `window_start = 0`, `max_length = 0`, and a simple integer counter `zeros_count = 0`.
2. Iterate `window_end` across the array to expand the window.
3. If the element entering the window is `0`, increment `zeros_count`.
4. Check if the window is valid: `while zeros_count > k`.
5. If invalid, shrink the window from the left by moving `window_start`. If the element leaving the window is `0`, decrement `zeros_count`.
6. Once the window is valid again, calculate its size (`window_end - window_start + 1`) and update `max_length`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `arr = [0, 1, 1, 0, 0, 0, 1, 1, 0]`, `k = 2`
Initialization: `start = 0`, `max_len = 0`, `zeros = 0`

| Step | `end` val | `zeros` count | > 2? | Action (Update max_len, Shrink) |
|------|-----------|---------------|------|---------------------------------|
| 1 | `0` (val 0) | `1` | No | `max_len` = max(0, 1) = **1**. (`[0]`) |
| 2 | `1` (val 1) | `1` | No | `max_len` = max(1, 2) = **2**. (`[0, 1]`) |
| 3 | `2` (val 1) | `1` | No | `max_len` = max(2, 3) = **3**. (`[0, 1, 1]`) |
| 4 | `3` (val 0) | `2` | No | `max_len` = max(3, 4) = **4**. (`[0, 1, 1, 0]`) |
| 5 | `4` (val 0) | `3` | **Yes** | *SHRINK*: Drop `arr[0]` (which is `0`). `zeros` drops to `2`. `start = 1`. Valid! <br> `max_len` = max(4, 4) = **4**. (`[1, 1, 0, 0]`) |
| 6 | `5` (val 0) | `3` | **Yes** | *SHRINK*: Drop `arr[1]` (1), `arr[2]` (1), `arr[3]` (0). `zeros` drops to `2`. `start = 4`. Valid! <br> `max_len` = max(4, 2) = **4**. (`[0, 0]`) |
| 7 | `6` (val 1) | `2` | No | `max_len` = max(4, 3) = **4**. (`[0, 0, 1]`) |
| 8 | `7` (val 1) | `2` | No | `max_len` = max(4, 4) = **4**. (`[0, 0, 1, 1]`) |
| 9 | `8` (val 0) | `3` | **Yes** | *SHRINK*: Drop `arr[4]` (0). `zeros` drops to `2`. `start = 5`. Valid! <br> `max_len` = max(4, 4) = **4**. (`[0, 1, 1, 0]`) |

Result: The max length is `4`.

## 📊 Visual Diagram
Here is a visualization of the window expanding and shrinking based on the zero count:

```mermaid
flowchart TD
    subgraph Iteration 4 [end = 3]
        W1["[ 0, 1, 1, 0 ], 0, 0, 1, 1..."]
        N1["Zeros: 2. Valid! Max Len = 4"]
    end
    
    subgraph Iteration 5 Expand [end = 4]
        W2["[ 0, 1, 1, 0, 0 ], 0, 1, 1..."]
        N2["Zeros: 3. Invalid! (3 > 2)"]
    end
    
    subgraph Iteration 5 Shrink [start = 1]
        W3["0, [ 1, 1, 0, 0 ], 0, 1, 1..."]
        N3["Drop arr[0] (a zero!).\nZeros: 2. Valid!"]
    end
    
    Iteration 4 --> Iteration 5 Expand
    Iteration 5 Expand --> Iteration 5 Shrink
    
    style W1 fill:#32CD32,color:#000
    style W2 fill:#ff6b6b,color:#000
    style W3 fill:#FFD700,color:#000,stroke:#f00,stroke-width:2px
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We iterate through the array exactly once. The `window_start` pointer only moves forward. The total number of operations is strictly proportional to the number of elements in the array.
- **Space Complexity:** $O(1)$. We only store simple integer variables (`window_start`, `max_length`, `zeros_count`), requiring strictly constant space regardless of the array's size.

### Edge Cases Handled Safely
- **`k = 0`:** The algorithm naturally defaults to finding the longest contiguous subarray of existing `1`s. The moment a `0` enters the window, `zeros_count` becomes `1 > 0`, triggering the shrink loop until the `0` is removed.
- **`k` is larger than total zeros in array:** The `while` loop never executes, and the window smoothly encompasses the entire array, returning the full array length.
- **Empty Array:** The initial `for` loop is skipped, returning `max_length` as `0`.
