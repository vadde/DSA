"""
============================================================
Problem: Even Odd Tree
Pattern: Tree BFS (Level Order Traversal)
Difficulty: Medium
Link: https://leetcode.com/problems/even-odd-tree/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A tree is "Even Odd" if:
- At EVEN-indexed levels (0, 2, 4...), all values are ODD and STRICTLY INCREASING left to right.
- At ODD-indexed levels (1, 3, 5...), all values are EVEN and STRICTLY DECREASING left to right.

APPROACH:
---------
1. BFS level by level.
2. At each level, check the parity and ordering rules.
3. If any violation is found, return False.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)

EDGE CASES:
-----------
- Single node at level 0 must be odd.
- Adjacent equal values violate STRICTLY increasing/decreasing.
============================================================
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_even_odd_tree(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    queue = deque([root])
    level = 0

    while queue:
        prev = None
        for _ in range(len(queue)):
            node = queue.popleft()

            # Check parity
            if level % 2 == 0:  # Even level → values must be odd
                if node.val % 2 == 0:
                    return False
                if prev is not None and node.val <= prev:
                    return False
            else:  # Odd level → values must be even
                if node.val % 2 == 1:
                    return False
                if prev is not None and node.val >= prev:
                    return False

            prev = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level += 1

    return True


if __name__ == "__main__":
    #         1
    #       /   \
    #      10    4
    #     / \     \
    #    3   7    11
    root = TreeNode(1, TreeNode(10, TreeNode(3), TreeNode(7)), TreeNode(4, None, TreeNode(11)))
    assert is_even_odd_tree(root) == True, "Test 1"

    #         5
    #       /   \
    #      4     2
    #     / \
    #    3   3
    root2 = TreeNode(5, TreeNode(4, TreeNode(3), TreeNode(3)), TreeNode(2))
    assert is_even_odd_tree(root2) == False, "Test 2: 3,3 not strictly increasing"

    assert is_even_odd_tree(TreeNode(1)) == True, "Test 3: single odd"
    assert is_even_odd_tree(TreeNode(2)) == False, "Test 4: even at level 0"
    print("All tests passed!")
