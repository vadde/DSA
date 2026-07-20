"""
============================================================
Problem: Flood Fill
Pattern: Island (Matrix Traversal)
Difficulty: Easy
Link: https://leetcode.com/problems/flood-fill/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Have you ever used Microsoft Paint? 
You draw a shape, then you click the "Paint Bucket" tool and click inside 
the shape. The whole inside fills up with a new color!
This problem is literally writing the code for the Paint Bucket tool.
You are given a starting pixel `(sr, sc)` and a `new_color`.
First, you look at the starting pixel to see what color it currently is 
(let's call this the `original_color`).
Then, you pour your paint! The paint spreads Up, Down, Left, and Right.
BUT, the paint ONLY spreads to pixels that match the `original_color`. 
It won't paint over black lines or different colored shapes.

APPROACH:
---------
1. Find the `original_color` of the starting pixel `image[sr][sc]`.
2. Check for an edge case: If the `original_color` is ALREADY the `new_color`, 
   we don't need to do anything! (If we don't check this, we might get stuck in 
   an infinite loop of painting the same color over and over).
3. Define our recursive `dfs(r, c)`:
   - Base Case: Out of bounds? Return.
   - Base Case: Is this pixel a DIFFERENT color than the `original_color`? 
     If yes, the paint stops spreading! Return.
   - Change the color: `image[r][c] = new_color`.
   - Recursively call DFS in all 4 directions.
4. Call `dfs(sr, sc)` to start the paint bucket.
5. Return the modified `image`.

COMPLEXITY:
-----------
Time:  O(M * N) — In the worst case (the whole screen is one color), we visit every pixel.
Space: O(M * N) — The recursion stack can grow to the size of the whole grid.

EDGE CASES:
-----------
- Edge case 1: The new color is exactly the same as the old color. We must return 
  immediately to prevent infinite recursion!
============================================================
"""

from typing import List

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """
    Performs a flood fill on the image starting from the given coordinates.
    """
    if not image:
        return image

    ROWS = len(image)
    COLS = len(image[0])
    original_color = image[sr][sc]

    # CRITICAL: If the color is already correct, do nothing to avoid infinite loops!
    if original_color == color:
        return image

    def dfs(r: int, c: int):
        # Base case: Out of bounds OR the pixel is a different color
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != original_color:
            return
        
        # SINK IT! Change to the new color
        image[r][c] = color

        # Spread the paint!
        dfs(r - 1, c) # Up
        dfs(r + 1, c) # Down
        dfs(r, c - 1) # Left
        dfs(r, c + 1) # Right

    # Drop the paint bucket at the starting coordinate
    dfs(sr, sc)

    return image

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    image1 = [
        [1,1,1],
        [1,1,0],
        [1,0,1]
    ]
    # Starting at (1,1), original color is 1, new color is 2
    # Should fill all connected 1s. The 1 at the bottom right is blocked by 0s!
    expected1 = [
        [2,2,2],
        [2,2,0],
        [2,0,1]
    ]
    assert flood_fill(image1, 1, 1, 2) == expected1, "Test 1 failed"

    # 🔲 Edge cases
    image2 = [
        [0,0,0],
        [0,0,0]
    ]
    # Starting at (0,0), original color is 0, new color is 0
    # Should return immediately without infinite recursion!
    expected2 = [
        [0,0,0],
        [0,0,0]
    ]
    assert flood_fill(image2, 0, 0, 0) == expected2, "Edge 1: Same color failed"

    print("All tests passed!")
