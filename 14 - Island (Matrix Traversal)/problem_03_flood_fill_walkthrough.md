# 🚶‍♂️ Walkthrough: Flood Fill

## 👶 Explain Like I'm 5
Have you ever used Microsoft Paint? 
You draw a shape, then you click the "Paint Bucket" tool and click inside the shape. The whole inside fills up with a new color!
This problem is literally writing the code for the Paint Bucket tool.

You are given a starting pixel `(sr, sc)` and a `new_color`.
First, you look at the starting pixel to see what color it currently is (let's call this the `original_color`).
Then, you pour your paint! The paint spreads Up, Down, Left, and Right.
BUT, the paint ONLY spreads to pixels that match the `original_color`. It won't paint over black lines or different colored shapes.

## 🎯 Core Strategy
This is another classic **Matrix DFS (Depth-First Search)** problem, extremely similar to "Number of Islands".

1. **Initialization**: Find the `original_color` of the starting pixel: `image[sr][sc]`.
2. **Infinite Loop Prevention (Crucial)**: If the `original_color` is *already* the `new_color`, we don't need to do anything! If we don't check this, our DFS will get stuck in an infinite loop because it keeps trying to paint a pixel that's already painted, thinking it's still finding "valid" pixels.
3. **Recursive DFS Helper**: `dfs(r, c)`
   - **Base Cases**: 
     - Are we out of bounds? Return.
     - Is this pixel a DIFFERENT color than the `original_color`? Return. The paint stops spreading here!
   - **Action**: Change the current pixel's color: `image[r][c] = new_color`.
   - **Spread**: Recursively call DFS in all 4 directions (Up, Down, Left, Right).
4. **Trigger**: Call `dfs(sr, sc)` to drop the paint bucket.
5. Return the modified `image`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Input**:
```text
image = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 1]
]
sr = 1, sc = 1, new_color = 2
```

### 1. Initialization
- Starting Pixel: `(1, 1)`.
- `original_color = image[1][1] = 1`.
- `new_color = 2`.
- `1 != 2`, so we proceed. Call `dfs(1, 1)`.

### 2. DFS Execution
- **`dfs(1, 1)`**: 
  - Matches `original_color` (1). Paint it: `image[1][1] = 2`.
  - Up `dfs(0, 1)`: Matches 1! Paint to 2. Recurse from `(0, 1)`.
    - Up (Out), Down (Already 2! Returns), Left `(0, 0)` -> Paints to 2, Right `(0, 2)` -> Paints to 2.
  - Down `dfs(2, 1)`: It's a `0`! **DOES NOT MATCH original_color**. Returns immediately.
  - Left `dfs(1, 0)`: Matches 1! Paint to 2. Recurse.
    - Up (Already 2), Down `(2, 0)` -> Matches 1! Paint to 2. Left (Out), Right (Already 2).
  - Right `dfs(1, 2)`: It's a `0`! **DOES NOT MATCH**. Returns immediately.

### 3. Result
Notice that the `1` at the bottom right `(2, 2)` was never reached because the DFS was blocked by the `0`s!

**Final Image**:
```text
  [2, 2, 2],
  [2, 2, 0],
  [2, 0, 1]
```

## 📊 Visual Diagram
Here's how the DFS spreads out from the center, stopping when it hits a boundary of a different color:

```mermaid
flowchart TD
    subgraph Grid Start State
        P11((1,1 : Color 1\nSTART)) --- P01((0,1 : Color 1))
        P11 --- P21((2,1 : Color 0\nBLOCK!))
        P11 --- P10((1,0 : Color 1))
        P11 --- P12((1,2 : Color 0\nBLOCK!))
        note1["DFS spreads Up and Left.\nDown and Right are blocked by 0s!"]
    end
    
    subgraph Grid End State
        F11((1,1 : Color 2)) --- F01((0,1 : Color 2))
        F11 --- F21((2,1 : Color 0))
        F11 --- F10((1,0 : Color 2))
        F11 --- F12((1,2 : Color 0))
    end
    
    Grid Start State --> Grid End State
    
    style P11 fill:#c8e6c9,color:#000
    style P01 fill:#c8e6c9,color:#000
    style P10 fill:#c8e6c9,color:#000
    
    style P21 fill:#ffcdd2,color:#000
    style P12 fill:#ffcdd2,color:#000
    
    style F11 fill:#bbdefb,color:#000
    style F01 fill:#bbdefb,color:#000
    style F10 fill:#bbdefb,color:#000
    style F21 fill:#ffcdd2,color:#000
    style F12 fill:#ffcdd2,color:#000
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(M \times N)$ where $M$ is rows and $N$ is cols. In the worst case (the entire screen is one color), the DFS visits every pixel. It never visits a pixel more than once because it immediately changes the color, which acts as a "visited" check.
- **Space Complexity:** $O(M \times N)$ for the recursion stack in the worst-case scenario.

### Edge Cases Handled Safely
- **Same Color Edge Case:** If the image is all `0`s and you try to flood fill with `0`, the line `if original_color == color: return image` instantly kicks in. Without this line, `dfs` would check `image[r][c] == original_color` (True), paint it `0`, then recurse to neighbors, which recurse back, causing a `RecursionError`!
- **Single Pixel Grid (`[[1]]`):** Perfectly handled. DFS paints it, all 4 directions return out-of-bounds. Done.
