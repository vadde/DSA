# 🚶‍♂️ Walkthrough: Number of Longest Increasing Subsequence

## 👶 Explain Like I'm 5
Finding the Longest Increasing Subsequence (LIS) is like finding the longest staircase you can climb using numbers.
But this time, we need to know HOW MANY different longest staircases exist!
If the numbers are `[1, 3, 5, 4, 7]`, you can climb `1 -> 3 -> 5 -> 7` (length 4) OR `1 -> 3 -> 4 -> 7` (length 4). Since both are the longest, the answer is 2!
To solve this, we keep two notebooks. One notebook (`length`) tracks the longest staircase ending at each number. The other notebook (`count`) tracks HOW MANY paths got us there. 
If we find a *longer* path to a number, we throw away the old count and start over. If we find *another* path of the exact same length, we add its count to our total!

## 🎯 Core Strategy
**Dynamic Programming (Double State)**.

*Note: While solvable in $O(N \log N)$ with a BIT, the $O(N^2)$ DP solution is the standard expected approach for interview constraints ($N \le 2000$).*

1. **State Tracking**: 
   - `length[i]`: The length of the LIS ending at index `i`. Initialize all to 1.
   - `count[i]`: The number of LIS paths of length `length[i]` ending at index `i`. Initialize all to 1.
2. **Double Loop**:
   - For every element `i` (from 1 to `N-1`), look at every previous element `j` (from 0 to `i-1`).
   - If `nums[j] < nums[i]` (we can extend the increasing sequence):
     - Check if extending from `j` gives us a **strictly longer** sequence: `length[j] + 1 > length[i]`. If so, update `length[i] = length[j] + 1` and overwrite `count[i] = count[j]`.
     - Check if extending from `j` gives us a sequence of the **same length** we've already found: `length[j] + 1 == length[i]`. If so, we found another valid path! `count[i] += count[j]`.
3. **Final Answer**: Find the global maximum length in the `length` array. Sum up `count[i]` for all indices `i` where `length[i]` equals the global maximum length.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `nums = [1, 3, 5, 4, 7]`
Init: `length = [1, 1, 1, 1, 1]`, `count = [1, 1, 1, 1, 1]`

- **i = 1 (num = 3)**:
  - `j = 0 (num = 1)`: `1 < 3`. `len[0]+1 (2) > len[1] (1)`. Update `len[1] = 2`, `cnt[1] = cnt[0] = 1`.
- **i = 2 (num = 5)**:
  - `j = 0 (num = 1)`: `len[2] = 2`, `cnt[2] = 1`.
  - `j = 1 (num = 3)`: `3 < 5`. `len[1]+1 (3) > len[2] (2)`. Update `len[2] = 3`, `cnt[2] = cnt[1] = 1`.
- **i = 3 (num = 4)**:
  - `j = 0 (num = 1)`: `len[3] = 2`, `cnt[3] = 1`.
  - `j = 1 (num = 3)`: `3 < 4`. `len[1]+1 (3) > len[3] (2)`. Update `len[3] = 3`, `cnt[3] = 1`.
  - `j = 2 (num = 5)`: `5 > 4` (skip).
- **i = 4 (num = 7)**:
  - `j = 0 (num = 1)`: `len[4] = 2, cnt[4] = 1`.
  - `j = 1 (num = 3)`: `len[4] = 3, cnt[4] = 1`.
  - `j = 2 (num = 5)`: `5 < 7`. `len[2]+1 (4) > len[4] (3)`. Update `len[4] = 4`, `cnt[4] = cnt[2] = 1`.
  - `j = 3 (num = 4)`: `4 < 7`. `len[3]+1 (4) == len[4] (4)`. Another path found! `cnt[4] += cnt[3]` -> `cnt[4] = 1 + 1 = 2`.

**Max Length** = 4. 
Indices with length 4 is index 4. `cnt[4]` = 2.
Result: **2**. ✅

## 📊 Visual Diagram

```mermaid
flowchart TD
    A["Iterate i from 1 to N-1"] --> B["Iterate j from 0 to i-1"]
    B --> C{"nums[j] < nums[i]?"}
    
    C -->|YES| D{"len[j] + 1 > len[i]?"}
    D -->|YES (New Max)| E["len[i] = len[j] + 1\ncnt[i] = cnt[j]"]
    D -->|NO| F{"len[j] + 1 == len[i]?"}
    F -->|YES (Another Path)| G["cnt[i] += cnt[j]"]
    F -->|NO| B
    E --> B
    G --> B
    
    C -->|NO| B
    
    style E fill:#c8e6c9,color:#000
    style G fill:#fff9c4,color:#000
```

## 🛑 Complexity
- **Time:** $O(N^2)$ due to the nested loop evaluating all pairs.
- **Space:** $O(N)$ for the `length` and `count` DP arrays.
