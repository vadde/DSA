# 🚶‍♂️ Walkthrough: Find the Missing Number

## 👶 Explain Like I'm 5
You have a set of puzzle pieces numbered from 0 to $N$. But there is one problem: your box only holds $N$ pieces, so exactly ONE piece is missing!
Because the pieces are numbered starting at 0, their numbers match their spots perfectly! (Piece 0 belongs at index 0, Piece 3 belongs at index 3).

Wait, what if we find Piece $N$? There is no index $N$ since the box only holds $N$ pieces (indices 0 to $N-1$). That's totally fine! If we find Piece $N$, we just ignore it and leave it where it is. We just keep swapping all the OTHER pieces into their correct spots.
Once we are done swapping, we just walk down the line. If we look at index 2 and don't see Piece 2, we know that Piece 2 is the missing one!

## 🎯 Core Strategy
This is a standard **Cyclic Sort** with two minor twists: numbers start at $0$, and one number ($N$) is out of bounds.

1. **Sort (Cyclic Sort pass):**
   - Initialize pointer `i = 0`.
   - Loop through the array using a `while i < n` loop.
   - The correct index for the number `nums[i]` is exactly `nums[i]`. Let `j = nums[i]`.
   - **Check Bounds & Swap**: If the number is a valid index (`j < n`) AND it is not already at its correct index (`nums[i] != nums[j]`):
     - Swap `nums[i]` and `nums[j]`.
     - Do NOT increment `i`.
   - **Ignore / Happy**: Else (the number is $N$, or it's already in the correct spot):
     - Increment `i += 1`.
2. **Find (Second pass):**
   - Iterate through the array `for i in range(n)`.
   - The first index where the number doesn't match the index (`nums[i] != i`) is the missing number! Return `i`.
3. If all indices match their numbers perfectly, the missing number must be $N$ itself. Return `n`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `nums = [4, 0, 3, 1]`. Length $N = 4$.
Initialization: `i = 0`.

### Phase 1: Cyclic Sort

| Step | `i` | `nums[i]` | Bounds Check (`j < 4`) | Happy? (`nums[i] == nums[j]`) | Action | Array State |
|------|-----|-----------|------------------------|-------------------------------|--------|-------------|
| 1 | `0` | `4` | `4 < 4`? **No (Out of bounds)** | - | Ignore. `i += 1`. | `[4, 0, 3, 1]` |
| 2 | `1` | `0` | `0 < 4`? Yes | No (`nums[1] != nums[0]`) | Swap index 1 and 0. | `[0, 4, 3, 1]` |
| 3 | `1` | `4` | `4 < 4`? **No (Out of bounds)** | - | Ignore. `i += 1`. | `[0, 4, 3, 1]` |
| 4 | `2` | `3` | `3 < 4`? Yes | No (`nums[2] != nums[3]`) | Swap index 2 and 3. | `[0, 4, 1, 3]` |
| 5 | `2` | `1` | `1 < 4`? Yes | No (`nums[2] != nums[1]`) | Swap index 2 and 1. | `[0, 1, 4, 3]` |
| 6 | `2` | `4` | `4 < 4`? **No (Out of bounds)** | - | Ignore. `i += 1`. | `[0, 1, 4, 3]` |
| 7 | `3` | `3` | `3 < 4`? Yes | **YES!** (`nums[3] == nums[3]`) | Happy. `i += 1`. | `[0, 1, 4, 3]` |

### Phase 2: Find Missing
Walk through `[0, 1, 4, 3]`:
- Index `0`: `0` (Match)
- Index `1`: `1` (Match)
- Index `2`: `4` (**MISMATCH!**) $\rightarrow$ Missing number is `2`.

Result: `2`.

## 📊 Visual Diagram
Here is how the out-of-bounds number $N$ is naturally ignored, leaving a hole where the missing number should be:

```mermaid
flowchart TD
    subgraph SortPass [Sort Pass]
        W1["Array: [4, 0, 3, 1]\nN = 4"]
        N1["Sort pushes 0, 1, 3 to their spots.\n4 is ignored because there is no index 4!"]
    end
    
    subgraph SortedState [Sorted State]
        W2["Array: [0, 1, 4, 3]"]
    end
    
    subgraph FindPass [Find Pass]
        W3["Index 0: 0\nIndex 1: 1\nIndex 2: 4 (Should be 2!)\nIndex 3: 3"]
        N3["Return 2!"]
    end

SortPass --> SortedState
SortedState --> Find Pass
    
    style N1 fill:#fff9c4,color:#000
    style W3 fill:#ffcdd2,color:#000
    style N3 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. The first pass places elements in their correct indices using at most $N-1$ swaps. The second pass iterates through the array once. $O(N) + O(N) = O(N)$.
- **Space Complexity:** $O(1)$. All operations are done in-place.

### Edge Cases Handled Safely
- **Missing number is $N$:** e.g., `[0, 1, 2]`. The sort phase finishes doing absolutely nothing. The second pass verifies `0==0`, `1==1`, `2==2`. The loop finishes without returning, so the function hits the final line `return n`, which correctly returns `3`.
- **Missing number is 0:** e.g., `[1, 2, 3]`. The sort phase results in `[3, 1, 2]`. The second pass immediately checks index 0, sees `3 != 0`, and returns `0`.
