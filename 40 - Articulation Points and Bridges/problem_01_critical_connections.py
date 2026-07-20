"""
============================================================
Problem: Critical Connections in a Network
Pattern: Articulation Points and Bridges (Tarjan's Algorithm)
Difficulty:
Link: https://leetcode.com/problem-placeholder/ Hard
LeetCode: #1192
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have `n` servers connected by cables (edges). A "critical connection" is a cable
that, if cut, makes some servers unable to talk to each other.
Find all the critical connections!

APPROACH: Tarjan's Bridge-Finding Algorithm
---------
1. Build an adjacency list (Graph).
2. Start a DFS. Assign every node a `discovery_time`.
3. Assume a node's `lowest_time` it can reach is initially its own `discovery_time`.
4. Visit all neighbors (except the immediate parent you just came from!).
5. If a neighbor is already visited, it's a back-edge! Update `lowest_time` using
   the neighbor's `discovery_time`.
6. If a neighbor is NOT visited, DFS into it. Then, update our `lowest_time` with
   the neighbor's `lowest_time`.
7. **THE BRIDGE CHECK**: If after returning from the neighbor, the neighbor's
   `lowest_time` is strictly GREATER than our `discovery_time`, it means the neighbor
   couldn't find ANY back-alley route to an earlier node. That edge is a bridge!

COMPLEXITY:
-----------
Time:  O(V + E) — Standard DFS traversal.
Space: O(V + E) — Graph representation and recursion stack.

EDGE CASES:
-----------
- Basic empty/null edge cases.
- Boundary constraints.
============================================================
"""

from typing import List


def critical_connections(n: int, connections: List[List[int]]) -> List[List[int]]:
    # Build Graph
    graph: List[List[int]] = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
        
    discovery_time = [-1] * n
    lowest_time = [-1] * n
    bridges = []
    time = 0
    
    def dfs(node: int, parent: int):
        nonlocal time
        discovery_time[node] = lowest_time[node] = time
        time += 1
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
                
            if discovery_time[neighbor] == -1:
                # Not visited yet, explore it
                dfs(neighbor, node)
                
                # After returning, update our lowest time based on what neighbor found
                lowest_time[node] = min(lowest_time[node], lowest_time[neighbor])
                
                # Check if it's a bridge!
                if lowest_time[neighbor] > discovery_time[node]:
                    bridges.append([node, neighbor])
            else:
                # Back-edge found! Update our lowest time
                lowest_time[node] = min(lowest_time[node], discovery_time[neighbor])

    # Graph is guaranteed to be connected, so we only need to start from 0
    dfs(0, -1)
    
    return bridges


if __name__ == "__main__":
    n = 4
    connections = [[0,1],[1,2],[2,0],[1,3]]
    # Node 3 is only connected to Node 1. Cutting [1,3] isolates Node 3.
    # Nodes 0, 1, 2 form a cycle, so cutting any of those leaves them connected.
    res = critical_connections(n, connections)
    assert len(res) == 1
    # Note: Edge can be [1, 3] or [3, 1]
    assert sorted(res[0]) == [1, 3], "Test 1"
    
    print("All tests passed!")
