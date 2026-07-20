"""
============================================================
Problem: Reverse a Sub-list
Pattern: In-place Reversal of a LinkedList
Difficulty: Medium
Link: https://leetcode.com/problems/reverse-linked-list-ii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a line of friends holding hands. This time, you don't want everyone 
to turn around. You only want the friends from position P to position Q to 
turn around!
If the line is: Alice -> Bob -> Charlie -> Dave -> Eve
And you want to reverse from position 2 (Bob) to position 4 (Dave):
First, you walk up to Alice. Alice is the "friend right before the flip".
You ask Alice to wait for a second and let go of Bob.
Then, you take the group (Bob, Charlie, Dave) and use the standard reversal trick 
we learned to flip them around: Dave -> Charlie -> Bob.
Now, you have a flipped group, but they are detached from the line!
You just need to reconnect them:
1. Alice needs to hold the hand of the new front of the group (Dave).
2. The new back of the group (Bob) needs to reach out and hold Eve's hand.
Boom! The line is back together, with just the middle part reversed!

APPROACH:
---------
1. Skip the first `p - 1` nodes to reach the node just before our sub-list.
   We'll call this `node_before_sublist`.
2. The next node is `p`. We will call this `last_node_of_sublist` because after 
   it gets reversed, it will end up at the very back of the group!
3. Reverse the exact `q - p + 1` nodes using our standard 4-step reversal block.
4. Reconnect the two severed ends:
   - If `node_before_sublist` exists, its `.next` points to `prev` (the new front of the reversed group).
   - If it doesn't exist (because `p=1`), `prev` becomes the new global `head`!
   - `last_node_of_sublist.next` points to `current` (the person waiting after the reversed group).
5. Return the (potentially new) `head`.

COMPLEXITY:
-----------
Time:  O(N) — We only walk down the list once to reach the node and perform the reversal.
Space: O(1) — Only a few pointer variables are used.

EDGE CASES:
-----------
- Edge case 1: `p == q`. Nothing to reverse, returns identical list.
- Edge case 2: `p == 1`. The sub-list starts at the very beginning, so the global `head` changes.
============================================================
"""

from typing import Optional

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_sub_list(head: Optional[Node], p: int, q: int) -> Optional[Node]:
    """
    Reverses a sub-list of a Singly LinkedList from position p to q in-place.
    """
    if p == q or not head:
        return head

    # 1. Skip the first p-1 nodes
    current: Optional[Node] = head
    prev: Optional[Node] = None
    
    # Example: if p=2, we loop 1 time.
    for _ in range(p - 1):
        prev = current
        current = current.next
        
    # 'prev' is now sitting on the node right before the sublist
    # 'current' is sitting on the first node of the sublist
    node_before_sublist = prev
    last_node_of_sublist = current
    
    # 2. Reverse the nodes between p and q
    # We do exactly q - p + 1 reversals
    for _ in range(q - p + 1):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    # 3. Reconnect the severed edges
    if node_before_sublist is not None:
        # The node before the sublist now points to the reversed head
        node_before_sublist.next = prev
    else:
        # We reversed from the very beginning! The head of the list changes.
        head = prev
        
    # The last node of the reversed sublist points to whatever comes next
    last_node_of_sublist.next = current
    
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
    # 1 -> 2 -> 3 -> 4 -> 5, reverse 2 to 4
    head1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    res1 = reverse_sub_list(head1, 2, 4)
    assert get_list_values(res1) == [1, 4, 3, 2, 5], f"Test 1 failed: {get_list_values(res1)}"

    # 🔲 Edge cases
    # Start at 1 (head changes)
    head2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    res2 = reverse_sub_list(head2, 1, 3)
    assert get_list_values(res2) == [3, 2, 1, 4, 5], "Edge 1 failed (p=1)"
    
    # p == q
    head3 = Node(1, Node(2, Node(3)))
    res3 = reverse_sub_list(head3, 2, 2)
    assert get_list_values(res3) == [1, 2, 3], "Edge 2 failed (p=q)"

    print("All tests passed!")
