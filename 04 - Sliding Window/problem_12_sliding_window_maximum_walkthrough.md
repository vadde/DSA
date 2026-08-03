# 🚶‍♂️ Walkthrough: Sliding Window Maximum

## 👶 Explain Like I'm 5
Imagine you are looking at a line of kids of different heights through a small window that only shows $K$ kids at a time. 
As you slide the window from left to right, you want to write down the height of the **tallest kid** you can see in the window at each step.

The tricky part is: when you slide the window right, the tallest kid might step *out* of the left side of your window. When that happens, how do you quickly know who the *second* tallest kid was without having to look at all the kids in the window again?

To solve this, we keep a "VIP Line" (a Deque). 
Whenever a new kid enters the window, they kick out anyone in the VIP line who is shorter than them (because the shorter kids arrived earlier and are shorter, so they will *never* be the tallest kid in any future window!). 
Because of this ruthless kicking, the VIP line is always sorted from tallest to shortest. The person at the front of the VIP line is ALWAYS the tallest kid currently in the window!

## 🎯 Core Strategy
This uses a **Fixed-Size Sliding Window** paired with a **Monotonic Deque** (Double-Ended Queue). "Monotonic" just means the elements inside the deque are strictly increasing or decreasing (in our case, strictly decreasing).
*Note: We store the **indices** of the elements in the deque, not the actual values, so we can easily check if an element has fallen out of the left side of our window.*

1. Initialize `window_start = 0`, a `result` array, and an empty `dq` (deque).
2. Iterate `window_end` through the array.
3. **Clean the VIP Line (Pop from Back)**: Before adding the current element `nums[window_end]`, look at the back of the deque. If the element at the back is $\le$ the current element, `pop` it! Keep doing this until the back element is strictly greater or the deque is empty.
4. Add the current element's index (`window_end`) to the back of the deque.
5. **Record & Shrink (If window size reached $K$)**: 
   - The maximum element in the window is guaranteed to be at the front of the deque! Append `nums[dq[0]]` to `result`.
   - Now, we need to slide the window forward. Look at the front of the deque. If `dq[0] == window_start`, it means the max element is about to fall out of our sliding window. `popleft()` to remove it!
   - Increment `window_start`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`
Initialization: `start = 0`, `result = []`, `dq = []`

| Step | `end` | `nums[end]` | Deque Action (Pop small, Add index) | Deque State (Indices) | Deque State (Values) | `start` / Record (if size=3) |
|------|-------|-------------|-------------------------------------|-----------------------|----------------------|------------------------------|
| 1 | `0` | `1` | Add `0`. | `[0]` | `[1]` | Size < 3. |
| 2 | `1` | `3` | `3 > 1`. Pop `0`. Add `1`. | `[1]` | `[3]` | Size < 3. |
| 3 | `2` | `-1` | `-1 < 3`. Add `2`. | `[1, 2]` | `[3, -1]` | Max is `nums[1]` (**3**). <br> `start` stays 0 (1 != 0). `start`->1. |
| 4 | `3` | `-3` | `-3 < -1`. Add `3`. | `[1, 2, 3]` | `[3, -1, -3]` | Max is `nums[1]` (**3**). <br> `dq[0]` is `1` (`start`). Popleft! `start`->2. |
| 5 | `4` | `5` | `5 > -3`, pop. `5 > -1`, pop. Add `4`. | `[4]` | `[5]` | Max is `nums[4]` (**5**). <br> `start` stays 2. `start`->3. |
| 6 | `5` | `3` | `3 < 5`. Add `5`. | `[4, 5]` | `[5, 3]` | Max is `nums[4]` (**5**). <br> `start` stays 3. `start`->4. |
| 7 | `6` | `6` | `6 > 3`, pop. `6 > 5`, pop. Add `6`.| `[6]` | `[6]` | Max is `nums[6]` (**6**). <br> `start` stays 4. `start`->5. |
| 8 | `7` | `7` | `7 > 6`, pop. Add `7`. | `[7]` | `[7]` | Max is `nums[7]` (**7**). |

Result: `[3, 3, 5, 5, 6, 7]`

## 📊 Visual Diagram
Here is how the Monotonic Deque dynamically maintains the maximums:

```mermaid
flowchart TD
    subgraph Step3 [Step 3: Window: 1, 3, -1.  end=2, nums= -1]
        W1["Deque Values: [3, -1]"]
        N1["-1 is smaller than 3, so it joins the line.\nMax is front: 3"]
    end
    
    subgraph Step4 [Step 4: Window: 3, -1, -3.  end=3, nums= -3]
        W2["Deque Values: [3, -1, -3]"]
        N2["Max is front: 3. But 3 is at window_start!\nPopleft! Deque becomes [-1, -3]"]
    end
    
    subgraph Step5 [Step 5: Window: -1, -3, 5. end=4, nums= 5]
        W3["New item '5' is larger than -3 and -1!"]
        N3["Pop -3! Pop -1! Add 5!\nDeque Values: [5]\nMax is front: 5"]
    end

Step3 --> Step4
Step4 --> Step 5
    
    style W1 fill:#e1f5fe,color:#000
    style W2 fill:#e1f5fe,color:#000
    style W3 fill:#ffcdd2,color:#000
    style N3 fill:#32CD32,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. At first glance, there is a `while` loop inside a `for` loop, which might look like $O(N^2)$. However, every element is pushed to the deque exactly *once* and popped from the deque at most *once*. Thus, across the entire $O(N)$ loop, the inner `while` loop runs a total of $O(N)$ times. $O(2N) = O(N)$.
- **Space Complexity:** $O(K)$. The deque only stores indices of elements within the current window of size $K$. Therefore, it uses space proportional to $K$.

### Edge Cases Handled Safely
- **`k = 1`:** The max of a window of size 1 is just the element itself. Handled gracefully with a fast-path `if k == 1: return nums`.
- **Strictly Decreasing Array:** e.g., `[5, 4, 3, 2]`. The deque just naturally fills up to size $K$ without popping from the back, and pops from the front as the window slides.
- **Strictly Increasing Array:** e.g., `[1, 2, 3, 4]`. The deque instantly pops the old element every single time, so it always has a size of `1` containing the most recent element. Perfectly efficient!
