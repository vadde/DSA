"""
============================================================
Problem: Reverse every K-element Sub-list
Pattern: In-place Reversal of a LinkedList
Difficulty: Medium
Link: https://www.educative.io/courses/grokking-the-coding-interview/rm8yLzKMr8Q
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You still have a line of friends holding hands. This time, you want them to turn 
around in groups of K. 
If K=3, you count 1, 2, 3 friends, and ask those 3 to flip around.
Then you count the next 1, 2, 3 friends, and ask them to flip around.
You keep doing this until you reach the end of the line.
If you get to the end and there are only 2 friends left (less than K), you just 
flip those last 2 friends anyway.
We can solve this by taking our "Reverse a Sub-list" magic trick and just putting 
it inside a giant `while` loop that keeps running until everyone is done!

APPROACH:
---------
1. Initialize `current = head`, `prev = None`.
2. Loop `while current is not None:`
   - Memorize `node_before_sublist = prev`.
   - Memorize `last_node_of_sublist = current`.
   - Run our standard 4-step reversal logic for EXACTLY `k` steps (or until `current` is None).
   - Reconnect the severed edges just like in Problem 2:
     - `node_before_sublist.next = prev` (or update `head = prev` if it's the very first group).
     - `last_node_of_sublist.next = current`
   - Set `prev = last_node_of_sublist`. This is the most crucial step! The tail of the 
     group we just reversed is now the "node before" for the NEXT group!
3. Return `head`.

COMPLEXITY:
-----------
Time:  O(N) — Every node is visited exactly once.
Space: O(1) — Sorting is done completely in-place.

EDGE CASES:
-----------
- Edge case 1: The last sub-list has fewer than K elements. Handled properly by the inner loop breaking on `current is None`.
- Edge case 2: `k <= 1`. A group of 1 doesn't need reversing. (Though the loop naturally handles it, we can just return early).
============================================================
"""

from typing import Optional

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_every_k_elements(head: Optional[Node], k: int) -> Optional[Node]:
    """
    Reverses every K-element sub-list in a Singly LinkedList in-place.
    """
    if k <= 1 or not head:
        return head

    current: Optional[Node] = head
    prev: Optional[Node] = None

    while current is not None:
        # Save pointers to reconnect later
        node_before_sublist = prev
        last_node_of_sublist = current
        
        # Reverse 'k' nodes
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
            # We are reversing the very first group, so the head changes
            head = prev
            
        last_node_of_sublist.next = current
        
        # Prepare for the next group
        # The tail of our newly reversed group becomes the 'prev' for the next group
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
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
    # k = 3
    # Expected: 3->2->1 -> 6->5->4 -> 8->7
    head1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
    res1 = reverse_every_k_elements(head1, 3)
    assert get_list_values(res1) == [3, 2, 1, 6, 5, 4, 8, 7], f"Test 1 failed: {get_list_values(res1)}"

    # 🔲 Edge cases
    # k = 2 (Even splits)
    # Expected: 2->1 -> 4->3 -> 6->5 -> 8->7
    head2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
    res2 = reverse_every_k_elements(head2, 2)
    assert get_list_values(res2) == [2, 1, 4, 3, 6, 5, 8, 7], "Edge 1 failed (k=2)"

    # k = 1 (No reversal needed)
    head3 = Node(1, Node(2, Node(3)))
    res3 = reverse_every_k_elements(head3, 1)
    assert get_list_values(res3) == [1, 2, 3], "Edge 2 failed (k=1)"

    print("All tests passed!")
