"""
============================================================
Problem: Count Paths for a Sum
Pattern: Tree Depth First Search / Hash Maps
Difficulty: Medium (Advanced)
Link: https://leetcode.com/problems/path-sum-iii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Remember the "Subarray Sum Equals K" problem where we used a magical notebook 
(Hash Map) to store our Running Totals? 
This is the EXACT same problem, but instead of an array, it's a tree!
The paths don't have to start at the root, and they don't have to end at a leaf. 
They just have to go straight down.
As we walk down a branch, we keep a Running Total.
If the Target is 8, and our Running Total is 10, we check our magical notebook:
"Did I ever have a Running Total of 2 higher up on this EXACT same path?"
If yes, that means the numbers between that old spot and our current spot 
add up exactly to 8!
BUT, there is a catch. When we hit a dead end and backtrack to try a different 
branch, we MUST erase our Running Total from the notebook! We can't let 
the left branch's totals accidentally get used by the right branch!

APPROACH:
---------
1. Initialize a Hash Map `prefix_sums = {0: 1}` (Base case: a path perfectly 
   matches the target from the very beginning).
2. Define `count_paths(node, current_sum, target_sum)`.
3. If `node` is None, return `0`.
4. Update `current_sum += node.value`.
5. Check if `current_sum - target_sum` exists in `prefix_sums`. If it does, 
   add that frequency to our `path_count`.
6. Add the current `current_sum` to `prefix_sums` (increment by 1).
7. Recursively calculate the path counts for the left and right subtrees and 
   add them to `path_count`.
8. BACKTRACK: Before returning from this node, DECREMENT the `current_sum` 
   in `prefix_sums` by 1. We are stepping back up, so this sum is no longer 
   available to other branches!
9. Return `path_count`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited exactly once, and Hash Map lookups are O(1).
Space: O(N) — The Hash Map can store up to N distinct prefix sums (if the tree is a straight line), and the recursion stack can also go O(N) deep.

EDGE CASES:
-----------
- Edge case 1: Tree with negative numbers. Hash Map handles it perfectly!
- Edge case 2: Empty tree. Returns `0`.
============================================================
"""

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def count_paths(root: Optional[TreeNode], target_sum: int) -> int:
    """
    Finds the total number of paths in the tree where the sum of nodes equals 
    target_sum.
    """
    # Base case: a prefix sum of 0 exists 1 time before we start
    prefix_sums = {0: 1}

    def dfs(node: Optional[TreeNode], current_sum: int) -> int:
        if not node:
            return 0

        current_sum += node.value
        path_count = 0

        # 1. Did we see a previous sum that leaves exactly target_sum?
        needed = current_sum - target_sum
        if needed in prefix_sums:
            path_count += prefix_sums[needed]

        # 2. Add the current sum to our notebook
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        # 3. Go down the left and right branches
        path_count += dfs(node.left, current_sum)
        path_count += dfs(node.right, current_sum)

        # 4. BACKTRACK! Remove the current sum as we go back up the tree
        prefix_sums[current_sum] -= 1

        return path_count

    return dfs(root, 0)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    #       12
    #      /  \
    #     7    1
    #    /    / \
    #   4    10  5
    root1 = TreeNode(12)
    root1.left = TreeNode(7)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(4)
    root1.right.left = TreeNode(10)
    root1.right.right = TreeNode(5)
    
    # Target = 11. Paths: (7 -> 4) and (1 -> 10)
    assert count_paths(root1, 11) == 2, f"Test 1 failed: {count_paths(root1, 11)}"

    # Target = 12. Path: (12)
    assert count_paths(root1, 12) == 1, "Test 2 failed"

    # 🔲 Edge cases
    assert count_paths(None, 0) == 0, "Edge 1: Empty tree"

    print("All tests passed!")
