"""
============================================================
Problem: Clone Graph
Pattern: Clone Pattern (DFS + Hash Map)
Difficulty: Medium
LeetCode: #133
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are given a node in a connected, undirected graph.
Make a deep copy (clone) of the entire graph.
You cannot just return the original nodes! You must make new ones.

APPROACH: DFS + Hash Map
---------
Use a Hash Map called `cloned` to map Original Node -> Cloned Node.
We use DFS:
1. If the node is `None`, return `None`.
2. If the node is already in `cloned`, return `cloned[node]`! (This prevents infinite loops).
3. Otherwise, create a new Node with the same value. Add it to `cloned` IMMEDIATELY.
4. Loop through the original node's neighbors, recursively clone them, and add
   them to the new node's neighbors list.

COMPLEXITY:
-----------
Time:  O(V + E) — Visit every vertex and edge once.
Space: O(V) — Hash Map stores all vertices.
============================================================
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: 'Node') -> 'Node':
    if not node:
        return None
        
    cloned_map = {}
    
    def dfs(curr: 'Node') -> 'Node':
        if curr in cloned_map:
            return cloned_map[curr]
            
        # Create clone and add to map IMMEDIATELY to prevent infinite cycles
        clone = Node(curr.val)
        cloned_map[curr] = clone
        
        # Clone all neighbors
        for neighbor in curr.neighbors:
            clone.neighbors.append(dfs(neighbor))
            
        return clone
        
    return dfs(node)


if __name__ == "__main__":
    # Create Graph: 1 -- 2
    #               |    |
    #               4 -- 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    cloned_node1 = clone_graph(node1)
    
    assert cloned_node1 is not node1, "Must be a deep copy!"
    assert cloned_node1.val == 1
    assert len(cloned_node1.neighbors) == 2
    assert cloned_node1.neighbors[0].val == 2
    assert cloned_node1.neighbors[1].val == 4
    
    # Check cycle reference
    assert cloned_node1.neighbors[0].neighbors[0] is cloned_node1, "Cycles must be preserved correctly!"
    
    print("All tests passed!")
