# 🧠 The Pattern Cracker: Your Mental Model for DSA

> **The One Rule**: You don't need to memorize 43 patterns. You need to memorize **5 questions** and let them guide you to the right pattern in under 10 seconds.

---

## 🔑 Layer 1: The 5-Second Decision Framework

When you read ANY problem, ask these 5 questions **in order**. Each question eliminates 80% of wrong patterns.

### Question 1: "What is the INPUT?"

| Input Type | Patterns to Consider |
|---|---|
| **Sorted Array / Sorted List** | Two Pointers, Binary Search |
| **Unsorted Array** | Sliding Window, Prefix Sum, Two Pointers, Cyclic Sort, Counting, Monotonic Stack |
| **String** | Sliding Window, Two Pointers, Trie, Backtracking |
| **Linked List** | Fast & Slow, In-place Reversal, Clone |
| **Tree** | BFS, DFS, Two Heaps, Serialize/Deserialize |
| **Graph / Dependencies** | BFS/DFS, Topological Sort, Union Find, Articulation Points |
| **Matrix / Grid** | Island (Matrix Traversal), BFS/DFS |
| **Intervals** | Merge Intervals, Greedy |
| **Numbers / Bits** | Bitwise XOR, Math |
| **Multiple Sorted Lists** | K-way Merge, Two Heaps |

### Question 2: "What is the OUTPUT asking for?"

| Output Type | Pattern Signal |
|---|---|
| **"Find a pair/triplet that..."** | Two Pointers |
| **"Find longest/shortest subarray..."** | Sliding Window |
| **"Find all combinations/permutations..."** | Subsets / Backtracking |
| **"Find the Kth largest/smallest..."** | Top K / Heap |
| **"Find if a path/cycle exists..."** | BFS / DFS / Fast & Slow |
| **"Find the minimum/maximum of..."** | Binary Search / DP / Greedy |
| **"Count the number of ways..."** | DP (Knapsack / Fibonacci) |
| **"Find the order to do tasks..."** | Topological Sort |
| **"Group connected components..."** | Union Find |
| **"Find sum of range / update range..."** | Segment Tree / BIT / Prefix Sum |

### Question 3: "Is there a CONSTRAINT I can exploit?"

| Constraint | What It Tells You |
|---|---|
| **"Array is sorted"** | Binary Search or Two Pointers |
| **"Numbers are in range [1, N]"** | Cyclic Sort (use index as hash!) |
| **"Return in O(N) time"** | Hash Map, Two Pointers, Sliding Window |
| **"Return in O(N log N) time"** | Sorting + Two Pointers, or Heap |
| **"Subarray must be contiguous"** | Sliding Window or Prefix Sum |
| **"Subsequence (not contiguous)"** | DP or Two Pointers |
| **"Tree is a BST"** | In-Order Traversal gives sorted order |
| **"Graph is a DAG"** | Topological Sort |
| **"Modify in-place, O(1) space"** | Two Pointers, Cyclic Sort, In-place Reversal |

### Question 4: "Do I need to REMEMBER something?"

| What to Remember | Pattern |
|---|---|
| **"Previous elements I've seen"** | Hash Map, Stack |
| **"Running total / cumulative"** | Prefix Sum |
| **"Minimum/Maximum so far"** | Monotonic Stack / Queue |
| **"Frequency of elements"** | Hash Map, Counting |
| **"Parent / Group membership"** | Union Find |
| **"State at step i depends on step i-1"** | Dynamic Programming |

### Question 5: "Does the problem SHRINK?"

| How It Shrinks | Pattern |
|---|---|
| **"I can cut the search space in half"** | Binary Search |
| **"I can make a choice and recurse"** | Backtracking / DFS |
| **"I can solve smaller subproblems first"** | Dynamic Programming |
| **"I can greedily pick the best local option"** | Greedy |

---

## 🎯 Layer 2: The Trigger Word Cheat Sheet

> **How to use**: Scan the problem statement for these exact keywords. They are almost always a dead giveaway.

### Instant Triggers (One keyword = One pattern)

| 🔍 When You See... | 💡 Think... | 🏷️ Pattern |
|---|---|---|
| "pair", "triplet", "two sum" | Shrink from both ends | **Two Pointers** |
| "cycle in linked list", "middle of list" | Tortoise and Hare | **Fast & Slow** |
| "longest substring with K distinct" | Expand right, shrink left | **Sliding Window** |
| "merge intervals", "overlapping" | Sort by start, merge greedily | **Merge Intervals** |
| "missing number", "duplicate", "range [1,N]" | Put each number at its index | **Cyclic Sort** |
| "reverse a linked list", "reverse between" | prev/curr/next dance | **In-place Reversal** |
| "next greater element", "daily temperatures" | Pop smaller, push current | **Monotonic Stack** |
| "level order", "zigzag level" | Queue with level size | **Tree BFS** |
| "max depth", "path sum", "diameter" | Recurse left + right | **Tree DFS** |
| "number of islands", "flood fill" | DFS/BFS on grid, mark visited | **Island Traversal** |
| "median of stream", "sliding window median" | Max-heap + Min-heap | **Two Heaps** |
| "all subsets", "power set" | Include/Exclude each element | **Subsets** |
| "search in rotated sorted array" | Modified binary search | **Binary Search** |
| "single number", "missing number (XOR)" | a ⊕ a = 0 | **Bitwise XOR** |
| "Kth largest", "K closest", "top K frequent" | Min-heap of size K | **Top K** |
| "merge K sorted lists" | Min-heap of K heads | **K-way Merge** |
| "minimum platforms", "task scheduler" | Sort + greedy pick | **Greedy** |
| "coin change", "0/1 knapsack", "subset sum" | Include/Exclude with memo | **0-1 Knapsack DP** |
| "climb stairs", "house robber" | dp[i] = dp[i-1] + dp[i-2] | **Fibonacci DP** |
| "longest palindromic subsequence" | 2D DP on string | **Palindromic DP** |
| "N-Queens", "generate parentheses", "sudoku" | Place, recurse, undo | **Backtracking** |
| "autocomplete", "word search II", "prefix" | Character-by-character tree | **Trie** |
| "course schedule", "build order" | In-degree + BFS queue | **Topological Sort** |
| "number of connected components", "redundant edge" | find() + union() | **Union Find** |
| "subarray sum equals K" | prefix[j] - prefix[i] = K | **Prefix Sum** |
| "sliding window maximum" | Deque maintaining decreasing order | **Monotonic Queue** |
| "serialize tree", "encode/decode" | Pre-order + null markers | **Serialize/Deserialize** |
| "clone graph", "copy list with random pointer" | Old→New mapping | **Clone** |
| "critical connections", "bridges" | Tarjan's DFS | **Articulation Points** |
| "range sum query mutable" | Tree over array | **Segment Tree / BIT** |

---

## 🧬 Layer 3: The Pattern DNA Cards

> **How to use**: Once you've identified the pattern, recall its "DNA" — the core variables, the loop structure, and the invariant (the rule that NEVER breaks).

---

### 🟢 TWO POINTERS
```
Variables:  left = 0, right = len - 1
Loop:       while left < right
Move:       Shrink inward based on condition
Invariant:  Answer lies between [left, right]
Template:   if condition → move left++, else → move right--
```
**When sorted**: Classic shrink-from-both-ends.
**When unsorted**: Sort first, THEN use two pointers.
**Gotcha**: Don't forget to handle duplicates (skip while `nums[left] == nums[left-1]`).

---

### 🟢 FAST & SLOW POINTERS
```
Variables:  slow = head, fast = head
Loop:       while fast and fast.next
Move:       slow = slow.next, fast = fast.next.next
Invariant:  Fast moves 2x speed. If cycle exists, they WILL meet.
```
**Cycle detection**: If they meet → cycle exists. Entry point: reset slow to head, move both at speed 1.
**Middle of list**: When fast reaches end, slow is at the middle.
**Gotcha**: Always check `fast AND fast.next` to avoid null pointer crashes.

---

### 🟡 SLIDING WINDOW
```
Variables:  left = 0, result = 0, window_state = {}
Loop:       for right in range(len)
Expand:     Add nums[right] to window_state
Shrink:     while window is INVALID → remove nums[left], left++
Update:     result = max/min(result, right - left + 1)
Invariant:  Window [left, right] always represents a VALID candidate.
```
**Fixed size window**: Shrink when `right - left + 1 > K`.
**Variable size window**: Shrink when window violates constraint.
**Gotcha**: Update result AFTER shrinking, not before. The window must be valid when you record the answer.

---

### 🟡 MERGE INTERVALS
```
Variables:  sorted_intervals, merged = [first]
Loop:       for each interval starting from second
Check:      if current.start <= merged[-1].end → OVERLAP
Merge:      merged[-1].end = max(merged[-1].end, current.end)
Else:       Append current to merged
```
**Gotcha**: Sort by START first. Use `max()` for the end, not just overwrite.

---

### 🟡 CYCLIC SORT
```
Variables:  i = 0
Loop:       while i < len(nums)
Check:      if nums[i] != i + 1 → swap nums[i] with nums[nums[i] - 1]
Else:       i++
Invariant:  After loop, nums[i] == i + 1 for all valid positions.
```
**The magic**: Numbers in range [1, N] can be used as their OWN index.
**Gotcha**: Swap in a `while` loop (not `if`), because the swapped-in element may also be wrong.

---

### 🟡 MONOTONIC STACK
```
Variables:  stack = [], result = []
Loop:       for i in range(len)
Pop:        while stack and nums[stack[-1]] < nums[i] → pop, record answer
Push:       stack.append(i)
Invariant:  Stack is always in decreasing (or increasing) order.
```
**"Next Greater Element"**: Decreasing stack. Pop when you find something bigger.
**"Next Smaller Element"**: Increasing stack. Pop when you find something smaller.
**Gotcha**: Store INDICES in the stack, not values. You'll need the index to record the answer.

---

### 🔴 BINARY SEARCH
```
Variables:  lo = 0, hi = len - 1
Loop:       while lo <= hi
Mid:        mid = lo + (hi - lo) // 2
Check:      if nums[mid] == target → return mid
Move:       if nums[mid] < target → lo = mid + 1, else → hi = mid - 1
```
**"Search space" trick**: Binary search doesn't need a sorted array! You can binary search on the ANSWER if you can write a function `is_feasible(mid)`.
**Gotcha**: Use `lo + (hi - lo) // 2` to avoid integer overflow. Watch for off-by-one errors with `lo <= hi` vs `lo < hi`.

---

### 🔴 TREE BFS
```
Variables:  queue = deque([root]), level = 0
Loop:       while queue
Level:      level_size = len(queue) → for _ in range(level_size)
Process:    node = queue.popleft(), process node
Expand:     if node.left → queue.append(node.left), same for right
```
**Level order**: The `level_size` loop trick gives you all nodes at one level.
**Gotcha**: Process level_size nodes per iteration, not just one.

---

### 🔴 TREE DFS
```
Template:   def dfs(node):
              if not node: return BASE_CASE
              left = dfs(node.left)
              right = dfs(node.right)
              return COMBINE(left, right, node.val)
```
**Path sum**: Pass running sum down as parameter.
**Diameter**: Track global max, return `1 + max(left, right)` height.
**Gotcha**: Return vs. Side-effect. Some problems need you to update a global variable inside DFS, not just return.

---

### 🔴 DYNAMIC PROGRAMMING (The DP Mantra)

> **Step 1**: Define the STATE. What does `dp[i]` represent?
> **Step 2**: Define the TRANSITION. How does `dp[i]` relate to previous states?
> **Step 3**: Define the BASE CASE. What is `dp[0]`?
> **Step 4**: Define the DIRECTION. Do you fill left→right or right→left?

| DP Type | State | Transition |
|---|---|---|
| **Fibonacci** | `dp[i]` = ways to reach step i | `dp[i] = dp[i-1] + dp[i-2]` |
| **0-1 Knapsack** | `dp[i][w]` = max value with items 0..i, capacity w | `dp[i][w] = max(exclude, include)` |
| **Palindrome** | `dp[i][j]` = answer for substring s[i..j] | `dp[i][j] = dp[i+1][j-1] + condition` |

**Gotcha**: If you can't define the state clearly in one sentence, you haven't understood the problem yet. Go back and re-read.

---

### 🔴 BACKTRACKING
```
Template:   def backtrack(path, choices):
              if GOAL_REACHED: result.append(path[:])
              for choice in choices:
                if is_valid(choice):
                  path.append(choice)       # CHOOSE
                  backtrack(path, ...)       # EXPLORE
                  path.pop()                # UN-CHOOSE ← THIS IS THE KEY
```
**Gotcha**: You MUST undo the choice after recursing. That's what makes it backtracking, not just DFS.

---

### 🔴 TOPOLOGICAL SORT
```
Variables:  in_degree = {}, queue = deque([nodes with in_degree 0])
Loop:       while queue → node = queue.popleft()
Process:    Add node to result
Update:     for neighbor: in_degree[neighbor] -= 1
              if in_degree[neighbor] == 0 → queue.append(neighbor)
Check:      if len(result) != num_nodes → CYCLE EXISTS
```
**Gotcha**: If result length != total nodes, there's a cycle. The problem is unsolvable.

---

### 🔴 UNION FIND
```
Variables:  parent = [i for i in range(N)], rank = [0] * N
find(x):    if parent[x] != x → parent[x] = find(parent[x])  # PATH COMPRESSION
union(x,y): px, py = find(x), find(y) → attach smaller rank to bigger
```
**"Are these connected?"**: `find(a) == find(b)`.
**"How many groups?"**: Count unique roots.
**Gotcha**: Always use path compression AND union by rank. Without them, find() degrades to O(N).

---

## 🚨 Layer 4: The Top 10 Mistakes That Cost You the Interview

| # | Mistake | Fix |
|---|---|---|
| 1 | **Jumping to code before understanding the problem** | Spend 3 minutes asking clarifying questions. Restate the problem in your own words. |
| 2 | **Not handling edge cases: empty input, single element, all same values** | Before coding, write down 3 edge cases. Test your logic mentally against them. |
| 3 | **Off-by-one errors in Binary Search** | Use the template: `lo <= hi`, `mid = lo + (hi - lo) // 2`. Practice 10 times until it's muscle memory. |
| 4 | **Forgetting to mark nodes as visited in BFS/DFS** | Mark visited BEFORE adding to queue, not after popping. This prevents duplicates. |
| 5 | **Using the wrong DP state definition** | If your transition feels forced or wrong, your state is wrong. Redefine `dp[i]`. |
| 6 | **Not sorting first when using Two Pointers** | Two Pointers on an unsorted array is almost always wrong (except for linked lists). |
| 7 | **Confusing Subarray (contiguous) vs Subsequence (not contiguous)** | Subarray → Sliding Window / Prefix Sum. Subsequence → DP / Two Pointers. |
| 8 | **Modifying a collection while iterating over it** | Make a copy first, or iterate over indices, or use a separate "to_delete" list. |
| 9 | **Not considering negative numbers** | Prefix Sum and Sliding Window behave differently with negatives. Sliding Window usually needs all positives. |
| 10 | **Overcomplicating the solution** | If your solution feels like 50+ lines, step back. There's probably a simpler pattern you're missing. |

---

## 🗺️ Layer 5: The One-Page Visual Map

> **Print this. Tape it to your wall. Look at it every day.**

```
                    ┌─────────────────────────────────────────┐
                    │         WHAT IS THE INPUT?              │
                    └─────────────┬───────────────────────────┘
                                  │
          ┌───────────┬───────────┼───────────┬───────────────┐
          ▼           ▼           ▼           ▼               ▼
      ┌───────┐  ┌─────────┐ ┌───────┐  ┌─────────┐   ┌───────────┐
      │ Array │  │Linked   │ │ Tree  │  │  Graph  │   │ Intervals │
      │/String│  │  List   │ │       │  │/Matrix  │   │           │
      └───┬───┘  └────┬────┘ └───┬───┘  └────┬────┘   └─────┬─────┘
          │           │          │            │               │
    ┌─────┴─────┐     │     ┌───┴───┐   ┌────┴────┐    Merge Intervals
    │           │     │     │       │   │         │         │
  Sorted?    Unsorted?│    BFS    DFS  BFS/DFS  Topo     Greedy
    │           │     │     │       │   Islands  Sort
    │           │     │     │       │   Union Find
  Binary    Sliding  Fast  Level  Path
  Search    Window   &Slow Order   Sum      
  Two Ptr   Prefix   Rev.  Zigzag Diameter
            Sum             
            Hash Map        
            Mono Stack      
            Cyclic Sort     

    ┌─────────────────────────────────────────────────────────┐
    │              WHAT IS THE OUTPUT ASKING?                  │
    └─────────────────────────┬───────────────────────────────┘
                              │
     ┌────────┬───────┬───────┼───────┬──────────┬────────┐
     ▼        ▼       ▼       ▼       ▼          ▼        ▼
  Optimize  Count   Find K  Find    Check     Generate  Range
  (min/max) Ways    Best    Order   Connect   All of..  Query
     │        │       │       │       │          │        │
   Greedy    DP    Top K   Topo    Union      Subsets  Seg Tree
   Binary         Heap    Sort    Find       Backtrack  BIT
   Search         K-Merge                    Prefix
   DP                                                  Sum
```

---

## 💎 The Golden Mnemonics

### The "SIFT" Method (for every problem)
- **S**tate the problem in your own words
- **I**dentify the input type and constraints  
- **F**ind the pattern using the trigger words
- **T**emplate: Write the skeleton code from memory

### The Pattern Families (memorize these 7 families)

| Family | Members | Core Idea |
|---|---|---|
| 🏃 **Runners** | Two Pointers, Fast & Slow, Sliding Window | Two things moving through the data |
| 📦 **Sorters** | Merge Intervals, Cyclic Sort, Linear Sort | Put things in the right place |
| 🌲 **Explorers** | BFS, DFS, Island, Backtracking | Visit nodes, explore paths |
| 📊 **Rankers** | Top K, Two Heaps, K-way Merge | Find the best K things |
| 🔍 **Searchers** | Binary Search, Trie, Hash Map | Find something fast |
| 🧮 **Counters** | Prefix Sum, DP, Counting, BIT | Count or accumulate values |
| 🔗 **Connectors** | Union Find, Topo Sort, Clone, Serialize | Manage relationships |

### The 3-Second Gut Check

> Before you write a single line of code, say this to yourself:
> 
> *"My input is a ____. I need to find ____. The constraint is ____. Therefore, the pattern is ____."*
> 
> If you can't fill in all 4 blanks, **re-read the problem**.

---

## 🎓 The Professor's Final Advice

1. **Don't memorize solutions. Memorize the SHAPE of solutions.** Every Two Pointers problem has the same `while left < right` skeleton. Every DFS problem has the same `if not node: return` base case. Learn the skeletons.

2. **When stuck, simplify.** Can't solve for N? Solve for N=1, then N=2, then N=3. The pattern will emerge.

3. **Talk out loud.** In an interview, silence is your enemy. Say: *"I notice the input is sorted, which makes me think of Binary Search or Two Pointers. Let me try Two Pointers because we need a pair."*

4. **The hardest problems combine 2 patterns.** "Sliding Window + Hash Map", "Binary Search + Greedy", "DFS + Backtracking". Once you master individual patterns, start thinking about combos.

5. **Speed comes from repetition, not intelligence.** The first time you see Topological Sort, it takes 30 minutes. The 10th time, it takes 3 minutes. There are no shortcuts. Do the reps.

---

## 🧭 Navigation & Cross-Pillar Bridges

| ← Previous (Pillar 1: Data Structures) | ↑ Fundamentals Hub | Next (Pillar 2: Patterns) → |
|:---|:---:|---:|
| [🕸️ 010 - Graphs (The Complete Guide)](../010%20-%20Graphs%20%28The%20Complete%20Guide%29/) | [📚 Fundamentals Index](../README.md) | [01 - Warmup Patterns →](../../01%20-%20Warmup/) |

> ### 🏛️ Theoretical Foundations & Engine Room Links:
> - **The Decision Physics:** Need the formal complexity triage behind these 5 questions? Consult [000 - Chapter 12: Kill Mode vs Pull the Plug](../000%20-%20Theoretical%20Foundations%20%28The%20Complete%20Guide%29/12_kill_mode_vs_pull_plug.md).
> - **Trees Engine Room:** Review the full hierarchical taxonomy in [009 - Trees (The Complete Guide)](../009%20-%20Trees%20%28The%20Complete%20Guide%29/).
> - **Graphs Engine Room:** Review traversals and representations in [010 - Graphs (The Complete Guide)](../010%20-%20Graphs%20%28The%20Complete%20Guide%29/).

