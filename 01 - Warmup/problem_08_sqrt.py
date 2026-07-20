"""
============================================================
Problem: Sqrt (Integer Floor Square Root)
Pattern: Warmup
Difficulty: Medium
LeetCode: #69
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
What is the square root of 8? It's roughly 2.828...
But we want just the INTEGER part: 2.
Think of it like: "What is the biggest whole number that, when you square it,
doesn't exceed 8?" The answer is 2, because 2*2=4 <= 8 but 3*3=9 > 8.

APPROACH: Binary Search on the Answer
---------
We don't compute sqrt(n) directly — we SEARCH for the answer.
1. lo = 0, hi = n
2. mid = (lo + hi) // 2
3. If mid*mid == n: answer is mid.
4. If mid*mid < n: answer is at least mid, so lo = mid + 1.
5. If mid*mid > n: answer is less than mid, so hi = mid - 1.
6. When lo > hi, the answer is hi (the last valid floor value).

Why hi at the end? Because hi is the last value where mid*mid <= n.

COMPLEXITY:
-----------
Time:  O(log N)
Space: O(1)

EDGE CASES:
-----------
- n = 0 → 0 (sqrt(0) = 0)
- n = 1 → 1 (sqrt(1) = 1)
- n = 4 → 2 (perfect square)
- n = 2147483647 (max int32) → 46340 (no overflow in Python)
============================================================
"""


def my_sqrt(n: int) -> int:
    if n < 2:
        return n
    lo, hi = 1, n // 2  # sqrt(n) <= n//2 for n >= 4
    while lo <= hi:
        mid = (lo + hi) // 2
        sq = mid * mid
        if sq == n:
            return mid
        elif sq < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi  # floor of sqrt


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert my_sqrt(0) == 0,          "Edge: 0"
    assert my_sqrt(1) == 1,          "Edge: 1"
    assert my_sqrt(4) == 2,          "Test 1: perfect square"
    assert my_sqrt(8) == 2,          "Test 2: floor(sqrt(8))=2"
    assert my_sqrt(9) == 3,          "Test 3: perfect square"
    assert my_sqrt(2147483647) == 46340, "Test 4: large input"
    assert my_sqrt(100) == 10,       "Test 5: 10*10=100"
    assert my_sqrt(99) == 9,         "Test 6: floor(sqrt(99))=9"
    print("All tests passed!")
