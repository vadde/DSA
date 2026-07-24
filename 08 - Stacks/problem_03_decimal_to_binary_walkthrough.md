# 🚶‍♂️ Walkthrough: Decimal to Binary Conversion

## 👶 Explain Like I'm 5
How do you turn a normal number (like 13) into binary (0s and 1s)?
You just keep dividing by 2!
13 divided by 2 is 6, with a remainder of **1**.
6 divided by 2 is 3, with a remainder of **0**.
3 divided by 2 is 1, with a remainder of **1**.
1 divided by 2 is 0, with a remainder of **1**.

If you read the remainders exactly as they came out, you get "1, 0, 1, 1".
But wait! Binary is written backwards. The FIRST remainder you got should actually be the very LAST digit of your binary number!
The correct binary for 13 is "1101".

This sounds like a perfect job for a Stack! 
We push every remainder onto a Stack as we get it. Since the first remainder is pushed to the very bottom of the stack, it will be the very LAST thing to be popped off!

## 🎯 Core Strategy
This is a standard base-conversion algorithm, naturally solved by a Stack due to the LIFO (Last-In, First-Out) requirement.

1. **Initialize** an empty stack (Python list).
2. **Handle Zero**: If the input `n` is `0` to begin with, just return `"0"`.
3. **Push Phase (Modulo & Divide)**:
   - Loop `while n > 0`:
   - Calculate the binary digit: `remainder = n % 2`.
   - Push `str(remainder)` to the stack.
   - Shrink the number: `n = n // 2` (integer division).
4. **Pop Phase**:
   - Pop elements from the stack one by one and append them to a result list. (In Python, it's faster to build lists and `.join()` them rather than doing string concatenation).
5. **Return** the joined result string.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `n = 13`

### Phase 1: Push Remainders
| `n` | `n % 2` (Remainder) | `n // 2` (New n) | Action | Stack State |
|-----|-------------------|------------------|--------|-------------|
| 13 | 1 | 6 | Push "1" | `['1']` |
| 6 | 0 | 3 | Push "0" | `['1', '0']` |
| 3 | 1 | 1 | Push "1" | `['1', '0', '1']` |
| 1 | 1 | 0 | Push "1" | `['1', '0', '1', '1']` |

Loop ends because $N = 0$.

### Phase 2: Pop to Read Backwards
- Pop! Returns "1".
- Pop! Returns "1".
- Pop! Returns "0".
- Pop! Returns "1".

Result list: `["1", "1", "0", "1"]`.
Joined: `"1101"`.

## 📊 Visual Diagram
Here is how the Stack automatically reverses the order of remainders:

```mermaid
flowchart TD
    subgraph Division Loop
        W1["13 % 2 = 1\n6 % 2 = 0\n3 % 2 = 1\n1 % 2 = 1"]
    end
    
    subgraph The Stack (Bottom to Top)
        S1["Bottom\n'1'\n'0'\n'1'\n'1'\nTop"]
    end
    
    subgraph Popping (Top to Bottom)
        P1["Read: 1, 1, 0, 1"]
    end
    
    Division Loop --> The Stack (Bottom to Top)
    The Stack (Bottom to Top) --> Popping (Top to Bottom)
    
    style S1 fill:#ffcdd2,color:#000
    style P1 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(\log N)$. We divide $N$ by 2 at every step. This means the loop runs exactly $\approx \log_2(N)$ times. Pushing and popping take $O(1)$ per operation. Total time is $O(\log N)$.
- **Space Complexity:** $O(\log N)$. The stack stores exactly $\approx \log_2(N)$ string characters.

### Edge Cases Handled Safely
- **Input is 0:** The `while n > 0:` loop would never run, returning an empty string. We specifically handle this with a fast-path at the very top: `if n == 0: return "0"`.
- **Input is 1:** The loop runs exactly once. Stack becomes `['1']`. Returns `"1"`. Perfect!
