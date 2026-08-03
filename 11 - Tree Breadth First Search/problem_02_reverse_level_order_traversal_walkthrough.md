# 🚶‍♂️ Walkthrough: Reverse Level Order Traversal

## 👶 Explain Like I'm 5
Remember taking pictures of every generation in the family tree?
What if the photo album company wants the pictures in the book backwards?
They want the youngest kids on Page 1, the parents on Page 2, the grandparents on Page 3, and the Great-Grandparent on the very last page!

We STILL take the pictures in the exact same order (top to bottom).
But when we put a picture into the photo album, instead of putting it at the END of the album, we shove it into the very FRONT of the album!
By always putting the newest picture at the front, the very first picture we took (the top of the tree) ends up at the very back of the album.

## 🎯 Core Strategy
This is almost identical to the standard **Tree Breadth First Search (BFS)** pattern. The only modification is how we store the results. Instead of appending levels to the end of an array, we prepend them to the beginning. To do this efficiently, we use a `deque` (Double-Ended Queue) for our results array as well as for our BFS queue.

1. **Initialization**: If the `root` is None, return `[]`. Initialize a `queue` using `collections.deque` with the `root`.
2. **Result Deque**: Initialize `result = deque()`. We use a deque for the result because inserting at the front of a standard Python list takes $O(N)$ time, but inserting at the front of a deque (`appendleft`) takes $O(1)$ time.
3. **Level Loop**: Loop `while queue is not empty`:
   - `level_size = len(queue)`
   - `current_level = []`
   - **Node Loop**: Loop exactly `level_size` times:
     - Pop `node` from queue.
     - Add `node.value` to `current_level`.
     - Append children to the queue (Left then Right).
   - **Prepend**: INSTEAD of `result.append`, do `result.appendleft(current_level)`. This pushes the current level to the *front* of the result list.
4. **Finalize**: Return `list(result)`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input Tree**:
```text
      12
     /  \
    7    1
   / \  / \
  9  2 10  5
```
Initialization: `queue = [12]`, `result = deque([])`.

### Level 1 (Top Level)
- Nodes processed: `12`.
- `current_level` = `[12]`.
- `result.appendleft([12])`.
- `result` is now `[[12]]`.
- Queue is now `[7, 1]`.

### Level 2 (Middle Level)
- Nodes processed: `7`, `1`.
- `current_level` = `[7, 1]`.
- `result.appendleft([7, 1])`.
- `result` is now `[[7, 1], [12]]`.
- Queue is now `[9, 2, 10, 5]`.

### Level 3 (Bottom Level)
- Nodes processed: `9`, `2`, `10`, `5`.
- `current_level` = `[9, 2, 10, 5]`.
- `result.appendleft([9, 2, 10, 5])`.
- `result` is now `[[9, 2, 10, 5], [7, 1], [12]]`.
- Queue is empty!

Convert `result` to list and return.

## 📊 Visual Diagram
Here is how `appendleft` magically reverses the order of the levels without needing to reverse the array at the end:

```mermaid
flowchart TD
    subgraph Iteration1Top ["Iteration 1 (Top)"]
        L1["current_level = [12]"]
        R1["result = [[12]]"]
    end
    
    subgraph Iteration2Middle ["Iteration 2 (Middle)"]
        L2["current_level = [7, 1]"]
        R2["result = [[7, 1], [12]]"]
    end
    
    subgraph Iteration3Bottom ["Iteration 3 (Bottom)"]
        L3["current_level = [9, 2, 10, 5]"]
        R3["result = [[9, 2, 10, 5], [7, 1], [12]]"]
    end

L1 --> R1
R1 --> Iteration 2 (Middle)
    L2 --> R2
R2 --> Iteration 3 (Bottom)
    L3 --> R3

styleR1fill:#e3f2fd,color:#000
    style R2 fill:#e3f2fd,color:#000
    style R3 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. Every node is visited exactly once. The `appendleft()` operation on a deque is $O(1)$, so inserting levels at the front is extremely fast. Converting the deque to a list at the very end takes $O(N)$ time, keeping the overall time complexity linear.
- **Space Complexity:** $O(N)$. The BFS queue can hold up to $N/2$ nodes. The `result` deque also holds $O(N)$ elements.

### Edge Cases Handled Safely
- **Empty Tree:** `if not root: return []` catches it instantly.
- **Unbalanced Tree / Single Sided:** Because BFS strictly processes nodes by depth, an unbalanced tree is handled perfectly. The levels are collected left-to-right exactly as they appear at that depth, regardless of how skewed the tree is.
