# 🚶‍♂️ Walkthrough: Longest Substring with K Distinct Characters

## 👶 Explain Like I'm 5
Imagine you are making a necklace out of beads with letters on them. You want the longest piece of the necklace you can make, but you're only allowed to use up to $K$ different types of beads. 

You keep adding beads from right to left. If you accidentally add a $(K+1)$th type of bead, you've broken the rule! You must take off beads from the left side until you're back down to $K$ types.
By keeping track of the longest valid stretch of beads you ever hold in your hand, you'll easily find the answer!

## 🎯 Core Strategy
This introduces a **Dynamic-Size Sliding Window** paired with a **HashMap** (or Frequency Counter) to track character frequencies.
1. Initialize `window_start = 0`, `max_length = 0`, and a `char_freq` hash map to count character occurrences.
2. Iterate `window_end` through the string, adding the right-most character to `char_freq`.
3. If the number of distinct characters (`len(char_freq)`) exceeds $K$, the window is invalid. We enter a `while` loop to shrink from the left.
4. While shrinking, decrement the count of `s[window_start]` in the hash map. **Crucially**, if a character's count hits `0`, it must be completely deleted from the hash map so `len(char_freq)` accurately reflects the number of distinct characters remaining.
5. Once the window is valid again, record its length with `max_length = max(max_length, window_end - window_start + 1)`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `s = "araaci"`, `k = 2`
Initialization: `start = 0`, `max_len = 0`, `freq = {}`

| Step | `end` char | `freq` map | Distinct > 2? | Action (Update max_len, Shrink) |
|------|------------|------------|---------------|---------------------------------|
| 1 | `0` ('a') | `{'a': 1}` | No (1 <= 2) | `max_len` = max(0, 1) = **1**. (`[a]`) |
| 2 | `1` ('r') | `{'a': 1, 'r': 1}` | No (2 <= 2) | `max_len` = max(1, 2) = **2**. (`[ar]`) |
| 3 | `2` ('a') | `{'a': 2, 'r': 1}` | No (2 <= 2) | `max_len` = max(2, 3) = **3**. (`[ara]`) |
| 4 | `3` ('a') | `{'a': 3, 'r': 1}` | No (2 <= 2) | `max_len` = max(3, 4) = **4**. (`[araa]`) |
| 5 | `4` ('c') | `{'a': 3, 'r': 1, 'c': 1}` | **Yes (3 > 2)** | *SHRINK LOOP*: <br> - Drop `s[0]` ('a'). `freq` = `{'a': 2, 'r': 1, 'c': 1}`. `start = 1`. Still > 2! <br> - Drop `s[1]` ('r'). `freq` = `{'a': 2, 'c': 1}`. `start = 2`. Valid! |
| 6 | - | - | - | After shrink: `max_len` = max(4, 3) = **4**. (`[aac]`) |
| 7 | `5` ('i') | `{'a': 2, 'c': 1, 'i': 1}` | **Yes (3 > 2)** | *SHRINK LOOP*: <br> - Drop `s[2]` ('a'). `freq` = `{'a': 1, 'c': 1, 'i': 1}`. `start = 3`. Still > 2! <br> - Drop `s[3]` ('a'). `freq` = `{'c': 1, 'i': 1}`. `start = 4`. Valid! |
| 8 | - | - | - | After shrink: `max_len` = max(4, 2) = **4**. (`[ci]`) |

Result: The max length is `4` (from the substring `"araa"`).

## 📊 Visual Diagram
Here is a visualization of the Sliding Window expanding and shrinking with the Hash Map:

```mermaid
flowchart TD
    subgraph Expand to 4 [end = 3]
        W1["[ a, r, a, a ], c, i"]
        M1["Freq: {a:3, r:1}"]
        N1["Valid! Max Len: 4"]
    end
    
    subgraph Invalid Expand [end = 4]
        W2["[ a, r, a, a, c ], i"]
        M2["Freq: {a:3, r:1, c:1}"]
        N2["Invalid! Distinct = 3"]
    end
    
    subgraph Shrink 1 [start = 1]
        W3["a, [ r, a, a, c ], i"]
        M3["Freq: {a:2, r:1, c:1}"]
        N3["Invalid! Distinct = 3"]
    end
    
    subgraph Shrink 2 [start = 2]
        W4["a, r, [ a, a, c ], i"]
        M4["Freq: {a:2, c:1}"]
        N4["Valid! Distinct = 2. Max: 4"]
    end
    
    Expand to 4 --> Invalid Expand
    Invalid Expand --> Shrink 1
    Shrink 1 --> Shrink 2
    
    style W1 fill:#32CD32,color:#000
    style W2 fill:#ff6b6b,color:#000
    style W3 fill:#ff6b6b,color:#000
    style W4 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. Even with the `while` loop, the right pointer adds each character exactly once, and the left pointer removes each character at most once. Hash map insertions and deletions take $O(1)$. Thus, the time scales linearly with the string length.
- **Space Complexity:** $O(K)$. We store characters in a Hash Map. Because we delete a character as soon as its count hits `0`, the map will only ever hold a maximum of $K + 1$ characters at any given time.

### Edge Cases Handled Safely
- **`k = 0` or empty string:** If we aren't allowed to have any distinct characters, or the string has no characters, the code immediately returns `0` at the very beginning.
- **`k` is larger than unique characters:** If `s = "abc"` and `k = 10`, the `while` loop never executes, and it perfectly returns `3`.
