"""
============================================================
Problem: Binary Tree Level Order Traversal
Pattern: Tree Breadth First Search
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a family tree. You want to take a picture of every generation separately.
First, a picture of the Great-Grandparents.
Then, a picture of the Grandparents.
Then, a picture of the Parents.
We can do this easily using a Queue (like a line for a rollercoaster).
First, the Great-Grandparents get in line.
You look at the line and say, "Okay, there is 1 person in line right now. Let's 
take a picture of just them."
While they are getting their picture taken, they tell all their kids (the Grandparents) 
to get in the back of the line!
Once the first picture is done, you look at the line again. Now there are 2 people 
in line (the Grandparents). You say, "Okay, I will take a picture of the next 2 
people!"
They get their picture taken, and tell THEIR kids to get in line.
By strictly counting how many people are in line *before* you start taking pictures 
for that round, you perfectly separate every generation!

APPROACH:
---------
1. If the `root` is None, return an empty list `[]`.
2. Initialize a queue using `collections.deque` and add the `root` to it.
3. Initialize an empty `result` list to hold the lists of values for each level.
4. Loop `while queue is not empty`:
   - Get the number of nodes currently in the queue: `level_size = len(queue)`.
     This is crucial because we only want to process THIS level.
   - Initialize `current_level = []` to hold the values for this generation.
   - Loop exactly `level_size` times:
     - Pop the front node: `node = queue.popleft()`.
     - Add its value to `current_level`.
     - If `node.left` exists, add it to the back of the queue.
     - If `node.right` exists, add it to the back of the queue.
   - After the inner loop, append `current_level` to `result`.
5. Return `result`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is added to the queue once and removed once.
Space: O(N) — The queue can hold up to N/2 nodes at the bottom level of the tree.

EDGE CASES:
-----------
- Edge case 1: Empty tree (`root` is None). Returns `[]`.
- Edge case 2: Tree with only one node (the root). Returns `[[root.value]]`.
============================================================
"""

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Returns the level order traversal of a binary tree's nodes' values.
    """
    if not root:
        return []

    result: List[List[int]] = []
    queue = deque([root])

    while queue:
        # Take a snapshot of how many nodes are on the current level
        level_size = len(queue)
        current_level: List[int] = []

        # Process exactly that many nodes
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            # Enqueue the children for the NEXT level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Store the current level's results
        result.append(current_level)

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
    
    expected1 = [[12], [7, 1], [9, 2, 10, 5]]
    assert level_order(root1) == expected1, f"Test 1 failed: {level_order(root1)}"

    # 🔲 Edge cases
    assert level_order(None) == [], "Edge 1: Empty tree"
    assert level_order(TreeNode(42)) == [[42]], "Edge 2: Single node"

    print("All tests passed!")
