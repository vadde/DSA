"""
============================================================
Problem: Clone N-ary Tree
Pattern: Clone Pattern (DFS + Hash Map)
Difficulty: Hard
Link: https://leetcode.com/problems/clone-n-ary-tree/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a tree where each node can have many children (not just 2 like a
binary tree). Create an exact deep copy — every node must be a NEW object
with the same value and same structure.

APPROACH:
---------
1. DFS: For each node, create a new Node with the same value.
2. Recursively clone all children and attach them.
3. No cycles in a tree, so no need for a visited hash map (unlike Clone Graph).

COMPLEXITY:
-----------
Time:  O(N) — visit every node once.
Space: O(N) — recursion stack + new tree nodes.

EDGE CASES:
-----------
- Empty tree → return None.
- Single node with no children.
- Very wide tree (many children per node).
============================================================
"""

from typing import Optional, List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


def clone_tree(root: Optional['Node']) -> Optional['Node']:
    if not root:
        return None

    clone = Node(root.val)
    for child in root.children:
        clone.children.append(clone_tree(child))

    return clone


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

    cloned = clone_tree(root)

    assert cloned is not root, "Must be a deep copy"
    assert cloned.val == 1
    assert len(cloned.children) == 3
    assert cloned.children[0].val == 3
    assert cloned.children[0] is not root.children[0], "Children must be clones too"
    assert cloned.children[0].children[0].val == 5
    assert cloned.children[0].children[1].val == 6

    # Empty
    assert clone_tree(None) is None, "Empty tree"

    # Single node
    single_clone = clone_tree(Node(42))
    assert single_clone.val == 42 and single_clone.children == [], "Single node"

    print("All tests passed!")
