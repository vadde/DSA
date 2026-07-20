"""
============================================================
Problem: Zigzag Traversal
Pattern: Tree Breadth First Search
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are taking pictures of the family tree again, but this time you want to be fancy.
For the Grandparents (Level 1), you take the picture from Left to Right.
For the Parents (Level 2), you take the picture from Right to Left!
For the Kids (Level 3), you go back to Left to Right.
It's a Zigzag!
To do this, we DO NOT change how people wait in line. They still wait in the exact 
same Queue (from left to right).
The ONLY thing that changes is how we put them into the photo album.
If it's a "Left to Right" round, we just append them normally to the end of the page.
If it's a "Right to Left" round, we push them into the FRONT of the page 
(`appendleft()`), so the first person we took a picture of ends up at the very back!
After every round, we just flip a boolean switch (`left_to_right = not left_to_right`).

APPROACH:
---------
1. If the `root` is None, return `[]`.
2. Initialize `queue = deque([root])`, `result = []`.
3. Initialize a boolean `left_to_right = True`.
4. Loop `while queue is not empty`:
   - `level_size = len(queue)`
   - `current_level = deque()`  <-- Use a deque for the current level!
   - Loop `level_size` times:
     - Pop `node` from queue.
     - IF `left_to_right`: `current_level.append(node.value)`
     - ELSE: `current_level.appendleft(node.value)`
     - Append children to the queue (always Left then Right).
   - Append `list(current_level)` to `result`.
   - Flip the switch: `left_to_right = not left_to_right`.
5. Return `result`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited once. `append` and `appendleft` on deque are O(1).
Space: O(N) — The queue can hold up to N/2 nodes at the bottom level of the tree.

EDGE CASES:
-----------
- Edge case 1: Empty tree. Returns `[]`.
- Edge case 2: Tree with only left children. Still zigzags properly.
============================================================
"""

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Returns the zigzag level order traversal of a binary tree's nodes' values.
    """
    if not root:
        return []

    result: List[List[int]] = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        current_level = deque()

        for _ in range(level_size):
            node = queue.popleft()
            
            # The magic happens here!
            if left_to_right:
                current_level.append(node.value)
            else:
                current_level.appendleft(node.value)

            # Children are always added to the queue left-to-right
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(current_level))
        # Flip the direction for the next level
        left_to_right = not left_to_right

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
    # L0: L->R [12]
    # L1: R->L [1, 7]
    # L2: L->R [9, 2, 10, 5]
    expected1 = [[12], [1, 7], [9, 2, 10, 5]]
    assert zigzag_traversal(root1) == expected1, f"Test 1 failed: {zigzag_traversal(root1)}"

    # 🔲 Edge cases
    assert zigzag_traversal(None) == [], "Edge 1: Empty tree"
    assert zigzag_traversal(TreeNode(42)) == [[42]], "Edge 2: Single node"

    print("All tests passed!")
