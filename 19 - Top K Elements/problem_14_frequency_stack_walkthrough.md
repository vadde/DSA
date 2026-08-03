# 🚶‍♂️ Walkthrough: Frequency Stack

## 👶 Explain Like I'm 5
You are designing a magic box. You can put numbers into it (`push`), and you can ask it to give you a number back (`pop`).
Normally, a box gives you the LAST thing you put in (that's a normal Stack).
But this magic box gives you the **MOST POPULAR** thing inside it! (The most frequent).
If there is a tie (e.g., both `5` and `7` are inside the box twice), it gives you the one that was put in **MOST RECENTLY**.

How do we build this? We need three things to decide who wins:
1. **Frequency** (Higher wins)
2. **Sequence / Age** (Newer wins)

So, we use a **Max-Heap**! But what do we put in the Max-Heap?
We put a tuple: `(-frequency, -sequence_number, number)`.
- The first thing the heap looks at is `frequency`. The highest (most negative) wins.
- If they tie, it looks at `sequence_number`. The newest (most negative) wins!

*"But wait!"* you say. *"If I push `5` twice, do I have to search the heap to update its frequency?!"*
**NO!** This is the most beautiful part of this algorithm.
When you push `5` the first time, you put `(freq=1, seq=1, num=5)` in the heap.
When you push `5` the second time, you just put a NEW entry in the heap: `(freq=2, seq=2, num=5)`.
The heap now has TWO entries for `5`. But the `freq=2` one is guaranteed to be popped first! 
When you pop it, you just decrease the count of `5` in your tally back to `1`. The old `freq=1` entry is still sitting in the heap, waiting perfectly for the next time you need a `5` with frequency 1!

## 🎯 Core Strategy
This is an incredibly elegant use of the **Top K Elements** pattern leveraging **Lazy Updates**.

1. **State**: 
   - `sequence_number`: A counter that increments on every push to act as a unique timestamp.
   - `frequency_map`: A hash map tracking the *current* real frequency of elements in the stack.
   - `max_heap`: A heap storing tuples of `(-freq, -seq, num)`.
2. **Pushing**: 
   - Increment the element's count in the `frequency_map`.
   - Increment `sequence_number`.
   - Push `(-freq, -seq, num)` to the heap. **We do not modify existing entries for `num`. We just push a new, higher-frequency snapshot.**
3. **Popping**: 
   - `heappop()` naturally yields the highest frequency, breaking ties with the highest sequence number.
   - Extract the `num`.
   - Decrement `num`'s frequency in `frequency_map`.
   - Return `num`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Operations**: `push(1), push(2), push(1), pop(), pop()`

### Setup
- `seq = 0`, `map = {}`, `heap = []`.

### Push 1
- `map[1] = 1`, `seq = 1`.
- Push `(-1, -1, 1)`. Heap = `[(-1, -1, 1)]`.

### Push 2
- `map[2] = 1`, `seq = 2`.
- Push `(-1, -2, 2)`. Heap = `[(-1, -2, 2), (-1, -1, 1)]`. (Notice `-1, -2` beats `-1, -1`).

### Push 1
- `map[1] = 2`, `seq = 3`.
- Push `(-2, -3, 1)`. Heap = `[(-2, -3, 1), (-1, -1, 1), (-1, -2, 2)]`.

### Pop
- Pop root: `(-2, -3, 1)`. `num = 1`.
- `map[1]` goes from `2` down to `1`.
- Return `1`.
- Heap is now: `[(-1, -2, 2), (-1, -1, 1)]`.

### Pop
- Pop root: `(-1, -2, 2)`. `num = 2`.
- `map[2]` goes from `1` down to `0`.
- Return `2`.
- Heap is now: `[(-1, -1, 1)]`. 
- *(Look! The old snapshot for `1` is perfectly positioned to be popped next!)*

## 📊 Visual Diagram
Here's how the snapshots stack up in the heap, effortlessly maintaining history without requiring manual updates:

```mermaid
flowchart TD
    subgraph PushPhase [Push Phase]
        P1["push(1)\nSeq=1"] --> H1["Heap: [(-1, -1, 1)]"]
        P2["push(2)\nSeq=2"] --> H2["Heap: [(-1, -2, 2),\n (-1, -1, 1)]"]
        P3["push(1)\nSeq=3"] --> H3["Heap: [(-2, -3, 1),\n (-1, -2, 2),\n (-1, -1, 1)]"]
    end
    
    subgraph Pop1 [Pop 1]
        H3 --> Pop1["heappop()"]
        Pop1 --> R1["Returns 1"]
        R1 --> H4["Heap recovers:\n["(-1, -2, 2),\n (-1, -1, 1)"]"]
    end
    
    subgraph Pop2 [Pop 2]
        H4 --> Pop2["heappop()"]
        Pop2 --> R2["Returns 2"]
        R2 --> H5["Heap recovers:\n["(-1, -1, 1)"]"]
    end
    
    style H1 fill:#e3f2fd,color:#000
    style H2 fill:#e3f2fd,color:#000
    style H3 fill:#e3f2fd,color:#000
    style Pop1 fill:#ffcdd2,color:#000
    style Pop2 fill:#ffcdd2,color:#000
    style H4 fill:#c8e6c9,color:#000
    style H5 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(\log N)$ for both `push()` and `pop()`. Pushing to and popping from a heap of size $N$ takes $O(\log N)$. Modifying the hash map is $O(1)$.
- **Space Complexity:** $O(N)$ where $N$ is the total number of items pushed, because every push creates a new tuple in the heap.

### Edge Cases Handled Safely
- **Ties in frequency:** Handled natively and invisibly by the sequence number. Because `seq` strictly increments on every single operation, two elements will NEVER have the same sequence number, ensuring a deterministic stack-like LIFO (Last-In-First-Out) resolution for ties.
- **Popping the same element multiple times:** Works flawlessly because every push creates an independent snapshot. When the highest frequency snapshot is destroyed, the next highest frequency snapshot seamlessly slides into place.
