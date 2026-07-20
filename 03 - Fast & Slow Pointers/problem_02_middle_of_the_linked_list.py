"""
============================================================
Problem: Middle of the LinkedList
Pattern: Fast & Slow Pointers
Difficulty: Easy
Link: https://leetcode.com/problems/middle-of-the-linked-list/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you want to find the exact middle of a long, straight road, but you don't 
know how long the road is, and you don't have a measuring tape. 
You can use two cars: a Slow Car (goes 1 mile per hour) and a Fast Car (goes 2 
miles per hour). Both start at the beginning at the same time.
Because the Fast Car is exactly twice as fast, when the Fast Car reaches the end 
of the road, the Slow Car will be exactly HALFWAY there!
So you just drive both cars, and the moment the Fast Car hits the end, you look 
at where the Slow Car is. That's the middle!

APPROACH:
---------
1. Initialize two pointers, `slow` and `fast`, pointing to the `head` of the LinkedList.
2. Loop while `fast` is not `None` and `fast.next` is not `None`:
   - `slow` moves one step (`slow = slow.next`)
   - `fast` moves two steps (`fast = fast.next.next`)
3. When the loop ends, `fast` is either at the last node or has fallen off the end (None).
4. `slow` will be pointing exactly at the middle node.
5. Return `slow`.

COMPLEXITY:
-----------
Time:  O(N) — The fast pointer traverses the list once.
Space: O(1) — We only use two pointers.

EDGE CASES:
-----------
- Edge case 1: List has only 1 node. Loop doesn't run, returns the `head`.
- Edge case 2: List has an EVEN number of nodes (e.g., 4). There are two "middles". 
  This approach naturally returns the SECOND middle (node 3) because `fast` will hit `None`, 
  allowing `slow` to take one extra step.
============================================================
"""

from typing import Optional

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle_of_linked_list(head: Optional[Node]) -> Optional[Node]:
    """
    Given the head of a Singly LinkedList, returns the middle node.
    If the total number of nodes is even, returns the second middle node.
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps

    return slow

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # Helper to print list from a node
    def get_list_values(node):
        res = []
        while node:
            res.append(node.value)
            node = node.next
        return res

    # ✅ Normal cases (Odd length)
    head1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    assert find_middle_of_linked_list(head1).value == 3, "Test 1 failed: Odd length"

    # ✅ Normal cases (Even length - should return 2nd middle)
    head2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    assert find_middle_of_linked_list(head2).value == 4, "Test 2 failed: Even length"
    
    # 🔲 Edge cases
    head3 = Node(1)
    assert find_middle_of_linked_list(head3).value == 1, "Edge 1: Single node"
    
    assert find_middle_of_linked_list(None) is None, "Edge 2: Empty list"

    print("All tests passed!")
