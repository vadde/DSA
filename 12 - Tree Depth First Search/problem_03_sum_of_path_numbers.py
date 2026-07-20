"""
============================================================
Problem: Sum of Path Numbers
Pattern: Tree Depth First Search
Difficulty: Medium
Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine every node in the tree is a single digit (0-9).
As you walk down a path from the top of the tree to a leaf, you write down the 
numbers you see.
If you see a `1`, then a `7`, then a `3`, you just formed the number `173`.
Your job is to find ALL the numbers formed by every possible path to the bottom, 
and add them all together!
How do we build the number as we walk down?
Math! If you currently have the number `17`, and you step on a `3`, you don't 
add 3 to 17. You multiply 17 by 10 (which makes it 170), and THEN add 3 (which 
makes it 173).
Formula: `current_number = (current_number * 10) + node.value`
When you hit a leaf, you return that fully built number.
When branches split, you just add the total from the left branch and the total 
from the right branch!

APPROACH:
---------
1. Define a recursive helper `find_sum(node, path_sum)`.
2. If the `node` is None, return `0`.
3. Update the `path_sum` using our math trick: `path_sum = 10 * path_sum + node.value`.
4. Is this a leaf node?
   - If yes, return the `path_sum`! This path is finished.
5. If it's not a leaf, return the sum of the left subtree PLUS the sum of the 
   right subtree.
   - `return find_sum(node.left, path_sum) + find_sum(node.right, path_sum)`
6. Start the recursion from the root with a starting sum of `0`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited once.
Space: O(H) — The recursion stack goes as deep as the tree height.

EDGE CASES:
-----------
- Edge case 1: Empty tree. Returns `0`.
- Edge case 2: Tree with single node (e.g. `5`). Returns `5`.
============================================================
"""

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_numbers(root: Optional[TreeNode]) -> int:
    """
    Finds the total sum of all the numbers represented by all root-to-leaf paths.
    """
    def find_sum(node: Optional[TreeNode], path_sum: int) -> int:
        if not node:
            return 0

        # Calculate the number formed so far
        path_sum = 10 * path_sum + node.value

        # If it's a leaf, return the fully formed number
        if not node.left and not node.right:
            return path_sum

        # Recursively find the sums from the left and right branches and add them together
        return find_sum(node.left, path_sum) + find_sum(node.right, path_sum)

    return find_sum(root, 0)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    #       1
    #      / \
    #     7   9
    #        / \
    #       2   9
    root1 = TreeNode(1)
    root1.left = TreeNode(7)
    root1.right = TreeNode(9)
    root1.right.left = TreeNode(2)
    root1.right.right = TreeNode(9)
    
    # Path 1: 1 -> 7 = 17
    # Path 2: 1 -> 9 -> 2 = 192
    # Path 3: 1 -> 9 -> 9 = 199
    # Total = 17 + 192 + 199 = 408
    assert sum_numbers(root1) == 408, f"Test 1 failed: {sum_numbers(root1)}"

    #       4
    #      / \
    #     9   0
    #    / \
    #   5   1
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    
    # Paths: 495 + 491 + 40 = 1026
    assert sum_numbers(root2) == 1026, f"Test 2 failed: {sum_numbers(root2)}"

    # 🔲 Edge cases
    assert sum_numbers(None) == 0, "Edge 1: Empty tree"
    assert sum_numbers(TreeNode(5)) == 5, "Edge 2: Single node"

    print("All tests passed!")
