"""
============================================================
Problem: XOR Queries of a Subarray
Pattern: MO's Algorithm / Prefix XOR
Difficulty: Medium
Link: https://leetcode.com/problems/xor-queries-of-a-subarray/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array, answer multiple queries of the form: "What is the XOR of all
elements from index L to index R?" XOR is like a toggle switch — it flips
bits. The key property: A XOR A = 0, and A XOR 0 = A.

APPROACH: Prefix XOR (O(1) per query)
---------
While MO's Algorithm works, this specific problem has a much simpler O(1) per
query solution using Prefix XOR (similar to Prefix Sum but with XOR).
1. Build prefix_xor[i] = arr[0] XOR arr[1] XOR ... XOR arr[i-1].
2. XOR of range [L, R] = prefix_xor[R+1] XOR prefix_xor[L].
   (Because XOR-ing the same prefix cancels out!)

COMPLEXITY:
-----------
Time:  O(N + Q) — O(N) to build prefix, O(1) per query.
Space: O(N) for prefix array.

EDGE CASES:
-----------
- Single element query (L == R) → just return arr[L].
- Entire array.
============================================================
"""

from typing import List


def xor_queries(arr: List[int], queries: List[List[int]]) -> List[int]:
    n = len(arr)
    prefix_xor = [0] * (n + 1)

    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

    result = []
    for l, r in queries:
        result.append(prefix_xor[r + 1] ^ prefix_xor[l])

    return result


if __name__ == "__main__":
    assert xor_queries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]) == [2,7,14,8], "Test 1"
    assert xor_queries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]) == [8,0,4,4], "Test 2"
    assert xor_queries([5], [[0,0]]) == [5], "Test 3: single"
    print("All tests passed!")
