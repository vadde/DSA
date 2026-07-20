"""
============================================================
Problem: Balanced Parentheses
Pattern: Stacks
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a bunch of nested boxes. 
A square box `[` can go inside a round box `(`, which gives you `([ ])`.
But you can't close a round box if the square box inside it is still open! `([ )]` is wrong.
Every time you open a box (an opening bracket), you write it down on a notepad 
(Push it to a Stack).
Every time you want to close a box, you look at the last box you opened (Pop from the Stack).
If it's the exact same shape, great! You close it.
If it's a different shape, or if your notepad is empty (you didn't open any boxes!), 
then it's an error.

APPROACH:
---------
1. Create a `stack` (a Python list).
2. Create a mapping (dictionary) to match closing brackets to opening brackets.
   `mapping = {')': '(', '}': '{', ']': '['}`
3. Loop through every character in the string.
4. If the character is an opening bracket `({[`, push it to the stack.
5. If the character is a closing bracket `)}]`:
   - If the stack is empty, return False (trying to close something that isn't open).
   - Pop the top character from the stack.
   - Check if the popped character matches `mapping[char]`. If not, return False.
6. After the loop, if the stack is NOT empty, it means we opened boxes we never closed! 
   Return False. Otherwise, return True.

COMPLEXITY:
-----------
Time:  O(N) — Iterate through the string once. Push and pop are O(1).
Space: O(N) — Worst case (e.g., `((((((`), the stack stores every character.

EDGE CASES:
-----------
- Edge case 1: String is completely empty. Returns True.
- Edge case 2: String only has closing brackets `)))`. Stack check catches it.
- Edge case 3: String only has opening brackets `((((`. Final length check catches it.
============================================================
"""

def is_balanced(s: str) -> bool:
    """
    Checks if a string of brackets is validly balanced using a Stack.
    """
    stack: list[str] = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        # If it's a closing bracket
        if char in mapping:
            # Pop from stack if not empty, else assign a dummy character
            top_element = stack.pop() if stack else '#'
            
            # If the popped opening bracket doesn't match the required opening bracket
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it to the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched perfectly!
    return len(stack) == 0

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert is_balanced("()") == True, "Test 1 failed"
    assert is_balanced("()[]{}") == True, "Test 2 failed"
    assert is_balanced("(]") == False, "Test 3 failed"
    assert is_balanced("([)]") == False, "Test 4 failed"
    assert is_balanced("{[]}") == True, "Test 5 failed"

    # 🔲 Edge cases
    assert is_balanced("") == True, "Edge 1: Empty string"
    assert is_balanced("(((") == False, "Edge 2: Only opening brackets"
    assert is_balanced("]]]") == False, "Edge 3: Only closing brackets"

    print("All tests passed!")
