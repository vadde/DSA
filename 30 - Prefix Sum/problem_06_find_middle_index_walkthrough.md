# 🚶‍♂️ Walkthrough: Find the Middle Index in Array

## 👶 Explain Like I'm 5
You have a row of numbers. Find an index where the sum of everything to its LEFT is exactly equal to the sum of everything to its RIGHT. The number at the index itself doesn't count towards either side.

If you know the `total_sum` of the whole array, and you keep track of the `left_sum` as you walk through, you can easily calculate the `right_sum` without looking ahead!

## 🎯 Core Strategy
**Total Sum - Left Sum**.

1. First pass: compute the `total_sum` of the entire array.
2. Maintain a running `left_sum`, initialized to 0.
3. Second pass: iterate through the array. For each number at index `i`:
   - Calculate `right_sum = total_sum - left_sum - nums[i]`.
   - If `left_sum == right_sum`, return `i`!
   - Otherwise, add `nums[i]` to `left_sum` and move to the next index.
4. If the loop finishes without finding a match, return `-1`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `nums = [2, 3, -1, 8, 4]`

1. `total_sum = 2 + 3 - 1 + 8 + 4 = 16`
2. `left_sum = 0`

| i | nums[i] | left_sum | right_sum (16 - left - num) | Equal? | New left_sum |
|---|---|---|---|---|---|
| 0 | 2 | 0 | 16 - 0 - 2 = 14 | 0 == 14? No | 0 + 2 = 2 |
| 1 | 3 | 2 | 16 - 2 - 3 = 11 | 2 == 11? No | 2 + 3 = 5 |
| 2 | -1| 5 | 16 - 5 - (-1) = 12| 5 == 12? No | 5 + (-1) = 4|
| 3 | 8 | 4 | 16 - 4 - 8 = 4 | 4 == 4? **YES** | - |

Return `3` ✅

## 📊 Visual Diagram

```mermaid
flowchart LR
    A["Calculate total_sum"] --> B["left_sum = 0"]
    B --> C["Loop array"]
    
    subgraphIteration
C --> D["right_sum = total - left - num"]
        D --> E{"left == right?"}
        E -->|YES| F["Return current index"]
        E -->|NO| G["left_sum += num"]
    end
G --> C

styleFfill:#c8e6c9,color:#000
    style A fill:#bbdefb,color:#000
```

## 🛑 Complexity
- **Time:** $O(N)$ — one pass to sum, one pass to check.
- **Space:** $O(1)$ — just a few variables.
