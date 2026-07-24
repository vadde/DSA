# 🚶‍♂️ Walkthrough: Words Concatenation

## 👶 Explain Like I'm 5
Imagine you have a few specific Lego blocks of the exact same size, each with a word on it (like "cat" and "fox"). You are looking at a very long track built entirely out of identical-sized Lego blocks. 

You want to find every place on the track where your specific blocks are laid out right next to each other in ANY order, with NO extra blocks in between! So "catfox" and "foxcat" are both winners.
Because every single block is the exact same size, instead of slowly moving forward one tiny bump at a time, you can put on your giant boots and step forward **block by block**! You check the block, step forward, check the next block, and see if they match the blocks in your hands.

## 🎯 Core Strategy
Since all words have the exact same length, this is a beautiful adaptation of the "String Anagrams" algorithm where instead of matching *characters*, we match *entire words*.
1. Create a `word_freq` map counting how many times we need each word.
2. Because we take giant steps of `word_length`, we might miss the correct starting position if we only start at index `0`. To fix this, we run the Sliding Window `word_length` times! (Once starting at index 0, once at index 1... up to `word_length - 1`).
3. For each starting offset, initialize a `words_seen` map, `window_start = offset`, and `matched = 0`.
4. Iterate `window_end` in steps of `word_length`. Slice out the `current_word`.
   - **Match**: If `current_word` is in `word_freq`, add it to `words_seen`. If the count exactly matches what we need, increment `matched`.
   - **Too Many**: If we've seen this word *too many* times (e.g., we need one "cat" but we just saw our second "cat"), we shrink the window from the left by `word_length` steps until the surplus is removed.
   - **Win**: If `matched == len(word_freq)` (meaning we matched all distinct words perfectly), record `window_start`.
   - **Break**: If `current_word` is NOT in `word_freq`, our continuous chain is broken! We immediately reset `window_start` past this bad word, clear `words_seen`, and reset `matched`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `s = "catfoxcat"`, `words = ["cat", "fox"]`
Initialization: `word_length = 3`. `word_freq = {'cat':1, 'fox':1}`. Distinct = 2.
We will run the sliding window 3 times (offsets 0, 1, 2). Let's trace offset `0`:
`start = 0`, `matched = 0`, `words_seen = {}`

| Step | `end` index | Extract Word | In `word_freq`? | Action (Update seen, matched, shrink) |
|------|-------------|--------------|-----------------|---------------------------------------|
| 1 | `0` | `"cat"` | **Yes** | `seen['cat'] = 1`. `matched = 1`. <br> Not too many. <br> `matched != 2`. |
| 2 | `3` (step+3)| `"fox"` | **Yes** | `seen['fox'] = 1`. `matched = 2`. <br> Not too many. <br> `matched == 2` -> **YES!** Record `start=0`. |
| 3 | `6` (step+3)| `"cat"` | **Yes** | `seen['cat'] = 2`. `matched = 2`. <br> *TOO MANY!* (2 > 1). <br> *SHRINK*: Drop left word ("cat"). `seen['cat'] = 1`. `matched = 2`. `start = 3`. <br> `matched == 2` -> **YES!** Record `start=3`. |

Result: `[0, 3]`. (Offsets 1 and 2 will hit bad words and reset immediately).

## 📊 Visual Diagram
Here is how stepping and breaking the chain works:

```mermaid
flowchart TD
    subgraph Iteration 1 [Start at Offset 0]
        W1["Window: [cat]foxbad..."]
        N1["'cat' is good! words_seen={cat:1}"]
    end
    
    subgraph Iteration 2 [Step 3]
        W2["Window: [cat, fox]bad..."]
        N2["'fox' is good! matched=2. WIN! Record 0."]
    end
    
    subgraph Iteration 3 [Step 3]
        W3["Window: cat, fox, [bad]..."]
        N3["'bad' is NOT in our list!"]
    end
    
    subgraph Reset
        W4["Window broken! start moves past 'bad'"]
        N4["Clear words_seen, matched=0"]
    end
    
    Iteration 1 --> Iteration 2
    Iteration 2 --> Iteration 3
    Iteration 3 --> Reset
    
    style Iteration 2 fill:#32CD32,color:#000
    style Iteration 3 fill:#ff6b6b,color:#000
    style Reset fill:#FFD700,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We run `word_length` outer loops, but inside we jump by `word_length`. This perfectly balances out, meaning every character in the string is processed essentially twice (once when the word is added to the window, once when it's removed). Slicing the substring takes $O(word\_length)$, keeping the entire algorithm strictly $O(N)$ with respect to the string length.
- **Space Complexity:** $O(M \times word\_length)$, where $M$ is the number of words. We store the frequency of the words in hash maps, which takes space proportional to the total length of the words in the list.

### Edge Cases Handled Safely
- **Chain Broken by Junk Words:** The `else` block (when a word is not in the required list) instantly resets the entire window. This is highly optimized so we don't slowly drag a window through a garbage section of the string.
- **Overlapping Same Words:** E.g., `s="catcatfox"`. When the second "cat" is seen, the inner `while` loop triggers and shrinks the window from the left until the first "cat" is dropped. The window slides perfectly from `[cat, cat]` to `cat, [cat, fox]`.
