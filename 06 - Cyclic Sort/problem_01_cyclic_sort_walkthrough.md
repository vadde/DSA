# 🚶‍♂️ Walkthrough: Cyclic Sort

## 👶 Explain Like I'm 5
You have a bunch of numbered boxes mixed up in a row. The numbers on the boxes are exactly 1, 2, 3, up to $N$. 
You want to put Box 1 in the 1st spot, Box 2 in the 2nd spot, and so on.

Instead of looking at all the boxes at once and getting confused, you just look at the box in the **1st spot**.
If it's Box 4, you say, "Hey! You belong in the 4th spot!" So you take Box 4 and swap it with whatever box is currently sitting in the 4th spot.
Now you look at the 1st spot again (it has a new box in it now). Is it Box 1 yet? If not, keep swapping it with the spot where it belongs! 
Once Box 1 is finally in the 1st spot, you move on to the 2nd spot and repeat. 
Eventually, every box gets swapped exactly once into its perfect home.

## 🎯 Core Strategy
When you are given an array of numbers in a known range (like $1$ to $N$), the **Cyclic Sort** pattern is the most powerful $O(N)$ sorting algorithm because it uses the numbers *themselves* as indices.

1. Initialize a pointer `i = 0`.
2. Loop through the array using a `while` loop (because we only want to move `i` forward when a condition is met).
3. The correct index for the number `nums[i]` is `nums[i] - 1` (because numbers start at 1, but array indices start at 0). Let's call this correct index `j`.
4. **Not Happy**: If `nums[i]` is NOT currently sitting at its correct index `j` (`nums[i] != nums[j]`):
   - Swap `nums[i]` and `nums[j]`.
   - Do NOT increment `i` yet! The new number we just swapped into index `i` might still be wrong, so we have to check it again on the next loop.
5. **Happy**: If `nums[i]` IS at its correct index:
   - Everything is perfect here. Increment `i += 1`.
6. Return the sorted array.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `nums = [3, 1, 5, 4, 2]`
Initialization: `i = 0`.

| Step | `i` | `nums[i]` | Correct Index `j` (`nums[i] - 1`) | Is it Happy? (`nums[i] == nums[j]`) | Action | Array State |
|------|-----|-----------|-----------------------------------|-------------------------------------|--------|-------------|
| 1 | `0` | `3` | `3 - 1 = 2` | No. `nums[0] != nums[2]` (`3 != 5`) | Swap index 0 and 2. | `[5, 1, 3, 4, 2]` |
| 2 | `0` | `5` | `5 - 1 = 4` | No. `nums[0] != nums[4]` (`5 != 2`) | Swap index 0 and 4. | `[2, 1, 3, 4, 5]` |
| 3 | `0` | `2` | `2 - 1 = 1` | No. `nums[0] != nums[1]` (`2 != 1`) | Swap index 0 and 1. | `[1, 2, 3, 4, 5]` |
| 4 | `0` | `1` | `1 - 1 = 0` | **YES!** `nums[0] == nums[0]` | `i += 1`. | `[1, 2, 3, 4, 5]` |
| 5 | `1` | `2` | `2 - 1 = 1` | **YES!** | `i += 1`. | `[1, 2, 3, 4, 5]` |
| 6 | `2` | `3` | `3 - 1 = 2` | **YES!** | `i += 1`. | `[1, 2, 3, 4, 5]` |
| 7 | `3` | `4` | `4 - 1 = 3` | **YES!** | `i += 1`. | `[1, 2, 3, 4, 5]` |
| 8 | `4` | `5` | `5 - 1 = 4` | **YES!** | `i += 1`. Loop ends. | `[1, 2, 3, 4, 5]` |

Result: `[1, 2, 3, 4, 5]`

## 📊 Visual Diagram
Here is how the first index aggressively swaps until it finds the right number:

```mermaid
flowchart TD
    subgraph Step1 [Step 1: Index 0 has '3']
        W1["Array: [3, 1, 5, 4, 2]"]
        N1["3 belongs at index 2!\nSwap 3 and 5."]
    end
    
    subgraph Step2 [Step 2: Index 0 has '5']
        W2["Array: [5, 1, 3, 4, 2]"]
        N2["5 belongs at index 4!\nSwap 5 and 2."]
    end
    
    subgraph Step3 [Step 3: Index 0 has '2']
        W3["Array: [2, 1, 3, 4, 5]"]
        N3["2 belongs at index 1!\nSwap 2 and 1."]
    end
    
    subgraph Step4 [Step 4: Index 0 has '1']
        W4["Array: [1, 2, 3, 4, 5]"]
        N4["1 belongs at index 0!\nIt is HAPPY! Move i forward."]
    end

Step1 --> Step2
Step2 --> Step 3
    Step3 --> Step4

styleW1fill:#ffcdd2,color:#000
    style W2 fill:#ffcdd2,color:#000
    style W3 fill:#ffcdd2,color:#000
    style W4 fill:#c8e6c9,color:#000
    style N4 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. Even though there is a `while` loop containing an `if/else`, every single time a swap happens, at least one number is permanently placed in its correct, final position. Since there are $N$ numbers, there can be at most $N-1$ swaps. The outer `while` loop iterates $N$ times. Total operations bounded by $2N \rightarrow O(N)$.
- **Space Complexity:** $O(1)$. All sorting is done in-place by swapping elements. No extra memory is used.

### Edge Cases Handled Safely
- **Already Sorted:** `[1, 2, 3, 4, 5]`. The `if nums[i] != nums[j]` condition will always be false. `i` will increment $N$ times with 0 swaps.
- **Reverse Order:** `[5, 4, 3, 2, 1]`. Performs exactly $O(N)$ swaps, constantly tossing the numbers into their proper buckets.
