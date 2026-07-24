# 🚶‍♂️ Walkthrough: String Permutations by Changing Case

## 👶 Explain Like I'm 5
You are given a password like `"a1b"`.
Some characters are letters, some are numbers.
For every letter, it can be either lowercase or uppercase. You want to find EVERY possible combination of passwords!

You start with your original password in a box: `["a1b"]`.
You scan the password from left to right.
First character is `'a'`. It's a letter!
So, you make a copy of everything in your box. In the copies, you change the `'a'` to an `'A'`.
Now your box has: `["a1b", "A1b"]`.

Second character is `'1'`. It's a number! We ignore it and do nothing.

Third character is `'b'`. It's a letter!
You make copies of EVERYTHING in your box, and change the `'b'` to a `'B'` in the copies.
Now your box has: `["a1b", "A1b", "a1B", "A1B"]`.
You are done!

## 🎯 Core Strategy
This uses the **Subsets (BFS)** pattern applied to Strings.

1. **Initialization**: Start with a list containing just the original string: `permutations = [s]`.
2. **Outer Loop**: Loop through every character index `i` from `0` to `len(s) - 1`.
3. **Condition**: Check if the current character `s[i]` is a letter using `.isalpha()`. We only branch for letters.
4. **Snapshot**: Take a snapshot of the current list size: `n = len(permutations)`.
5. **Inner Loop (The Copying)**: Loop `j` from `0` to `n - 1`:
   - *Python Quirk*: Strings in Python are immutable (cannot be changed). To change a single character, we must first convert the string to a list of characters: `chs = list(permutations[j])`.
   - Swap the case of the character at index `i`: `chs[i] = chs[i].swapcase()`.
   - Convert the list back to a string and append it to our main list: `permutations.append("".join(chs))`.
6. Return `permutations`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: `s = "a1b"`

### Initialization
`permutations = ["a1b"]`

### Loop `i = 0` (char `'a'`)
- Is `'a'` a letter? YES.
- `n = 1`.
- `j = 0`:
  - `chs = ['a', '1', 'b']`
  - Swap `chs[0]` to `'A'`.
  - Append `"A1b"`.
- `permutations = ["a1b", "A1b"]`.

### Loop `i = 1` (char `'1'`)
- Is `'1'` a letter? NO.
- Do nothing. 
- `permutations = ["a1b", "A1b"]`.

### Loop `i = 2` (char `'b'`)
- Is `'b'` a letter? YES.
- `n = 2`.
- `j = 0`:
  - Look at `"a1b"`. `chs = ['a', '1', 'b']`.
  - Swap `chs[2]` to `'B'`.
  - Append `"a1B"`.
- `j = 1`:
  - Look at `"A1b"`. `chs = ['A', '1', 'b']`.
  - Swap `chs[2]` to `'B'`.
  - Append `"A1B"`.
- `permutations = ["a1b", "A1b", "a1B", "A1B"]`.

Return `["a1b", "A1b", "a1B", "A1B"]`.

## 📊 Visual Diagram
Here is how the BFS tree only branches when it hits a letter:

```mermaid
flowchart TD
    subgraph Start
        S0["a1b"]
    end
    
    subgraph i=0 'a'
        S1_1["a1b"]
        S1_2["A1b"]
    end
    
    subgraph i=1 '1'
        note1["(No branching for numbers)"]
    end
    
    subgraph i=2 'b'
        S3_1["a1b"]
        S3_2["a1B"]
        
        S3_3["A1b"]
        S3_4["A1B"]
    end
    
    Start -- "Keep 'a'" --> S1_1
    Start -- "Swap 'a' -> 'A'" --> S1_2
    
    S1_1 -- "Pass '1'" --> S3_1
    S1_1 -- "Pass '1', Swap 'b' -> 'B'" --> S3_2
    
    S1_2 -- "Pass '1'" --> S3_3
    S1_2 -- "Pass '1', Swap 'b' -> 'B'" --> S3_4
    
    style Start fill:#e3f2fd,color:#000
    style S1_1 fill:#bbdefb,color:#000
    style S1_2 fill:#bbdefb,color:#000
    style note1 fill:#f5f5f5,stroke-dasharray: 5 5,color:#000
    style S3_1 fill:#90caf9,color:#000
    style S3_2 fill:#90caf9,color:#000
    style S3_3 fill:#90caf9,color:#000
    style S3_4 fill:#90caf9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \times 2^N)$. In the worst case, the string is made entirely of letters. There will be $2^N$ permutations. For each permutation, we convert strings to lists and back, taking $O(N)$ time.
- **Space Complexity:** $O(N \times 2^N)$ to store all $2^N$ strings in the result array, each of length $N$.

### Edge Cases Handled Safely
- **No Letters:** `s = "123"`. The `isalpha()` check prevents the inner loop from ever running. Returns `["123"]` natively without doing any useless array copying.
- **All Uppercase Input:** `.swapcase()` automatically toggles `A -> a` and `a -> A`. So `s = "C"` will generate `["C", "c"]` perfectly.
