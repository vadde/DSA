# 🚶‍♂️ Walkthrough: Permutations

## 👶 Explain Like I'm 5
This time, you aren't just deciding whether to put toys IN or OUT of a box.
You MUST put ALL the toys in the box, but you care about what **ORDER** they are in!

Let's say you have toys `[1, 2, 3]`.
You start with an empty lineup: `[]`.
You pick up Toy 1. The only place it can go is at the start: `[1]`.

You pick up Toy 2. Where can it go? It can go BEFORE Toy 1, or AFTER Toy 1!
So you take your `[1]` lineup, and make TWO copies:
- Put Toy 2 at the front: `[2, 1]`
- Put Toy 2 at the back: `[1, 2]`

Now you pick up Toy 3. You take BOTH of those lineups, and for each one, Toy 3 can go at the front, in the middle, or at the back!
- From `[2, 1]`, you make: `[3, 2, 1]`, `[2, 3, 1]`, `[2, 1, 3]`
- From `[1, 2]`, you make: `[3, 1, 2]`, `[1, 3, 2]`, `[1, 2, 3]`

You just found all 6 permutations!

## 🎯 Core Strategy
This uses the **Subsets (BFS)** pattern with a `Queue` to build the permutations slot by slot.

1. **Initialization**: Initialize a `result` array and a `queue` holding an empty list: `deque([[]])`.
2. **Outer Loop (The Elements)**: Loop through every `current_number` in `nums`.
3. **Queue Snapshot**: Take a snapshot of the queue size: `n = len(queue)`.
4. **Inner Loop (The Processing)**: Loop `n` times:
   - Pop an `old_permutation` from the front of the queue.
   - We want to insert the `current_number` into EVERY possible slot of this `old_permutation`.
   - The number of slots is exactly `len(old_permutation) + 1` (e.g., if length is 2, valid indices are 0, 1, and 2).
5. **Deepest Loop (The Insertion)**: Loop `j` from `0` to `len(old_permutation)`:
   - Create a deep copy: `new_permutation = list(old_permutation)`.
   - Insert the number at index `j`: `new_permutation.insert(j, current_number)`.
   - **Check Size**: If the `new_permutation` is full size (`== len(nums)`), append it to the `result` array.
   - **Re-queue**: Otherwise, append it to the back of the `queue` so it's ready for the next number!

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `nums = [1, 2, 3]`

### Initialization
`queue = [[]]`
`result = []`

### Processing `1`
- `n = 1`. 
- Pop `[]`. Size is 0, so slots = 1 (index 0).
- `j = 0`: Insert `1` at 0 -> `[1]`. Size is 1 (not full yet).
- Push `[1]` to queue.
- `queue = [[1]]`.

### Processing `2`
- `n = 1`.
- Pop `[1]`. Size is 1, so slots = 2 (index 0, 1).
- `j = 0`: Insert `2` at 0 -> `[2, 1]`. Push to queue.
- `j = 1`: Insert `2` at 1 -> `[1, 2]`. Push to queue.
- `queue = [[2, 1], [1, 2]]`.

### Processing `3`
- `n = 2`.
- **Pop `[2, 1]`**. Size is 2, slots = 3 (index 0, 1, 2).
  - `j = 0`: Insert `3` at 0 -> `[3, 2, 1]`. Length is 3 (Full!). Append to `result`.
  - `j = 1`: Insert `3` at 1 -> `[2, 3, 1]`. Length is 3 (Full!). Append to `result`.
  - `j = 2`: Insert `3` at 2 -> `[2, 1, 3]`. Length is 3 (Full!). Append to `result`.
- **Pop `[1, 2]`**. Size is 2, slots = 3.
  - `j = 0`: Insert `3` at 0 -> `[3, 1, 2]`. Append to `result`.
  - `j = 1`: Insert `3` at 1 -> `[1, 3, 2]`. Append to `result`.
  - `j = 2`: Insert `3` at 2 -> `[1, 2, 3]`. Append to `result`.

**Result array**: `[[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]`.
Length is exactly 6 ($3!$).

## 📊 Visual Diagram
Here is a tree visualization showing how the new number is inserted into every possible slot at each level:

```mermaid
flowchart TD
    subgraph Level 0
        Q0["[ ]"]
    end
    
    subgraph Level 1: Insert 1
        Q1["[1]"]
    end
    
    subgraph Level 2: Insert 2
        Q2_A["[2, 1]"]
        Q2_B["[1, 2]"]
    end
    
    subgraph Level 3: Insert 3 (Full!)
        Q3_A["[3, 2, 1]"]
        Q3_B["[2, 3, 1]"]
        Q3_C["[2, 1, 3]"]
        
        Q3_D["[3, 1, 2]"]
        Q3_E["[1, 3, 2]"]
        Q3_F["[1, 2, 3]"]
    end
    
    Q0 -- "idx 0" --> Q1
    
    Q1 -- "idx 0" --> Q2_A
    Q1 -- "idx 1" --> Q2_B
    
    Q2_A -- "idx 0" --> Q3_A
    Q2_A -- "idx 1" --> Q3_B
    Q2_A -- "idx 2" --> Q3_C
    
    Q2_B -- "idx 0" --> Q3_D
    Q2_B -- "idx 1" --> Q3_E
    Q2_B -- "idx 2" --> Q3_F
    
    style Q0 fill:#e3f2fd,color:#000
    style Q1 fill:#bbdefb,color:#000
    style Q2_A fill:#90caf9,color:#000
    style Q2_B fill:#90caf9,color:#000
    style Q3_A fill:#a5d6a7,color:#000
    style Q3_F fill:#a5d6a7,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \times N!)$. There are exactly $N!$ permutations for an array of size $N$. For each permutation, we created a deep copy (`list()`) which takes $O(N)$ time. 
- **Space Complexity:** $O(N \times N!)$. We need to store all $N!$ permutations in the `result` list, and at its peak, the `queue` will also hold $N!$ elements.

### Edge Cases Handled Safely
- **Single Element (`[1]`):** Returns `[[1]]` immediately on the first pass.
- **Empty Array (`[]`):** The initial `if not nums:` check catches this and returns `[[]]`. If we let the loop run, it wouldn't process anything, but returning early is cleaner.
