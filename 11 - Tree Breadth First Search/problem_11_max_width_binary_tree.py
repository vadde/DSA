"""
============================================================
Problem: Maximum Width of Binary Tree
Pattern: Tree BFS (Level Order Traversal)
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
The "width" of a level is the distance between the leftmost and rightmost
non-null nodes (including any null nodes in between). Find the level with
the maximum width.

KEY INSIGHT: Assign each node a position index. Root = 0. Left child = 2*pos,
right child = 2*pos + 1. Width of a level = rightmost_pos - leftmost_pos + 1.
To prevent integer overflow with deep trees, normalize positions per level by
subtracting the first position.

APPROACH:
---------
1. BFS, tracking (node, position) pairs.
2. At each level, width = last_pos - first_pos + 1.
3. Normalize: subtract the first position of each level to keep numbers small.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)

EDGE CASES:
-----------
- Skewed tree → width is always 1.
- Full binary tree → width doubles each level.
============================================================
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def width_of_binary_tree(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    max_width = 0
    queue = deque([(root, 0)])

    while queue:
        level_size = len(queue)
        first_pos = queue[0][1]  # Normalize to prevent overflow

        for _ in range(level_size):
            node, pos = queue.popleft()
            pos -= first_pos  # Normalize
            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))

        max_width = max(max_width, pos + 1)  # pos is the last position (0-indexed)

    return max_width


if __name__ == "__main__":
    #       1
    #      / \
    #     3   2
    #    /     \
    #   5       9
    root = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2, None, TreeNode(9)))
    assert width_of_binary_tree(root) == 4, "Test 1: level 3 has positions 0 and 3"

    #     1
    #    /
    #   2
    #  /
    # 3
    skewed = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert width_of_binary_tree(skewed) == 1, "Test 2: skewed"

    assert width_of_binary_tree(None) == 0, "Test 3: empty"
    print("All tests passed!")
