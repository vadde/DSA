"""
============================================================
Problem: Maximum Length of Pair Chain
Pattern: Greedy Algorithms
Difficulty: Medium
LeetCode: #646
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a set of chains/links. Each link is a pair [a, b] (a < b).
A chain can be formed by connecting links: link [c, d] can follow [a, b]
ONLY IF c > b (the second link starts AFTER the first one ends).
Find the longest chain you can make.

APPROACH: Greedy — Sort by END value
---------
This is the classic "Activity Selection" greedy problem!
Greedy choice: always pick the pair whose END value is smallest.
Why? A smaller end value leaves the most "room" for future pairs to follow.

1. Sort pairs by their second element (end value).
2. Track current_end = -infinity, chain_length = 0.
3. For each pair [a, b]:
   - If a > current_end: we can append this pair! Increment length, update current_end = b.
4. Return chain_length.

COMPLEXITY:
-----------
Time:  O(N log N) — sorting dominates
Space: O(1) — excluding sort's stack space

EDGE CASES:
-----------
- Single pair → 1
- All pairs overlap → 1 (can only pick one)
============================================================
"""

from typing import List


def find_longest_chain(pairs: List[List[int]]) -> int:
    # Sort by end value (greedy: pick smallest end first)
    pairs.sort(key=lambda p: p[1])

    chain_length = 0
    current_end = float('-inf')

    for start, end in pairs:
        if start > current_end:
            chain_length += 1
            current_end = end

    return chain_length


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert find_longest_chain([[1, 2], [2, 3], [3, 4]]) == 2, "Test 1"
    assert find_longest_chain([[1, 2], [7, 8], [4, 5]]) == 3, "Test 2"
    assert find_longest_chain([[1, 10], [2, 3], [4, 5]]) == 2, "Test 3"
    assert find_longest_chain([[1, 2]]) == 1, "Edge: single pair"
    print("All tests passed!")
