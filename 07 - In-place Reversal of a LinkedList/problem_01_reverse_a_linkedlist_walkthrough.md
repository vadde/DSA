# 🚶‍♂️ Walkthrough: Reverse a LinkedList

## 👶 Explain Like I'm 5
Imagine a line of people holding hands, all facing forward. Person A is holding Person B's hand, Person B is holding Person C's hand.
You want everyone to turn around, so Person C holds Person B's hand, and Person B holds Person A's hand.

You can't just tell everyone to turn around at once! If Person A lets go of Person B, Person A might forget who Person B was.
So you walk down the line. You ask Person A to let go of Person B, and instead reach out their hand behind them (to nothing, `None`). But before they let go, you memorized that Person B was next!
Then you step over to Person B. You tell them to let go of Person C (after memorizing Person C), and reach back to grab Person A.
You repeat this until you reach the end of the line!

## 🎯 Core Strategy
This is the fundamental **In-place Reversal** pattern that is the building block for all other LinkedList problems in this chapter.

1. We need 3 variables to keep track of state:
   - `prev`: The node we just processed (starts as `None`).
   - `current`: The node we are currently looking at (starts as `head`).
   - `next_node`: The node coming up next (we temporarily save this).
2. Loop while `current` is not `None` (until we fall off the end of the list):
   - **Save**: `next_node = current.next` (Memorize the next node so we don't sever the list and lose it).
   - **Reverse**: `current.next = prev` (Turn around! Point to the previous node).
   - **Advance `prev`**: `prev = current` (Step forward. You are now the 'previous' node for the next step).
   - **Advance `current`**: `current = next_node` (Step forward. Move to the node we saved).
3. When the loop ends, `current` has fallen off the edge and is `None`. `prev` is standing on the very last node. That last node is now the new `head` of our reversed list! Return `prev`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `2 -> 4 -> 6 -> 8 -> null`
Initialization: `prev = null`, `current = 2`.

| Step | `current` | Save `next_node` | Reverse (`current.next = prev`) | Advance `prev` | Advance `current` |
|------|-----------|------------------|---------------------------------|----------------|-------------------|
| 1 | `2` | `4` | `2.next = null` (2 points backwards) | `prev = 2` | `current = 4` |
| 2 | `4` | `6` | `4.next = 2` (4 points to 2) | `prev = 4` | `current = 6` |
| 3 | `6` | `8` | `6.next = 4` (6 points to 4) | `prev = 6` | `current = 8` |
| 4 | `8` | `null` | `8.next = 6` (8 points to 6) | `prev = 8` | `current = null`|

Loop ends because `current` is `null`.
Result: `prev` is `8`. The list is now `8 -> 6 -> 4 -> 2 -> null`.

## 📊 Visual Diagram
Here is a snapshot of Step 2, reversing the link from `4` to `2`:

```mermaid
flowchart LR
    subgraph BeforeStep2 [Before Step 2]
        P1["prev: 2"] -.-> N0["null"]
        C1["current: 4"] --> N1["6"] --> N2["8"]
    end
    
    subgraph Action
        S1["1. next_node = 6"]
        S2["2. current.next = prev (4 points to 2)"]
    end
    
    subgraph AfterStep2 [After Step 2]
        C2["current (was 6)"] --> N3["8"]
        P2["prev (was 4)"] --> P3["2"] -.-> N4["null"]
    end

BeforeStep2 --> Action
Action --> After Step 2
    
    style Action fill:#fff9c4,color:#000
    style S2 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We iterate exactly once over the linked list of $N$ nodes.
- **Space Complexity:** $O(1)$. We only use three temporary pointers (`prev`, `current`, `next_node`), regardless of how massive the linked list is.

### Edge Cases Handled Safely
- **Empty list:** If `head` is `None`, the `while current is not None:` loop never runs. The function instantly returns `prev`, which is initialized to `None`. This is perfectly correct.
- **Single node:** `head = 2 -> null`. Loop runs exactly once. `2` points to `null`. `prev` becomes `2`. Loop terminates and returns `2`. Correct!
