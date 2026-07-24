# 🚶‍♂️ Walkthrough: Sliding Window Median

## 👶 Explain Like I'm 5
Remember the Two Heaps we used to find the Median of a stream of scores?
What if the principal changes the rules: *"I only care about the median of the LAST 3 SCORES!"*
As the 4th score comes in, the 1st score "slides" out of the window and must be thrown in the trash.

But here's the problem: Our magical sorting hats (Heaps) are only designed to pull numbers out of the very **TOP** of the hat. What if the score we need to throw away is buried deep at the bottom of the hat? We can't easily dig it out!

So, we use a trick called **"Lazy Deletion"**.
We keep a "Trash List" (a Hash Map). When a score leaves the window, we just write it down on the Trash List and leave the actual paper inside the hat!
Whenever we go to check the Top of the hat, we first look at the top paper and ask: *"Wait, is this number on the Trash List?"*
If yes, we finally pull it out, throw it away, cross it off the Trash List, and check the NEXT paper.
We keep pulling trash out of the top until we see a clean, valid number!

## 🎯 Core Strategy
This combines **Sliding Window** with **Two Heaps** and **Lazy Deletion**.

1. **State Tracking**:
   - `max_heap` (bottom half) and `min_heap` (top half).
   - `trash`: Hash Map counting how many times a number should be deleted (`num -> count`).
   - `max_size` and `min_size`: Integer counters of how many *valid* numbers are currently in each heap (ignoring the buried trash).
2. **`insert(num)`**: 
   - Push to `max_heap`, pop top, push to `min_heap`. Update `min_size += 1`.
   - Rebalance sizes if needed.
3. **`remove(old_num)`**:
   - When window exceeds size $K$, increment `trash[old_num] += 1`.
   - Determine which heap `old_num` is buried in. If `old_num <= -max_heap[0]`, it's in `max_heap` -> `max_size -= 1`. Else, it's in `min_heap` -> `min_size -= 1`.
4. **Rebalance Again**:
   - Because we just logically removed a number, the valid sizes might be unbalanced!
   - If `max_size` is too big or too small, transfer an element from one heap to the other.
   - **Crucial**: Before you pop an element to transfer it, you MUST run `clean_heap_top()` on that heap. You can't transfer a piece of trash to the other heap!
5. **Get Median**:
   - Run `clean_heap_top()` on both heaps so the tops are guaranteed to be real, valid numbers.
   - Return the median just like in the Data Stream problem.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `nums = [1, 3, -1, -3]`, `k = 3`

### Insert 1, 3, -1 (First Window)
*(Skipping inner balancing steps for brevity)*
- `max_heap` has `[-1]`, `min_heap` has `[3]`, `1` was moved around.
- Ultimately: `max_heap` valid elements: `[-1, 1]`. (Wait, `-1` is smaller than `1`. So `max_heap` has `-1, 1`. Root is `1`? No, python max_heap negates. `-1` negated is `1`. Root is `-(-1) = 1`? Let's stick to logical view).
- Logical View: `max_heap = [1, -1]`. `min_heap = [3]`. 
- `max_size = 2`, `min_size = 1`.
- Window size is 3. Median = `max_heap[0] = 1`. Result: `[1]`.

### Insert -3, Remove 1 (Slide Window)
- **Insert -3**: 
  - `max_heap` gets `-3`. Moves things around. `min_heap` gets updated.
  - Logical: `max_heap = [1, -1, -3]`, `min_heap = [3]`.
- **Remove 1**: 
  - `trash = {1: 1}`.
  - `1 <= 1` (Top of max_heap). So it's in `max_heap`.
  - `max_size -= 1`. Now `max_size = 2`, `min_size = 1`.
  - Sizes are balanced (2 is just 1 more than 1).
- **Get Median**:
  - `clean_heap_top(max_heap)`: The top of `max_heap` is `1`!
  - `1` is in `trash`! Count is `1 > 0`.
  - Pop `1` from `max_heap`! Decrement trash count `trash[1] = 0`.
  - New top of `max_heap` is `-1`. Not in trash. Stop cleaning.
  - Median = `max_heap[0] = -1`. Result: `[1, -1]`.

## 📊 Visual Diagram
Here is how Lazy Deletion works when the trash floats to the top:

```mermaid
flowchart TD
    subgraph max_heap State
        T1(("1\n(TRASH)")) --- N1(("-1\n(Valid)"))
        T1 --- N3(("-3\n(Valid)"))
        note1["max_heap physically has 3 items.\nBut max_size = 2."]
    end
    
    subgraph clean_heap_top
        CHECK["Top is 1. Check trash dict:\ntrash[1] == 1"] --> POP["Pop 1!\ntrash[1] = 0"]
        POP --> CHECK2["New Top is -1.\ntrash[-1] == 0.\nDone!"]
    end
    
    max_heap State --> clean_heap_top
    
    style T1 fill:#ffcdd2,color:#000,stroke:#d32f2f,stroke-width:4px
    style N1 fill:#c8e6c9,color:#000
    style N3 fill:#c8e6c9,color:#000
    style POP fill:#ff9800,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log K)$. Every number is pushed to the heap once and popped at most once. The heaps are constrained to size $O(K)$ because we continually pop elements when they reach the top if they are in the trash.
- **Space Complexity:** $O(K)$. The heaps store at most $K + \text{trash elements}$. Since trash elements are popped when they reach the top, the heap sizes generally hover around $O(K)$. The `trash` dictionary also uses $O(K)$ space.

### Edge Cases Handled Safely
- **Duplicate Elements:** The `trash` dictionary correctly counts *frequencies* of numbers to be deleted (`trash[old_num] += 1`). If we add two `5`s and remove one `5`, `trash[5]` goes from `1` to `0`, and only one `5` is lazily deleted.
- **Trash Never Reaches Top:** If a number is so small (or so large) it gets buried at the absolute bottom of a heap and never reaches the top to be lazily deleted, that's perfectly fine! It doesn't affect the top of the heap, so it doesn't affect our median calculations. It will just waste a tiny bit of space until the program ends.
