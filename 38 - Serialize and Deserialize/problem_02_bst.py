"""
============================================================
Problem: Serialize and Deserialize BST
Pattern: Serialize and Deserialize
Difficulty:
Link: https://leetcode.com/problem-placeholder/ Medium
LeetCode: #449
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Like the previous problem, but for a Binary Search Tree (BST).
Can we make the string shorter? Yes! Since it's a BST, the values themselves
dictate the structure (left is smaller, right is bigger). We don't need to store "N"!

APPROACH: Pre-order Traversal + Upper/Lower Bounds
---------
Serialization: Just normal pre-order traversal (Root, Left, Right). No "N" markers!
Deserialization: We read the values. Because it's a BST, we can use an upper and
lower bound to determine if a value belongs to the left child or the right child.

COMPLEXITY:
-----------
Time:  O(N) for both.
Space: O(N)

EDGE CASES:
-----------
- Basic empty/null edge cases.
- Boundary constraints.
============================================================
"""

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        res = []
        def dfs(node):
            if not node:
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
            
        vals = collections.deque(int(x) for x in data.split(","))
        
        def build(min_val, max_val):
            if not vals:
                return None
            if not (min_val < vals[0] < max_val):
                return None
                
            val = vals.popleft()
            node = TreeNode(val)
            node.left = build(min_val, val)
            node.right = build(val, max_val)
            return node
            
        return build(float('-inf'), float('inf'))


if __name__ == "__main__":
    # BST:
    #       5
    #      / \
    #     3   7
    #    / \   \
    #   2   4   8
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)
    
    codec = Codec()
    serialized = codec.serialize(root)
    assert serialized == "5,3,2,4,7,8"
    
    decoded = codec.deserialize(serialized)
    assert decoded.val == 5
    assert decoded.left.left.val == 2
    assert decoded.right.right.val == 8
    
    print("All tests passed!")
