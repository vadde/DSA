# 🚶‍♂️ Walkthrough: Course Schedule

## 👶 Explain Like I'm 5
You are in college and you want to graduate. 
But to take "Advanced Math" (Course A), you first have to pass "Basic Math" (Course B).
This is a dependency. We can draw this as a one-way road: `B -> A`.
What if a computer glitch makes "Basic Math" require "Algebra", and "Algebra" requires "Advanced Math"?
Then you have: `Algebra -> Advanced Math -> Basic Math -> Algebra...`
This is a **CYCLE**! You can never graduate because you are stuck in an infinite loop of prerequisites.

To find out if you can graduate, we explore the map. As we walk down a path of courses, we carry a "Current Path" notebook.
If we ever step on a course that is ALREADY in our "Current Path" notebook, we found a cycle! You can't graduate.
When we hit a dead end (a course with no more prerequisites) and step backwards, we ERASE the course from our "Current Path" notebook, and instead write it in our "Fully Finished" notebook.
If we see a course that is already in our "Fully Finished" notebook, we don't need to check it again.

## 🎯 Core Strategy
This is a classic **Topological Sort** or **Cycle Detection** problem in a Directed Graph using **Depth First Search (DFS)**. 

1. **Build the Graph**: Convert the array of edges into an Adjacency List. We map `prereq -> course`.
2. **State Trackers**: 
   - `visited`: Global set of nodes that have been fully processed and are guaranteed NOT to be part of a cycle.
   - `path_visited`: Local set representing the *current* DFS path. If we hit a node already in here, we have a back-edge (a cycle).
3. **Recursive DFS**: 
   - Base cases: If `course` is in `path_visited`, return `False` (Cycle!). If `course` is in `visited`, return `True` (Safe).
   - Add `course` to BOTH `path_visited` and `visited`.
   - Recurse on all `neighbors` (courses that depend on this one).
   - **Backtrack**: Remove `course` from `path_visited` before returning `True`.
4. **Outer Loop**: Loop through every single course `0` to `numCourses - 1`. If `dfs(course)` returns `False`, return `False`.
5. Return `True`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Example Prereqs**: `[[1, 0], [2, 1], [0, 2]]` 
- Course 1 requires 0 (`0 -> 1`)
- Course 2 requires 1 (`1 -> 2`)
- Course 0 requires 2 (`2 -> 0`)
**Graph**: `0: [1], 1: [2], 2: [0]`

### Execution
1. **Outer Loop**: Start at Course 0. `dfs(0)`.
2. **At 0**: 
   - Not in `path_visited` or `visited`.
   - Add 0 to both. `path_visited = {0}`, `visited = {0}`.
   - Check neighbors: `[1]`.
   - Call `dfs(1)`.
3. **At 1**:
   - Not in `path_visited` or `visited`.
   - Add 1 to both. `path_visited = {0, 1}`, `visited = {0, 1}`.
   - Check neighbors: `[2]`.
   - Call `dfs(2)`.
4. **At 2**:
   - Not in `path_visited` or `visited`.
   - Add 2 to both. `path_visited = {0, 1, 2}`, `visited = {0, 1, 2}`.
   - Check neighbors: `[0]`.
   - Call `dfs(0)`.
5. **At 0 (Again)**:
   - Is 0 in `path_visited`? **YES!** It's `{0, 1, 2}`.
   - We just found a path that goes `0 -> 1 -> 2 -> 0`. This is a cycle.
   - **Return `False`**.
6. `dfs(2)` returns `False`. `dfs(1)` returns `False`. `dfs(0)` returns `False`.
7. Outer loop receives `False` and returns `False`. You cannot finish the courses!

## 📊 Visual Diagram
Here is how the two sets differentiate between a "Safe Cross-Edge" and a "Dangerous Back-Edge" (Cycle):

```mermaid
flowchart TD
    subgraph Safe Graph (No Cycle)
        A["Course 0\npath_visited: {0}"] --> B["Course 1\npath_visited: {0, 1}"]
        A --> C["Course 2\npath_visited: {0, 2}"]
        B --> D["Course 3\npath_visited: {0, 1, 3}"]
        C --> D
        note1["dfs(1) reaches 3 and finishes.\n3 is removed from path_visited.\n3 is in visited."]
        note2["dfs(2) reaches 3.\n3 is in visited, NOT in path_visited.\nSAFE! Returns True!"]
    end
```

## 🛑 Edge Cases & Complexity

### Complexity
- **Time Complexity:** $O(V + E)$ where $V$ is the number of courses (vertices) and $E$ is the number of prerequisites (edges). We visit every node exactly once because of the `visited` set.
- **Space Complexity:** $O(V + E)$ to store the adjacency list graph. The recursion stack and sets take up to $O(V)$ space.

### Edge Cases Handled Safely
- **Disconnected Graphs:** The outer `for i in range(num_courses):` loop ensures that even if you have two completely separate majors with their own prerequisites, all courses are checked.
- **No Prerequisites:** The graph builds with empty arrays. `dfs()` loops over empty arrays, instantly returns `True`, and the outer loop verifies all courses in $O(N)$ time.
- **Multiple paths to same course:** E.g., 1 requires 0, 2 requires 0, 3 requires both 1 and 2. Node 3 will be checked by path `0->1->3`. When path `0->2->3` hits it, it checks the `visited` set, sees it's already cleared, and skips it!
