"""
============================================================
Problem: Path Sum III
Pattern: Prefix Sum on a Tree + Hash Map
Difficulty: Medium
LeetCode: #437
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a binary tree. Find the number of paths that sum to a given target sum.
The path does NOT need to start at the root or end at a leaf, but it MUST go
downwards (parent to child).

APPROACH: Prefix Sum + DFS
---------
This is exactly "Subarray Sum Equals K", but on a Tree!
As we go down a path (DFS), we keep a running `current_sum`.
We check if `current_sum - targetSum` exists in our Hash Map of prefix sums.
CRITICAL: When we finish exploring a node's children and backtrack UP the tree,
we MUST remove the node's `current_sum` from the Hash Map, because that prefix
sum is no longer part of the path for other branches!

COMPLEXITY:
-----------
Time:  O(N) — One pass over all nodes.
Space: O(H) — Hash map stores at most Height elements.
============================================================
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: TreeNode, target_sum: int) -> int:
    prefix_counts: dict[int, int] = {0: 1}

    def dfs(node: TreeNode, current_sum: int) -> int:
        if not node:
            return 0

        current_sum += node.val
        needed = current_sum - target_sum
        
        # How many times have we seen the needed prefix sum in the CURRENT path?
        count = prefix_counts.get(needed, 0)

        # Add current sum to map
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

        # Recurse to children
        count += dfs(node.left, current_sum)
        count += dfs(node.right, current_sum)

        # BACKTRACK: remove the current sum from the map so it doesn't affect parallel branches!
        prefix_counts[current_sum] -= 1
        
        return count

    return dfs(root, 0)


if __name__ == "__main__":
    # Tree:
    #       10
    #      /  \
    #     5   -3
    #    / \    \
    #   3   2   11
    #  / \   \
    # 3  -2   1
    
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    
    assert path_sum(root, 8) == 3, "Test 1: Paths summing to 8"
    assert path_sum(None, 0) == 0, "Edge: Empty tree"
    print("All tests passed!")
