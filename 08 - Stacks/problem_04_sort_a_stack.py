"""
============================================================
Problem: Sort a Stack
Pattern: Stacks
Difficulty: Medium
Link: https://www.educative.io/courses/grokking-the-coding-interview/3wE58G2n70q
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a stack of heavy boxes with numbers on them, and they are all out of order.
You want to sort them so the smallest number is at the top, and the biggest number 
is at the bottom.
But you only have ONE empty space next to you (a temporary stack) to help you sort.
Here is the trick:
1. You take the top box off the main stack and hold it in your hands.
2. You look at the temporary stack. Is the top box there BIGGER than the one in your hands?
   If it is, you can't put your box down! You have to move the bigger box back to the 
   main stack for a second, to make room.
3. You keep moving boxes back until you find the perfect spot in the temporary stack.
4. Then you put your box down on the temporary stack.
5. You repeat this until the main stack is empty. Now the temporary stack has all the 
   boxes sorted (with the biggest at the top). 
   Wait, if we want the smallest at the top, we just pour the temporary stack back 
   into the main stack!

APPROACH:
---------
1. Initialize `temp_stack = []`.
2. Loop while `stack` is not empty:
   - Pop the top element and store it in `temp` (hold it in your hands).
   - While `temp_stack` is not empty AND `temp_stack[-1] > temp`:
     - We can't put `temp` down yet. Pop from `temp_stack` and push it back to `stack`.
   - Now it's safe to push `temp` onto `temp_stack`.
3. After the loop, `temp_stack` is sorted with the largest element at the top.
4. To return a stack with the smallest element at the top, we pop everything from 
   `temp_stack` and push it back into `stack`.
5. Return the original `stack`.

COMPLEXITY:
-----------
Time:  O(N^2) — In the worst case (reverse sorted), we have to move elements back and forth many times.
Space: O(N) — We use one additional stack of size N.

EDGE CASES:
-----------
- Edge case 1: Stack is already sorted. Inner while loop never runs. O(N) time.
- Edge case 2: Empty stack. Handled safely.
============================================================
"""

def sort_stack(stack: list[int]) -> list[int]:
    """
    Sorts a stack such that the smallest elements are on top, 
    using only one additional stack.
    """
    temp_stack: list[int] = []

    while stack:
        # 1. Take the top element
        temp = stack.pop()
        
        # 2. While the temporary stack has larger elements on top, 
        # move them back to the main stack to make room for 'temp'.
        while temp_stack and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())
            
        # 3. Now the top of temp_stack is smaller than or equal to temp, so it's safe to place it.
        temp_stack.append(temp)

    # 4. temp_stack now has the largest elements at the top. 
    # Pour them back into the original stack so the smallest end up on top!
    while temp_stack:
        stack.append(temp_stack.pop())

    return stack

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    stack1 = [34, 3, 31, 98, 92, 23]
    # Expected output (smallest on top): [98, 92, 34, 31, 23, 3] 
    # Wait! Python lists have the 'top' at the END (index -1). 
    # So if smallest is on top, the list should look like [biggest, ..., smallest].
    # So [98, 92, 34, 31, 23, 3] is correct.
    res1 = sort_stack(stack1)
    assert res1 == [98, 92, 34, 31, 23, 3], f"Test 1 failed: {res1}"

    stack2 = [3, 5, 1, 4, 2, 8]
    res2 = sort_stack(stack2)
    assert res2 == [8, 5, 4, 3, 2, 1], f"Test 2 failed: {res2}"

    # 🔲 Edge cases
    assert sort_stack([]) == [], "Edge 1: Empty stack"
    assert sort_stack([1]) == [1], "Edge 2: Single element"

    print("All tests passed!")
