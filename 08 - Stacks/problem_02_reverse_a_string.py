"""
============================================================
Problem: Reverse a String using a Stack
Pattern: Stacks
Difficulty: Easy
Link: https://www.educative.io/courses/grokking-the-coding-interview/3j6QJ9n3V2y
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a stack of blocks with letters on them.
You have the word "CAT".
First, you put 'C' on the table.
Then, you put 'A' on top of 'C'.
Then, you put 'T' on top of 'A'.
Now you have a tower of blocks: T is on top, A is in the middle, C is at the bottom.
To take them down, you have to take the top block first.
You take off 'T' and write it down.
You take off 'A' and write it down.
You take off 'C' and write it down.
What did you write? "TAC"! 
You just reversed the word just by using the natural rules of a Stack (Last-In, First-Out).

APPROACH:
---------
1. Initialize an empty stack (Python list).
2. Loop through every character in the string, pushing it onto the stack.
3. Initialize an empty string or a list for the result.
4. While the stack is not empty, `pop` the top character and add it to the result.
5. Return the joined result string.

NOTE: In real Python code, you should just use `s[::-1]`. However, this problem 
tests your understanding of the Stack data structure.

COMPLEXITY:
-----------
Time:  O(N) — Pushing N characters takes O(N), popping N characters takes O(N).
Space: O(N) — We store all N characters in the stack.

EDGE CASES:
-----------
- Edge case 1: Empty string `""`. Returns `""`.
- Edge case 2: String with one character `"a"`. Returns `"a"`.
============================================================
"""

def reverse_string(s: str) -> str:
    """
    Reverses a string using a Stack data structure.
    """
    stack: list[str] = []

    # 1. Push all characters onto the stack
    for char in s:
        stack.append(char)

    # 2. Pop all characters off the stack
    reversed_chars: list[str] = []
    while stack:
        reversed_chars.append(stack.pop())

    # 3. Join them back into a single string
    return "".join(reversed_chars)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert reverse_string("Hello, World!") == "!dlroW ,olleH", "Test 1 failed"
    assert reverse_string("Python") == "nohtyP", "Test 2 failed"
    assert reverse_string("racecar") == "racecar", "Test 3 failed"

    # 🔲 Edge cases
    assert reverse_string("") == "", "Edge 1: Empty string"
    assert reverse_string("a") == "a", "Edge 2: Single character"

    print("All tests passed!")
