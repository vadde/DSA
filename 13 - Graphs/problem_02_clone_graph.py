"""
============================================================
Problem: Clone Graph
Pattern: Graphs / Hash Maps
Difficulty: Medium
Link: https://leetcode.com/problems/clone-graph/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are holding a blueprint of a city, and you want to build an EXACT duplicate 
of the entire city on a new island.
If you build "New City A", you also have to build the road connecting it to 
"New City B".
But what if "New City B" connects back to "New City A"? 
If you aren't careful, you might accidentally build a SECOND "New City A"! 
You would end up building infinite cities forever.
To prevent this, you carry a magical notebook (a Hash Map).
Whenever you build a new city, you write down: "Old City A translates to New City A".
If you ever need to build a road to a city, you first check the notebook.
"Did I already build the new version of this city?"
If yes, just connect the road to the one you already built!
If no, build the new city, write it in the notebook, and then connect the road.

APPROACH:
---------
1. Initialize a Hash Map `old_to_new = {}`. This maps original nodes to cloned nodes.
   This ALSO acts as our `visited` set! If an old node is in the map, it means 
   we already visited it and cloned it.
2. Define a recursive helper `clone(node)`.
3. If `node` is None, return `None`.
4. If `node` is already in `old_to_new`, return the cloned version: 
   `return old_to_new[node]`.
5. If it's not in the map, we must clone it!
   - `copy = Node(node.val)`
6. IMMEDIATELY add it to the map BEFORE exploring its neighbors. This prevents 
   infinite loops if a neighbor links back to this node.
   - `old_to_new[node] = copy`
7. Loop through all the original node's neighbors.
   - For every neighbor, recursively clone it, and append the result to the 
     copy's neighbors list.
   - `copy.neighbors.append(clone(neighbor))`
8. Return the `copy`.

COMPLEXITY:
-----------
Time:  O(V + E) — We visit every Vertex (node) once, and traverse every Edge once.
Space: O(V) — The Hash Map stores exactly V nodes, and the recursion stack goes up to V deep.

EDGE CASES:
-----------
- Edge case 1: Empty graph (node is None). Returns `None`.
- Edge case 2: Graph with a single node (no neighbors). Returns a clone of that single node.
============================================================
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: 'Node') -> 'Node':
    """
    Returns a deep copy (clone) of the given graph.
    """
    if not node:
        return None

    # This dictionary maps Old Nodes to their New Cloned Nodes
    old_to_new = {}

    def clone(current_node: 'Node') -> 'Node':
        # If we already cloned this node, just return the clone!
        # This prevents infinite loops in cycles.
        if current_node in old_to_new:
            return old_to_new[current_node]

        # 1. Create the new node
        copy = Node(current_node.val)
        
        # 2. Add it to our mapping IMMEDIATELY before visiting neighbors
        old_to_new[current_node] = copy

        # 3. Recursively clone all neighbors and attach them to the new node
        for neighbor in current_node.neighbors:
            copy.neighbors.append(clone(neighbor))

        return copy

    return clone(node)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # 1 --- 2
    # |     |
    # 4 --- 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    cloned_node1 = clone_graph(node1)
    
    # Assert it's a different object in memory
    assert cloned_node1 is not node1, "Test 1 failed: Not a deep copy!"
    # Assert values are the same
    assert cloned_node1.val == 1, "Test 1 failed: Value mismatch"
    # Assert graph structure is identical (Check neighbors of 1)
    assert len(cloned_node1.neighbors) == 2, "Test 1 failed: Neighbor count mismatch"
    assert cloned_node1.neighbors[0].val == 2, "Test 1 failed: Neighbor value mismatch"
    
    # Check for the cycle
    # cloned_node1 -> cloned_node2 -> cloned_node1
    cloned_node2 = cloned_node1.neighbors[0]
    assert cloned_node2.neighbors[0] is cloned_node1, "Test 1 failed: Cycle not preserved!"

    # 🔲 Edge cases
    assert clone_graph(None) is None, "Edge 1: Empty graph"
    
    single_node = Node(42)
    cloned_single = clone_graph(single_node)
    assert cloned_single is not single_node, "Edge 2: Not a deep copy"
    assert cloned_single.val == 42, "Edge 2: Value mismatch"
    assert len(cloned_single.neighbors) == 0, "Edge 2: Neighbors mismatch"

    print("All tests passed!")
