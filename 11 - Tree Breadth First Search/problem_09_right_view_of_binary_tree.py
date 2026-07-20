"""
============================================================
Problem: Right View of a Binary Tree
Pattern: Tree Breadth First Search
Difficulty: Easy (Grokking) | Medium (LeetCode)
Link: https://leetcode.com/problems/binary-tree-right-side-view/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you're standing on the RIGHT side of a Christmas tree, looking at it
from the side. You can only see the RIGHTMOST ornament on each row. If a row
has ornaments [4, 5, 6], you only see 6. Return all the ornaments you can see
from top to bottom.

APPROACH:
---------
1. BFS level by level.
2. For each level, the LAST node in the queue for that level is the one visible
   from the right side.
3. After processing each level, append that last node's value to the result.

COMPLEXITY:
-----------
Time:  O(N) — visit every node.
Space: O(N) — queue can hold up to N/2 nodes.

EDGE CASES:
-----------
- Empty tree → return [].
- Single node → return [root.val].
- Skewed left tree → every level has 1 node, all visible.
============================================================
"""

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # The last node in this level is the rightmost
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #      \   \
    #       5   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    assert right_side_view(root) == [1, 3, 4], "Test 1"

    # Skewed left
    left_tree = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert right_side_view(left_tree) == [1, 2, 3], "Test 2: skewed left"

    # Empty
    assert right_side_view(None) == [], "Test 3: empty"

    # Single
    assert right_side_view(TreeNode(42)) == [42], "Test 4: single"

    print("All tests passed!")
