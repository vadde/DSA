"""
============================================================
Problem: Find Bridges in a Graph
Pattern: Articulation Points and Bridges (Tarjan's Algorithm)
Difficulty: Hard
Link: https://leetcode.com/problems/critical-connections-in-a-network/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A "bridge" (or critical connection) in a graph is an edge that, if removed, 
splits the graph into two disconnected pieces. We need to find all such edges.

APPROACH (Tarjan's Algorithm):
---------
1. DFS traversal to assign a `discovery_time` to each node.
2. Maintain a `lowest_reachable_time` for each node (the lowest discovery time
   reachable from the node, including its descendants, but NOT going back through
   the parent edge).
3. If a child's `lowest_reachable_time` is strictly GREATER than the current
   node's `discovery_time`, it means there's no back-edge from the child to an
   ancestor. Therefore, the edge to the child is a BRIDGE!

COMPLEXITY:
-----------
Time:  O(V + E)
Space: O(V + E)

EDGE CASES:
-----------
- Cycles (no bridges inside a cycle).
- Tree (every edge is a bridge).
============================================================
"""

from typing import List
from collections import defaultdict

def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
        
    bridges = []
    discovery_time = [-1] * n
    lowest_reachable = [-1] * n
    time = 0
    
    def dfs(curr: int, parent: int):
        nonlocal time
        discovery_time[curr] = lowest_reachable[curr] = time
        time += 1
        
        for neighbor in graph[curr]:
            if neighbor == parent:
                continue
                
            if discovery_time[neighbor] == -1: # unvisited
                dfs(neighbor, curr)
                lowest_reachable[curr] = min(lowest_reachable[curr], lowest_reachable[neighbor])
                
                if lowest_reachable[neighbor] > discovery_time[curr]:
                    bridges.append([curr, neighbor])
            else:
                # Back-edge
                lowest_reachable[curr] = min(lowest_reachable[curr], discovery_time[neighbor])
                
    dfs(0, -1)
    return bridges

if __name__ == "__main__":
    assert sorted(sorted(b) for b in criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])) == [[1,3]], "Test 1"
    assert sorted(sorted(b) for b in criticalConnections(2, [[0,1]])) == [[0,1]], "Test 2"
    print("All tests passed!")
