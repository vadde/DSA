# 🚶‍♂️ Walkthrough: Kth Smallest Number in a Sorted Matrix

## 👶 Explain Like I'm 5
You have a square grid of numbers where **every row** is sorted from left to right AND **every column** is sorted from top to bottom.

Think of it like a bookshelf where each shelf (row) is organized from smallest to largest, and the shelves themselves (columns, top-to-bottom) are also organized smallest to largest.

You want to find the *k*th smallest number in the whole grid **without** dumping everything into one pile and sorting it.

Since the top-left corner is guaranteed to be the smallest, we start there. After picking the smallest, the **next** candidates are its right neighbor and its bottom neighbor. We throw them in a **Min-Heap** and repeat!

## 🎯 Core Strategy
This applies **K-way Merge** to a 2D matrix. The matrix's rows and columns are treated as `K` sorted sequences, but we navigate them spatially using coordinates instead of explicit pointers.

1. **Initialization**: Push the top-left element `(matrix[0][0], row=0, col=0)` into the `min_heap`. Add `(0, 0)` to a `visited` set.
2. **Count-driven Pop**: Loop `k` times:
   - Pop the smallest `(value, r, c)`.
   - Increment `count`. If `count == k`, return `value`.
   - If the right neighbor `(r, c+1)` exists AND hasn't been visited, push it and mark visited.
   - If the bottom neighbor `(r+1, c)` exists AND hasn't been visited, push it and mark visited.
3. **Why it works**: Because rows and columns are sorted, both the right and bottom neighbors of any cell are guaranteed to be greater than or equal to the current cell. The heap always contains the exact frontier of "next candidate smallest" elements.
4. **Why we need `visited`**: From any cell `(r, c)`, both the cells `(r-1, c)` and `(r, c-1)` could push `(r, c)` into the heap. Without the visited set, `(r, c)` would be pushed **twice**, corrupting the count.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**:
```
[[1,  5,  9],
 [10, 11, 13],
 [12, 13, 15]]
```
`K = 5`

### Step 1: Initialize
- Push `(1, 0, 0)`. Heap = `[(1, 0, 0)]`. Visited = `{(0,0)}`.

### Step 2: Iterate
| Count | Pop | Push Neighbors | Return? |
|---|---|---|---|
| 1 | `(1, 0, 0)` | Right `(5, 0, 1)`, Bottom `(10, 1, 0)` | No |
| 2 | `(5, 0, 1)` | Right `(9, 0, 2)`, Bottom `(11, 1, 1)` | No |
| 3 | `(9, 0, 2)` | Right: none, Bottom `(13, 1, 2)` | No |
| 4 | `(10, 1, 0)` | Right `(11, 1, 1)` already visited, Bottom `(12, 2, 0)` | No |
| 5 | `(11, 1, 1)` | — | **count=5 == K! Return 11** ✅ |

## 📊 Visual Diagram
Here is how the heap explores the matrix like a frontier, always expanding outwards from the smallest corner:

```mermaid
flowchart TD
    subgraph Matrix
        R0["Row 0: [1, 5, 9]"]
        R1["Row 1: [10, 11, 13]"]
        R2["Row 2: [12, 13, 15]"]
    end
    
    subgraph Expansion from (0,0)
        S0["Start: (1, r=0, c=0)"]
        P1["Pop (1)\nPush Right: (5, 0, 1)\nPush Down: (10, 1, 0)"]
    end
    
    subgraph Count Progress
        C1["#1: 1 | #2: 5 | #3: 9 | #4: 10 | #5: 11 ✅"]
    end
    
    subgraph Visited Set Key
        V["Prevents double-push!\nAny cell can be reached\nfrom its left AND its top."]
    end
    
    R0 --> S0
    S0 --> P1
    P1 --> C1
    V --> P1
    
    style S0 fill:#bbdefb,color:#000
    style P1 fill:#fff9c4,color:#000
    style C1 fill:#c8e6c9,color:#000
    style V fill:#ffcdd2,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(K \log K)$. In the worst case, the heap can grow up to $O(K)$ in size (each pop can push up to 2 new elements). We perform $K$ pop operations, each $O(\log K)$.
- **Space Complexity:** $O(K)$ for the Min-Heap and the visited set.

### Edge Cases Handled Safely
- **Empty matrix:** The `if not matrix or not matrix[0]: return -1` guard at the start handles both empty outer list and empty inner rows.
- **K out of bounds:** `if k < 1 or k > total: return -1` validates the range immediately.
- **Duplicate values in matrix:** E.g., `13` appears twice at `(1, 2)` and `(2, 1)`. The heap tuple is `(value, row, col)`. Since `(row, col)` is unique for each cell, ties in value are broken by `row` then `col`, ensuring perfectly correct ordering without crashes.
