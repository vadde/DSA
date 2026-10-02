"""
Silicon-Level Bit Manipulation Algorithms Library.

This module provides reference implementations of core bitwise techniques:
1. Brian Kernighan's set-bit counting (Hamming Weight)
2. Single Number (XOR cancellation)
3. Two Single Numbers (differing bit partition)
4. Submask Enumeration in O(3^N)
5. Power-of-2 verification
"""

from typing import Iterator, List, Tuple


def count_set_bits(n: int) -> int:
    """Counts set bits using Brian Kernighan's algorithm.

    Complexity: O(K) where K is number of set bits (skips zero bits entirely).
    """
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count


def is_power_of_two(n: int) -> bool:
    """Determines whether n is a positive power of 2 in O(1) time."""
    return n > 0 and (n & (n - 1)) == 0


def single_number(nums: List[int]) -> int:
    """Finds the single unique number where all others appear twice.

    Complexity: O(N) time, O(1) space.
    """
    unique = 0
    for x in nums:
        unique ^= x
    return unique


def two_single_numbers(nums: List[int]) -> Tuple[int, int]:
    """Finds the two unique numbers where all others appear twice.

    Complexity: O(N) time, O(1) space.
    """
    xor_all = 0
    for x in nums:
        xor_all ^= x

    # Isolate lowest set bit where a and b differ
    diff_bit = xor_all & (-xor_all)

    a = b = 0
    for x in nums:
        if x & diff_bit:
            a ^= x
        else:
            b ^= x

    return (min(a, b), max(a, b))


def enumerate_submasks(mask: int) -> List[int]:
    """Enumerates all submasks of a mask in descending order."""
    submasks: List[int] = []
    sub = mask
    while sub > 0:
        submasks.append(sub)
        sub = (sub - 1) & mask
    submasks.append(0)
    return submasks


def test_bit_manipulation() -> None:
    """Unit tests verifying bit manipulation functions."""
    # 1. Brian Kernighan count set bits
    assert count_set_bits(0) == 0
    assert count_set_bits(1) == 1
    assert count_set_bits(7) == 3   # 0b111
    assert count_set_bits(16) == 1  # 0b10000
    assert count_set_bits(255) == 8 # 0b11111111

    # 2. Power of two check
    assert is_power_of_two(1) is True
    assert is_power_of_two(2) is True
    assert is_power_of_two(16) is True
    assert is_power_of_two(18) is False
    assert is_power_of_two(0) is False
    assert is_power_of_two(-8) is False

    # 3. Single Number
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([2, 2, 1]) == 1

    # 4. Two Single Numbers
    assert two_single_numbers([1, 2, 1, 3, 2, 5]) == (3, 5)
    assert two_single_numbers([-1, 0]) == (-1, 0)

    # 5. Submask enumeration
    # mask = 0b101 = 5. Submasks: 5 (101), 4 (100), 1 (001), 0 (000)
    assert enumerate_submasks(5) == [5, 4, 1, 0]

    print("✅ All Bit Manipulation tests passed successfully!")


if __name__ == "__main__":
    test_bit_manipulation()
