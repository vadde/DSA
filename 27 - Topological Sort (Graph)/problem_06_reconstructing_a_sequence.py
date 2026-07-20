"""
============================================================
Problem: Reconstructing a Sequence
Pattern: Topological Sort (Graph)
Difficulty: Hard
LeetCode: #444
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given a sequence `org` and a list of subsequences `seqs`, determine if `org`
is the ONLY shortest supersequence that can be reconstructed from `seqs`.
In other words: is the topological ordering from `seqs` UNIQUE AND equal to `org`?

APPROACH: Kahn's with uniqueness check
---------
Build a graph from `seqs`. At each step in Kahn's BFS, check:
- The queue must have EXACTLY 1 node (otherwise multiple valid orderings exist).
- The node must match org[idx].

COMPLEXITY: O(V + E).
============================================================
"""

from typing import List
from collections import deque, defaultdict


def sequence_reconstruction(org: List[int], seqs: List[List[int]]) -> bool:
    if not seqs:
        return False

    all_nums: set[int] = set()
    for seq in seqs:
        for n in seq:
            all_nums.add(n)

    if set(org) != all_nums:
        return False

    adj: dict[int, List[int]] = defaultdict(list)
    in_degree: dict[int, int] = {n: 0 for n in all_nums}

    for seq in seqs:
        for i in range(len(seq) - 1):
            u, v = seq[i], seq[i + 1]
            adj[u].append(v)
            in_degree[v] += 1

    queue: deque[int] = deque(n for n in in_degree if in_degree[n] == 0)
    idx = 0

    while queue:
        if len(queue) > 1:
            return False  # Multiple options → ordering not unique
        node = queue.popleft()
        if idx >= len(org) or org[idx] != node:
            return False
        idx += 1
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return idx == len(org)


if __name__ == "__main__":
    assert sequence_reconstruction([1,2,3], [[1,2],[1,3],[2,3]]) is True,  "Test 1"
    assert sequence_reconstruction([1,2,3], [[1,2]]) is False,             "Test 2: incomplete"
    assert sequence_reconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]]) is True, "Test 3"
    assert sequence_reconstruction([1], [[1],[1]]) is True,                "Edge: single element"
    print("All tests passed!")
