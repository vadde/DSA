"""
============================================================
Problem: Merge K Sorted Lists
Pattern: K-way Merge
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cdea00cc465d6c827b5
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have 3 chains of paperclips. Each chain is sorted by size.
You want to combine all 3 chains into ONE giant chain that is also sorted by size.
Since the chains are already sorted, the smallest paperclip in the ENTIRE world 
MUST be at the very front of one of the 3 chains!
So, you just look at the 3 front paperclips. You pick the smallest one, take 
it off its chain, and put it on your new giant chain.
When you take it off, the next paperclip in that chain becomes the new front!
You repeat this, always looking at the front of the 3 chains, picking the smallest.
To make finding the smallest super fast, we use a **Min-Heap**!
The Min-Heap will hold exactly 3 paperclips (the fronts of the 3 chains).
When we pull one out, we look at the chain it came from, grab the next paperclip, 
and throw it into the Min-Heap!

APPROACH:
---------
1. Put the head node of each of the `K` LinkedLists into a `min_heap`.
   - Python's `heapq` sorts tuples by the first element. If there's a tie, it 
     checks the second. If we push `(node.value, node)`, Python will crash if 
     values tie because it doesn't know how to compare two `Node` objects!
   - We must push a tie-breaker: `(node.value, index, node)`, where `index` is 
     the index of the list it came from.
2. Initialize `result_head` and `result_tail` to `None`.
3. Loop while `min_heap` is not empty:
   - Pop the smallest node: `value, i, node = heappop(min_heap)`.
   - Append `node` to the result list (using `result_head` and `result_tail`).
   - If `node.next` exists, push it into the heap! `(node.next.value, i, node.next)`.
4. Return `result_head`.

COMPLEXITY:
-----------
Time:  O(N * log K) — N is total number of nodes. Heap never grows larger than K.
Space: O(K) — For the heap.

EDGE CASES:
-----------
- Edge case 1: Some or all lists are empty. We only push heads that are not None.
============================================================
"""

import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges K sorted linked lists into one sorted linked list.
    """
    min_heap = []
    
    # 1. Put the root of each list into the Min-Heap
    for i, root in enumerate(lists):
        if root is not None:
            # We push (value, array_index, node) to avoid Python crashing on ties
            heapq.heappush(min_heap, (root.value, i, root))
            
    result_head = None
    result_tail = None
    
    # 2. Keep popping the smallest node and advancing its list
    while min_heap:
        value, i, node = heapq.heappop(min_heap)
        
        # Append the popped node to the result list
        if result_head is None:
            result_head = node
            result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next
            
        # 3. If the list this node came from has more nodes, push the next one!
        if node.next is not None:
            heapq.heappush(min_heap, (node.next.value, i, node.next))
            
    return result_head

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    def create_linked_list(arr):
        if not arr: return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head
        
    def linked_list_to_list(head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.value)
            curr = curr.next
        return arr

    # ✅ Normal cases
    l1 = create_linked_list([2, 6, 8])
    l2 = create_linked_list([3, 6, 7])
    l3 = create_linked_list([1, 3, 4])
    
    merged_head = merge_lists([l1, l2, l3])
    assert linked_list_to_list(merged_head) == [1, 2, 3, 3, 4, 6, 6, 7, 8], "Test 1"

    # 🔲 Edge cases
    assert linked_list_to_list(merge_lists([])) == [], "Edge 1: Empty input list"
    assert linked_list_to_list(merge_lists([None, None])) == [], "Edge 2: Lists of Nones"

    print("All tests passed!")
