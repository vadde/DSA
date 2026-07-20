"""
============================================================
Problem: Redundant Connection (Union Find)
Pattern: Graphs / Union Find
Difficulty: Medium
Link: https://leetcode.com/problems/redundant-connection/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a group of friends forming a club. 
At first, everyone is in their own 1-person club.
When Alice and Bob become friends, they merge their clubs into one bigger club 
(this is called a "Union"). They pick one person (say, Alice) to be the "President".
When Bob becomes friends with Charlie, Charlie joins Alice's club, because Bob 
is already in it.
Before two people merge their clubs, they first check: 
"Wait, do we have the same President?" (this is called a "Find").
If Alice and Charlie want to become friends, they check their Presidents. 
They realize they BOTH already have Alice as their President! They are already 
in the same club!
If they draw a friendship line between each other anyway, they create a CYCLE 
(a loop of friends).
The problem gives us a list of friendships, and exactly ONE friendship creates 
a cycle. Our job is to find it!

APPROACH:
---------
This is the classic Disjoint Set (Union Find) algorithm.
1. Initialize an array/dictionary `parent` where every node is its own parent.
   `parent = {1: 1, 2: 2, 3: 3...}`
2. Define `find(node)`:
   - If `parent[node] == node`, we found the "President" (the root).
   - Otherwise, recursively call `find(parent[node])`.
   - **Path Compression Optimization**: As we return from the recursion, we 
     update the node's parent to point DIRECTLY to the President. This makes 
     future lookups blazing fast!
     `parent[node] = find(parent[node])`
3. Define `union(node1, node2)`:
   - Find the President of `node1` and the President of `node2`.
   - If they are the SAME, we just found the cycle! Return `False`.
   - If they are different, make one President the parent of the other. 
     Return `True`.
4. Loop through the given `edges`. Try to `union` them. 
   - The first edge that returns `False` is the redundant one! Return it.

COMPLEXITY:
-----------
Time:  O(N * α(N)) — Where α is the Inverse Ackermann function. Practically, 
       this is O(1) per operation! So O(N) overall.
Space: O(N) — To store the `parent` array.

EDGE CASES:
-----------
- The problem guarantees exactly one redundant edge, so we don't need to worry 
  about not finding one.
============================================================
"""

from typing import List

def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """
    Finds the redundant edge that creates a cycle in a tree.
    """
    # 1. Initialize: Everyone is their own parent (President)
    parent = {}
    for u, v in edges:
        parent[u] = u
        parent[v] = v

    # 2. Find function with Path Compression
    def find(node: int) -> int:
        # If I am my own parent, I am the President of this club.
        if parent[node] == node:
            return node
        
        # Path Compression: Connect directly to the ultimate President
        parent[node] = find(parent[node])
        return parent[node]

    # 3. Union function
    def union(node1: int, node2: int) -> bool:
        root1 = find(node1)
        root2 = find(node2)

        # If they already have the same President, connecting them makes a cycle!
        if root1 == root2:
            return False

        # Otherwise, merge the clubs
        parent[root1] = root2
        return True

    # 4. Process all edges
    for u, v in edges:
        if not union(u, v):
            # This edge created a cycle!
            return [u, v]

    return []

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # 1 - 2
    # | /
    # 3
    # Edges: [1,2], [1,3], [2,3]
    # When processing [2,3], they are already in the same set {1,2,3}!
    assert find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3], "Test 1 failed"

    # 1 - 2 - 3
    # |   |
    # 5 - 4
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    # Processing [1, 4]: 1 and 4 are already connected via 1->2->3->4
    assert find_redundant_connection(edges2) == [1, 4], "Test 2 failed"

    print("All tests passed!")
