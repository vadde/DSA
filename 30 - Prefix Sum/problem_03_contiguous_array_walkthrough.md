# 🚶‍♂️ Walkthrough: Contiguous Array (Equal 0s and 1s)

## 👶 Explain Like I'm 5
You have an array of `0`s and `1`s. Find the longest contiguous subarray with an EQUAL number of `0`s and `1`s.

If we turn every `0` into a `-1`, then an array with an equal number of `-1`s and `1`s will sum up to exactly `0`. 
Now this problem is exactly identical to "Maximum Size Subarray Sum Equals K", where `K = 0`.

## 🎯 Core Strategy
**Transformation + Prefix Sum Map**.

1. Loop through the array. Treat every `0` as `-1`.
2. Keep a `current_sum`. 
3. Use a hash map to store the first time we see each prefix sum (`{0: -1}`).
4. If we see the same prefix sum again, the elements between the first occurrence and the current index must sum to 0!
5. Update max length.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `[0, 1, 0]`

Treat as: `[-1, 1, -1]`. Target `K = 0`.

Init: `map = {0: -1}`, `max_len = 0`

| i | num | treated | current_sum | In map? | length (i - map[sum]) | Map updates |
|---|---|---|---|---|---|---|
| 0 | 0 | -1 | -1 | No | - | `{0:-1, -1:0}` |
| 1 | 1 | +1 | 0 | Yes (-1) | 1 - (-1) = **2** | no update (keep earliest) |
| 2 | 0 | -1 | -1 | Yes (0) | 2 - 0 = **2** | no update |

Max length = 2 ✅

## 📊 Visual Diagram

```mermaid
flowchart LR
    A["Transform: 0 -> -1"] --> B["Problem becomes:\nMax Subarray Sum = 0"]
    
    subgraph Execution
        C["current_sum += 1 or -1"]
        D{"current_sum seen?"}
        E["Update max_len\nusing earliest index"]
        F["Store current_sum: i\n(if not seen)"]
        
        C --> D
        D -->|YES| E
        D -->|NO| F
    end
    B --> Execution
    
    style A fill:#bbdefb,color:#000
    style E fill:#c8e6c9,color:#000
```

## 🛑 Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$
