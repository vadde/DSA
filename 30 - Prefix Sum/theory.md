# Pattern 30: Prefix Sum

## 👶 Explain Like I'm 5

Imagine keeping track of your money each day.
- Day 1: +$5 (Total: $5)
- Day 2: +$3 (Total: $8)
- Day 3: -$2 (Total: $6)
- Day 4: +$4 (Total: $10)

If someone asks: "How much did you make from Day 2 to Day 4?"
Instead of adding Day 2 + Day 3 + Day 4, you just take:
`Total at Day 4` MINUS `Total at Day 1` = $10 - $5 = $5.
That's the **Prefix Sum**! By keeping a running total, you can find the sum of ANY
slice (subarray) instantly.

---

## 🧩 Core Idea & Pattern Detection

**Prefix Sum Array**: `prefix[i] = prefix[i-1] + nums[i]`
Sum of subarray `nums[i...j]` = `prefix[j] - prefix[i-1]`.

Often paired with a **Hash Map**:
If we are looking for a subarray that sums to `K`, we know:
`Current_Prefix_Sum - Previous_Prefix_Sum = K`
Which means: `Previous_Prefix_Sum = Current_Prefix_Sum - K`

So we store every `prefix_sum` we see in a hash map. At each step, we just check
if `(current_sum - K)` is already in the hash map!

### When to use it:
- Finding subarrays that sum to a specific target.
- Queries about the sum of elements in a range.
- Arrays containing positive AND negative numbers (where Sliding Window fails).
- Keywords: "subarray sum", "sum equals k", "continuous sequence sum".

---

## 🔧 Visual Anatomy

Finding a subarray summing to `K = 7`:

```mermaid
flowchart LR
    A["Index: 0"] --> B["1"]
    B --> C["2"]
    C --> D["3"]
    A -- sum=3 --> B
    B -- sum=4 --> C
    C -- sum=7 --> D
    
    style A fill:#475569
    style B fill:#3b82f6
    style C fill:#3b82f6
    style D fill:#3b82f6
```
Current prefix sum at D is `14`. Target `K = 7`.
Does `14 - 7 = 7` exist in our past prefixes? Yes, at index 0 (sum=3 was past prefix, wait... no, if prefix sum at 0 is 3, at D is 14... 14 - 7 = 7. If we saw a prefix sum of 7, the subarray AFTER it up to D sums to 7).

---

## ⏱️ Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Create Prefix Array | O(N) | O(N) (or O(1) if running sum) |
| Range Sum Query | O(1) | O(1) |
| Find Subarray Sum=K | O(N) | O(N) for Hash Map |

---

## ✅ Problems in This Pattern

| # | Problem | Difficulty | LeetCode |
|---|---------|------------|----------|
| 1 | Subarray Sum Equals K | Medium | #560 |
| 2 | Max Size Subarray Sum Equals K | Medium | #325 |
| 3 | Contiguous Array (Equal 0s and 1s) | Medium | #525 |
| 4 | Range Sum Query 2D - Immutable | Medium | #304 |
| 5 | Path Sum III (Tree + Prefix Sum) | Medium | #437 |


## 📦 Prerequisite Data Structures
- Basic understanding of Arrays, Hash Maps, and Prefix Sum fundamentals.


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
def solve_prefix_sum(nums):
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
