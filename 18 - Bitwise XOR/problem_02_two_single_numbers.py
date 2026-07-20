"""
============================================================
Problem: Two Single Numbers
Pattern: Bitwise XOR
Difficulty: Medium
Link: https://leetcode.com/problems/single-number-iii/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bag of numbers. Every number has a twin, except for TWO lonely numbers!
For example: `[1, 5, 1, 9]`.
The loners are `5` and `9`.
If you do our trick from the last problem (XORing everything together), all 
the twins cancel out!
But you are left with `5 ^ 9`, which equals `12`.
How do we separate `12` back into `5` and `9`?!
Look at the binary of the XOR result (`12` is `1100`).
If a bit is `1` in the XOR result, it means that `5` and `9` have DIFFERENT 
bits at that exact position! (One of them has a 1, the other has a 0).
Let's find just ONE bit that is different. We usually pick the rightmost `1`.
For `12` (`1100`), the rightmost `1` is the 4s place (`0100`).
Now, we look at the original bag of numbers, and we divide them into TWO groups:
Group A: Numbers where the 4s place is a `1`.
Group B: Numbers where the 4s place is a `0`.
Our two loners (`5` and `9`) are guaranteed to be in DIFFERENT groups!
And all the twins are guaranteed to be in the SAME group as each other!
So now we just run the basic "Single Number" XOR trick on Group A and Group B 
separately, and we find our two loners!

APPROACH:
---------
1. XOR all numbers in the array together. Let's call the result `n1xn2`.
2. Find the rightmost set bit in `n1xn2`.
   - `rightmost_set_bit = 1`
   - `while (rightmost_set_bit & n1xn2) == 0:`
     - `rightmost_set_bit = rightmost_set_bit << 1`
3. Initialize `num1 = 0` and `num2 = 0`.
4. Loop through the array again.
   - If `(num & rightmost_set_bit) != 0`, `num` belongs to Group A. `num1 ^= num`.
   - Else, `num` belongs to Group B. `num2 ^= num`.
5. Return `[num1, num2]`.

COMPLEXITY:
-----------
Time:  O(N) — We pass through the array twice.
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: Array only has 2 elements, which must be the two single numbers.
============================================================
"""

from typing import List

def find_two_single_numbers(arr: List[int]) -> List[int]:
    """
    Finds the two numbers in an array that appear only once, while all others appear twice.
    """
    # 1. Get the XOR of the two numbers
    n1xn2 = 0
    for num in arr:
        n1xn2 ^= num
        
    # 2. Find the rightmost set bit in n1xn2
    # This bit is DIFFERENT between num1 and num2
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
        
    num1, num2 = 0, 0
    
    # 3. Partition the array into two groups based on the rightmost set bit
    # XOR each group to find the single number in it
    for num in arr:
        if (num & rightmost_set_bit) != 0:
            num1 ^= num
        else:
            num2 ^= num
            
    return [num1, num2]

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    result1 = find_two_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])
    # The two singles are 4 and 6
    assert sorted(result1) == [4, 6], f"Test 1 failed. Got {result1}"
    
    result2 = find_two_single_numbers([2, 1, 3, 2])
    # The two singles are 1 and 3
    assert sorted(result2) == [1, 3], f"Test 2 failed. Got {result2}"

    # 🔲 Edge cases
    assert sorted(find_two_single_numbers([42, 99])) == [42, 99], "Edge 1: Only two elements"

    print("All tests passed!")
