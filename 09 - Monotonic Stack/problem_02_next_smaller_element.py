"""
============================================================
Problem: Next Smaller Element
Pattern: Monotonic Stack
Difficulty: Easy
Link: https://www.geeksforgeeks.org/next-smaller-element/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
This is exactly the same as the "Next Greater Element" problem, but reversed!
Instead of a very TALL person walking in and telling all the shorter people they 
can leave the waiting room...
A very SHORT person walks in! 
If you are height 10, and a person of height 3 stands behind you, you can't see 
anyone shorter than 3 ever again. That short person blocks the view of anything 
shorter down the line.
So, when a SHORT person enters the waiting room, EVERYONE in the room who is 
TALLER than them says "Aha! That's my Next Smaller Element!" 
They write down the short person's height and leave the room.

APPROACH:
---------
1. Initialize an array `result` of the same length as the input, filled with `-1`.
2. Initialize an empty `stack` (to store the indices).
3. Loop `for i, num in enumerate(arr)`:
   - While the stack is not empty AND `num` is SMALLER than the element currently 
     at the top of the stack (`arr[stack[-1]]`):
     - A shorter person arrived! 
     - Pop the index from the stack: `popped_index = stack.pop()`
     - Update the result for that person: `result[popped_index] = num`
   - Push the current person's index into the waiting room: `stack.append(i)`
4. Return `result`.

COMPLEXITY:
-----------
Time:  O(N) — Every element is pushed to the stack once and popped at most once.
Space: O(N) — The stack can store all elements in the worst case (e.g., sorted ascending).

EDGE CASES:
-----------
- Edge case 1: Array is sorted in ascending order `[1, 2, 3]`. Stack just keeps growing. Result is `[-1, -1, -1]`.
- Edge case 2: Empty array. Returns `[]`.
============================================================
"""

def next_smaller_element(arr: list[int]) -> list[int]:
    """
    Finds the Next Smaller Element for every element in an array.
    """
    if not arr:
        return []

    result: list[int] = [-1] * len(arr)
    stack: list[int] = []  # Stores *indices*, not values!

    for i, num in enumerate(arr):
        # The 'rule' of our Monotonic Stack is perfectly increasing.
        # If 'num' is smaller, the rule is broken! Pop the larger elements.
        while stack and num < arr[stack[-1]]:
            popped_index = stack.pop()
            result[popped_index] = num
            
        # Push the current index to the waiting room
        stack.append(i)

    return result

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    arr1 = [4, 8, 5, 2, 25]
    assert next_smaller_element(arr1) == [2, 5, 2, -1, -1], f"Test 1 failed: {next_smaller_element(arr1)}"

    arr2 = [13, 7, 6, 12]
    assert next_smaller_element(arr2) == [7, 6, -1, -1], "Test 2 failed"
    
    # 🔲 Edge cases
    arr3 = [1, 2, 3, 4, 5]
    assert next_smaller_element(arr3) == [-1, -1, -1, -1, -1], "Edge 1: Ascending array"
    
    assert next_smaller_element([]) == [], "Edge 2: Empty array"

    print("All tests passed!")
