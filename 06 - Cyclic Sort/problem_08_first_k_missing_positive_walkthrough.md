# 🚶‍♂️ Walkthrough: Find the First K Missing Positive Numbers

## 👶 Explain Like I'm 5
You have your messy room full of toys, just like the last problem. But this time, your parents want you to find the **first $K$ missing positive toy numbers**. (Like, find the first 3 missing toys starting from 1).

First, we do the exact same trick: Cyclic Sort. We try to put Toy 1 in Spot 1, Toy 2 in Spot 2... ignoring negatives and toys with huge numbers.
When we are done sorting, we walk through the spots. 
If Spot 1 doesn't have Toy 1, then Toy 1 is missing! We write down "1".

But wait! What if the toy sitting in Spot 1 is Toy 100?
Toy 100 is an "extra" toy that we don't care about right now, but we absolutely **need to remember we have it**. Why? Because if we still need to find more missing numbers after checking all $N$ spots, we have to start counting up: $N+1$, $N+2$, $N+3$...
If we accidentally say "Oh, Toy 100 is missing," we'd be wrong, because it was sitting right there in Spot 1!
So we keep a little notepad (`extra_numbers` set) to write down any out-of-bounds toys we see sitting in wrong spots. Then we can safely count up past $N$ without making a mistake.

## 🎯 Core Strategy
This builds on the "Smallest Missing Positive" logic but requires us to keep track of the junk we ignored, because that junk might actually be one of the numbers we are searching for beyond $N$.

1. **Sort (Cyclic Sort pass):**
   - Initialize pointer `i = 0`.
   - Loop `while i < n` and Cyclic Sort. Ignore out-of-bounds numbers (`nums[i] <= 0` or `nums[i] > n`).
2. **Find inside $N$ (Second pass):**
   - Initialize `missing_numbers = []` and `extra_numbers = set()`.
   - Iterate through the array `for i in range(n)`.
   - If we have found $K$ missing numbers, stop entirely! (`break`).
   - If `nums[i] != i + 1`:
     - The number `i + 1` is missing. Add it to `missing_numbers`.
     - The number currently sitting here (`nums[i]`) is an extra out-of-bounds number. Add it to `extra_numbers`.
3. **Find outside $N$ (Third pass):**
   - If we STILL need more numbers (`len(missing_numbers) < k`), we start checking numbers greater than $N$: `candidate = n + 1`.
   - `while len(missing_numbers) < k`:
     - If `candidate` is NOT in `extra_numbers`, it's truly missing! Add it.
     - `candidate += 1`.
4. Return `missing_numbers`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `nums = [3, -1, 4, 5, 5]`, `K = 3`. Length $N = 5$.
Initialization: `i = 0`.

### Phase 1: Cyclic Sort
*Ignoring negatives and duplicates.*
Array becomes: `[-1, 5, 3, 4, 5]` (Spot 1 is `-1`, Spot 2 is `5`, Spot 3 is `3`, Spot 4 is `4`, Spot 5 is `5`).

### Phase 2: Find Inside $N$
Walk through `[-1, 5, 3, 4, 5]`:
- Spot 1 (Index 0): `-1`. **Mismatch!**
  - Add `1` to `missing_numbers`.
  - Add `-1` to `extra_numbers`.
- Spot 2 (Index 1): `5`. **Mismatch!**
  - Add `2` to `missing_numbers`.
  - Add `5` to `extra_numbers`.
- Spot 3 (Index 2): `3`. (Match)
- Spot 4 (Index 3): `4`. (Match)
- Spot 5 (Index 4): `5`. (Match)

`missing_numbers` = `[1, 2]`. We still need 1 more! (Because $K=3$).
`extra_numbers` = `{-1, 5}`.

### Phase 3: Find Outside $N$
Start `candidate = 6` ($N+1$).
- Is `6` in `extra_numbers`? No.
- Add `6` to `missing_numbers`.
- Now `len(missing_numbers) == 3`. Stop!

Result: `[1, 2, 6]`.

## 📊 Visual Diagram
Here is why tracking `extra_numbers` is critical for numbers beyond $N$:

```mermaid
flowchart TD
    subgraph Sorted Array
        W1["Array: [-1, 5, 3, 4, 5]\nN = 5"]
        N1["Spot 2 has a '5'.\nSo '2' is missing.\nBut we must remember we HAVE a 5!"]
    end
    
    subgraph Look Beyond N
        W2["Need 1 more number.\nCheck N+1 (6)."]
        N2["Is 6 in our extra_numbers set {-1, 5}?\nNo. So 6 is truly missing!"]
    end
    
    Sorted Array --> Look Beyond N
    
    style N1 fill:#ffcdd2,color:#000
    style N2 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N + K)$. The cyclic sort takes at most $N-1$ swaps. The second pass takes exactly $N$ steps. The third pass takes at most $K$ steps. Total time is $O(N + K)$.
- **Space Complexity:** $O(K)$. The `extra_numbers` set will store at most $K$ out-of-bounds numbers (because we stop looking after finding $K$ missing numbers). The `missing_numbers` list takes $O(K)$ space.

### Edge Cases Handled Safely
- **$K$ is much larger than missing numbers inside array:** The third pass `while` loop cleanly generates `N+1`, `N+2`, `N+3`... checking against the `extra_numbers` set until it fulfills the quota.
- **Perfectly sorted array:** e.g., `[1, 2, 3]`, $K=2$. Sort does nothing. Second pass does nothing. `extra_numbers` is empty. Third pass generates `4` and `5`. Result: `[4, 5]`. Perfectly logical.
