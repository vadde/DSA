"""
============================================================
Problem: Binary Tree Path Sum
Pattern: Tree Depth First Search
Difficulty: Easy
Link: https://leetcode.com/problems/path-sum/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are walking through a magical forest (a tree).
Every tree branch has a number on it.
You have a backpack with a target number, say `22`.
As you walk down a path, you subtract the number you see from your backpack.
If the first branch says `5`, your backpack now holds `17`.
If you reach the very end of the path (a leaf node) and your backpack is 
exactly empty (`0`), you win!
But if you reach a leaf and your backpack isn't `0`, that path was a loser, 
so you magically teleport backward (Backtracking) and try a different path!

APPROACH:
---------
1. If the `root` is None, return `False`. (A non-existent path can't equal the sum).
2. If the current node is a leaf (no left, no right children):
   - Check if `root.value == target_sum`. If it is, return `True`!
3. If it's not a leaf, recursively check the left and right subtrees.
   - BUT, remember to subtract the current node's value from the `target_sum`!
   - `return has_path_sum(root.left, target_sum - root.value) or has_path_sum(root.right, target_sum - root.value)`

COMPLEXITY:
-----------
Time:  O(N) — In the worst case, we visit every node in the tree.
Space: O(H) — Where H is the height of the tree, representing the recursion stack. (O(log N) for balanced trees, O(N) for skewed trees).

EDGE CASES:
-----------
- Edge case 1: Empty tree. Returns `False`.
- Edge case 2: Tree with a single node equal to the target. Returns `True`.
============================================================
"""

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    """
    Returns True if the tree has a root-to-leaf path such that adding up all 
    the values along the path equals the given target_sum.
    """
    if not root:
        return False

    # Check if the current node is a leaf
    if not root.left and not root.right:
        # If it's a leaf, the remaining target must exactly match the leaf's value
        return root.value == target_sum

    # Recursively check the left and right subtrees, passing down the remaining sum needed
    return has_path_sum(root.left, target_sum - root.value) or \
           has_path_sum(root.right, target_sum - root.value)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    #       12
    #      /  \
    #     7    1
    #    /    / \
    #   9    10  5
    root1 = TreeNode(12)
    root1.left = TreeNode(7)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(9)
    root1.right.left = TreeNode(10)
    root1.right.right = TreeNode(5)
    
    # Path: 12 -> 1 -> 10 == 23
    assert has_path_sum(root1, 23) == True, "Test 1 failed"
    
    # Path: 12 -> 7 -> 9 == 28
    assert has_path_sum(root1, 28) == True, "Test 2 failed"
    
    # Not a root-to-leaf path sum (12 -> 1 == 13, but 1 is not a leaf!)
    assert has_path_sum(root1, 13) == False, "Test 3 failed"

    # 🔲 Edge cases
    assert has_path_sum(None, 0) == False, "Edge 1: Empty tree"
    assert has_path_sum(TreeNode(42), 42) == True, "Edge 2: Single node matches"
    assert has_path_sum(TreeNode(42), 10) == False, "Edge 3: Single node doesn't match"

    print("All tests passed!")
