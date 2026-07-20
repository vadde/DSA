"""
============================================================
Problem: All Paths for a Sum
Pattern: Tree Depth First Search
Difficulty: Medium
Link: https://leetcode.com/problems/path-sum-ii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
This is just like the previous game! You have a backpack with a target number, 
and you subtract the tree branch numbers as you walk down.
BUT this time, instead of just shouting "I won!" when you reach a leaf and hit 0, 
you have to write down the EXACT path you took to win. 
And you have to find ALL the winning paths, not just one!
Because you are walking up and down branches, you keep a "current path" list.
When you step onto a branch, you add that number to your list.
When you hit a dead end and need to backtrack, you take that number OUT of 
your list (`pop()`) before you step back up. This way, your list always perfectly 
represents where you are currently standing!

APPROACH:
---------
1. Initialize an empty list `all_paths = []` to store the winning paths.
2. Define a recursive helper function `find_paths_recursive(node, current_sum, current_path)`.
3. If `node` is None, return.
4. Append the current node's value to `current_path`.
5. Check if it's a leaf node AND `current_sum == node.value`:
   - If it is, we found a winner! 
   - CRITICAL: Append a COPY of `current_path` to `all_paths`. `list(current_path)`.
     If we don't copy it, any future changes to the path will ruin our saved answer!
6. If it's not a winner, recursively call the left and right subtrees with 
   `current_sum - node.value`.
7. CRITICAL BACKTRACKING: After the left and right subtrees finish, we are about 
   to step backward up the tree. We MUST remove the current node from `current_path` 
   by calling `current_path.pop()`.
8. Return `all_paths`.

COMPLEXITY:
-----------
Time:  O(N^2) — In the worst case (where every path is a winner), copying the path takes O(N) time for each of the O(N) leaves.
Space: O(N log N) — The recursion stack is O(log N) for balanced trees, but storing all paths can take O(N * log N) space.

EDGE CASES:
-----------
- Edge case 1: Empty tree. Returns `[]`.
- Edge case 2: No paths equal the sum. Returns `[]`.
============================================================
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_paths(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    Finds all root-to-leaf paths where each path's sum equals the target_sum.
    """
    all_paths: List[List[int]] = []

    def find_paths_recursive(node: Optional[TreeNode], current_sum: int, current_path: List[int]):
        if not node:
            return

        # 1. Add the current node to the path
        current_path.append(node.value)

        # 2. Check if we reached a leaf AND the sum matches
        if not node.left and not node.right and current_sum == node.value:
            # We found a winner! Add a COPY of the path.
            all_paths.append(list(current_path))
        else:
            # 3. If not a leaf, keep going down
            find_paths_recursive(node.left, current_sum - node.value, current_path)
            find_paths_recursive(node.right, current_sum - node.value, current_path)

        # 4. BACKTRACK! We are about to go back UP the tree, so remove this node.
        current_path.pop()

    find_paths_recursive(root, target_sum, [])
    return all_paths

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
    
    # Target = 23. Paths: 12->7->4 (23) and 12->1->10 (23)
    expected1 = [[12, 7, 4], [12, 1, 10]]
    assert find_paths(root1, 23) == expected1, f"Test 1 failed: {find_paths(root1, 23)}"

    # 🔲 Edge cases
    assert find_paths(None, 0) == [], "Edge 1: Empty tree"
    assert find_paths(TreeNode(42), 42) == [[42]], "Edge 2: Single node matches"
    assert find_paths(TreeNode(42), 10) == [], "Edge 3: Single node doesn't match"

    print("All tests passed!")
