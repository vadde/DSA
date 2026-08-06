# 🚶‍♂️ Walkthrough: Data Stream as Disjoint Intervals

## 👶 Explain Like I'm 5
Imagine you are building a jigsaw puzzle, but someone is handing you pieces one by one. Each piece has a number. 
If someone hands you piece 1, you put it down. If someone hands you piece 3, you put it down. Right now you have two separate blocks: `[1, 1]` and `[3, 3]`.
If someone then hands you piece 2, suddenly all three pieces connect! You can merge them all together to say you have a single solid block from `[1, 3]`.

Because pieces are handed to you one by one, you need a fast way to slot a piece into the correct place in your sorted list, and then just check if it connects to its immediate left or right neighbors.

## 🎯 Core Strategy
Since the integers arrive as a stream, we can't afford to re-sort the entire list every single time using $O(N \log N)$. Instead, we use **Binary Search** and **Dynamic Insertion**.

1. Maintain a `intervals` list that is always sorted and merged.
2. When a new `value` arrives, use Binary Search to find its exact insertion position.
   - If the value is already completely inside one of the existing intervals, it's a duplicate! Ignore it entirely.
3. If it's not a duplicate, insert a tiny single-point interval `[value, value]` at the found index.
4. **Merge Left**: Check the newly inserted interval against its immediate LEFT neighbor.
   - If `left_neighbor.end + 1 == new_interval.start`, they connect perfectly!
   - Expand the left neighbor's end, and delete the `new_interval`. The left neighbor is now the "active" merged interval.
5. **Merge Right**: Check the active interval against its immediate RIGHT neighbor.
   - If `active_interval.end + 1 == right_neighbor.start`, they connect perfectly!
   - Expand the active interval's end, and delete the right neighbor.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Stream**: `add(1), add(3), add(7), add(2)`

| Action | Stream | Binary Search Index | Insertion & Merge Logic | Resulting `intervals` |
|--------|--------|---------------------|-------------------------|-----------------------|
| `add(1)` | `1` | `0` | Insert `[1, 1]`. No neighbors to merge. | `[[1, 1]]` |
| `add(3)` | `3` | `1` | Insert `[3, 3]`. Left `1+1 != 3`. No merge. | `[[1, 1], [3, 3]]` |
| `add(7)` | `7` | `2` | Insert `[7, 7]`. Left `3+1 != 7`. No merge. | `[[1, 1], [3, 3], [7, 7]]`|
| `add(2)` | `2` | `1` | Insert `[2, 2]` at idx 1. <br> **Merge Left**: `1+1 == 2`. Merge into `[1, 2]`. <br> **Merge Right**: `2+1 == 3`. Merge into `[1, 3]`. | `[[1, 3], [7, 7]]` |

Result after all additions: `[[1, 3], [7, 7]]`

## 📊 Visual Diagram
Here is a visualization of the double-merge when inserting `2`:

```mermaid
flowchart TD
    subgraph State1 [State 1: Before Insert]
        W1["Intervals: [1, 1], [3, 3], [7, 7]"]
    end
    
    subgraph State2 [State 2: Insert [2, 2]]
        W2["Intervals: [1, 1], [2, 2], [3, 3], [7, 7]"]
    end
    
    subgraph State3 [State 3: Merge Left]
        W3["Left neighbor ends at 1.\n1 + 1 == 2. Merge!"]
        N3["Intervals: [1, 2], [3, 3], [7, 7]"]
    end
    
    subgraph State4 [State 4: Merge Right]
        W4["Right neighbor starts at 3.\n2 + 1 == 3. Merge!"]
        N4["Intervals: [1, 3], [7, 7]"]
    end

State1 --> State2
State2 --> State3
    State3 --> State4

styleW3fill:#fff9c4,color:#000
    style W4 fill:#fff9c4,color:#000
    style N4 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** 
  - `addNum(value)`: $O(N)$. Binary search takes $O(\log N)$, but inserting an element into the middle of a Python list takes $O(N)$ because elements must be shifted. Merging takes $O(1)$.
  - `getIntervals()`: $O(1)$. We just return the already-maintained list.
- **Space Complexity:** $O(N)$. We store up to $N$ disjoint intervals in the worst case where no numbers connect.

### Edge Cases Handled Safely
- **Duplicate numbers:** Handled gracefully by the Binary Search phase. `if interval.start <= value <= interval.end: return`. This guarantees $O(\log N)$ time for duplicates, instantly rejecting them.
- **Cascading Merges:** This algorithm relies on the fact that inserting ONE number can at most merge ONE interval on the left and ONE interval on the right. It cannot trigger a massive chain reaction, so the double `if` check is perfectly sufficient without needing a `while` loop.
