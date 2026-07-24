# 🚶‍♂️ Walkthrough: String Anagrams

## 👶 Explain Like I'm 5
Remember the Scrabble tiles from the "Permutation in a String" problem? This time, instead of stopping and shouting "I found it!" when you find the *first* match, you want to walk down the entire row of tiles on the table and **write down the starting position** of EVERY single place where your tiles match. 

*(PS: An anagram is just a fancy word for a permutation — the exact same letters, but mixed up in a different order!)*

We use the exact same strategy: slide a frame that is exactly the width of your Scrabble tiles across the table. Every time you slide, add the new tile entering the right side, and drop the old tile leaving the left side. Whenever the tiles perfectly match, write down the left edge's location!

## 🎯 Core Strategy
This is identical to the algorithm for "Permutation in a String", except we collect an array of indices instead of returning `True`.
1. Create a `char_freq` map counting the required characters of the `pattern`.
2. Keep a `matched` counter. We need `matched == len(char_freq)` to have a valid anagram.
3. Iterate `window_end` through the string `s`:
   - If the incoming character is in `char_freq`, decrement its required count. 
   - If its count hits `0`, increment `matched`.
4. If `matched == len(char_freq)`, we found an anagram! **Append `window_start` to our `result_indices` list.**
5. **Shrink**: Once `window_end >= len(pattern) - 1`, we have to shrink from the left before the next loop to keep the window size strictly equal to the pattern's length.
   - If the outgoing character was in `char_freq`, restore it. 
   - If its count was exactly `0`, we just lost a perfect match, so decrement `matched`.
   - Increment its count in `char_freq` and increment `window_start`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `pattern = "abc"`, `s = "cbaebabacd"`
Initialization: `pattern` length is 3. `freq = {'a':1, 'b':1, 'c':1}`. 
`start = 0`, `matched = 0`, `result = []`.

| Step | `end` char | `freq` map (Needed) | `matched` | Valid? (matched==3) | Action (Record, Shrink) |
|------|------------|---------------------|-----------|---------------------|-------------------------|
| 1 | `0` ('c') | `{'a':1, 'b':1, 'c':0}` | `1` | No | Size < 3, no shrink. |
| 2 | `1` ('b') | `{'a':1, 'b':0, 'c':0}` | `2` | No | Size < 3, no shrink. |
| 3 | `2` ('a') | `{'a':0, 'b':0, 'c':0}` | `3` | **YES!** | Record `start=0` -> `result=[0]`. <br> Shrink: Drop `s[0]` ('c'). `freq['c']=1`. `matched=2`. `start=1`. |
| 4 | `3` ('e') | `{'a':0, 'b':0, 'c':1}` | `2` ('e' ignored) | No | Shrink: Drop `s[1]` ('b'). `freq['b']=1`. `matched=1`. `start=2`. |
| 5 | `4` ('b') | `{'a':0, 'b':0, 'c':1}` | `2` | No | Shrink: Drop `s[2]` ('a'). `freq['a']=1`. `matched=1`. `start=3`. |
| 6 | `5` ('a') | `{'a':0, 'b':0, 'c':1}` | `2` | No | Shrink: Drop `s[3]` ('e'). (Ignored). `start=4`. |
| 7 | `6` ('b') | `{'a':0, 'b':-1, 'c':1}`| `2` | No | Shrink: Drop `s[4]` ('b'). `freq['b']=0`. `start=5`. |
| 8 | `7` ('a') | `{'a':-1, 'b':0, 'c':1}`| `2` | No | Shrink: Drop `s[5]` ('a'). `freq['a']=0`. `start=6`. |
| 9 | `8` ('c') | `{'a':-1, 'b':0, 'c':0}`| `3` | **YES!** | Record `start=6` -> `result=[0, 6]`. <br> Shrink: Drop `s[6]` ('b'). `freq['b']=1`. `matched=2`. `start=7`. |
| 10 | `9` ('d') | `{'a':-1, 'b':1, 'c':0}`| `2` ('d' ignored) | No | Shrink: Drop `s[7]` ('a'). `freq['a']=0` (wait, it was -1, so it becomes 0, matched stays 2). `start=8`. |

Result: `[0, 6]` (The anagrams are "cba" and "bac").

## 📊 Visual Diagram
Here is how multiple overlapping anagrams are found smoothly (e.g. `s = "abab"`, `pattern = "ab"`):

```mermaid
flowchart TD
    subgraph Step 2 [end=1. Window: [a, b]]
        W1["Match! Record index 0"]
        S1["Shrink: Drop 'a'. start=1"]
    end
    
    subgraph Step 3 [end=2. Window: [b, a]]
        W2["Add 'a'. Match! Record index 1"]
        S2["Shrink: Drop 'b'. start=2"]
    end
    
    subgraph Step 4 [end=3. Window: [a, b]]
        W3["Add 'b'. Match! Record index 2"]
        S3["Shrink: Drop 'a'. start=3"]
    end
    
    Step 2 --> Step 3
    Step 3 --> Step 4
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N + M)$. We populate the frequency map in $O(M)$ time and traverse the string `s` exactly once in $O(N)$ time.
- **Space Complexity:** $O(M)$ or $O(1)$ for the hash map storing only the characters of the pattern. The space used for the `result_indices` list is $O(N)$ in the worst case, but this is usually not considered auxiliary space.

### Edge Cases Handled Safely
- **Pattern longer than string:** Impossible to find an anagram. Returns `[]` instantly.
- **Overlapping Anagrams:** Because we shrink from the left but *keep* the rest of the window intact, overlapping matches (like finding `ab` in `abab`) are perfectly captured without any extra work!
