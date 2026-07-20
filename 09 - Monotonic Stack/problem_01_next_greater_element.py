"""
============================================================
Problem: Next Greater Element
Pattern: Monotonic Stack
Difficulty: Easy
Link: https://www.educative.io/courses/grokking-the-coding-interview/YQO90rM5v3B
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are walking down a line of people of different heights.
For every single person, you want to tell them: "Hey, the very next person who 
is TALLER than you is standing right over there!"
If no one taller is standing behind them, you tell them "-1".
Instead of each person individually looking all the way down the line (which takes 
a long time), we can just have everyone who hasn't found a taller person yet wait 
in a special "Waiting Room" (our Stack).
When a super tall person walks into the room, EVERYONE in the waiting room who is 
shorter than the tall person says "Aha! That's my Next Greater Element!" 
They write down the tall person's height and happily leave the waiting room.
Then the tall person enters the waiting room to see if anyone even taller comes 
along later!

APPROACH:
---------
1. Initialize an array `result` of the same length as the input, filled with `-1`.
2. Initialize an empty `stack`. The stack will store the **indices** of the elements 
   waiting to find a greater element.
3. Loop `for i, num in enumerate(arr)`:
   - While the stack is not empty AND `num` is GREATER than the element currently 
     at the top of the stack (`arr[stack[-1]]`):
     - A taller person arrived! 
     - Pop the index from the stack: `popped_index = stack.pop()`
     - Update the result for that person: `result[popped_index] = num`
   - Push the current person's index into the waiting room: `stack.append(i)`
4. Any indices left in the stack at the end never found a greater element, so they 
   correctly remain `-1` in the `result` array.
5. Return `result`.

COMPLEXITY:
-----------
Time:  O(N) — Every element is pushed to the stack once and popped at most once.
Space: O(N) — The stack can store all elements in the worst case (e.g., sorted descending).

EDGE CASES:
-----------
- Edge case 1: Array is sorted in descending order `[5, 4, 3]`. Stack just keeps growing, no pops happen. Result is `[-1, -1, -1]`.
- Edge case 2: Empty array. Returns `[]`.
============================================================
"""

def next_greater_element(arr: list[int]) -> list[int]:
    """
    Finds the Next Greater Element for every element in an array.
    """
    if not arr:
        return []

    result: list[int] = [-1] * len(arr)
    stack: list[int] = []  # Stores *indices*, not values!

    for i, num in enumerate(arr):
        # The 'rule' of our Monotonic Stack is perfectly decreasing.
        # If 'num' is greater, the rule is broken! Pop the smaller elements.
        while stack and num > arr[stack[-1]]:
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
    arr1 = [4, 6, 3, 2, 8, 1]
    assert next_greater_element(arr1) == [6, 8, 8, 8, -1, -1], f"Test 1 failed: {next_greater_element(arr1)}"

    arr2 = [1, 2, 3, 4, 5]
    assert next_greater_element(arr2) == [2, 3, 4, 5, -1], "Test 2 failed"
    
    # 🔲 Edge cases
    arr3 = [5, 4, 3, 2, 1]
    assert next_greater_element(arr3) == [-1, -1, -1, -1, -1], "Edge 1: Descending array"
    
    assert next_greater_element([]) == [], "Edge 2: Empty array"

    print("All tests passed!")
