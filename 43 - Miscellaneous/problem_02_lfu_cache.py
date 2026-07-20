"""
============================================================
Problem: LFU Cache
Pattern: Hash Maps + Doubly Linked Lists
Difficulty:
Link: https://leetcode.com/problem-placeholder/ Hard
LeetCode: #460
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Like LRU cache, but when it's full, you throw away the item that was used
the LEAST FREQUENTLY (fewest number of times).
If there is a tie (multiple items used the same fewest number of times),
THEN you throw away the Least Recently Used among them.

APPROACH: Two Hash Maps
---------
1. `key_to_node`: Maps `key` to `Node(key, val, freq)`.
2. `freq_to_list`: Maps `frequency` to a `DoublyLinkedList`.
   This is the genius part: Every frequency has its OWN LRU cache!
3. `min_freq`: An integer keeping track of the current lowest frequency in the cache.
   When the cache is full, we look at `freq_to_list[min_freq]` and pop its LRU tail!

COMPLEXITY:
-----------
Time:  O(1) for all operations.
Space: O(Capacity)

EDGE CASES:
-----------
- Basic empty/null edge cases.
- Boundary constraints.
============================================================
"""

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def add(self, node: Node):
        p = self.head
        n = self.head.next
        p.next = node
        node.prev = p
        node.next = n
        n.prev = node
        self.size += 1
        
    def remove(self, node: Node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        self.size -= 1
        
    def pop_tail(self) -> Node:
        if self.size == 0:
            return None
        lru = self.tail.prev
        self.remove(lru)
        return lru


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_node = {} # key -> Node
        import collections
        self.freq_list = collections.defaultdict(DoublyLinkedList) # freq -> DLL

    def _update_freq(self, node: Node):
        """Moves a node from its current frequency list to the freq+1 list."""
        freq = node.freq
        self.freq_list[freq].remove(node)
        
        # If the list we just removed from was the min_freq list and is now empty,
        # we must increment min_freq!
        if self.min_freq == freq and self.freq_list[freq].size == 0:
            self.min_freq += 1
            
        node.freq += 1
        self.freq_list[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self._update_freq(node)
            return
            
        if len(self.key_node) >= self.capacity:
            # Evict LFU (and LRU if tied)
            lru_list = self.freq_list[self.min_freq]
            evicted_node = lru_list.pop_tail()
            del self.key_node[evicted_node.key]
            
        # Create new node
        new_node = Node(key, value)
        self.key_node[key] = new_node
        self.min_freq = 1
        self.freq_list[1].add(new_node)


if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
    lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
    assert lfu.get(1) == 1, "Test 1"      # return 1, cache=[1,2], cnt(1)=2, cnt(2)=1
    lfu.put(3, 3)   # 2 is the LFU key because cnt(2)=1 is the min, evict 2. cache=[3,1]
    assert lfu.get(2) == -1, "Test 2"     # return -1 (not found)
    assert lfu.get(3) == 3, "Test 3"      # return 3, cache=[3,1], cnt(3)=2, cnt(1)=2
    lfu.put(4, 4)   # Both 1 and 3 have cnt=2, but 1 is LRU, evict 1. cache=[4,3]
    assert lfu.get(1) == -1, "Test 4"     # return -1 (not found)
    assert lfu.get(3) == 3, "Test 5"      # return 3
    assert lfu.get(4) == 4, "Test 6"      # return 4
    print("All tests passed!")
