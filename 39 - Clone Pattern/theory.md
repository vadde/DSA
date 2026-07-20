# Pattern 39: Clone Pattern (Deep Copy)

## 👶 Explain Like I'm 5

Imagine you have a complicated spider web of connected Lego pieces (a Graph).
You want to build an EXACT replica of it.
If you just pick up a red Lego from the original web and place it in your new web,
you ruined the original web! (That's a Shallow Copy).

To make a true **Deep Copy**, you need to look at a piece in the original web,
buy a brand new piece that looks exactly like it, and put it in your new web.
But wait! How do you remember which original piece matches which new piece so you
can connect them properly?
You keep a notebook (a Hash Map): "Original Red Lego -> New Red Lego".

---

## 🧩 Core Idea & Pattern Detection

The **Clone Pattern** is all about traversing a pointer-based data structure
(like a Graph or a Linked List with random pointers) and creating a deep copy.
Because the structure can have cycles (loops), if you aren't careful, you will
get stuck in an infinite loop creating infinite new nodes!

### The Golden Rule: The Hash Map
Always use a Hash Map to map `Original Node -> Cloned Node`.
1. When you visit a node, check the Hash Map.
2. If it's already there, just return the cloned node! (This prevents infinite loops).
3. If not, create a new node, put it in the Hash Map immediately, and then
   recursively clone its neighbors/children.

### When to use it:
- "Deep copy" of a Graph.
- "Copy List with Random Pointer".
- Keywords: "clone", "deep copy", "random pointer".

---

## 🔧 Visual Anatomy

Cloning a Linked List with a Random Pointer:

```mermaid
flowchart TD
    A["Original: A"] -->|next| B["Original: B"]
    B -->|random| A
    C["Map: {A: A_clone, B: B_clone}"]
    D["Clone: A_clone"] -->|next| E["Clone: B_clone"]
    E -->|random| D
    
    style C fill:#475569,stroke:#eab308
```

---

## ⏱️ Complexity Analysis

| Scenario | Time | Space |
|----------|------|-------|
| Clone Graph | O(V + E) | O(V) for Hash Map + Call Stack |
| Copy List w/ Random | O(N) | O(N) for Hash Map |

*(Note: Copy List with Random Pointer can also be done in O(1) space by weaving the cloned nodes into the original list, which is a brilliant trick!)*

---

## ✅ Problems in This Pattern

| # | Problem | Difficulty | LeetCode |
|---|---------|------------|----------|
| 1 | Clone Graph | Medium | #133 |
| 2 | Copy List with Random Pointer | Medium | #138 |


## 📦 Prerequisite Data Structures
- Basic understanding of Arrays, Hash Maps, and Clone Pattern fundamentals.


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
def solve_clone_pattern(nums):
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
