"""
============================================================
Problem: Trapping Rain Water
Pattern: Two Pointers (Advanced: Converging Boundaries)
Difficulty: Hard
Link: https://leetcode.com/problems/trapping-rain-water/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a landscape made of square blocks of different heights. It starts 
raining heavily. Water will get trapped in the "valleys" between the tall blocks.
How much water sits on top of any single block? It depends entirely on the tallest 
block to its left, and the tallest block to its right. The water level will rise 
until it spills over the SHORTER of those two tall blocks. 
Instead of walking across the whole landscape for every single block to find the 
tallest ones, we can just send two scouts: one starting from the left, one from the 
right. The scout standing on the shorter block ALWAYS knows their limiting wall 
(it's the one they are currently standing on or just passed), so they can safely 
calculate the water on their block and take a step forward!

APPROACH:
---------
1. Initialize `left = 0` and `right = len(height) - 1`.
2. Initialize `max_left = 0` and `max_right = 0` to track the highest walls seen so far.
3. Initialize `total_water = 0`.
4. Loop `while left < right`:
   a. We always process the side with the SHORTER current height. Why? Because the 
      water level above a block is strictly determined by `min(max_left, max_right)`. 
      If `height[left] < height[right]`, we are GUARANTEED that `max_left` will be 
      smaller than or equal to whatever `max_right` is, so `max_left` is our bottleneck!
   b. If `height[left] < height[right]`:
      - If `height[left] >= max_left`, we can't trap water here. Update `max_left = height[left]`.
      - Else, water is trapped! Add `max_left - height[left]` to `total_water`.
      - Move `left += 1`.
   c. Else (if `height[left] >= height[right]`):
      - If `height[right] >= max_right`, update `max_right = height[right]`.
      - Else, add `max_right - height[right]` to `total_water`.
      - Move `right -= 1`.
5. Return `total_water`.

COMPLEXITY:
-----------
Time:  O(N) — We scan the array exactly once from both ends.
Space: O(1) — We only use a few integer variables.

EDGE CASES:
-----------
- Edge case 1: Array is empty or has fewer than 3 blocks. Impossible to trap water, returns 0.
- Edge case 2: Array is perfectly flat or just a pyramid `^`. Returns 0.
============================================================
"""

def trap_water(height: list[int]) -> int:
    """
    Computes how much water can be trapped after raining.
    """
    if not height or len(height) < 3:
        return 0

    left: int = 0
    right: int = len(height) - 1
    
    max_left: int = 0
    max_right: int = 0
    total_water: int = 0

    while left < right:
        if height[left] < height[right]:
            # The left side is shorter, so it dictates the bottleneck for the left pointer
            if height[left] >= max_left:
                max_left = height[left]
            else:
                total_water += max_left - height[left]
            left += 1
        else:
            # The right side is shorter (or equal), so it dictates the bottleneck for the right pointer
            if height[right] >= max_right:
                max_right = height[right]
            else:
                total_water += max_right - height[right]
            right -= 1

    return total_water

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Test 1 failed: Standard LC case"
    assert trap_water([4, 2, 0, 3, 2, 5]) == 9, "Test 2 failed"
    
    # 🔲 Edge cases
    assert trap_water([3, 2, 1, 2, 3]) == 4, "Edge 1: Perfect bowl"
    assert trap_water([1, 2, 3, 4, 5]) == 0, "Edge 2: Stairs up"
    assert trap_water([5, 4, 3, 2, 1]) == 0, "Edge 3: Stairs down"

    print("All tests passed!")
