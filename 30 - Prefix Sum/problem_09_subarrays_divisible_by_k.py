"""
============================================================
Problem: Subarray Sums Divisible by K
Pattern: Prefix Sum + Modular Arithmetic
Difficulty: Medium
Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Count how many contiguous chunks (subarrays) have a sum that divides evenly
by K (no remainder). For example, if K=5, sums like 0, 5, 10, -5 all work.

KEY INSIGHT: If two prefix sums have the SAME remainder when divided by K,
then the subarray between them has a sum divisible by K!
(Because prefix[j] - prefix[i] is divisible by K if they share a remainder.)

APPROACH:
---------
1. Maintain `prefix_sum` modulo K.
2. Use a hash map counting how many times each remainder has appeared.
3. At each index, add the count of previous prefix sums with the same remainder.
4. IMPORTANT: In Python, `%` on negative numbers already gives a non-negative
   remainder, which is exactly what we want.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(K) for the hash map (at most K different remainders).

EDGE CASES:
-----------
- Negative numbers in the array.
- K = 1 → every subarray sum is divisible by 1.
- Single element divisible by K.
============================================================
"""

from typing import List
from collections import defaultdict


def subarrays_div_by_k(nums: List[int], k: int) -> int:
    remainder_count = defaultdict(int)
    remainder_count[0] = 1
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k  # Python handles negatives correctly
        count += remainder_count[remainder]
        remainder_count[remainder] += 1

    return count


if __name__ == "__main__":
    assert subarrays_div_by_k([4,5,0,-2,-3,1], 5) == 7, "Test 1"
    assert subarrays_div_by_k([5], 9) == 0, "Test 2"
    assert subarrays_div_by_k([-1,2,9], 2) == 2, "Test 3: negatives"
    assert subarrays_div_by_k([1,2,3], 1) == 6, "Test 4: k=1, all subarrays"
    print("All tests passed!")
