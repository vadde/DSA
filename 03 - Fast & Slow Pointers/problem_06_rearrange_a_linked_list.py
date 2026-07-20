"""
============================================================
Problem: Rearrange a LinkedList
Pattern: Fast & Slow Pointers (Middle + In-Place Reversal)
Difficulty: Medium
Link: https://leetcode.com/problems/reorder-list/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a long line of dominoes numbered 1, 2, 3, 4, 5, 6.
You want to reorganize them into a very specific pattern: 
1st Domino, LAST Domino, 2nd Domino, SECOND-TO-LAST Domino, and so on...
So it becomes 1, 6, 2, 5, 3, 4.

If we just had a regular array, this would be easy. But with a LinkedList, we can 
only move forward! How do we grab the "last" one easily?
We can split the problem into three simple steps:
1. Find the MIDDLE of the LinkedList (using Fast & Slow pointers).
2. Take the entire second half and REVERSE it (so it now points backwards).
3. Now we have two lists starting from opposite ends. We simply take turns picking 
   one domino from the first list, then one from the second list, weaving them 
   together like a zipper!

APPROACH:
---------
1. Find the middle of the LinkedList using `slow` and `fast` pointers.
2. Call a helper function `reverse(node)` starting from `slow`. Let the returned 
   node be `second_half`.
3. Let `first_half` be the original `head`.
4. While `first_half is not None` and `second_half is not None`:
   a. Save the next pointers (`temp = first_half.next`).
   b. Point the current `first_half` node to the current `second_half` node.
   c. Move `first_half` forward (`first_half = temp`).
   
   d. Save the next pointers (`temp = second_half.next`).
   e. Point the current `second_half` node to the new `first_half` node.
   f. Move `second_half` forward (`second_half = temp`).
5. Important: The last node processed will naturally point to `None` because the 
   reversal algorithm sets the tail's next to `None`.
6. Note: To prevent a cycle, before we reverse, we might want to sever the connection 
   between the first half and the second half, OR we can rely on the reversal logic. 
   Actually, `reverse(slow)` makes the node at `slow` point to `None`. But the node 
   JUST BEFORE `slow` (the end of the first half) still points to `slow`. 
   To be perfectly safe and prevent a cycle, we should set `slow_prev.next = None` 
   or handle it during the weaving. If we weave until `first_half` or `second_half` is `None`, 
   and set `curr_first.next = None` if `curr_first` exists at the end, that breaks any cycles.
   Let's ensure the tail always points to `None` by doing `if first_half: first_half.next = None`.

COMPLEXITY:
-----------
Time:  O(N) — Finding middle O(N/2), Reversing O(N/2), Weaving O(N/2). Total O(N).
Space: O(1) — Done completely in-place.

EDGE CASES:
-----------
- Edge case 1: List with 1 or 2 nodes. Requires no rearranging.
- Edge case 2: Odd vs Even lengths.
============================================================
"""

from typing import Optional

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head: Optional[Node]) -> Optional[Node]:
    """
    Reverses a Singly LinkedList in-place and returns the new head.
    """
    prev: Optional[Node] = None
    curr: Optional[Node] = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def reorder_list(head: Optional[Node]) -> None:
    """
    Modifies the LinkedList in-place by weaving the first half 
    with the reversed second half.
    """
    if head is None or head.next is None:
        return

    # 1. Find the middle
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse the second half
    # slow is now at the middle.
    second_half = reverse_linked_list(slow)
    first_half = head

    # 3. Weave the two halves together
    while first_half is not None and second_half is not None:
        # We don't want to weave a node onto itself (middle node in odd lengths)
        if first_half == second_half:
            break
            
        temp_first = first_half.next
        temp_second = second_half.next

        # Link first to second
        first_half.next = second_half
        # Link second to the rest of the first
        second_half.next = temp_first

        first_half = temp_first
        second_half = temp_second

    # Ensure the last node points to None to prevent cycles
    if first_half is not None:
        first_half.next = None


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

    # ✅ Normal cases (Even length)
    head1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    reorder_list(head1)
    assert get_list_values(head1) == [1, 6, 2, 5, 3, 4], f"Test 1 failed: {get_list_values(head1)}"

    # ✅ Normal cases (Odd length)
    head2 = Node(2, Node(4, Node(6, Node(8, Node(10)))))
    reorder_list(head2)
    assert get_list_values(head2) == [2, 10, 4, 8, 6], f"Test 2 failed: {get_list_values(head2)}"
    
    # 🔲 Edge cases
    head3 = Node(1)
    reorder_list(head3)
    assert get_list_values(head3) == [1], "Edge 1: Single node"
    
    head4 = Node(1, Node(2))
    reorder_list(head4)
    assert get_list_values(head4) == [1, 2], "Edge 2: Two nodes"

    print("All tests passed!")
