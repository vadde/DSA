# 🚶‍♂️ Walkthrough: Balanced Parentheses

## 👶 Explain Like I'm 5
Imagine you have a bunch of nested boxes. 
A square box `[` can go inside a round box `(`, which gives you `([ ])`.
But you can't close a round box if the square box inside it is still open! `([ )]` is wrong.

Every time you open a box (an opening bracket), you write it down on a notepad (Push it to a Stack).
Every time you want to close a box, you look at the last box you opened (Pop from the Stack).
If it's the exact same shape, great! You close it.
If it's a different shape, or if your notepad is empty (you didn't open any boxes!), then it's an error.

## 🎯 Core Strategy
This is the textbook problem for learning how **Stacks** operate with a Last-In, First-Out (LIFO) pattern. 

1. Create a `stack` (in Python, just a standard `list`).
2. Create a mapping (dictionary) to match closing brackets to opening brackets: `mapping = {')': '(', '}': '{', ']': '['}`.
3. Loop through every character in the string:
   - If the character is an opening bracket `({[`, **push** it to the stack.
   - If the character is a closing bracket `)}]`:
     - If the stack is empty, return `False` (trying to close something that isn't open).
     - **Pop** the top character from the stack.
     - Check if the popped character matches `mapping[char]`. If not, return `False`.
4. After the loop finishes, check the stack. If the stack is NOT empty, it means we opened boxes we never closed! Return `False`. Otherwise, return `True`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `"{[()]}"`

| Char | Type | Action | Stack State | Result |
|------|------|--------|-------------|--------|
| `{` | Opening | Push `{` | `['{']` | Valid |
| `[` | Opening | Push `[` | `['{', '[']` | Valid |
| `(` | Opening | Push `(` | `['{', '[', '(']` | Valid |
| `)` | Closing | Pop `(`. Match `)`? Yes! | `['{', '[']` | Valid |
| `]` | Closing | Pop `[`. Match `]`? Yes! | `['{']` | Valid |
| `}` | Closing | Pop `{`. Match `}`? Yes! | `[]` | Valid |

Loop finishes. Stack is empty. Return `True`!

**Example Input**: `"([)]"`

| Char | Type | Action | Stack State | Result |
|------|------|--------|-------------|--------|
| `(` | Opening | Push `(` | `['(']` | Valid |
| `[` | Opening | Push `[` | `['(', '[']` | Valid |
| `)` | Closing | Pop `[`. Match `)`? NO! `[` != `(` | `['(']` | **Return False!** |

## 📊 Visual Diagram
Here is a visualization of how nested brackets enter and exit the stack:

```mermaid
flowchart TD
    subgraph Input
        W1["{ [ ] }"]
    end
    
    subgraph Step 1: Push {
        S1["Stack: Bottom -> { -> Top"]
    end
    
    subgraph Step 2: Push [
        S2["Stack: Bottom -> { -> [ -> Top"]
    end
    
    subgraph Step 3: See ], Pop!
        S3["Pop '['! Does '[' match ']'? YES!"]
        S3_2["Stack shrinks: Bottom -> { -> Top"]
    end
    
    Input --> Step 1
    Step 1 --> Step 2
    Step 2 --> Step 3
    
    style S2 fill:#ffcdd2,color:#000
    style S3 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We iterate through the string of length $N$ exactly once. Pushing to and popping from the end of a Python list is $O(1)$.
- **Space Complexity:** $O(N)$. In the worst case (e.g., `"((((((((("`), the stack stores every single character.

### Edge Cases Handled Safely
- **String is completely empty:** The `for` loop skips entirely. `len(stack) == 0` evaluates to `True`. Correct!
- **String only has closing brackets:** e.g. `"))) "`. The very first character `)` triggers a `pop()`. The code handles this via `stack.pop() if stack else '#'`, which safely returns `#`. Since `# != (`, it immediately returns `False`.
- **String only has opening brackets:** e.g. `"((("`. The loop pushes three `(` characters and finishes. The stack length is 3. `len(stack) == 0` evaluates to `False`. Correct!
