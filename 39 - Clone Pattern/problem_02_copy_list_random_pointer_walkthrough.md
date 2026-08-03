# 🚶‍♂️ Walkthrough: Copy List with Random Pointer

## 👶 Explain Like I'm 5
You have a line of people holding hands, but each person is also pointing at one random person in the line (or nobody).
You need to make a perfect clone of this line.
Instead of making a separate list and keeping a confusing notebook of who is who, we use a brilliant trick!
For every person, we make their clone stand *immediately behind them* in the line!
`Original A -> Clone A -> Original B -> Clone B`.
Now, if Original A is pointing at Original B, Clone A just points to whatever Original B is holding hands with (which is Clone B)!
Once all the pointing is done, we just separate the Originals and the Clones into two different lines!

## 🎯 Core Strategy
**O(1) Space Weaving Technique**.

This avoids the $O(N)$ space Hash Map approach.
1. **Pass 1 (Weave)**: Iterate through the original list. For each node, create a clone node. Set the clone's `next` to the original's `next`. Then set the original's `next` to the clone.
   - Result: `A -> A' -> B -> B' -> C -> C'`
2. **Pass 2 (Assign Randoms)**: Iterate through the weaved list. The clone is always `curr.next`.
   - If `curr.random` exists, then `clone.random` should be `curr.random.next` (because the original random's clone is sitting right next to it!).
3. **Pass 3 (Unweave)**: Separate the list back into two.
   - `curr.next = curr.next.next`
   - `clone.next = clone.next.next`

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**List**: `A(7) -> B(13)`. `A.random = None`, `B.random = A`.

**Pass 1 (Weave)**:
- `A` points to `A'`. `A'` points to `B`.
- `B` points to `B'`. `B'` points to `None`.
`A -> A' -> B -> B' -> None`

**Pass 2 (Assign Randoms)**:
- `curr = A`. `A.random` is `None`. `A'.random` = `None`. Move to `B`.
- `curr = B`. `B.random` is `A`. `B'.random` = `B.random.next`, which is `A'`. Move to `None`.
(Perfect! `B'` now points to `A'`).

**Pass 3 (Unweave)**:
- `clone_head = A'`.
- `curr = A`, `clone = A'`.
  - `A.next = A'.next` (which is `B`).
  - `A'.next = B.next` (which is `B'`).
- `curr = B`, `clone = B'`.
  - `B.next = B'.next` (which is `None`).
  - `B'.next = None`.

Original restored: `A -> B -> None`
Clone extracted: `A' -> B' -> None` ✅

## 📊 Visual Diagram

```mermaid
flowchart TD
    subgraph Pass1Weave ["Pass 1: Weave"]
    A["curr = head"] --> B{"curr?"}
    B -->|YES| C["clone = Node(val)\nclone.next = curr.next\ncurr.next = clone\ncurr = clone.next"]
    C --> B
end

subgraphPass2: Assign Randoms
    D["curr = head"] --> E{"curr?"}
    E -->|YES| F{"curr.random exists?"}
    F -->|YES| G["curr.next.random = curr.random.next"]
    F -->|NO| H["curr = curr.next.next"]
    G --> H
H --> E
    end
    
    subgraph Pass3Unweave ["Pass 3: Unweave"]
    I["curr = head\nclone_head = head.next"] --> J{"curr?"}
    J -->|YES| K["clone = curr.next\ncurr.next = clone.next\nIf clone.next: clone.next = clone.next.next"]
    K --> L["curr = curr.next"]
    L --> J
J -->|NO| M["Return clone_head"]
    end
    
    style M fill:#c8e6c9,color:#000
```

## 🛑 Complexity
- **Time:** $O(N)$ — 3 distinct passes over the list.
- **Space:** $O(1)$ — We don't use any extra data structures, just pointers!
