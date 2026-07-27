"""
============================================================
Problem: Singly Linked List Implementation
Pattern: Data Structures (Fundamentals)
Difficulty: Medium
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A Linked List is like a treasure hunt. You get a clue (the head), which tells
you where the first treasure is, and also gives you a map to the next treasure.
Unlike arrays (like a carton of eggs where everything is perfectly lined up in 
memory), Linked List items can be anywhere in memory, but they "link" to each other!

APPROACH: High-Performance Modern Python 3.14
---------
- We use `__slots__` for `Node` to avoid the memory overhead of `__dict__`.
- We use PEP 695 Type Parameters (`class Node[T]:`) for clean Generics.
- We maintain a `_tail` pointer and `_size` tracker to make `append()` and `len()` O(1).
- We use `@property` for getter methods like `head` and `tail` to prevent 
  external modification of internal pointers.
- We implement standard Python magic methods (`__len__`, `__iter__`, `__repr__`)
  so the LinkedList acts just like a native Python list!

COMPLEXITY:
-----------
Time:  
  - Append/Prepend/Head/Tail: O(1)
  - Search/Insert/Delete/Reverse: O(N)
Space: O(N) for storing N nodes.
============================================================
"""

from typing import Optional, Any
import collections.abc

class Node[T]:
    """
    A single node in the Linked List.
    Using __slots__ prevents dynamic dictionary creation, saving ~65% memory per node!
    """
    __slots__ = ("val", "next")

    def __init__(self, val: T, next_node: Optional['Node[T]'] = None):
        self.val = val
        self.next = next_node

    def __repr__(self) -> str:
        return f"Node({self.val})"


class LinkedList[T]:
    """
    A highly optimized Singly Linked List.
    Tracks head, tail, and size for maximum efficiency.
    """
    __slots__ = ("_head", "_tail", "_size")

    def __init__(self):
        self._head: Optional[Node[T]] = None
        self._tail: Optional[Node[T]] = None
        self._size: int = 0

    @property
    def is_empty(self) -> bool:
        return self._size == 0

    @property
    def head(self) -> Optional[Node[T]]:
        return self._head

    @property
    def tail(self) -> Optional[Node[T]]:
        return self._tail

    def __len__(self) -> int:
        """Enables len(my_list) in O(1) time."""
        return self._size

    def __iter__(self) -> collections.abc.Iterator[T]:
        """Enables for loop traversal: 'for item in my_list:'"""
        curr = self._head
        while curr:
            yield curr.val
            curr = curr.next

    def __repr__(self) -> str:
        """Enables clean printing: 'LinkedList[1 -> 2 -> 3]'"""
        values = " -> ".join(str(val) for val in self)
        return f"LinkedList[{values}]"

    def append(self, val: T) -> 'LinkedList[T]':
        """Adds a node to the END of the list in O(1) time."""
        new_node = Node(val)
        if self.is_empty:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1
        return self  # Return self for method chaining

    def prepend(self, val: T) -> 'LinkedList[T]':
        """Adds a node to the FRONT of the list in O(1) time."""
        new_node = Node(val, self._head)
        self._head = new_node
        if self.is_empty:
            self._tail = new_node
        self._size += 1
        return self

    def insert_at(self, index: int, val: T) -> 'LinkedList[T]':
        """Inserts a node at a specific index in O(N) time."""
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        match index:
            case 0:
                return self.prepend(val)
            case idx if idx == self._size:
                return self.append(val)
            case _:
                # Traverse to the node JUST BEFORE the insertion point
                curr = self._head
                for _ in range(index - 1):
                    curr = curr.next
                
                new_node = Node(val, curr.next)
                curr.next = new_node
                self._size += 1
                return self

    def delete(self, val: T) -> bool:
        """Deletes the FIRST occurrence of a value. Returns True if deleted, else False. O(N) time."""
        if self.is_empty:
            return False

        if self._head.val == val:
            self._head = self._head.next
            self._size -= 1
            if self.is_empty:
                self._tail = None
            return True

        curr = self._head
        while curr.next:
            if curr.next.val == val:
                if curr.next == self._tail:
                    self._tail = curr  # Update tail if deleting the last node
                curr.next = curr.next.next
                self._size -= 1
                return True
            curr = curr.next

        return False

    def search(self, val: T) -> bool:
        """Searches for a value in the list. O(N) time."""
        return any(curr_val == val for curr_val in self)

    def reverse(self) -> 'LinkedList[T]':
        """Reverses the linked list in-place in O(N) time."""
        prev = None
        curr = self._head
        self._tail = self._head  # The old head becomes the new tail

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self._head = prev  # The old tail becomes the new head
        return self


if __name__ == "__main__":
    print("Testing highly optimized Python 3.14 LinkedList...")
    
    # 1. Initialization and Appending (Testing Generics and Method Chaining)
    ll: LinkedList[int] = LinkedList()
    ll.append(1).append(2).append(3)
    
    assert len(ll) == 3
    assert ll.head.val == 1
    assert ll.tail.val == 3
    assert str(ll) == "LinkedList[1 -> 2 -> 3]"
    print("✅ Append & Initialization passed!")

    # 2. Prepending
    ll.prepend(0)
    assert len(ll) == 4
    assert ll.head.val == 0
    assert str(ll) == "LinkedList[0 -> 1 -> 2 -> 3]"
    print("✅ Prepend passed!")

    # 3. Insertion (Testing Pattern Matching logic)
    ll.insert_at(2, 99)
    assert str(ll) == "LinkedList[0 -> 1 -> 99 -> 2 -> 3]"
    assert len(ll) == 5
    print("✅ Insert passed!")

    # 4. Deletion
    # Delete middle
    deleted = ll.delete(99)
    assert deleted is True
    assert str(ll) == "LinkedList[0 -> 1 -> 2 -> 3]"
    
    # Delete head
    ll.delete(0)
    assert str(ll) == "LinkedList[1 -> 2 -> 3]"
    assert ll.head.val == 1
    
    # Delete tail
    ll.delete(3)
    assert str(ll) == "LinkedList[1 -> 2]"
    assert ll.tail.val == 2
    assert len(ll) == 2
    print("✅ Delete passed!")

    # 5. Searching (Testing __iter__)
    assert ll.search(2) is True
    assert ll.search(99) is False
    print("✅ Search passed!")

    # 6. Reversal
    ll.append(3).append(4)
    assert str(ll) == "LinkedList[1 -> 2 -> 3 -> 4]"
    ll.reverse()
    assert str(ll) == "LinkedList[4 -> 3 -> 2 -> 1]"
    assert ll.head.val == 4
    assert ll.tail.val == 1
    print("✅ Reverse passed!")
    
    print("🎉 All LinkedList tests passed successfully!")
