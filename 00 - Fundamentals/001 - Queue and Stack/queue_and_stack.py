"""
============================================================
Problem: Queue and Stack Implementation
Pattern: Data Structures (Fundamentals)
Difficulty: Easy
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Stack (LIFO - Last In, First Out): Imagine a stack of plates. When you put a 
new plate down (Push), it goes on top. When you take a plate off (Pop), you take 
it from the top. The last plate you put down is the first one you pick up.

Queue (FIFO - First In, First Out): Imagine a line at the grocery store. You 
join the line at the back (Enqueue). The cashier serves the person at the front 
(Dequeue). The first person to join the line is the first one served.

APPROACH: High-Performance Modern Python 3.14
---------
- While Python has `list` for Stacks and `collections.deque` for Queues, 
  implementing them from scratch using Linked Nodes teaches core fundamentals.
- **Stack**: Only needs a `_head` pointer (acting as the "top"). Push inserts 
  at the head, Pop removes from the head. Both are O(1).
- **Queue**: Needs both a `_head` (front) and `_tail` (back). Enqueue inserts 
  at the tail, Dequeue removes from the head. Both are O(1).
- We use `__slots__` and PEP 695 Type Parameters (`class Stack[T]:`).

COMPLEXITY:
-----------
Time:  O(1) for all Push, Pop, Enqueue, Dequeue operations.
Space: O(N) for storing N nodes.
============================================================
"""

from typing import Optional, Any
import collections.abc

class Node[T]:
    """Singly linked node for Stack and Queue."""
    __slots__ = ("val", "next")
    def __init__(self, val: T, next_node: Optional['Node[T]'] = None):
        self.val = val
        self.next = next_node
    def __repr__(self) -> str:
        return f"Node({self.val})"


class Stack[T]:
    """LIFO Data Structure using a Singly Linked List (Head pointer only)."""
    __slots__ = ("_head", "_size")

    def __init__(self):
        self._head: Optional[Node[T]] = None
        self._size: int = 0

    @property
    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def push(self, val: T) -> None:
        """Adds an item to the top of the stack. O(1) time."""
        self._head = Node(val, self._head)
        self._size += 1

    def pop(self) -> T:
        """Removes and returns the top item. O(1) time."""
        if self.is_empty:
            raise IndexError("pop from empty Stack")
        val = self._head.val
        self._head = self._head.next
        self._size -= 1
        return val

    def peek(self) -> T:
        """Returns the top item without removing it. O(1) time."""
        if self.is_empty:
            raise IndexError("peek from empty Stack")
        return self._head.val
        
    def __repr__(self) -> str:
        curr = self._head
        vals = []
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return f"Stack(Top -> [{', '.join(vals)}])"


class Queue[T]:
    """FIFO Data Structure using a Singly Linked List (Head and Tail pointers)."""
    __slots__ = ("_head", "_tail", "_size")

    def __init__(self):
        self._head: Optional[Node[T]] = None
        self._tail: Optional[Node[T]] = None
        self._size: int = 0

    @property
    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def enqueue(self, val: T) -> None:
        """Adds an item to the back of the queue. O(1) time."""
        new_node = Node(val)
        if self.is_empty:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self) -> T:
        """Removes and returns the front item. O(1) time."""
        if self.is_empty:
            raise IndexError("dequeue from empty Queue")
        val = self._head.val
        self._head = self._head.next
        self._size -= 1
        if self.is_empty:
            self._tail = None
        return val

    def peek(self) -> T:
        """Returns the front item without removing it. O(1) time."""
        if self.is_empty:
            raise IndexError("peek from empty Queue")
        return self._head.val

    def __repr__(self) -> str:
        curr = self._head
        vals = []
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return f"Queue(Front -> [{', '.join(vals)}] <- Back)"


if __name__ == "__main__":
    print("Testing Stack (LIFO)...")
    stack: Stack[int] = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert str(stack) == "Stack(Top -> [3, 2, 1])"
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert len(stack) == 1
    assert stack.pop() == 1
    assert stack.is_empty
    print("✅ Stack tests passed!")

    print("\nTesting Queue (FIFO)...")
    queue: Queue[str] = Queue()
    queue.enqueue("Alice")
    queue.enqueue("Bob")
    queue.enqueue("Charlie")
    assert str(queue) == "Queue(Front -> [Alice, Bob, Charlie] <- Back)"
    assert queue.peek() == "Alice"
    assert queue.dequeue() == "Alice"
    assert queue.dequeue() == "Bob"
    assert len(queue) == 1
    assert queue.dequeue() == "Charlie"
    assert queue.is_empty
    print("✅ Queue tests passed!")
