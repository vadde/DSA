# 🚶‍♂️ Walkthrough: Count Substrings with All Three Characters

## 👶 Explain Like I'm 5
Imagine you need to buy an Apple, a Banana, and a Carrot. You are walking down a long row of fruit stands. You walk from the left to the right. As soon as you have bought at least one of each item, you are happy!

But here's the trick: if you are happy right now, you would STILL be happy if you kept walking and bought even MORE fruits from the stands further down the road! 
So, instead of just saying "Yes, I found one happy stretch of stands", we can instantly count **ALL** the longer stretches down the road that start from the exact same place! We add that massive number to our total score in a single math operation. 
Then, we step away from the very first stand we visited to see if the remaining stands in our hands still make us happy.

## 🎯 Core Strategy
This uses a **Dynamic-Size Sliding Window** combined with a very powerful **Mathematical Counting Trick**.
1. Initialize `window_start = 0`, `total_substrings = 0`, and a dictionary to count `a`, `b`, and `c`. Let $N$ be the length of the string.
2. Iterate `window_end` through the string, incrementing the count of the incoming character.
3. Check if the window is valid: `while counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0`.
4. **The Math Trick**: The current window from `window_start` to `window_end` contains at least one of each character. Therefore, any substring starting at `window_start` and ending at `window_end` **or any index after it** is ALSO valid!
   - How many substrings is that? It's exactly the number of characters from `window_end` to the end of the string.
   - We calculate this as `N - window_end` and add it directly to `total_substrings`.
5. Shrink the window from the left by decrementing the count of `s[window_start]` and moving `window_start` forward.
6. The loop continues until the condition fails, and then we go back to expanding `window_end`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `s = "aaacb"`. Length $N = 5$.
Initialization: `start = 0`, `total = 0`, `counts = {a:0, b:0, c:0}`

| Step | `end` char | `counts` state | All 3 > 0? | Math Trick (Add to total) & Shrink |
|------|------------|----------------|------------|------------------------------------|
| 1 | `0` ('a') | `{a:1, b:0, c:0}` | No | Expand. |
| 2 | `1` ('a') | `{a:2, b:0, c:0}` | No | Expand. |
| 3 | `2` ('a') | `{a:3, b:0, c:0}` | No | Expand. |
| 4 | `3` ('c') | `{a:3, b:0, c:1}` | No | Expand. |
| 5 | `4` ('b') | `{a:3, b:1, c:1}` | **YES!** | *SHRINK LOOP START* (Window: `aaacb`) |

**Inside the Shrink Loop (at `end = 4`):**
1. Valid! Add `5 - 4 = 1`. (`total = 1`). Valid string: `[aaacb]`.
   - Drop `s[0]` ('a'). `counts={a:2, b:1, c:1}`. `start = 1`.
2. Valid! Add `5 - 4 = 1`. (`total = 2`). Valid string: `[aacb]`.
   - Drop `s[1]` ('a'). `counts={a:1, b:1, c:1}`. `start = 2`.
3. Valid! Add `5 - 4 = 1`. (`total = 3`). Valid string: `[acb]`.
   - Drop `s[2]` ('a'). `counts={a:0, b:1, c:1}`. `start = 3`.
4. Not valid! Loop breaks.

Result: `total = 3`.

## 📊 Visual Diagram
Here is a visualization of the Mathematical Counting Trick:

```mermaid
flowchart TD
    subgraph State 1 [Valid Window found!]
        W1["String: a, b, c, a, b, c\nWindow: [a, b, c], a, b, c\nend = 2. N = 6."]
    end
    
    subgraph Math [The Counting Trick]
        W2["Since [a,b,c] is valid, so are:\n1. [a,b,c]\n2. [a,b,c,a]\n3. [a,b,c,a,b]\n4. [a,b,c,a,b,c]"]
        N2["Total added: 6 - 2 = 4!"]
    end
    
    subgraph Shrink [Shrink to find more]
        W3["Drop first 'a'. Window: b, c...\nExpand to find next 'a'"]
    end
    
    State 1 --> Math
    Math --> Shrink
    
    style W2 fill:#32CD32,color:#000
    style N2 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. The `window_end` pointer iterates over the string once from left to right. The `window_start` pointer also moves from left to right, iterating over the string at most once. Hash map operations (with exactly 3 keys) take $O(1)$. Total operations are proportional to $2N$, which is strictly linear.
- **Space Complexity:** $O(1)$. The dictionary always stores exactly 3 keys (`'a'`, `'b'`, `'c'`), regardless of the size of the input string. This requires constant space.

### Edge Cases Handled Safely
- **Missing Characters:** e.g., `s = "aaaaaaa"`. The counts for `'b'` and `'c'` will remain `0`. The `while` loop condition will never evaluate to `True`. The function safely and quickly returns `0`.
- **String smaller than 3 characters:** `s = "ab"`. The `while` loop will never be entered. Returns `0`.
