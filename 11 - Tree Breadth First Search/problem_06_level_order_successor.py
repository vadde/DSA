"""
============================================================
Problem: Level Order Successor
Pattern: Tree Breadth First Search
Difficulty: Easy
Link: https://www.educative.io/courses/grokking-the-coding-interview/7nO4VmA74Lr
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are calling out the names of everyone in the family tree, level by level, 
left to right.
Someone asks you: "Hey, right after you call out 'Bob', who is the very next 
person you call?"
That next person is Bob's "Level Order Successor".
Because we are already using a Queue that perfectly lines everyone up in the 
exact order we call their names, this is incredibly easy!
We just pop people out of the line one by one.
The moment we pop "Bob", we stop! 
Who is the next person we were *going* to call? It's simply the person standing 
at the very front of the line right now!

APPROACH:
---------
1. If the `root` is None, return `None`.
2. Initialize `queue = deque([root])`.
3. Loop `while queue is not empty`:
   - Pop `node` from queue.
   - Append its children (Left then Right) to the queue.
   - Did we just pop the target node? `if node.value == target_value:`
     - YELL STOP! We found our guy. Break out of the loop.
4. After breaking out of the loop, the successor is exactly `queue[0]`. 
   If the queue is empty (meaning the target was the very last node in the tree), 
   return `None`.

COMPLEXITY:
-----------
Time:  O(N) — We visit nodes until we find the target.
Space: O(N) — The queue holds up to N/2 nodes.

EDGE CASES:
-----------
- Edge case 1: Target is the very last node in the traversal. Queue is empty, returns `None`.
- Edge case 2: Target is not in the tree. Returns `None`.
============================================================
"""

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_successor(root: Optional[TreeNode], target_value: int) -> Optional[TreeNode]:
    """
    Finds the level order successor of the given node in a binary tree.
    """
    if not root:
        return None

    queue = deque([root])

    while queue:
        # Notice we don't need `level_size` here! 
        # We don't care about generations, just the absolute ordering in the queue.
        node = queue.popleft()

        # Insert children BEFORE we check the target.
        # Why? Because if the target is the last node on Level 2, its successor
        # is the first node on Level 3. We need Level 3 to be in the queue!
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        if node.value == target_value:
            break

    # If the queue is not empty, the next person in line is the successor
    return queue[0] if queue else None

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    #       12
    #      /  \
    #     7    1
    #    / \  / \
    #   9  2 10  5
    root1 = TreeNode(12)
    root1.left = TreeNode(7)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(9)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(10)
    root1.right.right = TreeNode(5)
    
    # Level order: 12, 7, 1, 9, 2, 10, 5
    
    res1 = find_successor(root1, 12)
    assert res1 and res1.value == 7, "Test 1 failed: Successor of 12 should be 7"

    res2 = find_successor(root1, 9)
    assert res2 and res2.value == 2, "Test 2 failed: Successor of 9 should be 2"

    # The tricky cross-level jump!
    res3 = find_successor(root1, 1)
    assert res3 and res3.value == 9, "Test 3 failed: Successor of 1 should be 9"

    # 🔲 Edge cases
    # Last node in tree
    res4 = find_successor(root1, 5)
    assert res4 is None, "Edge 1 failed: Successor of last node should be None"

    print("All tests passed!")
