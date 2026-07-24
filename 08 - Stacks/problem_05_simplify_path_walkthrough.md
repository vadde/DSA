# 🚶‍♂️ Walkthrough: Simplify Path

## 👶 Explain Like I'm 5
Imagine you are exploring folders on a computer. You start at the very beginning (the root `/`).
The path you are given is like a map with some weird, messy instructions:
- `/a/` means "go into folder 'a'".
- `.` means "stay in the current folder".
- `..` means "go BACK out of this folder to the previous one".
- `//` means nothing special, it's just a typo, treat it like a single `/`.

You want to read this messy map and draw a clean, simple map that gets you to the exact same final folder without any backtracking or typos.

Since `..` literally means "undo my last move", this is the perfect job for a Stack!
Every time you go into a folder, you **push** it onto the stack.
Every time you see `..`, you **pop** the top folder off the stack (undoing your last move).
If you see `.` or empty spaces from typos, you just **ignore** them!

## 🎯 Core Strategy
Because of the "undo" operation (`..`), this problem is perfectly suited for a Last-In, First-Out (LIFO) Stack.

1. Initialize an empty `stack`.
2. **Tokenize**: Split the input path by `/`. This automatically breaks the string into distinct parts, and turns multiple slashes like `//` into empty string tokens `""`.
   *(e.g., `"/a//b/./../c/"` becomes `['', 'a', '', 'b', '.', '..', 'c', '']`).*
3. Loop through each `part` in the parts:
   - **Undo**: If `part == '..'`: We need to go back! `pop()` from the stack IF the stack is not empty.
   - **Ignore**: If `part == '.'` or `part == ''`: Just `continue` and ignore it.
   - **Enter Folder**: Else: It's a real folder name! `push()` it to the stack.
4. After the loop, the stack contains exactly the sequence of folders you need to enter.
5. Reconstruct the final string by joining the stack with `/`, and prepend a leading `/` because it's an absolute path.
   Return `"/" + "/".join(stack)`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `"/a/./b/../../c/"`

**Split into parts:** `['', 'a', '.', 'b', '..', '..', 'c', '']`

| `part` | Action | Stack State |
|--------|--------|-------------|
| `""` | Ignore | `[]` |
| `"a"` | Push "a" | `["a"]` |
| `"."` | Ignore | `["a"]` |
| `"b"` | Push "b" | `["a", "b"]` |
| `".."` | Pop! (Undoes "b") | `["a"]` |
| `".."` | Pop! (Undoes "a") | `[]` |
| `"c"` | Push "c" | `["c"]` |
| `""` | Ignore | `["c"]` |

Loop ends.
Join stack elements with `/`: `"c"`.
Prepend `/`: `"/c"`.

Final Result: `"/c"`.

## 📊 Visual Diagram
Here is how the Stack automatically resolves backward navigation:

```mermaid
flowchart TD
    subgraph Path
        W1["/a/b/../c"]
    end
    
    subgraph Operations
        O1["Push 'a'"]
        O2["Push 'b'"]
        O3["See '..', Pop 'b'!"]
        O4["Push 'c'"]
    end
    
    subgraph Final Stack
        S1["[Top]\n'c'\n'a'\n[Bottom]"]
        R1["Result: /a/c"]
    end
    
    Path --> Operations
    Operations --> Final Stack
    
    style O3 fill:#ffcdd2,color:#000
    style S1 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. Splitting the string takes $O(N)$. Iterating through the parts takes $O(N)$ because pushing and popping are $O(1)$. Total time is $O(N)$.
- **Space Complexity:** $O(N)$. The stack can store up to $O(N)$ parts if the path is very deep and contains no `..` commands.

### Edge Cases Handled Safely
- **Trying to go above root (`"/../"`):** The split yields `['', '..', '']`. When it processes `'..'`, it sees the stack is empty. The `if stack: stack.pop()` logic prevents an error and safely ignores it. The final result is `"/"`. Perfect.
- **Multiple slashes (`"/a//b"`):** The split yields `['', 'a', '', 'b']`. The empty strings `''` are safely ignored by the `elif part == '':` check.
- **Dots as valid names (`"/..."`):** Only `.` and `..` are special. `...` is technically a valid folder name in Unix. The `else:` block catches it and pushes it to the stack perfectly.
