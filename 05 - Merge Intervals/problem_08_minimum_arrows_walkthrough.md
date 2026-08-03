# 🚶‍♂️ Walkthrough: Minimum Number of Arrows to Burst Balloons

## 👶 Explain Like I'm 5
Imagine there are several long balloons taped to a wall. You have a bow and arrow. When you shoot an arrow straight up, it pops EVERY balloon it touches on its way up! 
You want to pop all the balloons using the FEWEST arrows possible.

To pop the most balloons with a single arrow, you want to wait as long as possible before shooting. Specifically, you should shoot at the exact moment the FIRST balloon in your line of sight is about to end. 
If you shoot there, you pop that balloon, AND you pop any other balloons that have already started!
To do this easily, we DON'T sort the balloons by when they start. We sort the balloons by when they **END**. Then we just shoot an arrow at the end of the first balloon, and skip over all other balloons that get popped by that arrow!

## 🎯 Core Strategy
This uses a **Greedy Strategy** by sorting intervals by their **END time**.
1. **Sort** the balloons based on their `end` time, not `start` time.
2. Initialize `arrows = 1`. (Assuming there is at least one balloon, we always need at least one arrow).
3. Set `current_arrow_pos = balloons[0].end`. This is where we aggressively shoot our first arrow.
4. Loop through the remaining balloons:
   - **Missed!**: If the next balloon starts strictly AFTER our `current_arrow_pos` (`balloon.start > current_arrow_pos`):
     - Our current arrow completely missed this balloon! We need to shoot a new one.
     - Increment `arrows += 1`.
     - Update our new shooting spot to the end of this new balloon: `current_arrow_pos = balloon.end`.
   - **Popped!**: If the next balloon starts BEFORE or EXACTLY ON the `current_arrow_pos` (`balloon.start <= current_arrow_pos`), it gets popped by our current arrow! We do absolutely nothing and move to the next balloon.
5. Return the total number of `arrows`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `balloons = [[10, 16], [2, 8], [1, 6], [7, 12]]`
1. **Sort by End Time**: `[[1, 6], [2, 8], [7, 12], [10, 16]]`
2. Initialize: `arrows = 1`, `current_arrow_pos = 6` (End of the first balloon).

| Step | Current Balloon | Arrow Position | Balloon Start > Arrow? | Action (New Arrow?) | Arrow Pos State | `arrows` Count |
|------|-----------------|----------------|------------------------|---------------------|-----------------|----------------|
| 1 | `[2, 8]` | `6` | `2 > 6`? No. | Popped! Do nothing. | `6` | `1` |
| 2 | `[7, 12]` | `6` | `7 > 6`? **YES!** | Missed! New arrow. | `12` | `2` |
| 3 | `[10, 16]`| `12` | `10 > 12`? No. | Popped! Do nothing. | `12` | `2` |

Result: `2` arrows.

## 📊 Visual Diagram
Here is why sorting by **End Time** is the secret sauce:

```mermaid
flowchart TD
    subgraph Step1 [Step 1: Sort by END Time]
        W1["1. [1, 6]\n2. [2, 8]\n3. [7, 12]\n4. [10, 16]"]
    end
    
    subgraph Step2 [Step 2: Shoot at End of 1st Balloon]
        W2["Shoot Arrow at x = 6!"]
        N2["Balloon 1 [1, 6] POPPED!\nBalloon 2 [2, 8] POPPED!"]
    end
    
    subgraph Step3 [Step 3: Balloon 3 Survives]
        W3["Balloon 3 [7, 12] starts at 7."]
        N3["7 > 6. It survived!\nShoot new Arrow at x = 12!"]
    end

Step1 --> Step2
Step2 --> Step 3
    
    style W2 fill:#ffcdd2,color:#000
    style N3 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \log N)$. Sorting the balloons by their end times takes $O(N \log N)$. The subsequent greedy pass only loops through the array once, taking $O(N)$ time. The total complexity is dominated by the sort.
- **Space Complexity:** $O(N)$ or $O(\log N)$ depending on the underlying sorting algorithm used by the language (Python's Timsort uses $O(N)$ space). 

### Edge Cases Handled Safely
- **Balloons exactly touch boundaries:** e.g., `[1, 2]` and `[2, 3]`. Arrow shoots at `x=2`. For the second balloon, `start (2) > arrow (2)` is False. The code perfectly recognizes that a single arrow shot exactly at the boundary pops both!
- **Empty List:** Fast-path `if not balloons: return 0` handles it safely.
