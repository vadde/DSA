"""
============================================================
Problem: Tree Diameter
Pattern: Tree Depth First Search
Difficulty: Hard (Advanced)
Link: https://leetcode.com/problems/diameter-of-binary-tree/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine stretching a string from one leaf of the tree as far across the tree as 
possible to another leaf. 
The length of this string is the "Diameter" of the tree.
You might think: "Oh, it's just the distance from the furthest leaf on the left 
to the furthest leaf on the right of the ROOT!"
But wait! What if the left branch is extremely short, but the right branch is 
MASSIVE and branches out into its own two giant sub-branches? 
The longest string might be completely inside the right branch, never even touching 
the root!
To solve this, we can't just check from the top down. We have to work BOTTOM-UP.
Every node asks its left child: "How tall are you?"
And asks its right child: "How tall are you?"
The node then says: "If I stretch my string from the bottom of my left child, 
through me, down to the bottom of my right child, the string would be exactly 
`left_tall + right_tall + 1` nodes long!"
Every single node calculates this, and we just remember the biggest number we see.
To answer its own parent, the node passes up its OWN height: 
`max(left_tall, right_tall) + 1`.
Because we process the children before the parent, this is called **Post-order Traversal**.

APPROACH:
---------
1. Initialize a global/nonlocal variable `max_diameter = 0`.
2. Define a recursive helper `calculate_height(node)`.
3. Base case: If `node` is None, its height is `0`.
4. Recursive step:
   - `left_height = calculate_height(node.left)`
   - `right_height = calculate_height(node.right)`
5. The diameter of the tree passing *through* the current node is:
   - `current_diameter = left_height + right_height + 1` (Count of nodes)
   - Note: Some variations (like LeetCode) ask for the number of EDGES, which is 
     `left_height + right_height`. The Educative variation asks for number of NODES.
     We will calculate nodes.
6. Update our record: `max_diameter = max(max_diameter, current_diameter)`.
7. Return the height of the current node to its parent:
   - `return max(left_height, right_height) + 1`.
8. Start the recursion from the root and return `max_diameter`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited once.
Space: O(H) — The recursion stack is bounded by the height of the tree.

EDGE CASES:
-----------
- Edge case 1: Empty tree. Returns `0`.
- Edge case 2: Tree with one node. Returns `1`.
============================================================
"""

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_diameter(root: Optional[TreeNode]) -> int:
    """
    Finds the diameter of a binary tree (represented as the maximum number of nodes).
    """
    max_diameter = 0

    def calculate_height(node: Optional[TreeNode]) -> int:
        nonlocal max_diameter
        
        if not node:
            return 0

        # POST-ORDER: Ask the children first
        left_height = calculate_height(node.left)
        right_height = calculate_height(node.right)

        # Do the math for the current node
        current_diameter = left_height + right_height + 1
        
        # Update the global record if this is the longest string we've seen
        max_diameter = max(max_diameter, current_diameter)

        # Tell our parent how tall we are
        return max(left_height, right_height) + 1

    calculate_height(root)
    return max_diameter

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    
    # Path: 4 -> 2 -> 1 -> 3 (4 nodes)
    # OR 5 -> 2 -> 1 -> 3 (4 nodes)
    assert find_diameter(root1) == 4, f"Test 1 failed: {find_diameter(root1)}"

    # Diameter completely contained in the right subtree
    #       1
    #      / \
    #     2   3
    #        / \
    #       5   6
    #      /     \
    #     7       8
    #    /         \
    #   9           10
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(6)
    root2.right.left.left = TreeNode(7)
    root2.right.left.left.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)
    root2.right.right.right.right = TreeNode(10)
    
    # Path: 9 -> 7 -> 5 -> 3 -> 6 -> 8 -> 10 (7 nodes)
    assert find_diameter(root2) == 7, f"Test 2 failed: {find_diameter(root2)}"

    # 🔲 Edge cases
    assert find_diameter(None) == 0, "Edge 1: Empty tree"
    assert find_diameter(TreeNode(1)) == 1, "Edge 2: Single node"

    print("All tests passed!")
