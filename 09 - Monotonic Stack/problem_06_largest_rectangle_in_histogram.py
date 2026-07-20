"""
============================================================
Problem: Largest Rectangle in Histogram
Pattern: Monotonic Stack
Difficulty: Hard
Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you built a city skyline using LEGO blocks, all lined up in a row.
You want to paint the absolute largest solid rectangle possible across these buildings.
If you pick a short building, you can paint a very wide rectangle across all the 
taller buildings next to it! But it will be short.
If you pick a very tall building, the rectangle will be tall, but probably very skinny, 
because the next building might be shorter and block it.
How do we find the biggest one?
We use a Monotonic INCREASING Stack! 
We push buildings onto our stack as long as they keep getting taller.
But the moment a SHORT building appears, it ruins the streak! 
It tells the tall buildings on the stack: "You can't stretch any further to the right!"
So, we pop the tall buildings one by one, and for each one, we calculate:
"Okay, how tall are you? And how far to the LEFT did you stretch before you hit 
another short building?" (The answer is whatever is underneath it on the stack!).
We multiply Height * Width, and keep track of the biggest rectangle we find.

APPROACH:
---------
1. Initialize `max_area = 0`.
2. Initialize an empty `stack` to store indices of the buildings.
3. **Trick**: Add a `0` height building to the very end of the array. This acts as 
   a tiny "janitor" building that forces the stack to pop and calculate the area 
   for ALL remaining buildings at the very end.
4. Loop through `for i, h in enumerate(heights)`:
   - While the stack is not empty AND the current building `h` is SHORTER than 
     the building at the top of the stack:
     - The top building is trapped! Let's calculate its area.
     - `height = heights[stack.pop()]`
     - How wide can it stretch? 
       - It stretches to the right up to index `i` (exclusive).
       - It stretches to the left down to the new top of the stack (exclusive).
       - `width = i if not stack else i - stack[-1] - 1`
     - `max_area = max(max_area, height * width)`
   - Push the current index `i` onto the stack.
5. (Optional) Remove the `0` from the end of the array to clean up.
6. Return `max_area`.

COMPLEXITY:
-----------
Time:  O(N) — Every building is pushed and popped exactly once.
Space: O(N) — The stack can grow up to size N.

EDGE CASES:
-----------
- Edge case 1: All buildings same height `[2, 2, 2]`. Area = 2 * 3 = 6.
- Edge case 2: Empty array. Returns 0.
- Edge case 3: Single building `[5]`. Area = 5.
============================================================
"""

def largest_rectangle_area(heights: list[int]) -> int:
    """
    Finds the largest rectangular area possible in a histogram.
    """
    if not heights:
        return 0

    max_area = 0
    stack: list[int] = []
    
    # Append a 0 to act as a trigger to flush the stack at the end
    heights.append(0)

    for i, h in enumerate(heights):
        # A shorter building forces us to calculate the area for taller buildings
        while stack and h < heights[stack[-1]]:
            # 1. Get the height of the trapped building
            height = heights[stack.pop()]
            
            # 2. Calculate the width
            # If stack is empty, it means this building was the shortest so far, 
            # so it stretches all the way from index 0 to i.
            if not stack:
                width = i
            else:
                # It stretches from the building just to its left (the new stack top) up to i.
                width = i - stack[-1] - 1
                
            # 3. Update max area
            max_area = max(max_area, height * width)
            
        stack.append(i)

    # Clean up the array by removing the dummy 0
    heights.pop()

    return max_area

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10, "Test 1 failed"  # 5 and 6 give 5*2 = 10
    assert largest_rectangle_area([2, 4]) == 4, "Test 2 failed"
    
    # 🔲 Edge cases
    assert largest_rectangle_area([2, 2, 2, 2]) == 8, "Edge 1: Flat histogram"
    assert largest_rectangle_area([5]) == 5, "Edge 2: Single bar"
    assert largest_rectangle_area([]) == 0, "Edge 3: Empty"
    
    # Ascending array (flushed by the 0 at the end)
    assert largest_rectangle_area([1, 2, 3, 4, 5]) == 9, "Edge 4: Ascending (3*3)"

    print("All tests passed!")
