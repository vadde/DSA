# 🚶‍♂️ Walkthrough: First Non-repeating Character

## 👶 Explain Like I'm 5
You have a word like "apple".
You want to find the first letter that appears exactly ONE time in the whole word.

If you look at `'a'`, it appears 1 time. It's the very first letter! So the answer is `'a'`.
What about `"aabbc"`?
`'a'` appears 2 times. `'b'` appears 2 times. `'c'` appears 1 time. So the answer is `'c'`.

To solve this quickly, we just read the word twice:
- **First time**: We write down in our magical notebook how many times we see every single letter.
- **Second time**: We look at the letters in order from left to right, check the notebook, and as soon as we find a letter with a count of exactly 1, we stop and return its index!

## 🎯 Core Strategy
This uses a **Hash Map for Frequency Counting**, which is one of the most common applications of a Hash Map. By counting the frequencies first, we can answer questions about uniqueness in $O(1)$ time on the second pass.

1. Initialize an empty dictionary `freq_map = {}` to store character counts (`char -> int`).
2. **First Pass (Build)**: Loop through the string.
   - For every character, increment its count in `freq_map`.
   - Python idiom: `freq_map[char] = freq_map.get(char, 0) + 1`
3. **Second Pass (Find)**: Loop through the string again using `enumerate` to get the index `i` and `char`.
   - Check the frequency: `if freq_map[char] == 1`.
   - If true, instantly return the index `i`.
4. If the loop finishes and we didn't return anything, it means every character was repeated! Return `-1`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `"loveleetcode"`

### Phase 1: Build the Frequency Map
We scan the entire string and count occurrences.
`freq_map` = `{'l': 2, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1}`

### Phase 2: Find the First Unique
Now we walk through the string from left to right and check the map.

| `i` | `char` | `freq_map[char]` | Action |
|-----|--------|------------------|--------|
| 0 | `'l'` | 2 | Continue |
| 1 | `'o'` | 2 | Continue |
| 2 | `'v'` | **1** | Return `2`! |

Final Result: **2**.

## 📊 Visual Diagram
Here is how the two-pass algorithm elegantly separates "counting" from "searching":

```mermaid
flowchart TD
    subgraph Input
        W1["String: l-o-v-e-l-e-e-t-c-o-d-e"]
    end
    
    subgraph Pass 1: Tally up
        N1["Map Built:\n{'l': 2, 'o': 2, 'v': 1, 'e': 4...}"]
    end
    
    subgraph Pass 2: Scan for 1
        N2["Index 0: 'l' -> Count 2 (Skip)\nIndex 1: 'o' -> Count 2 (Skip)\nIndex 2: 'v' -> Count 1 (FOUND IT!)"]
    end
    
    Input --> Pass 1: Tally up
    Pass 1: Tally up --> Pass 2: Scan for 1
    
    style N1 fill:#e3f2fd,color:#000
    style N2 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We loop through the string of length $N$ exactly twice. $O(2N)$ simplifies to $O(N)$. Dictionary lookups and insertions are $O(1)$.
- **Space Complexity:** $O(1)$ strictly speaking. Even though we create a Hash Map, the string only consists of English letters. There are at most 26 unique lowercase English letters. The dictionary will never grow beyond size 26, which is an $O(1)$ constant space bound.

### Edge Cases Handled Safely
- **All characters repeat:** e.g., `"aabb"`. The second loop checks `a` (count 2) and `b` (count 2), finds nothing with count 1, finishes the loop, and safely returns `-1`.
- **Empty string:** `""`. Both loops skip entirely. Returns `-1`.
- **Single character:** `"z"`. Map built as `{'z': 1}`. Second pass immediately finds `z` at index 0 and returns `0`.
