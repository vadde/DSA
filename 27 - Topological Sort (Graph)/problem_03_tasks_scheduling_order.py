"""
============================================================
Problem: Tasks Scheduling Order (Course Schedule II)
Pattern: Topological Sort (Graph)
Difficulty: Medium
LeetCode: #210
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Same as Course Schedule I, but now return the ACTUAL ORDER to take the courses.
If impossible (cycle), return [].

COMPLEXITY: O(V + E), Space O(V + E).
============================================================
"""

from typing import List
from collections import deque


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    adj: List[List[int]] = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1

    queue: deque[int] = deque(c for c in range(num_courses) if in_degree[c] == 0)
    result: List[int] = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == num_courses else []


if __name__ == "__main__":
    assert find_order(2, [[1, 0]]) == [0, 1], "Test 1"
    order = find_order(4, [[1,0],[2,0],[3,1],[3,2]])
    assert order.index(0) < order.index(1) < order.index(3), "Test 2 constraint"
    assert find_order(2, [[1,0],[0,1]]) == [], "Test 3: cycle"
    assert find_order(1, []) == [0],           "Edge: single course"
    print("All tests passed!")
