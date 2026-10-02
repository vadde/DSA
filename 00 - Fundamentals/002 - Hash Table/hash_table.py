"""
Separate Chaining Hash Table Implementation from Scratch.

This module provides a production-grade HashTable class with dynamic resizing,
load factor monitoring, collision chain handling, and Python mapping protocol integration.
"""

from typing import Any, Iterator, Optional, Tuple


class HashNode:
    """A single key-value node within a collision chain."""

    __slots__ = ("key", "value", "next")

    def __init__(self, key: Any, value: Any, next_node: Optional["HashNode"] = None) -> None:
        self.key: Any = key
        self.value: Any = value
        self.next: Optional[HashNode] = next_node


class HashTable:
    """A resilient, dynamically resizing hash map using separate chaining.

    Complexity:
        - Access: Average O(1), Worst O(N)
        - Insert/Update: Average O(1), Worst O(N) on resize
        - Delete: Average O(1), Worst O(N)
        - Space: O(N + M) where M is bucket capacity
    """

    INITIAL_CAPACITY: int = 16
    MAX_LOAD_FACTOR: float = 0.75

    def __init__(self, capacity: Optional[int] = None) -> None:
        """Initializes hash table with given capacity or default 16 buckets."""
        self._capacity: int = capacity if capacity else self.INITIAL_CAPACITY
        self._size: int = 0
        self._buckets: list[Optional[HashNode]] = [None] * self._capacity

    def __len__(self) -> int:
        """Returns the number of active key-value pairs."""
        return self._size

    @property
    def capacity(self) -> int:
        """Returns the number of internal buckets."""
        return self._capacity

    @property
    def load_factor(self) -> float:
        """Returns the current load factor alpha = N / M."""
        return self._size / self._capacity

    def _hash(self, key: Any) -> int:
        """Computes internal bucket index using positive 31-bit modulo."""
        return (hash(key) & 0x7FFFFFFF) % self._capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        """Inserts or updates a key-value pair in average O(1) time."""
        index = self._hash(key)
        head = self._buckets[index]

        # Scan for existing key in bucket chain
        curr = head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        # Insert new node at head of chain
        new_node = HashNode(key, value, head)
        self._buckets[index] = new_node
        self._size += 1

        # Check if resize threshold exceeded
        if self.load_factor > self.MAX_LOAD_FACTOR:
            self._rehash(self._capacity * 2)

    def __getitem__(self, key: Any) -> Any:
        """Retrieves value associated with key, raising KeyError if absent."""
        index = self._hash(key)
        curr = self._buckets[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        raise KeyError(f"Key '{key}' not found in hash table")

    def __delitem__(self, key: Any) -> None:
        """Deletes key-value pair in average O(1) time."""
        index = self._hash(key)
        curr = self._buckets[index]
        prev: Optional[HashNode] = None

        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self._buckets[index] = curr.next
                self._size -= 1
                return
            prev = curr
            curr = curr.next

        raise KeyError(f"Key '{key}' not found for deletion")

    def __contains__(self, key: Any) -> bool:
        """Checks if key exists in table."""
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def get(self, key: Any, default: Any = None) -> Any:
        """Retrieves value or default fallback."""
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def _rehash(self, new_capacity: int) -> None:
        """Re-allocates bucket table and migrates all existing nodes."""
        old_buckets = self._buckets
        self._capacity = new_capacity
        self._buckets = [None] * self._capacity
        self._size = 0  # Re-tallied via __setitem__

        for head in old_buckets:
            curr = head
            while curr:
                self.__setitem__(curr.key, curr.value)
                curr = curr.next

    def items(self) -> Iterator[Tuple[Any, Any]]:
        """Yields (key, value) pairs."""
        for head in self._buckets:
            curr = head
            while curr:
                yield (curr.key, curr.value)
                curr = curr.next

    def keys(self) -> Iterator[Any]:
        """Yields keys."""
        for k, _ in self.items():
            yield k

    def values(self) -> Iterator[Any]:
        """Yields values."""
        for _, v in self.items():
            yield v

    def __iter__(self) -> Iterator[Any]:
        """Default iteration over keys."""
        return self.keys()

    def __repr__(self) -> str:
        """Visual representation of key-value pairs."""
        pairs = [f"{repr(k)}: {repr(v)}" for k, v in self.items()]
        return f"HashTable({{{', '.join(pairs)}}}, size={self._size}, capacity={self._capacity})"


def test_hash_table() -> None:
    """Unit tests verifying HashTable correctness and collision handling."""
    ht = HashTable(capacity=4)
    assert len(ht) == 0
    assert ht.capacity == 4

    # Insert elements
    ht["apple"] = 100
    ht["banana"] = 200
    ht["cherry"] = 300
    assert len(ht) == 3
    assert ht["apple"] == 100
    assert ht["banana"] == 200
    assert ht["cherry"] == 300

    # Overwrite existing key
    ht["banana"] = 250
    assert ht["banana"] == 250
    assert len(ht) == 3

    # Trigger rehash (load factor > 0.75: 4 items in 4 buckets = 1.0 > 0.75)
    ht["date"] = 400
    assert len(ht) == 4
    assert ht.capacity == 8  # Doubled!
    assert ht["apple"] == 100
    assert ht["date"] == 400

    # Test membership
    assert "apple" in ht
    assert "grape" not in ht
    assert ht.get("grape", 999) == 999

    # Test deletion
    del ht["banana"]
    assert len(ht) == 3
    assert "banana" not in ht

    print("✅ All HashTable tests passed successfully!")


if __name__ == "__main__":
    test_hash_table()
