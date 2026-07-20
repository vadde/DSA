"""
============================================================
Problem: Reverse Level Order Traversal
Pattern: Tree Breadth First Search
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Remember taking pictures of every generation in the family tree?
What if the photo album company wants the pictures in the book backwards?
They want the youngest kids on Page 1, the parents on Page 2, the grandparents 
on Page 3, and the Great-Grandparent on the very last page!
We STILL take the pictures in the exact same order (top to bottom).
But when we put a picture into the photo album, instead of putting it at the 
END of the album, we shove it into the very FRONT of the album!
By always putting the newest picture at the front, the very first picture we 
took (the top of the tree) ends up at the very back of the album.

APPROACH:
---------
1. If the `root` is None, return `[]`.
2. Initialize a queue using `collections.deque` with the `root`.
3. Initialize `result = deque()`. We use a deque for the result too, so we can 
   efficiently push new levels to the FRONT!
4. Loop `while queue is not empty`:
   - `level_size = len(queue)`
   - `current_level = []`
   - Loop `level_size` times:
     - Pop `node` from queue.
     - Add `node.value` to `current_level`.
     - Append children to the queue (Left then Right).
   - INSTEAD of `result.append`, do `result.appendleft(current_level)`.
5. Return `list(result)`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited once. `appendleft()` on a deque is O(1).
Space: O(N) — The queue and the result deque take up O(N) space.

EDGE CASES:
-----------
- Edge case 1: Empty tree. Returns `[]`.
- Edge case 2: Unbalanced tree. Handled perfectly since BFS naturally groups by depth.
============================================================
"""

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reverse_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Returns the reverse level order traversal of a binary tree's nodes' values.
    (i.e., from bottom to top, level by level).
    """
    if not root:
        return []

    result = deque()
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level: List[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Push the current level to the FRONT of the result list
        result.appendleft(current_level)

    return list(result)

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
    
    # Bottom level first!
    expected1 = [[9, 2, 10, 5], [7, 1], [12]]
    assert reverse_level_order(root1) == expected1, f"Test 1 failed: {reverse_level_order(root1)}"

    # 🔲 Edge cases
    assert reverse_level_order(None) == [], "Edge 1: Empty tree"
    assert reverse_level_order(TreeNode(42)) == [[42]], "Edge 2: Single node"

    print("All tests passed!")
