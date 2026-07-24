# 🚶‍♂️ Walkthrough: Subarray Sum Equals K

## 👶 Explain Like I'm 5
You have a line of numbers, some positive and some negative: `[1, -1, 1, 1, 1, 1]`.
You want to find how many continuous blocks (subarrays) add up exactly to $K$ (e.g., $K=3$).

Normally, we could use the "Sliding Window" pattern for subarrays. 
BUT WAIT! Sliding Window ONLY works if all numbers are positive (because adding makes the sum bigger, and shrinking makes the sum smaller). 
Here, we have negative numbers! Adding a '-1' actually makes the sum smaller, so the Sliding Window breaks.

Instead, we keep a "Running Total" (Prefix Sum) from the very beginning.
If our Running Total right now is 10, and we are looking for $K = 3$...
We just need to look in our magical notebook to see: "Did my Running Total ever equal 7 in the past?"
If it was 7 in the past, and it's 10 now, that means the numbers in between must add up exactly to 3!
We use a Hash Map to keep track of how many times we've seen every Running Total.

## 🎯 Core Strategy
This is the quintessential **Prefix Sum + Hash Map** pattern. It reduces an $O(N^2)$ brute-force subarray search into an elegant $O(N)$ solution.

1. Initialize `count = 0` (our answer) and `current_sum = 0`.
2. Initialize a dictionary `prefix_sums = {0: 1}`. 
   - **Crucial step**: Why `{0: 1}`? Because before we look at any numbers, our running total is $0$. If we find a number that exactly equals $K$ on its own, `current_sum - K` will be $0$. If $0$ isn't in the map, we'd miss it!
3. Loop through every `num` in the array:
   - **Update Running Total**: `current_sum += num`.
   - **Check for Complement**: Calculate what prefix we would need to chop off to leave exactly $K$: `needed = current_sum - k`.
   - If `needed` is in our `prefix_sums` map, add that frequency to `count`.
   - **Update Map**: Finally, add the new `current_sum` to our `prefix_sums` map (or increment its count if we've seen it before).
4. Return `count`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `nums = [1, 2, 3]`, $k = 3$
Initialization: `count = 0`, `current_sum = 0`, `prefix_sums = {0: 1}`.

| `num` | `current_sum` | `needed` ($sum - 3$) | Is `needed` in map? | `count` | Update `prefix_sums` |
|-------|---------------|----------------------|---------------------|---------|----------------------|
| `1` | 1 | $1 - 3 = -2$ | No | 0 | `{0: 1, 1: 1}` |
| `2` | 3 | $3 - 3 = 0$ | **Yes** (freq 1) | 1 | `{0: 1, 1: 1, 3: 1}` |
| `3` | 6 | $6 - 3 = 3$ | **Yes** (freq 1) | 2 | `{0: 1, 1: 1, 3: 1, 6: 1}` |

Result: 2. (The subarrays are `[1, 2]` and `[3]`).

## 📊 Visual Diagram
Here is a visualization of how chopping off a prefix sum leaves exactly $K$:

```mermaid
flowchart TD
    subgraph Array
        W1["[ 3, 4, 7, 2, -3, 1, 4, 2 ]"]
    end
    
    subgraph Current State
        N1["We are at index 6 (value 4).\nCurrent Running Total (Sum from start) = 18.\nTarget K = 7."]
    end
    
    subgraph Logic
        N2["To get a block that equals 7 at the end,\nwe must chop off a block at the start that equals 11.\n(Because 18 - 7 = 11)"]
    end
    
    subgraph Hash Map Check
        N3["Did the running total ever equal 11 in the past?\nCheck Map: {..., 11: 1, ...}\nYES! The prefix sum was 11 at index 1!"]
        N4["Subarray found from index 2 to 6: [7, 2, -3, 1, 4] = 7!"]
    end
    
    Array --> Current State
    Current State --> Logic
    Logic --> Hash Map Check
    
    style N2 fill:#fff9c4,color:#000
    style N3 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We iterate through the array exactly once. Dictionary lookups and updates in Python are $O(1)$.
- **Space Complexity:** $O(N)$. In the worst case, every single prefix sum is unique, meaning we store $N$ distinct values in the Hash Map.

### Edge Cases Handled Safely
- **Array with negative numbers and zeros:** `[1, -1, 0]`, target $K=0$.
  - Init: `map={0:1}`, `sum=0`, `count=0`
  - `num=1`: `sum=1`, `needed=1-0=1`. Not in map. `map={0:1, 1:1}`.
  - `num=-1`: `sum=0`, `needed=0-0=0`. In map! `count += 1` (now 1). `map={0:2, 1:1}`.
  - `num=0`: `sum=0`, `needed=0-0=0`. In map! `count += 2` (now 3). `map={0:3, 1:1}`.
  - Returns `3`. Correct! (The subarrays are `[1, -1]`, `[-1, 0]`, and `[1, -1, 0]`). The frequency counter handled overlapping zero-sums flawlessly.
- **Empty Array:** Loop skips. Returns `0`. Correct!
