"""
============================================================
Problem: Complement of Base 10 Number
Pattern: Bitwise XOR
Difficulty: Medium
Link: https://leetcode.com/problems/complement-of-base-10-integer/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are given a number, like `8`.
In binary (computer talk), `8` is written as `1000`.
To find the "complement", you just flip all the `0`s to `1`s and `1`s to `0`s!
So `1000` becomes `0111`. (Which is `7` in normal numbers).
You might think: "I'll just use the `~` (NOT) operator in Python! `~8`!"
But wait! Python numbers are weird. They don't have a fixed size.
If you type `~8` in Python, you get `-9`! That's not what we want.
Instead, we can use XOR (`^`).
If you XOR a bit with `1`, it flips! (`1 ^ 1 = 0`, and `0 ^ 1 = 1`).
So we just need to create a mask of all `1`s that is exactly the same length 
as our number.
For `1000` (length 4), we need a mask of `1111`.
How do we make `1111`?
We take `1`, shift it left 4 times (`10000`), and subtract 1!
`10000 - 1 = 1111`.
Then we just do `1000 ^ 1111`, and we get our flipped number!

APPROACH:
---------
1. Edge case: If `num == 0`, its binary is `"0"`, its complement is `"1"`. Return `1`.
2. Count how many bits are in `num`.
   - `bit_count = 0`, `n = num`
   - Loop while `n > 0`: `bit_count += 1`, `n = n >> 1` (shift right).
3. Create the mask of all 1s.
   - `all_bits_set = (1 << bit_count) - 1`
4. Return `num ^ all_bits_set`.

COMPLEXITY:
-----------
Time:  O(b) — Where 'b' is the number of bits in the integer. Since integers are 
       typically 32 or 64 bits, this is effectively O(1).
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: `num == 0`. Loop wouldn't run, mask would be 0, result would be 0. 
  But the complement of `0` is `1`. We must handle this explicitly.
============================================================
"""

def bitwise_complement(num: int) -> int:
    """
    Returns the complement of a base-10 integer.
    """
    # 1. Edge case for 0
    if num == 0:
        return 1
        
    # 2. Count the number of bits
    bit_count = 0
    n = num
    while n > 0:
        bit_count += 1
        n = n >> 1
        
    # 3. Create a mask of all 1s that is exactly 'bit_count' long
    # e.g., if bit_count is 3, 1 << 3 is 8 (1000). 8 - 1 is 7 (111).
    all_bits_set = (1 << bit_count) - 1
    
    # 4. XOR with the mask to flip all bits
    return num ^ all_bits_set

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # 8 is 1000. Complement is 0111, which is 7.
    assert bitwise_complement(8) == 7, "Test 1"
    
    # 10 is 1010. Complement is 0101, which is 5.
    assert bitwise_complement(10) == 5, "Test 2"

    # 🔲 Edge cases
    assert bitwise_complement(0) == 1, "Edge 1: Zero"

    print("All tests passed!")
