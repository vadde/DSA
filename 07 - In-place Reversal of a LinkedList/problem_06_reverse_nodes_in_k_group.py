"""
============================================================
Problem: Reverse Nodes in k-Group
Pattern: In-place Reversal of a LinkedList
Difficulty: Hard
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
This is a very strict version of the "Reverse every K-element Sub-list" problem.
Imagine you have a line of friends and K=3. 
You walk up to the first 3 friends, and flip them around.
You walk up to the next 3 friends, and flip them around.
Finally, you reach the end of the line, and there are only 2 friends left.
In the old problem, we flipped them anyway!
But in THIS problem, the rule is: "If there are less than 3 friends, DO NOT touch them!"
So you just leave the last 2 friends exactly as they are and go home.
To do this safely, before we even *start* flipping a group, we just do a quick count:
"1, 2, 3... okay, we have enough, let's flip!"
If the count stops at 2 because the line ended, we just stop entirely.

APPROACH:
---------
1. Write a small helper function `has_k_nodes(node, k)` that just walks forward `k` steps.
   If it hits `None` before reaching `k`, it returns `False`. Otherwise `True`.
2. Initialize `current = head`, `prev = None`.
3. Loop `while current is not None:`
   - NEW STEP: `if not has_k_nodes(current, k): break`
   - Memorize `node_before_sublist = prev` and `last_node_of_sublist = current`.
   - Run standard reversal logic for EXACTLY `k` steps.
   - Reconnect edges just like all other problems.
   - Set `prev = last_node_of_sublist`.
4. Return `head`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited twice (once by `has_k_nodes` to count, once to reverse/skip).
Space: O(1) — Completely in-place.

EDGE CASES:
-----------
- Edge case 1: Length of list is not a multiple of `k`. Leftover nodes remain unchanged.
- Edge case 2: `k = 1`. Returns list unchanged.
============================================================
"""

from typing import Optional

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_k_nodes(node: Optional[Node], k: int) -> bool:
    count = 0
    while node and count < k:
        node = node.next
        count += 1
    return count == k

def reverse_k_group(head: Optional[Node], k: int) -> Optional[Node]:
    """
    Reverses nodes in k-group. If the final group has < k nodes, it is left unchanged.
    """
    if k <= 1 or not head:
        return head

    current: Optional[Node] = head
    prev: Optional[Node] = None

    while current is not None:
        # Check if we have at least k nodes remaining
        if not has_k_nodes(current, k):
            break

        # Save pointers to reconnect later
        node_before_sublist = prev
        last_node_of_sublist = current
        
        # Reverse EXACTLY 'k' nodes
        i = 0
        while current is not None and i < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            i += 1
            
        # Reconnect the reversed sub-list
        if node_before_sublist is not None:
            node_before_sublist.next = prev
        else:
            head = prev
            
        last_node_of_sublist.next = current
        
        # Prepare for the next group
        prev = last_node_of_sublist

    return head

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    def get_list_values(node):
        res = []
        while node:
            res.append(node.value)
            node = node.next
        return res

    # ✅ Normal cases
    # 1 -> 2 -> 3 -> 4 -> 5, k = 2
    # Expected: 2->1 -> 4->3 -> 5 (leftover)
    head1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    res1 = reverse_k_group(head1, 2)
    assert get_list_values(res1) == [2, 1, 4, 3, 5], f"Test 1 failed: {get_list_values(res1)}"

    # 1 -> 2 -> 3 -> 4 -> 5, k = 3
    # Expected: 3->2->1 -> 4->5 (leftover)
    head2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    res2 = reverse_k_group(head2, 3)
    assert get_list_values(res2) == [3, 2, 1, 4, 5], "Test 2 failed"

    # 🔲 Edge cases
    # k = 1 (No reversal needed)
    head3 = Node(1, Node(2, Node(3)))
    res3 = reverse_k_group(head3, 1)
    assert get_list_values(res3) == [1, 2, 3], "Edge 1 failed (k=1)"

    print("All tests passed!")
