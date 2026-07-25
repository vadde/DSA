# 🚶‍♂️ Walkthrough: Game of Life

## 👶 Explain Like I'm 5
You have a grid of cells that can be alive (1) or dead (0). Every cell looks at its 8 neighbors and decides to live or die based on rules. 
The catch: everyone has to update at the *exact same time*. If you update cell A, cell B next to it needs to know what cell A *used to be*!
Since we can't make a copy of the grid, we use special numbers! Let's say 2 means "I was dead, but I'm coming alive" and 3 means "I was alive, but I'm dying".

## 🎯 Core Strategy
**In-Place State Machine Encoding**.

1. **Pass 1: Apply rules.** For every cell, count live neighbors. To check if a neighbor *was* alive, check if it's `1` or `3` (since 3 means it was alive but is dying).
   - If it was alive (1) and should die: set it to `3`.
   - If it was dead (0) and should live: set it to `2`.
2. **Pass 2: Clean up.** Go through the grid again.
   - Any cell that is `2` becomes `1`.
   - Any cell that is `3` becomes `0`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Cell State Guide**:
- 0: Dead -> Dead
- 1: Alive -> Alive
- 2: Dead -> Alive
- 3: Alive -> Dead

**Grid**:
`[0, 1, 0]`
`[0, 0, 1]`
`[1, 1, 1]`

Let's look at Cell (r=1, c=1), which is a `0`.
- Neighbors: 1, 0, 0, 1, 1, 1, 1 (Wait, let's just count the 1s and 3s around it).
- Neighbors that are 1 or 3: 5 of them!
- Rule: A dead cell only comes alive if it has EXACTLY 3 neighbors. So it stays 0.

Let's look at Cell (r=0, c=1), which is a `1`.
- Neighbors that are 1 or 3: only 1 of them (the cell at 1,2).
- Rule: A live cell with < 2 neighbors dies!
- We change `grid[0][1]` from `1` to `3`.

## 📊 Visual Diagram

```mermaid
flowchart TD
    A["Iterate all cells (Pass 1)"] --> B["Count neighbors that are 1 or 3"]
    B --> C{"Cell is currently Alive (1)?"}
    
    C -->|YES| D{"Neighbors < 2 OR > 3?"}
    D -->|YES| E["Set to 3 (Alive -> Dead)"]
    D -->|NO| F["Stays 1"]
    
    C -->|NO (0)| G{"Neighbors == 3?"}
    G -->|YES| H["Set to 2 (Dead -> Alive)"]
    G -->|NO| I["Stays 0"]
    
    E & F & H & I --> A
    
    A -.->|Pass 2| J["Iterate all cells"]
    J --> K["If 2, change to 1\nIf 3, change to 0"]
    
    style E fill:#fff9c4,color:#000
    style H fill:#fff9c4,color:#000
    style K fill:#c8e6c9,color:#000
```

## 🛑 Complexity
- **Time:** $O(R \times C)$ — Two passes over the grid.
- **Space:** $O(1)$ — Modified in place!
