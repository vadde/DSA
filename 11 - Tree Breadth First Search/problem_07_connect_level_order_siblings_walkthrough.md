# 🚶‍♂️ Walkthrough: Connect Level Order Siblings

## 👶 Explain Like I'm 5
Imagine all the kids in a generation are holding hands from left to right.
The leftmost kid holds the hand of the kid next to them, and so on.
The rightmost kid doesn't have anyone to hold onto, so their hand just hangs empty (points to `None`).

We already know how to perfectly line up each generation using a Queue!
All we have to do is remember who the "Previous" kid was.
When we pull a kid out of the line, we tell the "Previous" kid to grab this new kid's hand (`previous_node.next = current_node`).
Then, the new kid becomes the "Previous" kid for the *next* time we pull someone out!
At the start of every new generation, we reset the "Previous" kid to `None`, so generations don't accidentally hold hands with each other.

## 🎯 Core Strategy
This problem requires us to link nodes using a `.next` pointer. Since the links only happen *within* the same level, **Tree Breadth First Search (BFS)** is the perfect tool. We maintain state within the inner level loop to connect adjacent nodes.

1. **Initialization**: If the `root` is None, return `None`. Initialize `queue = deque([root])`.
2. **Level Loop**: Loop `while queue is not empty`:
   - `level_size = len(queue)`.
   - **Reset State**: Initialize `previous_node = None`. This ensures that the last node of Level 1 doesn't accidentally connect to the first node of Level 2.
   - **Node Loop**: Loop exactly `level_size` times:
     - Pop `current_node` from queue.
     - **Make the Connection**: If `previous_node` is not None (meaning this isn't the first node of the level):
       - `previous_node.next = current_node`.
     - **Advance State**: Update `previous_node = current_node`.
     - Append children to the queue (Left then Right).
3. Return the modified `root`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input Tree**:
```text
      12
     /  \
    7    1
   / \  / \
  9  2 10  5
```
Initialization: `queue = [12]`.

### Level 1 (Top Level)
- `level_size` = 1.
- `previous_node` = `None`.
- Pop `12`.
- `previous_node` is `None`. Skip connection.
- `previous_node` becomes `12`.
- Push `7`, `1`. Queue: `[7, 1]`.
- End of level. Node `12`'s `next` pointer naturally defaults to `None`.

### Level 2 (Middle Level)
- `level_size` = 2.
- **`previous_node` is RESET to `None`!**
- **Iteration 1**:
  - Pop `7`.
  - `previous_node` is `None`. Skip connection.
  - `previous_node` becomes `7`.
  - Push `9`, `2`. Queue: `[1, 9, 2]`.
- **Iteration 2**:
  - Pop `1`.
  - `previous_node` is `7`. CONNECT: **`7.next = 1`**.
  - `previous_node` becomes `1`.
  - Push `10`, `5`. Queue: `[9, 2, 10, 5]`.
- End of level. Node `1`'s `next` pointer remains `None`.

### Level 3 (Bottom Level)
- `level_size` = 4.
- **`previous_node` is RESET to `None`!**
- Pop `9`. `prev` becomes `9`.
- Pop `2`. CONNECT: **`9.next = 2`**. `prev` becomes `2`.
- Pop `10`. CONNECT: **`2.next = 10`**. `prev` becomes `10`.
- Pop `5`. CONNECT: **`10.next = 5`**. `prev` becomes `5`.
- End of level. Node `5`'s `next` pointer remains `None`.

## 📊 Visual Diagram
Here is a diagram showing the state of variables during the processing of Level 2:

```mermaid
flowchart TD
    subgraph Setup
        S1["level_size = 2\nprevious_node = None"]
    end
    
    subgraph Pop 7
        P1["Pop 7\nNo prev to connect to.\nprevious_node = 7\nQueue: [1, 9, 2]"]
    end
    
    subgraph Pop 1
        P2["Pop 1\nprevious_node is 7.\nCONNECT: 7 -> 1\nprevious_node = 1\nQueue: [9, 2, 10, 5]"]
    end
    
    Setup --> Pop 7
    Pop 7 --> Pop 1
    
    style S1 fill:#eeeeee,color:#000
    style P1 fill:#fff9c4,color:#000
    style P2 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We visit every node exactly once. Setting pointers takes $O(1)$ time.
- **Space Complexity:** $O(N)$. The BFS queue can hold up to $N/2$ nodes at the bottom level. (Note: The problem description on LeetCode sometimes asks for an $O(1)$ space solution using already established `next` pointers, but this standard BFS approach is $O(N)$ space and perfectly acceptable as the primary solution).

### Edge Cases Handled Safely
- **Empty Tree:** Handled by initial `if not root:` check.
- **Tree missing children:** The BFS handles null children gracefully. If the tree is just `12 -> 7 -> 9` (a straight line leftwards), `level_size` is always 1, `previous_node` is always None when the single node is popped, so no connections are falsely made! All nodes correctly point to `None`.
