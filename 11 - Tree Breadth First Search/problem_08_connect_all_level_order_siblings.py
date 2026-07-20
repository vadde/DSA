"""
============================================================
Problem: Connect All Level Order Siblings
Pattern: Tree Breadth First Search
Difficulty: Medium
Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine kids standing in lines for a school photo. In the last problem, we
connected kids standing in the SAME row. Now, the LAST kid in every row should
also point to the FIRST kid of the NEXT row. So everyone forms ONE long chain
from top to bottom, left to right — like a conga line winding through the tree!

APPROACH:
---------
1. Do a standard BFS (Level Order Traversal).
2. Instead of just connecting within a level, connect EVERY node to the next
   node dequeued — regardless of whether they're on the same level or not.
3. After BFS, every node's `next` points to the node that would come next
   if you read the tree left-to-right, top-to-bottom.

COMPLEXITY:
-----------
Time:  O(N) — visit every node once.
Space: O(N) — queue can hold up to N/2 nodes (last level).

EDGE CASES:
-----------
- Empty tree → return None.
- Single node → next stays None.
- Skewed tree (all left or all right children).
============================================================
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect_all_siblings(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    queue = deque([root])
    prev = None

    while queue:
        node = queue.popleft()

        # Link previous node to current — regardless of level boundaries
        if prev:
            prev.next = node
        prev = node

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    connect_all_siblings(root)

    # Walk the chain: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    chain = []
    node = root
    while node:
        chain.append(node.val)
        node = node.next
    assert chain == [1, 2, 3, 4, 5, 6], f"Test 1 failed: {chain}"

    # Edge: single node
    single = TreeNode(42)
    connect_all_siblings(single)
    assert single.next is None, "Test 2: single node"

    # Edge: empty tree
    assert connect_all_siblings(None) is None, "Test 3: empty"

    print("All tests passed!")
