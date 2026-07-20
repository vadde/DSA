"""
============================================================
Problem: N-ary Tree Level Order Traversal
Pattern: Tree BFS (Level Order Traversal)
Difficulty: Medium
Link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Like a normal level order traversal, but nodes can have many children instead
of just a left and right child. We need to return a list of lists, where each
inner list contains the values of the nodes at that level.

APPROACH:
---------
1. Standard BFS using a queue.
2. At each level, determine the number of nodes currently in the queue.
3. Dequeue that many nodes, add their values to the current level's list.
4. Enqueue all children of those nodes.

COMPLEXITY:
-----------
Time:  O(N) - visit each node exactly once.
Space: O(N) - queue can hold at most N nodes (the widest level).

EDGE CASES:
-----------
- Empty tree -> return [].
- Tree with only a root node.
- A very wide tree where the root has hundreds of children.
============================================================
"""

from collections import deque
from typing import List, Optional

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def levelOrder(root: 'Node') -> List[List[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            for child in node.children:
                queue.append(child)
                
        result.append(current_level)
        
    return result

if __name__ == "__main__":
    # Test 1:
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
    assert levelOrder(root) == [[1], [3, 2, 4], [5, 6]], "Test 1 Failed"
    
    # Test 2: Empty tree
    assert levelOrder(None) == [], "Test 2 Failed"
    
    # Test 3: Single node
    assert levelOrder(Node(42)) == [[42]], "Test 3 Failed"
    
    print("All tests passed!")
