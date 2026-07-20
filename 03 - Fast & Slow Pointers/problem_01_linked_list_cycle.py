"""
============================================================
Problem: LinkedList Cycle
Pattern: Fast & Slow Pointers
Difficulty: Easy
Link: https://leetcode.com/problems/linked-list-cycle/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you are walking down a path made of stepping stones. You want to know 
if the path is a straight line that eventually ends, or if it loops around in a 
circle forever.
If you just keep walking, you might walk forever if there's a loop! You need a 
smarter way to check.
Send two friends down the path: a Slow Tortoise and a Fast Hare. 
The Tortoise takes 1 step at a time. The Hare takes 2 steps at a time.
If the path has an end, the Hare will just reach the end first.
But if the path is a circle, they will both end up running in circles. Because 
the Hare is faster, he will eventually run all the way around and lap the Tortoise!
If they ever land on the exact same stone at the same time, you know for sure 
there is a loop!

APPROACH:
---------
1. Initialize two pointers, `slow` and `fast`, pointing to the `head` of the LinkedList.
2. Loop while `fast` is not `None` and `fast.next` is not `None`.
   - `slow` moves one step: `slow = slow.next`
   - `fast` moves two steps: `fast = fast.next.next`
3. If at any point `slow == fast`, a cycle is detected, return `True`.
4. If the loop ends naturally (meaning `fast` hit the end of the list), return `False`.

COMPLEXITY:
-----------
Time:  O(N) — In the worst case (a cycle), the fast pointer will catch the slow pointer in at most N steps.
Space: O(1) — We only use two pointers.

EDGE CASES:
-----------
- Edge case 1: Empty LinkedList (`head` is None). Loop condition fails immediately, returns `False`.
- Edge case 2: Single node without a cycle. Returns `False`.
- Edge case 3: Single node with a cycle (pointing to itself). Handled correctly, returns `True`.
============================================================
"""

from typing import Optional

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head: Optional[Node]) -> bool:
    """
    Given the head of a Singly LinkedList, determine if the LinkedList 
    has a cycle in it or not.
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps
        
        if slow == fast:
            return True           # Cycle found

    return False

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next # Cycle to Node 3
    assert has_cycle(head) == True, "Test 1 failed"

    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(3) # No cycle
    assert has_cycle(head2) == False, "Test 2 failed"
    
    # 🔲 Edge cases
    assert has_cycle(None) == False, "Edge 1: Empty list"
    
    head3 = Node(1) # Single node no cycle
    assert has_cycle(head3) == False, "Edge 2: Single node no cycle"
    
    head4 = Node(1)
    head4.next = head4 # Single node with cycle
    assert has_cycle(head4) == True, "Edge 3: Single node with cycle"

    print("All tests passed!")
