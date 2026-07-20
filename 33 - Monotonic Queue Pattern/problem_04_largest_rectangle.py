"""
============================================================
Problem: Largest Rectangle in Histogram
Pattern: Monotonic Stack
Difficulty: Hard
LeetCode: #84
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bar chart (histogram). What's the largest rectangle you can draw inside it?
A rectangle is limited by the SHORTEST bar it includes.

APPROACH: Monotonic Increasing Stack
---------
We need a stack that is strictly increasing.
If we see a bar that is SHORTER than the top of the stack, it means the rectangle
for the stack's top bar cannot extend any further to the right!
So, we pop it, calculate the area it formed (height * width), and check if it's the max.
Width = (current_index - new_top_of_stack_index - 1)
To easily process remaining bars at the end, we append a 0-height bar to the array.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)
============================================================
"""

from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    # Append a 0 so that all bars left in stack get processed at the end
    heights.append(0)
    stack = [-1]  # Dummy index to calculate width easily for the very first bar
    max_area = 0
    
    for i in range(len(heights)):
        # If current bar is SHORTER than the top of the stack,
        # we can't extend the top bar's rectangle any further.
        while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
            
        stack.append(i)
        
    heights.pop()  # Clean up the appended 0 just in case
    return max_area


if __name__ == "__main__":
    assert largest_rectangle_area([2,1,5,6,2,3]) == 10, "Test 1"
    assert largest_rectangle_area([2,4]) == 4,          "Test 2"
    assert largest_rectangle_area([2,1,2]) == 3,        "Test 3"
    print("All tests passed!")
