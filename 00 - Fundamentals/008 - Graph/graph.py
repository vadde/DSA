"""
============================================================
Problem: Graph (Adjacency List) Implementation
Pattern: Data Structures (Fundamentals)
Difficulty: Medium
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A Graph is just a network of dots (Vertices/Nodes) connected by lines (Edges). 
Think of it like a map of a city. The intersections are the vertices, and the 
roads are the edges. 
- If a road is one-way, it's a "Directed Graph".
- If a road is two-way, it's an "Undirected Graph".

Instead of storing this as a giant grid (a matrix) with lots of empty space, 
we use an "Adjacency List". For every intersection, we just keep a list of the 
other intersections it connects to! It saves a ton of space.

APPROACH: High-Performance Modern Python 3.14
---------
- We use a flat Python dictionary: `_adj_list: dict[T, set[T]]`.
- Mapping a Vertex (of type T) to a `set` of neighbor Vertices ensures O(1) 
  lookups for edge existence and prevents duplicate edges effortlessly.
- **Add Vertex**: Just add it to the dictionary with an empty set. O(1).
- **Add Edge**: Add `dst` to `adj_list[src]`. If undirected, also add `src` to `adj_list[dst]`. O(1).
- **Remove Edge**: Remove from the sets. O(1).
- **Remove Vertex**: Remove the vertex from the dictionary, and then iterate through 
  all other vertices to remove it from their neighbor sets. O(V).

COMPLEXITY:
-----------
Time:  O(1) to Add Vertex, Add Edge, Remove Edge, Get Neighbors.
       O(V) to Remove Vertex.
Space: O(V + E) where V is vertices and E is edges. Extremely efficient!
============================================================
"""

from typing import Generic, TypeVar, Optional, Generator
import collections.abc

T = TypeVar('T')

class Graph(Generic[T]):
    __slots__ = ("_adj_list", "_is_directed")

    def __init__(self, is_directed: bool = False):
        # We use a set for neighbors for O(1) edge lookups and removals!
        self._adj_list: dict[T, set[T]] = {}
        self._is_directed = is_directed

    @property
    def vertex_count(self) -> int:
        return len(self._adj_list)

    @property
    def edge_count(self) -> int:
        count = sum(len(neighbors) for neighbors in self._adj_list.values())
        return count if self._is_directed else count // 2

    def __contains__(self, vertex: T) -> bool:
        """Enables 'if vertex in graph:'"""
        return vertex in self._adj_list

    def __repr__(self) -> str:
        kind = "DirectedGraph" if self._is_directed else "UndirectedGraph"
        return f"{kind}(Vertices: {self.vertex_count}, Edges: {self.edge_count})"

    def add_vertex(self, vertex: T) -> None:
        """Adds a vertex to the graph in O(1) time."""
        if vertex not in self._adj_list:
            self._adj_list[vertex] = set()

    def add_edge(self, src: T, dst: T) -> None:
        """Adds an edge between src and dst in O(1) time."""
        # Ensure both vertices exist
        self.add_vertex(src)
        self.add_vertex(dst)
        
        self._adj_list[src].add(dst)
        if not self._is_directed:
            self._adj_list[dst].add(src)

    def remove_edge(self, src: T, dst: T) -> None:
        """Removes the edge between src and dst in O(1) time."""
        if src in self._adj_list and dst in self._adj_list[src]:
            self._adj_list[src].remove(dst)
            
        if not self._is_directed:
            if dst in self._adj_list and src in self._adj_list[dst]:
                self._adj_list[dst].remove(src)

    def remove_vertex(self, vertex: T) -> None:
        """Removes a vertex and ALL its connected edges in O(V) time."""
        if vertex not in self._adj_list:
            return
            
        # 1. Remove the vertex completely from the adjacency list
        del self._adj_list[vertex]
        
        # 2. Iterate through all other vertices and remove this vertex from their sets
        for neighbors in self._adj_list.values():
            neighbors.discard(vertex)  # discard removes without throwing KeyError

    def get_neighbors(self, vertex: T) -> set[T]:
        """Returns the neighbors of a vertex in O(1) time."""
        if vertex not in self._adj_list:
            raise KeyError(f"Vertex {vertex} not found in graph.")
        return self._adj_list[vertex]

    def get_vertices(self) -> list[T]:
        """Returns all vertices in the graph."""
        return list(self._adj_list.keys())


if __name__ == "__main__":
    print("Testing Undirected Graph...")
    graph: Graph[str] = Graph(is_directed=False)
    
    # Add vertices and edges
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")
    
    assert graph.vertex_count == 3
    assert graph.edge_count == 3
    assert "B" in graph.get_neighbors("A")
    assert "A" in graph.get_neighbors("B")
    print("✅ Add Edges passed!")

    # Remove Edge
    graph.remove_edge("A", "B")
    assert "B" not in graph.get_neighbors("A")
    assert "A" not in graph.get_neighbors("B")
    assert graph.edge_count == 2
    print("✅ Remove Edge passed!")

    # Remove Vertex
    graph.remove_vertex("C")
    assert "C" not in graph
    assert graph.vertex_count == 2
    assert graph.edge_count == 0  # C held the last two edges
    print("✅ Remove Vertex passed!")
    
    print("\nTesting Directed Graph...")
    di_graph: Graph[int] = Graph(is_directed=True)
    di_graph.add_edge(1, 2)
    
    assert 2 in di_graph.get_neighbors(1)
    assert 1 not in di_graph.get_neighbors(2)  # One-way street!
    assert di_graph.edge_count == 1
    print("✅ Directed Edges passed!")

    print("\n🎉 All Graph tests passed successfully!")
