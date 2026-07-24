# 🚶‍♂️ Walkthrough: Find if Path Exists in Graph

## 👶 Explain Like I'm 5
You have a map of roads connecting cities. Given a start city and a destination city, can you actually drive from the start to the destination using the roads? You just need a yes or no answer — any path works!

Think of it like pouring water onto a city map starting at your source city. The water flows down every connected road to every city it can reach. If the water eventually reaches your destination city, the answer is `True`. If the water stops spreading and never touches your destination, the answer is `False`.

## 🎯 Core Strategy
This is the most basic application of **Breadth-First Search (BFS)** or **Depth-First Search (DFS)**. BFS (used here) is often slightly better for finding *any* path in an unweighted graph because it expands uniformly, avoiding going too deep into giant unrelated branches.

1. **Base Case**: If `source == destination`, return `True` immediately. You're already there!
2. **Build Graph**: Convert the edge list into an Adjacency List `graph` using a `defaultdict`. Since the roads go both ways (undirected graph), if `[u, v]` is an edge, we add `v` to `u`'s list and `u` to `v`'s list.
3. **Initialize BFS**:
   - Create a `visited` set to avoid driving in circles forever. Add `source` to it.
   - Create a `queue` and add `source` to it.
4. **BFS Loop**:
   - Pop a `node` from the front of the queue.
   - Did we reach the destination? `if node == destination: return True`.
   - If not, look at all of the node's `neighbors` (connected cities).
   - If a neighbor hasn't been visited yet:
     - Mark it as visited (add to set).
     - Add it to the back of the queue to explore later.
5. **End of Loop**: If the queue becomes empty and we never found the destination, they are entirely disconnected. Return `False`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `n = 6`, `edges = [[0,1], [0,2], [3,5], [5,4], [4,3]]`
**Source = 0, Destination = 5**

### Initialization
- Graph is built:
  - 0: `[1, 2]`
  - 1: `[0]`
  - 2: `[0]`
  - 3: `[5, 4]`
  - 4: `[5, 3]`
  - 5: `[3, 4]`
- `visited = {0}`
- `queue = [0]`

### Execution
1. **Pop 0**:
   - `0 != 5`.
   - Neighbors of 0 are 1 and 2.
   - Both are unvisited. Add both to `visited` and `queue`.
   - `visited = {0, 1, 2}`. `queue = [1, 2]`.
2. **Pop 1**:
   - `1 != 5`.
   - Neighbor is 0. Already visited. Ignore.
   - `queue = [2]`.
3. **Pop 2**:
   - `2 != 5`.
   - Neighbor is 0. Already visited. Ignore.
   - `queue = []` (Empty!)

The queue is empty. We explored everything connected to 0 and never saw 5.
Return `False`.

## 📊 Visual Diagram
Here is how the BFS explores components and why it correctly returns False for disconnected subgraphs:

```mermaid
flowchart TD
    subgraph Component A (Reachable from 0)
        A0((City 0)) --- A1((City 1))
        A0 --- A2((City 2))
        note1["Water (BFS) starts at 0,\nspreads to 1 and 2.\nQueue empties here!"]
    end
    
    subgraph Component B (Disconnected!)
        B3((City 3)) --- B5((City 5\nTARGET))
        B5 --- B4((City 4))
        B4 --- B3
        note2["Since no road connects A to B,\nCity 5 is never reached."]
    end
    
    style A0 fill:#e3f2fd,color:#000
    style A1 fill:#e3f2fd,color:#000
    style A2 fill:#e3f2fd,color:#000
    
    style B5 fill:#ffcdd2,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(V + E)$ where $V$ is the number of vertices (cities) and $E$ is the number of edges (roads). We build the adjacency list in $O(E)$ time, and the BFS visits each node and checks each connected edge at most once.
- **Space Complexity:** $O(V + E)$ for the adjacency list. The `visited` set and the `queue` take $O(V)$ space. Overall space is linear.

### Edge Cases Handled Safely
- **Source is Destination:** `if source == destination: return True`. Solves instantly in $O(1)$ time, even if there are 0 edges.
- **No Edges ($E=0$):** `graph` builds empty. If source != dest, queue pops source, has no neighbors, queue empties, returns `False`. Correct.
- **Cycles in Graph:** Handled safely by the `visited` set. If the graph is `0 - 1 - 2 - 0`, BFS won't get stuck in a loop.
