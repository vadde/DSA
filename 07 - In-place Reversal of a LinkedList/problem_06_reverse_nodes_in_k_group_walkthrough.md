# 🚶‍♂️ Walkthrough: Reverse Nodes in k-Group

## 👶 Explain Like I'm 5
This is a very strict version of the "Reverse every K-element Sub-list" problem.
Imagine you have a line of friends and $K=3$. 
You walk up to the first 3 friends, and flip them around.
You walk up to the next 3 friends, and flip them around.
Finally, you reach the end of the line, and there are only 2 friends left.
In the old problem, we flipped them anyway!
But in THIS problem, the rule is: **"If there are less than 3 friends, DO NOT touch them!"**
So you just leave the last 2 friends exactly as they are and go home.

To do this safely, before we even *start* flipping a group, we just do a quick count:
"1, 2, 3... okay, we have enough, let's flip!"
If the count stops at 2 because the line ended, we just stop entirely.

## 🎯 Core Strategy
We use the exact same logic from "Reverse every K-element Sub-list", but we add a "Look-Ahead" helper function to count the remaining nodes.

1. **Look-Ahead (`has_k_nodes`)**: Write a small helper function that takes a node and walks forward $K$ steps. If it hits `None` before reaching $K$, it returns `False`. Otherwise `True`.
2. Initialize `current = head`, `prev = None`.
3. Loop `while current is not None`:
   - **NEW STEP**: Run `has_k_nodes(current, k)`. If it returns `False`, we simply `break` out of the entire `while` loop! The leftover nodes stay exactly where they are.
   - **Memorize Borders**: `node_before_sublist = prev` and `last_node_of_sublist = current`.
   - **Reverse**: Run the standard 4-step reversal logic for exactly $K$ steps.
   - **Reconnect Borders**:
     - `node_before_sublist.next = prev` (or update `head = prev`).
     - `last_node_of_sublist.next = current`.
   - **Prepare for Next Group**: Set `prev = last_node_of_sublist`.
4. Return `head`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `1 -> 2 -> 3 -> 4 -> 5`, $K = 3$.
Initialization: `current = 1`, `prev = null`.

### Group 1 (Nodes 1, 2, 3)
- `has_k_nodes(1, 3)`: Counts 1, 2, 3. Returns `True`!
- Memorize: `node_before = null`, `last_node = 1`.
- Reverse 3 nodes. `current` moves to `4`, `prev` moves to `3`.
- Reconnect:
  - `head = prev` (`head = 3`).
  - `last_node (1).next = current (4)`.
- List is now `3 -> 2 -> 1 -> 4 -> 5`.
- Set `prev = last_node` (`prev = 1`).

### Group 2 (Nodes 4, 5)
- `current` is `4`.
- `has_k_nodes(4, 3)`: Counts 4, 5... hits `null`. Count is 2. Returns `False`!
- The outer `while` loop `break`s instantly!

Result: `3 -> 2 -> 1 -> 4 -> 5`. The `4 -> 5` part was completely untouched!

## 📊 Visual Diagram
Here is a visualization of the Look-Ahead function preventing a reversal:

```mermaid
flowchart TD
    subgraph Group1Done [Group 1 Done]
        W1["[3] -> [2] -> [1] -> [4] -> [5]"]
        N1["prev is [1], current is [4]"]
    end
    
    subgraph LookAheadCheck ["Look-Ahead Check"]
        W2["has_k_nodes(current=4, k=3)"]
        N2["Count 1: Node 4\nCount 2: Node 5\nCount 3: null!"]
    end
    
    subgraph Action
        W3["Return False!"]
        N3["Break loop immediately.\nLeftover nodes [4] -> [5] are safe!"]
    end

Group1Done --> Look-Ahead Check
    Look-Ahead Check --> Action
    
    style W2 fill:#fff9c4,color:#000
    style N3 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. Every node is visited twice. Once by the `has_k_nodes` helper function to verify it's part of a valid group, and once by the main pointer to actually reverse it. $O(2N)$ simplifies strictly to $O(N)$.
- **Space Complexity:** $O(1)$. It's completely in-place.

### Edge Cases Handled Safely
- **Length of list is not a multiple of $K$:** Handled perfectly by the `break` condition. The leftover nodes remain untouched.
- **$K = 1$:** The fast-path `if k <= 1: return head` handles this instantly.
- **Empty list:** Handled instantly by the fast-path check.
