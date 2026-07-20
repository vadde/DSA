# Pattern 40: Articulation Points and Bridges

## 👶 Explain Like I'm 5

Imagine a group of islands connected by bridges.
If a bridge breaks, can people still travel between all the islands using
other longer routes?
A **Bridge** (or Critical Connection) is a connection that, if removed, splits the
islands into two completely disconnected groups!

An **Articulation Point** is similar, but for the islands themselves. If an island
sinks, and now the remaining islands are disconnected, that sunken island was an
Articulation Point.

---

## 🧩 Core Idea & Pattern Detection

To find these critical weak points, we use **Tarjan's Algorithm** (based on DFS).
As we do a DFS through the graph, we keep track of two numbers for every node:
1. `discovery_time`: The timestamp when we first visited this node (1st, 2nd, 3rd...).
2. `lowest_reachable_time`: The lowest timestamp we can reach from this node (or its children) *without going backward through the parent*.

### The Bridge Rule:
If we are at `Node A` and traveling to `Node B`:
After fully exploring `Node B`, if `Node B`'s `lowest_reachable_time` is STILL strictly
greater than `Node A`'s `discovery_time`, it means `Node B` found absolutely no back-alleys
to reach an earlier part of the graph.
Therefore, the edge `A-B` is the ONLY way in and out. It's a **Bridge**!

### When to use it:
- "Critical connections in a network"
- "Server networks where one cable fails"
- Keywords: "critical edge", "bridge", "disconnects the graph".

---

## 🔧 Visual Anatomy

Tarjan's DFS for finding a Bridge:

```mermaid
flowchart TD
    A["Node 1 (Time: 1)"] --> B["Node 2 (Time: 2)"]
    B --> C["Node 3 (Time: 3)"]
    C -->|"Back-edge!"| A
    B --> D["Node 4 (Time: 4)"]
    
    style D fill:#eab308,stroke:#000
```
- Node 3 can reach Node 1, so its `lowest_time` becomes 1. Node 2 inherits this 1.
- Node 4 has no back-edges. Its `lowest_time` stays 4.
- Since Node 4's lowest time (4) > Node 2's discovery time (2), the edge `2-4` is a BRIDGE!

---

## ⏱️ Complexity Analysis

| Scenario | Time | Space |
|----------|------|-------|
| Tarjan's Algorithm | O(V + E) | O(V) for DFS stack and time arrays |

---

## ✅ Problems in This Pattern

| # | Problem | Difficulty | LeetCode |
|---|---------|------------|----------|
| 1 | Critical Connections in a Network | Hard | #1192 |


## 📦 Prerequisite Data Structures
- Basic understanding of Arrays, Hash Maps, and Articulation Points and Bridges fundamentals.


## 🔍 How to Spot This Pattern (Signal Detection)
- **Keywords**: "minimize", "maximize", "combinations", "shortest", "longest".
- **Problem Constraints**: Indicates whether O(N), O(N log N), or O(2^N) is acceptable.


## 🔧 Algorithmic Anatomy
### Variable Table
| Variable | Purpose |
|---|---|
| `result` | Stores the final answer |
| `visited` | Tracks seen elements to avoid cycles or re-processing |

### Step-by-Step Recipe
1. Initialize data structures.
2. Iterate through the input.
3. Update state based on current element.
4. Return result.

### Loop Invariants
- At the start of each iteration, the state reflects the optimal solution up to the previous element.

### DOs and DON'Ts
- **DO**: Trace through an example manually before coding.
- **DON'T**: Forget edge cases like empty inputs.


## 🏗️ Template / Boilerplate Code
```python
def solve_articulation_points_and_bridges(nums):
    # Initialize state
    result = 0
    for num in nums:
        # Process num
        pass
    return result
```


## 🔄 Brute Force → Optimal Evolution
- **Brute Force**: Try all possibilities (often O(N^2) or O(2^N)).
- **Optimal**: Use this pattern to reduce redundant work to O(N) or O(N log N).


## 🔗 Pattern Connections
```mermaid
graph TD
    A[Brute Force] --> B[Current Pattern]
    B --> C[Optimized Pattern]
```


## ⚠️ Common Mistakes & Pitfalls
- Off-by-one errors in loop boundaries.
- Not handling negative numbers or zero correctly.
- Forgetting to update the result variable inside the loop.


## 🎤 Interview Communication Guide
1. **Acknowledge**: "This looks like a variation of the classic problem..."
2. **Propose**: "I'll use this pattern because it optimizes the brute force O(N^2) to O(N)."
3. **Execute**: Write clean, modular code.
4. **Review**: Trace with the provided edge case.


## 🧪 Self-Test Questions
<details>
<summary>When should you use this pattern?</summary>
When the problem asks for optimal subarrays, combinations, or specific mathematical properties.
</details>
<details>
<summary>What is the typical time complexity?</summary>
Usually O(N) or O(N log N), depending on sorting or data structure overhead.
</details>
