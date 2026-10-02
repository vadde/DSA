"""
============================================================
Problem: Circular Linked List Implementation
Pattern: Data Structures (Fundamentals)
Difficulty: Medium
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a group of friends holding hands, but instead of the last person standing 
with one hand free (pointing to None), they reach around and hold the hand of 
the FIRST person in line! They form a complete circle!
In a Circular Linked List, there is no "None" at the end. The Tail always 
points back to the Head. This means you can keep walking forward forever, 
going around and around the circle.

APPROACH: High-Performance Modern Python 3.14
---------
- We use a Singly Linked Node structure with `__slots__ = ("val", "next")`.
- We maintain a `_tail` pointer and a `_size` tracker.
- FUN FACT: We actually don't NEED a `_head` pointer! Why? Because in a circular 
  list, the head is always exactly `_tail.next`! But we will keep an explicit `_head`
  property for code readability and familiarity.
- Appending is O(1): We insert after tail, and the new tail points to the head.
- Prepending is O(1): We insert before head, and the tail updates to point to the new head.

COMPLEXITY:
-----------
Time:  
  - Append/Prepend/Head/Tail/Rotate: O(1)
  - Search/Insert/Delete: O(N)
Space: O(N) for storing N nodes.
============================================================
"""

from typing import Optional, Any
import collections.abc

class Node[T]:
    """
    A single node in a Circular Linked List.
    __slots__ prevents dynamic dictionary creation for extreme memory efficiency.
    """
    __slots__ = ("val", "next")

    def __init__(self, val: T, next_node: Optional['Node[T]'] = None):
        self.val = val
        self.next = next_node

    def __repr__(self) -> str:
        return f"Node({self.val})"


class CircularLinkedList[T]:
    """
    A highly optimized Circular Linked List.
    Tracks head, tail, and size. Tail always points back to Head.
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
        """
        Enables forward traversal. 
        Because it's circular, we MUST stop when we reach the head again to prevent infinite loops!
        """
        if self.is_empty:
            return
            
        curr = self._head
        while True:
            yield curr.val
            curr = curr.next
            if curr == self._head:
                break

    def __repr__(self) -> str:
        """Enables clean printing: 'CLL[1 -> 2 -> 3 -> (back to 1)]'"""
        if self.is_empty:
            return "CLL[]"
        values = " -> ".join(str(val) for val in self)
        return f"CLL[{values} -> (back to {self._head.val})]"

    def append(self, val: T) -> 'CircularLinkedList[T]':
        """Adds a node to the END of the list in O(1) time."""
        new_node = Node(val)
        if self.is_empty:
            self._head = self._tail = new_node
            new_node.next = new_node  # Point to itself to form a circle of 1
        else:
            new_node.next = self._head  # New tail must point back to head
            self._tail.next = new_node  # Old tail points to new tail
            self._tail = new_node
        self._size += 1
        return self

    def prepend(self, val: T) -> 'CircularLinkedList[T]':
        """Adds a node to the FRONT of the list in O(1) time."""
        new_node = Node(val)
        if self.is_empty:
            self._head = self._tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self._head
            self._head = new_node
            self._tail.next = self._head  # Tail must point to the NEW head
        self._size += 1
        return self

    def insert_at(self, index: int, val: T) -> 'CircularLinkedList[T]':
        """Inserts a node at a specific index in O(N) time."""
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        match index:
            case 0:
                return self.prepend(val)
            case idx if idx == self._size:
                return self.append(val)
            case _:
                curr = self._head
                for _ in range(index - 1):
                    curr = curr.next
                
                new_node = Node(val, curr.next)
                curr.next = new_node
                self._size += 1
                return self

    def rotate(self) -> 'CircularLinkedList[T]':
        """
        Rotates the circular linked list by 1 step in O(1) time.
        The current head becomes the tail, and head.next becomes the new head.
        """
        if self._size > 1:
            self._tail = self._head
            self._head = self._head.next
        return self

    def delete(self, val: T) -> bool:
        """Deletes the FIRST occurrence of a value. O(N) time."""
        if self.is_empty:
            return False

        # Case 1: Deleting the Head
        if self._head.val == val:
            if self._size == 1:
                # Last element being deleted
                self._head = self._tail = None
            else:
                self._head = self._head.next
                self._tail.next = self._head  # Maintain circle
            self._size -= 1
            return True

        # Case 2: Deleting somewhere in the middle or tail
        curr = self._head
        while curr.next != self._head:
            if curr.next.val == val:
                # If we are deleting the tail, we must update the tail pointer
                if curr.next == self._tail:
                    self._tail = curr
                
                curr.next = curr.next.next
                self._size -= 1
                return True
            curr = curr.next

        return False

    def search(self, val: T) -> bool:
        """Searches for a value in the list. O(N) time."""
        return any(curr_val == val for curr_val in self)


if __name__ == "__main__":
    print("Testing highly optimized Python 3.14 CircularLinkedList...")
    
    # 1. Initialization and Appending
    cll: CircularLinkedList[int] = CircularLinkedList()
    cll.append(1).append(2).append(3)
    
    assert len(cll) == 3
    assert cll.head.val == 1
    assert cll.tail.val == 3
    # Check the circular link!
    assert cll.tail.next == cll.head 
    assert str(cll) == "CLL[1 -> 2 -> 3 -> (back to 1)]"
    print("✅ Append & Circular Link passed!")

    # 2. Prepending
    cll.prepend(0)
    assert len(cll) == 4
    assert cll.head.val == 0
    assert cll.tail.next == cll.head
    assert str(cll) == "CLL[0 -> 1 -> 2 -> 3 -> (back to 0)]"
    print("✅ Prepend passed!")

    # 3. Rotate
    cll.rotate()
    assert cll.head.val == 1
    assert cll.tail.val == 0
    assert str(cll) == "CLL[1 -> 2 -> 3 -> 0 -> (back to 1)]"
    print("✅ Rotate O(1) passed!")

    # 4. Deletion
    # Delete middle
    cll.delete(3)
    assert str(cll) == "CLL[1 -> 2 -> 0 -> (back to 1)]"
    
    # Delete head
    cll.delete(1)
    assert cll.head.val == 2
    assert cll.tail.next == cll.head
    assert str(cll) == "CLL[2 -> 0 -> (back to 2)]"
    
    # Delete tail
    cll.delete(0)
    assert cll.tail.val == 2
    assert cll.head.val == 2
    assert cll.tail.next == cll.head
    assert len(cll) == 1
    assert str(cll) == "CLL[2 -> (back to 2)]"
    print("✅ Delete passed!")

    print("🎉 All CircularLinkedList tests passed successfully!")

# ==============================================================================
# ⚠️ PYTHON < 3.12 COMPATIBILITY FALLBACK
# ==============================================================================
# The modern `class Name[T]:` syntax (PEP 695) requires Python 3.12+.
# If you are running this code in an older environment (like an online IDE), 
# you will get a "SyntaxError: invalid syntax".
# 
# To fix this, replace the modern syntax with the traditional Generic typing:
# 
# 1. Import Generic and TypeVar:
#    from typing import Generic, TypeVar
# 
# 2. Define the TypeVar:
#    T = TypeVar('T')
# 
# 3. Inherit from Generic[T]:
#    class Node(Generic[T]):
#        ...
#    
#    class DataStructure(Generic[T]):
#        ...
# ==============================================================================
