# 🚶‍♂️ Walkthrough: Number of Closed Islands

## 👶 Explain Like I'm 5
**WARNING:** In this specific problem, `0` is Land, and `1` is Water!

A "Closed Island" is a piece of land that is COMPLETELY surrounded by water.
If an island touches the very edge of the map, it is NOT closed, because we don't know what's beyond the edge of the map! It might be connected to a huge continent just off-screen.

So how do we only count the completely closed ones? We do this in Two Passes (two steps).

**Step 1: The "Border Patrol"**
We walk entirely around the outer edge of the map. If we see ANY land (`0`) touching the edge, we drop our paint bucket and sink that entire island (turn it to `1`). By the time we finish the border patrol, every single island that was touching the edge of the map is gone.

**Step 2: The "Safe Zone"**
Now we just scan the whole map normally, exactly like we did in Problem 1. Any land we find NOW is guaranteed to be a completely Closed Island! We count it, sink it, and keep scanning.

## 🎯 Core Strategy
This uses a classic **Two-Pass Matrix DFS** pattern. It leverages the exact same DFS function as the basic "Number of Islands" problem, but controls *when* and *why* it is called.

1. **DFS Helper `sink(r, c)`**: Standard DFS that turns connected `0`s into `1`s.
2. **Pass 1 (Border Patrol)**:
   - Loop through every cell in the grid.
   - If the cell is on the border (`r == 0` or `r == ROWS - 1` or `c == 0` or `c == COLS - 1`) **AND** it is land (`grid[r][c] == 0`), call `sink(r, c)`.
   - This effectively erases all invalid islands from the grid.
3. **Pass 2 (Count Closed Islands)**:
   - Initialize `closed_islands = 0`.
   - Loop through every cell in the grid.
   - If the cell is land (`grid[r][c] == 0`), it must be a closed island! 
   - Increment `closed_islands += 1`.
   - Call `sink(r, c)` so we don't double-count it.
4. Return `closed_islands`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**:
```text
  0 1 2 3
0 1 0 1 1   (0 touches top border)
1 1 0 1 1   (Connects to top border)
2 1 1 0 1   (Closed Island!)
3 0 1 1 1   (0 touches bottom/left border)
```
*Note: `1` is water, `0` is land.*

### Pass 1: Border Patrol
- Scan the borders. 
- `(0, 1)` is `0` and on the top border. Call `sink(0, 1)`.
  - DFS sinks `(0, 1)` and its neighbor `(1, 1)`. 
  - They become `1`s.
- `(3, 0)` is `0` and on the bottom/left border. Call `sink(3, 0)`.
  - DFS sinks `(3, 0)`. It becomes a `1`.
  
**Grid after Border Patrol**:
```text
  0 1 2 3
0 1 1 1 1
1 1 1 1 1
2 1 1 0 1
3 1 1 1 1
```

### Pass 2: Safe Zone Scan
- Loop through the entire grid.
- All cells are `1` until we hit `(2, 2)`.
- `(2, 2)` is `0`! 
  - `closed_islands += 1` (Now `1`).
  - Call `sink(2, 2)`. It turns into a `1`.
- Finish scanning.

Return `1`.

## 📊 Visual Diagram
Here is a visualization of how Pass 1 prepares the grid for Pass 2:

```mermaid
flowchart TD
    subgraph Initial Grid
        B1((0,1 : 0\nBORDER)) --- B2((1,1 : 0))
        C1((2,2 : 0\nCLOSED))
        B3((3,0 : 0\nBORDER))
    end
    
    subgraph Pass 1: Border Patrol
        S1["sink(0,1)"] --> B1
        S1 --> B2
        S2["sink(3,0)"] --> B3
        note1["Border 0s and all connected 0s\nare turned to 1s (Water)."]
    end
    
    subgraph Pass 2: Safe Zone Scan
        C1
        note2["Only the Closed island remains!\nScan finds it, counts it, and sinks it."]
    end
    
    Initial Grid --> Pass 1: Border Patrol
    Pass 1: Border Patrol --> Pass 2: Safe Zone Scan
    
    style B1 fill:#ffcdd2,color:#000
    style B2 fill:#ffcdd2,color:#000
    style B3 fill:#ffcdd2,color:#000
    
    style C1 fill:#c8e6c9,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(M \times N)$ where $M$ is rows and $N$ is columns. We scan the grid multiple times, but no cell is processed by the heavy DFS recursion more than once because we sink land to water immediately. $2 \times M \times N$ simplifies to $O(M \times N)$.
- **Space Complexity:** $O(M \times N)$ for the recursion stack in the worst case (a giant island filling the grid).

### Edge Cases Handled Safely
- **All Land Grid (`[[0, 0], [0, 0]]`):** The entire grid is on the border! Pass 1 will trigger on `(0, 0)` and sink the entire grid. Pass 2 will find only water. Returns `0`. Correct!
- **No Land (`[[1, 1], [1, 1]]`):** Neither pass triggers DFS. Returns `0`. Correct.
- **Island with Lakes:** If a closed island has water inside of it, the DFS only spreads on `0`s (land). The lake (`1`) is ignored, and the island is still correctly counted and sunk.
