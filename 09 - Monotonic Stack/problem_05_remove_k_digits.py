"""
============================================================
Problem: Remove K Digits
Pattern: Monotonic Stack (Greedy)
Difficulty: Medium
Link: https://leetcode.com/problems/remove-k-digits/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are given a huge number like "1432219" and you are allowed to erase exactly 
K digits to make the number as small as possible.
If K = 3, which digits do you erase?
You always want smaller numbers at the front! (e.g., 100 is smaller than 900).
So we read the numbers one by one and put them in a stack.
If we see a '4' at the top of the stack, and the next number is '3', we think: 
"Wait! If I erase this 4 right now, the 3 will take its place, making the whole 
number smaller!"
So as long as we have "erasers" left (K > 0), any time a smaller number comes along, 
we POP the bigger numbers off the stack to make room for the small guy!
This naturally builds an increasing sequence (1, 2, 3...) which is the smallest 
possible number.

APPROACH:
---------
1. Initialize an empty `stack`.
2. Loop through every `digit` in the string `num`:
   - While the stack is not empty, AND `k > 0`, AND the `digit` is SMALLER than the 
     top of the stack:
     - Pop the top of the stack! We just used an "eraser".
     - `k -= 1`
   - Push the `digit` onto the stack.
3. What if we still have erasers left? (e.g. the number was already sorted like "1234").
   Then we just erase the biggest numbers, which are at the very end of our stack!
   - `stack = stack[:-k]`
4. Join the stack into a string. We might have leading zeros (like "0200"). 
   We must strip them using `.lstrip('0')`.
5. If the final string is empty, return "0". Otherwise, return the string.

COMPLEXITY:
-----------
Time:  O(N) — Each digit is pushed and popped at most once.
Space: O(N) — The stack can store up to N characters.

EDGE CASES:
-----------
- Edge case 1: String is already sorted ascending "12345", k=2. We just slice off the end -> "123".
- Edge case 2: We pop everything and get leading zeros "10200", k=1. '1' is popped for '0'. -> "0200" -> "200".
- Edge case 3: We erase everything. Return "0".
============================================================
"""

def remove_k_digits(num: str, k: int) -> str:
    """
    Returns the smallest possible integer after removing k digits from num.
    """
    if k == len(num):
        return "0"
        
    stack: list[str] = []

    for digit in num:
        # If we still have removals left, and the current digit is smaller 
        # than the last digit we kept, it's better to replace the last digit!
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
            
        stack.append(digit)

    # If we still have removals left (e.g., all digits were ascending like "12345")
    # we just chop off the largest ones at the end.
    if k > 0:
        stack = stack[:-k]

    # Join the stack and strip any leading zeros
    result = "".join(stack).lstrip('0')

    # If the result is completely empty, it means we erased everything or all zeros
    return result if result else "0"

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # 1432219 -> 1 32219 (erase 4) -> 1 2219 (erase 3) -> 12 19 (erase 2) = 1219
    assert remove_k_digits("1432219", 3) == "1219", "Test 1 failed"
    
    # 10200 -> 0200 (erase 1) -> strip leading 0 -> 200
    assert remove_k_digits("10200", 1) == "200", "Test 2 failed"
    
    # 🔲 Edge cases
    assert remove_k_digits("10", 2) == "0", "Edge 1: Erase everything"
    assert remove_k_digits("9", 1) == "0", "Edge 2: Erase single digit"
    assert remove_k_digits("1111", 2) == "11", "Edge 3: Identical digits"
    assert remove_k_digits("12345", 2) == "123", "Edge 4: Already sorted"

    print("All tests passed!")
