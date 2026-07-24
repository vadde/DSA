# 🚶‍♂️ Walkthrough: Remove K Digits

## 👶 Explain Like I'm 5
You are given a huge number like "1432219" and you are allowed to erase exactly $K$ digits to make the number as small as possible.
If $K = 3$, which digits do you erase?
You always want smaller numbers at the front! (e.g., 100 is smaller than 900).

So we read the numbers one by one and put them in a stack.
If we see a '4' at the top of our stack, and the next number coming along is a '3', we think: 
"Wait! If I erase this '4' right now, the '3' will slide over and take its place, making the whole number smaller!"
So as long as we have "erasers" left ($K > 0$), any time a smaller number comes along, we POP the bigger numbers off the stack to make room for the small guy!
This naturally builds a small increasing sequence (1, 2, 3...) which guarantees the smallest possible number.

## 🎯 Core Strategy
This is a Greedy algorithm executed via a **monotonically increasing stack**. At every step, we try to keep the stack strictly increasing by throwing away (popping) larger digits when a smaller digit is encountered, limited only by $K$.

1. Initialize an empty `stack`.
2. **Greedy Deletion**: Loop through every `digit` in the string `num`:
   - While the stack is not empty, AND we still have removals left (`k > 0`), AND the `digit` is SMALLER than the top of the stack (`stack[-1] > digit`):
     - We found a better (smaller) digit to take this place!
     - Pop the top of the stack.
     - Decrement `k` (we just used an eraser).
   - Push the current `digit` onto the stack.
3. **Handle Leftovers**: What if we still have erasers left? (e.g., the number was already sorted like `"1234"`). Then we just erase the biggest numbers, which are naturally sitting at the very end of our stack! `stack = stack[:-k]`.
4. **Clean up**: Join the stack into a string. We might have leading zeros (like `"0200"`). We must strip them using `.lstrip('0')`.
5. If the final string is completely empty (we erased everything), return `"0"`. Otherwise, return the string.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `num = "1432219"`, `k = 3`

| `digit` | `k` | Action | Stack State |
|---------|-----|--------|-------------|
| `"1"` | 3 | Push 1 | `["1"]` |
| `"4"` | 3 | `4 > 1`. Push 4 | `["1", "4"]` |
| `"3"` | 3 | `3 < 4`. Pop 4! `k = 2`.<br>Push 3. | `["1", "3"]` |
| `"2"` | 2 | `2 < 3`. Pop 3! `k = 1`.<br>Push 2. | `["1", "2"]` |
| `"2"` | 1 | `2 == 2`. Push 2. | `["1", "2", "2"]` |
| `"1"` | 1 | `1 < 2`. Pop 2! `k = 0`. (Erasers gone!).<br>Push 1. | `["1", "2", "1"]` |
| `"9"` | 0 | `k=0`, just push 9. | `["1", "2", "1", "9"]` |

Loop finishes. `k = 0`.
Result string: `"1219"`. No leading zeros to strip.
Final Result: `"1219"`.

## 📊 Visual Diagram
Here is a visualization of the greedy logic. If you replace a high digit with a lower digit at the most significant (leftmost) possible place, the total value plummets!

```mermaid
flowchart TD
    subgraph State
        W1["Stack: [1, 4]\nIncoming digit: '3'\nErasers left: 3"]
    end
    
    subgraph The Greedy Choice
        W2["Compare: 4 vs 3.\nIf we keep 4, number starts '14...'\nIf we erase 4 and keep 3, number starts '13...'\n13 is much smaller than 14!"]
    end
    
    subgraph Action
        W3["Use an eraser! Pop 4.\nStack: [1, 3]\nErasers left: 2"]
    end
    
    State --> The Greedy Choice
    The Greedy Choice --> Action
    
    style W2 fill:#fff9c4,color:#000
    style W3 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We iterate through the $N$ digits of the string exactly once. Each digit is pushed to the stack once and popped at most once.
- **Space Complexity:** $O(N)$ to store the characters in the stack and to build the final string.

### Edge Cases Handled Safely
- **Already Sorted:** `num = "12345", k = 2`. The inner `while` loop never triggers because `stack[-1] < digit`. At the end, `k` is still `2`. The code handles this via `if k > 0: stack = stack[:-k]`, cleanly slicing off the last two characters to return `"123"`.
- **Leading Zeros Formed:** `num = "10200", k = 1`. `0` pops `1` (because `0 < 1`). Stack becomes `["0", "2", "0", "0"]`. The `.lstrip('0')` cleans it to `"200"`.
- **Everything is Erased / All Zeros:** `num = "10", k = 2` or `num = "9", k = 1`. Stack ends up empty. `.lstrip('0')` leaves an empty string `""`. The return statement `result if result else "0"` safely turns this into `"0"`.
