"""
============================================================
Problem: Level Averages in a Binary Tree
Pattern: Tree Breadth First Search
Difficulty: Easy
Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are still looking at your family tree, but instead of taking pictures, you 
want to find the AVERAGE age of each generation.
What's the average age of the Great-Grandparents?
What's the average age of the Grandparents?
What's the average age of the Parents?
Just like before, we use our Queue to line everyone up generation by generation.
When a generation is ready, instead of putting their names in a list, we just 
add up all their ages!
If the parents are 40 and 44, their total age is 84. Since there are 2 of them, 
the average is 84 / 2 = 42.
We already know how many people are in the generation because of `level_size = len(queue)`!

APPROACH:
---------
1. If the `root` is None, return `[]`.
2. Initialize `queue = deque([root])`, `result = []`.
3. Loop `while queue is not empty`:
   - `level_size = len(queue)`
   - `level_sum = 0.0`
   - Loop `level_size` times:
     - Pop `node` from queue.
     - Add `node.value` to `level_sum`.
     - Append children to the queue (Left then Right).
   - After the inner loop, append `level_sum / level_size` to `result`.
4. Return `result`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited once.
Space: O(N) — The queue can hold up to N/2 nodes at the bottom level of the tree.

EDGE CASES:
-----------
- Edge case 1: Empty tree. Returns `[]`.
- Edge case 2: Tree with single node. Returns `[root.value]`.
============================================================
"""

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_level_averages(root: Optional[TreeNode]) -> List[float]:
    """
    Returns the average value of nodes on each level of a binary tree.
    """
    if not root:
        return []

    result: List[float] = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0.0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.value

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Calculate and store the average for this level
        result.append(level_sum / level_size)

    return result

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
    
    # Expected: 
    # L0: 12.0
    # L1: (7+1)/2 = 4.0
    # L2: (9+2+10+5)/4 = 26/4 = 6.5
    expected1 = [12.0, 4.0, 6.5]
    assert find_level_averages(root1) == expected1, f"Test 1 failed: {find_level_averages(root1)}"

    # 🔲 Edge cases
    assert find_level_averages(None) == [], "Edge 1: Empty tree"
    assert find_level_averages(TreeNode(42)) == [42.0], "Edge 2: Single node"

    print("All tests passed!")
