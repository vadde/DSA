"""
============================================================
Problem: Single Number
Pattern: Bitwise XOR
Difficulty: Easy
Link: https://leetcode.com/problems/single-number/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bag of numbers. 
Every number has an identical twin in the bag, EXCEPT for one lonely number.
For example: `[1, 4, 2, 1, 2]`.
- 1 has a twin.
- 2 has a twin.
- 4 is all alone!
We want to find the lonely number.
Normally, you'd make a list, check off the twins as you see them, and see who 
is left. But that requires extra memory (a Hash Map).
Instead, we use a magic math operator called XOR (`^`).
XOR is like a light switch. If you flip it ONCE with a number, it turns on. 
If you flip it TWICE with the exact same number, it turns off and disappears (`0`)!
If you just XOR every number in the bag together, all the twins will cancel 
each other out, and ONLY the lonely number will be left shining at the end!
`1 ^ 4 ^ 2 ^ 1 ^ 2` -> `(1 ^ 1) ^ (2 ^ 2) ^ 4` -> `0 ^ 0 ^ 4` -> `4`.

APPROACH:
---------
1. Initialize a variable `x1 = 0`. (0 XOR anything is the thing itself).
2. Loop through every number `num` in the array.
3. `x1 ^= num`.
4. Return `x1`.

COMPLEXITY:
-----------
Time:  O(N) — We loop through the array exactly once.
Space: O(1) — We only use one integer variable. No Hash Maps!

EDGE CASES:
-----------
- Edge case 1: Array has only 1 element. Loop runs once, returns that element.
============================================================
"""

from typing import List

def find_single_number(arr: List[int]) -> int:
    """
    Finds the single number in an array where every other number appears exactly twice.
    """
    x1 = 0
    for num in arr:
        x1 ^= num
    return x1

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert find_single_number([1, 4, 2, 1, 2]) == 4, "Test 1"
    assert find_single_number([7, 9, 7]) == 9, "Test 2"

    # 🔲 Edge cases
    assert find_single_number([42]) == 42, "Edge 1: Single element array"

    print("All tests passed!")
