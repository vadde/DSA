# 🚶‍♂️ Walkthrough: Find the Median of a Number Stream

## 👶 Explain Like I'm 5
You are a teacher receiving a constant stream of test scores from your students.
Every time a new score comes in, the principal bursts into the room and yells: *"WHAT IS THE MEDIAN SCORE RIGHT NOW?!"*
If you have to sort the entire stack of papers every single time he asks, you will never get any work done.

Instead, you put two baskets on your desk:
1. The **"Bottom Half"** basket. (It only shows you the LARGEST score inside it).
2. The **"Top Half"** basket. (It only shows you the SMALLEST score inside it).

When a new score comes in, you drop it into the Bottom Half basket.
But what if that score was a 100%? It belongs in the Top Half!
So, you immediately grab the largest score from the Bottom Half basket and throw it into the Top Half basket. This perfectly filters the scores!
Finally, if the Top Half basket ever gets fuller than the Bottom Half basket, you grab its smallest score and throw it back into the Bottom Half basket. This guarantees the Bottom Half is always exactly equal to, or exactly 1 paper larger than, the Top Half.

When the principal yells, you just look at the top paper in both baskets!

## 🎯 Core Strategy
This is the foundational **Two Heaps** pattern. It allows us to dynamically track the median of a growing stream of numbers in $O(\log N)$ time per insertion and $O(1)$ time to get the median.

1. **State Tracking**:
   - `max_heap`: Stores the smaller half of the numbers. Python only has Min Heaps natively, so we simulate a Max Heap by pushing `-num`.
   - `min_heap`: Stores the larger half of the numbers.
2. **`insert_num(num)`**:
   - **Step 1 (Insert)**: Always push to the `max_heap` first (negate the number for Python: `heapq.heappush(max_heap, -num)`).
   - **Step 2 (Filter)**: The number we just added might actually belong in the top half. Pop the maximum element from `max_heap` (remember to negate it back!) and push it onto `min_heap`.
   - **Step 3 (Balance)**: We maintain an invariant: `max_heap` is allowed to have at most 1 more element than `min_heap`. If `len(min_heap) > len(max_heap)`, pop from `min_heap` and push it (negated) back to `max_heap`.
3. **`find_median()`**:
   - If both heaps are the same size (even total numbers), the median is the average of the top elements of both heaps: `(-max_heap[0] + min_heap[0]) / 2.0`.
   - If `max_heap` is larger (odd total numbers), the median is simply the top element of `max_heap`: `-max_heap[0] / 1.0`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Action Stream**: Insert 3, Insert 1, Insert 5, Insert 4

### Insert 3
- Step 1: Push `-3` to `max_heap`. `max_heap = [-3]`.
- Step 2: Pop `-3` (becomes `3`), push to `min_heap`. `max_heap = []`, `min_heap = [3]`.
- Step 3: `min_heap` (size 1) > `max_heap` (size 0). Pop `3`, push `-3` to `max_heap`.
- **Result**: `max_heap = [-3]`, `min_heap = []`. Median = 3.0.

### Insert 1
- Step 1: Push `-1` to `max_heap`. `max_heap = [-1, -3]` (Note: -1 is at the top because it's the largest mathematically).
- Step 2: Pop `-1` (becomes `1`), push to `min_heap`. `max_heap = [-3]`, `min_heap = [1]`.
- Step 3: Sizes are equal (1 == 1). No rebalancing needed.
- **Result**: `max_heap = [-3]`, `min_heap = [1]`. Median = (-(-3) + 1)/2 = 2.0.

### Insert 5
- Step 1: Push `-5` to `max_heap`. `max_heap = [-3, -5]`.
- Step 2: Pop `-3` (becomes `3`), push to `min_heap`. `max_heap = [-5]`, `min_heap = [1, 3]`.
- Step 3: `min_heap` (size 2) > `max_heap` (size 1). Pop `1`, push `-1` to `max_heap`. `max_heap = [-1, -5]`, `min_heap = [3]`.
- **Result**: `max_heap = [-1, -5]`, `min_heap = [3]`. Median = 1.0 (Wait, 1 is top of max_heap). Wait, sizes: `max_heap` has size 2, `min_heap` has size 1. Median is `-max_heap[0] = 1.0`. But numbers are 1, 3, 5, median should be 3! Let's re-trace.

*Wait! Re-trace Step 2 for Insert 5:*
- `max_heap` is `[-3]`. `min_heap` is `[1]`. (Oops! In Python Min Heap, 1 is smaller than 3, so `min_heap` has 1 at the top, wait, wait...)
Actually, when we inserted 1:
- `max_heap = [-3]`, `min_heap = []`.
- Insert 1: push `-1` to `max_heap`. `max_heap` is now `[-1, -3]`.
- Pop `max_heap`: pops `-1` (becomes 1). Push 1 to `min_heap`. `max_heap = [-3]`, `min_heap = [1]`.
- Wait, the smaller numbers belong in `max_heap`. The larger numbers belong in `min_heap`.
If numbers are 1 and 3. `max_heap` should have 1, `min_heap` should have 3.
In the trace above: `max_heap` has 3, `min_heap` has 1. This is BACKWARDS!

Why did it go backward? Let's trace correctly:
`Insert 3`: `max_heap = [-3]`, `min_heap = []`.
`Insert 1`:
- Push `-1` to `max_heap`. `max_heap` becomes `[-1, -3]`. (Note: -1 is > -3, so in Python min-heap, -3 is at the root. Ah! `heapq` pops the smallest element, which is `-3`. NOT `-1`. Negating `-3` gives `3`!)
- Pop `max_heap`: pops `-3` (becomes `3`). Push `3` to `min_heap`. `max_heap = [-1]`, `min_heap = [3]`.
- Balancing: Sizes equal.
- Result: `max_heap = [-1]`, `min_heap = [3]`. Median = (-(-1) + 3) / 2 = (1+3)/2 = 2.0. Correct!

Let's do `Insert 5`:
- `max_heap = [-1]`, `min_heap = [3]`.
- Push `-5` to `max_heap`. `max_heap = [-5, -1]`. (Smallest is `-5`).
- Pop `max_heap`: pops `-5` (becomes `5`). Push `5` to `min_heap`. `max_heap = [-1]`, `min_heap = [3, 5]`. (Smallest in `min_heap` is `3`).
- Balancing: `min_heap` (size 2) > `max_heap` (size 1). Pop `min_heap`: pops `3`. Push `-3` to `max_heap`. `max_heap = [-3, -1]`, `min_heap = [5]`.
- Result: `max_heap` root is `-3` (so `3`). `min_heap` root is `5`. Total sizes: 3. Median = `3`. Correct!

## 📊 Visual Diagram
Here is how the numbers logically sit between the two heaps, with the tops of the heaps acting as the "gateway" to the median:

```mermaid
flowchart TD
    subgraph Stream
        S1["Numbers: 1, 3, 4, 5"]
    end
    
    subgraph max_heapBottomHalf ["max_heap (Bottom Half)"]
        MH1((3))
        MH2((1))
        MH1 --- MH2
        note1["Python: [-3, -1]\nRoot is -3 (Max is 3)"]
    end
    
    subgraph min_heapTopHalf ["min_heap (Top Half)"]
        mH1((4))
        mH2((5))
        mH1 --- mH2
        note2["Python: [4, 5]\nRoot is 4 (Min is 4)"]
    end
    
    MH1 == Average = 3.5 ==> mH1
    
    style MH1 fill:#ffcdd2,color:#000
    style MH2 fill:#e3f2fd,color:#000
    
    style mH1 fill:#c8e6c9,color:#000
    style mH2 fill:#e3f2fd,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** 
  - `insert_num()`: $O(\log N)$ because pushing and popping from a heap takes logarithmic time. We do this at most 3 times per insertion.
  - `find_median()`: $O(1)$ because we just look at the `[0]` index of the arrays.
- **Space Complexity:** $O(N)$ because the heaps will collectively store all $N$ numbers exactly once.

### Edge Cases Handled Safely
- **Single Element:** First insertion leaves `max_heap` with size 1 and `min_heap` with size 0. Median returns `max_heap[0]` divided by 1.0. Correct!
- **Negative Numbers:** The negation trick `heapq.heappush(max_heap, -num)` works perfectly even if `num` is already negative (it becomes positive in the heap, maintaining the reverse-sorting logic).
- **Duplicate Numbers:** Heaps handle duplicates effortlessly, they just settle into adjacent layers in the binary tree.
