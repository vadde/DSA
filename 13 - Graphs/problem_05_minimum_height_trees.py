"""
============================================================
Problem: Minimum Height Trees (Topological Sort)
Pattern: Graphs / Topological Sort
Difficulty: Hard (Advanced)
Link: https://leetcode.com/problems/minimum-height-trees/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a spider web made of nodes and strings, but it doesn't have any loops 
(it's technically a Tree).
If you pick it up by one node and let the rest dangle down, the tree will have 
a certain "height" (how far down it dangles).
If you pick it up by a node at the very edge (a Leaf), it will dangle VERY far down! 
(Maximum Height).
But if you pick it up exactly in the middle (the "Centroid"), the dangling parts 
are balanced, giving you the MINIMUM Height!
So the problem is really asking: "Find the exact center of this graph."
How do we find the center? 
We eat the graph from the outside in!
Imagine setting the outer edge of a leaf on fire. The fire burns the leaves, 
exposing the next layer of nodes (which become the new leaves).
If you keep burning the outermost leaves layer by layer, eventually the fire will 
meet exactly in the middle!
The last 1 or 2 surviving nodes before the whole thing burns up are your 
Minimum Height Tree roots.
(Fun fact: A tree can only ever have 1 or 2 centers. Never 3, or it would have 
a cycle!).

APPROACH:
---------
This is a variation of Topological Sort, but instead of sorting by directed arrows, 
we sort by degree (number of connections).
1. If `n <= 2`, every node is a valid root. Return all of them.
2. Build an adjacency list `graph`. Because we need to quickly remove edges, we 
   will use `set()` instead of lists for the neighbors.
3. Find all current LEAVES (nodes that only have exactly 1 connection: `len(graph[i]) == 1`).
   Add them to a `queue`.
4. Initialize `remaining_nodes = n`.
5. Loop while `remaining_nodes > 2`:
   - `leaves_count = len(queue)`
   - `remaining_nodes -= leaves_count` (Burn this entire layer of leaves!)
   - For every leaf in this layer:
     - Pop it from the queue.
     - Look at its ONLY neighbor. (We can get it using `graph[leaf].pop()`).
     - Go to that neighbor, and erase the leaf from its connections: 
       `graph[neighbor].remove(leaf)`.
     - If the neighbor now ONLY has 1 connection left, it just became a leaf!
       Add it to the `queue` for the next layer of burning.
6. When the while loop finishes, whatever is left in the `queue` are the centers! 
   Return them as a list.

COMPLEXITY:
-----------
Time:  O(V + E) — We process each leaf and its single edge once.
Space: O(V + E) — To store the graph and the queue.

EDGE CASES:
-----------
- Edge case 1: Tree with 1 node (`n=1`, `edges=[]`). Returns `[0]`.
- Edge case 2: Tree with 2 nodes. Returns `[0, 1]`.
============================================================
"""

from typing import List
from collections import deque

def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
    """
    Finds the root nodes that yield Minimum Height Trees.
    """
    if n <= 2:
        return [i for i in range(n)]

    # 1. Build the graph using sets for fast deletion
    graph = {i: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # 2. Find all initial leaves (nodes with exactly 1 connection)
    leaves = deque()
    for i in range(n):
        if len(graph[i]) == 1:
            leaves.append(i)

    # 3. Burn the graph from the outside in!
    remaining_nodes = n
    while remaining_nodes > 2:
        leaves_count = len(leaves)
        remaining_nodes -= leaves_count

        # Process exactly one "layer" of outer leaves
        for _ in range(leaves_count):
            leaf = leaves.popleft()
            
            # Since it's a leaf, it only has ONE neighbor. Pop it.
            neighbor = graph[leaf].pop()
            
            # Remove the leaf from the neighbor's connections
            graph[neighbor].remove(leaf)
            
            # Did the neighbor just become a leaf itself?
            if len(graph[neighbor]) == 1:
                leaves.append(neighbor)

    # Whatever survives the fire are our centroids!
    return list(leaves)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # 0 - 3 - 1
    #     |
    #     2
    # Node 3 is clearly the center.
    assert find_min_height_trees(4, [[1, 0], [1, 2], [1, 3]]) == [1] # Wait, the edges are 1-0, 1-2, 1-3. So 1 is center.
    assert find_min_height_trees(4, [[1, 0], [1, 2], [1, 3]]) == [1], "Test 1 failed"

    #   0
    #   |
    #   1 - 2 - 3
    #       |   |
    #       4   5
    # Let's trace it.
    edges2 = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    # Let's construct a graph that has two centers
    # 0 - 1 - 2 - 3
    assert find_min_height_trees(4, [[0, 1], [1, 2], [2, 3]]) == [1, 2], "Test 2 failed"

    # 🔲 Edge cases
    assert find_min_height_trees(1, []) == [0], "Edge 1: Single node"
    assert find_min_height_trees(2, [[0, 1]]) == [0, 1], "Edge 2: Two nodes"

    print("All tests passed!")
