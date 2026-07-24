# 🚶‍♂️ Walkthrough: Next Greater Element

## 👶 Explain Like I'm 5
You are walking down a line of people of different heights.
For every single person, you want to tell them: "Hey, the very next person who is TALLER than you is standing right over there!"
If no one taller is standing behind them, you tell them "-1".

Instead of each person individually looking all the way down the line (which takes a long time), we can just have everyone who hasn't found a taller person yet wait in a special "Waiting Room" (our Stack).
When a super tall person walks into the room, EVERYONE in the waiting room who is shorter than the tall person says "Aha! That's my Next Greater Element!" 
They write down the tall person's height and happily leave the waiting room.
Then the tall person enters the waiting room themselves to see if anyone even taller comes along later!

## 🎯 Core Strategy
This is the foundational **Monotonic Stack** pattern. A "monotonic" stack is just a stack whose elements are always completely sorted (either always increasing or always decreasing). In this case, we maintain a **monotonically decreasing stack**.

1. Initialize a `result` array of the same length as the input, filled with `-1`.
2. Initialize an empty `stack`. The stack will store the **indices** of the elements waiting to find a greater element.
3. Loop `for i, num in enumerate(arr)`:
   - **Pop & Resolve**: While the stack is not empty AND `num` is GREATER than the element currently at the top of the stack (`arr[stack[-1]]`):
     - The rule of our monotonically decreasing stack is broken by `num`!
     - Pop the index from the stack: `popped_index = stack.pop()`.
     - Update the result for that person: `result[popped_index] = num`.
   - **Push**: Push the current person's index into the waiting room: `stack.append(i)`.
4. Any indices left in the stack at the end never found a greater element, so they correctly remain `-1` in the `result` array. Return `result`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `arr = [4, 6, 3, 2, 8, 1]`
Initialization: `result = [-1, -1, -1, -1, -1, -1]`, `stack = []`.

| `i` | `num` | Action | `stack` (Indices) | `result` |
|-----|-------|--------|-------------------|----------|
| 0 | `4` | Stack empty. Push 0. | `[0]` | `[-1, -1, -1, -1, -1, -1]` |
| 1 | `6` | `6 > arr[0]` (4). Pop 0. `result[0] = 6`. Push 1. | `[1]` | `[6, -1, -1, -1, -1, -1]` |
| 2 | `3` | `3 < arr[1]` (6). Push 2. | `[1, 2]` | `[6, -1, -1, -1, -1, -1]` |
| 3 | `2` | `2 < arr[2]` (3). Push 3. | `[1, 2, 3]` | `[6, -1, -1, -1, -1, -1]` |
| 4 | `8` | `8 > arr[3]` (2). Pop 3. `result[3] = 8`. <br> `8 > arr[2]` (3). Pop 2. `result[2] = 8`. <br> `8 > arr[1]` (6). Pop 1. `result[1] = 8`. <br> Push 4. | `[4]` | `[6, 8, 8, 8, -1, -1]` |
| 5 | `1` | `1 < arr[4]` (8). Push 5. | `[4, 5]` | `[6, 8, 8, 8, -1, -1]` |

Loop ends.
Final `result`: `[6, 8, 8, 8, -1, -1]`.

## 📊 Visual Diagram
Here is how the giant '8' resolves everyone waiting in the stack:

```mermaid
flowchart TD
    subgraph Wait Room
        W1["Stack before 8 arrives:\n[Index 1 (Value 6)]\n[Index 2 (Value 3)]\n[Index 3 (Value 2)]"]
    end
    
    subgraph The Giant Arrives
        A1["'8' arrives at Index 4"]
    end
    
    subgraph Resolutions
        R1["8 > 2. Pop Index 3. result[3] = 8"]
        R2["8 > 3. Pop Index 2. result[2] = 8"]
        R3["8 > 6. Pop Index 1. result[1] = 8"]
        N1["Push Index 4."]
    end
    
    Wait Room --> The Giant Arrives
    The Giant Arrives --> Resolutions
    
    style A1 fill:#c8e6c9,color:#000
    style R1 fill:#fff9c4,color:#000
    style R2 fill:#fff9c4,color:#000
    style R3 fill:#fff9c4,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We loop through the array of length $N$ exactly once. Even though there is a `while` loop inside, every single index is pushed onto the stack exactly once, and popped off at most once. So the inner loop only executes $N$ times total across the entire program.
- **Space Complexity:** $O(N)$. In the worst-case scenario (an array sorted in descending order like `[5, 4, 3, 2, 1]`), nobody ever finds a greater element, and the stack grows to hold all $N$ indices.

### Edge Cases Handled Safely
- **Descending Array:** `[5, 4, 3, 2, 1]`. The `while stack and num > arr[stack[-1]]` loop literally never executes. The stack just fills up. Result remains identically `[-1, -1, -1, -1, -1]`. Perfect!
- **Ascending Array:** `[1, 2, 3, 4, 5]`. Every single number pops the previous one immediately. Result is `[2, 3, 4, 5, -1]`. Perfect!
