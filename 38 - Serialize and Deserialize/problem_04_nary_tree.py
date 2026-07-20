"""
============================================================
Problem: Serialize and Deserialize N-ary Tree
Pattern: Serialize and Deserialize
Difficulty: Hard
Link: https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Like serializing a Binary Tree, but each node can have ANY number of children
(not just left and right). We need to encode the tree into a string and decode
it back perfectly.

KEY CHALLENGE: How do you know where one node's children end and siblings begin?
Use a SENTINEL (e.g., "#") to mark the end of a node's children list.

APPROACH:
---------
Serialization (Pre-order DFS):
1. Write the node's value.
2. Recursively serialize each child.
3. After all children are done, write "#" (end-of-children marker).

Deserialization:
1. Read the next token. If it's "#", return None (end of children).
2. Otherwise, create a node with that value.
3. Keep reading children until you encounter "#".

COMPLEXITY:
-----------
Time:  O(N) for both.
Space: O(N)

EDGE CASES:
-----------
- Empty tree → None.
- Node with 0 children (leaf).
- Very deep tree.
============================================================
"""

from typing import List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


class Codec:
    def serialize(self, root: Optional['Node']) -> str:
        if not root:
            return ""

        tokens = []

        def dfs(node):
            tokens.append(str(node.val))
            for child in node.children:
                dfs(child)
            tokens.append("#")  # End-of-children sentinel

        dfs(root)
        return ",".join(tokens)

    def deserialize(self, data: str) -> Optional['Node']:
        if not data:
            return None

        it = iter(data.split(","))

        def dfs():
            val = next(it)
            if val == "#":
                return None
            node = Node(int(val))
            while True:
                child = dfs()
                if child is None:
                    break
                node.children.append(child)
            return node

        return dfs()


if __name__ == "__main__":
    # N-ary tree:
    #       1
    #     / | \
    #    3  2  4
    #   / \
    #  5   6
    root = Node(1, [
        Node(3, [Node(5), Node(6)]),
        Node(2),
        Node(4)
    ])

    codec = Codec()
    serialized = codec.serialize(root)
    decoded = codec.deserialize(serialized)

    assert decoded.val == 1
    assert len(decoded.children) == 3
    assert decoded.children[0].val == 3
    assert len(decoded.children[0].children) == 2
    assert decoded.children[0].children[0].val == 5
    assert decoded.children[0].children[1].val == 6
    assert decoded.children[1].val == 2
    assert decoded.children[2].val == 4

    # Empty tree
    assert codec.deserialize(codec.serialize(None)) is None, "Empty tree"

    # Single node
    single = Node(42)
    dec = codec.deserialize(codec.serialize(single))
    assert dec.val == 42 and dec.children == [], "Single node"

    print("All tests passed!")
