# 🚶‍♂️ Walkthrough: Maximum Size Subarray Sum Equals K

## 👶 Explain Like I'm 5
Like the previous problem, we want to find subarrays that sum to `K`. But instead of COUNTING how many there are, we want the LENGTH of the LONGEST one.

To get the longest subarray, we want to subtract the *earliest possible* prefix sum that gives us `K`.

## 🎯 Core Strategy
**Prefix Sum + Hash Map (storing INDICES)**.

1. Maintain `current_sum`.
2. Hash map `prefix_indices` stores the **first index** where we saw a particular prefix sum.
3. Initialize with `{0: -1}` so a prefix starting at index 0 works correctly (length will be `i - (-1) = i + 1`).
4. At each step, if `current_sum - K` is in the map:
   - Calculate length: `i - prefix_indices[current_sum - K]`.
   - Update `max_len = max(max_len, length)`.
5. **Crucial rule**: Only add `current_sum` to the map if it's NOT already there. We want to preserve the earliest occurrence to maximize future lengths.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `nums = [1, -1, 5, -2, 3]`, `K = 3`

Init: `map = {0: -1}`, `max_len = 0`

| i | num | current_sum | needed (sum-3) | In map? | length | Updated map |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | -2 | No | - | `{0:-1, 1:0}` |
| 1 | -1 | 0 | -3 | No | - | `{0:-1, 1:0}` (0 already in map, skip) |
| 2 | 5 | 5 | 2 | No | - | `{0:-1, 1:0, 5:2}` |
| 3 | -2 | 3 | 0 | Yes (idx -1) | 3 - (-1) = **4** | `{0:-1, 1:0, 5:2, 3:3}` |
| 4 | 3 | 6 | 3 | Yes (idx 3) | 4 - 3 = 1 | `{0:-1, 1:0, 5:2, 3:3, 6:4}` |

Max length = 4 ✅

## 📊 Visual Diagram

```mermaid
flowchart TD
    A["Init: map = {0: -1}, max_len = 0"]
    B["For i, num in enumerate(nums)"]
    C["current_sum += num\nneeded = current_sum - K"]
    D{"needed in map?"}
    E["length = i - map[needed]\nmax_len = max(max_len, length)"]
    F{"current_sum in map?"}
    G["map[current_sum] = i"]
    H["Next iteration"]
    
    A --> B --> C --> D
    D -->|YES| E --> F
    D -->|NO| F
    F -->|NO (Store earliest)| G --> H
    F -->|YES| H
    
    style E fill:#c8e6c9,color:#000
    style G fill:#fff9c4,color:#000
```

## 🛑 Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$
