"""
============================================================
Problem: Connect Level Order Siblings
Pattern: Tree Breadth First Search
Difficulty: Medium
Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine all the kids in a generation are holding hands from left to right.
The leftmost kid holds the hand of the kid next to them, and so on.
The rightmost kid doesn't have anyone to hold onto, so their hand just hangs 
empty (points to `None`).
We already know how to perfectly line up each generation using BFS!
All we have to do is remember who the "Previous" kid was.
When we pop a kid out of the line, we tell the "Previous" kid to grab this 
new kid's hand (`previous_node.next = current_node`).
Then, the new kid becomes the "Previous" kid for the *next* time we pop!
At the start of every new generation, we reset the "Previous" kid to `None`, 
so generations don't accidentally hold hands with each other.

APPROACH:
---------
1. If the `root` is None, return `None`.
2. Initialize `queue = deque([root])`.
3. Loop `while queue is not empty`:
   - `level_size = len(queue)`
   - Initialize `previous_node = None`. This resets at the start of every level!
   - Loop `level_size` times:
     - Pop `current_node` from queue.
     - If `previous_node` is not None:
       - `previous_node.next = current_node`
     - Update `previous_node = current_node`.
     - Append children to the queue (Left then Right).
4. Return the modified `root`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited once.
Space: O(N) — The queue can hold up to N/2 nodes at the bottom level of the tree.

EDGE CASES:
-----------
- Edge case 1: Empty tree. Returns `None`.
- Edge case 2: Tree with single node. Root's `next` remains `None`.
============================================================
"""

from collections import deque
from typing import Optional

class Node:
    def __init__(self, value=0, left=None, right=None, next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

def connect_siblings(root: Optional[Node]) -> Optional[Node]:
    """
    Connects each node in a binary tree with its level order sibling.
    """
    if not root:
        return None

    queue = deque([root])

    while queue:
        level_size = len(queue)
        
        # Reset previous_node at the start of every new level
        previous_node = None

        for _ in range(level_size):
            current_node = queue.popleft()

            # If there was a previous node on this level, link it to the current one
            if previous_node:
                previous_node.next = current_node
            
            # The current node becomes the previous node for the next iteration
            previous_node = current_node

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return root

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    def get_next_values(root):
        """Helper to collect 'next' pointer values for easy testing."""
        res = []
        curr = root
        while curr:
            level_head = curr
            level_res = []
            while level_head:
                level_res.append(level_head.value)
                level_head = level_head.next
            res.append(level_res)
            curr = curr.left
        return res

    # ✅ Normal cases
    #       12
    #      /  \
    #     7    1
    #    / \  / \
    #   9  2 10  5
    root1 = Node(12)
    root1.left = Node(7)
    root1.right = Node(1)
    root1.left.left = Node(9)
    root1.left.right = Node(2)
    root1.right.left = Node(10)
    root1.right.right = Node(5)
    
    connected_root = connect_siblings(root1)
    
    # Let's verify the connections!
    assert connected_root.next is None, "12 -> None"
    assert connected_root.left.next == connected_root.right, "7 -> 1"
    assert connected_root.right.next is None, "1 -> None"
    assert connected_root.left.left.next == connected_root.left.right, "9 -> 2"
    assert connected_root.left.right.next == connected_root.right.left, "2 -> 10"
    assert connected_root.right.left.next == connected_root.right.right, "10 -> 5"
    assert connected_root.right.right.next is None, "5 -> None"

    # Using our helper
    expected1 = [[12], [7, 1], [9, 2, 10, 5]]
    assert get_next_values(connected_root) == expected1, "Helper traversal failed"

    # 🔲 Edge cases
    assert connect_siblings(None) is None, "Edge 1: Empty tree"

    print("All tests passed!")
