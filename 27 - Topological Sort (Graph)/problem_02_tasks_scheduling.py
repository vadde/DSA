"""
============================================================
Problem: Tasks Scheduling (Course Schedule)
Pattern: Topological Sort (Graph)
Difficulty: Medium
LeetCode: #207
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have N courses. Some require prerequisites: [a, b] means "take b before a".
Can you finish ALL courses? (i.e., is there no circular dependency?)

APPROACH: Kahn's BFS Topological Sort
---------
If we can produce a valid topological ordering of all courses → True.
If a cycle exists (some courses remain in-degree > 0 at the end) → False.

COMPLEXITY: O(V + E), Space O(V + E).
============================================================
"""

from typing import List
from collections import deque


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    adj: List[List[int]] = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1

    queue: deque[int] = deque(c for c in range(num_courses) if in_degree[c] == 0)
    finished = 0

    while queue:
        node = queue.popleft()
        finished += 1
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return finished == num_courses


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True,          "Test 1"
    assert can_finish(2, [[1, 0], [0, 1]]) is False, "Test 2: cycle"
    assert can_finish(4, [[1,0],[2,0],[3,1],[3,2]]) is True, "Test 3"
    assert can_finish(1, []) is True,                "Edge: single course"
    print("All tests passed!")
