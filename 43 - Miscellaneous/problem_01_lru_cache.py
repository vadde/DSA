"""
============================================================
Problem: LRU Cache
Pattern: Hash Map + Doubly Linked List
Difficulty: Medium
LeetCode: #146
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Design a cache with a maximum capacity.
When you `put` a new item and the cache is full, you must throw away the item
that hasn't been used in the longest amount of time (Least Recently Used).
`get` and `put` must both be O(1) time!

APPROACH: Hash Map + Doubly Linked List
---------
1. **Hash Map**: Stores `key: Node`. Gives O(1) access to any node.
2. **Doubly Linked List**: Keeps nodes in order of recency.
   - `Head` (dummy): Most recently used items go right after the head.
   - `Tail` (dummy): Least recently used items fall down to right before the tail.
3. **Operations**:
   - `get(key)`: If it exists, move the node to the front (right after Head). Return value.
   - `put(key, val)`: If it exists, update value and move to front. 
     If new, create node, add to front, and add to map. If capacity exceeded, 
     remove the node right before the Tail from both the list and the map!

COMPLEXITY:
-----------
Time:  O(1) for all operations.
Space: O(Capacity)
============================================================
"""

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # map key to node
        
        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the linked list."""
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node: Node):
        """Add a node right after the dummy head (Most Recently Used)."""
        p = self.head
        n = self.head.next
        p.next = node
        node.prev = p
        node.next = n
        n.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to front (Most Recently Used)
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            # Remove the Least Recently Used (node right before tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1) # cache is {1=1}
    lRUCache.put(2, 2) # cache is {1=1, 2=2}
    assert lRUCache.get(1) == 1, "Test 1" # return 1
    lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert lRUCache.get(2) == -1, "Test 2" # returns -1 (not found)
    lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert lRUCache.get(1) == -1, "Test 3" # return -1 (not found)
    assert lRUCache.get(3) == 3, "Test 4"  # return 3
    assert lRUCache.get(4) == 4, "Test 5"  # return 4
    print("All tests passed!")
