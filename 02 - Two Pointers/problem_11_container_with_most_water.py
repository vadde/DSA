"""
============================================================
Problem: Container With Most Water
Pattern: Two Pointers (Advanced: Greedy Area Maximization)
Difficulty: Medium
Link: https://leetcode.com/problems/container-with-most-water/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a bunch of wooden walls of different heights planted in the ground 
at equal distances. You want to pick two walls to form a fish tank, and you want 
the tank that can hold the MOST water.
The amount of water a tank can hold depends on two things:
1. How far apart the walls are (Width).
2. The height of the SHORTER wall (if one wall is tall and the other is short, 
   the water will just spill over the short one).

If we start by picking the two walls that are the FARTEST apart (left and right ends), 
we get the maximum possible Width.
To find a tank with even more water, we MUST find a taller wall. If we move the taller 
wall inwards, the width gets smaller AND the water is STILL limited by the shorter 
wall! That's a lose-lose situation. 
So, we greedily move the SHORTER wall inwards, hoping to find a much taller wall 
that makes up for the lost width.

APPROACH:
---------
1. Initialize `left = 0` and `right = len(height) - 1`.
2. Initialize `max_area = 0`.
3. Loop `while left < right`:
   a. Calculate the `current_width = right - left`.
   b. Calculate the `current_height = min(height[left], height[right])`.
   c. Calculate `current_area = current_width * current_height`.
   d. Update `max_area = max(max_area, current_area)`.
   e. Greedily move the pointer pointing to the shorter line inward.
      - If `height[left] < height[right]`, increment `left`.
      - Else, decrement `right`.
4. Return `max_area`.

COMPLEXITY:
-----------
Time:  O(N) — We scan the array exactly once from both ends.
Space: O(1) — Only a few variables for pointers and max area.

EDGE CASES:
-----------
- Edge case 1: Array has only 2 lines. Returns exactly the area between them.
- Edge case 2: Multiple lines of the same height. Logic holds.
============================================================
"""

def max_area(height: list[int]) -> int:
    """
    Finds two lines that together with the x-axis form a container, 
    such that the container contains the most water.
    """
    left: int = 0
    right: int = len(height) - 1
    max_water: int = 0

    while left < right:
        current_width: int = right - left
        current_height: int = min(height[left], height[right])
        current_area: int = current_width * current_height
        
        max_water = max(max_water, current_area)

        # Move the pointer pointing to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "Test 1 failed: Standard case"
    assert max_area([4, 3, 2, 1, 4]) == 16, "Test 2 failed: Bowl shape"
    
    # 🔲 Edge cases
    assert max_area([1, 1]) == 1, "Edge 1: Minimum two lines"
    assert max_area([1, 2, 1]) == 2, "Edge 2: Triangle shape"

    print("All tests passed!")
