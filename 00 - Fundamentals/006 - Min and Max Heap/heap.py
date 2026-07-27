"""
============================================================
Problem: Min Heap / Priority Queue Implementation
Pattern: Data Structures (Fundamentals)
Difficulty: Medium
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a company hierarchy where the boss is always the smallest (or biggest)
person in the room. Every time a new person joins, they start at the bottom. 
If they are smaller than their manager, they swap places! They keep swapping 
upwards until they find a manager smaller than them.
When the top boss leaves, the person at the very bottom takes their place, 
and then they swap downwards with the smallest of their subordinates until 
they find their proper rank.
A Heap is usually stored in a simple Array! Because it's a "Complete Binary Tree",
we can use math to find someone's manager or subordinates without any pointers!

APPROACH: High-Performance Modern Python 3.14
---------
- We use a flat `list` to store the heap.
- The math magic (0-indexed):
  - Left Child of `i` = `2 * i + 1`
  - Right Child of `i` = `2 * i + 2`
  - Parent of `i` = `(i - 1) // 2`
- `push`: Append to the end of the list, then `_sift_up`.
- `pop`: Swap the root (index 0) with the last element. Pop the last element. 
  Then `_sift_down` the new root.
- We support a generic `T` assuming it implements `__lt__` (comparable).

COMPLEXITY:
-----------
Time:  O(log N) for push and pop. O(1) for peek/min. O(N) for heapify (build heap).
Space: O(N) to store elements.
============================================================
"""

from typing import Generic, TypeVar, Optional, List, Callable, Any

T = TypeVar('T')

class Heap(Generic[T]):
    __slots__ = ("_data", "_is_min_heap", "_compare")

    def __init__(self, is_min_heap: bool = True, key: Optional[Callable[[T], Any]] = None):
        self._data: List[T] = []
        self._is_min_heap = is_min_heap
        
        # Determine the comparison function based on min/max and custom key
        if key:
            if self._is_min_heap:
                self._compare = lambda a, b: key(a) < key(b)
            else:
                self._compare = lambda a, b: key(a) > key(b)
        else:
            if self._is_min_heap:
                self._compare = lambda a, b: a < b
            else:
                self._compare = lambda a, b: a > b

    @property
    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)
        
    def __repr__(self) -> str:
        kind = "MinHeap" if self._is_min_heap else "MaxHeap"
        return f"{kind}({self._data})"

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_up(self, index: int) -> None:
        """Bubble the element up until heap property is restored."""
        while index > 0:
            parent_idx = (index - 1) // 2
            # If the current element should be "above" its parent based on comparison
            if self._compare(self._data[index], self._data[parent_idx]):
                self._swap(index, parent_idx)
                index = parent_idx
            else:
                break

    def _sift_down(self, index: int) -> None:
        """Bubble the element down until heap property is restored."""
        size = len(self._data)
        
        while True:
            left_idx = 2 * index + 1
            right_idx = 2 * index + 2
            extreme_idx = index  # smallest for MinHeap, largest for MaxHeap

            # Check if left child is more "extreme" than current extreme
            if left_idx < size and self._compare(self._data[left_idx], self._data[extreme_idx]):
                extreme_idx = left_idx
                
            # Check if right child is more "extreme" than current extreme
            if right_idx < size and self._compare(self._data[right_idx], self._data[extreme_idx]):
                extreme_idx = right_idx

            if extreme_idx != index:
                self._swap(index, extreme_idx)
                index = extreme_idx
            else:
                break

    def push(self, val: T) -> None:
        """Adds a value to the heap in O(log N) time."""
        self._data.append(val)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> T:
        """Removes and returns the extreme (min/max) value in O(log N) time."""
        if self.is_empty:
            raise IndexError("pop from empty heap")
            
        # If there's only 1 element, just pop it directly
        if len(self._data) == 1:
            return self._data.pop()
            
        extreme_val = self._data[0]
        # Move the last leaf to the root, then sift it down
        self._data[0] = self._data.pop()
        self._sift_down(0)
        
        return extreme_val

    def peek(self) -> T:
        """Returns the extreme value without removing it in O(1) time."""
        if self.is_empty:
            raise IndexError("peek from empty heap")
        return self._data[0]


if __name__ == "__main__":
    print("Testing MinHeap...")
    min_heap: Heap[int] = Heap(is_min_heap=True)
    for num in [10, 4, 15, 20, 0, 30]:
        min_heap.push(num)
        
    assert min_heap.peek() == 0
    assert min_heap.pop() == 0
    assert min_heap.pop() == 4
    assert min_heap.pop() == 10
    assert len(min_heap) == 3
    print("✅ MinHeap passed!")

    print("\nTesting MaxHeap...")
    max_heap: Heap[int] = Heap(is_min_heap=False)
    for num in [10, 4, 15, 20, 0, 30]:
        max_heap.push(num)
        
    assert max_heap.peek() == 30
    assert max_heap.pop() == 30
    assert max_heap.pop() == 20
    assert max_heap.pop() == 15
    assert len(max_heap) == 3
    print("✅ MaxHeap passed!")
    
    print("\nTesting Custom Key Heap (Sort by string length)...")
    len_heap: Heap[str] = Heap(is_min_heap=True, key=lambda x: len(x))
    len_heap.push("Apple")
    len_heap.push("Kiwi")
    len_heap.push("Strawberry")
    
    assert len_heap.pop() == "Kiwi"
    assert len_heap.pop() == "Apple"
    print("✅ Custom Key Heap passed!")

    print("\n🎉 All Heap tests passed successfully!")

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
