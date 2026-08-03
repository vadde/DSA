# 🚶‍♂️ Walkthrough: Shortest Subarray with Sum at Least K

## 👶 Explain Like I'm 5
Imagine a board game where moving forward usually gets you points, but some spaces actually **LOSE** you points (they are negative numbers!). You want to find the shortest path that scores at least $K$ points.

Normally, we'd use a sliding window: just keep expanding to get more points, and shrink when we have enough. But because of the negative numbers, this breaks! Adding a new space might *lower* your score, and removing a space might *raise* it! It's completely unpredictable.

To fix this, we write down our "total score from the start line" at every single step. This is called a **Prefix Sum**.
To find the score of any path, we just look at our current total score, and subtract the total score from where we started the path.
Then, we use a smart "VIP Line" (a Deque) to remember the **lowest scores** we've seen recently. We always want to subtract a *low* score to get a *high* final score, and we want to start as close to our current position as possible to keep the path short!

## 🎯 Core Strategy
This is an advanced technique combining **Prefix Sums** and a **Monotonic Deque**.
1. Create a `prefix_sum` array. `prefix_sum[i]` is the sum of all elements before `i`. 
   *Magic Formula: `Sum(i to j) = prefix_sum[j] - prefix_sum[i]`.*
2. Initialize an empty deque `dq` to store the INDICES of the prefix sum array.
3. Iterate `i` through the `prefix_sum` array:
   - **Check Valid Window (Pop Left)**: If the current prefix sum minus the prefix sum at the front of the deque is $\ge K$, we found a valid subarray! 
     Record the length `i - dq[0]`. Then `popleft()`. Why? Because any future `i` paired with this `dq[0]` will only result in a *longer* subarray, so we never need `dq[0]` again.
   - **Optimize Starting Points (Pop Right)**: If the current prefix sum is $\le$ the prefix sum at the back of the deque, we `pop()` from the back. Why? Because the current index `i` is both *closer* (makes shorter subarrays) and *smaller* (easier to reach target $K$ when subtracted). The older, larger prefix sum is completely outclassed and useless.
   - Add the current index `i` to the deque.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `nums = [2, -1, 2]`, `k = 3`
1. Build `prefix_sum`: `[0, 2, 1, 3]` (Indices 0 to 3)
2. `dq = []`, `min_len = infinity`

| Step `i` | `prefix[i]` | Deque Action: Pop Left (Valid?) | Deque Action: Pop Right (Optimize) | Deque State | `min_len` |
|----------|-------------|---------------------------------|------------------------------------|-------------|-----------|
| `0` | `0` | No. (Deque empty) | No. | `[0]` | `inf` |
| `1` | `2` | No. `2 - prefix[0] (0) = 2 < 3` | No. `2 > prefix[0] (0)` | `[0, 1]` | `inf` |
| `2` | `1` | No. `1 - prefix[0] (0) = 1 < 3` | Yes! `1 <= prefix[1] (2)`. Pop `1`! | `[0, 2]` | `inf` |
| `3` | `3` | **Yes!** `3 - prefix[0] (0) = 3 >= 3`.<br>Record `3 - 0 = 3`. Popleft! | No. `3 > prefix[2] (1)` | `[2, 3]` | `3` |

Result: `min_len = 3`.

## 📊 Visual Diagram
Here is how the Monotonic Deque optimizes starting points:

```mermaid
flowchart TD
    subgraph State1 [State 1: i=1. prefix=2]
        W1["Deque: [idx 0(val 0), idx 1(val 2)]"]
    end
    
    subgraph State2 [State 2: i=2. prefix=1]
        W2["New prefix is 1."]
        N2["1 is a BETTER starting point than 2!\nIt is mathematically smaller and physically closer."]
        A2["Pop idx 1! Add idx 2!"]
    end
    
    subgraph State3 [State 3: Result]
        W3["Deque: [idx 0(val 0), idx 2(val 1)]"]
    end

State1 --> State2
State2 --> State 3
    
    style W2 fill:#ffcdd2,color:#000
    style A2 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We build the prefix sum array in $O(N)$. Then we iterate through the prefix sum array. Every index is pushed into the deque exactly once, and popped from the deque at most once. Therefore, the inner `while` loops do not cause $O(N^2)$ behavior. The total time is strictly $O(N)$.
- **Space Complexity:** $O(N)$ to store the `prefix_sum` array of size $N+1$ and the deque which can grow up to size $N+1$ in the worst case (if all numbers are positive).

### Edge Cases Handled Safely
- **Negative numbers:** Handled flawlessly. The `while prefix_sum[i] <= prefix_sum[dq[-1]]: dq.pop()` logic specifically kicks in when a negative number causes the prefix sum to drop. It immediately recognizes that this new, lower sum is an incredibly valuable starting point for future calculations and clears out the worse options.
- **Impossible target:** If no subarray reaches $K$, the first `while` loop (which pops left) never triggers. `min_length` remains `infinity`, and the function safely returns `-1` at the end.
