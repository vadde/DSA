# 🚶‍♂️ Walkthrough: Longest Consecutive Sequence

## 👶 Explain Like I'm 5
You have a bucket of completely random numbers: `[100, 4, 200, 1, 3, 2]`.
You want to find the longest sequence of numbers that count up by 1.
In this bucket, the longest sequence is `1, 2, 3, 4` (length 4).

How do we do this without sorting the bucket? (Sorting takes too long, $O(N \log N)$).
First, we pour the bucket into a magical Hash Set. A Set is just a Hash Map that only stores Keys (no Values). It lets us ask "Do you have this number?" instantly.
Then, we pick up a number, like `4`. We ask: "Is `3` in the Set?"
If `3` IS in the set, that means `4` is NOT the beginning of a sequence! It's just the middle or end. So we ignore `4` for now.
But if we pick up `1` and ask "Is `0` in the set?" The answer is NO!
That means `1` is the glorious START of a new sequence!
Since we found a starting line, we just start counting up: "Do you have 2? 3? 4? 5?" until the set says NO.
We keep track of the longest streak we find.

## 🎯 Core Strategy
This is the premier **Hash Set** problem. A Hash Set gives us $O(1)$ constant time lookups. We use this to identify the *start* of a sequence, and then build the sequence from there.

1. **Build Hash Set**: Convert the input array into a `nums_set` (a Hash Set). This removes duplicates and allows $O(1)$ lookups.
2. Initialize `longest_streak = 0`.
3. Loop through every `num` in the `nums_set`:
   - **Identify the Start**: Check if `num` is the START of a sequence. It is the start ONLY if `num - 1` is NOT in the set.
   - If it is the start:
     - Initialize `current_num = num` and `current_streak = 1`.
     - **Count Up**: While `current_num + 1` IS in the set:
       - Increment `current_num` and `current_streak`.
     - Update our record: `longest_streak = max(longest_streak, current_streak)`.
4. Return `longest_streak`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `nums = [100, 4, 200, 1, 3, 2]`
`nums_set` = `{1, 2, 3, 4, 100, 200}`

| `num` | Is `num - 1` in set? | Action | `longest_streak` |
|-------|----------------------|--------|------------------|
| `100` | `99` not in set. YES!| Start sequence. `101` in set? No. Streak is 1. | 1 |
| `4` | `3` is in set. NO. | Skip! `4` is not a start. | 1 |
| `200` | `199` not in set. YES!| Start sequence. `201` in set? No. Streak is 1. | 1 |
| `1` | `0` not in set. YES! | Start sequence. <br>`2` in set? Yes. <br>`3` in set? Yes. <br>`4` in set? Yes. <br>`5` in set? No. Streak is 4. | **4** |
| `3` | `2` is in set. NO. | Skip! | 4 |
| `2` | `1` is in set. NO. | Skip! | 4 |

Loop finishes. Return 4.

## 📊 Visual Diagram
Here is how the algorithm avoids doing extra work by skipping numbers that aren't the start:

```mermaid
flowchart TD
    subgraph Iteration
        W1["Looping through set: {1, 2, 3, 4, 100, 200}"]
    end
    
    subgraph Is it a Start?
        N1["num = 4. Is 3 in set? YES.\n4 is NOT a start. Ignore it!"]
        N2["num = 1. Is 0 in set? NO.\n1 IS a start!"]
    end
    
    subgraph The Build Phase
        N3["Build from 1:\nFound 2!\nFound 3!\nFound 4!\n5 not found. Streak is 4."]
    end
    
    Iteration --> Is it a Start?
    Is it a Start? --> N1
    Is it a Start? --> N2
    N2 --> N3
    
    style N1 fill:#ffcdd2,color:#000
    style N2 fill:#fff9c4,color:#000
    style N3 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We build the set in $O(N)$. Then we loop through the set. We ONLY enter the `while` loop if we are at the start of a sequence. Thus, the `while` loop only runs for the exact length of that sequence. Every number is visited at most twice (once in the outer loop, and once in the inner `while` loop). $O(N + N) = O(N)$.
- **Space Complexity:** $O(N)$ because we pour all the numbers into a Hash Set.

### Edge Cases Handled Safely
- **Empty Array:** Handled by `if not nums: return 0` at the very top.
- **Array with Duplicates:** `[1, 2, 0, 1]`. The `set(nums)` automatically removes the duplicates! It becomes `{0, 1, 2}`. Then it correctly identifies `0` as the start, and counts up to `2`, returning length `3`. Perfectly handled.
