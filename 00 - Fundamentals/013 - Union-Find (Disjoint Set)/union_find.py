"""
Disjoint-Set Union (Union-Find) Implementation.

This module provides a production-grade UnionFind class featuring:
- Two-pass iterative path compression (immune to recursion limits)
- Union by size (maintaining shallow tree depth)
- Dynamic connected component tracking
- Maximum cluster size queries
"""

from typing import List


class UnionFind:
    """Disjoint-Set Union supporting near-constant time operations.

    Complexity:
        - find(x): O(alpha(N)) amortized
        - union(x, y): O(alpha(N)) amortized
        - connected(x, y): O(alpha(N)) amortized
        - Space: O(N)
    """

    def __init__(self, n: int) -> None:
        """Initializes DSU with N disjoint singleton sets [0 ... N-1]."""
        self._n = n
        self.parent: List[int] = list(range(n))
        self.size: List[int] = [1] * n
        self.num_components: int = n
        self.max_component_size: int = 1 if n > 0 else 0

    def find(self, x: int) -> int:
        """Finds representative of x's set with iterative path compression."""
        root = x
        while root != self.parent[root]:
            root = self.parent[root]

        # Path compression: update ancestors to point directly to root
        curr = x
        while curr != root:
            nxt = self.parent[curr]
            self.parent[curr] = root
            curr = nxt

        return root

    def union(self, x: int, y: int) -> bool:
        """Merges sets containing x and y.

        Returns:
            True if elements were in separate sets and merged.
            False if elements were already in the same set (detected a cycle!).
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by size: attach smaller tree under larger tree
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.num_components -= 1

        if self.size[root_x] > self.max_component_size:
            self.max_component_size = self.size[root_x]

        return True

    def connected(self, x: int, y: int) -> bool:
        """Returns True if x and y share the same component root."""
        return self.find(x) == self.find(y)

    def get_component_size(self, x: int) -> int:
        """Returns the number of elements in the component containing x."""
        return self.size[self.find(x)]


def test_union_find() -> None:
    """Unit tests verifying UnionFind correctness and component tracking."""
    uf = UnionFind(6)
    assert uf.num_components == 6
    assert uf.max_component_size == 1

    # Merge {0, 1}
    assert uf.union(0, 1) is True
    assert uf.connected(0, 1) is True
    assert uf.connected(0, 2) is False
    assert uf.num_components == 5
    assert uf.get_component_size(0) == 2

    # Merge {1, 2} -> component becomes {0, 1, 2}
    assert uf.union(1, 2) is True
    assert uf.connected(0, 2) is True
    assert uf.num_components == 4
    assert uf.get_component_size(2) == 3

    # Redundant connection (cycle detection test)
    assert uf.union(0, 2) is False  # Already connected!
    assert uf.num_components == 4

    # Merge {3, 4} and {4, 5}
    assert uf.union(3, 4) is True
    assert uf.union(4, 5) is True
    assert uf.num_components == 2

    # Final bridge between {0, 1, 2} and {3, 4, 5}
    assert uf.union(2, 5) is True
    assert uf.num_components == 1
    assert uf.max_component_size == 6
    assert uf.connected(0, 5) is True

    print("✅ All UnionFind tests passed successfully!")


if __name__ == "__main__":
    test_union_find()
