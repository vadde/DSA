# Pattern 37: MO's Algorithm (Square Root Decomposition)

## 👶 Explain Like I'm 5

Imagine you have a long bookshelf. Someone keeps asking you questions like:
"How many *different* books are there between shelf 2 and shelf 8?"
"How many between shelf 1 and 3?"
"How many between shelf 5 and 9?"

If you walk back and forth for every question, you'll get very tired.
What if you collected ALL the questions first (Offline Queries), sorted them
so you answer questions about shelf 1-3, then 2-8, then 5-9?
By slightly moving your "start" and "end" pointers, you reuse the work from the
previous question!
**MO's Algorithm** perfectly sorts these questions into "Blocks" so your pointers
move the absolute minimum distance possible.

---

## 🧩 Core Idea & Pattern Detection

MO's Algorithm is used for **Offline Range Queries**.
"Offline" means you are given all the queries up front and you don't have to answer
them in the order they were asked.

### How it works:
1. Divide the array of size `N` into blocks of size `sqrt(N)`.
2. Sort the queries.
   - Primary sort: The block index of the Left pointer (`L // sqrt(N)`).
   - Secondary sort: The Right pointer (`R`).
3. Maintain two pointers, `current_L` and `current_R`, and a sliding window state.
4. For each sorted query, `add` or `remove` elements by moving `current_L` and `current_R`
   until they match the query's `L` and `R`.

### When to use it:
- Processing many range queries where `add(element)` and `remove(element)` are O(1).
- Questions asking for "Distinct elements in range [L, R]" or "Mode in range [L, R]".
- Keywords: "queries", "offline", "distinct elements in subarray".

---

## 🔧 Visual Anatomy

Sorting Queries into Blocks:

```mermaid
flowchart TD
    A["Array: [0, 1, 2, 3, 4, 5, 6, 7, 8], Block size = 3"] --> B["Block 0: [0, 1, 2]"]
    A --> C["Block 1: [3, 4, 5]"]
    A --> D["Block 2: [6, 7, 8]"]
    B --> E["Queries starting in Block 0 are sorted by R"]
    E --> F["Q1: [1, 3] -> Q2: [2, 6] -> Q3: [0, 8]"]
    C --> G["Queries starting in Block 1 are sorted by R"]
    G --> H["Q4: [4, 5] -> Q5: [5, 8]"]
```

---

## ⏱️ Complexity Analysis

| Scenario | Time | Space |
|----------|------|-------|
| MO's Algorithm | O((N + Q) * sqrt(N)) | O(N) |

The right pointer moves continuously forward inside a block.
The left pointer only moves `sqrt(N)` steps per query.

---

## ✅ Problems in This Pattern

| # | Problem | Difficulty | Note |
|---|---------|------------|------|
| 1 | Range Sum Query (MO's Intro) | Medium | Illustrates the pointers |
| 2 | Range Distinct Elements | Hard | The classic use-case |


## 📦 Prerequisite Data Structures
- Basic understanding of Arrays, Hash Maps, and MO's Algorithm fundamentals.


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
def solve_mo's_algorithm(nums):
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
