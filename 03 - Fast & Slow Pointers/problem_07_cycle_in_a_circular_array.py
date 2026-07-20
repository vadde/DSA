"""
============================================================
Problem: Cycle in a Circular Array
Pattern: Fast & Slow Pointers
Difficulty: Hard
Link: https://leetcode.com/problems/circular-array-loop/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a board game where the spaces are arranged in a circle. Each space has a 
number on it. If you land on a space with a "3", you jump forward 3 spaces. If 
you land on "-2", you jump backward 2 spaces. 
Because it's a circle, jumping off the end just wraps you around to the beginning.
We want to know if there is an INFINITE LOOP in this board game!
BUT, there are two rules for a valid loop:
1. The loop must involve AT LEAST two spaces. (Jumping from space 4 back to space 4 doesn't count).
2. The loop must only go in ONE DIRECTION. You can't jump forward, then backward, 
   then forward again to make a loop. That's just bouncing back and forth.

To solve this, we can pretend every space is the start of a LinkedList and use 
our Fast & Slow Pointers. If the Tortoise and Hare ever meet, we found a loop!
If they hit a wall (e.g., changing directions or a 1-element loop), they stop, 
and we just start over from the next space.

APPROACH:
---------
1. Loop through each index `i` in the array.
2. For each index, initialize `slow = i` and `fast = i`.
3. Check if the movement starting from `i` is forward (`arr[i] > 0`).
4. Create a helper `get_next_index(arr, is_forward, current_index)`:
   - It calculates the next index with wrapping: `(current_index + arr[current_index]) % len(arr)`.
   - If the new direction is different from `is_forward`, return -1.
   - If the new index is the SAME as the `current_index` (1-element loop), return -1.
5. While `True`:
   - `slow = get_next_index(arr, is_forward, slow)`
   - `fast = get_next_index(arr, is_forward, fast)`
   - `if fast != -1: fast = get_next_index(arr, is_forward, fast)`
   - If either becomes -1, there's no valid cycle starting here. Break.
   - If `slow == fast`, a valid cycle is found! Return `True`.
6. If the outer loop finishes testing all indices, return `False`.

COMPLEXITY:
-----------
Time:  O(N^2) worst case — If we test every node and it takes O(N) to fail. (Optimizable to O(N) by marking visited nodes).
Space: O(1) — No extra memory is used.

EDGE CASES:
-----------
- Edge case 1: Single element loops. Helper correctly flags as -1.
- Edge case 2: Alternating directions (e.g. `[1, -1]`). Helper flags as -1.
============================================================
"""

def get_next_index(arr: list[int], is_forward: bool, current_index: int) -> int:
    """
    Helper function to find the next index based on the jump value.
    Returns -1 if the direction changes or if it's a 1-element loop.
    """
    direction = arr[current_index] >= 0
    
    # If the direction changes, it's not a valid cycle
    if is_forward != direction:
        return -1

    # Calculate next index with wrap-around
    next_index = (current_index + arr[current_index]) % len(arr)

    # 1-element loops are not valid
    if next_index == current_index:
        return -1

    return next_index


def circular_array_loop_exists(arr: list[int]) -> bool:
    """
    Determines if there is a valid cycle in the circular array.
    """
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow = i
        fast = i

        # If we hit an invalid condition, get_next_index returns -1
        while True:
            # Move slow 1 step
            slow = get_next_index(arr, is_forward, slow)
            # Move fast 1 step
            fast = get_next_index(arr, is_forward, fast)
            # Move fast another step if it didn't already fail
            if fast != -1:
                fast = get_next_index(arr, is_forward, fast)

            # If either hit a wall (direction change or 1-element loop)
            if slow == -1 or fast == -1:
                break

            # If they meet, we found a valid cycle!
            if slow == fast:
                return True

    return False

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert circular_array_loop_exists([1, 2, -1, 2, 2]) == True, "Test 1 failed: [1, 2, 2]"
    assert circular_array_loop_exists([2, 2, -1, 2]) == True, "Test 2 failed"
    
    # 🔲 Edge cases
    assert circular_array_loop_exists([2, 1, -1, -2]) == False, "Edge 1: Direction changes (bouncing)"
    assert circular_array_loop_exists([1, -2]) == False, "Edge 2: Only 1-element forward or backward"

    print("All tests passed!")
