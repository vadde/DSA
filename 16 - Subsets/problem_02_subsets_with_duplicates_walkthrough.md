# 🚶‍♂️ Walkthrough: Subsets With Duplicates

## 👶 Explain Like I'm 5
You have an empty box `[]`.
This time, your toys are an Apple, a Bear, and ANOTHER Bear! `[A, B, B]`.

If you do the exact same thing as before, you will eventually create two boxes that both just have `[A, B]` inside them, because you added the first Bear to an `[A]` box, and later you added the second Bear to an `[A]` box.
We don't want duplicate boxes!

To fix this, we sort the toys so the two Bears are right next to each other.
When we pick up the FIRST Bear, we add it to ALL of our existing boxes.
But when we pick up the SECOND Bear, we say: *"Wait! I just saw a Bear. If I add this new Bear to ALL my old boxes, I'll make duplicates. I should ONLY add this new Bear to the brand new boxes I JUST created in the previous step!"*

## 🎯 Core Strategy
This is a small variation of the **Subsets (BFS)** pattern. We add sorting and a dynamic start index.

1. **Sort**: First, sort the array `nums.sort()`. This guarantees that duplicate numbers sit right next to each other.
2. **Initialization**: Start with `subsets = [[]]`. Initialize `start_idx = 0` and `end_idx = 0`.
3. **Outer Loop**: Loop through every number `nums[i]`.
   - By default, reset `start_idx = 0`. This means we will append the number to ALL existing subsets.
   - **Duplicate Check**: If `i > 0` and `nums[i] == nums[i - 1]`, we found a duplicate! Instead of `0`, we set `start_idx = end_idx`. (This restricts us to only appending to the subsets created in the immediately preceding loop).
   - Set `end_idx = len(subsets)`. (This captures the total number of subsets before we start adding new ones).
4. **Inner Loop**: Loop `j` from `start_idx` to `end_idx - 1`:
   - Copy `subsets[j]`, append `nums[i]`, and push it to `subsets`.
5. Return `subsets`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `nums = [1, 3, 3]`

### Initialization
`subsets = [[]]`
`start_idx = 0`, `end_idx = 0`

### Loop `i = 0` (`num = 1`)
- Not a duplicate. `start_idx = 0`.
- `end_idx = len(subsets) = 1`.
- Inner loop from 0 to 0:
  - Copy `subsets[0]` (`[]`), append `1` -> `[1]`.
- `subsets` becomes `[[], [1]]`.

### Loop `i = 1` (`num = 3`)
- Not a duplicate (`3 != 1`). `start_idx = 0`.
- `end_idx = len(subsets) = 2`.
- Inner loop from 0 to 1:
  - Copy `[]`, append `3` -> `[3]`.
  - Copy `[1]`, append `3` -> `[1, 3]`.
- `subsets` becomes `[[], [1], [3], [1, 3]]`.

### Loop `i = 2` (`num = 3` - DUPLICATE!)
- **Duplicate found!** (`nums[2] == nums[1]`). 
- `start_idx = end_idx` (which is `2` from the previous step).
- `end_idx = len(subsets) = 4`.
- Inner loop from 2 to 3 (We ONLY look at `[3]` and `[1, 3]`):
  - Look at `subsets[2]` (`[3]`). Copy, append `3` -> `[3, 3]`.
  - Look at `subsets[3]` (`[1, 3]`). Copy, append `3` -> `[1, 3, 3]`.
- Notice we did NOT look at `[]` and `[1]`! If we had, we would have made another `[3]` and `[1, 3]` (Duplicates).
- `subsets` becomes `[[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]`.

Return `subsets`.

## 📊 Visual Diagram
Here is how the duplicate restriction acts as a filter, preventing the branches that create identical sets:

```mermaid
flowchart TD
    subgraph Start
        S0["[ ]"]
    end
    
    subgraph Add 1
        S1["[ ]\n[1]"]
    end
    
    subgraph Add First 3
        S2["[ ]\n[1]"]
        N2["[3]\n[1, 3]"]
    end
    
    subgraph Add Second 3
        S3["[ ]\n[1]\n[3]\n[1, 3]"]
        N3["[3, 3]\n[1, 3, 3]"]
    end
    
    Start -- "start=0" --> Add 1
    Add 1 -- "start=0" --> S2
    Add 1 -- "Append to all" --> N2
    
    S2 -- "start=2" --> S3
    N2 -- "start=2" --> S3
    
    N2 -- "Append ONLY to \nnewly created items" --> N3
    S2 -. "BLOCKED\n(Would create [3] and [1,3])" .-> X((X))
    
    style Start fill:#e3f2fd,color:#000
    style Add 1 fill:#bbdefb,color:#000
    style N2 fill:#90caf9,color:#000
    style N3 fill:#64b5f6,color:#000
    style X fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log N)$ for sorting, plus $O(N \times 2^N)$ for generating the subsets. Generating subsets strictly dominates, so the final time complexity is $O(N \times 2^N)$.
- **Space Complexity:** $O(N \times 2^N)$ to store all valid subsets in the result array.

### Edge Cases Handled Safely
- **All Duplicates (`[2, 2, 2]`):** First `2` makes `[[], [2]]`. Second `2` only appends to `[2]` making `[2, 2]`. Third `2` only appends to `[2, 2]` making `[2, 2, 2]`. The logic cleanly creates a staircase without ever duplicating.
- **Sorting Requirement:** If the array is `[3, 1, 3]`, our duplicate check `nums[i] == nums[i-1]` would completely fail because the `3`s are separated. The `nums.sort()` step at the very beginning is absolutely mandatory for this algorithm to function.
