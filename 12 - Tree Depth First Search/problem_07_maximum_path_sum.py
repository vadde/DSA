"""
============================================================
Problem: Maximum Path Sum
Pattern: Tree Depth First Search
Difficulty: Hard (Advanced)
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
This is just like the Tree Diameter problem, but instead of counting how many 
nodes are in the longest path, we want the path with the HIGHEST SCORE.
Every node has a score (some are positive, some are negative).
A node asks its left child: "What is the highest score I can get if I walk down 
your branch?"
And it asks its right child the same thing.
If a child returns a NEGATIVE score (like -10), the parent says: "Ew, no thanks! 
I'm just not going to walk down your branch at all!" 
So we replace any negative scores with a `0` (meaning we just ignore that branch).
The score of the path going THROUGH the current node is:
`left_score + right_score + node's own score`.
We keep track of the absolute highest score we ever see.
Then, to answer its OWN parent, the node can only pick ONE path to pass up 
(you can't walk down both branches and then go back up to the parent without 
retracing your steps).
So it passes up: `max(left_score, right_score) + node's own score`.

APPROACH:
---------
1. Initialize a global/nonlocal variable `max_sum = -infinity`.
2. Define a recursive helper `calculate_max_path_sum(node)`.
3. Base case: If `node` is None, return `0`.
4. Recursive step (POST-ORDER):
   - `left_sum = max(calculate_max_path_sum(node.left), 0)` <-- Ignore negative paths!
   - `right_sum = max(calculate_max_path_sum(node.right), 0)`
5. The max sum of the path passing *through* the current node is:
   - `current_max_sum = left_sum + right_sum + node.value`
6. Update our record: `max_sum = max(max_sum, current_max_sum)`.
7. Return the max sum of the single path to its parent:
   - `return max(left_sum, right_sum) + node.value`.
8. Start recursion and return `max_sum`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited once.
Space: O(H) — The recursion stack is bounded by the height of the tree.

EDGE CASES:
-----------
- Edge case 1: Tree with only negative numbers. We initialize `max_sum = -infinity` 
  so it correctly returns the smallest negative number instead of 0.
- Edge case 2: Empty tree. (Usually problems assume at least 1 node, but if empty, handle gracefully).
============================================================
"""

from typing import Optional
import math

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_maximum_path_sum(root: Optional[TreeNode]) -> int:
    """
    Finds the path with the maximum sum in a given binary tree.
    """
    if not root:
        return 0

    max_sum = -math.inf

    def calculate_max_path_sum(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        
        if not node:
            return 0

        # POST-ORDER: Ask the children first, but IGNORE them if they are negative!
        left_sum = max(calculate_max_path_sum(node.left), 0)
        right_sum = max(calculate_max_path_sum(node.right), 0)

        # The maximum path sum passing through the current node
        current_max_sum = left_sum + right_sum + node.value
        
        # Update the global maximum
        max_sum = max(max_sum, current_max_sum)

        # To the parent, we can only return ONE branch (either left or right) plus ourselves
        return max(left_sum, right_sum) + node.value

    calculate_max_path_sum(root)
    return int(max_sum)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    #       1
    #      / \
    #     2   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    
    # Path: 2 -> 1 -> 3 (Sum = 6)
    assert find_maximum_path_sum(root1) == 6, f"Test 1 failed: {find_maximum_path_sum(root1)}"

    #       1
    #      / \
    #     2   3
    #    /     \
    #   4       5
    #  / \     / \
    # -1 -2   -3 -4
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    root2.left.left.left = TreeNode(-1)
    root2.left.left.right = TreeNode(-2)
    root2.right.right.left = TreeNode(-3)
    root2.right.right.right = TreeNode(-4)
    
    # We ignore the negative leaves. 
    # Max path: 4 -> 2 -> 1 -> 3 -> 5 = 15
    assert find_maximum_path_sum(root2) == 15, f"Test 2 failed: {find_maximum_path_sum(root2)}"

    # 🔲 Edge cases
    # All negative numbers
    root3 = TreeNode(-10)
    root3.left = TreeNode(-20)
    root3.right = TreeNode(-30)
    # The max is just -10 itself
    assert find_maximum_path_sum(root3) == -10, f"Test 3 failed: {find_maximum_path_sum(root3)}"

    assert find_maximum_path_sum(None) == 0, "Edge 1: Empty tree"

    print("All tests passed!")
