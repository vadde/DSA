"""
============================================================
Problem: Rotate a LinkedList
Pattern: In-place Reversal of a LinkedList
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-list/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a line of friends holding hands again: 1 -> 2 -> 3 -> 4 -> 5.
You want to "rotate" the line to the right by 2.
This means the last 2 friends in the line (4 and 5) get detached from the back 
and moved to the very front of the line!
Result: 4 -> 5 -> 1 -> 2 -> 3.
How do we do this easily?
Imagine taking the last friend (5) and having them hold the first friend's hand (1).
Now they are standing in a perfect circle! (1 -> 2 -> 3 -> 4 -> 5 -> 1...)
To make the line straight again, we just need to break the circle at the right spot.
Since 2 friends moved to the front, that means the remaining 3 friends (5 - 2 = 3) 
stayed at the back. 
So we walk exactly 3 steps from the start, break the hand-hold there, and whatever 
is next becomes the new front of the line!

APPROACH:
---------
1. Find the total `length` of the LinkedList and get a pointer to the `tail` node.
2. If `k == 0`, `k % length == 0`, or the list is empty/length 1, just return `head`.
3. Normalize `k`: `k = k % length`. (Rotating a line of 5 people by 5 steps does nothing!).
4. Connect the `tail.next = head`. Now we have a circular LinkedList.
5. Find the new tail of the list. It will be the node at position `length - k`.
   - Walk from `head` for `length - k - 1` steps.
   - Let's call this `new_tail`.
6. The new head is `new_tail.next`.
7. Break the circle: `new_tail.next = None`.
8. Return the new head.

COMPLEXITY:
-----------
Time:  O(N) — One pass to find the length and tail. Another partial pass to find the new tail. Total O(N).
Space: O(1) — Only modifying pointers.

EDGE CASES:
-----------
- Edge case 1: `k` is a multiple of the length (e.g., `k=10`, `length=5`). It does nothing.
- Edge case 2: Empty list or list with one node. Handled early.
============================================================
"""

from typing import Optional

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def rotate_linked_list(head: Optional[Node], k: int) -> Optional[Node]:
    """
    Rotates a Singly LinkedList to the right by k nodes.
    """
    if not head or not head.next or k <= 0:
        return head

    # 1. Find the length and the tail of the list
    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1

    # 2. Normalize k (if k is a multiple of length, the list doesn't change)
    k %= length
    if k == 0:
        return head

    # 3. Connect tail to head to form a circle
    tail.next = head

    # 4. Find the new tail, which is at position (length - k)
    # We walk (length - k - 1) steps from the head to land exactly on the new tail
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    # 5. The new head is right after the new tail
    new_head = new_tail.next
    
    # 6. Break the circle
    new_tail.next = None

    return new_head

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
    # Expected: 4 -> 5 -> 1 -> 2 -> 3
    head1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    res1 = rotate_linked_list(head1, 2)
    assert get_list_values(res1) == [4, 5, 1, 2, 3], f"Test 1 failed: {get_list_values(res1)}"

    # 🔲 Edge cases
    # k = 7, length = 5 (effective k = 2)
    head2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    res2 = rotate_linked_list(head2, 7)
    assert get_list_values(res2) == [4, 5, 1, 2, 3], "Edge 1 failed (k > length)"

    # k = 5, length = 5 (effective k = 0)
    head3 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    res3 = rotate_linked_list(head3, 5)
    assert get_list_values(res3) == [1, 2, 3, 4, 5], "Edge 2 failed (k == length)"

    print("All tests passed!")
