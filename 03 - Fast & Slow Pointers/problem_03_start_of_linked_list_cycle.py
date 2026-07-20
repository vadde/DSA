"""
============================================================
Problem: Start of LinkedList Cycle
Pattern: Fast & Slow Pointers (Floyd's Cycle-Finding Phase 2)
Difficulty: Medium
Link: https://leetcode.com/problems/linked-list-cycle-ii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine our Slow Tortoise and Fast Hare are running on a track that has a straight 
path leading into a circle. We know they will eventually crash into each other 
inside the circle. But we want to know EXACTLY where the circle begins!
Through some really cool math, we know that the distance from the very start of 
the track to the start of the circle is EXACTLY THE SAME as the distance from 
their crash site to the start of the circle!
So, once they crash, we leave the Tortoise at the crash site. We pick up the Hare 
and put him all the way back at the start line. 
Now, they BOTH run at the EXACT SAME speed (1 step at a time). The exact spot 
where they meet again is the start of the circle!

APPROACH:
---------
1. Phase 1 (Detect Cycle):
   - `slow = head`, `fast = head`.
   - `slow` moves 1 step, `fast` moves 2 steps.
   - If they meet (`slow == fast`), we have a cycle. Break out of the loop.
   - If `fast` or `fast.next` becomes `None`, there is no cycle. Return `None`.
2. Phase 2 (Find Start):
   - Move ONE of the pointers (let's say `fast`) back to the `head`.
   - Now, move BOTH pointers at 1 step at a time (`slow = slow.next`, `fast = fast.next`).
   - The node where they meet (`slow == fast`) is the start of the cycle.
3. Return that node.

COMPLEXITY:
-----------
Time:  O(N) — Phase 1 takes at most N steps. Phase 2 takes at most N steps. Total is O(N).
Space: O(1) — We just use pointer references.

EDGE CASES:
-----------
- Edge case 1: No cycle exists. Returns `None`.
- Edge case 2: Cycle starts at the very first node (`head`). Phase 2 immediately succeeds at step 0.
============================================================
"""

from typing import Optional

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_cycle_start(head: Optional[Node]) -> Optional[Node]:
    """
    Finds the starting node of a cycle in a Singly LinkedList.
    Returns None if no cycle exists.
    """
    slow = head
    fast = head
    has_cycle = False

    # Phase 1: Detect Cycle
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            has_cycle = True
            break

    # If there's no cycle, return None
    if not has_cycle:
        return None

    # Phase 2: Find the start of the cycle
    # Reset one pointer to the head, leave the other at the meeting point
    fast = head
    
    while slow != fast:
        # Move both at the same speed!
        slow = slow.next
        fast = fast.next
        
    return slow

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    
    # Create a cycle: 6 points back to 3
    head1.next.next.next.next.next.next = head1.next.next 
    
    cycle_start = find_cycle_start(head1)
    assert cycle_start is not None and cycle_start.value == 3, "Test 1 failed"

    # ✅ Normal cases (Cycle at head)
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = head2
    
    assert find_cycle_start(head2).value == 1, "Test 2 failed: Cycle at head"
    
    # 🔲 Edge cases
    head3 = Node(1, Node(2, Node(3))) # No cycle
    assert find_cycle_start(head3) is None, "Edge 1: No cycle"
    assert find_cycle_start(None) is None, "Edge 2: Empty list"

    print("All tests passed!")
