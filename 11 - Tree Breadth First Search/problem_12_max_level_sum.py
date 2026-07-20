"""
============================================================
Problem: Maximum Level Sum of a Binary Tree
Pattern: Tree BFS (Level Order Traversal)
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Each row of the tree has a sum of all its values. Find which ROW NUMBER
(1-indexed) has the highest sum. If there's a tie, return the smallest
row number.

APPROACH:
---------
1. BFS level by level.
2. At each level, compute the sum of all node values.
3. Track the level with the highest sum (break ties with smallest level).

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)

EDGE CASES:
-----------
- Negative values (sum can decrease at deeper levels).
- Single node → level 1.
============================================================
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_level_sum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([root])
    max_sum = float('-inf')
    max_level = 1
    level = 0

    while queue:
        level += 1
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

    return max_level


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
    assert max_level_sum(root) == 2, "Test 1: level 2 has sum 7"

    assert max_level_sum(TreeNode(-100)) == 1, "Test 2: single negative"
    assert max_level_sum(TreeNode(1, TreeNode(1), TreeNode(1))) == 2, "Test 3: level 2 wins"
    print("All tests passed!")
