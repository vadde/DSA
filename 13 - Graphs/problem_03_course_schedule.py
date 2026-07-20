"""
============================================================
Problem: Course Schedule (Cycle Detection)
Pattern: Graphs / Topological Sort
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are in college and you want to graduate. 
But to take "Advanced Math" (Course A), you first have to pass "Basic Math" (Course B).
This is a dependency. We can draw this as a one-way road: B -> A.
What if a computer glitch makes "Basic Math" require "Algebra", and "Algebra" 
requires "Advanced Math"?
Then you have: Algebra -> Advanced Math -> Basic Math -> Algebra...
This is a CYCLE! You can never graduate because you are stuck in an infinite loop 
of prerequisites.
To find out if you can graduate, we need to check if there are any cycles.
We explore the map. As we walk down a path of courses, we carry a "Current Path" notebook.
If we ever step on a course that is ALREADY in our "Current Path" notebook, we found 
a cycle! You can't graduate.
When we hit a dead end (a course with no more prerequisites) and step backwards, 
we ERASE the course from our "Current Path" notebook, and instead write it in our 
"Fully Finished" notebook.
If we see a course that is already in our "Fully Finished" notebook, we don't 
need to check it again.

APPROACH:
---------
1. Build an Adjacency List `graph`. For `[course_a, pre_b]`, add `course_a` to 
   `graph[pre_b]`. (Arrow goes from Prerequisite -> Course).
2. Initialize two sets:
   - `visited`: The "Fully Finished" notebook. Courses we know for a fact don't lead to a cycle.
   - `path_visited`: The "Current Path" notebook. Courses we are actively exploring RIGHT NOW.
3. Define `dfs(course)`:
   - If `course` is in `path_visited`, we found a CYCLE! Return `False`.
   - If `course` is in `visited`, we already verified it's safe. Return `True`.
   - Add `course` to BOTH `path_visited` and `visited`.
   - Loop through all `neighbors` (courses that require this one). If `dfs(neighbor)` 
     returns False, return `False`.
   - BACKTRACK: Remove `course` from `path_visited` because we are stepping backward.
   - Return `True`.
4. Loop through every course from 0 to `numCourses - 1` and call `dfs`. If any 
   return False, return `False`.
5. Return `True`.

COMPLEXITY:
-----------
Time:  O(V + E) — We process every course and every prerequisite exactly once.
Space: O(V + E) — We store the graph, and the sets can hold up to V courses.

EDGE CASES:
-----------
- Edge case 1: No prerequisites. You can take all courses! Returns `True`.
- Edge case 2: Disconnected components (e.g. 2 separate majors). The outer loop handles this.
============================================================
"""

from typing import List

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Returns True if it is possible to finish all courses (i.e., no cycles).
    """
    # 1. Build the graph (Adjacency List)
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 2. State trackers
    visited = set()       # Courses completely verified to have no cycles
    path_visited = set()  # Courses currently in our recursive path

    # 3. Cycle Detection DFS
    def dfs(course: int) -> bool:
        if course in path_visited:
            # We found a back-edge (a cycle)!
            return False
        if course in visited:
            # We already fully explored this branch and it's safe
            return True

        # Mark as being actively explored
        path_visited.add(course)
        visited.add(course)

        # Explore all courses that depend on this one
        for next_course in graph[course]:
            if not dfs(next_course):
                return False

        # Backtrack: We are leaving this course, so remove it from the CURRENT path
        path_visited.remove(course)
        
        return True

    # 4. Check every course (to handle disconnected components)
    for i in range(num_courses):
        if not dfs(i):
            return False

    return True

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # 0 requires 1 (1 -> 0)
    assert can_finish(2, [[0, 1]]) == True, "Test 1 failed"

    # 1 requires 0, and 0 requires 1. (Cycle!)
    assert can_finish(2, [[1, 0], [0, 1]]) == False, "Test 2 failed"
    
    # 0 -> 1 -> 2 -> 3
    # \--------------^
    # No cycle, just multiple paths to 3.
    prereqs = [[1, 0], [2, 1], [3, 2], [3, 0]]
    assert can_finish(4, prereqs) == True, "Test 3 failed"
    
    # 0 -> 1 -> 2 -> 0 (Cycle!)
    prereqs_cycle = [[1, 0], [2, 1], [0, 2]]
    assert can_finish(3, prereqs_cycle) == False, "Test 4 failed"

    # 🔲 Edge cases
    assert can_finish(5, []) == True, "Edge 1: No prereqs"

    print("All tests passed!")
