"""
============================================================
Problem: Serialize and Deserialize Binary Tree
Pattern: Serialize and Deserialize
Difficulty: Hard
LeetCode: #297
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Convert a Binary Tree into a string, and then convert that string back
into the exact same Binary Tree.

APPROACH: Pre-order Traversal (DFS)
---------
Serialization: Visit root, then left, then right. Put a comma between values.
CRITICAL: If a child is `None`, write an "N". This ensures the tree's shape
is uniquely preserved!
Deserialization: Split the string by commas. Use an iterator (or queue) to
pop the first element. If it's "N", return `None`. Otherwise, create a Node,
recursively build its left child, then its right child.

COMPLEXITY:
-----------
Time:  O(N) for both.
Space: O(N) to store the string and recursion stack.
============================================================
"""


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
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        vals = iter(data.split(","))
        
        def dfs():
            val = next(vals)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()


if __name__ == "__main__":
    # Tree:
    #       1
    #      / \
    #     2   3
    #        / \
    #       4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    codec = Codec()
    serialized = codec.serialize(root)
    assert serialized == "1,2,N,N,3,4,N,N,5,N,N"
    
    decoded = codec.deserialize(serialized)
    assert decoded.val == 1
    assert decoded.left.val == 2
    assert decoded.right.left.val == 4
    
    print("All tests passed!")
