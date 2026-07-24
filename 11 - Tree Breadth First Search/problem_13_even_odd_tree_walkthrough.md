# 🚶‍♂️ Walkthrough: Even Odd Tree

## 👶 Explain Like I'm 5
Imagine a tree where the rows have strict rules about who can stand in them based on the row number:
- **Even Rows (0, 2, 4...)**: Only allow **ODD** numbers. And as you read the row from left to right, the numbers must be getting **strictly bigger**.
- **Odd Rows (1, 3, 5...)**: Only allow **EVEN** numbers. And as you read the row from left to right, the numbers must be getting **strictly smaller**.

Our job is to walk through the tree, row by row. If we see a single number that breaks the rules (wrong odd/even type, or going the wrong direction), we immediately blow the whistle and say `False`. If we check every row and everyone followed the rules, we say `True`!

## 🎯 Core Strategy
This is a validation problem that relies on **Tree Breadth First Search (BFS)** to examine the tree level by level. At each level, we validate the two conditions: parity (odd/even) and monotonicity (strictly increasing/decreasing).

1. **Initialization**: If the `root` is None, return `True` (an empty tree doesn't violate rules).
   - `queue = deque([root])`
   - `level = 0` (Zero-indexed levels).
2. **Level Loop**: Loop `while queue is not empty`:
   - Initialize `prev = None` (used to check if values are strictly increasing/decreasing).
   - **Node Loop**: Loop exactly `len(queue)` times:
     - Pop `node` from queue.
     - **Validation**: 
       - If `level` is even: Check that `node.val` is odd. Check that `node.val > prev`.
       - If `level` is odd: Check that `node.val` is even. Check that `node.val < prev`.
       - If any check fails, return `False`.
     - Update `prev = node.val`.
     - Append children to the queue (Left then Right).
   - Increment `level += 1`.
3. If the loop completes without returning False, return `True`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input Tree**:
```text
          1
        /   \
      10     4
     /  \     \
    3    7     9
```
Initialization: `queue = [1]`, `level = 0`.

### Row 0 (Even Row)
- `level = 0`. `prev = None`.
- Pop `1`.
- Rule 1 (Odd Value): `1 % 2 != 0`. Pass.
- Rule 2 (Increasing): `prev` is None, so skip comparison.
- `prev = 1`. Push `10`, `4`. Queue: `[10, 4]`.
- End of Row 0. `level` becomes 1.

### Row 1 (Odd Row)
- `level = 1`. `prev = None`.
- **Iteration 1**: Pop `10`.
  - Rule 1 (Even Value): `10 % 2 == 0`. Pass.
  - Rule 2 (Decreasing): `prev` is None. Pass.
  - `prev = 10`. Push `3`, `7`. Queue: `[4, 3, 7]`.
- **Iteration 2**: Pop `4`.
  - Rule 1 (Even Value): `4 % 2 == 0`. Pass.
  - Rule 2 (Decreasing): Is `4 < prev (10)`? Yes! Pass.
  - `prev = 4`. Push `9`. Queue: `[3, 7, 9]`.
- End of Row 1. `level` becomes 2.

### Row 2 (Even Row)
- `level = 2`. `prev = None`.
- Pop `3`. Value is odd. `prev` becomes `3`.
- Pop `7`. Value is odd. `7 > 3`. Pass! `prev` becomes `7`.
- Pop `9`. Value is odd. `9 > 7`. Pass! `prev` becomes `9`.
- Queue is empty.

Return `True`!

## 📊 Visual Diagram
Here is how the algorithm reacts when a rule is broken:

```mermaid
flowchart TD
    subgraph Row 2 (Even) - Must be ODD and INCREASING
        Q["Queue: [3, 3]"]
        N1["Pop 3\nValue is odd.\nprev = 3"]
        N2["Pop 3\nValue is odd.\nIs 3 > prev (3)?\nNO! It's equal."]
        R["Return False!"]
    end
    
    Q --> N1
    N1 --> N2
    N2 --> R
    
    style N2 fill:#ffcdd2,color:#000
    style R fill:#ff5252,color:#fff
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We visit every node at most once. The algorithm terminates early if it finds a violation.
- **Space Complexity:** $O(N)$. The BFS queue holds up to $N/2$ nodes.

### Edge Cases Handled Safely
- **Equal adjacent values:** `[3, 3]` in an even row correctly returns `False` because the condition is strictly greater (`node.val > prev`).
- **Single Node:** `root = [2]`. Level is 0 (even), but value is 2 (even). Instantly returns `False`.
- **Deep trees with early failure:** By using BFS instead of DFS, if a rule is broken near the top of the tree, we return `False` immediately without needing to visit the thousands of nodes beneath it.
