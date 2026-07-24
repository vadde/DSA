# 🚶‍♂️ Walkthrough: Subsets

## 👶 Explain Like I'm 5
You have an empty box `[]`.
You are given a list of toys: `[1, 2, 3]`.

You walk up to Toy 1. You make a copy of your empty box, and put Toy 1 inside.
Now you have two boxes: `[]` and `[1]`.

You walk up to Toy 2. You make copies of BOTH of your boxes, and put Toy 2 inside the copies.
Now you have four boxes: `[]`, `[1]`, `[2]`, `[1, 2]`.

You walk up to Toy 3. You make copies of ALL FOUR boxes, and put Toy 3 inside.
Now you have eight boxes! You have found every possible combination of toys.

This is exactly how we write the code! We loop through the toys, and for every toy, we double our list of boxes.

## 🎯 Core Strategy
This uses the **Subsets (BFS)** pattern. Instead of using recursive backtracking, we iteratively build the subsets level by level (like Breadth-First Search).

1. **Initialization**: Start with a list containing a single empty subset: `subsets = [[]]`.
2. **Outer Loop (The Elements)**: Loop through every number `num` in the input array `nums`.
3. **Snapshot**: Before adding new subsets, take a snapshot of how many subsets we currently have: `n = len(subsets)`.
   - *CRITICAL WARNING*: Do not just iterate `for subset in subsets:` while appending to it, or you will create an infinite loop! You must freeze the length `n` first.
4. **Inner Loop (The Copying)**: Loop `i` from `0` to `n - 1`:
   - Create a deep copy of the subset at index `i`: `set_copy = list(subsets[i])`.
   - Add the current `num` to the copy: `set_copy.append(num)`.
   - Add the new copy back to our main list: `subsets.append(set_copy)`.
5. Return the final list of `subsets`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `nums = [1, 2, 3]`

### Initialization
`subsets = [[]]`

### Loop 1: `num = 1`
- Snapshot: `n = 1` (We only have `[]`).
- Inner loop `i = 0`:
  - Look at `subsets[0]` which is `[]`.
  - Copy it: `set_copy = []`.
  - Append `num`: `set_copy = [1]`.
  - Add to main list: `subsets` becomes `[[], [1]]`.

### Loop 2: `num = 2`
- Snapshot: `n = 2` (We have `[]` and `[1]`).
- Inner loop `i = 0`:
  - Look at `subsets[0]` which is `[]`.
  - Copy it and append `2`: `[2]`.
  - Add to main list.
- Inner loop `i = 1`:
  - Look at `subsets[1]` which is `[1]`.
  - Copy it and append `2`: `[1, 2]`.
  - Add to main list.
- `subsets` becomes `[[], [1], [2], [1, 2]]`.

### Loop 3: `num = 3`
- Snapshot: `n = 4` (We have 4 subsets).
- Inner loop `i = 0 to 3`:
  - Copy `[]` -> `[3]`
  - Copy `[1]` -> `[1, 3]`
  - Copy `[2]` -> `[2, 3]`
  - Copy `[1, 2]` -> `[1, 2, 3]`
- Add them all to main list.
- `subsets` becomes `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`.

Return `subsets`!

## 📊 Visual Diagram
Here is how the list of subsets literally doubles in size with each new number added:

```mermaid
flowchart TD
    subgraph Start
        S0["[ ]"]
    end
    
    subgraph Add 1
        S1["[ ]\n[1]"]
    end
    
    subgraph Add 2
        S2["[ ]\n[1]\n[2]\n[1, 2]"]
    end
    
    subgraph Add 3
        S3["[ ]\n[1]\n[2]\n[1, 2]\n[3]\n[1, 3]\n[2, 3]\n[1, 2, 3]"]
    end
    
    Start -- "Copy & Append 1" --> Add 1
    Add 1 -- "Copy & Append 2" --> Add 2
    Add 2 -- "Copy & Append 3" --> Add 3
    
    style Start fill:#e3f2fd,color:#000
    style Add 1 fill:#bbdefb,color:#000
    style Add 2 fill:#90caf9,color:#000
    style Add 3 fill:#64b5f6,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \times 2^N)$. For $N$ numbers, there are exactly $2^N$ possible subsets. In each step, we copy arrays that can be up to length $N$. So copying takes $O(N)$, and we do it $2^N$ times.
- **Space Complexity:** $O(N \times 2^N)$ to store all $2^N$ subsets in the result array, where each subset has an average length of $N/2$.

### Edge Cases Handled Safely
- **Empty Input:** `nums = []`. The outer loop never runs. The algorithm immediately returns `[[]]`, which is the correct mathematical subset of an empty set.
- **Infinite Loop Trap:** By defining `n = len(subsets)` *before* the inner loop, we prevent the `range(n)` from infinitely chasing the growing list. If you used `for subset in subsets:`, it would run forever because you are actively pushing new items into `subsets` while iterating over it!
