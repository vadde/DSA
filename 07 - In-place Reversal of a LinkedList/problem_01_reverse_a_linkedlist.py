"""
============================================================
Problem: Reverse a LinkedList
Pattern: In-place Reversal of a LinkedList
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-linked-list/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a line of people holding hands, all facing forward. 
Person A is holding Person B's hand, Person B is holding Person C's hand.
You want everyone to turn around, so Person C holds Person B's hand, and Person B 
holds Person A's hand.
You can't just tell everyone to turn around at once! If Person A lets go of Person B, 
Person A might forget who Person B was.
So you walk down the line. You ask Person A to let go of Person B, and instead 
reach out their hand behind them (to nothing, `None`). 
But before they let go, you memorized that Person B was next!
Then you step over to Person B. You tell them to let go of Person C (after memorizing 
Person C), and reach back to grab Person A.
You repeat this until you reach the end of the line!

APPROACH:
---------
1. We need 3 variables: `prev` (who we just talked to), `current` (who we are talking to), 
   and `next_node` (who is next in line).
2. Initialize `prev = None` and `current = head`.
3. Loop while `current` is not `None`:
   - `next_node = current.next` (Memorize the next person so we don't lose them)
   - `current.next = prev` (Turn around! Grab the previous person)
   - `prev = current` (Step sideways. You are now the 'previous' person for the next step)
   - `current = next_node` (Step sideways. The next person in line is now the 'current' person)
4. When `current` reaches `None`, `prev` will be standing on the very last node.
   That last node is now the head of our reversed list! Return `prev`.

COMPLEXITY:
-----------
Time:  O(N) — We walk down the list exactly once.
Space: O(1) — We only use three variables, regardless of how long the line is.

EDGE CASES:
-----------
- Edge case 1: Empty list (`head` is `None`). Returns `None` perfectly.
- Edge case 2: Single node. Loop runs once, `prev` becomes that node, returns it perfectly.
============================================================
"""

from typing import Optional

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head: Optional[Node]) -> Optional[Node]:
    """
    Reverses a Singly LinkedList in-place and returns the new head.
    """
    prev: Optional[Node] = None
    current: Optional[Node] = head

    while current is not None:
        # 1. Save the next node so we don't lose the rest of the list
        next_node = current.next
        
        # 2. Reverse the pointer
        current.next = prev
        
        # 3. Advance both pointers forward
        prev = current
        current = next_node

    # After the loop, current is None, and prev is the new head!
    return prev

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
    head1 = Node(2, Node(4, Node(6, Node(8, Node(10)))))
    res1 = reverse(head1)
    assert get_list_values(res1) == [10, 8, 6, 4, 2], f"Test 1 failed: {get_list_values(res1)}"

    # 🔲 Edge cases
    assert reverse(None) is None, "Edge 1: Empty list"
    
    head2 = Node(1)
    res2 = reverse(head2)
    assert get_list_values(res2) == [1], "Edge 2: Single node"

    print("All tests passed!")
