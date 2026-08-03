# 🚶‍♂️ Walkthrough: Ceiling of a Number

## 👶 Explain Like I'm 5
You want to buy a pair of shoes that cost `$45`.
You are looking at a sorted list of price tags: `[$10, $20, $30, $40, $50, $60]`.

You don't have exactly `$45`, but you want to find the CHEAPEST shoe that is at least `$45` (so you can afford it with a `$50` bill). 
This is called the **"Ceiling"**. It's the smallest number that is `>=` your target.

If you do a normal Binary Search for `$45`, you won't find it. Usually, Binary Search just returns `-1` if the exact number isn't there.
BUT, when the Binary Search finishes and the `left` pointer crosses over the `right` pointer (so `left > right`), an amazing thing happens: the `left` pointer will magically be pointing exactly at the Ceiling! (In this case, the `$50` shoe).

Why? Because `left` only moves to the right when it sees numbers that are too small. It stops moving the moment it passes all the small numbers.
So, you just return `left`!

## 🎯 Core Strategy
This uses the **Modified Binary Search** pattern. We just alter what we return when the search fails.

1. **Upper Bound Check**: If the target `key` is larger than the very last element in the array (`arr[-1]`), there is NO ceiling. Return `-1` immediately.
2. **Initialization**: Initialize `left = 0` and `right = len(arr) - 1`.
3. **Binary Search Loop**: Loop while `left <= right`:
   - Calculate `mid = left + (right - left) // 2`.
   - If `arr[mid] == key`, we found an exact match! Return `mid` (because an exact match is a valid ceiling).
   - If `key < arr[mid]`, target is on the left (`right = mid - 1`).
   - If `key > arr[mid]`, target is on the right (`left = mid + 1`).
4. **The Magic Return**: The loop broke because `left > right`. We didn't find an exact match. But `left` is now naturally pointing to the smallest number greater than the target. Return `left`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `arr = [1, 3, 8, 10, 15]`, `key = 12`

### Initialization
- Check upper bound: `12 > 15`? No.
- `left = 0`, `right = 4`.

### Loop 1
- `left = 0, right = 4`.
- `mid = 0 + (4 - 0) // 2 = 2`.
- `arr[2]` is `8`.
- `8 == 12`? NO.
- Is `12 < 8`? NO. `12 > 8`.
- Target is larger, so search right: `left = mid + 1 = 3`.

### Loop 2
- `left = 3, right = 4`.
- `mid = 3 + (4 - 3) // 2 = 3`.
- `arr[3]` is `10`.
- `10 == 12`? NO.
- Is `12 < 10`? NO. `12 > 10`.
- Target is larger, so search right: `left = mid + 1 = 4`.

### Loop 3
- `left = 4, right = 4`.
- `mid = 4 + (4 - 4) // 2 = 4`.
- `arr[4]` is `15`.
- `15 == 12`? NO.
- Is `12 < 15`? YES!
- Target is smaller, so search left: `right = mid - 1 = 3`.

### Loop Ends
- `left` is `4`. `right` is `3`.
- `left <= right` is False. Loop breaks.
- Return `left` which is `4`.
- `arr[4]` is `15`. Correct! `$15` is the ceiling of `$12`.

## 📊 Visual Diagram
Here is a visual showing the final crossover moment:

```mermaid
flowchart TD
    subgraph FinalLoopState [Final Loop State]
        A["Array: [1, 3, 8, 10, 15]"]
        L1["Left=4 (Value: 15)"]
        R1["Right=4 (Value: 15)"]
        M1["Mid=4 (Value: 15)"]
        T["Target = 12"]
    end
    
    subgraph TheCrossover [The Crossover]
        C1["Target (12) < Mid (15)"]
        C2["Right pointer moves left: Right = Mid - 1 = 3"]
        C3["Left (4) > Right (3)\nLoop Breaks!"]
    end
    
    subgraph TheMagic [The Magic]
        M["Left pointer (4) is permanently parked\non the first number > 12"]
    end

FinalLoopState --> TheCrossover
TheCrossover --> The Magic
    
    style L1 fill:#bbdefb,color:#000
    style R1 fill:#ffcdd2,color:#000
    style M1 fill:#e1bee7,color:#000
    
    style C1 fill:#f5f5f5,color:#000
    style C3 fill:#ffcc80,color:#000
    style M fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(\log N)$. Standard binary search time.
- **Space Complexity:** $O(1)$. Just storing pointer variables.

### Edge Cases Handled Safely
- **Key is larger than ALL elements:** E.g., `key = 20`. The initial check `if key > arr[-1]: return -1` catches this immediately in $O(1)$ time without even doing the search.
- **Key is smaller than ALL elements:** E.g., `key = -5`. The loop will repeatedly move `right` to the left. Eventually, `right` becomes `-1`, while `left` stays solidly at `0`. The loop breaks, and it returns `left = 0`, correctly identifying the very first element as the ceiling.
