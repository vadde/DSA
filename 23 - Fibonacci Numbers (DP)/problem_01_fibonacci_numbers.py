"""
============================================================
Problem: Fibonacci Numbers
Pattern: Fibonacci Numbers (DP)
Difficulty: Easy
============================================================
"""


def fib(n: int) -> int:
    """Returns the nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1)."""
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(10) == 55
    assert fib(20) == 6765
    print("All tests passed!")
