"""
============================================================
Problem: Doubly Linked List Implementation
Pattern: Data Structures (Fundamentals)
Difficulty: Medium
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A Doubly Linked List is like a regular Linked List, but every friend holding
hands now looks at BOTH the person in front of them AND the person behind them!
This means you can walk forward down the line, but you can also walk BACKWARDS.
Because every node knows who is before it, deleting a node at the very end
(the tail) becomes super easy, because the tail just points backward to the
new tail!

APPROACH: High-Performance Modern Python 3.14
---------
- We use `__slots__ = ("val", "next", "prev")` for the `Node` to save memory.
- We use PEP 695 Type Parameters (`class Node[T]:`) for clean Generics.
- We maintain explicit `_head`, `_tail`, and `_size` properties.
- Deleting nodes becomes O(1) if you ALREADY have the node reference (unlike 
  Singly Linked Lists where you'd have to traverse from the head to find the 'prev').
  Deleting by value still takes O(N) to find the value.

COMPLEXITY:
-----------
Time:  
  - Append/Prepend/Head/Tail: O(1)
  - Search/Insert/Delete by Value/Reverse: O(N)
  - Delete by Node Reference: O(1)
Space: O(N) for storing N nodes.
============================================================
"""

from typing import Optional, Any
import collections.abc

class Node[T]:
    """
    A single node in a Doubly Linked List.
    __slots__ prevents dynamic dictionary creation for extreme memory efficiency.
    """
    __slots__ = ("val", "next", "prev")

    def __init__(self, val: T, next_node: Optional['Node[T]'] = None, prev_node: Optional['Node[T]'] = None):
        self.val = val
        self.next = next_node
        self.prev = prev_node

    def __repr__(self) -> str:
        return f"Node({self.val})"


class DoublyLinkedList[T]:
    """
    A highly optimized Doubly Linked List.
    Tracks head, tail, and size.
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
        """Enables forward traversal."""
        curr = self._head
        while curr:
            yield curr.val
            curr = curr.next

    def __reversed__(self) -> collections.abc.Iterator[T]:
        """Enables backward traversal: 'for item in reversed(my_list):'"""
        curr = self._tail
        while curr:
            yield curr.val
            curr = curr.prev

    def __repr__(self) -> str:
        """Enables clean printing: 'DLL[1 <-> 2 <-> 3]'"""
        values = " <-> ".join(str(val) for val in self)
        return f"DLL[{values}]"

    def append(self, val: T) -> 'DoublyLinkedList[T]':
        """Adds a node to the END of the list in O(1) time."""
        new_node = Node(val, prev_node=self._tail)
        if self.is_empty:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1
        return self

    def prepend(self, val: T) -> 'DoublyLinkedList[T]':
        """Adds a node to the FRONT of the list in O(1) time."""
        new_node = Node(val, next_node=self._head)
        if self.is_empty:
            self._head = self._tail = new_node
        else:
            self._head.prev = new_node
            self._head = new_node
        self._size += 1
        return self

    def insert_at(self, index: int, val: T) -> 'DoublyLinkedList[T]':
        """Inserts a node at a specific index in O(N) time."""
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        match index:
            case 0:
                return self.prepend(val)
            case idx if idx == self._size:
                return self.append(val)
            case _:
                # Optimize traversal: choose forward or backward based on index!
                if index < self._size // 2:
                    curr = self._head
                    for _ in range(index):
                        curr = curr.next
                else:
                    curr = self._tail
                    for _ in range(self._size - 1, index, -1):
                        curr = curr.prev
                
                # 'curr' is now the node that currently occupies the insertion index.
                # We want to insert 'new_node' right BEFORE 'curr'.
                prev_node = curr.prev
                new_node = Node(val, next_node=curr, prev_node=prev_node)
                
                if prev_node:
                    prev_node.next = new_node
                curr.prev = new_node
                
                self._size += 1
                return self

    def _remove_node(self, node: Node[T]) -> None:
        """Helper to remove a node directly in O(1) time if reference is known."""
        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next  # It was the head
            
        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = node.prev  # It was the tail
            
        self._size -= 1

    def delete(self, val: T) -> bool:
        """Deletes the FIRST occurrence of a value. O(N) time."""
        curr = self._head
        while curr:
            if curr.val == val:
                self._remove_node(curr)
                return True
            curr = curr.next
        return False

    def search(self, val: T) -> bool:
        """Searches for a value in the list. O(N) time."""
        return any(curr_val == val for curr_val in self)

    def reverse(self) -> 'DoublyLinkedList[T]':
        """Reverses the linked list in-place in O(N) time."""
        curr = self._head
        self._tail = self._head  # The old head becomes the new tail

        prev_node = None
        while curr:
            # Swap next and prev pointers
            next_node = curr.next
            curr.next = curr.prev
            curr.prev = next_node
            
            prev_node = curr
            curr = next_node  # Move to what was originally the next node

        self._head = prev_node  # The old tail becomes the new head
        return self


if __name__ == "__main__":
    print("Testing highly optimized Python 3.14 DoublyLinkedList...")
    
    # 1. Initialization and Appending
    dll: DoublyLinkedList[int] = DoublyLinkedList()
    dll.append(1).append(2).append(3)
    
    assert len(dll) == 3
    assert dll.head.val == 1
    assert dll.tail.val == 3
    assert str(dll) == "DLL[1 <-> 2 <-> 3]"
    print("✅ Append & Initialization passed!")

    # 2. Prepending
    dll.prepend(0)
    assert len(dll) == 4
    assert dll.head.val == 0
    assert str(dll) == "DLL[0 <-> 1 <-> 2 <-> 3]"
    print("✅ Prepend passed!")

    # 3. Insertion (Testing half-way optimized traversal)
    # Size is 4. Inserting at index 3 means it'll traverse from the tail!
    dll.insert_at(3, 99)
    assert str(dll) == "DLL[0 <-> 1 <-> 2 <-> 99 <-> 3]"
    assert len(dll) == 5
    print("✅ Insert passed!")

    # 4. Backward Traversal (Testing __reversed__)
    backward = list(reversed(dll))
    assert backward == [3, 99, 2, 1, 0]
    print("✅ Reversed traversal passed!")

    # 5. Deletion
    # Delete from middle
    dll.delete(99)
    assert str(dll) == "DLL[0 <-> 1 <-> 2 <-> 3]"
    # Delete head
    dll.delete(0)
    assert str(dll) == "DLL[1 <-> 2 <-> 3]"
    assert dll.head.val == 1
    # Delete tail
    dll.delete(3)
    assert str(dll) == "DLL[1 <-> 2]"
    assert dll.tail.val == 2
    assert len(dll) == 2
    print("✅ Delete passed!")

    # 6. Reversal
    dll.append(3).append(4)
    assert str(dll) == "DLL[1 <-> 2 <-> 3 <-> 4]"
    dll.reverse()
    assert str(dll) == "DLL[4 <-> 3 <-> 2 <-> 1]"
    assert dll.head.val == 4
    assert dll.tail.val == 1
    print("✅ Reverse in-place passed!")
    
    print("🎉 All DoublyLinkedList tests passed successfully!")
