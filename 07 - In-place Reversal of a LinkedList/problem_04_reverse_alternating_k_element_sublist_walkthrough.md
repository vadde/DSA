# 🚶‍♂️ Walkthrough: Reverse Alternating K-element Sub-list

## 👶 Explain Like I'm 5
You have a line of friends holding hands, and you want them to turn around in groups of $K$, but **skipping every other group!**

If $K=2$:
1. The first 2 friends flip.
2. The next 2 friends stay EXACTLY the same (just walk past them).
3. The next 2 friends flip.
4. The next 2 friends stay the same.

You keep doing this alternating pattern until you run out of friends.
This is exactly like our last problem ("Reverse every K-element Sub-list"), except after we reconnect the reversed group, we literally just tell our pointers to walk forward by $K$ steps before we repeat the giant loop!

## 🎯 Core Strategy
This is an iterative application of the "Reverse a Sub-list" logic, interleaved with a simple "Skip" logic.

1. Initialize `current = head`, `prev = None`.
2. Loop `while current is not None`:
   - **PHASE 1: REVERSE**
     - Memorize `node_before_sublist = prev`.
     - Memorize `last_node_of_sublist = current`.
     - Run standard 4-step reversal logic for exactly $K$ steps (or until `current` is None).
     - Reconnect edges (`node_before_sublist.next = prev`, `last_node_of_sublist.next = current`).
     - Set `prev = last_node_of_sublist`. (This prepares the `prev` anchor for the skipped group).
   - **PHASE 2: SKIP**
     - We just reversed a group of $K$. Now we must skip a group of $K$!
     - Loop `while current is not None and i < k`:
       - `prev = current`
       - `current = current.next`
       - Increment `i`.
     - *After this skip loop finishes, `prev` is resting on the final node of the skipped group. This perfectly sets it up to act as `node_before_sublist` for the NEXT reversal group!*
3. Return `head`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `1 -> 2 -> 3 -> 4 -> 5`, $K = 2$.
Initialization: `current = 1`, `prev = null`.

### Phase 1: Reverse Group (Nodes 1, 2)
- Memorize: `node_before = null`, `last_node = 1`.
- Reverse 2 nodes. `current` moves to `3`, `prev` moves to `2`.
- Reconnect:
  - `head = prev` (`head = 2`).
  - `last_node (1).next = current (3)`.
- List is now `2 -> 1 -> 3 -> 4 -> 5`.
- Set `prev = last_node` (`prev = 1`).

### Phase 2: Skip Group (Nodes 3, 4)
- Loop 2 times:
  - Iteration 1: `prev = 3`, `current = 4`.
  - Iteration 2: `prev = 4`, `current = 5`.

### Phase 1 Again: Reverse Group (Node 5)
- Memorize: `node_before = 4`, `last_node = 5`.
- Reverse 2 nodes (but only 1 exists). `current` hits `null`, `prev` moves to `5`.
- Reconnect:
  - `node_before (4).next = prev (5)`. (4 points to 5).
  - `last_node (5).next = current (null)`.
- List is now `2 -> 1 -> 3 -> 4 -> 5 -> null`.
- Outer loop terminates.

Result: `2 -> 1 -> 3 -> 4 -> 5 -> null`.

## 📊 Visual Diagram
Here is a visualization of how the Skip phase sets up the next Reversal phase perfectly:

```mermaid
flowchart TD
    subgraph ReversePhaseDone [Reverse Phase Done]
        W1["List: [2] -> [1] -> [3] -> [4] -> [5]"]
        N1["prev is [1]\ncurrent is [3]"]
    end
    
    subgraph SkipPhase [Skip Phase: Skip K=2]
        W2["Advance prev and current twice!"]
        N2["prev becomes [4]\ncurrent becomes [5]"]
    end
    
    subgraph NextReversePhaseBegins [Next Reverse Phase Begins]
        W3["Start reversing at current [5]"]
        N3["When done, the reversed group reconnects to prev [4]!"]
    end

ReversePhaseDone --> SkipPhase
SkipPhase --> Next Reverse Phase Begins
    
    style N2 fill:#fff9c4,color:#000
    style N3 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We visit every node exactly once—either during the inner reversal loop or the inner skip loop. The outer `while` loop guarantees we process the entire array without going backwards.
- **Space Complexity:** $O(1)$. All reversal and skipping is done using in-place pointer manipulation.

### Edge Cases Handled Safely
- **Leftover elements < $K$ (in skip phase):** Handled perfectly. The inner skip loop `while current is not None and i < k:` gracefully stops early when `current` hits `None`.
- **Leftover elements < $K$ (in reverse phase):** Handled perfectly. Reverses whatever is left and reconnects it exactly like normal.
