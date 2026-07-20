"""
============================================================
Problem: Reverse alternating K-element Sub-list
Pattern: In-place Reversal of a LinkedList
Difficulty: Medium
Link: https://www.educative.io/courses/grokking-the-coding-interview/m2GQywqAN0N
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a line of friends holding hands, and you want them to turn around in 
groups of K, but skipping every other group!
If K=2, the first 2 friends flip.
The next 2 friends stay EXACTLY the same (just skip past them).
The next 2 friends flip.
The next 2 friends stay the same.
You keep doing this alternating pattern until you run out of friends.
This is exactly like our last problem, except after we reconnect the reversed 
group, we literally just tell our `prev` and `current` pointers to walk forward 
by K steps before we repeat the loop!

APPROACH:
---------
1. Initialize `current = head`, `prev = None`.
2. Loop `while current is not None:`
   - Memorize `node_before_sublist = prev`.
   - Memorize `last_node_of_sublist = current`.
   - Run standard reversal logic for EXACTLY `k` steps (or until `current` is None).
   - Reconnect edges:
     - `node_before_sublist.next = prev` (or `head = prev`).
     - `last_node_of_sublist.next = current`.
   - Set `prev = last_node_of_sublist`.
   - NEW STEP: We just reversed a group of K. Now we must SKIP a group of K!
     Loop `i` from 0 to `k`:
       - If `current` is None, break!
       - `prev = current`
       - `current = current.next`
3. Return `head`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited either during reversal or during skipping. Total O(N).
Space: O(1) — Reversal and skipping are completely in-place.

EDGE CASES:
-----------
- Edge case 1: The skipped group has fewer than K elements. Handled properly by the inner skip loop breaking.
- Edge case 2: `k <= 1`. Return early.
============================================================
"""

from typing import Optional

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_alternate_k_elements(head: Optional[Node], k: int) -> Optional[Node]:
    """
    Reverses alternating K-element sub-lists in a Singly LinkedList in-place.
    """
    if k <= 1 or not head:
        return head

    current: Optional[Node] = head
    prev: Optional[Node] = None

    while current is not None:
        # Save pointers to reconnect later
        node_before_sublist = prev
        last_node_of_sublist = current
        
        # 1. Reverse 'k' nodes
        i = 0
        while current is not None and i < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            i += 1
            
        # 2. Reconnect the reversed sub-list
        if node_before_sublist is not None:
            node_before_sublist.next = prev
        else:
            head = prev
            
        last_node_of_sublist.next = current
        prev = last_node_of_sublist

        # 3. Skip the next 'k' nodes (leave them in their original order)
        i = 0
        while current is not None and i < k:
            prev = current
            current = current.next
            i += 1

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
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
    # k = 2
    # Expected: 2->1 -> 3->4 (skipped) -> 6->5 -> 7->8 (skipped)
    head1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
    res1 = reverse_alternate_k_elements(head1, 2)
    assert get_list_values(res1) == [2, 1, 3, 4, 6, 5, 7, 8], f"Test 1 failed: {get_list_values(res1)}"

    # 🔲 Edge cases
    # k = 3
    # Expected: 3->2->1 -> 4->5->6 (skipped) -> 8->7
    head2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
    res2 = reverse_alternate_k_elements(head2, 3)
    assert get_list_values(res2) == [3, 2, 1, 4, 5, 6, 8, 7], "Edge 1 failed (k=3)"

    print("All tests passed!")
