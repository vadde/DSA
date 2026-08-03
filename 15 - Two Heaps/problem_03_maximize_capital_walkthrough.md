# 🚶‍♂️ Walkthrough: Maximize Capital

## 👶 Explain Like I'm 5
You are an investor with some starting money (Capital `w`).
There are many projects you can invest in. Every project costs a certain amount of Capital to start, and gives you a certain amount of Profit.
You only have time to do `k` projects.
You want to make the absolute most money possible!

If you just pick the project with the highest profit, you might not have enough money to afford it yet.
So, you use Two Sorting Hats (Heaps):
1. The **"Too Expensive"** Hat (Min Heap): You put ALL projects in here, sorted by how much they COST.
2. The **"Affordable"** Hat (Max Heap): You put projects you can afford in here, sorted by how much PROFIT they make.

**Step 1:** You look at the "Too Expensive" hat. For any project that you can now afford (because `Cost <= your Capital w`), you take it out and throw it into the "Affordable" hat!
**Step 2:** You reach into the "Affordable" hat and pull out the SINGLE project that gives the most Profit. You do it, and you add the Profit to your Capital `w`!

Now that you have more money, maybe you can afford new projects! So you repeat Step 1 and Step 2 until you've done `k` projects.

## 🎯 Core Strategy
This is a standard **Two Heaps** pattern, but instead of tracking a median, we use them as "waitlists" for projects based on two different sorting criteria (Cost vs Profit).

1. **State Tracking**:
   - `min_capital_heap`: Min Heap storing `(capital_cost, profit)`. This naturally sorts the cheapest projects to the top.
   - `max_profit_heap`: Max Heap storing `(-profit, capital_cost)`. This naturally sorts the most profitable projects to the top. (Negate profit for Python's Min Heap).
2. **Initialization**:
   - Loop through all projects and push them onto `min_capital_heap`.
3. **The `k` Iterations**:
   - Loop `k` times (since we can do at most `k` projects):
     - **Transfer Phase**: While `min_capital_heap` is not empty AND the top project's cost is `<= w`:
       - Pop it.
       - Push it into `max_profit_heap` as `(-profit, cost)`.
     - **Action Phase**: 
       - If `max_profit_heap` is empty, it means we can't afford ANY projects! Break the loop early.
       - Otherwise, pop the top project from `max_profit_heap`.
       - Add its profit to `w`. (Because we negate profit to push it, negate it again to add it back).
4. Return the final Capital `w`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `k = 2`, `w = 0`, `profits = [1, 2, 3]`, `capital = [0, 1, 1]`

### Initialization
- Zip them up and push to `min_capital_heap`: 
  `[(0, 1), (1, 2), (1, 3)]`. (Sorted by cost).

### Iteration 1 (of 2)
- Current Capital `w = 0`.
- **Transfer**: What can we afford? Top of `min_capital_heap` is `(0, 1)`. `0 <= 0`!
  - Pop `(0, 1)`. Push `(-1, 0)` to `max_profit_heap`.
  - Next top is `(1, 2)`. Cost `1 > 0`. Stop transferring.
- **Action**: `max_profit_heap` has `[(-1, 0)]`.
  - Pop it! Profit is `-(-1) = 1`.
  - `w = 0 + 1 = 1`.

### Iteration 2 (of 2)
- Current Capital `w = 1`.
- **Transfer**: What can we afford now? Top of `min_capital_heap` is `(1, 2)`. `1 <= 1`!
  - Pop `(1, 2)`. Push `(-2, 1)` to `max_profit_heap`.
  - Next top is `(1, 3)`. `1 <= 1`!
  - Pop `(1, 3)`. Push `(-3, 1)` to `max_profit_heap`.
  - `min_capital_heap` is empty. Stop transferring.
- **Action**: `max_profit_heap` has `[(-3, 1), (-2, 1)]`.
  - Pop the top (most profitable)! It's `(-3, 1)`. Profit is `3`.
  - `w = 1 + 3 = 4`.

Return `w = 4`.

## 📊 Visual Diagram
Here is how the projects flow from the initial list, through the heaps, and into your pocket:

```mermaid
flowchart TD
    subgraph InitialState [Initial State]
        P1["Cost 0, Profit 1"]
        P2["Cost 1, Profit 2"]
        P3["Cost 1, Profit 3"]
        W["Capital = 0"]
    end
    
    subgraph Heaps
        MIN["min_capital_heap\n["(0,1), (1,2), (1,3)"]"]
        MAX["max_profit_heap\n[ ]"]
        MIN -- "Afford (Cost <= W)?" --> MAX
    end
    
    subgraph ExecutionLoop [Execution Loop]
        MAX -- "Do most profitable" --> POCKET["Add to Capital W"]
        POCKET -. "Loop K times" .-> Heaps
    end

InitialState --> MIN

styleMINfill:#ffcdd2,color:#000
    style MAX fill:#c8e6c9,color:#000
    style POCKET fill:#bbdefb,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log N + K \log N)$. Building the initial `min_capital_heap` takes $O(N \log N)$. In the worst case, all $N$ projects are transferred to `max_profit_heap` ($O(N \log N)$), and we extract $K$ projects from it ($O(K \log N)$). 
- **Space Complexity:** $O(N)$ for the two heaps storing all projects.

### Edge Cases Handled Safely
- **Cannot Afford Anything Initially:** If `w = 0` and the cheapest project costs `1`, the transfer phase doesn't run. `max_profit_heap` is empty. The `if not max_profit_heap: break` line catches it safely and returns `0`.
- **Run Out of Projects:** If $K=10$ but there are only 3 projects, the `if not max_profit_heap: break` line will gracefully end the loop after the 3rd project is completed.
- **Multiple Projects with Same Profit:** Python's `heapq` compares the full tuple. If profits are tied `(-3, 1)` and `(-3, 2)`, it will fall back to comparing the costs `1 < 2`. This is perfectly fine (and actually optimal: picking the cheaper one first).
