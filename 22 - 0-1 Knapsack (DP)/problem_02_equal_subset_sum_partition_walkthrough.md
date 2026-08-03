# 🚶‍♂️ Walkthrough: Equal Subset Sum Partition

## 👶 Explain Like I'm 5
Can you split an array into **TWO groups** that have **EQUAL sums**?
Example: `[1, 5, 11, 5]` → Group A: `{1, 5, 5}` (sum 11) and Group B: `{11}` (sum 11). Yes!

**Key Insight**: If the total sum is `S`, we need to find ONE group that sums to exactly `S/2`. If such a group exists, the rest automatically forms the other group with the same sum!
- If `S` is odd → impossible (no integer can be half of it).

## 🎯 Core Strategy
Reduces to the **Subset Sum** problem using 0/1 Knapsack Boolean DP.

`dp[w]` = `True` if any subset of numbers sums to exactly `w`.

1. **Parity Check**: If `sum(nums) % 2 != 0`, return `False`.
2. **Set Target**: `target = sum(nums) // 2`.
3. **Initialize**: `dp = [False] * (target + 1)`. Set `dp[0] = True` (empty subset sums to 0).
4. **Fill DP**: For each `num`, for `w` from `target` down to `num`:
   - `dp[w] = dp[w] or dp[w - num]`
   - "We can reach sum `w` if either we already could (without this `num`), OR we could reach `w - num` before (and add this `num`)."
5. **Return** `dp[target]`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `[1, 5, 11, 5]`, total = 22, target = 11

### Initial DP (size 12)
`dp = [T, F, F, F, F, F, F, F, F, F, F, F]`

### num = 1 (reverse from 11 to 1):
- `dp[1] |= dp[0]` → `True`
- `dp = [T, T, F, F, F, F, F, F, F, F, F, F]`

### num = 5 (reverse from 11 to 5):
- `dp[6] |= dp[1]` → `True`
- `dp[5] |= dp[0]` → `True`
- `dp = [T, T, F, F, F, T, T, F, F, F, F, F]`

### num = 11 (reverse from 11 to 11):
- `dp[11] |= dp[0]` → `True` ← Found a way!
- `dp = [T, T, F, F, F, T, T, F, F, F, F, T]`

### num = 5 (reverse from 11 to 5):
- `dp[11] |= dp[6]` → already `True`
- ... (other updates, but we already have `dp[11] = True`)

**Return `dp[11] = True`** ✅

## 📊 Visual Diagram

```mermaid
flowchart TD
    A["sum = 22, odd? NO\ntarget = 11"]
    B["dp["0..11"] = [T,F,F,...,F]"]
    C["Process each num\n(0/1 Knapsack, reversed)"]
    D["After num=11:\ndp[11] = True!"]
    E["Return dp[11] = True"]
    
    A --> B --> C --> D --> E
    
    style D fill:#c8e6c9,color:#000
    style E fill:#a5d6a7,color:#000
```

## 🛑 Edge Cases & Complexity
- **Time:** $O(N \times S/2)$ where $S$ is the total sum.
- **Space:** $O(S/2)$.
- **Odd sum:** E.g., `[1, 2, 3, 5]` — total = 11 (odd). Immediately return `False`.
- **Single element:** `[2]` — target = 1. `dp` array has no `True` reachable except `dp[0]`. Return `False`.
