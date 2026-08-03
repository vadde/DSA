# 🚶‍♂️ Walkthrough: Range Sum Query - Mutable (BIT Version)

## 👶 Explain Like I'm 5
This is the same problem as the Segment Tree one (finding the sum of a range, and updating numbers). But this time, we use a **Binary Indexed Tree (BIT)**, also called a Fenwick Tree.
A Segment Tree uses `4 * N` memory and requires writing lots of recursive code. A BIT uses exactly `N + 1` memory and is incredibly short to write!
How does it work? Every number in the array is in charge of a specific "chunk" of numbers based on its binary representation. 
To update a number, we add the change (delta) to it, and then we tell all its "bosses" up the chain about the change.
To get a sum from index 1 to 5, we just ask index 5 for its chunk, then ask its previous chunk, until we reach 0. To get a range like [3, 5], we just do: `Sum(5) - Sum(2)`!

## 🎯 Core Strategy
**Binary Indexed Tree (Fenwick Tree)**.

1. **Initialization**: Create a 1-indexed array `tree` of size `N + 1`, initially all 0s.
2. **The LSB (Lowest Significant Bit)**: The magic formula `i & (-i)` gives the rightmost 1-bit of `i`. 
   - Moving UP the tree (for updates): `i += i & (-i)`
   - Moving DOWN the tree (for querying prefix sums): `i -= i & (-i)`
3. **Update**: Instead of updating to a new absolute value, we find the difference (`delta = new_val - old_val`). We add this `delta` to `tree[i]`, and then jump to the next affected index `i += i & (-i)` until we exceed the array size.
4. **Query**: To get the sum of elements from 0 to `i`, we add `tree[i]` to our total, and jump to `i -= i & (-i)` until `i` is 0. 
5. **Range Sum**: `sumRange(L, R)` is simply `query(R + 1) - query(L)`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `nums = [1, 3, 5]`
Initialize BIT size 4 (indices 0 to 3): `tree = [0, 0, 0, 0]`

**Build**:
- Add 1 at index 1: `update(1, 1)`
  - `tree[1] += 1` -> `[0, 1, 0, 0]`
  - `1 + (1 & -1)` = 1 + 1 = 2. `tree[2] += 1` -> `[0, 1, 1, 0]`
  - `2 + (2 & -2)` = 2 + 2 = 4 (out of bounds).
- Add 3 at index 2: `update(2, 3)`
  - `tree[2] += 3` -> `[0, 1, 4, 0]`
  - `2 + 2` = 4 (out of bounds).
- Add 5 at index 3: `update(3, 5)`
  - `tree[3] += 5` -> `[0, 1, 4, 5]`
  - `3 + (3 & -3)` = 3 + 1 = 4 (out of bounds).

**Query(2)** (Sum up to original index 1, BIT index 2):
- `total += tree[2]` (4).
- `i = 2 - (2 & -2) = 0`. Loop ends. Result = **4**.

**Range(0, 2)** (Sum of entire array):
- `query(3) - query(0)`
- `query(3)`:
  - `total += tree[3]` (5). `i` becomes 2.
  - `total += tree[2]` (4). `i` becomes 0. Total = **9**.
- `query(0)` = 0.
- Result: **9**. ✅

## 📊 Visual Diagram

```mermaid
flowchart TD
    subgraph UpdateIDelta ["Update(i, delta)"]
    A["i < len(tree)?"] -->|YES| B["tree[i] += delta"]
    B --> C["i += i & (-i)"]
    C --> A
end

subgraphQuery(i)
    D["total = 0"] --> E["i > 0?"]
    E -->|YES| F["total += tree[i]"]
    F --> G["i -= i & (-i)"]
    G --> E
E -->|NO| H["Return total"]
    end
    
    style B fill:#fff9c4,color:#000
    style F fill:#e3f2fd,color:#000
```

## 🛑 Complexity
- **Time:** $O(N \log N)$ to build initially. $O(\log N)$ for updates and queries.
- **Space:** $O(N)$ for the `tree` array. (Specifically $N+1$, exactly one quarter of the memory required for a standard Segment Tree!).
