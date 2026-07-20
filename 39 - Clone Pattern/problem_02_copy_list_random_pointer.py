"""
============================================================
Problem: Copy List with Random Pointer
Pattern: Clone Pattern (Weaving Trick)
Difficulty:
Link: https://leetcode.com/problem-placeholder/ Medium
LeetCode: #138
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a Linked List where each node has a `next` pointer AND a `random` pointer
that can point to ANY node in the list (or None). Make a deep copy.
We could use a Hash Map (O(N) space), but there is a brilliant trick to do it
in O(1) extra space!

APPROACH: Weaving / Interleaving Nodes
---------
1. **Weave**: For each node, create a copy and insert it DIRECTLY AFTER the original node.
   `A -> A' -> B -> B' -> C -> C'`
2. **Link Randoms**: Now, the cloned node's random pointer is just the original
   node's random pointer's NEXT node!
   `curr.next.random = curr.random.next` (if `curr.random` exists).
3. **Unweave**: Separate the mixed list back into two distinct lists: the original
   and the fully cloned list.

COMPLEXITY:
-----------
Time:  O(N) — 3 passes.
Space: O(1) — No Hash Map used!

EDGE CASES:
-----------
- Basic empty/null edge cases.
- Boundary constraints.
============================================================
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: 'Node') -> 'Node':
    if not head:
        return None
        
    # Step 1: Weave the cloned nodes into the original list
    curr = head
    while curr:
        clone = Node(curr.val, curr.next, None)
        curr.next = clone
        curr = clone.next
        
    # Step 2: Assign random pointers for the cloned nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
        
    # Step 3: Unweave the lists to restore original and extract the clone
    curr = head
    clone_head = head.next
    
    while curr:
        clone = curr.next
        curr.next = clone.next
        if clone.next:
            clone.next = clone.next.next
        curr = curr.next
        
    return clone_head


if __name__ == "__main__":
    # Create List: A(7) -> B(13) -> C(11) -> D(10) -> E(1)
    nodeA = Node(7)
    nodeB = Node(13)
    nodeC = Node(11)
    nodeD = Node(10)
    nodeE = Node(1)
    
    nodeA.next, nodeA.random = nodeB, None
    nodeB.next, nodeB.random = nodeC, nodeA
    nodeC.next, nodeC.random = nodeD, nodeE
    nodeD.next, nodeD.random = nodeE, nodeC
    nodeE.next, nodeE.random = None, nodeA
    
    clonedA = copy_random_list(nodeA)
    
    assert clonedA is not nodeA, "Must be a deep copy"
    assert clonedA.val == 7
    assert clonedA.next.val == 13
    assert clonedA.next.random.val == 7, "B' random should point to A'"
    assert clonedA.next.random is clonedA, "B' random should point exactly to cloned A, not original A"
    
    print("All tests passed!")
