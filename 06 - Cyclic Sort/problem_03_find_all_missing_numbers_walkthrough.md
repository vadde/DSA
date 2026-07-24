# 🚶‍♂️ Walkthrough: Find all Missing Numbers

## 👶 Explain Like I'm 5
You have a box of 8 puzzle pieces, but someone mixed them up, and even worse, they accidentally put some duplicate pieces in the box and lost some of the original pieces! The pieces are supposed to be numbered 1 through 8.

We use our Cyclic Sort magic trick to put every piece in its correct spot. If we pick up Piece 3, we put it in the 3rd spot.
But what if we pick up another Piece 3 later? We look at the 3rd spot, see that a Piece 3 is already sitting there perfectly happy, and we say, "Oh well, you're a duplicate." We just leave the duplicate exactly where we found it and move on!

After we try to sort the whole box, we just walk down the line. If the 5th spot doesn't have a Piece 5 in it (maybe it has a duplicate Piece 3 stuck there instead), we know Piece 5 is missing! We write down '5' and keep checking the rest of the spots.

## 🎯 Core Strategy
This is a standard **Cyclic Sort** designed to naturally handle duplicates by ignoring them.

1. **Sort (Cyclic Sort pass):**
   - Initialize pointer `i = 0`.
   - Loop through the array using a `while i < n` loop.
   - The correct index for the number `nums[i]` is `nums[i] - 1`. Let `j = nums[i] - 1`.
   - **Check & Swap**: If the number is NOT already sitting at its correct index (`nums[i] != nums[j]`):
     - *Crucially, this check also means "if the number currently sitting at the target index `j` is not an identical duplicate".* If they are identical, `nums[i] == nums[j]` would evaluate to True!
     - Swap `nums[i]` and `nums[j]`. Do NOT increment `i`.
   - **Ignore / Happy**: If `nums[i] == nums[j]`, the number is either happily in its perfect home, OR it is a duplicate trapped in the wrong spot because its home is already occupied by its twin. Either way, just `i += 1`.
2. **Find (Second pass):**
   - Iterate through the array `for i in range(n)`.
   - If `nums[i] != i + 1`, then the number `i + 1` is missing. Add it to a `missing_numbers` list.
3. Return `missing_numbers`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `nums = [2, 3, 2, 1]`. Length $N = 4$.
Initialization: `i = 0`.

### Phase 1: Cyclic Sort

| Step | `i` | `nums[i]` | Target `j` (`nums[i]-1`) | Happy or Duplicate? (`nums[i] == nums[j]`) | Action | Array State |
|------|-----|-----------|--------------------------|--------------------------------------------|--------|-------------|
| 1 | `0` | `2` | `1` | No (`nums[0] != nums[1]`, `2 != 3`) | Swap 0 and 1. | `[3, 2, 2, 1]` |
| 2 | `0` | `3` | `2` | No (`nums[0] != nums[2]`, `3 != 2`) | Swap 0 and 2. | `[2, 2, 3, 1]` |
| 3 | `0` | `2` | `1` | **YES!** (`nums[0] == nums[1]`, `2 == 2`). It's a duplicate! | Ignore. `i += 1`. | `[2, 2, 3, 1]` |
| 4 | `1` | `2` | `1` | **YES!** (`nums[1] == nums[1]`). It's happy! | Ignore. `i += 1`. | `[2, 2, 3, 1]` |
| 5 | `2` | `3` | `2` | **YES!** (`nums[2] == nums[2]`). It's happy! | Ignore. `i += 1`. | `[2, 2, 3, 1]` |
| 6 | `3` | `1` | `0` | No (`nums[3] != nums[0]`, `1 != 2`) | Swap 3 and 0. | `[1, 2, 3, 2]` |
| 7 | `3` | `2` | `1` | **YES!** (`nums[3] == nums[1]`, `2 == 2`). It's a duplicate! | Ignore. `i += 1`. | `[1, 2, 3, 2]` |

### Phase 2: Find Missing
Walk through `[1, 2, 3, 2]`:
- Index `0` (Spot 1): `1` (Match)
- Index `1` (Spot 2): `2` (Match)
- Index `2` (Spot 3): `3` (Match)
- Index `3` (Spot 4): `2` (**MISMATCH!**) $\rightarrow$ Spot 4 is occupied by a duplicate `2`. The number `4` is missing.

Result: `[4]`.

## 📊 Visual Diagram
Here is how the cyclic sort elegantly traps duplicates:

```mermaid
flowchart TD
    subgraph Step 3 [Index 0 has '2']
        W1["Array: [2, 2, 3, 1]"]
        N1["2 belongs at index 1!\nBut index 1 already has a '2'!"]
    end
    
    subgraph The Trap
        W2["nums[0] == nums[1]\n2 == 2"]
        N2["It's a duplicate! We can't swap them,\nwe'd be stuck in an infinite loop!\nJust leave it trapped and i += 1."]
    end
    
    Step 3 --> The Trap
    
    style The Trap fill:#fff9c4,color:#000
    style N2 fill:#ff6b6b,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. The cyclic sort takes at most $N-1$ swaps, and the array iteration takes exactly $N$ steps. The second pass takes another $N$ steps. Total is strictly $O(N)$.
- **Space Complexity:** $O(1)$. All operations are done in-place, ignoring the space required for the output array.

### Edge Cases Handled Safely
- **No missing numbers:** e.g., `[1, 2, 3]`. The array perfectly sorts. The second pass verifies `1==1, 2==2, 3==3` and returns an empty list `[]`.
- **Many missing numbers:** The logic flawlessly scales to multiple gaps. Every index that doesn't match `i+1` is appended to the result.
