"""
============================================================
Problem: Path With Given Sequence
Pattern: Tree Depth First Search
Difficulty: Medium
Link: https://www.educative.io/courses/grokking-the-coding-interview/m280XNlPOkn
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are walking down a path in the forest, and you have a treasure map.
The map says: "Walk exactly on the numbers: 1, then 9, then 9".
If you step on a `1`, great! You check the map, and the next number should be `9`.
If the next branch says `5`, you know immediately this is the wrong path! 
You don't even need to walk to the end of it; you can turn around right away.
If you step on `1`, then `9`, then `9`, AND you are at a leaf (the end of a path), 
you found the treasure!
To keep track of where you are on the map, you carry a pointer called `sequence_index`.
Every time you step on a correct number, `sequence_index` goes up by 1.

APPROACH:
---------
1. Define a recursive helper `find_path_recursive(node, sequence, sequence_index)`.
2. If `node` is None, return `False`.
3. If `sequence_index` is too large (out of bounds of the map), return `False`.
4. If the `node.value` does NOT match the number on the map (`sequence[sequence_index]`), 
   return `False` immediately. This is an early exit!
5. If we made it this far, the number matches! Now we ask: Is this the very end 
   of the map AND the end of the tree?
   - `if sequence_index == len(sequence) - 1 and not node.left and not node.right:`
     - Return `True`!
6. If it's not the end yet, keep walking down both the left and right branches, 
   but tell them to look for the NEXT number on the map (`sequence_index + 1`).
   - `return find_path_recursive(...) or find_path_recursive(...)`

COMPLEXITY:
-----------
Time:  O(N) — In the worst case, we check all nodes. But often we exit early if the sequence breaks.
Space: O(H) — The recursion stack is O(H) for the height of the tree.

EDGE CASES:
-----------
- Edge case 1: The sequence is longer than any path in the tree. Returns `False`.
- Edge case 2: The sequence matches, but doesn't reach a leaf node (e.g. sequence is [1, 9] but the path goes [1, 9, 2]). The code specifically checks for `not node.left and not node.right` so it will correctly return `False`.
============================================================
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_path(root: Optional[TreeNode], sequence: List[int]) -> bool:
    """
    Returns True if the sequence is present as a root-to-leaf path.
    """
    if not root or not sequence:
        return False

    def find_path_recursive(node: Optional[TreeNode], sequence: List[int], sequence_index: int) -> bool:
        if not node:
            return False

        seq_len = len(sequence)

        # 1. Early exit if the index is out of bounds or the number doesn't match
        if sequence_index >= seq_len or node.value != sequence[sequence_index]:
            return False

        # 2. If it matches, check if it's the very last number AND a leaf node
        if sequence_index == seq_len - 1 and not node.left and not node.right:
            return True

        # 3. Otherwise, keep going down the tree, looking for the next number
        return find_path_recursive(node.left, sequence, sequence_index + 1) or \
               find_path_recursive(node.right, sequence, sequence_index + 1)

    return find_path_recursive(root, sequence, 0)

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
    
    assert find_path(root1, [1, 9, 9]) == True, "Test 1 failed"
    assert find_path(root1, [1, 7]) == True, "Test 2 failed"
    
    # 🔲 Edge cases
    # Matches part of the path, but doesn't end at a leaf
    assert find_path(root1, [1, 9]) == False, "Edge 1: Doesn't end at leaf"
    
    # Sequence is longer than the path
    assert find_path(root1, [1, 7, 3]) == False, "Edge 2: Sequence too long"
    
    assert find_path(None, [1, 2]) == False, "Edge 3: Empty tree"
    assert find_path(TreeNode(1), []) == False, "Edge 4: Empty sequence"

    print("All tests passed!")
