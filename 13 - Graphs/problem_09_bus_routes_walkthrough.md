# 🚶‍♂️ Walkthrough: Bus Routes

## 👶 Explain Like I'm 5
You're in a city with bus routes. Each route visits certain stops. You start at stop `source` and want to reach stop `target`. 
Each time you get on a bus, you can ride it to any of its stops for free, but switching buses counts as 1 more bus. What is the **MINIMUM** number of buses you need to take?

A naive approach is to imagine every bus stop is a city, and the bus routes are roads. But if a bus route has 50 stops, that's $50 \times 49$ roads! This gets way too big.
Instead of jumping from Stop to Stop, we jump from **Bus to Bus**! 
Two buses are "connected" if they share a bus stop (like a transfer station).
So we just ask: "I start on the Red Line. Can I transfer to the Blue Line? Does the Blue Line go to my destination?"

## 🎯 Core Strategy
This requires **Breadth-First Search (BFS)** for finding the shortest path, but the critical insight is to treat the **Routes as Nodes** in our graph, not the stops!

1. **Base Case**: If `source == target`, you need `0` buses.
2. **Build Transfer Map**: We need to know which buses go to which stops. We create `stop_to_routes`, a mapping of `stop -> list of route_indices`.
3. **Initialize BFS**:
   - Create `visited_routes` (so we don't ride the same bus twice).
   - Create `visited_stops` (so we don't evaluate the same transfer station twice).
   - `queue = deque()`
4. **Seed the Queue**:
   - Look up `stop_to_routes[source]`. This gives us every bus route that visits our starting stop.
   - Enqueue all of these routes with a bus count of `1`: `queue.append((route_idx, 1))`.
   - Mark them as visited in `visited_routes`.
5. **BFS Execution**:
   - Pop `(route_idx, buses)` from the queue.
   - For every `stop` on this current bus route:
     - If `stop == target`, we found it! Return `buses`.
     - If `stop` hasn't been evaluated as a transfer station yet:
       - Mark `stop` as visited.
       - Look up all `next_route`s in `stop_to_routes[stop]`.
       - If `next_route` hasn't been ridden yet, mark it visited and enqueue `(next_route, buses + 1)`.
6. **Failure**: If the queue empties, return `-1`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**: `routes = [[1, 2, 7], [3, 6, 7]]`, `source = 1`, `target = 6`
Let's call `[1, 2, 7]` Route 0 (Red Line), and `[3, 6, 7]` Route 1 (Blue Line).

### 1. Build Transfer Map
- Stop 1: `[Route 0]`
- Stop 2: `[Route 0]`
- Stop 7: `[Route 0, Route 1]` (Transfer Station!)
- Stop 3: `[Route 1]`
- Stop 6: `[Route 1]`

### 2. Seed Queue
- Our source is `1`. Who visits Stop 1? Route 0.
- `queue.append((Route 0, 1 bus))`
- `visited_routes = {Route 0}`

### 3. BFS Loop
- **Pop**: `(Route 0, 1 bus)`.
- Loop through Route 0's stops: `[1, 2, 7]`.
  - **Stop 1**: Not the target. Visited.
  - **Stop 2**: Not the target. Who visits Stop 2? Just Route 0 (already visited).
  - **Stop 7**: Not the target. Who visits Stop 7? Route 0 (visited) and **Route 1 (UNVISITED)**!
    - Enqueue `(Route 1, 1+1 = 2 buses)`.
    - `visited_routes = {Route 0, Route 1}`.
- **Pop**: `(Route 1, 2 buses)`.
- Loop through Route 1's stops: `[3, 6, 7]`.
  - **Stop 3**: Not the target.
  - **Stop 6**: `6 == target`! **BINGO!** 

Return `2`.

## 📊 Visual Diagram
Here is how BFS views the graph of *Routes* rather than the graph of *Stops*:

```mermaid
flowchart TD
    subgraph Stops (Too Complex to BFS directly)
        S1((Stop 1)) --- S2((Stop 2))
        S1 --- S7((Stop 7))
        S2 --- S7
        S3((Stop 3)) --- S6((Stop 6))
        S3 --- S7
        S6 --- S7
        note1["Fully connected route stops create massive sub-graphs!"]
    end
    
    subgraph Routes (Clean and Fast BFS)
        R0["Route 0\n(Buses: 1)"] -->|Transfer at Stop 7| R1["Route 1\n(Buses: 2)"]
        note2["R1 contains Target Stop 6.\nReturn 2."]
    end
    
    style R0 fill:#e3f2fd,color:#000
    style R1 fill:#c8e6c9,color:#000
    style S7 fill:#fff9c4,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(N \cdot M)$ where $N$ is the number of routes, and $M$ is the average number of stops per route. We process each stop on each route essentially once because of our `visited_stops` set, and we process each route once because of our `visited_routes` set.
- **Space Complexity:** $O(N \cdot M)$. The `stop_to_routes` dictionary stores a reference for every stop on every route. The queue and visited sets are bounded by this as well.

### Edge Cases Handled Safely
- **Source equals Target:** Instantly returns `0`. Handled.
- **Source and Target on the same route:** Returns `1` during the very first popped route.
- **Disconnected Routes:** If there are two competing bus companies and they share no stops, the queue will naturally empty without finding the target. Returns `-1`.
- **Circular/Redundant Routes:** The `visited_routes` and `visited_stops` sets instantly block any infinite loops or redundant processing.
