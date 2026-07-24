# 🚶‍♂️ Walkthrough: Permutation in a String

## 👶 Explain Like I'm 5
Imagine you have a specific set of Scrabble tiles, say `A`, `B`, and `C`. You are looking at a long row of other Scrabble tiles on a table. 
You want to see if you can find your exact set of tiles all clumped together in the long row. The order of the tiles doesn't matter, as long as you have all of them right next to each other. So `ABC`, `CBA`, and `BCA` are all winning matches!

You create a picture frame that is **exactly** as wide as your set of tiles (size 3). 
You slide this frame along the long row, one tile at a time. Every time you slide the frame:
1. You look at the new tile that entered the right side of the frame. Do you need it?
2. You look at the old tile that fell out of the left side of the frame. Did you need it?
If, at any point, the tiles inside your frame perfectly match the ones in your hand, you win!

## 🎯 Core Strategy
This introduces the **Fixed-Size Sliding Window** paired with a **HashMap & Match Counter**.
1. Create a `char_freq` map counting the required occurrences of each character in the `pattern`.
2. Keep a `matched` counter to track how many *distinct* characters have been completely satisfied. We need `matched == len(char_freq)`.
3. Iterate `window_end` through the string `s` to expand the window:
   - If the incoming character is in `char_freq`, decrement its required count. 
   - If its count hits `0`, increment `matched`.
4. If `matched == len(char_freq)`, return `True` immediately!
5. **Shrink**: Since the window size is strictly fixed to `len(pattern)`, once we reach that size, we must slide the left edge (`window_start`) forward before the next loop.
   - If the outgoing character was in `char_freq`, we restore it. 
   - If its count was exactly `0`, we just lost a perfect match for that character, so we decrement `matched`.
   - Increment its count in `char_freq` and increment `window_start`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `pattern = "abc"`, `s = "oidbcaf"`
Initialization: `pattern` length is 3. `freq = {'a':1, 'b':1, 'c':1}`. Distinct chars = 3. 
`start = 0`, `matched = 0`.

| Step | `end` char | `freq` map (Needed) | `matched` | Valid? (matched==3) | Action (Shrink Window) |
|------|------------|---------------------|-----------|---------------------|------------------------|
| 1 | `0` ('o') | `{'a':1, 'b':1, 'c':1}` (not in pattern) | `0` | No | Window is `[o]`. Size < 3, no shrink. |
| 2 | `1` ('i') | `{'a':1, 'b':1, 'c':1}` (not in pattern) | `0` | No | Window is `[o, i]`. Size < 3, no shrink. |
| 3 | `2` ('d') | `{'a':1, 'b':1, 'c':1}` (not in pattern) | `0` | No | Window `[o, i, d]`. Size = 3. Shrink! <br> Drop `s[0]` ('o'). Start=1. |
| 4 | `3` ('b') | `{'a':1, 'b':0, 'c':1}` | `1` ('b' hits 0)| No | Window `[i, d, b]`. Size = 3. Shrink! <br> Drop `s[1]` ('i'). Start=2. |
| 5 | `4` ('c') | `{'a':1, 'b':0, 'c':0}` | `2` ('c' hits 0)| No | Window `[d, b, c]`. Size = 3. Shrink! <br> Drop `s[2]` ('d'). Start=3. |
| 6 | `5` ('a') | `{'a':0, 'b':0, 'c':0}` | `3` ('a' hits 0)| **YES!** | Return `True` immediately! |

Result: `True` (The permutation is `"bca"`).

## 📊 Visual Diagram
Here is how the Fixed Window and Match Counter interact:

```mermaid
flowchart TD
    subgraph Iteration 5 [end=4. Window: d, b, c]
        W1["Add 'c'. freq['c'] reaches 0!"]
        N1["matched = 2"]
    end
    
    subgraph Shrink [Drop left side]
        W2["Drop 'd'"]
        N2["'d' not in pattern. freq and matched unchanged."]
    end
    
    subgraph Iteration 6 [end=5. Window: b, c, a]
        W3["Add 'a'. freq['a'] reaches 0!"]
        N3["matched = 3. TARGET MET!"]
    end
    
    Iteration 5 --> Shrink
    Shrink --> Iteration 6
    
    style W1 fill:#32CD32,color:#000
    style W2 fill:#FFD700,color:#000
    style W3 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N + M)$, where $N$ is the length of the string `s` and $M$ is the length of the `pattern`. We first populate the frequency map in $O(M)$ time. Then we slide the window across the string `s` in $O(N)$ time.
- **Space Complexity:** $O(M)$ or $O(26) = O(1)$ if assuming only lowercase English letters. The hash map only stores characters from the `pattern`.

### Edge Cases Handled Safely
- **Pattern longer than string:** If `len(pattern) > len(s)`, it is physically impossible to find a permutation. The code catches this immediately (`if len(pattern) > len(s): return False`) and saves time.
- **Duplicate characters in pattern:** E.g., `pattern = "aab"`. `freq['a']` starts at 2. It will only increment `matched` when we find exactly two 'a's inside the window, because `matched` only increments when the count hits exactly `0`. If we find a third 'a', `freq['a']` becomes `-1`, which does nothing to `matched`. This is incredibly robust!
