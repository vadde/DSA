"""
============================================================
Problem: Largest Palindromic Number
Pattern: Greedy Algorithms
Difficulty: Medium
LeetCode: #2384
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You're given a string of digits. Arrange SOME of those digits to form the
LARGEST palindromic number possible (as a string, no leading zeros allowed
unless the result is "0").

A palindrome reads the same forwards and backwards: "9119", "8008", "5".
Strategy:
  - Pair up digits: two 9s → put one on each side
  - Pick the LARGEST pairs first (greedy!) to maximize the number
  - If any digit has an odd count, put the LARGEST such digit in the middle
  - Watch out for leading zeros!

APPROACH:
---------
1. Count frequency of each digit.
2. For digits 9 down to 0, collect pairs: take freq[d] // 2 pairs of digit d.
   Append d * (freq[d] // 2) to the LEFT half.
3. The right half = reverse of left half.
4. Find the largest digit with odd frequency → that's the middle.
5. Strip leading zeros: if left half is all zeros, the result is "0" or middle.
6. Return left_half + middle + right_half.

COMPLEXITY:
-----------
Time:  O(N) — counting digits, then O(10) = O(1) for building result
Space: O(1) — digit counts, bounded by 10 digits

EDGE CASES:
-----------
- Only zeros: "000" → result is "0"
- Single digit: return it
- All same digit: "333" → "333" (if 3 pairs + 1 middle)
============================================================
"""

from collections import Counter


def largest_palindromic(num: str) -> str:
    freq = Counter(num)
    left_half = []
    middle = ""

    # Greedy: use larger digits first to maximize the palindrome
    for digit in "9876543210":
        pairs = freq[digit] // 2
        if pairs > 0:
            left_half.append(digit * pairs)
        # Track largest digit with an odd count for the middle
        if freq[digit] % 2 == 1 and (not middle or digit > middle):
            middle = digit

    left_str = "".join(left_half)

    # Handle leading zeros: if left_half is all zeros
    if left_str and left_str[0] == "0":
        # The only meaningful result without leading zeros
        return middle if middle else "0"

    right_str = left_str[::-1]
    return left_str + middle + right_str


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert largest_palindromic("444947137") == "7449447", "Test 1"
    assert largest_palindromic("00009") == "9",           "Test 2: leading zeros"
    assert largest_palindromic("00") == "0",              "Test 3: only zeros"
    assert largest_palindromic("5") == "5",               "Edge: single digit"
    assert largest_palindromic("9") == "9",               "Edge: single 9"
    print("All tests passed!")
