"""
Dynamic Array Implementation from Scratch.

This module provides a production-grade DynamicArray class implementing
geometric resizing, amortized O(1) appending, index bounds verification,
and Python sequence protocol integration.
"""

from typing import Any, Iterator, Optional


class DynamicArray:
    """A resilient, dynamically resizing array similar to Python list or C++ std::vector.

    Complexity:
        - Access: O(1)
        - Update: O(1)
        - Append: Amortized O(1), Worst-case O(N) on resize
        - Pop: O(1)
        - Insert (arbitrary): O(N)
        - Delete (arbitrary): O(N)
        - Space: O(N)
    """

    INITIAL_CAPACITY: int = 4
    GROWTH_FACTOR: int = 2

    def __init__(self, initial_capacity: Optional[int] = None) -> None:
        """Initializes dynamic array with given or default capacity."""
        self._capacity: int = initial_capacity if initial_capacity else self.INITIAL_CAPACITY
        self._size: int = 0
        self._buffer: list[Any] = [None] * self._capacity

    def __len__(self) -> int:
        """Returns the number of active elements in the array."""
        return self._size

    @property
    def capacity(self) -> int:
        """Returns the current internal buffer capacity."""
        return self._capacity

    def is_empty(self) -> bool:
        """Returns True if the array contains zero elements."""
        return self._size == 0

    def __getitem__(self, index: int) -> Any:
        """Retrieves an element at the specified index."""
        actual_index = self._normalize_index(index)
        return self._buffer[actual_index]

    def __setitem__(self, index: int, value: Any) -> None:
        """Assigns a value to the specified index."""
        actual_index = self._normalize_index(index)
        self._buffer[actual_index] = value

    def append(self, item: Any) -> None:
        """Appends an item to the end of the array in amortized O(1) time."""
        if self._size == self._capacity:
            self._resize(self._capacity * self.GROWTH_FACTOR)
        self._buffer[self._size] = item
        self._size += 1

    def pop(self) -> Any:
        """Removes and returns the last element in O(1) time."""
        if self._size == 0:
            raise IndexError("pop from empty dynamic array")
        self._size -= 1
        val = self._buffer[self._size]
        self._buffer[self._size] = None  # Prevent lingering memory references

        # Quarter-capacity shrink threshold to avoid resizing thrash
        if 0 < self._size <= self._capacity // 4 and self._capacity > self.INITIAL_CAPACITY:
            self._resize(max(self.INITIAL_CAPACITY, self._capacity // 2))
        return val

    def insert(self, index: int, item: Any) -> None:
        """Inserts an element at an arbitrary index in O(N) time."""
        if index < 0:
            index += self._size
        if not (0 <= index <= self._size):
            raise IndexError(f"Insert index {index} out of bounds for size {self._size}")

        if self._size == self._capacity:
            self._resize(self._capacity * self.GROWTH_FACTOR)

        for i in range(self._size, index, -1):
            self._buffer[i] = self._buffer[i - 1]

        self._buffer[index] = item
        self._size += 1

    def delete(self, index: int) -> Any:
        """Deletes and returns the element at the specified index in O(N) time."""
        actual_index = self._normalize_index(index)
        removed_val = self._buffer[actual_index]

        for i in range(actual_index, self._size - 1):
            self._buffer[i] = self._buffer[i + 1]

        self._size -= 1
        self._buffer[self._size] = None

        if 0 < self._size <= self._capacity // 4 and self._capacity > self.INITIAL_CAPACITY:
            self._resize(max(self.INITIAL_CAPACITY, self._capacity // 2))

        return removed_val

    def _resize(self, new_capacity: int) -> None:
        """Allocates a new buffer of specified capacity and copies existing items."""
        new_buffer: list[Any] = [None] * new_capacity
        for i in range(self._size):
            new_buffer[i] = self._buffer[i]
        self._buffer = new_buffer
        self._capacity = new_capacity

    def _normalize_index(self, index: int) -> int:
        """Handles negative indexing and raises IndexError for out-of-bounds access."""
        actual_index = index if index >= 0 else index + self._size
        if not (0 <= actual_index < self._size):
            raise IndexError(f"Index {index} out of bounds for array of size {self._size}")
        return actual_index

    def __iter__(self) -> Iterator[Any]:
        """Provides sequential iteration over elements."""
        for i in range(self._size):
            yield self._buffer[i]

    def __repr__(self) -> str:
        """String representation of the dynamic array."""
        elements = [repr(self._buffer[i]) for i in range(self._size)]
        return f"DynamicArray([{', '.join(elements)}], size={self._size}, capacity={self._capacity})"


def test_dynamic_array() -> None:
    """Unit tests verifying DynamicArray behavior under edge cases."""
    arr = DynamicArray(initial_capacity=2)
    assert len(arr) == 0
    assert arr.is_empty()

    # Append tests and resizing
    arr.append(10)
    arr.append(20)
    assert len(arr) == 2
    assert arr.capacity == 2

    # Trigger geometric resize
    arr.append(30)
    assert len(arr) == 3
    assert arr.capacity == 4
    assert arr[0] == 10
    assert arr[1] == 20
    assert arr[2] == 30
    assert arr[-1] == 30

    # Insert test
    arr.insert(1, 15)
    assert list(arr) == [10, 15, 20, 30]

    # Pop test
    popped = arr.pop()
    assert popped == 30
    assert list(arr) == [10, 15, 20]

    # Delete test
    deleted = arr.delete(1)
    assert deleted == 15
    assert list(arr) == [10, 20]

    print("✅ All DynamicArray tests passed successfully!")


if __name__ == "__main__":
    test_dynamic_array()
