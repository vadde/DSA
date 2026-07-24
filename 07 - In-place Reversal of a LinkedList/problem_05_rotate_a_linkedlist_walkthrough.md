# 🚶‍♂️ Walkthrough: Rotate a LinkedList

## 👶 Explain Like I'm 5
You have a line of friends holding hands again: **1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 4 $\rightarrow$ 5**.
You want to "rotate" the line to the right by 2.
This means the last 2 friends in the line (4 and 5) get detached from the back and moved to the very front of the line!
Result: **4 $\rightarrow$ 5 $\rightarrow$ 1 $\rightarrow$ 2 $\rightarrow$ 3**.

How do we do this easily?
Imagine taking the last friend (5) and having them reach out to hold the first friend's hand (1).
Now they are standing in a perfect circle! **(1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 4 $\rightarrow$ 5 $\rightarrow$ 1...)**
To make the line straight again, we just need to break the circle at the right spot.
Since 2 friends moved to the front, that means the remaining 3 friends (5 - 2 = 3) stayed at the back. 
So we walk exactly 3 steps from the start, break the hand-hold there, and whatever is next becomes the new front of the line!

## 🎯 Core Strategy
This doesn't actually require the standard node-by-node reversal! Instead, we can elegantly solve this by temporarily converting the Singly LinkedList into a **Circular LinkedList**.

1. **Find Length & Tail**: Traverse the entire list to find its `length` and the last node (`tail`).
2. **Normalize $K$**: If someone asks to rotate a line of 5 people by 12 steps, it's the exact same as rotating it by 2 steps ($12 \pmod 5 = 2$). So, `k = k % length`. If $K = 0$, we just return the head because the list doesn't change!
3. **Form a Circle**: Connect the end to the beginning: `tail.next = head`.
4. **Find the Break Point**: 
   - The new tail of the list will be at position `length - k`.
   - We walk from `head` for `(length - k) - 1` steps to land exactly on this `new_tail`.
5. **Break the Circle**: 
   - The node directly after our `new_tail` is the `new_head`!
   - We break the circle by setting `new_tail.next = None`.
6. Return the `new_head`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `1 -> 2 -> 3 -> 4 -> 5`, $K = 2$.

### Phase 1: Setup
- Traverse to find `length`: 5. `tail` is pointing at `5`.
- Normalize $K$: `2 % 5 = 2`.
- Form Circle: `tail.next = head`. (Node 5 now points to Node 1).

### Phase 2: Break the Circle
- Calculate steps to new tail: `length - k` = `5 - 2` = 3.
- Walk `3 - 1 = 2` steps from the head:
  - Start at `head` (1).
  - Step 1: `new_tail = 2`.
  - Step 2: `new_tail = 3`.
- The new head is `new_tail.next`, which is `4`.
- Break the circle: `new_tail (3).next = None`.

Result: `new_head` is `4`. The list is `4 -> 5 -> 1 -> 2 -> 3 -> null`.

## 📊 Visual Diagram
Here is a visualization of the circle-breaking logic:

```mermaid
flowchart TD
    subgraph Step 1: Form a Circle
        C1["1 -> 2 -> 3 -> 4 -> 5"]
        N1["Connect 5 to 1!"]
    end
    
    subgraph Step 2: Find the Break Point
        C2["1 -> 2 -> 3 (new_tail) -> 4 (new_head) -> 5"]
        N2["Walk (length - k) steps: 5 - 2 = 3.\nLand on Node 3."]
    end
    
    subgraph Step 3: Break the Circle
        C3["4 -> 5 -> 1 -> 2 -> 3 -> null"]
        N3["Set 3.next = null.\nReturn 4!"]
    end
    
    Step 1: Form a Circle --> Step 2: Find the Break Point
    Step 2: Find the Break Point --> Step 3: Break the Circle
    
    style N1 fill:#fff9c4,color:#000
    style N2 fill:#fff9c4,color:#000
    style N3 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N)$. We do one full pass to find the length and the tail, and then a partial pass (at most $N$ steps) to find the new tail. Total time is $O(N)$.
- **Space Complexity:** $O(1)$. We are only manipulating existing pointers in place.

### Edge Cases Handled Safely
- **$K$ is much larger than length:** e.g., $K = 7$, Length = 5. `k % length` gracefully turns $K$ into 2.
- **$K$ is exactly a multiple of length:** e.g., $K = 5$, Length = 5. `k % length` turns $K$ into 0. The check `if k == 0: return head` instantly catches this and does zero work!
- **Empty list or single node:** Handled immediately at the top `if not head or not head.next: return head`.
