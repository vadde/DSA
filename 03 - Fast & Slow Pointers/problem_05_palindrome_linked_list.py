"""
============================================================
Problem: Palindrome LinkedList
Pattern: Fast & Slow Pointers
Difficulty: Medium
Link: https://leetcode.com/problems/palindrome-linked-list/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A palindrome is a word that is spelled the same forwards and backwards (like 
RACECAR or 1-2-3-2-1).
If you have a LinkedList, you can't easily read it backwards because the arrows 
only point forward!
So, how do we compare the front to the back? 
1. We use our Tortoise and Hare to find the EXACT MIDDLE of the list.
2. We take the entire second half of the list and manually turn all the arrows 
   around (Reverse it).
3. Now we have two lists starting from the outside and pointing inward. We just 
   walk down both of them step by step. If they match completely, it's a palindrome!
4. (Bonus points: we reverse the second half back to normal so we don't break 
   the original list permanently).

APPROACH:
---------
1. Initialize `slow` and `fast` pointers at the head to find the middle.
2. When `fast` reaches the end, `slow` is at the middle.
3. Call a helper function `reverse(node)` to reverse the second half starting at `slow`. 
   Let `head_second_half` be the new head of the reversed second half.
4. Set `copy_head_second_half = head_second_half` (so we can restore it later).
5. Compare `head` and `head_second_half`:
   - `while head is not None and head_second_half is not None`:
     - If their values don't match, break early (it's not a palindrome).
6. Restore the second half: `reverse(copy_head_second_half)`.
7. Return whether it was a palindrome or not.

COMPLEXITY:
-----------
Time:  O(N) — Finding the middle is O(N/2), reversing is O(N/2), comparing is O(N/2). Total O(N).
Space: O(1) — Reversing is done in place by just changing pointers. No extra memory used.

EDGE CASES:
-----------
- Edge case 1: Single node. It's a palindrome.
- Edge case 2: Two nodes (`[1, 1]` or `[1, 2]`).
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

def is_palindrome(head: Optional[Node]) -> bool:
    """
    Checks if a Singly LinkedList is a palindrome.
    Restores the LinkedList back to its original state before returning.
    """
    if head is None or head.next is None:
        return True

    # 1. Find the middle of the LinkedList
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse the second half
    head_second_half = reverse_linked_list(slow)
    copy_head_second_half = head_second_half

    # 3. Compare the first and the second half
    curr_first_half = head
    curr_second_half = head_second_half
    
    is_palin = True
    while curr_first_half is not None and curr_second_half is not None:
        if curr_first_half.value != curr_second_half.value:
            is_palin = False
            break
        curr_first_half = curr_first_half.next
        curr_second_half = curr_second_half.next

    # 4. Restore the reversed second half
    reverse_linked_list(copy_head_second_half)

    return is_palin

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
    head1 = Node(2, Node(4, Node(6, Node(4, Node(2)))))
    assert is_palindrome(head1) == True, "Test 1 failed"
    # Verify the list wasn't permanently mutated
    assert get_list_values(head1) == [2, 4, 6, 4, 2], "Test 1 mutation failed"

    head2 = Node(2, Node(4, Node(6, Node(4, Node(2, Node(2))))))
    assert is_palindrome(head2) == False, "Test 2 failed"
    
    # 🔲 Edge cases
    head3 = Node(2, Node(2))
    assert is_palindrome(head3) == True, "Edge 1: Even length true"
    
    head4 = Node(1)
    assert is_palindrome(head4) == True, "Edge 2: Single node"

    print("All tests passed!")
