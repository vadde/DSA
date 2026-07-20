"""
============================================================
Problem: Minimum Depth of a Binary Tree
Pattern: Tree Breadth First Search
Difficulty: Easy
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are climbing down a tree, starting from the very top (the root).
You want to find the fastest way to hit the ground (a leaf).
A leaf is a node that has NO children (no left, no right).
If you use Depth First Search (DFS), you might climb all the way down the deepest, 
longest branch first, taking forever just to realize there was a leaf right next 
to the root!
But if you use Breadth First Search (BFS), you check the entire Level 1 first.
Then you check the entire Level 2.
The very FIRST time you see a leaf node, you yell "I FOUND IT!" and stop immediately!
Because you are checking level by level, the first leaf you find is mathematically 
guaranteed to be the closest one to the root.

APPROACH:
---------
1. If the `root` is None, return `0`.
2. Initialize `queue = deque([root])`.
3. Initialize `depth = 1`.
4. Loop `while queue is not empty`:
   - `level_size = len(queue)`
   - Loop `level_size` times:
     - Pop `node` from queue.
     - Is it a leaf? `if not node.left and not node.right:`
       - YES! Return `depth` immediately!
     - If not a leaf, append its children to the queue.
   - After finishing the entire level, we haven't found a leaf, so we go deeper.
   - `depth += 1`.

COMPLEXITY:
-----------
Time:  O(N) — In the worst case, we check all nodes. But in the best case, we stop very early!
Space: O(N) — The queue can hold up to N/2 nodes.

EDGE CASES:
-----------
- Edge case 1: Empty tree. Returns `0`.
- Edge case 2: Tree with single node. Returns `1`.
============================================================
"""

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def min_depth(root: Optional[TreeNode]) -> int:
    """
    Finds the minimum depth of a binary tree.
    """
    if not root:
        return 0

    queue = deque([root])
    depth = 1

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            # The very first time we see a leaf node, we return the depth!
            # Because BFS goes level by level, this is guaranteed to be the minimum.
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Move to the next generation
        depth += 1

    return depth

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    #       12
    #      /  \
    #     7    1
    #         / \
    #        10  5
    root1 = TreeNode(12)
    root1.left = TreeNode(7)
    root1.right = TreeNode(1)
    root1.right.left = TreeNode(10)
    root1.right.right = TreeNode(5)
    
    # 7 is a leaf at depth 2!
    assert min_depth(root1) == 2, f"Test 1 failed: {min_depth(root1)}"

    #       12
    #      /  \
    #     7    1
    #    /      \
    #   9        5
    root2 = TreeNode(12)
    root2.left = TreeNode(7)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(9)
    root2.right.right = TreeNode(5)
    
    assert min_depth(root2) == 3, f"Test 2 failed: {min_depth(root2)}"

    # 🔲 Edge cases
    assert min_depth(None) == 0, "Edge 1: Empty tree"
    assert min_depth(TreeNode(42)) == 1, "Edge 2: Single node"

    print("All tests passed!")
