# 🚶‍♂️ Walkthrough: Minimum Window Sort

## 👶 Explain Like I'm 5
Imagine a bookshelf where the books are almost perfectly sorted by height from shortest to tallest. But, a mischievous cat knocked over a chunk in the middle and scrambled them. 

You want to find the *exact* chunk of books you need to pull out and re-sort so the ENTIRE shelf is perfectly sorted. You don't want to re-sort the whole shelf, just the messy part!

1. **Find the messy chunk:** You walk from the left until you find a book that is taller than the one after it. That's the start of the mess. Then, you walk from the right until you find a book shorter than the one before it. That's the end of the mess.
2. **The Catch:** What if the smallest book *inside* the mess is actually smaller than the books to the left of the mess? You have to include those left books in your sorting chunk! Similarly, if the tallest book in the mess is taller than the books to the right, you must include those right books too.
3. Once you expand your messy chunk to include those anomalies, you know exactly how many books to pull out.

## 🎯 Core Strategy
This uses a multi-pass **Two Pointers (Opposite Ends)** strategy.
1. Find the first dip from the left to set `low`.
2. Find the first bump from the right to set `high`.
3. If `low` reaches the end of the array, the array is already sorted.
4. Find the `min` and `max` values strictly within the `arr[low:high+1]` subarray.
5. **Expand**:
   - Decrement `low` if the element before it is strictly greater than the `min` of the subarray.
   - Increment `high` if the element after it is strictly less than the `max` of the subarray.
6. The minimum window length is `high - low + 1`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `arr = [1, 3, 2, 0, -1, 7, 10]`

| Step | Action | Values / Indices | Explanation |
|------|--------|------------------|-------------|
| 1 | **Find `low`** (from left) | `1 < 3` (ok). `3 > 2` (dip!) | First out-of-order element is at index `1` (`arr[1] = 3`). So, `low = 1`. |
| 2 | **Find `high`** (from right) | `10 > 7` (ok). `7 > -1` (ok). `-1 < 0` (bump!) | First out-of-order element from right is index `4` (`arr[4] = -1`). So, `high = 4`. |
| 3 | **Find Min/Max in window** | Window: `[3, 2, 0, -1]` | Minimum in window is `-1`. Maximum in window is `3`. |
| 4 | **Expand `low`** | Compare `-1` with elements to the left. | `arr[0] = 1`. `1 > -1`. So `low` expands backwards to `0`. Cannot expand further because index is `0`. |
| 5 | **Expand `high`** | Compare `3` with elements to the right. | `arr[5] = 7`. `7 < 3` is False. So `high` does not expand. `high` remains `4`. |
| 6 | **Calculate Length** | `low = 0`, `high = 4` | Length = `4 - 0 + 1 = 5`. The unsorted window is `[1, 3, 2, 0, -1]`. |

## 📊 Visual Diagram
Here is a visual representation of why the expansion step is critical:

```mermaid
stateDiagram-v2
    state "arr = [1, 3, 2, 0, -1, 7, 10]" as S0
    
    state "Find initial boundaries" as S1
    state "low = 1 (val: 3) | high = 4 (val: -1)" as S2
    
    state "Subarray: [3, 2, 0, -1]" as S3
    state "Min = -1 | Max = 3" as S4
    
    state "Expand Left: Is arr[low-1] > Min?" as S5
    state "arr[0] is 1. 1 > -1. Yes!" as S6
    state "low becomes 0" as S7
    
    state "Expand Right: Is arr[high+1] < Max?" as S8
    state "arr[5] is 7. 7 < 3. No." as S9
    state "high stays 4" as S10
    
    state "Final Window: arr["0...4"] -> Length 5" as Final
    
    S0 --> S1
S1 --> S2
    S2 --> S3
S3 --> S4
    S4 --> S5
S5 --> S6
    S6 --> S7
S7 --> S8
    S8 --> S9
S9 --> S10
    S10 --> Final
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We scan the array to find `low`, to find `high`, to find the min/max of the subarray, and finally to expand. All these operations are linear, resulting in an overall $O(N)$ time.
- **Space Complexity:** $O(1)$. We only track pointer indices and min/max values.

### Edge Cases Handled Safely
- **Already Sorted Array:** The first `while` loop finding `low` will traverse the entire array. The check `if low == n - 1:` immediately triggers and safely returns `0`.
- **Reverse Sorted Array:** (e.g., `[3, 2, 1]`). `low` stops at `0` because `3 > 2`. `high` stops at `2` because `2 > 1`. The min is `1` and max is `3`. It expands fully and returns `len(arr)`.
- **Duplicates:** The comparisons use `<=` and `>=` when initially finding boundaries to skip over identical sorted elements properly.
