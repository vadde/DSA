"""
============================================================
Problem: Decimal to Binary Conversion
Pattern: Stacks
Difficulty: Easy
Link: https://www.educative.io/courses/grokking-the-coding-interview/3w2X2r7m5M1
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
How do you turn a normal number (like 13) into binary (0s and 1s)?
You divide by 2!
13 divided by 2 is 6, with a remainder of **1**.
6 divided by 2 is 3, with a remainder of **0**.
3 divided by 2 is 1, with a remainder of **1**.
1 divided by 2 is 0, with a remainder of **1**.
If you read the remainders exactly as they came out, you get "1, 0, 1, 1".
But wait! Binary is written backwards. The FIRST remainder you got should 
actually be the very LAST digit of your binary number!
The correct binary for 13 is "1101".
This sounds like a perfect job for a Stack! 
We push every remainder onto a Stack as we get it. Since the first remainder is 
pushed to the bottom of the stack, it will be the very LAST thing to be popped off!

APPROACH:
---------
1. Initialize an empty stack.
2. Loop `while n > 0`:
   - Calculate `remainder = n % 2`.
   - Push `str(remainder)` to the stack.
   - Update `n = n // 2` (integer division).
3. If the input was `0` to begin with, just return `"0"`.
4. Pop from the stack one by one and append to our result string.
5. Return the result string.

COMPLEXITY:
-----------
Time:  O(log N) — We divide `n` by 2 every step, which takes log(N) steps.
Space: O(log N) — The stack stores log(N) remainders.

EDGE CASES:
-----------
- Edge case 1: Input is `0`. Returns `"0"`.
============================================================
"""

def decimal_to_binary(n: int) -> str:
    """
    Converts a positive decimal integer into its binary representation string using a Stack.
    """
    if n == 0:
        return "0"

    stack: list[str] = []

    # 1. Push remainders to the stack
    while n > 0:
        remainder = n % 2
        stack.append(str(remainder))
        n = n // 2

    # 2. Pop to read them in reverse order
    binary_chars: list[str] = []
    while stack:
        binary_chars.append(stack.pop())

    return "".join(binary_chars)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert decimal_to_binary(2) == "10", "Test 1 failed"
    assert decimal_to_binary(7) == "111", "Test 2 failed"
    assert decimal_to_binary(13) == "1101", "Test 3 failed"
    assert decimal_to_binary(18) == "10010", "Test 4 failed"

    # 🔲 Edge cases
    assert decimal_to_binary(0) == "0", "Edge 1: Input is zero"
    assert decimal_to_binary(1) == "1", "Edge 2: Input is one"

    print("All tests passed!")
