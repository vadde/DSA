"""
============================================================
Problem: Find Largest Value in Each Tree Row
Pattern: Tree BFS (Level Order Traversal)
Difficulty: Medium
Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Look at each row of a tree. For each row, tell me the biggest number.

APPROACH:
---------
1. BFS level by level.
2. For each level, track the maximum value.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)

EDGE CASES:
-----------
- Empty tree → [].
- Negative values.
============================================================
"""

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largest_values(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_max = float('-inf')
        for _ in range(len(queue)):
            node = queue.popleft()
            level_max = max(level_max, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_max)

    return result


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    assert largest_values(root) == [1, 3, 9], "Test 1"
    assert largest_values(TreeNode(-1)) == [-1], "Test 2: negative"
    assert largest_values(None) == [], "Test 3: empty"
    print("All tests passed!")
